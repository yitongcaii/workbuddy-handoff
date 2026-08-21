# -*- coding: utf-8 -*-
"""下午茶研讨 二十二轮补采 (2026-08-21) — 渲染增量 + 追加进累计墙 + 更新 index.json + Obsidian + 乐享上传
仅 ②上下级 / ③高管间，0 peer。"""
import json, os, re, urllib.request, urllib.error

BASE = os.path.dirname(os.path.abspath(__file__))
AT_DIR = os.path.join(BASE, "afternoontea")
CUM = os.path.join(AT_DIR, "afternoontea.html")
IDX = os.path.join(BASE, "index.json")
DATE = "20260821"
RUN_NAME = "afternoontea-20260821.html"
RUN_PATH = os.path.join(AT_DIR, RUN_NAME)

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---- 本轮新增卡（仅 ②上下级 / ③高管间，0 peer；7张全 NEW，URL 均未命中 index/wall）----
CARDS = [
    {
        "emoji": "\U0001F3E6",
        "title": "建行兴安分行党委书记\u201c一对一\u201d访谈·下沉基层全覆盖",
        "cat": "领导谈心",
        "rel": "r2", "rel_text": "上下级",
        "src": "b1", "src_text": "一手",
        "val": "建设银行兴安分行党委书记、行长王晓霞带头，党委班子全员参与，以\u201c一对一\u201d访谈方式与基层员工谈心谈话，实现访谈全覆盖。围绕\u201c未来规划/月收入/年休假/困难/建议\u201d等，与一线和机关员工逐一促膝长谈，听真话、察实情、解难题；现场解决温水供应等具体问题，不能马上解决的明确期限，确保\u201c凡事有交代、件件有着落、事事有回音\u201d，全部问题已解决、合理化建议全采纳。",
        "how": "做 leadership 下沉谈心，学建行\u201c一把手带头+班子全覆盖+一对一促膝\u201d：用具体问题（规划/收入/休假/困难）代替空泛关怀，现场能解的现场解、不能解的明期限；核心是\u201c件件有回音\u201d的闭环，让基层感到被真正看见而非走过场。",
        "url": "https://www.northnews.cn/p/2359976",
        "note": "适用：② 党委书记/行领导 × 基层一线员工（官方报道一手案例；一把手下沉全覆盖谈心 + 闭环回音，可作金融/大企业民主管理范本）。",
    },
    {
        "emoji": "\U0001F33F",
        "title": "苏州园林集团经营层与业务骨干深度谈心谈话",
        "cat": "经营层沟通",
        "rel": "r2", "rel_text": "上下级",
        "src": "b1", "src_text": "一手",
        "val": "苏州园林集团于2月12日起开展经营层与各部门业务骨干谈心谈话，采取双向互动、面对面方式，围绕五大维度：回顾成绩与不足、新一年计划与目标、管理问题与团队凝聚力、职业发展规划、对公司战略/管理的建议。领导班子与骨干深度沟通，员工敞开心扉提真实想法，领导耐心解答、谈透谈深，汇聚发展合力。",
        "how": "做经营层×骨干沟通，学苏州园林\u201c五大维度框架+双向面对面\u201d：不只谈工作，也谈个人成长与公司战略；领导耐心解答而非单向宣讲，把谈心变成\u201c信息+情感\u201d双重交融；适合年度开局（春节后）统一思想、凝聚合力。",
        "url": "https://www.szyljt.com/groupDynamics/media/2025-03-12/1361.html",
        "note": "适用：② 经营层/高管 × 业务骨干（企业官方一手案例；五维谈心框架 + 年度开局凝聚，可作中层骨干深度沟通范本）。",
    },
    {
        "emoji": "\U0001F91D",
        "title": "台茂精机新员工茶话会·总经理现身破冰倾听",
        "cat": "新人融入",
        "rel": "r2", "rel_text": "上下级",
        "src": "b1", "src_text": "一手",
        "val": "台茂精机召开新员工茶话会，通过聊天互动帮新人熟悉团队、解答入职疑问、在破冰中发掘潜力。公司领导与新员工面对面，总经理刘应省出席并分享自身经历：\u201c公司是大家的坚强后盾，困难随时找我或管理层\u201d；新员工逐一自我介绍破冰，领导关心状态、答疑解惑。一场茶话会成心与心的连接。",
        "how": "办新人茶话会，学台茂：总经理/高管亲自出席+用自身经历鼓舞（而非只让HR主持），现场答疑+明确\u201c门常开\u201d承诺；用自我介绍破冰+茶点降拘谨，让新人首月就被看见、被托住。关键是领导\u201c在场\u201d而非 delegation。",
        "url": "http://www.taimaocnc.com/News-123682.html",
        "note": "适用：② 公司领导/总经理 × 新入职员工（企业官方一手案例；高管现身破冰 + 承诺可及，新人融入范本）。",
    },
    {
        "emoji": "\U0001F504",
        "title": "沃尔玛式越级沟通·二八倾听法则",
        "cat": "越级沟通",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "沃尔玛总裁萨姆·沃尔顿名言：\u201c若把沃尔玛管理浓缩成一种思想，就是越级沟通。\u201d越级沟通（非越级指挥）是了解组织、促内部互通的良药。下属在越级面谈中常因上级威严说假话，故高管应主动约员工、把会面安排在岗位旁/休息室/食堂等放松处，以聊天形式、多用\u201c请教/分享\u201d让对方感平等；并遵循二八法则——80%时间听、20%说，用说话时间问问题/补充/赞美。认真记录评价与建议回传用人部门。",
        "how": "做越级沟通，学沃尔玛\u201c主动约+放松场景+二八倾听\u201d：把面谈放食堂/休息室降防御，多用请教语气；高管严守二八法则（听8说2），用说话时间提问而非演讲；面谈记录回传直线经理，既评人 also 查流程漏。避免把越级面谈变个人秀。",
        "url": "https://media.workercn.cn/sites/media/lnzgb/2013_12/06/GR0512.htm",
        "note": "适用：② 高管/中层 leader 做越级沟通倾听（中工网方法论二手；二八法则 + 放松场景，与 Range/super-intern skip-level 议程互补）。",
    },
    {
        "emoji": "\U0001F465",
        "title": "CEO 同侪顾问小组·保密决策压力测试（Vistage/EO/Helix）",
        "cat": "高管同侪",
        "rel": "r3", "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "CEO 同侪小组由 6-12 位非竞争 CEO 每月在绝对保密下聚会，压力测试\u201c公司内部无人可核\u201d的决策。典型形式：每位带一个真实决策，全员先问清问题再给建议，呈现者最后发言；Vistage（1957，付费主席主持，12-16人/月/全天）、EO Forum（1987，成员主持，Gestalt 协议禁建议、只分享亲身经历）、Helix（2024，无主席、百席上限）。价值依次显现：决策速度→问责→模式获取；纪律（禁推销/挖人/募资/旁观）决定小组生死。",
        "how": "经营高管同侪圈，参考 Vistage/EO 模式：小范围（6-12人）+ 绝对保密 + 固定月频 +\u201c带真实决策、先问后荐、呈现者最后说\u201d；用\u201c亲身经历\u201d替代空泛建议（EO 禁建议协议反直觉但有效）。把同侪对话当\u201c没人能给你的董事会\u201d，慎选人、守纪律，避免变推销场。",
        "url": "https://www.joinhelix.co/founder/ceo-peer-groups/",
        "note": "适用：③ 创始人/CEO × 同侪高管（二手方法论；保密同侪顾问小组，可作高管圈层运营参考，非内部员工活动）。",
    },
    {
        "emoji": "\U0001F373",
        "title": "高管闭门早餐会·策展式同行对话（Val Wright）",
        "cat": "高管 breakfast",
        "rel": "r3", "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "Val Wright Consulting 在洛杉矶办\u201cThe Executive Breakfast\u201d：15-20 位高管（CEO、其直接下属、现任董事）一上午闭门，无赞助无供应商，\u201cexecutive to executive 对话 only\u201d。每场 5 位高管分享当下所学，并跑结构化\u201cAsks & Gives\u201d环节——到场领 GIVE/ASK 卡，手写能给出与想要的资源，贴墙上互相认领（过往 GIVE 含 CNBC CEO Council 引荐、CFO 对 live M&A 视角、PE 董事席位等）。与会者称其\u201c部分治疗、部分战略、部分执行手册\u201d，零废话。",
        "how": "办高管早餐/闭门会，学 Val Wright\u201c策展式 + Asks & Gives\u201d：严选同层级（CEO+直报+董事）、无赞助保坦诚、结构化\u201c能给/想要\u201d卡片墙促成实质资源对接；把松散 networking 变成\u201c可带走的资源与承诺\u201d。适合作高管同侪圈层的固定轻量载体。",
        "url": "https://www.valwrightconsulting.com/executivebreakfast",
        "note": "适用：③ CEO/董事/高管 × 同侪（二手活动案例；策展式闭门早餐 + Asks&Gives 资源对接，可作高管生态运营参考）。",
    },
    {
        "emoji": "\U0001F510",
        "title": "保密早餐会·董事会级敏感决策场",
        "cat": "保密决策",
        "rel": "r3", "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "保密早餐会（Confidential Breakfast）是精选高层的小范围闭门：仅限 C-suite、投资者、关键决策者与受信内部人，于安全私密场所（隔音包厢/私密俱乐部）进行，签 NDA、限知需知。在此董事会可就并购等敏感议题辩论选项、权衡利弊、高效达成共识，免去大会议的官僚延迟；信任来自 exclusivity + discretion，组织者建模透明、会后跟进致谢。常配破冰/圆桌促有机对话，催生合作、导师或融资。",
        "how": "办董事会级保密早餐，学\u201c限知需知+安全场所+NDA+圆桌\u201d：把 M&A/战略等敏感议题放小范围闭门，降泄露风险、提决策速度；用破冰/圆桌促坦诚；会后跟进关键结论并致谢，把单次会议变信任资产。适合并购期/敏感战略对齐。",
        "url": "https://anmeal.com/article/what-is-confidential-breakfast",
        "note": "适用：③ 董事会/高管 × 同侪决策者（二手方法论；保密早餐会做敏感决策，可作治理层闭门参考，非员工活动）。",
    },
]

