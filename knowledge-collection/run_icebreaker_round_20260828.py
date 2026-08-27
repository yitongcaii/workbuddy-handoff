# -*- coding: utf-8 -*-
"""破冰 本轮补采 (2026-08-28) — 仅②③（0 peer）。
新增 4 张经六维评估通过、与既有 158 卡去重后的卡（③×3 / ②×1），
覆盖治理层/高管对齐新角度（高管团队运营章程 / 董事会-CEO 运营协议 / 联席CEO协议）+ 越级会谈领导者侧实战手册。
流程：增量页 + 累计墙追加 + index.json + Obsidian(00索引/破冰汇总笔记) + GitHub + 乐享(文件上传·新建独立页)。
"""
import json, os, re, subprocess, urllib.request, urllib.error

BASE = os.path.dirname(os.path.abspath(__file__))
AT = os.path.join(BASE, "icebreaker")
CUM = os.path.join(AT, "icebreaker.html")
INC_NAME = "icebreaker-20260828.html"
INC_PATH = os.path.join(AT, INC_NAME)
IDX = os.path.join(BASE, "index.json")
MAP = os.path.join(BASE, "lexiang-entry-map.json")
VN = "2026-08-28"
ROUND_LABEL = "2026-08-28 补采(+4)"

VAULT = r"C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库"
NOTE_PATH = os.path.join(VAULT, "素材", "icebreaker", "破冰-知识卡汇总.md")
IDX00 = os.path.join(VAULT, "00-知识采集索引.md")
GP_URL = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker"

def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

