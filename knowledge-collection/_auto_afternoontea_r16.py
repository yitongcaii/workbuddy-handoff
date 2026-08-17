# -*- coding: utf-8 -*-
"""下午茶研讨 十六轮 enrich (2026-08-17) — 渲染增量页 + 追加进累计墙 + 更新 index.json"""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
AT_DIR = os.path.join(BASE, "afternoontea")
CUM = os.path.join(AT_DIR, "afternoontea.html")
IDX = os.path.join(BASE, "index.json")
DATE = "20260817"
ROUND = "十六轮 enrich 2026-08-17(+4)"

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---- 本轮新增卡（仅 ②上下级 / ③高管间，0 peer；4张全 NEW，URL 均未在 index.json 命中）----
CARDS = [
    {
        "emoji": "🌍",
        "title": "跨文化咖啡仪式·把咖啡做成「文化桥梁」溶解层级",
        "cat": "多元融合",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "结构化文化咖啡仪式（埃塞俄比亚 Buna 三巡手冲 / 瑞典 Fika 定时暂停 / 土耳其咖啡占卜叙旧）作为多元团队融合工具：研究指结构化仪式比随意茶歇更能建立连接——参与同事文化仪式的员工 77% 更欣赏职场多样性，层级壁垒在仪式中暂时溶解。四要素 = 专属文化空间（不靠豪华改造，用心意）+ 固定时段（不可随意占用）+ 文化讲解（讲清由来与礼仪）+ 领导以「学习者」而非「权威」身份参与，制造心理安全。",
        "how": "办多元/跨国团队茶歇时，别只备咖啡——把某一种文化仪式做成固定栏目（如每月一期「某国咖啡/茶仪式」），请该文化背景同事当主讲；领导坐下来当学生；固定时段、免手机、讲清礼仪。把茶歇从「摸鱼时间」升级为「文化桥梁」，尤其适合外籍/跨地同事多的团队。",
        "url": "https://www.coffeeoncue.com.au/blogs/workplace-experience/cultural-coffee-ceremonies-boost-workplace-connection-productivity",
        "note": "适用：② 多元/跨国团队主管，用仪式化茶歇溶解层级、提升包容（③ 全球高管跨文化领导可借同一逻辑）。",
    },
    {
        "emoji": "🔀",
        "title": "并购变革期 tea time·跨部门破壁+员工随时找老总",
        "cat": "变革沟通",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "惠普中国与康柏合并动荡期，总裁孙振耀发起 tea time：小规模跨部门（财务×行政、行政×销售、销售×技术）10 人左右、2 小时、每月 1-2 次；员工可随时找老总谈；专设「金狮奖」表彰推动跨部门交流的员工。用非正式场景稳定合并期人心、打破部门墙、让员工敢于提意见，而不是只靠邮件和全员大会。",
        "how": "组织合并/重组/转型期，别只靠邮件和大会——设固定 tea time 让不同部门小范围混坐，领导在场但不主导；允许员工随时约老总聊；设小奖激励「主动跨部门交流」的人。把焦虑情绪从正式会议引流到茶桌，先稳住人再谈变革。",
        "url": "https://down1.tech.sina.com.cn/it/m/2002-11-20/1240151024.shtml",
        "note": "适用：② 变革期 leader/HR，用茶歇当「稳定军心+破部门墙」的缓冲带（非日常倾听，专治合并重组动荡）。",
    },
    {
        "emoji": "☕",
        "title": "全球领导者咖啡文化·跨文化领导拉平层级",
        "cat": "跨文化领导",
        "rel": "r3", "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "全球领导者视角——巴西 Cafézinho（关系黏合剂，信任在保温壶旁建立，跳过寒暄=失礼）/ 瑞典 Fika（定时民主仪式，CEO 与新人同席分肉桂卷，层级在此拉平、最佳点子胜出）/ 法国 Pause Café（正式会议前的战略辩论场，真决策常在咖啡机旁先定）。同一杯咖啡，在不同文化里是关系、是平等、是决策。",
        "how": "管跨国/多元团队的高管，先把「咖啡/茶」当战略触点而非休息：在关系型文化（巴西/印度）先聊人再聊事；在平等型文化（瑞典）用固定咖啡仪式拉平层级、听见一线；在分析型文化（法国）把非正式咖啡当战略预对齐场。别用「效率优先」一刀切毁掉文化 bonding。",
        "url": "https://www.linkedin.com/pulse/coffee-break-theory-beyond-caffeine-global-career-mendes-zeni-pmp--vqsif",
        "note": "适用：③ 跨国/全球高管，把咖啡仪式用作跨文化领导与拉平层级的杠杆（与②团队文化桥梁互补，视角在 leader 决策层）。",
    },
    {
        "emoji": "🏛️",
        "title": "独立董事南京会客厅·治理层闭门茶叙圈层",
        "cat": "治理层圈层",
        "rel": "r3", "rel_text": "高管间",
        "src": "b1", "src_text": "一手",
        "val": "《董事会》杂志「独立董事南京会客厅」：18 位上市公司独董（代表近 60 家）闭门沙龙，围绕新规下独董履职与风险应对热烈讨论；定位「独董之家」，群聚独董群体、共建交流平台，共同防范履职风险、促进规范运作。把监管压力下的同侪困惑，变成闭门茶叙里的经验互换。",
        "how": "做治理/合规圈层运营时，参考「会客厅」模式——定向邀约同层级（如独董/董秘/CFO）小范围闭门，议题紧扣当下监管痛点，由专业媒体/协会背书增信；茶叙降低姿态、提升坦诚，让同侪敢讲真问题。适合作为高管治理圈层的固定载体。",
        "url": "https://www.163.com/dy/article/KELQNCDD0530IE6O.html",
        "note": "适用：③ 治理层/董秘/合规高管，闭门茶叙式同侪圈层（非对外，纯治理层私密交流）。",
    },
]

