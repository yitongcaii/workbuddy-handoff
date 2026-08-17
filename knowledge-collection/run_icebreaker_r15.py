# -*- coding: utf-8 -*-
"""知识采集自动化 · 破冰 第15轮（2026-08-18）注入脚本。
把 8 张新卡（2×③高管间 + 6×②上下级）注入 icebreaker.html 累计墙，
写 .run_newcards.tmp.html，并追加到 index.json。"""
import json, re, os

BASE = r"C:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection"
WALL = os.path.join(BASE, "icebreaker", "icebreaker.html")
TMP = os.path.join(BASE, "icebreaker", ".run_newcards.tmp.html")
IDX = os.path.join(BASE, "index.json")

REL_LABEL = {"r2": "上下级", "r3": "高管间"}
SRC_LABEL = {"b1": "一手", "b2": "二手"}

# 8 张新卡：顺序 [③×2, ②×6]
CARDS = [
    # ---- ③ 高管间 ----
    dict(emoji="🤝", title="高管 Offsite 团队融合案例·Lencioni 五 dysfunction + LAP 模型", cat="高管Offsite",
         rel="r3", src="b2",
         val="Meeraq 为某全球药企 MD 群体(10人)设计的 1 日高管 offsite + 行动教练(LAP 模型)真实案例：基于 Lencioni 五 dysfunction 诊断团队，目标把一群 group leader 变『一个 cohesive team』——建信任、破 silo、对齐共享目标。流程：Pre-study & 利益相关者访谈定调 → 反思性 pre-work(当前团队信任/凝聚力/功能理解) → 1 日工作坊(解五 dysfunction) → 行动教练+进度复盘(Kirkpatrick 评估)。结果：57% 参与者在团队凝聚力/协作/冲突解决能力上提升最高达 67%。启示：高管融合用诊断+工作坊+后续跟进三段式，facilitator 用框架把行为变可追踪承诺。",
         exec="高管 offsite 融合用『Lencioni 五 dysfunction 诊断 → 1 日工作坊解 dysfunction → 行动教练+进度复盘』三段式；配 pre-study 访谈与反思性 pre-work 提升相关性；用 Kirkpatrick 量化行为改变而非只看热闹。",
         url="https://meeraq.com/senior-leadership-offsite-team-building-on-working-as-one-cohesive-team/",
         label="meeraq.com/.../senior-leadership-offsite-team-building",
         note="适用：③ 高管团队融合 offsite 真实案例——Lencioni 框架诊断 + LAP 行动教练闭环，57% 参与者协作力提升。"),
    dict(emoji="🏥", title="NHS 领导力 Offsite·转型协作(5 Voices 诊断+1日offsite)", cat="领导力Offsite",
         rel="r3", src="b2",
         val="Five&Co 为 NHS 遭遇重大变革的地区高管团队做的转型 offsite 案例：目标在变革中建信任、强化跨业务协作。做法：Discovery 访谈 + 领导力测评「The 5 Voices of a team」(照见沟通/信任/对齐模式) → 现场旁听会议给结构反馈 → 设计引导 1 日 offsite 深化信任、建 mutual understanding、约定共享工作惯例 → Team Insights 反思流程 + 后续工作坊 → 对团队 leader 持续 1:1 教练(战略 thought partnership)。结果：信心/协作提升、跨职能连接增强、会议结构与参与改善、心理安全感萌芽。金句：『不是团建，而是诚实地啃硬骨头』。",
         exec="变革期高管 offsite 用『诊断访谈+5 Voices 测评 → 1 日引导 offsite(信任/共识工作惯例)→ 反思流程+1:1 教练』；把 offsite 当硬对话空间而非社交，落地靠后续跟进 workshop 与 leader 教练。",
         url="https://fiveandco.com/transformational-offsites-strengthening-collaboration-in-the-face-of-change/",
         label="fiveandco.com/.../transformational-offsites",
         note="适用：③ 变革期高管团队 offsite——诊断+测评+1日offsite+教练闭环，用诚实对话替代团建。"),
    # ---- ② 上下级 ----
    dict(emoji="🧱", title="新经理首会建信任·三支柱(胜任/善意/正直)+对的破冰", cat="新经理首会",
         rel="r2", src="b2",
         val="新经理首会本质是『把房间从被动变在场』。信任三支柱(管理学经典)：①胜任(competence)——能帮团队成事才真被信，光讨喜不是领导；②善意(benevolence)——把功劳公开具体给做事的人、背锅时护住团队(当政治 fallout 的缓冲)，问下属职业目标+给拉伸任务是最强善意信号；③正直(integrity)——言行值对齐，信任滴建桶失，一次『周五回你』却消失可抵数周友好，道歉要 naming harm+担责+具体改变。破冰：差的破冰比没有更糟(40人轮流 fun fact 到第15人能量枯竭)；对的破冰=『你希望别人知道你角色的哪一点』『用三个词形容工作风格』(personal 又 safe)；虚拟用『同时打在聊天框』技术兼顾内向者；避开『精神动物/厨房电器/没人知道的事』等 forcing 表演。",
         exec="新经理首会用信任三支柱定调：胜任(帮成事)+善意(功归团队/背锅护队)+正直(言行一致、道歉具体)；破冰用『角色希望被知道的/三词形容风格』等 low-stakes 问题，虚拟用 simultaneous chat，避开强迫表演型问题；信任修复要 immediate+specific。",
         url="https://www.befreed.ai/zh/podcast/first-team-meeting-building-trust",
         label="befreed.ai/zh/podcast/first-team-meeting-building-trust",
         note="适用：② 新经理首会建信任——胜任/善意/正直三支柱 + 对的破冰问题设计，避开强迫表演型暖场。"),
    dict(emoji="💬", title="新团队首会 6 话题 + Stop/Start/Continue + 心理安全感", cat="新经理首会",
         rel="r2", src="b2",
         val="Fellow 新团队首会框架：先准备议程+提前发+轮值角色。6 话题：①互相认识(破冰建信任，用 stop/start/continue 反馈法)；②关于你(经理)——分享价值观/决策方式/如何评估绩效，Harvard 的 Carolyn O'Hara 强调透明承诺，并区分 swift trust(立即信、被证伪才撤)与 passable trust(更持久深层)；③反馈(stop/start/continue)——也匿名问团队对你的反馈；④团队愿景与目标(组织→部门→团队三层，鼓励讨论障碍/资源)；⑤角色与职责(org chart+决策权+互联)；⑥沟通期望(工具/响应时效/会议节奏/冲突解决/决策方式)。Q&A 收尾表透明。",
         exec="新经理首会用 6 话题结构(认识→关于你→反馈→目标→职责→沟通)，公开价值观与 swift/passable 信任观；用 stop/start/continue 既给团队反馈也匿名收团队对己反馈；沟通规范共议定稿。",
         url="https://fellow.ai/blog/first-meeting-with-your-new-team-and-first-team-meeting-agenda/",
         label="fellow.ai/blog/first-meeting-with-your-new-team",
         note="适用：② 新经理首会结构化议程——6 话题 + swift/passable 信任 + stop/start/continue 双向反馈。"),
    dict(emoji="🎯", title="新经理首会 5 招·赢下新团队(准备/以身作则/让人了解你/备问/强收尾)", cat="新经理首会",
         rel="r2", src="b2",
         val="Niagara Institute 新经理首会 5 招：①准备——记名字/职务、摸清团队文化与强弱、读公司官网历史使命竞品(引 Michael Watkins《First 90 Days》：印象形成快且 sticky)；②以身作则——早到、手机收起、积极倾听、乐观，用行动定调；③让人了解你——分享驱动力/核心价值观/协作哲学/沟通风格/小成功故事/业余爱好，保持简短+谦逊(示学习模式)；④提前备问——把大部分时间给 discovery：『我怎么做能让你更成功』『我们该 start/stop/continue 什么』『若有资源想加什么』，叫停霸话者、点名未发言者；⑤强收尾——重申期待+会议/1:1 节奏+待办与时间线。",
         exec="新经理首会五步：充分准备(名字/文化/公司)→以身作则定行为基调→简短谦逊自我介绍(驱动力/价值观/风格)→把时间给 discovery 提问(叫停霸话、点名沉默者)→强收尾(节奏+待办+时间线)。",
         url="https://niagarainstitute.com/blog/first-meeting-employees-new-manager",
         label="niagarainstitute.com/blog/first-meeting-employees-new-manager",
         note="适用：② 新经理首会实操 5 招——从准备到强收尾，把首会变成共建而非单向宣讲。"),
    dict(emoji="📋", title="首会 10 必备议程·含破冰/团队规范/沟通期望", cat="新经理首会",
         rel="r2", src="b2",
         val="GrowthTactics 新经理首会 10 必备议程：①破冰(5-10min，Two Truths and a Lie/Speed Networking/Common Ground/Would You Rather/Show and Tell，按团队文化选、不超 10min)；②自我介绍与欢迎(领导哲学/为何来这角色/对团队初印象/小轶事)；③团队愿景与目标(组织→部门→团队三层+如何贡献/障碍/资源)；④角色与职责(org chart+决策权+互联+『如何支持同伴』)；⑤沟通期望(工具/响应时效/会议频率/报告/远程/冲突解决/决策方式)；⑥团队规范与价值观(共拟核心值+ punctuality/会议礼仪/工作生活平衡)；⑦当前项目概览(Gantt/Kanban+卡点)；⑧Q&A；⑨个人/职业发展(1:1 目标)；⑩收尾与下一步。强调用共享文档实时捕获规范。",
         exec="新经理首会用 10 段议程模板：破冰(≤10min,按文化选)→自我介绍→愿景目标三层→职责→沟通期望→团队规范→项目→Q&A→发展→收尾；用协作文档实时沉淀规范与价值观，避免只谈事不谈怎么一起工作。",
         url="https://www.growthtactics.net/first-team-meeting-agenda/",
         label="growthtactics.net/first-team-meeting-agenda",
         note="适用：② 新经理首会完整议程模板——破冰到规范到收尾十段，可直接套用。"),
    dict(emoji="⤴️", title="越级(Skip-level)会谈·42 问 + 9 个避坑", cat="越级沟通",
         rel="r2", src="b2",
         val="Deel skip-level 指南：越级会谈=员工与其经理的经理的直接对话，跳过一层拿未过滤洞察、建透明文化。42 问分域：破冰/rapport(爱好/榜样/最有成就感的项目/偏好被认可方式)→团队感知(什么在顺/该立马改什么/如何庆祝)→角色与职业目标(路障/长期抱负/想发展技能)→创新创意(公司是否重视创新/创意被接纳吗)→对直属经理反馈(经理给够反馈吗/如何助你成长/经理可改的一件事)→文化(如何向朋友描述文化/满意度打分/最想改的一点)→政策与 D&I。9 个避坑：勿让经理感到被绕过、勿承诺无法兑现、勿只收集不行动、保护发言者匿名、勿在公开场合点名、勿把会谈变绩效审查、勿跳过后续闭环、勿问诱导性/侵犯性问题、勿让经理缺席关键决策。",
         exec="越级会谈用分域 42 问拿未过滤洞察(破冰→团队→职业→创新→对经理反馈→文化→政策)，严守 9 避坑：保护来源安全感、不绕过直属经理、收集必转行动、会后闭环；把 1:1 设固定节奏让上层直接听基层。",
         url="https://www.deel.com/blog/skip-level-meeting-questions/llm-info",
         label="deel.com/blog/skip-level-meeting-questions",
         note="适用：② 越级(skip-level)会谈问题库与避坑——上层直接听基层、建透明，且不架空直属经理。"),
    dict(emoji="🤝", title="越级会谈问题库·建 rapport + 团队反馈 + 对直属上级反馈", cat="越级沟通",
         rel="r2", src="b2",
         val="Workhuman skip-level 指南：会谈=员工与经理的经理，目标对齐公司目标愿景、双向受益。建 rapport 破冰(最爱引用/一年内非工作成就/推荐的书影/当前目标/有趣事实/理想假期/充电方式)→团队反馈(沟通协作如何/贡献被认可吗/什么在顺什么不在/工作量合适吗/路障/该 stop 的一件事/要什么资源)→对直属经理反馈(经理如何建正向文化/如何确保有效沟通/如何促创新/是否担责/有无偏袒/工作生活平衡/打分给支持度/是否敢提 concerns/如何处理冲突)。强调 rapport 建信任才敢说真话(组织行为研究：rapport 对话促信任、透明交流、共创解题)。",
         exec="越级会谈三段：rapport 破冰(非工作成就/兴趣)→团队反馈(顺/不顺/路障/资源)→对直属经理反馈(文化/沟通/创新/偏袒/支持度)；先建 rapport 信任再要坦诚反馈，中立者角色让下属敢谈对经理的观察。",
         url="https://www.workhuman.com/blog/skip-level-meeting-questions/",
         label="workhuman.com/blog/skip-level-meeting-questions",
         note="适用：② 越级会谈问题库——rapport 先行再收团队与对经理反馈，中立桥接不越权。"),
]