CARDS = [
    {
        "emoji": "\U0001F4DC",  # 📜
        "title": "高管团队运营章程·6 项承诺 + DRI + 禁三角传递",
        "cat": "高管团队章程",
        "rel": "exec", "rel_text": "高管间", "src": "b2", "src_text": "二手",
        "val": "高管团队需要一份「运营章程」（Operating Charter），不是裱起来的价值观海报，而是一份行为协议——当某个行为不支持团队变高绩效时，能随手拿出来用。最少约定六件事：①首要团队（Executive Team 是每位成员的第一团队，优先于本职能）；②承诺（说了做，或截止前重谈，不设「忘了」）；③反馈（顾虑直接、快速提出）；④冲突（承诺前先辩论，而非会后私下抱怨）；⑤DRI（每个重要决策/目标/项目有且仅有 1 个直接责任人——多人「共创」= 混乱）；⑥行为底线（明确不容忍：迟到、八卦、三角传递 / triangulation）。关键纪律：章程不要第一天就推广给全公司——先在团队内部「活出来」，等成员已身体力行，再外溢成更广的领导力框架；否则只是「bollocks」。破筒仓：让职能负责人认领跨公司能力线（如招聘/中层发展/产品质量），每条一个 DRI；用 TOM（target operating model，管日常）+ OKR（管变革）双轨，让团队互相问责而非事事升级给创始人。节奏：日站会清阻塞、周会定优先级+2 个需辩论的约束、月会深度职能复盘、季会重置 90 天 OKR；每位高管每周至少与 1 名职能外员工 + 1 名客户对话，把一线信号带回周会。",
        "exec": "高管团队先签「运营章程」：首要团队优先本职能、承诺必践或重谈、冲突先辩后决、DRI 一人负全责、零容忍八卦三角传递；先团队内部活出来再外推；TOM+OKR 双轨 + 日/周/月/季节奏 + 每周 1 员工 1 客户对话带回周会。",
        "url": "https://www.monkhouseandcompany.com/blog/how-to-supercharge-your-executive-team",
        "url_disp": "monkhouseandcompany.com/blog/how-to-supercharge-your-executive-team",
        "note": "适用：③ 高管团队运营章程——6 承诺 + DRI 单一问责 + 禁三角传递 + 先活出来再推广 + TOM/OKR 双轨节奏，「活出来再外推」是治理层契约落地关键（高管间，非游戏）。",
    },
    {
        "emoji": "\U0001F3DB\uFE0F",  # 🏛️
        "title": "董事会-CEO 运营协议·四级决策权 + 客观阈值",
        "cat": "治理层对齐",
        "rel": "exec", "rel_text": "高管间", "src": "b2", "src_text": "二手",
        "val": "CEO 与董事会的张力几乎从不是「决策内容」，而是「谁来做这个决策」的模糊。解法：写一份 Board-CEO Operating Agreement（非法律文件、1-2 页，CEO 与董事会的书面共识）。核心四层决策权（成为双方通用语言）：①独自决策（CEO 径行决定）；②决定并告知（CEO 决定后报董事会）；③建议并批准（CEO 出建议、董事会批准方行动）；④董事会保留（依章程/法律保留）。把重复出现的决策逐条归类到这四层——讨论过程本身最常暴露「原来我们多年假设不同」。原则：能用客观阈值绝不用主观词（「重大支出」人人理解不同，写死金额；职级/法律风险/融资同理）。运营承诺：CEO 拟遵循的基本操作系统（节奏/汇报/沟通）。价值：消除「小事频频请示显得不自信」「大事独断越过董事会预期」两种失败模式；董事会最恨 surprise，定期把「我已决定、你本该有发言权」变成会前对齐。少了它，信任在「谁做主」的模糊里一点点流失。",
        "exec": "建 1-2 页 Board-CEO 运营协议：把反复出现的决策归入「独自决/决定并告知/建议批准/董事会保留」四层；阈值写死金额/职级/法律风险不用主观词；会前对齐避免 surprise；把「谁做主」的模糊变显式，信任由重复一致行为建成。",
        "url": "https://www.managingthefuture.co/p/the-agreement-every-board-and-ceo",
        "url_disp": "managingthefuture.co/p/the-agreement-every-board-and-ceo",
        "note": "适用：③ 治理层（董事会-CEO）对齐——运营协议四层决策权 + 客观阈值 + 会前对齐消 surprise（高管间/治理层，非游戏）。",
    },
    {
        "emoji": "\U0001F91D",  # 🤝
        "title": "联席 CEO/共治团队协议·决策权/沟通/冲突/基调 四领域",
        "cat": "共治团队协议",
        "rel": "exec", "rel_text": "高管间", "src": "b2", "src_text": "二手",
        "val": "联席领导（Co-CEO/双人共治）结构不同于单人领导：两人共享权威时，每一个未说破的假设都是潜在断层。根因几乎不是「坏意图」，而是缺少「两人如何实际协作」的显式协议。最关键的协议覆盖四领域：①决策权（谁独占哪些决策、哪些需双方对齐、意见相左时怎么办——无关信任，只为降低持续谈判的认知负荷、给团队清晰答案）；②沟通协议（何时互 loop、如何；重大公告/敏感对话/方向变更前是否先知会对方；一方对董事会/投资者/全员讲话，另一方是否先知道）；③冲突与分歧（看法不同时怎么办、如何「对外呈现统一立场」——最有价值的协议之一）；④基调/文化/建模（两人想在领导团队与更广组织前共同示范什么）。构建原则：早建（关系新鲜、摩擦低时比紧张中重谈容易）、写下来（口头的会漂，一页纸即可）、点名困难场景（「想退出怎么办」「重大招聘根本分歧」「董事会对一方失信心怎么办」）、设复盘节奏（季/半年度回看、随组织演进）。诚信：协议一旦设就被当真承诺，越过一步即削弱——信任由「无人看见时也做到」的重复一致行为建成，非好意或共享价值观。",
        "exec": "联席/共治领导先签「团队协议」四领域：决策权（独占/对齐/分歧处理）、沟通协议（重大动作先互 loop）、冲突（对外统一立场）、基调建模；早建+写下来+点名困难场景+季/半年度复盘；越过一步即削弱信任。",
        "url": "https://www.ceonextchapter.com/insights-blog/why-co-ceos-need-team-agreements",
        "url_disp": "ceonextchapter.com/insights-blog/why-co-ceos-need-team-agreements",
        "note": "适用：③ 共治/联席领导（Co-CEO）对齐——决策权/沟通/冲突/基调四领域协议（高管间，治理层，非游戏）。",
    },
    {
        "emoji": "\U0001F52D",  # 🔭
        "title": "越级会谈·领导者实战手册（先告中层 + 6Ps 预简报 + 45min 高密度议程）",
        "cat": "越级会谈",
        "rel": "supervisor", "rel_text": "上下级", "src": "b2", "src_text": "二手",
        "val": "越级会谈（skip-level）不是办工作坊，而是用一致的思维模型，让跨层的「组织机制真相」随时间浮现。先定格式：1:1（挖真话但覆盖慢）、小组（看团队内对齐/分裂、省时但安静者易自审）、混合（季度小组+对弱信号做定向 1:1，推荐）。会前「设计信任、降恐惧」：发简短具体的 pre-brief——说明目的（「理解什么在帮/碍绩效、我层能修什么」）、谈什么（6Ps 大白话）、不做什么（「不是攻击个人/谈个人安排」）、保密边界（「不点名引用；需行动就以主题提」）、好输入长啥样（「具体例子、重复模式、对客户/交付的影响」）。关键：先 briefing 你的中层经理（10 分钟：意图/边界/承诺「与你分享主题、闭环」/他们的角色「鼓励坦诚、不脚本、准备接主题」），并问「你觉得我会听到什么你已知道」「系统在哪让你的团队更难」——把越级从「威胁」变「联合诊断」。议程（紧 45min 防跑偏）：0-5 设规则（目的+保密+要具体模式非传闻）；5-30 高密度问题——优先级清晰度（「问 3 人本季 Top3，答案会一致吗」）、执行阻力、决策延迟、质量/客户影响、角色清晰度、经理赋能、文化真相、留任风险（「强者明天走，真实原因是啥」）；30-40 测模式与矛盾（「多频繁」「近期例子」「还有谁」「你试过啥」「只修一件哪件杠杆最大」）；40-45 收尾承诺。纪律：不把「你觉经理咋样」当问题（那是人格审判），要组织机制与模式。",
        "exec": "越级会谈先定格式（1:1/小组/混合）；会前发 6Ps pre-brief + 先 briefing 中层经理（变联合诊断）；45min 议程：设规则→高密度 6Ps 追问→测模式矛盾→收尾承诺；问组织机制非人格，不作考核、保匿名。",
        "url": "https://performanceninja.co.uk/post/skip-level-meetings-that-work-a-leaders-playbook",
        "url_disp": "performanceninja.co.uk/post/skip-level-meetings-that-work-a-leaders-playbook",
        "note": "适用：② 越级会谈（领导者侧实战手册）——先告中层+6Ps 预简报+45min 高密度议程+组织机制追问（上下级，leader↔跨层员工，避免变「打小报告」/考核中层）。",
    },
]

