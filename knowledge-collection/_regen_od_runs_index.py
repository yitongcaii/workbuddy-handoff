# -*- coding: utf-8 -*-
"""重建 openday/runs/index.html 分页索引（legacy b1/b2 拆分 + 真实轮次 r10~r16，按采集先后序）。"""
import os, re
BASE="C:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection"
RUNS=os.path.join(BASE,"openday","runs")

def count_cards(fn):
    p=os.path.join(RUNS,fn)
    if not os.path.exists(p): return 0
    return open(p,encoding='utf-8').read().count('class="hl"')

# (文件名, 序号, 轮次标签, 日期, 卡片数, 说明)
items=[
 ("openday-2026-08-10-b1.html",1,"批次 b1","2026-08-10",12,"历史拆分批次（前12卡·采集最早）"),
 ("openday-2026-08-10-b2.html",2,"批次 b2","2026-08-10",3,"历史拆分批次（次3卡）"),
 ("openday-2026-08-11-r10.html",3,"第10轮","2026-08-11",11,"央企媒体/客户/品牌/公众开放日+员工总部开放日+方法论"),
 ("openday-2026-08-12-r11.html",4,"第11轮","2026-08-12",12,"环保设施/政法/电力/媒体/消防/客户开放日向"),
 ("openday-2026-08-13-r12.html",5,"第12轮","2026-08-13",13,"博物馆/纪念馆/医院/政府开放月/高校实验室/社区开放日"),
 ("openday-2026-08-14-r13.html",6,"第13轮","2026-08-14",13,"地铁轨交/环保设施/图书馆文化馆/气象地震/公交/工业旅游开放日"),
 ("openday-2026-08-15-r14.html",7,"第14轮","2026-08-15",14,"警营/公用事业/航空科普/金融公众/农业科技/港口/政法/文化馆开放日"),
 ("openday-2026-08-15-r15.html",8,"第15轮","2026-08-15",15,"税务/消防/铁路/水务/法院/海关·国门公众开放日向"),
 ("openday-2026-08-16-r16.html",9,"第16轮","2026-08-16",16,"校园/科技馆科普/市场监管食药安全/医院卫健/电力变电站公众开放日向"),
]

cards_html=''
for fn,seq,label,date,nc,note in items:
    cards_html+=f'''    <div class="idxcard">
      <div class="seq">{seq}</div>
      <h3>🚪 Open Day 开放日 · {label}</h3>
      <div class="meta">{date} ｜ {nc} 张卡 ｜ {note}</div>
      <a href="{fn}">查看本批 →</a>
    </div>
'''
n_total=sum(count_cards(fn) for fn,_,_,_,_,_ in items)
html=f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Open Day 开放日 · 分页索引</title>
<style>
:root{{--bg:#f4f6fb;--card:#ffffff;--ink:#1f2430;--sub:#5b6478;--accent:#6c5ce7;--accent2:#00b8d9;--chip:#eef0ff;}}
*{{box-sizing:border-box;margin:0;padding:0;}}
body{{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:linear-gradient(135deg,#eef1ff 0%,#e6f7ff 100%);color:var(--ink);padding:28px 18px;line-height:1.6;}}
.wrap{{max-width:1080px;margin:0 auto;}}
.hero{{background:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);border-radius:22px;padding:30px 32px;color:#fff;box-shadow:0 14px 40px rgba(108,92,231,.25);margin-bottom:22px;}}
.hero h1{{font-size:26px;font-weight:800;letter-spacing:1px;margin-bottom:8px;}}
.hero p{{font-size:14px;opacity:.95;}}
.relbar{{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px;}}
.relbar span{{background:rgba(255,255,255,.2);border-radius:20px;padding:5px 14px;font-size:13px;font-weight:600;}}
.nav{{margin:0 0 14px;}}
.nav a{{display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;}}
.grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;}}
.idxcard{{position:relative;background:#fff;border-radius:16px;padding:22px 18px 16px;border-top:4px solid var(--accent);box-shadow:0 10px 32px rgba(108,92,231,.10);}}
.idxcard .seq{{position:absolute;top:-14px;left:18px;width:30px;height:30px;border-radius:50%;background:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);color:#fff;font-weight:800;font-size:14px;display:flex;align-items:center;justify-content:center;box-shadow:0 6px 16px rgba(108,92,231,.35);}}
.idxcard h3{{font-size:16px;margin-bottom:6px;}}
.idxcard .meta{{font-size:12.5px;color:var(--sub);}}
.idxcard a{{display:inline-block;margin-top:10px;color:var(--accent2);text-decoration:none;font-weight:600;font-size:13px;}}
footer{{text-align:center;padding:24px;color:#94a3b8;font-size:13px;border-top:1px solid #e2e8f0;margin-top:40px;}}
</style>
</head>
<body>
<div class="wrap">
<div class="nav"><a href="../openday.html">🗂 累计总索引</a></div>
  <div class="hero">
    <h1>🚪 Open Day 开放日 · 分页独立页索引</h1>
    <p>累计墙 <a href="../openday.html" style="color:#fff;text-decoration:underline;">openday.html</a> 共拆为 {len(items)} 个独立页（含 2 个历史拆分批次 + 7 个真实补采轮次）｜ 按<b>采集 / 创建顺序从早到晚</b>排列（序号 1 → {len(items)}）｜ 共 {n_total} 张卡（与累计墙 109 卡一致：含早期历史拆分来源 + 真实轮次）｜ 仅②上下级 / ③高管间，剔除①</p>
    <div class="relbar">
      <span>② 领导↔员工（上下级）</span>
      <span>③ 领导↔领导（高管间）</span>
    </div>
  </div>
  <div class="grid">
{cards_html}  </div>
</div>
<footer style="text-align:center;padding:24px;color:#94a3b8;font-size:13px;border-top:1px solid #e2e8f0;margin-top:40px;">📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>
</body>
</html>
'''
out=os.path.join(RUNS,"index.html")
open(out,'w',encoding='utf-8').write(html)
print('runs/index.html regenerated:',len(items),'pages,',n_total,'cards')
