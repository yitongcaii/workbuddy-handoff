# -*- coding: utf-8 -*-
"""生成知识卡数量总览海报（竖版，基于 6 张墙真实数据）。"""
import os, json, collections
from urllib.parse import urlparse
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.abspath(__file__))
DIRS = ['staff-meeting', 'offsite', 'icebreaker', 'award', 'openday', 'afternoontea']
NAMES = {'staff-meeting': '员工大会', 'offsite': 'Offsite 团建务虚', 'icebreaker': '破冰',
         'award': '颁奖', 'openday': 'Open Day', 'afternoontea': '下午茶研讨'}

TENCENT = {'qq.com', 'tencent.com', 'woa.com', 'km.woa.com', 'lexiangla.com', 'qq.com.cn'}
AGG = {'toutiao.com', 'bytedance.com'}
NEWS = {'sohu.com', 'sina.com.cn', '163.com', 'ifeng.com', 'people.com.cn', 'xinhuanet.com',
        'chinanews.com.cn', 'thepaper.cn', 'yicai.com', 'cctv.com'}
DOC = {'renrendoc.com', 'qg68.cn', 'doc88.com', 'wenku.baidu.com', 'book118.com',
       'originaldown.cn', 'max.book118.com'}
WX = {'mp.weixin.qq.com', 'weixin.qq.com'}
HR = {'ihr360.com', 'shangyexinzhi.com', 'hrtxt.com', 'sanmao.cn', 'hroot.com'}
OV = {'linkedin.com', 'medium.com', 'blogspot.com', 'wordpress.com', 'inc.com', 'substack.com'}

def src_cat(host):
    h = host.lower().replace('www.', '').replace('m.', '')
    if any(t in h for t in TENCENT): return '腾讯系（KM/乐享/腾讯新闻）'
    if any(t in h for t in AGG): return '头条/资讯聚合'
    if any(t in h for t in NEWS) or (h.endswith('.cn') and ('news' in h or 'rb' in h or 'daily' in h)): return '新闻门户'
    if any(t in h for t in DOC): return '文档文库（转载）'
    if any(t in h for t in WX): return '微信公众号'
    if any(t in h for t in HR): return 'HR 专业媒体'
    if any(t in h for t in OV): return '海外媒体/博客（英文）'
    if h.endswith('.edu') or h.endswith('.gov') or 'edu.' in h: return '学术/官方报告'
    if h.endswith('.org'): return '机构/非营利'
    return '企业官网/官方 SOP'

class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.hldep = 0; s.stack = []; s.cur = None; s.cards = []
    def handle_starttag(s, tag, attrs):
        d = {k: v for k, v in attrs}; cl = d.get('class', '')
        if tag == 'div':
            s.stack.append(cl)
            if cl == 'hl':
                s.hldep += 1
                if s.hldep == 1: s.cur = {'rels': set(), 'src': None, 'url': None}
        if tag == 'span' and s.cur and s.hldep == 1:
            sp = cl.split()
            if 'r3' in sp: s.cur['rels'].add('r3')
            if 'r2' in sp: s.cur['rels'].add('r2')
            if 'b1' in sp: s.cur['src'] = 'b1'
            if 'b2' in sp: s.cur['src'] = 'b2'
        if tag == 'a' and s.cur and s.hldep == 1 and s.cur['url'] is None and s.stack and s.stack[-1] == 'src':
            s.cur['url'] = d.get('href')
    def handle_endtag(s, tag):
        if tag == 'div' and s.stack:
            cl = s.stack.pop()
            if cl == 'hl':
                s.hldep -= 1
                if s.hldep == 0 and s.cur is not None: s.cards.append(s.cur); s.cur = None

tot = r3 = r2 = b1 = b2 = 0
cat = collections.Counter(); per = []
for d in DIRS:
    f = os.path.join(ROOT, d, f'{d}.html')
    if not os.path.exists(f): continue
    p = P(); p.feed(open(f, encoding='utf-8').read()); n = len(p.cards)
    per.append((NAMES[d], n)); tot += n
    for c in p.cards:
        if 'r3' in c['rels']: r3 += 1
        if 'r2' in c['rels']: r2 += 1
        if c['src'] == 'b1': b1 += 1
        elif c['src'] == 'b2': b2 += 1
        host = urlparse(c['url']).netloc.lower().replace('www.', '') if c['url'] else ''
        cat[src_cat(host) if host else '未标注来源'] += 1

per.sort(key=lambda x: -x[1])
src_top = cat.most_common(6)
double = r3 + r2 - tot
maxn = max(n for _, n in per)