def card_block(c):
    rel_badge = 'r3' if c["rel"] == "exec" else 'r2'
    return (
        '    <div class="hl">\n'
        '      <div class="top"><span class="emoji">{emoji}</span><h3>{title}</h3>'
        '<span class="cat">{cat}</span><span class="badge {rb}">{rel_text}</span>'
        '<span class="badge {src}">{src_text}</span></div>\n'
        '      <p class="val">{val}</p>\n'
        '      <details class="exec"><summary>怎么做</summary><div class="inner">{exec_inner}</div></details>\n'
        '      <div class="src">\U0001F517 <a href="{url}" target="_blank">{url_disp}</a></div>\n'
        '      <div class="note">适用：{note}</div>\n'
        '    </div>\n'
    ).format(
        emoji=esc(c["emoji"]), title=esc(c["title"]), cat=esc(c["cat"]),
        rb=rel_badge, rel_text=esc(c["rel_text"]), src=c["src"], src_text=esc(c["src_text"]),
        val=esc(c["val"]), exec_inner=(c["exec"]), url=c["url"], url_disp=esc(c["url_disp"]),
        note=esc(c["note"]),
    )

EXEC_CARDS = [c for c in CARDS if c["rel"] == "exec"]
SUP_CARDS = [c for c in CARDS if c["rel"] == "supervisor"]
print("EXEC:", len(EXEC_CARDS), "SUP:", len(SUP_CARDS), "TOTAL:", len(CARDS))

