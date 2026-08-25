# -*- coding: utf-8 -*-
"""Open Day R28 (2026-08-26, +13: 10② + 3③) — clean inject + standalone page.
Baseline = LIVE GitHub Pages openday.html (207 cards, ends 二十七轮+10).
My 13 cards become 二十八轮 to avoid clashing with the live 二十七轮(+10).
"""
import re, json, os

BASE = os.path.dirname(os.path.abspath(__file__))
SUM = os.path.join(BASE, "openday", "openday.html")
CARDS = os.path.join(BASE, "_openday_r27_cards.json")
RUNS = os.path.join(BASE, "openday", "runs")

d = json.load(open(CARDS, encoding="utf-8"))
cards = d["cards"]

def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def card_html(c):
    b = "b1" if c["primary"] else "b2"
    bl = "一手" if c["primary"] else "二手"
    disp = c["url"].replace("https://", "").replace("http://", "")
    return (
        '<div class="hl">\n'
        '      <div class="top"><span class="emoji">{e}</span>'
        '<h3>{t}</h3><span class="cat">{cat}</span>'
        '<span class="badge {rc}">{rl}</span>'
        '<span class="badge {b}">{bl}</span></div>\n'
        '      <p class="val">{v}</p>\n'
        '      <details class="exec"><summary>怎么做</summary>'
        '<div class="inner">{h}</div></details>\n'
        '      <div class="src">\u2705 <a href="{u}" target="_blank">{disp}</a></div>\n'
        '      <div class="note">{n}</div>\n'
        '    </div>\n'
    ).format(e=esc(c["emoji"]), t=esc(c["title"]), cat=esc(c["cat"]),
             rc=c["rel_class"], rl=esc(c["rel_label"]), b=b, bl=bl,
             v=esc(c["value"]), h=esc(c["how"]), n=esc(c["note"]),
             u=esc(c["url"]), disp=esc(disp))

r2 = [c for c in cards if c["rel_class"] == "r2"]   # supervisor 10
r3 = [c for c in cards if c["rel_class"] == "r3"]   # exec 3
print("r2:", len(r2), "r3:", len(r3), "total:", len(cards))

