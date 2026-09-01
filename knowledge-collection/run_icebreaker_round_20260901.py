# -*- coding: utf-8 -*-
"""破冰 本轮补采 (2026-09-01) — 仅②③（0 peer）。
新增 4 张经六维评估通过、与既有 217 卡去重后的卡（③×2 / ②×2），
覆盖治理层决策权新角度（RAPID 单点问责·Bain 一手）+ 高管同侪顾问网络，
以及上下级新角度（一线经理 1:1 实战·主动倾听/开放式提问/去干扰 + 远程虚拟 1:1 四法）。
流程：临时新卡 HTML → gen_run_page 独立页 → 累计墙追加 → index.json → Obsidian(00索引/破冰汇总/runs独立笔记) → GitHub → 乐享(whoami 探活·累计墙更新+新建独立页)。
"""
import json, os, re, subprocess, urllib.request, urllib.error

BASE = os.path.dirname(os.path.abspath(__file__))
AT = os.path.join(BASE, "icebreaker")
CUM = os.path.join(AT, "icebreaker.html")
TMP = os.path.join(AT, ".run_newcards.tmp.html")
RUNS = os.path.join(AT, "runs")
IDX = os.path.join(BASE, "index.json")
MAP = os.path.join(BASE, "lexiang-entry-map.json")
VN = "2026-09-01"
ROUND = 25
RUN_NAME = "icebreaker-2026-09-01-r%d.html" % ROUND
RUN_PATH = os.path.join(RUNS, RUN_NAME)
IDX00 = r"C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库/00-知识采集索引.md"
NOTE_PATH = r"C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库/素材/icebreaker/破冰-知识卡汇总.md"
RUNS_NOTE = r"C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库/素材/icebreaker/runs/icebreaker-2026-09-01-第%d轮-知识卡.md" % ROUND
GP_URL = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker"
RUN_GP = GP_URL + "/runs/" + RUN_NAME
VAULT_RUNS = "knowledge-collection/icebreaker/runs/" + RUN_NAME
ROUND_LABEL = "二十五轮补采 +4（2026-09-01，②×2/③×2）"

def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