# ---------- 1) 增量页 icebreaker-20260828.html ----------
CSS = '''<style>
:root{--bg:#f4f6fb;--card:#ffffff;--ink:#1f2430;--sub:#5b6478;--accent:#6c5ce7;--accent2:#00b8d9;--chip:#eef0ff;}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:linear-gradient(135deg,#eef1ff 0%,#e6f7ff 100%);color:var(--ink);padding:28px 18px;line-height:1.6;}
.wrap{max-width:1080px;margin:0 auto;}
.hero{background:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);border-radius:22px;padding:30px 32px;color:#fff;box-shadow:0 14px 40px rgba(108,92,231,.25);margin-bottom:22px;}
.hero h1{font-size:28px;font-weight:800;letter-spacing:1px;margin-bottom:8px;}
.hero p{font-size:14px;opacity:.95;}
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
.b1{background:#eaf2ff;color:#2b6cb0;}
.r1{background:#eaf2ff;color:#2b6cb0;}
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
</style>'''

def build_inc_page():
    parts = []
    parts.append('<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n<meta charset="UTF-8">\n'
                 '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
                 '<title>破冰 · 知识采集增量页 ' + VN + '</title>\n' + CSS + '\n</head>\n<body>\n<div class="wrap">')
    parts.append('<div class="hero"><h1>\U0001F9CA 破冰 · 知识采集增量页</h1>'
                 '<p>采集于 ' + VN + ' ｜ 本轮 +' + str(len(CARDS)) + '（仅②上下级 / ③高管间，0 peer）｜ 六维评估（含关系适配度）｜ 一手/二手标注 ｜ 历史去重</p>'
                 '<div class="relbar"><span>② 领导↔员工（上下级，supervisor）</span>'
                 '<span>③ 领导↔领导（高管间，exec）</span></div></div>')
    # SEC3 exec
    parts.append('<div class="sec sec3"><h2>③ 领导↔领导（高管间 · exec）</h2>'
                 '<span class="tag">' + str(len(EXEC_CARDS)) + ' 卡</span>'
                 '<span class="desc">本轮新增治理层/高管对齐角度（运营章程/董事会-CEO 协议/联席CEO协议），均非游戏。</span></div>')
    parts.append('<div class="grid">')
    for c in EXEC_CARDS:
        parts.append(card_block(c))
    parts.append('</div>')
    # SEC2 supervisor
    parts.append('<div class="sec sec2"><h2>② 领导↔员工（上下级 · supervisor）</h2>'
                 '<span class="tag">' + str(len(SUP_CARDS)) + ' 卡</span>'
                 '<span class="desc">本轮新增越级会谈领导者侧实战手册（先告中层+高密度议程）。</span></div>')
    parts.append('<div class="grid">')
    for c in SUP_CARDS:
        parts.append(card_block(c))
    parts.append('</div>')
    parts.append('<footer>\U0001F538 本页由 yitong 沉淀整理 · 文化活动知识库</footer>')
    parts.append('</div>\n</body>\n</html>')
    out = "\n".join(parts)
    open(INC_PATH, "w", encoding="utf-8").write(out)
    print("增量页已生成:", INC_PATH, len(out), "字节")

build_inc_page()

# ---------- 2) 累计墙 icebreaker.html 追加 ----------
def update_summary():
    html = open(CUM, encoding="utf-8").read()
    # 计数更新
    html = html.replace('<span class="tag">84 卡</span>', '<span class="tag">87 卡</span>', 1)
    html = html.replace('<span class="tag">138 卡</span>', '<span class="tag">139 卡</span>', 1)
    # exec 卡插入到 <div class="sec sec2"> 之前
    exec_html = "".join(card_block(c) for c in EXEC_CARDS)
    assert '<div class="sec sec2">' in html
    html = html.replace('<div class="sec sec2">', exec_html + '<div class="sec sec2">', 1)
    # supervisor 卡插入到 <footer> 之前
    sup_html = "".join(card_block(c) for c in SUP_CARDS)
    assert '<footer>' in html
    html = html.replace('<footer>', sup_html + '<footer>', 1)
    # hero <p> 追加本轮纪要（在 hero 内第一个 </p> 前）
    hp = html.find('<div class="hero">')
    pe = html.find('</p>', hp)
    assert pe != -1
    round_txt = (' ｜ 本轮补采 +' + str(len(CARDS)) + '（' + VN + '，②×' + str(len(SUP_CARDS))
                 + '/③×' + str(len(EXEC_CARDS)) + '）：高管团队运营章程(Monkhouse)、董事会-CEO 运营协议(managingthefuture)、'
                   '联席 CEO/共治协议(ceonextchapter)（③）；越级会谈·领导者实战手册(performanceninja)（②）')
    html = html[:pe] + round_txt + html[pe:]
    open(CUM, "w", encoding="utf-8").write(html)
    print("累计墙已更新:", CUM, len(html), "字节（exec +%d, sup +%d）" % (len(EXEC_CARDS), len(SUP_CARDS)))

