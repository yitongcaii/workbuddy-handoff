# -*- coding: utf-8 -*-
"""生成本周知识采集周报 (2026-08-17 ~ 2026-08-21)。"""
import os, re, json, collections
from urllib.parse import urlparse
from html.parser import HTMLParser

DIR = os.path.dirname(os.path.abspath(__file__))
KC = DIR
DIRS = ['staff-meeting','offsite','icebreaker','award','openday','afternoontea']
NAMES = {'staff-meeting':'员工大会','offsite':'Offsite 团建务虚','icebreaker':'破冰',
         'award':'颁奖','openday':'Open Day 开放日','afternoontea':'下午茶研讨'}

TENCENT={'qq.com','tencent.com','woa.com','km.woa.com','lexiangla.com','qq.com.cn'}
AGG={'toutiao.com','bytedance.com'}
NEWS={'sohu.com','sina.com.cn','163.com','ifeng.com','people.com.cn','xinhuanet.com','chinanews.com.cn','thepaper.cn','yicai.com','cctv.com'}
DOC={'renrendoc.com','qg68.cn','doc88.com','wenku.baidu.com','book118.com','originaldown.cn','max.book118.com'}
WX={'mp.weixin.qq.com','weixin.qq.com'}
HR={'ihr360.com','shangyexinzhi.com','hrtxt.com','sanmao.cn','hroot.com'}
OV={'linkedin.com','medium.com','blogspot.com','wordpress.com','inc.com','substack.com'}
def src_cat(host):
    h=host.lower().replace('www.','').replace('m.','')
    if any(t in h for t in TENCENT): return '腾讯系（KM/乐享/腾讯新闻）'
    if any(t in h for t in AGG): return '头条/资讯聚合'
    if any(t in h for t in NEWS) or (h.endswith('.cn') and ('news' in h or 'rb' in h or 'daily' in h)): return '新闻门户'
    if any(t in h for t in DOC): return '文档文库（转载）'
    if any(t in h for t in WX): return '微信公众号'
    if any(t in h for t in HR): return 'HR专业媒体'
    if any(t in h for t in OV): return '海外媒体/博客（英文）'
    if h.endswith('.edu') or h.endswith('.gov') or 'edu.' in h: return '学术/官方报告'
    if h.endswith('.org'): return '机构/非营利'
    return '企业官网/SOP'

class P(HTMLParser):
    def __init__(s): super().__init__(); s.hldep=0; s.stack=[]; s.cur=None; s.cards=[]
    def handle_starttag(s,tag,attrs):
        d={k:v for k,v in attrs}; cl=d.get('class','')
        if tag=='div':
            s.stack.append(cl)
            if cl=='hl':
                s.hldep+=1
                if s.hldep==1: s.cur={'rels':set(),'src':None,'url':None}
        if tag=='span' and s.cur and s.hldep==1:
            sp=cl.split()
            if 'r3' in sp: s.cur['rels'].add('r3')
            if 'r2' in sp: s.cur['rels'].add('r2')
            if 'b1' in sp: s.cur['src']='b1'
            if 'b2' in sp: s.cur['src']='b2'
        if tag=='a' and s.cur and s.hldep==1 and s.cur['url'] is None and s.stack and s.stack[-1]=='src':
            s.cur['url']=d.get('href')
    def handle_endtag(s,tag):
        if tag=='div' and s.stack:
            cl=s.stack.pop()
            if cl=='hl':
                s.hldep-=1
                if s.hldep==0 and s.cur is not None: s.cards.append(s.cur); s.cur=None

# 各墙当前真实卡数 + 关系/来源档
wall={}; rel3=rel2=b1=b2=0; cat=collections.Counter()
for d in DIRS:
    f=os.path.join(KC,f"{d}/{d}.html")
    if not os.path.exists(f): continue
    p=P(); p.feed(open(f,encoding='utf-8').read())
    n=len(p.cards); wall[d]=n
    for c in p.cards:
        if 'r3' in c['rels']: rel3+=1
        if 'r2' in c['rels']: rel2+=1
        if c['src']=='b1': b1+=1
        elif c['src']=='b2': b2+=1
        host=urlparse(c['url']).netloc.lower().replace('www.','') if c['url'] else ''
        cat[src_cat(host) if host else '未标注来源']+=1
total=sum(wall.values())
dbl=rel3+rel2-total

# 本周 runs（08-17~21）净增 + 轮次明细
weekly=collections.Counter(); rounds=[]
for d in DIRS:
    rd=os.path.join(KC,f"{d}/runs")
    if not os.path.isdir(rd): continue
    for fn in sorted(os.listdir(rd)):
        if not fn.endswith('.html'): continue
        m=re.match(rf"{d}-(\d{{4}}-\d{{2}}-\d{{2}})-r(\d+)\.html", fn)
        if not m: continue
        date=m.group(1); rnd=int(m.group(2))
        if date < '2026-08-17' or date > '2026-08-21': continue
        p=P(); p.feed(open(os.path.join(rd,fn),encoding='utf-8').read())
        c=len(p.cards); weekly[d]+=c
        rounds.append((NAMES[d], date, rnd, c))