CARDS = [
    {
        "emoji": "\U0001F3AF",  # 🎯
        "title": "高管团队决策权 RAPID 模型·R/A/P/I/D 五角色单点问责（Bain 一手）",
        "cat": "决策权治理",
        "rel": "exec", "rel_text": "高管间", "src": "b1", "src_text": "一手",
        "val": "决策是企业硬通货，但模糊的问责常卡死决策。Bain 调研 350+ 全球组织：仅约 15% 做到有效决策；瓶颈多在「谁对这决策负责」不清晰。解法 RAPID（Recommend/Agree/Perform/Input/Decide）：R 提议（牵头收集分析、给备选）、A 同意（必须签批才能推进，如法务/合规；有否决权但须给替代方案或升级）、P 执行（落地，越早卷入越接地气）、I 输入（提供事实与判断，无否决权）、D 决定（唯一一人拍板、对结果负全责——「有 D 的人」）。关键纪律：①全公司只允许一个 D，两个 D=拔河；②A 过多=瘫痪（说明决策没下放够）；③I 过多=噪声；④RAPID 是决策速度与治理（高管层），RACI 是执行纪律（交付层），二者不同层、互补。落地：用一页「决策地图」把最关键 20-30 个决策列成行、R/A/P/I/D 成列，标出单点 D 与必要否决；做一场 90 分钟「决策权审计」——列决策→定 D→标 A/I→用真实流程压测→每季度回看。",
        "exec": "给最关键 20-30 个决策画「决策地图」：每决策单点问责（唯一 Decider=「有 D 的人」）+ R(提议) 收分析 / I(输入) 给事实无否决 / A(同意) 必要会签可否决但须给替代 / P(执行)。避坑：只允许一个 D、A 过多=瘫痪、I 过多=噪声；RACI 管执行纪律、RAPID 管决策速度与治理，二者不同层。90 分钟决策权审计：列决策→定 D→标 A/I→用真实流程压测→每季度回看刷新。",
        "url": "https://bain.com/insights/manager-at-work-who-has-the-d",
        "url_disp": "bain.com/insights/manager-at-work-who-has-the-d",
        "note": "适用：③ 高管团队决策权治理——RAPID 五角色（R/A/P/I/D）单点问责「有 D 的人」+ 避 A/I 泛滥 + RACI(执行)≠RAPID(决策) 双轨 + 90min 决策权审计（高管间，治理层，非游戏，Bain 一手方法论）。",
    },
    {
        "emoji": "\U0001F91D",  # 🤝
        "title": "CEO 同侪顾问董事会·保密非竞争高管圈 + 结构化议题处理 + 互问责",
        "cat": "高管同侪网络",
        "rel": "exec", "rel_text": "高管间", "src": "b2", "src_text": "二手",
        "val": "「高处不胜寒」的孤立是 CEO 决策质量的最大隐性杀手。破法：搭一个「同侪顾问董事会」——甄选 12-16 位非竞争行业 CEO/高管，每月一次保密结构化聚会，由资深主席（曾任 CEO）引导。运作三要素：①保密同侪圈：成员零竞争冲突、跨行业多样，敢说真话；②结构化议题处理（issue-processing framework）：把真实挑战摆上桌——挑战无评判、共享问责（你承诺行动，同侪期待你回报进展）；③配 1:1 教练。价值：多视角打磨决策、战略优先级更清、压力下有底气、破解孤立。Vistage 模式（1957 至今、45k+ 成员）：成员公司营收增长显著优于同业，核心在「持续挑战+支持+视角」而非单次 networking。落地提醒：成员零竞争冲突、保密为基、主席懂引导、定期复盘问责，别把它办成社交局。",
        "exec": "为高管建「同侪顾问董事会」：甄选 12-16 位非竞争行业 CEO/高管，每月一次保密结构化聚会，由资深主席（曾任 CEO）引导；用「议题处理框架」把真实挑战摆上桌——挑战无评判、共享问责（你承诺行动，同侪期待你回报进展）。配 1:1 教练。价值：多视角打磨决策、战略优先级更清、压力下有底气、破解「高处不胜寒」的孤立。落地提醒：成员零竞争冲突、保密为基、定期复盘问责。",
        "url": "https://www.vistage.com.au/leadership/beyond-networking-how-peer-advisory-gives-ceos-the-edge",
        "url_disp": "vistage.com.au/leadership/beyond-networking-how-peer-advisory-gives-ceos-the-edge",
        "note": "适用：③ 高管同侪顾问网络——非竞争 CEO 保密圈 + 资深主席引导 + 结构化议题处理 + 共享问责（高管间，治理/成长层，非游戏；Vistage 实践模式，二手）。",
    },
    {
        "emoji": "\U0001F4AC",  # 💬
        "title": "一线经理 1:1 会议实战·主动倾听 + 开放式提问 + 去干扰 + 问题库",
        "cat": "经理 1:1",
        "rel": "supervisor", "rel_text": "上下级", "src": "b2", "src_text": "二手",
        "val": "1:1 是反馈与关系的核心机制，不是进度汇报。主动倾听：眼神接触、对方说完先停 2 秒再回、复述确认「我听到的是…对吗」；远程更要刻意——镜头齐眼、看屏幕而非自己、关掉可见干扰。开放式提问优于是非题（what/how/讲讲看），邀对方展开而非确认。彻底去干扰：关标签页、静通知、锁门/戴耳机——分心=「你不重要」的信号，破坏信任。把自我放门外（Susan Scott《Fierce Conversations》：别用你的战例抢走对方的话；问「你觉得该怎么做」后闭嘴）。按目的建问题库：关系破冰 / 当前工作 / 卡点与阻塞 / 成长发展 / 对「我作为你上级」的反馈。HBR 研究：员工发言应占会议 50-90% 才有效。",
        "exec": "把 1:1 当教练对话而非进度汇报：①主动倾听——眼神接触、对方说完先停 2 秒再回、复述确认「我听到的是…对吗」；②开放式提问（what/how/讲讲看）替代是非题；③彻底去干扰——关标签页、静通知、锁门/戴耳机；④把自我放门外（少讲自己的战例、问「你觉得该怎么做」后闭嘴）。按目的建问题库：关系/当前工作/卡点/成长/对「我作为你上级」的反馈；员工发言占 50-90% 才有效。",
        "url": "https://fellow.ai/blog/one-on-one-meeting-definitive-guide/",
        "url_disp": "fellow.ai/blog/one-on-one-meeting-definitive-guide",
        "note": "适用：② 一线经理↔直属下属 1:1 实战——主动倾听+开放式提问+去干扰+问题库（上下级，leader↔individual contributor，非游戏）。",
    },
    {
        "emoji": "\U0001F310",  # 🌐
        "title": "远程/虚拟 1:1 四法·让下属选时段 + 用视频 + 培养独立 + 按节奏建关系",
        "cat": "远程 1:1",
        "rel": "supervisor", "rel_text": "上下级", "src": "b2", "src_text": "二手",
        "val": "远程团队信任建立更慢，1:1 要更用心。四法（Ken Blanchard）：①让下属自己选时段——精力有波动，选其不赶deadline、愿反思的时段，让通话成「连接/投资」而非打扰；②用技术「显更多」——优先视频，纯语音时听「说出的/未说的/语气下的」；③用提问培养独立性——「还有哪些因素在影响」「什么在挡路」「怎么知道计划奏效」，把下属练成能自己推进；④按对方节奏建关系——你先透明示范，但不强求亲密，每次 1-2 个开放式问题，让下属掌控分享程度。核心：距离不应让人疏远，关系资本靠持续小动作积累。",
        "exec": "远程团队信任建立更慢，1:1 四法：①让下属自己选时段（尊重其精力节律，别变成打扰）；②用技术「显更多」——优先视频，纯语音时听「说出的/未说的/语气下的」；③用提问培养独立性（还有哪些因素在影响？什么在挡路？怎么知道计划奏效？）；④按对方节奏建关系——你先透明示范，但不强求亲密，每次 1-2 个开放式问题，让下属掌控分享程度。",
        "url": "https://leaderchat.org/2014/01/23/four-ways-to-increase-the-power-and-quality-of-virtual-one-on-one-meetings/",
        "url_disp": "leaderchat.org/2014/01/23/four-ways-to-increase-the-power-and-quality-of-virtual-one-on-one-meetings",
        "note": "适用：② 远程/混合团队经理↔下属 1:1——让下属选时段+用视频+培养独立+按节奏建关系（上下级，远程场景，非游戏；Blanchard 实践，二手）。",
    },
]