# ============ 卡片 HTML（墙/页通用）============
def card_html(c, indent=4):
    sp = " " * indent
    sp2 = " " * (indent + 2)
    rel_badge = '<span class="badge {0}">{1}</span>'.format(c["rel"], c["rel_text"])
    src_badge = '<span class="badge {0}">{1}</span>'.format(c["src"], c["src_text"])
    return (
        sp + '<div class="hl">\n'
        + sp2 + '<div class="top"><span class="emoji">' + esc(c["emoji"]) + '</span>'
        + '<h3>' + esc(c["title"]) + '</h3><span class="cat">' + esc(c["cat"]) + '</span>'
        + rel_badge + src_badge + '</div>\n'
        + sp2 + '<p class="val">' + esc(c["val"]) + '</p>\n'
        + sp2 + '<details class="exec"><summary>怎么做</summary><div class="inner">' + esc(c["how"]) + '</div></details>\n'
        + sp2 + '<div class="src">\U0001F517 <a href="' + esc(c["url"]) + '" target="_blank">' + esc(c["url"]) + '</a></div>\n'
        + sp2 + '<div class="note">' + esc(c["note"]) + '</div>\n'
        + sp + '</div>\n'
    )

def find_grid_close(h, sec_start):
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
                return i
            depth -= 1
            i += 5
        else:
            i += 1
    raise RuntimeError("unbalanced")