# ---------- 1) Build standalone R28 increment page ----------
sec3_html = "".join(card_html(c) for c in r3)
sec2_html = "".join(card_html(c) for c in r2)
inc = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Open Day 开放日 · 第28轮补采（独立页）</title>
<style>
:root{{
  --bg:#f4f6fb; --card:#ffffff; --ink:#1f2430; --sub:#5b6478;
  --accent:#6c5ce7; --accent2:#00b8d9; --chip:#eef0ff;
}}
*{{box-sizing:border-box;margin:0;padding:0;}}
body{{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:linear-gradient(135deg,#eef1ff 0%,#e6f7ff 100%);color:var(--ink);padding:28px 18px;line-height:1.6;}}
.wrap{{max-width:1080px;margin:0 auto;}}
.hero{{background:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);border-radius:22px;padding:30px 32px;color:#fff;box-shadow:0 14px 40px rgba(108,92,231,.25);margin-bottom:22px;}}
.hero h1{{font-size:26px;font-weight:800;letter-spacing:1px;margin-bottom:8px;}}
.hero p{{font-size:14px;opacity:.95;}}
.relbar{{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px;}}
.relbar span{{background:rgba(255,255,255,.2);border-radius:20px;padding:5px 14px;font-size:13px;font-weight:600;}}
.back{{display:inline-block;margin:0 0 14px;font-size:13px;color:var(--accent2);text-decoration:none;font-weight:600;}}
.sec{{margin:30px 0 12px;display:flex;align-items:center;gap:10px;}}
.sec h2{{font-size:19px;font-weight:800;}}
.sec .tag{{font-size:12px;padding:4px 12px;border-radius:12px;font-weight:700;}}
.sec3 .tag{{background:#f3e8ff;color:#7b2cbf;}} .sec3 h2{{color:#7b2cbf;}}
.sec2 .tag{{background:#fff3e0;color:#c0651a;}} .sec2 h2{{color:#c0651a;}}
.sec1 .tag{{background:#eaf2ff;color:#2b6cb0;}} .sec1 h2{{color:#2b6cb0;}}
.sec .desc{{font-size:12.5px;color:var(--sub);margin-left:2px;}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;}}
.hl{{background:var(--card);border-radius:18px;padding:18px 18px 16px;border-top:4px solid var(--accent);box-shadow:0 10px 32px rgba(108,92,231,.10);display:flex;flex-direction:column;gap:9px;}}
.top{{display:flex;align-items:center;gap:8px;flex-wrap:wrap;}}
.emoji{{font-size:22px;}}
.hl h3{{font-size:16px;font-weight:700;flex:1;min-width:120px;}}
.cat{{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:600;background:var(--chip);color:var(--accent);}}
.badge{{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:700;}}
.b2{{background:#fff1e6;color:#c0651a;}}
.b1{{background:#e6f9ed;color:#1a9e5a;}}
.r1{{background:#eaf2ff;color:#2b6cb0;}}
.r2{{background:#fff3e0;color:#c0651a;}}
.r3{{background:#f3e8ff;color:#7b2cbf;}}
.val{{font-size:13.5px;color:var(--sub);}}
.exec{{margin-top:2px;border-top:1px dashed #e2e8f0;padding-top:8px;}}
.exec summary{{cursor:pointer;font-size:13px;font-weight:600;color:var(--accent);}}
.exec .inner{{font-size:13px;color:var(--sub);margin-top:6px;padding-left:4px;}}
.src{{font-size:12px;word-break:break-all;}}
.src a{{color:var(--accent2);text-decoration:none;}}
.note{{font-size:12px;color:#94a3b8;border-left:3px solid #e2e8f0;padding-left:8px;}}
footer{{text-align:center;padding:24px;color:#94a3b8;font-size:13px;border-top:1px solid #e2e8f0;margin-top:40px;}}
</style>
</head>
<body>
<div class="wrap">
  <div class="hero">
    <h1>\U0001F6AA Open Day 开放日 · 第28轮补采（独立页）</h1>
    <p>采集于 2026-08-26 ｜ 本轮新增 13 卡（③高管间 3 / ②上下级 10）｜ 六维评估 ｜ 一手/二手标注 ｜ 受众关系分层（仅②③，剔除①）｜ 累计总索引见 <a href="../openday.html" style="color:#fff;text-decoration:underline;">openday.html</a></p>
    <div class="relbar">
      <span>② 领导↔员工（上下级）</span>
      <span>③ 领导↔领导（高管间）</span>
    </div>
  </div>
  <div class="sec sec3">
    <h2>③ 领导↔领导（高管间，exec）</h2>
    <span class="tag">{n3} 卡</span>
  </div>
  <div class="grid">
{sec3_html}  </div>
  <div class="sec sec2">
    <h2>② 领导↔员工（上下级，supervisor）</h2>
    <span class="tag">{n2} 卡</span>
  </div>
  <div class="grid">
{sec2_html}  </div>

</div>
<footer style="text-align:center;padding:24px;color:#94a3b8;font-size:13px;border-top:1px solid #e2e8f0;margin-top:40px;">\U0001F4CC 本页由 yitong 沉淀整理 · 文化活动知识库</footer>
</body>
</html>
""".format(n3=len(r3), n2=len(r2), sec3_html=sec3_html, sec2_html=sec2_html)

os.makedirs(RUNS, exist_ok=True)
inc_path = os.path.join(RUNS, "openday-20260826-r28.html")
open(inc_path, "w", encoding="utf-8").write(inc)
print("WROTE increment:", inc_path, len(inc), "bytes, cards:", inc.count('<div class="hl"'))

# ---------- 2) Inject into summary openday.html ----------
s = open(SUM, encoding="utf-8").read()
assert s.count('<div class="hl"') == 207, "baseline changed! " + str(s.count('<div class="hl"'))

def grid_close(s, open_idx):
    i = s.find(">", open_idx) + 1
    depth = 1; j = i
    while j < len(s):
        if s.startswith("<div", j):
            depth += 1; j += 4
        elif s.startswith("</div>", j):
            depth -= 1; j += 6
            if depth == 0:
                return j
        else:
            j += 1
    return -1

# anchor: sec3 h2
h2s = [m.start() for m in re.finditer(r"<h2", s)]
sec3_h2 = h2s[1]
# sec3 region grid (first grid.open after sec3 h2)
grids = [m.start() for m in re.finditer(r'<div class="grid"', s)]
grid3 = next(g for g in grids if g > sec3_h2)
g3c = grid_close(s, grid3)

# Inject sec3 cards inside grid#3 (before its close) -> appends into 高管间 section
s = s[:g3c] + "".join(card_html(c) for c in r3) + s[g3c:]
# re-find sec3 h2 (unchanged, insertion was after it)
h2s = [m.start() for m in re.finditer(r"<h2", s)]
sec3_h2 = h2s[1]
# Inject sec2 cards as loose cards before sec3 h2 (inside sec2 section, matching neighbors)
s = s[:sec3_h2] + "".join(card_html(c) for c in r2) + s[sec3_h2:]

# ---------- 3) Update header tags ----------
s = re.sub(r'(<div class="sec sec2">.*?<span class="tag">)\d+ 卡(</span>)',
           r'\g<1>202 卡\g<2>', s, count=1, flags=re.S)
s = re.sub(r'(<div class="sec sec3">.*?<span class="tag">)\d+ 卡(</span>)',
           r'\g<1>30 卡\g<2>', s, count=1, flags=re.S)

# ---------- 4) Append 二十八轮 to hero (before hero closing </div>) ----------
hero_open = s.find('<div class="hero">')
hc = grid_close(s, hero_open)
seg = ("｜ 二十八轮补采 2026-08-26(+13，驻德使馆领事开放日/哈使馆走进中国开放日/"
       "驻澳部队军营开放/空军航空开放/工业园区政府开放日/河南联通客户开放日/"
       "国网云开放日/中石化公众开放日/余江残联开放日/崖西乡村振兴开放日·10② + "
       "包头政商早餐会/梅河口政企早餐会/中新商会CEO闭门圆桌·3③，12一手+1二手)")
s = s[:hc] + seg + s[hc:]

# sanity: no card lost
assert s.count('<div class="hl"') == 220, "card count mismatch " + str(s.count('<div class="hl"'))
assert s.count(">上下级<") == 202, "r2 mismatch " + str(s.count(">上下级<"))
assert s.count(">高管间<") == 30, "r3 mismatch " + str(s.count(">高管间<"))
open(SUM, "w", encoding="utf-8").write(s)
print("WROTE summary:", SUM, "cards:", s.count('<div class="hl"'),
      "r2:", s.count(">上下级<"), "r3:", s.count(">高管间<"))

# ---------- 5) Remove mislabeled local increment page ----------
mis = os.path.join(BASE, "openday", "openday-20260826.html")
if os.path.exists(mis):
    os.remove(mis)
    print("REMOVED mislabeled:", mis)
print("DONE")