def card_block(c):
    rb = 'r3' if c["rel"] == "exec" else 'r2'
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
        rb=rb, rel_text=esc(c["rel_text"]), src=c["src"], src_text=esc(c["src_text"]),
        val=esc(c["val"]), exec_inner=esc(c["exec"]), url=c["url"], url_disp=esc(c["url_disp"]),
        note=esc(c["note"]),
    )

EXEC_CARDS = [c for c in CARDS if c["rel"] == "exec"]
SUP_CARDS = [c for c in CARDS if c["rel"] == "supervisor"]
print("EXEC:", len(EXEC_CARDS), "SUP:", len(SUP_CARDS), "TOTAL:", len(CARDS))

# ---------- 1) 临时新卡 HTML（供 gen_run_page 拆分）----------
open(TMP, "w", encoding="utf-8").write("".join(card_block(c) for c in CARDS))
print("临时新卡写入:", TMP)

# ---------- 2) gen_run_page 生成独立页 ----------
try:
    rs = subprocess.run(
        ["python", os.path.join(BASE, "gen_run_page.py"),
         "--topic", "icebreaker", "--topic-name", "破冰",
         "--date", VN, "--round", str(ROUND),
         "--cards-file", TMP],
        capture_output=True, text=True, timeout=120)
    print("gen_run_page:", rs.returncode, (rs.stdout.strip()[-160:] if rs.stdout else ""),
          (rs.stderr.strip()[:160] if rs.stderr else ""))
except Exception as e:
    print("⚠️ gen_run_page 异常:", str(e)[:160])

# ---------- 3) 累计墙 icebreaker.html 追加 ----------
def update_summary():
    html = open(CUM, encoding="utf-8").read()
    html = html.replace('<span class="tag">87 卡</span>', '<span class="tag">89 卡</span>', 1)
    html = html.replace('<span class="tag">139 卡</span>', '<span class="tag">141 卡</span>', 1)
    exec_html = "".join(card_block(c) for c in EXEC_CARDS)
    assert '<div class="sec sec2">' in html
    html = html.replace('<div class="sec sec2">', exec_html + '<div class="sec sec2">', 1)
    sup_html = "".join(card_block(c) for c in SUP_CARDS)
    assert '<footer>' in html
    html = html.replace('<footer>', sup_html + '<footer>', 1)
    hp = html.find('<div class="hero">')
    pe = html.find('</p>', hp)
    assert pe != -1
    round_txt = (' ｜ 二十五轮补采 +4（2026-09-01，②×2/③×2）：高管团队决策权 RAPID 模型(Bain·一手)、'
                 'CEO 同侪顾问董事会(Vistage)（③）；一线经理 1:1 实战(fellow.ai)、远程/虚拟 1:1 四法(Blanchard)（②）')
    html = html[:pe] + round_txt + html[pe:]
    open(CUM, "w", encoding="utf-8").write(html)
    print("累计墙已更新:", CUM, len(html), "字节（exec +%d, sup +%d）" % (len(EXEC_CARDS), len(SUP_CARDS)))