def card_html(c, indent=4):
    sp = " " * indent
    sp2 = " " * (indent + 2)
    rel_badge = f'<span class="badge {c["rel"]}">{c["rel_text"]}</span>'
    src_badge = f'<span class="badge {c["src"]}">{c["src_text"]}</span>'
    return (
        f'{sp}<div class="hl">\n'
        f'{sp2}<div class="top"><span class="emoji">{esc(c["emoji"])}</span>'
        f'<h3>{esc(c["title"])}</h3><span class="cat">{esc(c["cat"])}</span>'
        f'{rel_badge}{src_badge}</div>\n'
        f'{sp2}<p class="val">{esc(c["val"])}</p>\n'
        f'{sp2}<details class="exec"><summary>怎么做</summary><div class="inner">{esc(c["how"])}</div></details>\n'
        f'{sp2}<div class="src">🔗 <a href="{esc(c["url"])}" target="_blank">{esc(c["url"])}</a></div>\n'
        f'{sp2}<div class="note">{esc(c["note"])}</div>\n'
        f'{sp}</div>\n'
    )

# ---- 增量页 ----
cards_sec3 = [c for c in CARDS if c["rel"] == "r3"]
cards_sec2 = [c for c in CARDS if c["rel"] == "r2"]
grid_html = "".join(card_html(c) for c in CARDS)
rel_summary = f"③高管间 {len(cards_sec3)} 张 + ②上下级 {len(cards_sec2)} 张"

inc_title = f"下午茶研讨 · 十六轮增量卡片（2026-08-17）"
wall_url = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/afternoontea/afternoontea.html"
portal_url = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/index.html"