weekly_total=sum(weekly.values())

b1p=f"{b1/total*100:.1f}%"; b2p=f"{b2/total*100:.1f}%"
r3p=f"{rel3/total*100:.1f}%"; r2p=f"{rel2/total*100:.1f}%"

# 主题排行（累计）
ranked=sorted(wall.items(), key=lambda x:-x[1])

def bar_row(name, val, maxv, extra=''):
    pct=int(val/maxv*100) if maxv else 0
    return f'''<div class="brow"><span class="bl">{name}</span>
      <div class="btrack"><div class="bfill" style="width:{pct}%"></div></div>
      <span class="bv">{val}{extra}</span></div>'''

# 主题累计排行条
maxw=max(wall.values())
theme_bars="\n".join(bar_row(NAMES[d], wall[d], maxw,
    f' <span class="wk">本周+{weekly[d]}</span>' if weekly[d] else ' <span class="wk0">本周无新采</span>')
    for d,_ in ranked)

# 轮次明细表
round_rows="\n".join(
    f"<tr><td>{nm}</td><td>{dt}</td><td>第 {r} 轮</td><td class='pos'>+{c}</td></tr>"
    for nm,dt,r,c in rounds)

# 来源细分
src_rows="\n".join(
    f'''<div class="brow"><span class="bl">{k}</span>
      <div class="btrack"><div class="bfill s2" style="width:{int(v/total*100)}%"></div></div>
      <span class="bv">{v} · {v/total*100:.1f}%</span></div>'''
    for k,v in cat.most_common())

# 来源档 / 关系档 进度条
rel_bar=f'''<div class="brow"><span class="bl">高管间 exec</span><div class="btrack"><div class="bfill r3" style="width:{int(rel3/total*100)}%"></div></div><span class="bv">{rel3} · {r3p}</span></div>
<div class="brow"><span class="bl">上下级 supervisor</span><div class="btrack"><div class="bfill r2" style="width:{int(rel2/total*100)}%"></div></div><span class="bv">{rel2} · {r2p}</span></div>
<div class="note">含 {dbl} 张双档（同时适用高管间+上下级），实际独立卡 {total} 张</div>'''
src_bar=f'''<div class="brow"><span class="bl">一手源</span><div class="btrack"><div class="bfill b1" style="width:{int(b1/total*100)}%"></div></div><span class="bv">{b1} · {b1p}</span></div>
<div class="brow"><span class="bl">二手源</span><div class="btrack"><div class="bfill b2" style="width:{int(b2/total*100)}%"></div></div><span class="bv">{b2} · {b2p}</span></div>'''

