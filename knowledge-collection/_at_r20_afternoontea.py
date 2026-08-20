# -*- coding: utf-8 -*-
"""知识采集自动化 · 下午茶研讨 二十轮 enrich（2026-08-20）。
渲染增量页 + 追加累计墙 + 更新 index.json + Obsidian 笔记 + 00索引 + 推进指针。
仅 ②上下级 / ③高管间，0 peer。"""
import os, json, re

BASE = os.path.dirname(os.path.abspath(__file__))
AT_DIR = os.path.join(BASE, "afternoontea")
CUM = os.path.join(AT_DIR, "afternoontea.html")
IDX = os.path.join(BASE, "index.json")
DATE = "20260820"
RUN_NAME = "afternoontea-%s.html" % DATE
RUN_PATH = os.path.join(AT_DIR, RUN_NAME)
VAULT = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库"
NOTE = os.path.join(VAULT, "素材", "afternoontea", "下午茶研讨-知识卡汇总.md")
IDX00 = os.path.join(VAULT, "00-知识采集索引.md")
LAST = os.path.join(BASE, "last-topic.txt")
GP = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection"
WALL = GP + "/afternoontea/afternoontea.html"
ROUND_LABEL = "二十轮 enrich 2026-08-20(+6)"

# ---- 6 张新卡（仅 ②上下级 / ③高管间，0 peer）----
CARDS = [
    dict(emoji="🫖", title="清风茶室·廉政谈心谈话常态化", cat="廉政监督", rel="r2", rel_text="上下级",
         src="b1", src_text="一手",
         url="https://www.hnsjw.gov.cn/sitesources/hnsjct/page_pc/gzdt/dfzf/article5ad9a8081fab46ef80aa8fbfa35153c0.html",
         val="鹤壁市宝山经开区纪工委监察工委设「清风茶室」专用于谈心谈话：把监督关口前移、严在日常，邀党员干部喝茶道廉，直点痛处、亮明问题；首期即对综合办/党群/建设局等重点部门负责人谈话，近距离有原则接触，全面了解政治表现/能力绩效/作风并归入个人廉政档案，对苗头性问题提醒限期改正；强调常态化、因对象年龄性格差异采取不同谈话方式，让廉政意识入脑入心。核心：用「茶室+谈心」把廉政教育从会议室搬到轻松场景，治未病、防微杜渐。",
         how="做廉政/纪律谈心，别只在办公室严肃谈——设专属茶室营造松弛但有原则的场域，按岗位风险「量身定制」谈话提纲（提拔/节点/苗头分三类），谈话记录归入廉政档案、发现问题限期改；关键是常态化+分类谈，把「红脸出汗」做成日常监督而非运动式。",
         note="适用：② 纪检监察/组织部门对下级干部的日常监督谈心（上级监督者↔被监督干部，强权力距离、非朋友向）；把纪律教育做成可触达、可追踪的轻场景。",
         qual=5),
    dict(emoji="🍵", title="中鸿永信「倾诉茶吧」·合伙人轮值+全闭环心理疏导", cat="心理疏导", rel="r2", rel_text="上下级",
         src="b2", src_text="二手",
         url="https://js.news.cn/20260609/adcb981304ef4fbcb44cdb70d102ccda/c.html",
         val="江苏中鸿永信会计师事务所（110人）设「倾诉茶吧」作干群沟通+心理疏导阵地：每日固定时段开放、无会议式严肃，员工放顾虑畅言工作难题/生活困惑/发展建议；核心机制=合伙人轮值（管理人员以平等身份倾听记录）+全闭环（建议统一梳理专题研讨、办理结果公示反馈，事事有回音件件有着落）；累计开放数百场次、收集建议千余条、办结率超98%，据此优化流程/数字化/培训轮岗/后勤/心理疏导。",
         how="做员工心理疏导/建言平台，别只办一次性活动——设固定开放「茶吧」+合伙人轮值（管理层平等倾听，不居高临下）+强闭环（收集→研讨→公示→反馈，办结率量化），让「敢说话、愿建言」成常态；据建议改流程/后勤/心理支持，把关怀落到制度。",
         note="适用：② 中小机构/企业管理层对一线员工的心理疏压与建言闭环（合伙人↔员工，强信任不越界）；用轻场景把 EAP/民主管理做成日常。",
         qual=4),
    dict(emoji="🍽️", title="Credera 新人午餐会·对话而非独白", cat="新人融入", rel="r2", rel_text="上下级",
         src="b2", src_text="二手",
         url="https://www.credera.com/insights/life-at-credera-leadership-through-conversation-lunch-with-new-hires-leaders",
         val="咨询公司 Credera 在每位新人入职头几个月邀其与各业务线合伙人/高管共进午餐：只问两个问题——「入职首月最正的体验」「最想改进的一点」，合伙人追问并狂记笔记，后续跟进；强调领导是「对话而非独白」（引 HBR：聪明领导更像平等交谈而非自上而下命令）。价值=高层持续可及+新人被听见+把建议纳入改进，避免「一年一次动员大会」式走过场。",
         how="做新人融入，别只靠入职培训——设「合伙人/高管×新人午餐」，用 2 个开放式问题（最赞体验/最想改）引导对话、领导多听少说并现场记要点，会后真跟进；核心是「对话式领导」而非宣讲，让新人首月就感到高层可及。",
         note="适用：② 企业管理层对新入职员工的倾听式融入（高管↔新人，尊重不施压）；把「领导可及」做成入职头 90 天的固定动作。",
         qual=4),
    dict(emoji="☕", title="EXL「Coffee with CEO」降低应届流失 45%", cat="留才对话", rel="r2", rel_text="上下级",
         src="b2", src_text="二手",
         url="https://www.markivis.com/blog/from-attrition-to-connection-how-exl-cut-early-career-turnover-by-45/",
         val="EXL 针对早期员工高流失（声音不被听/与高层隔绝/目标脱节）设计「Coffee with CEO」：15-20 名应届/入门员工与 CEO 小规模围坐，聊工作挑战/组织优先级/个人职业目标；设计要点=公平普惠（Noida/Gurgaon 两办轮换、先到先得、限重复参与让更多人见到 CEO）。结果=早期职业流失率降 45%，把层级换成人情连接、给难得发声平台并「人性化领导层」。",
         how="降应届/早期流失，别只加薪——做「CEO×小批新人咖啡」，15-20人/场、公平轮换+限重复参与保覆盖；聊真实挑战与目标而非宣讲；用低成本高频连接补「高层可及性缺口」，让人留因为被看见。",
         note="适用：② 企业 CEO/高管对应届与一线新人的留才对话（高管↔新人，强可及性）；用可量化结果（流失-45%）证明「咖啡」胜过宣讲。",
         qual=4),
    dict(emoji="🤝", title="国金证券「转型临界点」上市公司董事长闭门会", cat="董事长闭门", rel="r3", rel_text="高管间",
         src="b2", src_text="二手",
         url="https://m.cls.cn/share/article/2312164?sv=846&os=web",
         val="国金证券主办「转型临界点」上市公司董事长闭门会（成都）：主题「智改数转·科技革命与增长跃迁」，国金董事长/所长/首席经济学家与 60 家上市及拟上市企业董事长、总经理、核心高管闭门，围绕前沿科技探索与落地应用深度交流；四川省上市公司协会支持。定位=券商以产业研究+资源对接+综合金融服务，陪伴企业从技术突破到生态构建，共建产业新生态。",
         how="办高管闭门会，别只请大咖站台——由券商/机构做「主办方+连接者」，定「智改数转/增长跃迁」等硬议题，邀同层级董事长/总经理小范围闭门、重落地对话而非致辞；用研究+资本资源做持续陪伴，把单次会做成产业生态入口。",
         note="适用：③ 券商/机构主办、面向上市公司董事长/总经理的闭门茶叙（高管↔高管，专业/共同目标切入，避免幼稚社交）；把行业痛点变同侪共识。",
         qual=4),
    dict(emoji="🏛️", title="2026 CGF 中国董事CEO闭门交流会议", cat="行业CEO闭门", rel="r3", rel_text="高管间",
         src="b2", src_text="二手",
         url="https://bain.cn/news_info.php?id=2121",
         val="消费品论坛（CGF）主办、京东承办、贝恩支持的「2026 CGF 中国董事CEO闭门交流会议」：18 家全球及本土头部消费品/零售 CEO + 近 70 位高管闭门，围绕「零供协作」与「AI 破局」高质量对话；CEO 们共识从价格/流量消耗战转向以消费者价值创造与品类渗透为核心的协同创新，贝恩建议把共同洞察—联合创新—柔性供给—数据共享机制化。价值=以 CEO 层前瞻视野凝聚行业共识、跳出消耗式竞争。",
         how="办行业 CEO 闭门，别搞成发布会——由行业协会/咨询牵头、头部企业 CEO 小范围闭门，定「零供协作/AI 破局」等真议题，引导从消耗战转向价值共创；把共识落成标准共建/数据互联/创新共创的可执行项目，让闭门产出行业级杠杆。",
         note="适用：③ 行业协会/咨询机构主办的跨企业 CEO 闭门（高管↔高管，以行业战略/共同挑战切入）；把同侪对话变机制化协同。",
         qual=4),
]

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def card_html(c, indent=4):
    sp = " " * indent; sp2 = " " * (indent + 2)
    rel_badge = '<span class="badge %s">%s</span>' % (c["rel"], c["rel_text"])
    src_badge = '<span class="badge %s">%s</span>' % (c["src"], c["src_text"])
    return (
        '%s<div class="hl">\n' % sp
        + '%s<div class="top"><span class="emoji">%s</span><h3>%s</h3><span class="cat">%s</span>%s%s</div>\n'
          % (sp2, esc(c["emoji"]), esc(c["title"]), esc(c["cat"]), rel_badge, src_badge)
        + '%s<p class="val">%s</p>\n' % (sp2, esc(c["val"]))
        + '%s<details class="exec"><summary>怎么做</summary><div class="inner">%s</div></details>\n' % (sp2, esc(c["how"]))
        + '%s<div class="src">🔗 <a href="%s" target="_blank">%s</a></div>\n' % (sp2, esc(c["url"]), esc(c["url"]))
        + '%s<div class="note">%s</div>\n' % (sp2, esc(c["note"]))
        + '%s</div>\n' % sp
    )

