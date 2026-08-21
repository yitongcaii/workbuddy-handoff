# -*- coding: utf-8 -*-
"""破冰 r19 (2026-08-21) 自动采集：7 张新卡（4 高管间 + 3 上下级，0 peer）。
1) 注入 icebreaker.html 累计墙（sec3/sec2 各自 section 内）
2) 写 .run_newcards.tmp.html（当轮新卡）
3) 更新 index.json（追加 7 条，topic=icebreaker）
"""
import re, json, os

WS = r"C:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection"
WALL = os.path.join(WS, "icebreaker", "icebreaker.html")
TMP = os.path.join(WS, "icebreaker", ".run_newcards.tmp.html")
IDX = os.path.join(WS, "index.json")

# ---- 新卡数据（relation: r3=高管间 / r2=上下级；sourceType 全 secondary→二手 b2）----
CARDS = [
    {  # ③ exec
        "emoji": "🔍", "relation": "r3", "cat": "高管训练",
        "title": "领导力训练转化团队·CSI模拟/领导力披萨/即兴剧/战略商战",
        "url": "https://quarterdeck.co.uk/articles/leadership-training-exercises",
        "val": "Quarterdeck 高管训练设计（尊重经验、挑战固有模式、建脆弱信任）：CSI模拟——高管扮调查员查虚构公司罪案，竞争型领导在无威胁下协作；领导力披萨——用披萨图把战略优先级可视化（slice=资源占比、topping=举措），借隐喻谈资源冲突与取舍；即兴剧「Yes, And」——练接纳他人点子而非默认批评，创新指标+32%；战略商战模拟——管虚拟公司多季度决策，暴露决策偏见与风险承受；虚拟版含密室逃脱/沟通大师(描述-绘制,误沟通-25%)/轮值Happy Hour主持。研究：敬业领导团队使员工敬业度+39%。",
        "howto": "高管训练用「CSI模拟/领导力披萨/即兴Yes-And/战略商战」在轻松隐喻下逼出真实决策风格与协作模式；每活动必 debrief 提炼洞察，虚拟版用轮值主持与数字白板延续。",
        "note": "③ 高管团队训练——用CSI模拟/领导力披萨/即兴剧/战略商战在隐喻下暴露决策风格，每活动必 debrief（员工敬业度+39%关联）。",
    },
    {  # ③ exec
        "emoji": "🌊", "relation": "r3", "cat": "高管冒险体验",
        "title": "C-Suite 冒险式领导力·帆船/战略挑战/海岸远征",
        "url": "https://adventour.com.sg/leadership-team-building-for-c-suite-executives-why-adventure-based-experiences-build-stronger-leadership-teams/",
        "val": "AdvenTOUR 新加坡 C-Suite 领导力项目：传统会议室工作坊难打动高管，体验式学习通过真实挑战激活。①帆船领导力——角色协调/风向应变/共享责任/战略协同，快速显影领导团队如何运作；②战略冒险挑战——导航+解谜+体力解题，练战略决策/授权/敏捷；③海岸远征与务虚——自然松弛环境做战略反思、对齐对话、非正式关系建设、未来愿景。价值：共享有意义体验建心理安全与信任底座，带回职场；外部专业引导+可定制（offsite/务虚/领导力发展）。",
        "howto": "C-Suite 用冒险体验（帆船/战略挑战/海岸远征）在真实压力与不确定中练决策与协同；自然松弛环境做务虚对齐与关系建设，配外部引导师。",
        "note": "③ C-Suite 领导力务虚——帆船/战略挑战/海岸远征等冒险体验在真实压力练协同，自然环境中做战略对齐（新加坡案例，外部引导）。",
    },
    {  # ③ exec
        "emoji": "🧱", "relation": "r3", "cat": "高管团队建设",
        "title": "高管团队建设·Lego Serious Play/武士之道/生存课/品酒",
        "url": "https://kaizenteambuilding.com/en/gestion-del-liderazgo/team-building-para-directivos-y-comites-de-direccion",
        "val": "Kaizen 高管委员会团队建设：高管团队最缺非正式信任空间，且小群体(4-15人)每人权重高、难藏拙，活动须「第一分钟就有清晰目的+执行零瑕疵」。适配活动：①Lego Serious Play——用积木做战略思考，让常规会议沉默的观点浮现；②武士之道——沉浸式练领导力/纪律/压力决策；③生存课——把委员会拉出舒适区，显影谁站出来领导、压力下如何分担；④收尾品酒——恰到好处的精致放松不丢严肃。外部引导师关键：同级别无人能中立主持同侪。最佳时点：新CEO/新成员到任、重组/战略变革启动、艰难一年后、新财年对齐前。",
        "howto": "高管委员会团队建设选「小群体高权重」适配活动（Lego Serious Play/武士之道/生存课/收尾品酒），第一分钟亮明目的、配外部引导师；最佳时点为新CEO到任/重组启动/新财年对齐前。",
        "note": "③ 高管委员会/管理团队建设——Lego Serious Play/武士之道/生存课/品酒，小群体高权重须目的明确+外部引导师，时点选新CEO到任/重组/新财年。",
    },
    {  # ③ exec
        "emoji": "📈", "relation": "r3", "cat": "高管战略团建",
        "title": "高管战略团队建设·工作坊/沉浸培训/反思务虚/公益/KPI度量",
        "url": "https://www.nickwarnerconsulting.com?p=2116/",
        "val": "Nick Warner 高管战略团建：传统破冰游戏对高管无效（显幼稚），须给专业发展与真实影响。四类：①聚焦工作坊——领导力/战略/沟通/冲突解决，小群体讨论真实议题（如Agile工作风）；②沉浸培训——场景化危机管理/谈判推演，练批判思维与应变；③反思务虚——离岗深度谈团队动态与经验教训、对齐长期愿景；④公益活动——组队做NGO志愿，建情谊+练解题。共享体验（品酒/烹饪/密室）促跨部门联结。度量ROI：前置KPI（沟通改善/效率/决策速度），追踪决策速度、落地效能、沟通模式变化。",
        "howto": "高管战略团建避开幼稚游戏，用「聚焦工作坊/沉浸培训/反思务虚/公益」四类给真实专业发展；共享体验(品酒/烹饪/密室)促联结，前置KPI追踪决策速度与沟通模式变化度量ROI。",
        "note": "③ 高管战略团队建设——工作坊/沉浸培训/反思务虚/公益四类的真实专业发展，共享体验促联结，前置KPI度量ROI（避幼稚游戏）。",
    },
    {  # ② supervisor
        "emoji": "🧩", "relation": "r2", "cat": "跨部门启动会",
        "title": "跨部门项目启动会·会前白皮书+思维导图整合+责任到人（实战案例）",
        "url": "https://www.coze.cn/gallery/detail/69a91dfcf077f301f9ec2fd8.html",
        "val": "扣子平台实战案例：某跨部门项目启动会因「各说各话」陷入沟通僵局、上线延迟。重构流程后——会前3天发项目白皮书（背景/目标/各部门KPI），收各部门核心诉求与风险；会中锁定「目标共识+协作规则」，用思维导图实时整合「用户需求-技术实现-运营落地-市场推广」闭环；分组讨论20min→共识确认责任边界与交付节点→全员电子签字；会后固定每周三同步会、产品经理任总协调人。效果：上线提前15天、沟通效率+60%、首月用户破10万。",
        "howto": "跨部门启动会先把「信息同步」做在会前（白皮书+风险清单），会中只谈目标共识与协作框架并用可视化工具整合发散观点；责任必须签到具体人与交付标准，设固定同步节奏防「人人有责无人负责」。",
        "note": "② 跨部门项目启动会——会前白皮书同步+思维导图整合+责任到人，破「各说各话」僵局（实战案例，上线提前15天）。",
    },
    {  # ② supervisor
        "emoji": "🚀", "relation": "r2", "cat": "项目启动会",
        "title": "项目启动会（Kickoff）怎么开·7步法（含跨部门）",
        "url": "https://otter.ai/blog/kickoff-meetings",
        "val": "Otter.ai 跨区域/跨部门 Kickoff 实操：1)会前发议程（范围/里程碑/预算/交付），让成员带着方案而非问题来；2)开宗明义讲清项目目标给团队「目的感」；3)走一遍时间线与依赖，标注关键deadline；4)明确角色与职责，新/远程团队用破冰开场；5)点出潜在风险邀反馈brainstorm缓冲；6)留Q&A挖盲点；7)结尾快速复盘行动项。核心：验证每个团队理解「自己的工作如何影响他人」，跨部门启动会优先谈角色职责与协作沟通机制。",
        "howto": "跨部门 Kickoff 七步走：会前发议程+目标共识+时间线依赖+角色职责（破冰开场）+风险共创+Q&A盲点+结尾行动项复盘；始终把「我的工作如何影响他人」讲透。",
        "note": "② 项目/跨部门 Kickoff 启动会——七步法（议程前置/目标/依赖/角色/风险/Q&A/复盘），远程与新团队加破冰开场。",
    },
    {  # ② supervisor
        "emoji": "🔗", "relation": "r2", "cat": "跨部门融合",
        "title": "跨部门融合·部门工作坊+跨职能规划议程（破筒仓）",
        "url": "https://twilio.withconfetti.com/blog/post/cross-team-integration-how-to-break-down-silos-and-improve-collaboration-between-departments",
        "val": "Confetti 跨部门融合实操：部门工作坊用「理解/对齐/改进」框架——各团队快照（拥有什么/本季聚焦/需要对方什么/当前拉胯处）+handoff映射（客户请求怎么从销售→产品流动、支持问题怎么变产品洞察，标注信息在哪丢、期望在哪模糊、延迟在哪）+摩擦与假设（「希望你团队知道X」「我们对你团队的假设Y」「什么能让协作更易」「该一起解决的老问题」）+选1-2个改进测试+owner与复盘。跨职能规划75分钟：共享目标→角色图(Driver/Decider/Contributor/Reviewer/Informed)→依赖→风险→运营节奏(周同步/决策日志/月复盘)→下一步owner。",
        "howto": "跨部门融合用部门工作坊（团队快照+handoff映射+摩擦四问）把指责变「如何更好一起」；跨职能规划用角色图+RACI式依赖+运营节奏落 accountable owner，避免 blame。",
        "note": "② 跨部门融合/破筒仓——部门工作坊(handoff映射+摩擦四问)+跨职能规划(角色图+依赖+运营节奏)，把指责转对齐。",
    },
]