# ============ 主样式（与墙一致，单花括号，正确渲染）============
STYLE = """.wrap{max-width:1080px;margin:0 auto;}
.hero{background:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);border-radius:22px;padding:26px 30px;color:#fff;box-shadow:0 14px 40px rgba(108,92,231,.25);margin-bottom:22px;}
.hero h1{font-size:24px;font-weight:800;letter-spacing:1px;margin-bottom:6px;}
.hero p{font-size:13px;opacity:.95;}
.relbar{display:flex;gap:10px;flex-wrap:wrap;margin-top:12px;}
.relbar span{background:rgba(255,255,255,.2);border-radius:20px;padding:5px 14px;font-size:13px;font-weight:600;}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;}
.hl{background:#fff;border-radius:18px;padding:18px 18px 16px;border-top:4px solid #6c5ce7;box-shadow:0 10px 32px rgba(108,92,231,.10);display:flex;flex-direction:column;gap:9px;}
.top{display:flex;align-items:center;gap:8px;flex-wrap:wrap;}
.emoji{font-size:22px;}
.hl h3{font-size:16px;font-weight:700;flex:1;min-width:120px;}
.cat{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:600;background:#eef0ff;color:#6c5ce7;}
.badge{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:700;}
.b2{background:#fff1e6;color:#c0651a;}
.b1{background:#e6f9ed;color:#1a9e5a;}
.r2{background:#fff3e0;color:#c0651a;}
.r3{background:#f3e8ff;color:#7b2cbf;}
.val{font-size:13.5px;color:#5b6478;}
.exec{margin-top:2px;border-top:1px dashed #e2e8f0;padding-top:8px;}
.exec summary{cursor:pointer;font-size:13px;font-weight:600;color:#6c5ce7;}
.exec .inner{font-size:13px;color:#5b6478;margin-top:6px;padding-left:4px;}
.src{font-size:12px;word-break:break-all;}
.src a{color:#00b8d9;text-decoration:none;}
.note{font-size:12px;color:#94a3b8;border-left:3px solid #e2e8f0;padding-left:8px;}
footer{text-align:center;padding:24px;color:#94a3b8;font-size:13px;border-top:1px solid #e2e8f0;margin-top:40px;}
:root{--accent:#6c5ce7;--accent2:#00b8d9;}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:linear-gradient(135deg,#eef1ff 0%,#e6f7ff 100%);color:#1f2430;padding:28px 18px;line-height:1.6;}"""