update_summary()

# ---------- 4) index.json 去重 + 追加 ----------
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

# ---------- 5) Obsidian：破冰-知识卡汇总.md ----------
def update_note():
    if not os.path.exists(NOTE_PATH):
        print("⚠️ 笔记不存在，跳过:", NOTE_PATH); return
    t = open(NOTE_PATH, encoding="utf-8").read()
    t = re.sub(r'(date:\s*)\d{4}-\d{2}-\d{2}', r'\g<1>' + VN, t, count=1)
    t = re.sub(r'\*\*本轮增量页（[^）]*）\*\*：\[[^\]]*\]\([^)]*\)',
               '**本轮增量页（' + VN + '）**：[icebreaker-2026-09-01-r%d.html · GitHub Pages](%s)' % (ROUND, RUN_GP),
               t, count=1)
    t = re.sub(r'\*\*本机源\*\*：`[^`]*`',
               '**本机源**：`' + VAULT_RUNS + '`', t, count=1)
    round_q = ('\n> ' + ROUND_LABEL + '：高管团队决策权 RAPID 模型·五角色单点问责(Bain·一手)、'
               'CEO 同侪顾问董事会·保密非竞争高管圈(Vistage)（③）；一线经理 1:1 实战·主动倾听+开放式提问+去干扰(fellow.ai)、'
               '远程/虚拟 1:1 四法·让下属选时段+用视频+培养独立(Blanchard)（②）\n')
    if '## 卡片总表' in t and round_q.strip() not in t:
        t = t.replace('## 卡片总表', round_q + '## 卡片总表', 1)
    nums = [int(m.group(1)) for m in re.finditer(r'^\|\s*(\d+)\s*\|', t, re.M)]
    last = max(nums) if nums else 0
    rows = []
    for c in CARDS:
        last += 1
        rel_cell = "③高管间" if c["rel"] == "exec" else "②上下级"
        src_cell = "一手" if c["src"] == "b1" else "二手"
        rows.append("| %d | %s | %s | %s | %s |" % (last, esc(c["title"]), rel_cell, src_cell, esc(c["val"][:80] + "…")))
    row_block = "\n".join(rows) + "\n"
    t = t.rstrip("\n") + "\n" + row_block
    new_total = last
    t = re.sub(r'（\d+ 卡 · 仅②/③）', '（%d 卡 · 仅②/③）' % new_total, t, count=1)
    open(NOTE_PATH, "w", encoding="utf-8").write(t)
    print("Obsidian 笔记已更新:", NOTE_PATH, "（末尾追加 %d 行，总表至 %d 卡）" % (len(CARDS), new_total))

update_note()

# ---------- 6) Obsidian：00-知识采集索引.md ----------
def update_index00():
    if not os.path.exists(IDX00):
        print("⚠️ 00 索引不存在，跳过"); return
    t = open(IDX00, encoding="utf-8").read()
    t = re.sub(r'(## 主题：破冰（[^）]*?)\s*）', lambda m: m.group(1) + ' ｜ ' + ROUND_LABEL + '）', t, count=1)
    nav = '📄 主题汇总笔记：[[知识采集库/素材/icebreaker/破冰-知识卡汇总|破冰-知识卡汇总]]'
    assert nav in t, "nav line not found"
    bullet = (
        '\n> ' + ROUND_LABEL + ' 新增 ' + str(len(CARDS)) + ' 卡（仅②/③、0 peer）：\n'
        + '> - \U0001F3AF ' + esc(CARDS[0]["title"]) + '（③高管间·一手·Bain）\n'
        + '> - \U0001F91D ' + esc(CARDS[1]["title"]) + '（③高管间·二手·Vistage）\n'
        + '> - \U0001F4AC ' + esc(CARDS[2]["title"]) + '（②上下级·二手·fellow.ai）\n'
        + '> - \U0001F310 ' + esc(CARDS[3]["title"]) + '（②上下级·二手·Blanchard）\n'
    )
    t = t.replace(nav, nav + bullet, 1)
    open(IDX00, "w", encoding="utf-8").write(t)
    print("00-知识采集索引.md 已更新（破冰分区追加 4 卡明细）")