HTML = f"""<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:#0e1020;padding:28px}}
.poster{{max-width:760px;margin:0 auto;background:linear-gradient(160deg,#f5f3ff 0%,#eef6ff 100%);border-radius:28px;overflow:hidden;box-shadow:0 20px 60px rgba(80,40,160,.25)}}
.head{{background:linear-gradient(120deg,#7c5cff,#22d3ee);padding:38px 34px 30px;color:#fff;position:relative}}
.head .k{{font-size:15px;letter-spacing:3px;opacity:.9}}
.head h1{{font-size:40px;font-weight:800;margin-top:6px;letter-spacing:1px}}
.head .sub{{font-size:16px;opacity:.92;margin-top:8px}}
.hero{{display:flex;gap:18px;padding:30px 34px 8px}}
.hero .box{{flex:1;background:#fff;border-radius:20px;padding:22px 18px;text-align:center;box-shadow:0 8px 22px rgba(80,40,160,.10)}}
.hero .num{{font-size:52px;font-weight:900;line-height:1;color:#e23a3a}}
.hero .lab{{font-size:15px;color:#444;margin-top:8px}}
.hero .num.s{{color:#e23a3a;font-size:40px}}
.sec{{padding:18px 34px}}
.sec h2{{font-size:19px;color:#3b2f7a;font-weight:800;margin-bottom:14px;display:flex;align-items:center;gap:8px}}
.sec h2::before{{content:"";width:6px;height:20px;background:linear-gradient(#7c5cff,#22d3ee);border-radius:4px}}
.bar{{display:flex;align-items:center;gap:12px;margin:11px 0}}
.bar .name{{width:130px;font-size:15px;color:#333;text-align:right}}
.bar .track{{flex:1;height:24px;background:#eceafc;border-radius:12px;overflow:hidden}}
.bar .fill{{height:100%;background:linear-gradient(90deg,#7c5cff,#22d3ee);border-radius:12px;display:flex;align-items:center;justify-content:flex-end;padding-right:10px;color:#fff;font-size:13px;font-weight:700}}
.grid2{{display:flex;gap:14px}}
.grid2 .c{{flex:1;background:#fff;border-radius:18px;padding:18px;text-align:center;box-shadow:0 6px 16px rgba(80,40,160,.08)}}
.grid2 .c .n{{font-size:34px;font-weight:900}}
.grid2 .c.r3 .n{{color:#7c5cff}} .grid2 .c.r2 .n{{color:#fb923c}}
.grid2 .c .t{{font-size:15px;color:#555;margin-top:6px}}
.srcrow{{display:flex;align-items:center;gap:10px;margin:9px 0;font-size:14px}}
.srcrow .sn{{width:200px;color:#444;text-align:right}}
.srcrow .st{{width:54px;font-weight:700;color:#3b2f7a}}
.srcrow .track{{flex:1;height:14px;background:#eceafc;border-radius:8px;overflow:hidden}}
.srcrow .fill{{height:100%;background:linear-gradient(90deg,#22d3ee,#7c5cff);border-radius:8px}}
.foot{{text-align:center;padding:20px;font-size:13px;color:#8a86b8;background:#faf8ff}}
</style></head><body><div class="poster">
<div class="head"><div class="k">CULTURE ACTIVITY KNOWLEDGE BASE</div>
<h1>文化活动知识库 · 知识卡总览</h1>
<div class="sub">6 大主题 · 受众关系分层 · 来源细分看板</div></div>
<div class="hero">
<div class="box"><div class="num">{tot}</div><div class="lab">全库累计知识卡</div></div>
<div class="box"><div class="num s">{len(DIRS)}</div><div class="lab">采集主题</div></div>
</div>
<div class="sec"><h2>主题采集量排行</h2>
"""
for name, n in per:
    pct = int(n / maxn * 100)
    HTML += f'<div class="bar"><div class="name">{name}</div><div class="track"><div class="fill" style="width:{pct}%">{n}</div></div></div>\n'
HTML += f"""</div>
<div class="sec"><h2>受众关系档</h2><div class="grid2">
<div class="c r3"><div class="n">{r3}</div><div class="t">高管间（exec）</div></div>
<div class="c r2"><div class="n">{r2}</div><div class="t">上下级（supervisor）</div></div>
</div><div style="font-size:13px;color:#8a86b8;margin-top:10px">注：平级/朋友向（peer）已按治理规则全部剔除，不计入。其中 {double} 张为双档卡。</div></div>
<div class="sec"><h2>来源一手 / 二手</h2><div class="grid2">
<div class="c r3"><div class="n">{b1}</div><div class="t">一手源（{b1/tot*100:.0f}%）</div></div>
<div class="c r2"><div class="n">{b2}</div><div class="t">二手源（{b2/tot*100:.0f}%）</div></div>
</div></div>
<div class="sec"><h2>来源细分（按媒体类型）</h2>
"""
maxtop = max(v for _, v in src_top)
for name, v in src_top:
    pct = int(v / maxtop * 100)
    HTML += f'<div class="srcrow"><div class="sn">{name}</div><div class="st">{v}</div><div class="track"><div class="fill" style="width:{pct}%"></div></div></div>\n'
HTML += f"""</div>
<div class="foot">📌 本页由 yitong 沉淀整理 · 文化活动知识库</div>
</div></body></html>"""

out = os.path.join(ROOT, 'knowledge-cards-overview-poster.html')
open(out, 'w', encoding='utf-8').write(HTML)
print(f"poster written: {out}  ({os.path.getsize(out)} bytes)")
print(f"stats: total={tot} topics={len(DIRS)} r3={r3} r2={r2} b1={b1} b2={b2} double={double}")
print("per:", per)