WALL_URL = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/afternoontea/afternoontea.html"
PORTAL_URL = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/index.html"

def build_incremental():
    n_r3 = sum(1 for c in CARDS if c["rel"] == "r3")
    n_r2 = sum(1 for c in CARDS if c["rel"] == "r2")
    cards_block = "".join(card_html(c) for c in CARDS)
    html = (
        '<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '<title>\u4e0b\u5348\u8336\u7814\u8ba8 \u00b7 \u4e8c\u5341\u4e8c\u8f6e\u589e\u91cf\u5361\u7247\uff082026-08-21\uff09</title>\n'
        '<style>\n' + STYLE + '\n</style>\n</head><body>\n<div class="wrap">\n'
        '<p style="margin:0 0 16px"><a href="' + WALL_URL + '" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">\U0001F375 \u8fd4\u56de\u4e0b\u5348\u8336\u7d2f\u8ba1\u5361\u7247\u5899 \u2192</a> &nbsp; '
        '<a href="' + PORTAL_URL + '" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">\U0001F4DA \u8fd4\u56de\u77e5\u8bc6\u5e93\u95e8\u6237 \u2192</a></p>\n'
        '  <div class="hero">\n'
        '    <h1>\U0001F375 \u4e0b\u5348\u8336\u7814\u8ba8 \u00b7 \u4e8c\u5341\u4e8c\u8f6e\u589e\u91cf\u5361\u7247\uff082026-08-21\uff09</h1>\n'
        '    <p>\u672c\u8f6e\u65b0\u589e 7 \u5f20\uff08\u901a\u8fc7\u516d\u7ef4\u8bc4\u4f30\uff0c\u5254\u9664\u5e73\u7ea7/\u670b\u53cb\u5411\u2460\uff0c\u4ec5 ②\u4e0a\u4e0b\u7ea7 / ③\u9ad8\u7ba1\u95f4\uff09\uff1b\u5173\u7cfb\u6863\uff1a③\u9ad8\u7ba1\u95f4 3 \u5f20 + ②\u4e0a\u4e0b\u7ea7 4 \u5f20\u3002</p>\n'
        '    <div class="relbar">\n'
        '      <span>② \u9886\u5bfc\u2194\u5458\u5de5\uff08\u4e0a\u4e0b\u7ea7\uff0csupervisor\uff09</span>\n'
        '      <span>③ \u9886\u5bfc\u2194\u9886\u5bfc\uff08\u9ad8\u7ba1\u95f4\uff0cexec\uff09</span>\n'
        '    </div>\n'
        '  </div>\n'
        '  <div class="grid">\n' + cards_block + '  </div>\n'
        '<footer>\U0001F4CC \u672c\u9875\u7531 yitong \u6c89\u6dc0\u6574\u7406 \u00b7 \u6587\u5316\u6d3b\u52a8\u77e5\u8bc6\u5e93</footer>\n'
        '</div>\n</body>\n</html>\n'
    )
    open(RUN_PATH, "w", encoding="utf-8").write(html)
    return len(html.encode("utf-8"))