update_index00()

# ---------- 7) Obsidian：runs 独立笔记 ----------
def write_runs_note():
    os.makedirs(os.path.dirname(RUNS_NOTE), exist_ok=True)
    rows = []
    for c in CARDS:
        rel_cell = "③高管间" if c["rel"] == "exec" else "②上下级"
        src_cell = "一手" if c["src"] == "b1" else "二手"
        rows.append("| %s | %s | %s | %s |" % (esc(c["title"]), rel_cell, src_cell, esc(c["val"][:90] + "…")))
    md = (
        "---\n"
        "title: 破冰·第%d轮知识卡（2026-09-01）\n"
        "tags: [知识采集, 自动化采集, 破冰, 第%d轮]\n"
        "date: 2026-09-01\ntype: 自动化采集\nrelation: [supervisor, exec]\nsource_topic: 破冰\n"
        "---\n\n"
        "# 破冰 · 第%d轮知识卡（2026-09-01）\n\n"
        "> 本轮 +4 卡（②上下级 ×2 / ③高管间 ×2，0 peer）。六维评估（含关系适配度）全过，一手/二手标注，历史去重。\n\n"
        "**独立页（GitHub Pages）**：[%s](%s)\n\n"
        "**本机源**：`%s`\n\n"
        "## 本轮卡片\n\n"
        "| 卡片 | 关系档 | 一手/二手 | 核心要点 |\n|---|---|---|---|\n"
        "%s\n"
    ) % (ROUND, ROUND, ROUND, RUN_NAME, RUN_GP, VAULT_RUNS, "\n".join(rows))
    open(RUNS_NOTE, "w", encoding="utf-8").write(md)
    print("runs 独立笔记已写:", RUNS_NOTE)

write_runs_note()

# ---------- 8) GitHub 同步 ----------
try:
    sync = os.path.join(os.path.dirname(BASE), "sync_knowledge_github.py")
    rs = subprocess.run(["python", sync], capture_output=True, text=True, timeout=300)
    print("sync_knowledge_github:", rs.returncode, (rs.stdout.strip()[-200:] if rs.stdout else ""),
          (rs.stderr.strip()[:200] if rs.stderr else ""))
except Exception as e:
    print("⚠️ GitHub 同步异常（告警不阻断）：" + str(e)[:200])

# ---------- 9) 乐享上传（whoami 探活；累计墙 in-place 更新 + 新建独立页）----------
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
    # 9a) 累计墙 in-place 更新
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
    # 9b) 新建独立页
    run_bytes = open(RUN_PATH, "rb").read()
    r = mc.call("file_apply_upload", {"parent_entry_id": FOLDER, "name": RUN_NAME,
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
    ib_map["folder_id"] = FOLDER
    ib_map["wall"] = {"entry_id": WALL_ENTRY, "file_id": WALL_FILE, "name": "icebreaker.html",
                      "note": "累计墙（221卡）in-place 更新"}
    rec = {"date": VN, "entry_id": rid, "name": RUN_NAME, "note": "轮次页（+%d）" % len(CARDS)}
    if not any(x.get("name") == RUN_NAME for x in ib_map.get("rounds", [])):
        ib_map.setdefault("rounds", []).append(rec)
    json.dump(mp, open(MAP, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("已回写 lexiang-entry-map.json（wall + rounds）")
except Exception as e:
    print("⚠️ 乐享上传跳过（warning，不中断）：" + str(e)[:300])

# ---------- 10) last-topic.txt 推进 ----------
lt = os.path.join(BASE, "last-topic.txt")
open(lt, "w", encoding="utf-8").write("颁奖\n")
print("last-topic.txt -> 颁奖")

print("\n=== 破冰本轮完成：新增 %d 卡（③×%d / ②×%d）；独立页 %s；累计墙 +%d；00索引/笔记/runs笔记已更新 ==="
      % (len(CARDS), len(EXEC_CARDS), len(SUP_CARDS), RUN_PATH, len(CARDS)))
