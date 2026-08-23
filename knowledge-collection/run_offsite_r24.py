# -*- coding: utf-8 -*-
# 知识采集自动化 · Offsite 第二十四轮（2026-08-23）补采
# 主题：Offsite 团建务虚 ｜ 覆盖关系档：③高管间(2) / ②上下级(3) ｜ 剔除①平级
import os, re, json, subprocess, datetime

KC = r"C:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection"
WALL = os.path.join(KC, "offsite", "offsite.html")
TMP = os.path.join(KC, "offsite", ".run_newcards.tmp.html")
IDX = os.path.join(KC, "index.json")
OBS_SUM = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\offsite\Offsite-团建务虚-知识卡汇总.md"
OBS_00 = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
RUNS_NOTE = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\offsite\runs\Offsite-2026-08-23-第二十四轮-知识卡.md"
DATE = "2026-08-23"
ROUND = 24
TOPIC = "offsite"

# ---------- 5 张新卡 ----------
CARDS = [
    {
        "emoji": "🎯", "cat": "引导方法论", "rel": "r3", "rel_label": "高管间",
        "title": "高管 Offsite 引导：按「决策顺序」而非「主题桶」构建议程",
        "url": "https://averiadvisory.com/strategic-offsite-facilitation-for-executives/",
        "val": "核心主张——议程围绕「决策顺序」而非「主题桶」搭建：①澄清背景与约束→②检验假设→③辩论选项→④分配责任（颠倒会引发过早站位与政治防御）。形式：长汇报挤占思考氧气，用预读材料承载信息负载，会议室只做挑战、综合与决策。引导者需「超越中立」——保护对话质量但不夺取决策所有权，能在虚假共识固化前打断、点名被回避的权衡、在推理未支撑承诺时放慢节奏。会前保密访谈（非通用问卷）暴露断层线：对齐被夸大、假设分歧、决策权不清。",
        "exec_inner": "办高管 offsite 学 Averi「决策顺序四步 + 超越中立的引导者」：会前保密访谈摸断层线→议程按「澄清→检验→辩论→分配责任」排序（不按主题堆砌）→预读承载信息、现场只做决策→引导者护质量不夺权、在虚假共识固化前打断、点名被回避的权衡。何时请外部：模糊代价高 / 层级压制坦诚 / 需系统内无人能提供的纪律性挑战（结构变革、资本部署、领导层过渡、董事会审查）。",
        "note": "适用：③ 高管团队 offsite 引导设计，「决策顺序替代主题桶 + 引导者超越中立 + 何时请外部」，可作议程与引导师选型方法论。（咨询机构二手；2026-04 发布，强在「决策序列 + 引导者权威边界 + 外部引导触发点」）",
        "summary": "Averi Advisory 高管 offsite 引导方法论：议程按决策顺序（澄清→检验→辩论→分配责任）而非主题桶，引导者超越中立护对话质量不夺决策权，并给外部引导触发条件。",
        "quality": 4,
    },
    {
        "emoji": "🎤", "cat": "议程设计", "rel": "r3", "rel_label": "高管间",
        "title": "高管 Offsite 议程：先「对齐」不「汇报」+ 把讨论变承诺",
        "url": "https://www.chartwellspeakers.com/leadership-offsite-agenda-ideas-with-speaker-formats-that-land/",
        "val": "最强 offsite 不再围绕密集幻灯片与被动听，而创造清晰度、信任与可执行产出。关键做法：①开场用引导对话替代运营汇报——三问「自上次规划周期什么变了 / 哪些假设不再成立 / 哪里需要更快决策」，快速浮现优先级；②留专门决策时间块（战略优先级 / 资源分配 / 风险评估 / 责任指派），让输入→讨论→决策→问责闭环；③用工作坊解真实业务挑战（跨职能协作、变革通信、客户信任、AI 治理、继任）；④外部讲者兼引导师比纯演讲更易落地。结尾每人明确承诺 + 时间线，否则讨论回日常即失速。",
        "exec_inner": "设计高管 offsite 学 Chartwell「开场对齐三问替代汇报 + 专设决策时间块 + 真实挑战工作坊 + 讲者兼引导」：用三问浮优先级、每个 session 落到决策与 owner、用真实业务挑战做参与式工作坊、外部讲者带引导、结尾 capture 承诺与时限；并盯能量（别全程高浓度）、心理安全、时间纪律、每节明确「决定了什么 / 谁负责」。",
        "note": "适用：③ 高管团队 offsite 议程，「对齐三问替代汇报 + 决策时间块 + 真实挑战工作坊」，可作讲者/引导师选型与议程骨架。（讲者机构二手，方法论可采；偏「对话设计 + 讲者即引导」）",
        "summary": "Chartwell 高管 offsite 议程：用「对齐三问」替代运营汇报开场，专设决策时间块把讨论变承诺，以真实业务挑战工作坊 + 讲者兼引导落地。",
        "quality": 4,
    },
    {
        "emoji": "🛠️", "cat": "会前预工", "rel": "r2", "rel_label": "上下级",
        "title": "团队 Offsite 100 招：会前预工系统 + 「不尬」信任建设",
        "url": "https://www.consultclarity.org/post/100-team-offsite-ideas-that-actually-drive-results-2026",
        "val": "让 offsite 出结果的会前/会中系统：预工——①发背景文档 + 关键指标 + 每人需思考的问题；②会前个人书面反思（什么有效/无效/在回避什么/需要团队什么）；③匿名预调研让不敢当面说的真话浮现；④高 stakes 场做 1:1 保密访谈「什么让这成为好 offsite / 团队在回避什么对话」；⑤明确决策权（哪些 CEO 定 / 需共识 / 荐董事会）。议程架构——先连接后内容、硬决策放上午脑力峰值、留刻意留白（走廊对话才是真信任）、每区块设决策检查点（决定了什么/谁负责/下一步）、可见停车场、每日收尾整合、结尾具体承诺（做什么/何时/如何衡量）当场记录 24h 内共享。信任建设不尬——个人史（Lencioni 低风险成长背景分享）、结构化配对对话、Just Like Me 反思、工作风格偏好互述。",
        "exec_inner": "带团队 offsite 学 ConsultClarity「会前预工五件套 + 议程架构八法 + 不尬信任」：会前发背景+个人反思+匿名调研+高 stakes 1:1+厘清决策权；议程先连接、硬决策上午做、留白、每区块 capture 决策与 owner、停车场、每日整合、结尾承诺 24h 共享；信任用个人史/配对/Just Like Me 替代信任 fall。",
        "note": "适用：② 一线/中层 manager 带团队 offsite 的「会前预工 + 议程架构 + 不尬信任建设」全系统，可作策划 checklist。（咨询机构二手；2026 百招精选，强在「预工 + 决策检查点 + 不尬信任」）",
        "summary": "ConsultClarity 团队 offsite 100 招：会前预工五件套（背景/反思/匿名调研/1:1/决策权）+ 议程架构八法 + 不尬信任建设，把讨论变承诺并 24h 共享。",
        "quality": 4,
    },
    {
        "emoji": "📈", "cat": "ROI 测算", "rel": "r2", "rel_label": "上下级",
        "title": "Offsite ROI 测算：SMART 目标 + 有形/无形收益 + 成本三分",
        "url": "https://www.offsite.com/blog/maximizing-corporate-retreat-roi-evaluating-the-effectiveness-of-team-offsites",
        "val": "给 manager 向老板/CFO 证明 offsite 值得的测算框架：①SMART 目标（具体可衡量有时限）；②有形收益——项目完成率升、错误降、离职率降（留存即省钱）；③无形收益——团队凝聚力 / 创造力 / 文化（难量化但关键）；④成本三分——直接（差旅/场地/餐饮）、间接（规划占用工时/产能损失）、杂项（保险/设备租赁/意外），人均约 $4,000；⑤KPI——前后调研比对满意度/同伴感/凝聚力，项目完成率/协作频次/绩效；⑥ROI=(净收益/总成本)×100%，把软收益翻译成货币（如避免的离职成本）。",
        "exec_inner": "向老板证明 offsite 价值学 Offsite.com「SMART 目标 + 有形/无形双轨 + 成本三分 + 前后调研 KPI + ROI 公式」：先定可衡量目标；量化生产力/留存等有形与凝聚力等无形；成本拆直接/间接/杂项；会前会后用调研与完成率/协作频次做 KPI；用 ROI=(净收益/总成本)×100% 把软收益货币化。",
        "note": "适用：② 团队 lead/行政向管理层证明 offsite 预算合理性的「ROI 测算 + KPI + 前后调研」框架，可作立项/复盘报告模板。（平台商二手，方法论可采；含 $4,000/人 成本基准与 ROI 公式）",
        "summary": "Offsite.com 的 offsite ROI 测算框架：SMART 目标 + 有形/无形双轨收益 + 成本三分（直接/间接/杂项）+ 前后调研 KPI + ROI=(净收益/总成本)×100%。",
        "quality": 4,
    },
    {
        "emoji": "🚫", "cat": "活动设计", "rel": "r2", "rel_label": "上下级",
        "title": "团队 Offsite 活动「黑名单」与「真连接」清单 + 时段设计模板",
        "url": "https://www.teamdynamics.io/blog/examples-of-team-off-site-agendas-that-work-in-2023",
        "val": "可直接照抄的 manager 视角设计器：①「千万别做」清单——需身体暴露的、单独点名的、制造输家的竞赛、以酒为中心、信任 fall 等陈词滥调（强尬且伤信任）；②「真连接」清单——Personal Maps（分享背景兴趣）、Two Truths、Values Cards（聊什么重要）、Collaborative Challenges（一起解题）、Appreciation Circles（结构化正向反馈）；③每时段模板——开场10%/探索60%/综合20%/过渡10%，含目标与引导提示；④能量管理——每 90min 动一动、换物理空间、大小组交替、留户外；⑤清单——会前（场地/AV/物料/预读/饮食/紧急联系）、会中（引导/计时/停车场/拍照/反馈）、会后（48h 发纪要/跟行动/约跟进/收反馈）。",
        "exec_inner": "设计团队 offsite 学 TeamDynamics「黑名单 + 真连接清单 + 时段模板 + 能量管理 + 清单」：避开信任 fall/点名/输家竞赛/以酒为中心；用 Personal Maps/两真一假/价值观卡/协作挑战/欣赏圈建真实连接；每时段按开场10/探索60/综合20/过渡10 设计；每 90min 动一动换空间；会前/中/后清单兜底。",
        "note": "适用：② 一线/中层 manager 设计团队 offsite 活动与议程的「避坑清单 + 真连接活动库 + 时段模板 + 会后 48h」，可作策划速查。（测评工具商二手，清单实用；强在「活动黑名单 + 时段能量设计」）",
        "summary": "TeamDynamics 团队 offsite 设计器：活动黑名单（避信任 fall/点名/输家竞赛/以酒为中心）+ 真连接活动库 + 每时段 10/60/20/10 模板 + 能量管理与会前中后清单。",
        "quality": 4,
    },
]


