# -*- coding: utf-8 -*-
import json, os, io, sys

BASE = r"c:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection"
HTML = os.path.join(BASE, "afternoontea", "afternoontea.html")
INC = os.path.join(BASE, "afternoontea", "afternoontea-20260815b.html")
IDX = os.path.join(BASE, "index.json")
PORTAL = os.path.join(BASE, "index.html")
RUNS = os.path.join(BASE, "afternoontea", "runs", "index.html")
NOTE = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\afternoontea\下午茶研讨-知识卡汇总.md"
ZERO = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
LTP = os.path.join(BASE, "..", "last-topic.txt")
LTP = os.path.join(BASE, "last-topic.txt")

ONLINE = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/afternoontea"

def disp(url):
    return url.replace("https://", "").replace("http://", "")

def hl(emoji, title, cat, rel_cls, rel_txt, src_cls, src_txt, val, how, note, url):
    return (
        '    <div class="hl">\n'
        '      <div class="top"><span class="emoji">%s</span><h3>%s</h3>'
        '<span class="cat">%s</span><span class="badge %s">%s</span>'
        '<span class="badge %s">%s</span></div>\n'
        '      <p class="val">%s</p>\n'
        '      <details class="exec"><summary>怎么做</summary><div class="inner">%s</div></details>\n'
        '      <div class="src">🔗 <a href="%s" target="_blank">%s</a></div>\n'
        '      <div class="note">适用：%s</div>\n'
        '    </div>\n'
    ) % (emoji, title, cat, rel_cls, rel_txt, src_cls, src_txt, val, how, url, disp(url), note)

# ---- 4 new cards (all ②/③, no peer) ----
cards = [
    # exec 1
    hl("🤝", "一带一路新引擎·科技下午茶第八期·上市公司企业家闭门", "企业家闭门", "r3", "高管间", "b2", "二手",
       "中国投资协会创投发展中心（CRIOC）「科技下午茶」第八期，定位『一带一路新引擎』，定向邀约上市公司企业家、高管与投资人闭门交流，围绕跨境投资、产业出海与资本协同，不设媒体、只谈干货。",
       "复制其『闭门 + 定向邀约 + 固定栏目品牌』运营打法：每期设定主题主轴、严格筛选参会高管层级、前置议题征集、现场无媒体、会后形成纪要闭环；适合本公司面向核心客户 / 生态伙伴高管的轻量关系经营。",
       "③ 面向上市公司企业家 / 高管的闭门私享，商务化、以产业与资本共同目标切入",
       "https://crioc.org/index.php?s=/sys/209.html"),
    # exec 2
    hl("🏛️", "高企·小巨人 企业家下午茶（第四期）· 政企产投融合闭门", "产投融合", "r3", "高管间", "b2", "二手",
       "无锡市新吴区「高企·小巨人」企业家下午茶第四期，政府 + 高新技术企业 + 投资机构三方同场，围绕『产投融合』打通企业融资与产业落地，小范围、强筛选。",
       "借鉴『政府搭台、企业出题、资本答题』的小范围闭门机制：限定企业规模（高企 / 专精特新）与投资人层级，单场聚焦一个产业链命题，现场即形成对接清单；适合政企 / 产投类高管对话。",
       "③ 政企 + 产业 + 资本三方高管闭门对话，以产投共同目标切入",
       "https://wxzjtx.com/index.php?s=/Mobile/Show/index/cid/403/id/683.html"),
    # supervisor 1
    hl("🫖", "党工委书记「下午茶」· 中铁十七局青年职工交心", "书记谈心", "r2", "上下级", "b2", "二手",
       "中铁十七局党工委书记以『下午茶』形式与青年职工面对面交心，淡化会议感、拉近上下级距离，倾听一线诉求并现场回应。",
       "照搬『去会场化 + 一把手直接听 + 现场回应闭环』：选轻松场地、书记与青年员工同坐、提前收集匿名问题、能答的当场答、不能答的明确时限跟进；适合新员工 / 青年骨干的上下级信任建设。",
       "② 领导与青年 / 一线员工交心，尊重不越界、建信任不暴露隐私",
       "https://paper.crcc.cn/html/2017-06/24/nw.D110000zgtdjzb_20170624_3-3.htm"),
    # supervisor 2
    hl("💬", "周末下午茶·书记一对一谈心谈话", "一对一谈心", "r2", "上下级", "b2", "二手",
       "常州机关工委「周末下午茶」机制，书记与干部一对一谈心谈话，利用非工作时段、轻松场景开展日常思想政治工作与压力疏导。",
       "引入『固定时段 + 一对一 + 非正式场景』的谈心制度：每周固定一个轻松时段、按预约一对一、谈工作也谈状态、形成个人关注台账；适合管理者对直属下级的常态化情绪与成长关怀。",
       "② 管理者与直属下级一对一谈心，尊重边界、以倾听与支持切入",
       "https://jggw.changzhou.gov.cn/html/jggw/2022/AIJMPLLH_0601/29920.html"),
]