HTML=f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>知识采集周报 2026-08-17~21</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:#f4f5fb;color:#1f2233;padding:32px 18px}}
.wrap{{max-width:960px;margin:0 auto}}
header{{background:linear-gradient(120deg,#7c5cff,#22d3ee);border-radius:22px;padding:30px 34px;color:#fff;box-shadow:0 12px 30px rgba(124,92,255,.28)}}
header h1{{font-size:30px;font-weight:800;letter-spacing:1px}}
header .sub{{margin-top:8px;opacity:.92;font-size:15px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:16px;margin:26px 0}}
.kpi{{background:#fff;border-radius:18px;padding:20px 18px;box-shadow:0 6px 18px rgba(31,34,51,.07);border-top:4px solid #7c5cff}}
.kpi .num{{font-size:34px;font-weight:800;background:linear-gradient(120deg,#7c5cff,#22d3ee);-webkit-background-clip:text;background-clip:text;color:transparent}}
.kpi .lab{{font-size:13px;color:#6b7088;margin-top:4px}}
.kpi .sub{{font-size:12px;color:#9aa0b8;margin-top:3px}}
.sec{{background:#fff;border-radius:18px;padding:22px 24px;box-shadow:0 6px 18px rgba(31,34,51,.07);margin-bottom:22px}}
.sec h2{{font-size:19px;margin-bottom:16px;color:#2a2d44;display:flex;align-items:center;gap:8px}}
.sec h2::before{{content:"";width:6px;height:20px;border-radius:4px;background:linear-gradient(180deg,#7c5cff,#22d3ee)}}
.brow{{display:flex;align-items:center;gap:10px;margin:9px 0;font-size:14px}}
.bl{{width:150px;flex:none;color:#44495e;text-align:right}}
.btrack{{flex:1;height:14px;background:#eef0f7;border-radius:8px;overflow:hidden}}
.bfill{{height:100%;border-radius:8px;background:linear-gradient(90deg,#7c5cff,#22d3ee)}}
.bfill.s2{{background:linear-gradient(90deg,#22d3ee,#7c5cff)}}
.bfill.r3{{background:linear-gradient(90deg,#8b5cf6,#a78bfa)}}
.bfill.r2{{background:linear-gradient(90deg,#fb923c,#fdba74)}}
.bfill.b1{{background:linear-gradient(90deg,#22c55e,#4ade80)}}
.bfill.b2{{background:linear-gradient(90deg,#f59e0b,#fbbf24)}}
.bv{{width:120px;flex:none;color:#2a2d44;font-weight:600;font-size:13px}}
.wk{{color:#7c5cff;font-size:12px;font-weight:700}}
.wk0{{color:#aab;font-size:12px}}
.note{{font-size:12px;color:#9aa0b8;margin-top:8px}}
table{{width:100%;border-collapse:collapse;font-size:14px}}
th,td{{padding:10px 8px;text-align:left;border-bottom:1px solid #eef0f7}}
th{{color:#6b7088;font-weight:700;font-size:13px}}
td.pos{{color:#16a34a;font-weight:700}}
.pill{{display:inline-block;padding:3px 10px;border-radius:999px;font-size:12px;font-weight:700;margin:3px 4px 3px 0}}
.pill.ok{{background:#dcfce7;color:#15803d}}
.pill.w{{background:#fef3c7;color:#a16207}}
footer{{text-align:center;color:#9aa0b8;font-size:13px;margin-top:30px;padding:16px}}
@media(max-width:560px){{.bl{{width:96px;font-size:12px}}.bv{{width:84px}}}}
</style></head>
<body><div class="wrap">
<header>
  <h1>📚 文化活动知识采集 · 周报</h1>
  <div class="sub">统计区间：2026-08-17 ~ 2026-08-21（本周）｜ 自动补采 6h 轮询</div>
</header>

<div class="grid">
  <div class="kpi"><div class="num">{total}</div><div class="lab">全库累计知识卡</div><div class="sub">6 主题合计</div></div>
  <div class="kpi"><div class="num" style="background:linear-gradient(120deg,#16a34a,#22d3ee);-webkit-background-clip:text;background-clip:text;color:transparent">{weekly_total}</div><div class="lab">本周新增</div><div class="sub">净增·去重后</div></div>
  <div class="kpi"><div class="num">6</div><div class="lab">采集主题</div><div class="sub">员工大会/Offsite/破冰/颁奖/OpenDay/下午茶</div></div>
  <div class="kpi"><div class="num">{b1p}</div><div class="lab">一手源占比</div><div class="sub">一手 {b1} · 二手 {b2}</div></div>
  <div class="kpi"><div class="num">{len(rounds)}</div><div class="lab">本周补采轮次</div><div class="sub">4 主题被轮询</div></div>
</div>

<div class="sec">
  <h2>① 主题采集进度（累计 + 本周新增）</h2>
  {theme_bars}
</div>

<div class="sec">
  <h2>② 本周补采轮次明细</h2>
  <table><thead><tr><th>主题</th><th>日期</th><th>轮次</th><th>新增</th></tr></thead>
  <tbody>{round_rows}</tbody></table>
  <div class="note">offsite / 颁奖 本周未轮询（维持历史累计：Offsite {wall['offsite']} 卡 · 颁奖 {wall['award']} 卡）。下轮指针回到员工大会接续。</div>
</div>

<div class="sec">
  <h2>③ 关系档 / 来源档分布（全库）</h2>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px">
    <div><div class="note" style="margin:0 0 6px;color:#6b7088;font-weight:700">关系档（按受众权力距离）</div>{rel_bar}</div>
    <div><div class="note" style="margin:0 0 6px;color:#6b7088;font-weight:700">来源档（一手/二手）</div>{src_bar}</div>
  </div>
</div>

<div class="sec">
  <h2>④ 来源细分（按媒体类型，全库 {total} 卡）</h2>
  {src_rows}
  <div class="note">按每张卡首个来源链接域名启发式归类；企业官网/SOP 为主，一手源中腾讯系（KM/乐享）占 {cat.get('腾讯系（KM/乐享/腾讯新闻）',0)} 卡。</div>
</div>

<div class="sec">
  <h2>⑤ 三端同步状态</h2>
  <p style="font-size:14px;line-height:1.9">
    <span class="pill ok">✅ GitHub Pages</span> 各墙 + 独立轮次页 + index.json 已推送（master）<br>
    <span class="pill ok">✅ Obsidian</span> 各主题汇总笔记 + 00-索引 + 本轮独立笔记已落库<br>
    <span class="pill ok">✅ 乐享</span> 累计墙 in-place 更新 + 本周各轮次页独立 entry（待清洗素材/各主题子文件夹）<br>
    <span class="pill w">⏸ 企微群</span> 待你确认后再推送（本次未发）
  </p>
</div>

<footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>
</div></body></html>'''

out=os.path.join(KC,'weekly-report-2026-08-17_21.html')
open(out,'w',encoding='utf-8').write(HTML)
print("written:", out, os.path.getsize(out), "bytes")
print("total",total,"weekly",weekly_total,"rounds",len(rounds))