def card_html(c):
    return (
        '    <div class="hl">\n'
        f'      <div class="top"><span class="emoji">{c["emoji"]}</span><h3>{c["title"]}</h3>'
        f'<span class="cat">{c["cat"]}</span><span class="badge {c["rel"]}">{c["rel_label"]}</span>'
        '<span class="badge b2">二手</span></div>\n'
        f'      <p class="val">{c["val"]}</p>\n'
        '      <details class="exec"><summary>怎么做</summary>'
        f'<div class="inner">{c["exec_inner"]}</div></details>\n'
        f'      <div class="src">🔗 <a href="{c["url"]}" target="_blank">{c["url"]}</a></div>\n'
        f'      <div class="note">{c["note"]}</div>\n'
        '    </div>\n'
    )


def main():
    # ---------- 1) 注入累计墙 ----------
    html = open(WALL, encoding="utf-8").read()
    before = html.count('<div class="hl">')

    cards_r3 = "".join(card_html(c) for c in CARDS if c["rel"] == "r3")
    cards_r2 = "".join(card_html(c) for c in CARDS if c["rel"] == "r2")

    # sec3 grid：在 <div class="sec sec2"> 之前、sec3 grid 闭合 </div> 之前插入
    sec2_marker = '<div class="sec sec2">'
    i = html.index(sec2_marker)
    j = html[:i].rfind('</div>')  # sec3 grid 闭合
    html = html[:j] + cards_r3 + html[j:]

    # sec2 grid：在 <footer 之前、sec2 grid 闭合 </div> 之前插入
    fidx = html.index('<footer')
    k = html[:fidx].rfind('</div>')  # sec2 grid 闭合
    html = html[:k] + cards_r2 + html[k:]

    # hero round 注记
    html = html.replace(
        "2026-08-23 二十三轮补采 +10",
        "2026-08-23 二十三轮补采 +10 ｜ 2026-08-23 二十四轮补采 +5",
        1,
    )
    # tag 计数
    html = html.replace(">89 卡<", ">91 卡<", 1)
    html = html.replace(">63 卡<", ">66 卡<", 1)

    open(WALL, "w", encoding="utf-8").write(html)
    after = html.count('<div class="hl">')
    print(f"[wall] hl before={before} after={after} (+{after-before})")

    # ---------- 2) .run_newcards.tmp.html（当轮新卡，供 gen_run_page）----------
    open(TMP, "w", encoding="utf-8").write("".join(card_html(c) for c in CARDS))
    print("[tmp] wrote", len(CARDS), "cards")

    # ---------- 3) index.json 追加 ----------
    data = json.load(open(IDX, encoding="utf-8"))
    existing_urls = set()
    for e in data:
        u = e.get("url", "")
        u = u.strip().lower().replace("&amp;", "&")
        u = re.sub(r"^https?://", "", u); u = re.sub(r"^www\.", "", u); u = u.rstrip("/")
        existing_urls.add(u)
    added = 0
    for c in CARDS:
        u = c["url"]
        nu = u.strip().lower().replace("&amp;", "&")
        nu = re.sub(r"^https?://", "", nu); nu = re.sub(r"^www\.", "", nu); nu = nu.rstrip("/")
        if nu in existing_urls:
            continue
        data.append({
            "title": c["title"],
            "normKey": c["title"],
            "url": u,
            "sourceType": "secondary",
            "relation": "exec" if c["rel"] == "r3" else "supervisor",
            "summary": c["summary"],
        })
        existing_urls.add(nu)
        added += 1
    json.dump(data, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"[index.json] total={len(data)} added={added}")

    # ---------- 4) Obsidian 汇总笔记 ----------
    s = open(OBS_SUM, encoding="utf-8").read()
    s = s.replace("（142 卡", "（157 卡", 1)
    s = s.replace("二十二轮补采 +6。卡片墙", "二十二轮补采 +6｜ 2026-08-23 二十四轮补采 +5。卡片墙", 1)
    s = s.replace("二手 114", "二手 119", 1)
    r24_section = (
        "## 轮次 20260823·二十四轮（+5）\n\n"
        "| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n"
        "| 高管 Offsite 引导：按「决策顺序」而非「主题桶」构建议程（offsite.html） | 高管间 | 二手 |\n"
        "| 高管 Offsite 议程：先「对齐」不「汇报」+ 把讨论变承诺（offsite.html） | 高管间 | 二手 |\n"
        "| 团队 Offsite 100 招：会前预工系统 + 「不尬」信任建设（offsite.html） | 上下级 | 二手 |\n"
        "| Offsite ROI 测算：SMART 目标 + 有形/无形收益 + 成本三分（offsite.html） | 上下级 | 二手 |\n"
        "| 团队 Offsite 活动「黑名单」与「真连接」清单 + 时段设计模板（offsite.html） | 上下级 | 二手 |\n\n"
    )
    s = s.replace("## 轮次 20260823（+10）", r24_section + "## 轮次 20260823（+10）", 1)
    open(OBS_SUM, "w", encoding="utf-8").write(s)
    print("[obs-sum] updated")

    # ---------- 5) 00 索引 ----------
    z = open(OBS_00, encoding="utf-8").read()
    z = z.replace("**152 卡**", "**157 卡**", 1)
    z = z.replace("③高管间 89 卡 / ②上下级 63 卡", "③高管间 91 卡 / ②上下级 66 卡", 1)
    z = z.replace("2026-08-23 二十三轮补采 +10）", "2026-08-23 二十三轮补采 +10｜ 2026-08-23 二十四轮补采 +5）", 1)
    z = z.replace("二手 106", "二手 111", 1)
    rows = (
        "| 高管 Offsite 引导：按「决策顺序」而非「主题桶」构建议程（offsite.html） | 4 | 二手 | ③高管间 | Averi Advisory：决策顺序四步+超越中立引导者+外部引导时机 |\n"
        "| 高管 Offsite 议程：先「对齐」不「汇报」+ 把讨论变承诺（offsite.html） | 4 | 二手 | ③高管间 | Chartwell Speakers：对齐三问+决策时间块+真实挑战工作坊 |\n"
        "| 团队 Offsite 100 招：会前预工系统 + 「不尬」信任建设（offsite.html） | 4 | 二手 | ②上下级 | ConsultClarity：预工五件套+议程架构八法+不尬信任 |\n"
        "| Offsite ROI 测算：SMART 目标 + 有形/无形收益 + 成本三分（offsite.html） | 4 | 二手 | ②上下级 | Offsite.com：ROI框架+KPI+前后调研，向CFO证明预算 |\n"
        "| 团队 Offsite 活动「黑名单」与「真连接」清单 + 时段设计模板（offsite.html） | 4 | 二手 | ②上下级 | TeamDynamics：避坑清单+真连接活动库+时段模板 |\n"
    )
    z = z.replace("\n## 主题：破冰", "\n" + rows + "\n## 主题：破冰", 1)
    open(OBS_00, "w", encoding="utf-8").write(z)
    print("[obs-00] updated")

    # ---------- 6) 生成当轮独立页 ----------
    out = os.path.join(KC, "offsite", "runs", f"offsite-{DATE}-r{ROUND}.html")
    r = subprocess.run(
        ["python", os.path.join(KC, "gen_run_page.py"),
         "--topic", TOPIC, "--topic-name", "Offsite 团建务虚",
         "--date", DATE, "--round", str(ROUND),
         "--cards-file", TMP, "--out", out],
        capture_output=True, text=True, shell=True,
    )
    print("[run-page]", r.returncode, r.stdout.strip(), r.stderr.strip()[:200])

    # ---------- 7) 当轮独立笔记（Obsidian runs）----------
    rel_counts = {"r3": 0, "r2": 0}
    for c in CARDS:
        rel_counts[c["rel"]] += 1
    note = (
        "---\n"
        "title: Offsite-2026-08-23-第二十四轮-知识卡\n"
        "type: 自动化采集\n"
        "date: 2026-08-23\n"
        "tags: [知识采集, Offsite, 二十四轮]\n"
        "relation: [supervisor, exec]\n"
        "---\n\n"
        "# Offsite 团建务虚 · 第二十四轮补采（2026-08-23，+5）\n\n"
        "- **GitHub Pages 独立页**：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/offsite/runs/offsite-2026-08-23-r24.html\n"
        "- **本地路径**：`knowledge-collection/offsite/runs/offsite-2026-08-23-r24.html`\n"
        "- **累计卡片墙（总索引）**：`knowledge-collection/offsite/offsite.html`（[线上](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/offsite/offsite.html)）\n"
        f"- **覆盖关系档**：③高管间 {rel_counts['r3']} 卡 / ②上下级 {rel_counts['r2']} 卡（无①平级）\n"
        "- **乐享团队文件夹**：Offsite 子文件夹（463f5f5387de4a9bb87b773aef79767b，仅每轮独立页）\n\n"
        "## 本轮新增 5 卡\n\n"
        "| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n"
        "| 高管 Offsite 引导：按「决策顺序」而非「主题桶」构建议程 | 高管间 | 二手 |\n"
        "| 高管 Offsite 议程：先「对齐」不「汇报」+ 把讨论变承诺 | 高管间 | 二手 |\n"
        "| 团队 Offsite 100 招：会前预工系统 + 「不尬」信任建设 | 上下级 | 二手 |\n"
        "| Offsite ROI 测算：SMART 目标 + 有形/无形收益 + 成本三分 | 上下级 | 二手 |\n"
        "| 团队 Offsite 活动「黑名单」与「真连接」清单 + 时段设计模板 | 上下级 | 二手 |\n\n"
        "> 本笔记仅索引，不拷 HTML 副本；完整卡片见上方 GitHub Pages 独立页。\n"
    )
    open(RUNS_NOTE, "w", encoding="utf-8").write(note)
    print("[runs-note] wrote", RUNS_NOTE)


if __name__ == "__main__":
    main()