exec_block = cards[0] + cards[1]
sup_block = cards[2] + cards[3]

# ===== 1. cumulative afternoontea.html =====
s = open(HTML, encoding="utf-8").read()
grid = '  <div class="grid">'
i1 = s.find(grid)
assert i1 > 0, "sec3 grid not found"
s = s[:i1+len(grid)] + exec_block + s[i1+len(grid):]
i2 = s.find(grid, i1+len(grid)+1)
assert i2 > 0, "sec2 grid not found"
s = s[:i2+len(grid)] + sup_block + s[i2+len(grid):]
# counts
s = s.replace('<span class="tag">40 卡</span>', '<span class="tag">42 卡</span>', 1)
s = s.replace('<span class="tag">53 卡</span>', '<span class="tag">55 卡</span>', 1)
# hero
s = s.replace('十三轮 enrich 2026-08-15(+5)</p>', '十三轮 enrich 2026-08-15(+5)｜ 十四轮 enrich 2026-08-15(+4)</p>', 1)
tmp = HTML + ".tmp"
open(tmp, "w", encoding="utf-8").write(s)
os.replace(tmp, HTML)
print("afternoontea.html updated -> 95 cards (sec3=42, sec2=55)")

# ===== 2. incremental page afternoontea-20260815b.html =====
inc_html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>下午茶研讨 · 十四轮 enrich（+4）</title>
<style>
:root{--bg:#f4f6fb;--card:#ffffff;--ink:#1f2430;--sub:#5b6478;--accent:#6c5ce7;--accent2:#00b8d9;--chip:#eef0ff;}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:linear-gradient(135deg,#eef1ff 0%,#e6f7ff 100%);color:var(--ink);padding:28px 18px;line-height:1.6;}
.wrap{max-width:1080px;margin:0 auto;}
.hero{background:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);border-radius:22px;padding:30px 32px;color:#fff;box-shadow:0 14px 40px rgba(108,92,231,.25);margin-bottom:22px;}
.hero h1{font-size:28px;font-weight:800;letter-spacing:1px;margin-bottom:8px;}
.hero p{font-size:14px;opacity:.95;}
.relbar{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px;}
.relbar span{background:rgba(255,255,255,.2);border-radius:20px;padding:5px 14px;font-size:13px;font-weight:600;}
.back{display:inline-block;margin:0 0 14px;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;}
.sec{margin:30px 0 12px;display:flex;align-items:center;gap:10px;}
.sec h2{font-size:19px;font-weight:800;}
.sec .tag{font-size:12px;padding:4px 12px;border-radius:12px;font-weight:700;}
.sec3 .tag{background:#f3e8ff;color:#7b2cbf;} .sec3 h2{color:#7b2cbf;}
.sec2 .tag{background:#fff3e0;color:#c0651a;} .sec2 h2{color:#c0651a;}
.sec .desc{font-size:12.5px;color:var(--sub);margin-left:2px;}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;}
.hl{background:var(--card);border-radius:18px;padding:18px 18px 16px;border-top:4px solid var(--accent);box-shadow:0 10px 32px rgba(108,92,231,.10);display:flex;flex-direction:column;gap:9px;}
.top{display:flex;align-items:center;gap:8px;flex-wrap:wrap;}
.emoji{font-size:22px;}
.hl h3{font-size:16px;font-weight:700;flex:1;min-width:120px;}
.cat{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:600;background:var(--chip);color:var(--accent);}
.badge{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:700;}
.b2{background:#fff1e6;color:#c0651a;}
.b1{background:#e6f9ed;color:#1a9e5a;}
.r2{background:#fff3e0;color:#c0651a;}
.r3{background:#f3e8ff;color:#7b2cbf;}
.val{font-size:13.5px;color:var(--sub);}
.exec{margin-top:2px;border-top:1px dashed #e2e8f0;padding-top:8px;}
.exec summary{cursor:pointer;font-size:13px;font-weight:600;color:var(--accent);}
.exec .inner{font-size:13px;color:var(--sub);margin-top:6px;padding-left:4px;}
.src{font-size:12px;word-break:break-all;}
.src a{color:var(--accent2);text-decoration:none;}
.note{font-size:12px;color:#94a3b8;border-left:3px solid #e2e8f0;padding-left:8px;}
footer{text-align:center;padding:24px;color:#94a3b8;font-size:13px;border-top:1px solid #e2e8f0;margin-top:40px;}
</style>
</head>
<body>
<div class="wrap">
<a class="back" href="afternoontea.html">← 返回累计总索引</a>
  <div class="hero">
    <h1>🍵 下午茶研讨 · 十四轮 enrich（+4）</h1>
    <p>本轮 2026-08-15（+4）｜ 仅 ②上下级 / ③高管间 ｜ 已剔除平级 / 朋友向（①）</p>
    <div class="relbar">
      <span>② 领导↔员工（上下级，supervisor）</span>
      <span>③ 领导↔领导（高管间，exec）</span>
    </div>
  </div>
  <div class="sec sec3"><h2>③ 领导↔领导（高管间 · exec）</h2><span class="tag">2 卡</span></div>
  <div class="grid">
""" + exec_block + """  </div>
  <div class="sec sec2"><h2>② 领导↔员工（上下级 · supervisor）</h2><span class="tag">2 卡</span></div>
  <div class="grid">
""" + sup_block + """  </div>
  <footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>
</div>
</body>
</html>
"""
open(INC, "w", encoding="utf-8").write(inc_html)
print("incremental page written ->", INC)

# ===== 3. index.json =====
d = json.load(open(IDX, encoding="utf-8"))
before = len(d)
new_entries = [
    {"title":"一带一路新引擎·科技下午茶第八期·上市公司企业家闭门","normKey":"一带一路新引擎·科技下午茶第八期·上市公司企业家闭门","url":"https://crioc.org/index.php?s=/sys/209.html","sourceType":"secondary","relation":"exec","summary":"中国投资协会创投发展中心（CRIOC）「科技下午茶」第八期，定位『一带一路新引擎』，定向邀约上市公司企业家、高管与投资人闭门交流，围绕跨境投资、产业出海与资本协同，不设媒体、只谈干货。"},
    {"title":"高企·小巨人 企业家下午茶（第四期）· 政企产投融合闭门","normKey":"高企·小巨人 企业家下午茶（第四期）· 政企产投融合闭门","url":"https://wxzjtx.com/index.php?s=/Mobile/Show/index/cid/403/id/683.html","sourceType":"secondary","relation":"exec","summary":"无锡市新吴区「高企·小巨人」企业家下午茶第四期，政府 + 高新技术企业 + 投资机构三方同场，围绕『产投融合』打通企业融资与产业落地，小范围、强筛选。"},
    {"title":"党工委书记「下午茶」· 中铁十七局青年职工交心","normKey":"党工委书记「下午茶」· 中铁十七局青年职工交心","url":"https://paper.crcc.cn/html/2017-06/24/nw.D110000zgtdjzb_20170624_3-3.htm","sourceType":"secondary","relation":"supervisor","summary":"中铁十七局党工委书记以『下午茶』形式与青年职工面对面交心，淡化会议感、拉近上下级距离，倾听一线诉求并现场回应。"},
    {"title":"周末下午茶·书记一对一谈心谈话","normKey":"周末下午茶·书记一对一谈心谈话","url":"https://jggw.changzhou.gov.cn/html/jggw/2022/AIJMPLLH_0601/29920.html","sourceType":"secondary","relation":"supervisor","summary":"常州机关工委「周末下午茶」机制，书记与干部一对一谈心谈话，利用非工作时段、轻松场景开展日常思想政治工作与压力疏导。"},
]
for e in new_entries:
    d.append(e)
json.dump(d, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("index.json updated ->", before, "->", len(d), "(+4)")

# ===== 4. Obsidian note =====
n = open(NOTE, encoding="utf-8").read()
n = n.replace("（93 卡 · 上下级/高管间）", "（95 卡 · 上下级/高管间）", 1)
n = n.replace("｜ 十三轮 enrich 2026-08-15（+5）", "｜ 十三轮 enrich 2026-08-15（+5）｜ 十四轮 enrich 2026-08-15(+4)", 1)
round_block = (
    "## 轮次 2026-08-15（+4）\n\n"
    "> 本轮新增 4 张（上下级 2 / 高管间 2），全部为 ②上下级 / ③高管间，已剔除平级/朋友向（①）。线上：[本轮增量页](%s/afternoontea-20260815b.html) ｜ [累计卡片墙](%s/afternoontea.html)\n\n"
    "**③ 高管间（2）**\n"
    "- 一带一路新引擎·科技下午茶第八期·上市公司企业家闭门 — 二手（CRIOC 创投发展中心）：定向邀约上市公司企业家/高管/投资人，闭门谈跨境投资与资本协同，无媒体只谈干货\n"
    "- 高企·小巨人 企业家下午茶（第四期）·政企产投融合闭门 — 二手（无锡新吴区）：政府+高企+投资机构三方同场，单场聚焦一产业链命题，现场形成对接清单\n\n"
    "**② 上下级（2）**\n"
    "- 党工委书记「下午茶」·中铁十七局青年职工交心 — 二手（中国铁道建筑报）：一把手去会场化直接听青年职工，现场回应闭环\n"
    "- 周末下午茶·书记一对一谈心谈话 — 二手（常州机关工委）：固定时段+一对一+非正式场景，管理者对直属下级常态化情绪与成长关怀\n\n"
) % (ONLINE, ONLINE)
n = n.replace("## ③ 领导↔领导（高管间 · exec）— 40 卡",
              round_block + "## ③ 领导↔领导（高管间 · exec）— 42 卡", 1)
n = n.replace("## ② 领导↔员工（上下级 · supervisor）— 53 卡",
              "## ② 领导↔员工（上下级 · supervisor）— 55 卡", 1)
open(NOTE, "w", encoding="utf-8").write(n)
print("Obsidian note updated -> 95 cards (sec3=42, sec2=55)")

# ===== 5. 00-索引 =====
z = open(ZERO, encoding="utf-8").read()
z = z.replace("十三轮 enrich +5）", "十三轮 enrich +5 ｜ 2026-08-15 十四轮 enrich +4）", 1)
z = z.replace("**93 卡**", "**95 卡**", 1)
z = z.replace("③高管间(...) 40 卡 / ②上下级(...) 53 卡", "③高管间(...) 42 卡 / ②上下级(...) 55 卡", 1)
z = z.replace("一手 20 + 二手 73", "一手 20 + 二手 77", 1)
z = z.replace("②中安华力「穿透管理」一线茶话会）。",
              "②中安华力「穿透管理」一线茶话会）。十四轮 enrich 新增（③一带一路科技下午茶·上市公司企业家闭门 / ③高企·小巨人产投融合闭门 + ②中铁十七局党工委书记青年职工交心 / ②常州周末下午茶书记一对一谈心）。", 1)
rows = (
    "\n"
    "| 一带一路新引擎·科技下午茶第八期·上市公司企业家闭门（afternoontea.html） | 4 | 二手 | ③高管间 | 定向邀约上市公司企业家/高管/投资人闭门，谈跨境投资与资本协同，无媒体只谈干货 |\n"
    "| 高企·小巨人 企业家下午茶（第四期）·政企产投融合闭门（afternoontea.html） | 4 | 二手 | ③高管间 | 政府+高企+投资机构三方同场，单场聚焦一产业链命题，现场形成对接清单 |\n"
    "| 党工委书记「下午茶」·中铁十七局青年职工交心（afternoontea.html） | 4 | 二手 | ②上下级 | 一把手去会场化直接听青年职工，现场回应闭环，建信任不越界 |\n"
    "| 周末下午茶·书记一对一谈心谈话（afternoontea.html） | 4 | 二手 | ②上下级 | 固定时段+一对一+非正式场景，管理者对直属下级常态化情绪与成长关怀 |\n"
)
anchor = "## 主题：员工大会"
ai = z.find(anchor)
z = z[:ai] + rows + z[ai:]
open(ZERO, "w", encoding="utf-8").write(z)
print("00-知识采集索引 updated -> +4 rows, 95 cards")

# ===== 6. portal index.html =====
p = open(PORTAL, encoding="utf-8").read()
p = p.replace('<div class="n">599</div>', '<div class="n">603</div>', 1)
p = p.replace('599 张知识卡', '603 张知识卡', 1)
p = p.replace('<div class="cnt">93 卡</div>', '<div class="cnt">97 卡</div>', 1)
p = p.replace('一手 117 张、二手 482 张', '一手 117 张、二手 486 张', 1)
open(PORTAL, "w", encoding="utf-8").write(p)
print("portal index.html updated -> total 603, afternoontea 97, 二手 486")

# ===== 7. runs/index.html (minimal safe append) =====
r = open(RUNS, encoding="utf-8").read()
r = r.replace("共拆为 6 个批次独立页", "共拆为 7 个批次独立页", 1)
r = r.replace("（序号 1 → 6）", "（序号 1 → 7）", 1)
card7 = (
    '    <div class="idxcard">\n'
    '      <div class="seq">7</div>\n'
    '      <h3>第 7 / 共 7 批</h3>\n'
    '      <div class="meta">4 卡 ｜ ③高管间 2 / ②上下级 2</div>\n'
    '      <a href="../afternoontea-20260815b.html">查看本批 →</a>\n'
    '    </div>\n'
)
r = r.replace("PLACEHOLDER", card7 + "PLACEHOLDER", 1)
open(RUNS, "w", encoding="utf-8").write(r)
print("runs/index.html updated -> batch 7 added")

# ===== 8. last-topic.txt -> 员工大会 =====
open(os.path.join(BASE, "last-topic.txt"), "w", encoding="utf-8").write("员工大会\n")
print("last-topic.txt -> 员工大会")

print("\nDONE r14 afternoontea: N=4 M=0, 95 cards total")