INC = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{inc_title}</title>
<style>
:root{{--bg:#f4f6fb;--card:#ffffff;--ink:#1f2430;--sub:#5b6478;--accent:#6c5ce7;--accent2:#00b8d9;--chip:#eef0ff;}}
*{{box-sizing:border-box;margin:0;padding:0;}}
body{{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:linear-gradient(135deg,#eef1ff 0%,#e6f7ff 100%);color:var(--ink);padding:28px 18px;line-height:1.6;}}
.wrap{{max-width:1080px;margin:0 auto;}}
.hero{{background:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);border-radius:22px;padding:26px 30px;color:#fff;box-shadow:0 14px 40px rgba(108,92,231,.25);margin-bottom:22px;}}
.hero h1{{font-size:24px;font-weight:800;letter-spacing:1px;margin-bottom:6px;}}
.hero p{{font-size:13px;opacity:.95;}}
.relbar{{display:flex;gap:10px;flex-wrap:wrap;margin-top:12px;}}
.relbar span{{background:rgba(255,255,255,.2);border-radius:20px;padding:5px 14px;font-size:13px;font-weight:600;}}
.grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;}}
.hl{{background:var(--card);border-radius:18px;padding:18px 18px 16px;border-top:4px solid var(--accent);box-shadow:0 10px 32px rgba(108,92,231,.10);display:flex;flex-direction:column;gap:9px;}}
.top{{display:flex;align-items:center;gap:8px;flex-wrap:wrap;}}
.emoji{{font-size:22px;}}
.hl h3{{font-size:16px;font-weight:700;flex:1;min-width:120px;}}
.cat{{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:600;background:var(--chip);color:var(--accent);}}
.badge{{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:700;}}
.b2{{background:#fff1e6;color:#c0651a;}}
.b1{{background:#e6f9ed;color:#1a8c4a;}}
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
</head><body>
<div class="wrap">
<p style="margin:0 0 16px"><a href="{wall_url}" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">🍵 返回下午茶累计卡片墙 →</a> &nbsp; <a href="{portal_url}" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">📚 返回知识库门户 →</a></p>
  <div class="hero">
    <h1>🍵 {inc_title}</h1>
    <p>本轮新增 {len(CARDS)} 张（通过六维评估，剔除平级/朋友向①，仅 ②上下级 / ③高管间）；关系档：{rel_summary}。</p>
    <div class="relbar">
      <span>② 领导↔员工（上下级，supervisor）</span>
      <span>③ 领导↔领导（高管间，exec）</span>
    </div>
  </div>
  <div class="grid">
{grid_html}  </div>
<footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>
</div>
</body></html>
"""

inc_path = os.path.join(AT_DIR, f"afternoontea-{DATE}.html")
with open(inc_path, "w", encoding="utf-8") as f:
    f.write(INC)
inc_size = os.path.getsize(inc_path)
print("增量页:", inc_path, inc_size, "字节")

# ---- 追加进累计墙（balanced-div 插入）----
def find_grid_close(h, sec_start):
    # 从 sec_start 起找第一个 <div class="grid">，再平衡括号找其闭合 </div>
    gi = h.find('<div class="grid">', sec_start)
    assert gi != -1, "grid not found"
    depth = 0
    i = gi + len('<div class="grid">')
    while i < len(h):
        if h.startswith('<div', i):
            depth += 1
            i = h.find('>', i) + 1
        elif h.startswith('</div>', i):
            if depth == 0:
                return i  # 返回 '</div>' 起始位置
            depth -= 1
            i += 5
        else:
            i += 1
    raise RuntimeError("unbalanced")

html = open(CUM, encoding="utf-8").read()

# r3 卡插入 sec3 的 grid 闭合前
i3 = html.find('class="sec sec3"')
close3 = find_grid_close(html, i3)
card3_html = "".join(card_html(c) for c in cards_sec3)
html = html[:close3] + card3_html + html[close3:]

# r2 卡插入 sec2 的 grid 闭合前（重新定位，因 html 已变长）
i2 = html.find('class="sec sec2"')
close2 = find_grid_close(html, i2)
card2_html = "".join(card_html(c) for c in cards_sec2)
html = html[:close2] + card2_html + html[close2:]

# 更新 hero 时间线
hero_old = "十五轮 enrich 2026-08-16(+7)</p>"
hero_new = "十五轮 enrich 2026-08-16(+7)｜ 十六轮 enrich 2026-08-17(+4)</p>"
assert hero_old in html, "hero timeline marker not found"
html = html.replace(hero_old, hero_new, 1)

with open(CUM, "w", encoding="utf-8") as f:
    f.write(html)

# 校验
new_cards = html.count('class="hl"')
r2 = html.count('badge r2')
r3 = html.count('badge r3')
footer_ok = "📌 本页由 yitong" in html
print("累计墙卡片数:", new_cards, "| r2:", r2, "r3:", r3, "| footer:", footer_ok)

# ---- 更新 index.json ----
def normkey(t):
    out = []
    for ch in t.lower():
        if ch.isalnum() or "一" <= ch <= "鿿":
            out.append(ch)
    return "".join(out)

data = json.load(open(IDX, encoding="utf-8"))
existing_urls = {e.get("url", "").lower().rstrip("/") for e in data}
added = 0
for c in CARDS:
    u = c["url"].lower().rstrip("/")
    if u in existing_urls:
        print("SKIP dup url:", u)
        continue
    rel_map = {"r2": "supervisor", "r3": "exec"}
    entry = {
        "title": c["title"],
        "normKey": normkey(c["title"]),
        "url": c["url"],
        "sourceType": "secondary" if c["src"] == "b2" else "primary",
        "relation": rel_map[c["rel"]],
        "summary": c["cat"] + "：" + c["val"][:60],
    }
    data.append(entry)
    added += 1
print("index.json 新增:", added, "-> 现", len(data), "条")
json.dump(data, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

# 写出卡片数据供后续 Obsidian / 乐享步骤复用
meta = {
    "date": DATE, "round": ROUND, "inc_path": inc_path, "inc_size": inc_size,
    "added": added, "cards": CARDS,
    "wall_url": wall_url, "prev_total": 96, "new_total": new_cards,
}
json.dump(meta, open(os.path.join(BASE, "_afternoontea_r16_meta.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("meta 已写出")