update_summary()

# ---------- 3) index.json 去重 + 追加 ----------
def normkey(t):
    out = []
    for ch in t.lower():
        if ch.isalnum() or ("\u4e00" <= ch <= "\u9fff"):
            out.append(ch)
    return "".join(out)

def update_index():
    data = json.load(open(IDX, encoding="utf-8"))
    exist_urls = {e.get("url", "").lower().rstrip("/") for e in data}
    exist_keys = {e.get("normKey", "") for e in data if e.get("topic") == "icebreaker"}
    added = 0
    for c in CARDS:
        u = c["url"].lower().rstrip("/")
        k = normkey(c["title"])
        if u in exist_urls or k in exist_keys:
            print("SKIP 重复:", c["title"][:30]); continue
        entry = {
            "title": c["title"],
            "normKey": k,
            "url": c["url"],
            "sourceType": "primary" if c["src"] == "b1" else "secondary",
            "relation": c["rel"],
            "summary": (c["cat"] + "：" + c["val"][:60]),
            "topic": "icebreaker",
        }
        data.append(entry); added += 1; exist_urls.add(u); exist_keys.add(k)
    json.dump(data, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    ib = sum(1 for e in data if e.get("topic") == "icebreaker")
    print("index.json 本轮新增:", added, "-> icebreaker 现", ib, "条，总", len(data), "条")

update_index()

# ---------- 4) Obsidian：破冰-知识卡汇总.md ----------
def update_note():
    if not os.path.exists(NOTE_PATH):
        print("⚠️ 笔记不存在，跳过:", NOTE_PATH); return
    t = open(NOTE_PATH, encoding="utf-8").read()
    # 更新 frontmatter date
    t = re.sub(r'(date:\s*)\d{4}-\d{2}-\d{2}', r'\g<1>' + VN, t, count=1)
    # 更新「本轮增量页」行（2026-08-27→2026-08-28，URL 指向 icebreaker-20260828.html）
    t = re.sub(r'\*\*本轮增量页（[^）]*）\*\*：\[[^\]]*\]\([^)]*\)',
               '**本轮增量页（' + VN + '）**：[icebreaker-20260828.html · GitHub Pages](' + GP_URL + '/icebreaker-20260828.html)',
               t, count=1)
    t = re.sub(r'\*\*本机源\*\*：`[^`]*`',
               '**本机源**：`knowledge-collection/icebreaker/icebreaker-20260828.html`', t, count=1)
    # 在「## 卡片总表」前插入本轮纪要 blockquote
    round_q = ('\n> ' + ROUND_LABEL + '（③×' + str(len(EXEC_CARDS)) + '/②×' + str(len(SUP_CARDS))
               + '）：高管团队运营章程·6承诺+DRI+禁三角传递(Monkhouse)、董事会-CEO 运营协议·四级决策权(managingthefuture)、'
                 '联席 CEO/共治团队协议·四领域(ceonextchapter)（③）；越级会谈·领导者实战手册(performanceninja)（②）\n')
    if '## 卡片总表' in t and round_q.strip() not in t:
        t = t.replace('## 卡片总表', round_q + '## 卡片总表', 1)
    # 追加卡片总表行（延续编号）
    nums = [int(m.group(1)) for m in re.finditer(r'^\|\s*(\d+)\s*\|', t, re.M)]
    last = max(nums) if nums else 0
    rows = []
    for c in CARDS:
        last += 1
        rel_cell = "③高管间" if c["rel"] == "exec" else "②上下级"
        src_cell = "一手" if c["src"] == "b1" else "二手"
        rows.append("| %d | %s | %s | %s | %s |" % (last, esc(c["title"]), rel_cell, src_cell, esc(c["val"][:80] + "…")))
    row_block = "\n".join(rows) + "\n"
    # 插到文件末尾（最后一个表格行之后）
    t = t.rstrip("\n") + "\n" + row_block
    # 更新「222 卡」计数（改为实际 max+4）
    new_total = last
    t = re.sub(r'（\d+ 卡 · 仅②/③）', '（%d 卡 · 仅②/③）' % new_total, t, count=1)
    open(NOTE_PATH, "w", encoding="utf-8").write(t)
    print("Obsidian 笔记已更新:", NOTE_PATH, "（末尾追加 %d 行，总表至 %d 卡）" % (len(CARDS), new_total))

update_note()

# ---------- 5) Obsidian：00-知识采集索引.md ----------
def update_index00():
    if not os.path.exists(IDX00):
        print("⚠️ 00 索引不存在，跳过"); return
    t = open(IDX00, encoding="utf-8").read()
    # 标题行追加本轮标记（结尾全角 ）前）
    t = re.sub(r'(## 主题：破冰（[^）]*?)\s*）', lambda m: m.group(1) + ' ｜ ' + ROUND_LABEL + '）', t, count=1)
    # 在导航链接行后插入 4 卡明细 blockquote（不重复 nav 行）
    nav = '📄 主题汇总笔记：[[知识采集库/素材/icebreaker/破冰-知识卡汇总|破冰-知识卡汇总]]'
    assert nav in t, "nav line not found"
    bullet = (
        '\n> ' + ROUND_LABEL + ' 新增 ' + str(len(CARDS)) + ' 卡（仅②/③、0 peer）：\n'
        + '> - \U0001F4DC ' + esc(CARDS[0]["title"]) + '（③高管间·二手·Monkhouse）\n'
        + '> - \U0001F3DB\uFE0F ' + esc(CARDS[1]["title"]) + '（③高管间·二手·managingthefuture）\n'
        + '> - \U0001F91D ' + esc(CARDS[ 2]["title"]) + '（③高管间·二手·ceonextchapter）\n'
        + '> - \U0001F52D ' + esc(CARDS[3]["title"]) + '（②上下级·二手·performanceninja）\n'
    )
    t = t.replace(nav, nav + bullet, 1)
    open(IDX00, "w", encoding="utf-8").write(t)
    print("00-知识采集索引.md 已更新（破冰分区追加 4 卡明细）")

update_index00()

# ---------- 6) GitHub 同步 ----------
try:
    sync = os.path.join(os.path.dirname(BASE), "sync_knowledge_github.py")
    rs = subprocess.run(["python", sync], capture_output=True, text=True, timeout=300)
    print("sync_knowledge_github:", rs.returncode, (rs.stdout.strip()[-200:] if rs.stdout else ""),
          (rs.stderr.strip()[:200] if rs.stderr else ""))
except Exception as e:
    print("⚠️ GitHub 同步异常（告警不阻断）：" + str(e)[:200])

# ---------- 7) 乐享上传（whoami 探活；累计墙 in-place 更新 + 新建独立页）----------
MCP_JSON = r"C:/Users/v_yitcai/.workbuddy/mcp.json"
LEXIANG_URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"

class LexiangMCP:
    def __init__(self, token):
        self.token = token; self.session = None
    def _post(self, payload, retries=3):
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

def put_bytes(url, data, retries=3):
    last = None
    for _ in range(retries):
        try:
            req = urllib.request.Request(url, data=data, method="PUT")
            req.add_header("Content-Type", "text/html")
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.status
        except Exception as e:
            last = str(e); continue
    raise RuntimeError("PUT fail: " + str(last))

try:
    mp = json.load(open(MAP, encoding="utf-8"))
    ib_map = mp.setdefault("icebreaker", {})
    FOLDER = ib_map.get("folder_id") or "f51480b0cfac4857bc28495b151c624f"
    WALL = ib_map.get("wall", {})
    WALL_ENTRY = WALL.get("entry_id") or "637b3b31280140349221fbe6fa4e08ed"
    WALL_FILE = WALL.get("file_id") or "3c5c841631e54e1bb56474afc95af1b6"
    token = json.load(open(MCP_JSON, encoding="utf-8"))["mcpServers"]["lexiang"]["headers"]["Authorization"]
    mc = LexiangMCP(token); mc.initialize(); mc.initialized()
    try:
        w = mc.call("whoami", {})
        print("whoami:", json.dumps(mc.biz(w), ensure_ascii=False)[:120])
    except Exception as e:
        print("whoami 跳过:", str(e)[:120])
    # 7a) 累计墙 in-place 更新
    wall_bytes = open(CUM, "rb").read()
    r = mc.call("file_apply_upload", {"parent_entry_id": FOLDER, "name": "icebreaker.html",
                                      "extension":"html", "mime_type":"text/html",
                                      "upload_type":"PRE_SIGNED_URL", "size": str(len(wall_bytes)),
                                      "file_id": WALL_FILE, "entry_id": WALL_ENTRY})
    biz = mc.biz(r)
    if biz.get("code") != 0: raise RuntimeError("apply_upload(wall) FAIL {0}".format(biz.get("message")))
    sess = biz["data"]["session"]
    sid = sess.get("session_id") or sess.get("id")
    url = sess.get("upload_url") or sess["objects"][0]["upload_url"]
    st = put_bytes(url, wall_bytes)
    if st != 200: raise RuntimeError("PUT(wall) status " + str(st))
    r2 = mc.call("file_commit_upload", {"session_id": sid})
    biz2 = mc.biz(r2)
    if biz2.get("code") != 0: raise RuntimeError("commit(wall) FAIL " + str(biz2.get("message")))
    print("乐享累计墙 in-place 更新 OK entry_id=", WALL_ENTRY)
    # 7b) 新建独立页 icebreaker-20260828.html
    run_bytes = open(INC_PATH, "rb").read()
    r = mc.call("file_apply_upload", {"parent_entry_id": FOLDER, "name": INC_NAME,
                                      "extension":"html", "mime_type":"text/html",
                                      "upload_type":"PRE_SIGNED_URL", "size": str(len(run_bytes))})
    biz = mc.biz(r)
    if biz.get("code") != 0: raise RuntimeError("apply_upload(run) FAIL {0}".format(biz.get("message")))
    sess = biz["data"]["session"]
    sid = sess.get("session_id") or sess.get("id")
    url = sess.get("upload_url") or sess["objects"][0]["upload_url"]
    st = put_bytes(url, run_bytes)
    if st != 200: raise RuntimeError("PUT(run) status " + str(st))
    r2 = mc.call("file_commit_upload", {"session_id": sid})
    biz2 = mc.biz(r2)
    if biz2.get("code") != 0: raise RuntimeError("commit(run) FAIL " + str(biz2.get("message")))
    rid = biz2["data"]["entry"]["id"]
    print("乐享新建独立页 OK entry_id=", rid)
    # 7c) 回写 map
    ib_map["folder_id"] = FOLDER
    ib_map["wall"] = {"entry_id": WALL_ENTRY, "file_id": WALL_FILE, "name": "icebreaker.html",
                      "note": "累计墙（226卡）in-place 更新"}
    rec = {"date": VN, "entry_id": rid, "name": INC_NAME, "note": "轮次页（+%d）" % len(CARDS)}
    if not any(x.get("name") == INC_NAME for x in ib_map.get("rounds", [])):
        ib_map.setdefault("rounds", []).append(rec)
    json.dump(mp, open(MAP, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("已回写 lexiang-entry-map.json（wall + rounds）")
except Exception as e:
    print("⚠️ 乐享上传跳过（warning，不中断）：" + str(e)[:300])

# ---------- 8) last-topic.txt 推进 ----------
lt = os.path.join(BASE, "last-topic.txt")
open(lt, "w", encoding="utf-8").write("颁奖\n")
print("last-topic.txt -> 颁奖")

print("\n=== 破冰本轮完成：新增 %d 卡（③×%d / ②×%d）；增量页 %s；累计墙 +%d；00索引/笔记已更新 ==="
      % (len(CARDS), len(EXEC_CARDS), len(SUP_CARDS), INC_PATH, len(CARDS)))