# ============ 1) 增量页 ============
inc_bytes = build_incremental()
print("增量页已写出:", RUN_PATH, inc_bytes, "B")

# ============ 2) 墙注入 ============
html = open(CUM, encoding="utf-8").read()
before = html.count('<div class="hl">')
cards_sec3 = [c for c in CARDS if c["rel"] == "r3"]
cards_sec2 = [c for c in CARDS if c["rel"] == "r2"]
i3 = html.find('class="sec sec3"')
close3 = find_grid_close(html, i3)
html = html[:close3] + "".join(card_html(c) for c in cards_sec3) + html[close3:]
i2 = html.find('class="sec sec2"')
close2 = find_grid_close(html, i2)
html = html[:close2] + "".join(card_html(c) for c in cards_sec2) + html[close2:]
# hero
hero_old = "\u4e8c\u5341\u4e00\u8f6e enrich 2026-08-20(+9)</p>"
hero_new = "\u4e8c\u5341\u4e00\u8f6e enrich 2026-08-20(+9) \uff5c \u4e8c\u5341\u4e8c\u8f6e enrich 2026-08-21(+7)</p>"
assert hero_old in html, "hero marker not found"
html = html.replace(hero_old, hero_new, 1)
# recount
def recount(tagcls):
    s = html.find('class="' + tagcls + '"')
    e = html.find('class="sec', s + 10)
    return html[s:e].count('<div class="hl">')
r2n = recount('sec sec2'); r3n = recount('sec sec3')
html = re.sub(r'(<div class="sec sec2">.*?<span class="tag">)\d+( \u5361</span>)',
              lambda m: m.group(1) + str(r2n) + m.group(2), html, count=1, flags=re.S)
html = re.sub(r'(<div class="sec sec3">.*?<span class="tag">)\d+( \u5361</span>)',
              lambda m: m.group(1) + str(r3n) + m.group(2), html, count=1, flags=re.S)
open(CUM, "w", encoding="utf-8").write(html)
after = html.count('<div class="hl">')
r2b = html.count('badge r2'); r3b = html.count('badge r3')
b1b = html.count('badge b1'); b2b = html.count('badge b2')
footer_ok = "\U0001F4CC \u672c\u9875\u7531 yitong" in html
print("累计墙卡片数:", after, "(+", after - before, ") | r2:", r2b, "r3:", r3b, "| b1:", b1b, "b2:", b2b, "| footer:", footer_ok)
print("sec2 tag:", r2n, "sec3 tag:", r3n)

# ============ 3) index.json ============
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
        print("SKIP dup url:", u); continue
    entry = {
        "title": c["title"],
        "normKey": normkey(c["title"]),
        "url": c["url"],
        "sourceType": "secondary" if c["src"] == "b2" else "primary",
        "relation": "exec" if c["rel"] == "r3" else "supervisor",
        "summary": c["cat"] + "：" + c["val"][:60],
        "topic": "afternoontea",
    }
    data.append(entry); added += 1