REL_LABEL = {"r2": "上下级", "r3": "高管间"}

def card_html(c):
    disp = c["url"].split("//", 1)[-1]
    return (
        '  <div class="hl">\n'
        '      <div class="top"><span class="emoji">{emoji}</span><h3>{title}</h3>'
        '<span class="cat">{cat}</span><span class="badge {rel}">{rellabel}</span>'
        '<span class="badge b2">二手</span></div>\n'
        '      <p class="val">{val}</p>\n'
        '      <details class="exec"><summary>怎么做</summary><div class="inner">{howto}</div></details>\n'
        '      <div class="src">🔗 <a href="{url}" target="_blank">{disp}</a></div>\n'
        '      <div class="note">适用：{note}</div>\n'
        '    </div>\n'
    ).format(emoji=c["emoji"], title=c["title"], cat=c["cat"], rel=c["relation"],
             rellabel=REL_LABEL[c["relation"]], val=c["val"], howto=c["howto"],
             url=c["url"], disp=disp, note=c["note"])

def html_norm(s):
    return re.sub(r'[\s\u3000]+', '', s).lower()

def insert_into(html, sec_class, cards_html):
    pat = re.compile(r'(<div class="sec ' + sec_class + r'">.*?<div class="grid">)', re.S)
    m = pat.search(html)
    if not m:
        raise RuntimeError("section not found: " + sec_class)
    i = m.end()
    return html[:i] + "\n" + cards_html + html[i:]