def card_html(c):
    rel = REL_LABEL[c["rel"]]
    src = SRC_LABEL[c["src"]]
    return (
        '  <div class="hl">\n'
        f'      <div class="top"><span class="emoji">{c["emoji"]}</span><h3>{c["title"]}</h3>'
        f'<span class="cat">{c["cat"]}</span><span class="badge {c["rel"]}">{rel}</span>'
        f'<span class="badge {c["src"]}">{src}</span></div>\n'
        f'      <p class="val">{c["val"]}</p>\n'
        f'      <details class="exec"><summary>怎么做</summary><div class="inner">{c["exec"]}</div></details>\n'
        f'      <div class="src">🔗 <a href="{c["url"]}" target="_blank">{c["label"]}</a></div>\n'
        f'      <div class="note">{c["note"]}</div>\n'
        '    </div>\n'
    )

blocks = [card_html(c) for c in CARDS]
blocks_html = "".join(blocks)

# ---- 注入 icebreaker.html ----
html = open(WALL, encoding="utf-8").read()

# ③ 卡插入 sec3 grid（即在 <div class="sec sec2"> 之前）
assert "<div class=\"sec sec2\">" in html, "sec2 marker missing"
html = html.replace("<div class=\"sec sec2\">", "".join(blocks[:2]) + "<div class=\"sec sec2\">", 1)