print("index.json 新增:", added, "-> 现", len(data), "条")
json.dump(data, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

# ============ 4) Obsidian 笔记 ============
VAULT = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库"
NOTE = os.path.join(VAULT, "素材", "afternoontea", "下午茶研讨-知识卡汇总.md")
t = open(NOTE, encoding="utf-8").read()
assert "（138 卡 · 上下级/高管间）" in t
t = t.replace("（138 卡 · 上下级/高管间）", "（145 卡 · 上下级/高管间）", 1)
assert "\u4e8c\u5341\u4e00\u8f6e enrich 2026-08-20(+9)" in t
t = t.replace("\u4e8c\u4e00\u8f6e enrich 2026-08-20(+9)",
              "\u4e8c\u4e00\u8f6e enrich 2026-08-20(+9) \uff5c \u4e8c\u5341\u4e8c\u8f6e enrich 2026-08-21(+7)", 1)
assert "\u7d2f\u8ba1 138 \u5361\uff08③\u9ad8\u7ba1\u95f4 53 / ②\u4e0a\u4e0b\u7ea7 89\uff0c\u542b 4 \u5f20\u8de8\u6863\u53cc\u6807\uff1b\u4e00\u624b 40 + \u4e8c\u624b 98\uff09" in t
t = t.replace("\u7d2f\u8ba1 138 \u5361\uff08③\u9ad8\u7ba1\u95f4 53 / ②\u4e0a\u4e0b\u7ea7 89\uff0c\u542b 4 \u5f20\u8de8\u6863\u53cc\u6807\uff1b\u4e00\u624b 40 + \u4e8c\u624b 98\uff09",
              "\u7d2f\u8ba1 145 \u5361\uff08③\u9ad8\u7ba1\u95f4 56 / ②\u4e0a\u4e0b\u7ea7 93\uff0c\u542b 4 \u5f20\u8de8\u6863\u53cc\u6807\uff1b\u4e00\u624b 43 + \u4e8c\u624b 102\uff09", 1)
round_section = (
    "\n## 轮次 2026-08-21（+7）\n"
    "> 二十二轮 enrich：新增 7 卡（③ 高管间 +3：CEO 同侪顾问小组·保密决策压力测试（Vistage/EO/Helix）/ 高管闭门早餐会·策展式同行对话（Val Wright）/ 保密早餐会·董事会级敏感决策场；② 上下级 +4：建行兴安分行党委书记一对一访谈 / 苏州园林集团经营层谈心谈话 / 台茂精机新员工茶话会 / 沃尔玛式越级沟通·二八倾听法则）。无 peer，relation 仅取 supervisor/exec。\n"
    "> 线上预览：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/afternoontea/afternoontea.html ｜ 本轮增量页：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/afternoontea/afternoontea-20260821.html\n"
)
marker3 = "## ③ 领导↔领导（高管间 · exec）— 51 卡"
assert marker3 in t
t = t.replace(marker3, round_section + marker3.replace("51 卡", "56 卡"), 1)
marker2 = "## ② 领导↔员工（上下级 · supervisor）— 83 卡"
assert marker2 in t
r3_rows = "".join(
    "| {0} | {1}（afternoontea.html） | {2} | {3} |\n".format(52 + i, esc(c["title"]), "一手" if c["src"] == "b1" else "二手", "③高管间" if c["rel"] == "r3" else "②上下级")
    for i, c in enumerate(cards_sec3)
)
t = t.replace(marker2, r3_rows + "\n" + marker2.replace("83 卡", "93 卡"), 1)
r2_rows = "".join(
    "| {0} | {1}（afternoontea.html） | {2} | {3} |\n".format(84 + i, esc(c["title"]), "一手" if c["src"] == "b1" else "二手", "②上下级")
    for i, c in enumerate(cards_sec2)
)
t = t.rstrip("\n") + "\n" + r2_rows
open(NOTE, "w", encoding="utf-8").write(t)
print("Obsidian 笔记更新完成")

# ============ 5) 00-索引 ============
IDX0 = os.path.join(VAULT, "00-知识采集索引.md")
i0 = open(IDX0, encoding="utf-8").read()
hdr_old = "\u4e8c\u5341\u4e00\u8f6e enrich 2026-08-20(+9)\uff09"
assert hdr_old in i0
i0 = i0.replace(hdr_old, "\u4e8c\u5341\u4e00\u8f6e enrich 2026-08-20(+9) \uff5c \u4e8c\u5341\u4e8c\u8f6e enrich 2026-08-21(+7)\uff09", 1)
assert "**138 卡**" in i0
i0 = i0.replace("**138 卡**", "**145 卡**", 1)
assert "\u4e00\u624b 40 + \u4e8c\u624b 98" in i0
i0 = i0.replace("\u4e00\u624b 40 + \u4e8c\u624b 98", "\u4e00\u624b 43 + \u4e8c\u624b 102", 1)
assert "③高管间(...) 53 卡 / ②上下级(...) 89 卡\uff08\u542b 4 \u5f20\u8de8\u6863\u53cc\u6807\uff0c\u53bb\u91cd\u540e 128\uff09" in i0
i0 = i0.replace("③高管间(...) 53 卡 / ②上下级(...) 89 卡\uff08\u542b 4 \u5f20\u8de8\u6863\u53cc\u6807\uff0c\u53bb\u91cd\u540e 128\uff09",
                "③高管间(...) 56 卡 / ②上下级(...) 93 卡\uff08\u542b 4 \u5f20\u8de8\u6863\u53cc\u6807\uff0c\u53bb\u91cd\u540e 141\uff09", 1)
narr_tail = "卓尔科技总经理接待日，从员工状态/发展方向四方向听建议）。"
assert narr_tail in i0
i0 = i0.replace(narr_tail, narr_tail
    + "\u4e8c\u5341\u4e8c\u8f6e enrich \u65b0\u589e\uff08③CEO \u540c\u4f7a\u987e\u95ee\u5c0f\u7ec4\u00b7\u4fdd\u5bc6\u51b3\u7b56\u538b\u529b\u6d4b\u8bd5 / ③\u9ad8\u7ba1\u95ed\u95e8\u65e9\u9910\u4f1a\u00b7\u7b56\u5c55\u5f0f\u540c\u884c\u5bf9\u8bdd / ③\u4fdd\u5bc6\u65e9\u9910\u4f1a\u00b7\u8463\u4e8b\u4f1a\u7ea7\u654f\u611f\u51b3\u7b56\u573a + ②\u5efa\u884c\u5174\u5b89\u5206\u884c\u515a\u59d4\u4e66\u8bb0\u4e00\u5bf9\u4e00\u8bbf\u8c08 / ②\u82cf\u5dde\u56ed\u6797\u96c6\u56e2\u7ecf\u8425\u5c42\u8c08\u5fc3\u8c08\u8bdd / ②\u53f0\u8302\u7cbe\u673a\u65b0\u5458\u5de5\u8336\u8bdd\u4f1a / ②\u6c83\u5c14\u739b\u5f0f\u8d8a\u7ea7\u6c9f\u901a\u00b7\u4e8c\u516b\u503e\u542c\u6cd5\u5219\uff09\u3002", 1)
next_theme = i0.find("## 主题：", i0.find("## 主题：下午茶研讨") + 10)
assert next_theme != -1
rows = "".join(
    "| {0}\uff08afternoontea.html\uff09 | 6 | {1} | {2} |  |\n".format(c["title"], "一手" if c["src"] == "b1" else "二手", "③高管间" if c["rel"] == "r3" else "②上下级")
    for c in CARDS
)
i0 = i0[:next_theme] + rows + "\n" + i0[next_theme:]
open(IDX0, "w", encoding="utf-8").write(i0)
print("00-索引更新完成")

# ============ 6) 乐享上传（新建独立页文件模式）============
MCP_JSON = os.path.expanduser("~/.workbuddy/mcp.json")
LEXIANG_URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"
FOLDER = "96e0ca6a548e4202a12d43dc91b48938"
class LexiangMCP:
    def __init__(self, token):
        self.token = token; self.session = None
    def _post(self, payload, retries=2):
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(LEXIANG_URL, data=data, method="POST")
        req.add_header("Content-Type", "application/json")
        req.add_header("Accept", "application/json, text/event-stream")
        req.add_header("Authorization", self.token)
        if self.session: req.add_header("Mcp-Session-Id", self.session)
        last = None
        for _ in range(retries):
            try:
                resp = urllib.request.urlopen(req, timeout=120)
                sid = resp.headers.get("mcp-session-id")
                if sid: self.session = sid
                return self._parse(resp.read().decode("utf-8", "replace"))
            except urllib.error.HTTPError as e:
                last = "HTTP {0}: {1}".format(e.code, e.read().decode("utf-8", "replace")[:400]); continue
            except Exception as e:
                last = str(e); continue
        raise RuntimeError("POST fail: " + last)
    def _parse(self, raw):
        raw = raw.strip()
        if raw.startswith("data:"):
            raw = "\n".join(l[5:].strip() for l in raw.splitlines() if l.startswith("data:"))
        try: return json.loads(raw)
        except Exception: return json.loads(raw[raw.find("{"):])
    def initialize(self):
        return self._post({"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"wb-uploader","version":"1.0"}}})
    def initialized(self):
        try: self._post({"jsonrpc":"2.0","method":"notifications/initialized"})
        except Exception: pass
    def call(self, name, args):
        return self._post({"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":name,"arguments":args}})
    def biz(self, resp):
        res = resp.get("result")
        if not res: raise RuntimeError("no result: " + json.dumps(resp, ensure_ascii=False)[:300])
        text = ""
        for c in (res.get("content") or []):
            if c.get("type") == "text": text = c.get("text", ""); break
        try: return json.loads(text)
        except Exception: return {"_raw_text": text}
def put_bytes(url, data):
    req = urllib.request.Request(url, data=data, method="PUT")
    req.add_header("Content-Type", "text/html")
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.status
try:
    token = json.load(open(MCP_JSON, encoding="utf-8"))["mcpServers"]["lexiang"]["headers"]["Authorization"]
    mc = LexiangMCP(token); mc.initialize(); mc.initialized()
    try:
        print("whoami:", json.dumps(mc.biz(mc.call("whoami", {}))[:0] if False else mc.call("whoami", {}), ensure_ascii=False)[:120])
    except Exception as e:
        print("whoami 跳过:", str(e)[:120])
    data_bytes = open(RUN_PATH, "rb").read()
    r = mc.call("file_apply_upload", {"parent_entry_id": FOLDER, "name": RUN_NAME, "extension":"html", "mime_type":"text/html", "upload_type":"PRE_SIGNED_URL", "size": str(len(data_bytes))})
    biz = mc.biz(r)
    if biz.get("code") != 0:
        raise RuntimeError("apply_upload FAIL {0}".format(biz.get("message")))
    sess = biz["data"]["session"]
    sid = sess.get("session_id") or sess.get("id")
    url = sess.get("upload_url") or sess["objects"][0]["upload_url"]
    st = put_bytes(url, data_bytes)
    if st != 200: raise RuntimeError("PUT status " + str(st))
    r2 = mc.call("file_commit_upload", {"session_id": sid})
    biz2 = mc.biz(r2)
    if biz2.get("code") != 0: raise RuntimeError("commit FAIL " + str(biz2.get("message")))
    rid = biz2["data"]["entry"]["id"]
    print("乐享新建页 OK entry_id=", rid)
    mapf = json.load(open(os.path.join(BASE, "lexiang-entry-map.json"), encoding="utf-8"))
    sm = mapf.setdefault("afternoontea", {"folder_id": FOLDER, "rounds": []})
    sm["folder_id"] = FOLDER
    sm["rounds"].append({"date": DATE, "entry_id": rid, "name": RUN_NAME})
    json.dump(mapf, open(os.path.join(BASE, "lexiang-entry-map.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("已回写 lexiang-entry-map.json")
except Exception as e:
    print("\u26a0\ufe0f 乐享上传跳过（warning，不中断）：" + str(e)[:300])

print("\n=== R22 完成：新增", added, "卡，墙现", after, "卡 ===")