sec3_cards = [c for c in CARDS if c["rel"] == "r3"]
sec2_cards = [c for c in CARDS if c["rel"] == "r2"]
grid_html = "".join(card_html(c) for c in CARDS)
rel_summary = "③高管间 %d 张 + ②上下级 %d 张" % (len(sec3_cards), len(sec2_cards))

# ---------- 1) 增量页 ----------
inc_title = "下午茶研讨 · 二十轮增量卡片（2026-08-20）"
INC = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>@@TITLE@@</title>
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
<p style="margin:0 0 16px"><a href="@@WALL@@" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">🍵 返回下午茶累计卡片墙 →</a> &nbsp; <a href="@@PORTAL@@" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">📚 返回知识库门户 →</a></p>
  <div class="hero">
    <h1>🍵 @@TITLE@@</h1>
    <p>本轮新增 @@N@@ 张（通过六维评估，剔除平级/朋友向①，仅 ②上下级 / ③高管间）；关系档：@@RELSUM@@。</p>
    <div class="relbar">
      <span>② 领导↔员工（上下级，supervisor）</span>
      <span>③ 领导↔领导（高管间，exec）</span>
    </div>
  </div>
  <div class="grid">
@@GRID@@  </div>
<footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>
</div>
</body></html>
'''.replace("@@TITLE@@", inc_title).replace("@@N@@", str(len(CARDS))).replace("@@RELSUM@@", rel_summary) \
   .replace("@@WALL@@", WALL).replace("@@PORTAL@@", GP + "/index.html").replace("@@GRID@@", grid_html)

with open(RUN_PATH, "w", encoding="utf-8") as f:
    f.write(INC)
inc_size = os.path.getsize(RUN_PATH)
print("增量页:", RUN_PATH, inc_size, "字节")

# ---------- 2) 追加累计墙（balanced-div 插入）----------
def find_grid_close(h, sec_start):
    gi = h.find('<div class="grid">', sec_start)
    assert gi != -1, "grid not found"
    depth = 0; i = gi + len('<div class="grid">')
    while i < len(h):
        if h.startswith('<div', i):
            depth += 1; i = h.find('>', i) + 1
        elif h.startswith('</div>', i):
            if depth == 0:
                return i
            depth -= 1; i += 5
        else:
            i += 1
    raise RuntimeError("unbalanced")

html = open(CUM, encoding="utf-8").read()
i3 = html.find('class="sec sec3"'); close3 = find_grid_close(html, i3)
html = html[:close3] + "".join(card_html(c) for c in sec3_cards) + html[close3:]
i2 = html.find('class="sec sec2"'); close2 = find_grid_close(html, i2)
html = html[:close2] + "".join(card_html(c) for c in sec2_cards) + html[close2:]

# hero 时间线
hero_old = "十九轮 enrich 2026-08-19(+12)"
hero_new = hero_old + " ｜ " + ROUND_LABEL
assert hero_old in html, "hero timeline marker not found"
html = html.replace(hero_old, hero_new, 1)

with open(CUM, "w", encoding="utf-8") as f:
    f.write(html)
new_cards = html.count('class="hl"'); r2 = html.count('badge r2'); r3 = html.count('badge r3')
footer_ok = "📌 本页由 yitong" in html
print("累计墙卡片数:", new_cards, "| r2:", r2, "r3:", r3, "| footer:", footer_ok)

# ---------- 3) index.json（dedup by URL）----------
data = json.load(open(IDX, encoding="utf-8"))
existing_urls = {e.get("url", "").lower().rstrip("/") for e in data}
before = len(data); added = 0
for c in CARDS:
    u = c["url"].lower().rstrip("/")
    if u in existing_urls:
        print("SKIP dup url:", u); continue
    data.append(dict(
        title=c["title"], normKey=c["title"], url=c["url"],
        sourceType="secondary" if c["src"] == "b2" else "primary",
        relation="exec" if c["rel"] == "r3" else "supervisor",
        summary=c["cat"] + "：" + c["val"][:60],
    ))
    added += 1
json.dump(data, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("index.json:", before, "->", len(data), "(+%d)" % added)

# ---------- 4) Obsidian 笔记（动态计数）----------
t = open(NOTE, encoding="utf-8").read()
m = re.search(r'（(\d+) 卡 · 上下级/高管间）', t); tot = int(m.group(1))
t = t.replace('（%d 卡 · 上下级/高管间）' % tot, '（%d 卡 · 上下级/高管间）' % (tot + len(CARDS)), 1)
m3 = re.search(r'③.*?— (\d+) 卡', t); r3n = int(m3.group(1))
t = t.replace('— %d 卡' % r3n, '— %d 卡' % (r3n + len(sec3_cards)), 1)
m2 = re.search(r'②.*?— (\d+) 卡', t); r2n = int(m2.group(1))
t = t.replace('— %d 卡' % r2n, '— %d 卡' % (r2n + len(sec2_cards)), 1)
# 叙述累计行
nm = re.search(r'累计 (\d+) 卡（③高管间 (\d+) / ②上下级 (\d+)，[^）]*；一手 (\d+) \+ 二手 (\d+)）', t)
ct, c3, c2, b1, b2 = map(int, nm.groups())
new_b1 = b1 + sum(1 for c in CARDS if c["src"] == "b1")
new_b2 = b2 + sum(1 for c in CARDS if c["src"] == "b2")
t = t.replace(nm.group(0), '累计 %d 卡（③高管间 %d / ②上下级 %d，含 5 张跨档双标；一手 %d + 二手 %d）'
              % (ct + len(CARDS), c3 + len(sec3_cards), c2 + len(sec2_cards), new_b1, new_b2), 1)
# 轮次小节（插在 ## ③ 之前）
marker3 = "## ③"
assert marker3 in t
round_sec = (
    "\n## 轮次 2026-08-20（+%d）\n\n" % len(CARDS)
    + "> 二十轮 enrich：新增 %d 卡（③ 高管间 +%d：%s；② 上下级 +%d：%s）。无 peer，relation 仅取 supervisor/exec。\n"
      % (len(CARDS), len(sec3_cards), " / ".join(c["title"] for c in sec3_cards),
         len(sec2_cards), " / ".join(c["title"] for c in sec2_cards))
    + "> 线上预览：%s ｜ 本轮增量页：%s\n\n" % (WALL, GP + "/afternoontea/" + RUN_NAME)
)
t = t.replace(marker3, round_sec + marker3, 1)
# ③ 表追加（在 ## ② 之前）
sec3_text = t.split("## ③")[1].split("## ②")[0]
max3 = max([int(x) for x in re.findall(r'^\|\s*(\d+)\s*\|', sec3_text, re.M)] or [0])
rows3 = ""
for i, c in enumerate(sec3_cards):
    max3 += 1
    rows3 += "| %d | %s | %s | %s |\n" % (max3, c["title"], c["src_text"], c["val"])
t = t.replace("## ②", rows3 + "\n## ②", 1)
# ② 表追加（文件末尾）
sec2_text = t.split("## ②")[1]
max2 = max([int(x) for x in re.findall(r'^\|\s*(\d+)\s*\|', sec2_text, re.M)] or [0])
rows2 = ""
for c in sec2_cards:
    max2 += 1
    rows2 += "| %d | %s | %s | %s |\n" % (max2, c["title"], c["src_text"], c["val"])
t = t.rstrip("\n") + "\n" + rows2
open(NOTE, "w", encoding="utf-8").write(t)
print("Obsidian 笔记已更新:", NOTE)

# ---------- 5) 00-索引（动态计数）----------
i = open(IDX00, encoding="utf-8").read()
# 头部追加轮次
h_old = "十九轮 enrich 2026-08-19(+12)）"
h_new = "十九轮 enrich 2026-08-19(+12) ｜ " + ROUND_LABEL + "）"
assert h_old in i, "00 header marker not found"
i = i.replace(h_old, h_new, 1)
# 计数
im = re.search(r'\*\*(\d+) 卡\*\*', i); itot = int(im.group(1))
i = i.replace('**%d 卡**' % itot, '**%d 卡**' % (itot + len(CARDS)), 1)
im2 = re.search(r'一手 (\d+) \+ 二手 (\d+)', i)
i = i.replace('一手 %d + 二手 %d' % (int(im2.group(1)), int(im2.group(2))),
              '一手 %d + 二手 %d' % (int(im2.group(1)) + sum(1 for c in CARDS if c["src"]=="b1"),
                                     int(im2.group(2)) + sum(1 for c in CARDS if c["src"]=="b2")), 1)
ispl = re.search(r'③高管间\(\.\.\.\) (\d+) 卡 / ②上下级\(\.\.\.\) (\d+) 卡', i)
i = i.replace('③高管间(...) %d 卡 / ②上下级(...) %d 卡' % (int(ispl.group(1)), int(ispl.group(2))),
              '③高管间(...) %d 卡 / ②上下级(...) %d 卡' % (int(ispl.group(1)) + len(sec3_cards),
                                                          int(ispl.group(2)) + len(sec2_cards)), 1)
# 叙述行追加二十轮描述
nineteen = "十九轮 enrich 新增（③内江「甜城下午茶」制度化政企纾困"
assert nineteen in i, "十九轮 narrative not found"
tw_line = ("二十轮 enrich 新增（③国金证券「转型临界点」上市公司董事长闭门会 / ③2026 CGF 中国董事CEO闭门交流会议；"
           "②清风茶室·廉政谈心谈话常态化 / ②中鸿永信「倾诉茶吧」·合伙人轮值+全闭环心理疏导 / "
           "②Credera 新人午餐会·对话而非独白 / ②EXL「Coffee with CEO」降低应届流失 45%）。")
i = i.replace(nineteen, nineteen + "\n" + tw_line, 1)
# 表格追加 6 行（在下一个 ## 主题： 之前）
anchor = i.find("## 主题：", i.find("## 主题：下午茶研讨") + 10)
rows = ""
for c in CARDS:
    rel = "③高管间" if c["rel"]=="r3" else "②上下级"
    rows += "| %s（afternoontea.html） | %d | %s | %s | %s |\n" % (
        c["title"], c["qual"], c["src_text"], rel, c["note"].replace("适用：", ""))
i = i[:anchor] + rows + "\n" + i[anchor:]
open(IDX00, "w", encoding="utf-8").write(i)
print("00-索引已更新:", IDX00)

# ---------- 6) 推进指针 ----------
order = ["员工大会", "Offsite", "破冰", "颁奖", "Open Day", "下午茶研讨"]
cur = open(LAST, encoding="utf-8").read().strip()
idx = order.index(cur); nxt = order[(idx + 1) % len(order)]
open(LAST, "w", encoding="utf-8").write(nxt + "\n")
print("last-topic.txt:", cur, "->", nxt)

print("\n=== 运行摘要 ===")
print("本次主题：下午茶研讨（二十轮 enrich 2026-08-20）")
print("覆盖关系档：仅 ②上下级(%d) / ③高管间(%d)，0 peer" % (len(sec2_cards), len(sec3_cards)))
print("新增 N=%d，去重删 M=%d" % (added, len(CARDS) - added))
print("增量页：", RUN_PATH)
print("汇总页：", CUM)
print("DONE")