# ② 卡插入 sec2 grid（即在 <footer> 之前）
assert "<footer>" in html, "footer missing"
html = html.replace("<footer>", "".join(blocks[2:]) + "<footer>", 1)

# 更新 tag 计数
html = html.replace('<span class="tag">45 卡</span>', '<span class="tag">47 卡</span>', 1)
html = html.replace('<span class="tag">86 卡</span>', '<span class="tag">92 卡</span>', 1)

# 更新 hero <p>：追加 r15 说明
m = re.search(r'(<div class="hero">.*?<p>)(.*?)(</p>)', html, re.S)
assert m, "hero p not found"
r15 = (' ｜ 十五轮补采 +8（2026-08-18）：新经理首会信任三支柱/首会框架(Fellow·Niagara·GrowthTactics)/'
       '对的破冰问题(befreed)、越级会谈 42 问+9 避坑(Deel)+越级问题库(Workhuman)（②）；'
       '高管 Offsite 团队融合真实案例(Meeraq·Lencioni 五 dysfunction+LAP)/NHS 领导力 Offsite 转型协作(5 Voices)（③）')
new_p = m.group(2) + r15
html = html[:m.start()] + m.group(1) + new_p + m.group(3) + html[m.end():]

open(WALL, "w", encoding="utf-8").write(html)

# ---- 写 run tmp ----
open(TMP, "w", encoding="utf-8").write(blocks_html)

# ---- 追加 index.json ----
idx = json.load(open(IDX, encoding="utf-8"))
existing_urls = {e.get("url") for e in idx}
added = 0
for c in CARDS:
    if c["url"] in existing_urls:
        continue
    norm = re.sub(r'[\s\W]+', '', c["title"]).lower()
    rel = "exec" if c["rel"] == "r3" else "supervisor"
    idx.append({
        "title": c["title"],
        "normKey": norm,
        "url": c["url"],
        "sourceType": "primary" if c["src"] == "b1" else "secondary",
        "relation": rel,
        "topic": "icebreaker",
        "summary": c["val"],
    })
    added += 1
json.dump(idx, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

print(f"OK wall injected | new cards={len(CARDS)} | index added={added} | total index={len(idx)}")