def update_count(html, sec_class, newcount):
    pat = re.compile(r'(<div class="sec ' + sec_class + r'">.*?<span class="tag">)\d+( 卡</span>)', re.S)
    return pat.sub(lambda m: m.group(1) + str(newcount) + m.group(2), html, count=1)

# ---- 1) 注入累计墙 ----
html = open(WALL, encoding="utf-8").read()
html = html.replace('采集于 2026-08-17 ｜ R14', '采集于 2026-08-21 ｜ R19', 1) if False else html

# hero 注记
ROUND_NOTE = ("｜ 十九轮补采 +7（2026-08-21）：跨部门项目启动会(扣子实战·会前白皮书+思维导图+责任到人,"
              "上线提前15天)/Kickoff启动会7步法(otter)/跨部门融合部门工作坊(handoff映射+摩擦四问+跨职能规划)"
              "/领导力训练转化(CSI模拟/领导力披萨/即兴Yes-And/战略商战)/C-Suite冒险式领导力(帆船/战略挑战/海岸远征)"
              "/高管委员会建设(Lego Serious Play/武士之道/生存课/品酒)/高管战略团建(工作坊/沉浸培训/反思务虚/公益+KPI度量)")
m = re.search(r'(<div class="hero">.*?<p>)(.*?)(</p>)', html, re.S)
if m:
    html = html[:m.start()] + m.group(1) + m.group(2) + ROUND_NOTE + m.group(3) + html[m.end():]
else:
    raise RuntimeError("hero p not found")

# 分组
sec3_cards = [c for c in CARDS if c["relation"] == "r3"]
sec2_cards = [c for c in CARDS if c["relation"] == "r2"]
html = insert_into(html, "sec3", "\n".join(card_html(c) for c in sec3_cards))
html = insert_into(html, "sec2", "\n".join(card_html(c) for c in sec2_cards))

# 更新计数（基于实际段内 hl 数）
for sec_class, n in [("sec3", 58 + len(sec3_cards)), ("sec2", 110 + len(sec2_cards))]:
    html = update_count(html, sec_class, n)

assert "📌 本页由 yitong" in html, "footer lost!"
open(WALL, "w", encoding="utf-8").write(html)
print("WALL updated ->", WALL, "| total hl=", html.count('<div class="hl">'))

# ---- 2) 当轮新卡 tmp ----
tmp = "\n".join(card_html(c) for c in CARDS)
open(TMP, "w", encoding="utf-8").write(tmp)
print("TMP written ->", TMP, "| cards=", len(CARDS))

# ---- 3) 更新 index.json ----
data = json.load(open(IDX, encoding="utf-8"))
existing_urls = {e.get("url") for e in data}
added = 0
for c in CARDS:
    if c["url"] in existing_urls:
        print("SKIP dup url:", c["url"]); continue
    data.append({
        "title": c["title"],
        "normKey": html_norm(c["title"]),
        "url": c["url"],
        "sourceType": "secondary",
        "relation": "exec" if c["relation"] == "r3" else "supervisor",
        "topic": "icebreaker",
        "summary": c["note"].replace("适用：", ""),
    })
    added += 1
json.dump(data, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("INDEX updated -> added", added, "| total entries=", len(data))
