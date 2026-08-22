# -*- coding: utf-8 -*-
"""破冰 二十一轮补采 (2026-08-23) — 渲染增量 + 追加进累计墙 + 更新 index.json + Obsidian + 乐享上传
仅 ②上下级 / ③高管间，0 peer。本论增量页 icebreaker-2026-08-23-r21.html。
破冰在乐享既有累计墙 entry（637b3b31）in-place 更新 + 新建每轮独立页入「破冰」子文件夹。"""
import json, os, re, subprocess, urllib.request, urllib.error

BASE = os.path.dirname(os.path.abspath(__file__))
AT_DIR = os.path.join(BASE, "icebreaker")
CUM = os.path.join(AT_DIR, "icebreaker.html")
IDX = os.path.join(BASE, "index.json")
DATE = "2026-08-23"
RUN_NAME = "icebreaker-2026-08-23-r21.html"
RUN_PATH = os.path.join(AT_DIR, "runs", RUN_NAME)
TMP = os.path.join(AT_DIR, ".run_newcards.tmp.html")
ROUND = 21

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---- 本轮新增卡（仅 ②上下级 / ③高管间，0 peer；10张全 NEW，URL 均经 dedup 校验未命中 index/wall）----
# 关系档：③高管间 5 张（全二手）+ ②上下级 4 张（全二手）+ ②+③双档 1 张（落 sec3，双 chip）
CARDS = [
    {
        "emoji": "\U0001F3F7",
        "title": "Top 10 高管团队破冰练习（资深领导专属·非游戏）",
        "cat": "高管对齐练习",
        "rels": ["r3"], "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "The Offsite Co. 给 C-suite/资深领导设计的 10 个「对齐/信任/澄清」练习，明确拒绝信任摔与逃脱室。核心：Leadership Values Mapping（每人列顶层领导价值观→揭示隐性权力动态/价值错位是战略冲突根源）/ Silent Strategy Sprint（禁言仅符号草图→打破口头主导、暴露沟通缺口）/ Tough Talks Roundtable（用结构化反馈模型谈没人敢说的张力，必须外部引导师hold容器）/ CEO for a Day 危机模拟（每人轮值CEO，其余演真实角色，debrief 揭示对CEO决策负担的同理）/ Role Reversal 角色互换（运营辩护创意、法务讲销售→跨职能系统级通 fluent）/ Crisis Scenario Run（无预警实时危机演练→暴露谁牵头谁等指令）/ Legacy Letter 离任 legacy 信。主张：高管练习练的是「校准」，不是技能，给足结构让难对话安全发生。",
        "how": "给高管/资深领导做破冰对齐，学 The Offsite Co.「10 个非游戏练习」：用价值观地图/Silent Sprint/Tough Talks/CEO模拟/角色互换/危机演练替代信任摔；硬性要求外部中立引导师 hold 容器，内部人主导会让 candor 熄火。把破冰从「 mandatory fun」变「战略校准」。",
        "url": "http://www.theoffsiteco.com/news/executive-team-building-exercises",
        "note": "适用：③ 高管/C-suite 团队破冰对齐（活动机构二手；10 个非游戏练习+外部引导师铁律，可作资深领导 offsite 练习弹药库）。",
    },
    {
        "emoji": "\U0001F3E2",
        "title": "麦肯锡：破解顶层团队绩效密码（CEO 必修课·真实案例）",
        "cat": "顶层团队治理",
        "rels": ["r3"], "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "麦肯锡中国梳理「顶层团队」从各自为战到合力破局的四大真实案例。案例三·破除心理壁垒：某区域银行原「中心辐射式」管理、高管各自为政、决策全推CEO；CEO 重塑年度规划会——每位负责人 20 分钟不受干扰陈述战略+5-10 分钟厘清式提问（不打断不评判）+分组建设性反馈+「我能帮对方实现什么」互问，团队从部门优先走向集体担责，CFO/CMO 当场承诺调配资源。案例四·构建信任联结：某东南亚大型保险公司 CEO 在重组关键节点推「人生关键时刻(Crucible Moments)」定期论坛，成员分享塑造人生轨迹的关键经历（含价值观/内在激励/初心），辅以集中办公+1:1 午餐微习惯。结论：顶层团队唯有建立超越事务性互动的深厚信任，才释放真正潜能。",
        "how": "带高管顶层团队，学麦肯锡「两个真实案例」：① 年度规划会改「每人20分钟陈述+厘清式提问+互问我能帮什么」逼集体担责；② Crucible Moments 人生关键时刻论坛+集中办公/1:1午餐微习惯建超越职位的真诚联结。把「CEO 包揽决策」变「赋能团队主导+共同担责」。",
        "url": "https://www.mckinsey.com.cn/\u7834\u89e3\u9876\u5c42\u56e2\u961f\u7ee9\u6548\u5bc6\u7801\uff1aceo\u5fc5\u4fee\u8bfe",
        "note": "适用：③ 顶层/高管团队治理（麦肯锡权威二手；区域银行+东南亚保险真实案例，可作 CEO 顶层团队绩效突破范式）。",
    },
    {
        "emoji": "\U0001F4E2",
        "title": "汇辽集团务虚座谈会（批评与自我批评·真实案例）",
        "cat": "务虚座谈会",
        "rels": ["r3"], "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "安徽汇辽新型装饰材料 2026-01-27 召开「向内求索·破局生长」务虚座谈会，总经理主持，核心管理层+各部门负责人齐聚，以「批评与自我批评」为核心直面问题。摒弃传统务虚会泛泛而谈，倡导「先务虚、再务实」研讨逻辑，围绕「公司发展痛点」与「个人履职不足」两维度敞开心扉。管理层面反思协作效率不足/跨部门情绪内耗/部分岗位管理力待提升；文化层面剖析落地时效不足/人文关怀覆盖不全（工程部门福利遗漏事件→建「以解决问题为导向」协作机制）；品牌层面提宣传摆脱传统+舆情风险意识。总经理总结以「做健康快乐企业」为愿景，把反思转具体行动。",
        "how": "办管理层务虚会，学汇辽「批评与自我批评+先务虚再务实」：总经理主持、核心管理层+部门负责人同场，围绕发展痛点与履职不足两维度坦诚剖析（不绕弯）；管理/文化/品牌三层面各列短板与机制，总结把反思转行动、锚定长期主义。把务虚会从「泛泛而谈」变「辣味十足的对齐场」。",
        "url": "http://suotuo88.com/gsxw/551.html",
        "note": "适用：③ 管理层务虚座谈会（企业官网二手；批评与自我批评+先务虚再务实真实案例，可作务虚会范式）。",
    },
    {
        "emoji": "\U0001F453",
        "title": "FY26 蔡司光学中国区管理团队清远团建（真实案例）",
        "cat": "管理团队团建",
        "rels": ["r3"], "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "蔡司光学中国区管理团队清远两天内部战略会+1.5天「FY26 团建」，立意「不止于团建」，为跨部门管理者打造深度连接/高效协同/共识凝聚场域。首日上午「花式柱球」破冰，8 支跨部门小队初建、竞技中从相识到协同；午后北江大坝约9.2km徒步闯关，沿途四关呼应协作与战略主题（客户至上/唯快不破/全球一体/绩效优异）；次日转足球场重组促进跨部门融合，棒球所需战略布局/即时判断/紧密配合成为管理协同隐喻——「信任队友、补位协同」是成功关键。超越传统团建范畴，让管理者在共对挑战中建信任、理解战略、凝聚共识。",
        "how": "做管理团队团建，学蔡司光学「不止于团建」：战略会+体验式团建一体，破冰→徒步闯关（任务关卡呼应战略主题）→重组竞技（信任补位隐喻）；用精心设计的体验场景让跨部门管理者共对挑战、建信任、理解战略。把团建从「玩」变「战略赋能+文化浸润」。",
        "url": "http://gzrsr.cn/c8537.html",
        "note": "适用：③ 管理团队(跨部门)团建（活动机构二手；蔡司光学真实案例，可作战略会+体验式团建一体范式）。",
    },
    {
        "emoji": "\U0001F4E6",
        "title": "长财融担 2026 年度务虚工作会议（政府官网一手）",
        "cat": "年度务虚会",
        "rels": ["r3"], "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "湖南长财融担 2026 年度务虚工作会议，班子成员聚焦核心业务提质/创新能力提升/管理效能优化，董事长以《以作风之变聚力 以实干之风破局》作总结，为新年吹响奋斗号角。明确 2026 以「强作风、重实干」为总要求，着力打造「敢担当、善作为、能攻坚」干部员工队伍；坚决摒弃「怕、推、慢、庸、散」不良作风，树立「有为有位、无为让位」导向，强化「首办负责、闭环管理」机制，打造「上下联动、左右协同」格局，形成心往一处想、劲往一处使合力。务虚以求实、谋定而后动——统一思想、凝聚共识、提振士气。",
        "how": "办年度务虚工作会，学长财融担「以作风之变聚力 以实干之风破局」：班子成员聚焦核心业务，董事长总结定「强作风重实干」总要求，打造敢担当善作为能攻坚队伍；摒弃怕推慢庸散、立有为有位导向、强首办负责闭环管理、建上下联动左右协同格局。把务虚会从务虚变「统一思想+压实责任」的启动会。",
        "url": "https://dfjrjgj.hunan.gov.cn/dfjrjgj/jgfc/202601/t20260121_33898992.html",
        "note": "适用：③ 年度务虚工作会（政府金融监管官网二手；长财融担案例，可作国企/机构务虚会作风+实干范式）。",
    },
    {
        "emoji": "\U0001F4DC",
        "title": "新经理首场团队会·把焦点从「我」转到「他们」",
        "cat": "新经理首会",
        "rels": ["r2"], "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "Gregor Prah：新经理首场团队会定基调，焦点从「我」转到「他们」。团队在想「这影响我工作吗/会有大变化吗/新老板喜欢我吗」。做法：① 简洁自我介绍（专业背景+个人爱好 humanize，别背简历）；② 透明讲价值观（你stand for什么，让团队即刻 relate 或收到信号）；③ 讲清为何接这个挑战（motivation+vision，非「想要title」）；④ 保证不急着改——先理解团队/动态/角色，尊重现状；⑤ 宣布一对一面谈（listen+learn，要团队洞察、建信任对齐、让被听见→engagement+loyalty）；⑥ 轻松非正式聊每人。避开_metrics/目标，首会营造「we」协作环境，优先理解而非即刻改变。",
        "how": "新经理开首场会，学 Gregor Prah「焦点从me转they」：简洁humanize自我介绍+透明价值观+为何接挑战+承诺先理解再改+宣布1:1倾听面谈；避开场谈指标目标，营造「we」协作环境。把首会从「宣誓就职」变「建信任+对齐」的起点。",
        "url": "https://www.gregorprah.com/blog/how-to-lead-your-first-team-meeting-as-a-new-manager",
        "note": "适用：② 新任经理/团队领导（教练二手；首场会把焦点转团队+1:1倾听，可作新经理首会骨架）。",
    },
    {
        "emoji": "\U0001F4A1",
        "title": "新经理上任第一天·先建信任再谈改变",
        "cat": "新经理首天",
        "rels": ["r2"], "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "KD Recruitment：新经理第一天核心是「先建信任再谈改变」。团队对你天然存疑，只有信任了，你的自信与方向感才被视作正面。做法：展示值得信任（谦逊+ready to learn+意图是help）、show human side（谈激励你的事/承认没有所有答案/「我是新人，你们比我知道多，我来学」）；用轻松 get-to-know-you 问题+记笔记（未来会议/事件可用）；讲领导价值观（什么吸引你来这角色/经理首要目的）。结束前宣布未来几天排1:1，并开放「想更早聊也行」。准备接 tough questions，诚实谦逊答。核心是：不靠魅力解疑，靠可重复行为absorb skepticism。",
        "how": "新经理上任第一天，学 KD Recruitment「先建信任再谈改变」：展示谦逊+ready to learn+help意图、show human side+承认不知、用轻松问题记笔记、讲领导价值观；结束宣布排1:1并开放提前聊。把首天从「自我介绍演讲」变「吸收质疑+建可预测信任」的控制点。",
        "url": "https://kdrecruitment.co.uk/how-to-get-through-the-first-day-as-a-new-manager",
        "note": "适用：② 新任经理（招聘机构二手；上任第一天先建信任+absorb skepticism，可作新经理首日清单）。",
    },
    {
        "emoji": "\U0001F501",
        "title": "Meta 新经理前 30 天 1:1 模板（25 分钟控制环）",
        "cat": "新经理1:1",
        "rels": ["r2"], "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "sirjohnnymai 基于 Meta 新经理实践：前 30 天不靠魅力解团队疑，靠可重复行为——「准确胜赞美，可预测胜可见度」。1:1 用固定 25 分钟控制环（每周同 slot，结构不变=不临场发挥领导）：前5min上周变化/中5min卡在哪/中5min需我决策或资源/中5min给我的反馈/末5min下周复盘+owner。每人单页笔记（当前工作/风险/关系或运作问题/你的回应），跨周可比不靠记忆。边界：晋升/薪酬/绩效议题单开lane，不埋进信任建设 slot。首月排4次周25分1:1保持同slot——reschedule 传递「你仍optional」信号。",
        "how": "新经理前30天建1:1，学 sirjohnnymai「Meta 25分钟控制环」：每周同slot固定结构（变化/阻塞/需我决策/给我反馈/下周owner），单页笔记跨周比；准确胜赞美、可预测胜可见度；晋升薪酬绩效单开lane不埋信任slot。把1:1从「状态汇报」变「决策面+可预测信任」。",
        "url": "https://sirjohnnymai.com/blog/1on1-meeting-template-for-new-manager-at-meta",
        "note": "适用：② 新任经理/一线领导（个人实践二手；Meta式25分钟1:1控制环+边界，可作新经理前30天1:1模板）。",
    },
    {
        "emoji": "\U0001F91D",
        "title": "新经理首场员工会·定基调+建信任+跟进行动",
        "cat": "新经理首会",
        "rels": ["r2"], "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "Cecilia Gorman：新经理首场员工会四步——① 轻松开场（共同 improv，让个性闪光，问 deeper 问题显真实兴趣）；② 设预期+建信任（讲团队如何协作/沟通渠道/1:1频率，透明是信任基石，用 active listening+empathetic 回应）；③ 明确下一步+跟进（立即行动项+owner，排1:1深聊角色预期，会后速发摘要含关键行动点显 diligence）；④ 持续反馈机制（从一开始就 open to feedback，定期check-in/匿名建议箱/会议末留feedback时间）。前置：理解团队动态与历史（避免reopen旧伤），personalize 用自身经历 humanize。核心：不是完美知道一切，是建立连接+让团队听见你如何领导。",
        "how": "新经理开首场员工会，学 Cecilia Gorman「定基调+建信任+跟进」：轻松开场显个性→设协作/沟通/1:1预期（透明=信任基石）→明确行动项+owner+速发摘要→建持续反馈机制；前置理解团队历史避免旧伤、personalize humanize。把首会从「亮相」变「连接+可依赖的领导起点」。",
        "url": "https://ceciliagorman.com/resources/how-to-run-your-first-meeting-as-a-new-manager",
        "note": "适用：② 新任经理/团队领导（顾问二手；首场会四步+持续反馈机制，可作新经理首会清单）。",
    },
    {
        "emoji": "\U0001F5E3\uFE0F",
        "title": "新汉科技「同心·致远」C Leader 对话沙龙（中层×高管）",
        "cat": "中层×高管对话",
        "rels": ["r3", "r2"], "rel_text": "高管间/上下级",
        "src": "b2", "src_text": "二手",
        "val": "新汉科技组织「同心·致远」C Leader 对话沙龙：中层管理人员与高管同场，围绕「如何更好沟通」的开放场域——不设标准答案、不以结论为导向，让表达本身成为重点。日常中因职责分工与信息结构差异，想法多停留在各自语境缺充分表达空间；本次主打在既有沟通体系外创造更轻松/真实/平等方式。三组互动：① 卡牌话题「不一样的我」随机抽取，从岗位视角回个体视角（层级身份边界自然弱化）；② 高管盲盒职场小故事（CEO/SVP/CFO 分享关键节点，破刻板印象拉近距离）；③ 红绿牌挑战（支持/反对即时选择，高管现场回应焦点，立场并存走向感同身受）。不以统一结论为目标，建立深度互信，机制持续推进。",
        "how": "做中层×高管对话，学新汉「同心·致远」C Leader 沙龙：在既有沟通体系外造开放平等场（不设标准答案）；卡牌「不一样的我」弱层级边界+高管盲盒破刻板+红绿牌挑战让立场并存被回应；不以统一结论为目标、建深度互信、机制持续。把中层与高管的沟通从「传递」变「双向真实对话」。",
        "url": "https://www.flykingtech.com/372mppu9afnebcbr.html",
        "note": "适用：③高管间 / ②上下级（企业案例二手；中层×高管开放对话沙龙，双档适用——既可作高管信任破冰、也可作新经理/中层与上级沟通机制）。",
    },
]

def card_html(c, indent=4):
    sp = " " * indent
    sp2 = " " * (indent + 2)
    rel_badges = "".join('<span class="badge {0}">{1}</span>'.format(r, c["rel_text"].split("/")[i] if "/" in c["rel_text"] else c["rel_text"]) for i, r in enumerate(c["rels"]))
    # 双档时 rel_text 用「高管间/上下级」，按顺序拆分；单档直接用
    if "/" in c["rel_text"]:
        texts = c["rel_text"].split("/")
        rel_badges = "".join('<span class="badge {0}">{1}</span>'.format(r, texts[i]) for i, r in enumerate(c["rels"]))
    src_badge = '<span class="badge {0}">{1}</span>'.format(c["src"], c["src_text"])
    return (
        sp + '<div class="hl">\n'
        + sp2 + '<div class="top"><span class="emoji">' + esc(c["emoji"]) + '</span>'
        + '<h3>' + esc(c["title"]) + '</h3><span class="cat">' + esc(c["cat"]) + '</span>'
        + rel_badges + src_badge + '</div>\n'
        + sp2 + '<p class="val">' + esc(c["val"]) + '</p>\n'
        + sp2 + '<details class="exec"><summary>\u600e\u4e48\u505a</summary><div class="inner">' + esc(c["how"]) + '</div></details>\n'
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

# ---- 1) 写临时新卡块 ----
open(TMP, "w", encoding="utf-8").write("".join(card_html(c) for c in CARDS))
print("临时新卡块已写:", TMP)

# ---- 2) 墙注入 ----
html = open(CUM, encoding="utf-8").read()
before = html.count('<div class="hl">')
# 双档卡（rels 含 r3 与 r2）仅落 sec3（与既有墙约定一致，不重复进 sec2）
cards_sec3 = [c for c in CARDS if "r3" in c["rels"]]
cards_sec2 = [c for c in CARDS if c["rels"] == ["r2"]]
assert cards_sec3 and cards_sec2
i3 = html.find('class="sec sec3"')
close3 = find_grid_close(html, i3)
html = html[:close3] + "".join(card_html(c) for c in cards_sec3) + html[close3:]
i2 = html.find('class="sec sec2"')
close2 = find_grid_close(html, i2)
html = html[:close2] + "".join(card_html(c) for c in cards_sec2) + html[close2:]
# hero：在 hero 的 </p> 前插入本轮标记（hero 是 <div class="hero"> 后第一个 </p>）
hi = html.find('<div class="hero">')
he = html.find('</p>', hi)
assert hi != -1 and he != -1, "hero </p> not found"
hero_add = '\u3000｜ 二十一轮补采 +10\uff082026-08-23\uff09\uff1a\u65b0\u7ecf\u7406\u9996\u573a/\u4e0a\u4efb\u9996\u5929\u5efa\u4fe1\u4efb(Meta 25\u5206\u63a7\u5236\u73af)\uff08\u2461\uff09\uff1b\u9ad8\u7ba1\u56e2\u961f\u7834\u51b0\u7ec3\u4e60/The Offsite Co.10\u4e2a\u975e\u6e38\u620f\u7ec3\u4e60\u3001\u9ea6\u80af\u951a\u9876\u5c42\u56e2\u961f\u3001\u6c47\u8fbd/\u8521\u53f8/\u957f\u8d22\u52a1\u865a\u771f\u5b9e\u6848\u4f8b\u3001\u65b0\u6c49C Leader\u4e2d\u5c42\u00d7\u9ad8\u7ba1\u5bf9\u8bdd\u9500\u552e\uff08\u2462\uff09'
html = html[:he] + hero_add + html[he:]
# recount
def recount(tagcls):
    s = html.find('class="' + tagcls + '"')
    e = html.find('class="sec', s + 10)
    return html[s:e].count('<div class="hl">') if e != -1 else html[s:].count('<div class="hl">')
r2n = recount('sec sec2'); r3n = recount('sec sec3')
html = re.sub(r'(<div class="sec sec3">.*?<span class="tag">)\d+', lambda m: m.group(1) + str(r3n), html, count=1, flags=re.S)
html = re.sub(r'(<div class="sec sec2">.*?<span class="tag">)\d+', lambda m: m.group(1) + str(r2n), html, count=1, flags=re.S)
open(CUM, "w", encoding="utf-8").write(html)
after = html.count('<div class="hl">')
r2b = html.count('badge r2'); r3b = html.count('badge r3')
b1b = html.count('badge b1'); b2b = html.count('badge b2')
footer_ok = "\U0001F4CC \u672c\u9875\u7531 yitong" in html
print("累计墙卡片数:", after, "(+", after - before, ") | r2:", r2b, "r3:", r3b, "| b1:", b1b, "b2:", b2b, "| footer:", footer_ok)
print("sec2 tag:", r2n, "sec3 tag:", r3n)

# ---- 3) 独立页（gen_run_page.py，显式 --out 防嵌套路径 bug）----
gen = os.path.join(BASE, "gen_run_page.py")
r = subprocess.run(["python", gen, "--topic", "icebreaker", "--topic-name",
                    "\u7834\u51b0 \u56e2\u961f\u4fe1\u4efb", "--date", DATE, "--round", str(ROUND),
                    "--cards-file", TMP, "--out", RUN_PATH], capture_output=True, text=True)
print("gen_run_page:", r.returncode, r.stdout.strip(), (r.stderr.strip()[:200] if r.stderr else ""))

# ---- 4) index.json ----
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
        "relation": "exec,supervisor" if len(c["rels"]) > 1 else ("exec" if c["rels"][0] == "r3" else "supervisor"),
        "summary": c["cat"] + "：" + c["val"][:60],
        "topic": "icebreaker",
    }
    data.append(entry); added += 1; existing_urls.add(u)
print("index.json 新增:", added, "-> 现", len(data), "条")
json.dump(data, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

# ---- 5) Obsidian 主题汇总笔记（更新卡片总表计数 + 末尾追加轮次行 + 表前插入轮次说明）----
VAULT = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库"
NOTE = os.path.join(VAULT, "素材", "icebreaker", "破冰-知识卡汇总.md")
t = open(NOTE, encoding="utf-8").read()
# 计数标题
assert "## 卡片总表（183 卡" in t, "183 卡 heading not found"
t = t.replace("## 卡片总表（183 卡", "## 卡片总表（193 卡", 1)
# 在 ## 卡片总表 前插入本轮轮次说明（> 行）
round_note = "\n> 二十一轮补采 +10（2026-08-23）：新经理首场/上任首天建信任+Meta 25分1:1控制环（②）；高管团队破冰练习/The Offsite Co.10个非游戏练习、麦肯锡顶层团队、汇辽/蔡司/长财务虚真实案例、新汉C Leader中层×高管对话沙龙（③/②③）。\n"
ti = t.find("## 卡片总表")
assert ti != -1
t = t[:ti] + round_note + t[ti:]
# 末尾追加 10 行（184-193）
new_rows = ""
start = 184
for c in CARDS:
    rel = "高管间" if "r3" in c["rels"] and "r2" not in c["rels"] else ("上下级" if "r2" in c["rels"] and "r3" not in c["rels"] else "高管间/上下级")
    src = "一手" if c["src"] == "b1" else "二手"
    new_rows += "| {0} | {1}（icebreaker.html） | {2} | {3} | {4} |\n".format(
        start, esc(c["title"]), rel, src, esc(c["cat"] + "：" + c["val"][:36]))
    start += 1
t = t.rstrip("\n") + "\n" + new_rows
open(NOTE, "w", encoding="utf-8").write(t)
print("Obsidian 主题汇总笔记已更新（计数+轮次说明+末尾10行）")

# ---- 6) 00-索引（更新计数行 + 关系分层 + 追加卡行；破冰为最后主题，行追加到段末/EOF）----
IDX0 = os.path.join(VAULT, "00-知识采集索引.md")
i0 = open(IDX0, encoding="utf-8").read()
apos = i0.find("## 主题：破冰")
assert apos != -1
# 计数行：**183 卡** -> **193 卡**
assert "**183 卡**" in i0, "183 卡 marker not found"
i0 = i0.replace("**183 卡**", "**193 卡**", 1)
# 轮次标记追加（header 末 二十轮...(+8)） 后）
marker_old = "二十轮补采 2026-08-22(+8)）"
marker_new = "二十轮补采 2026-08-22(+8)） ｜ 二十一轮补采 2026-08-23(+10）"
assert marker_old in i0, "round marker not found"
i0 = i0.replace(marker_old, marker_new, 1)
# 关系分层 66/117 -> 72/121
assert "③高管间 66 卡 / ②上下级 117 卡" in i0, "rel split not found"
i0 = i0.replace("③高管间 66 卡 / ②上下级 117 卡", "③高管间 72 卡 / ②上下级 121 卡", 1)
# append rows：破冰为最后 ## 主题，找下一个 ## 主题（不存在则用 EOF）
npos = i0.find("## 主题：", apos + 10)
insert_at = npos if npos != -1 else len(i0)
rows = "".join(
    "| {0}（icebreaker.html） | 4 | {1} | {2} | {3} |\n".format(
        esc(c["title"]),
        "一手" if c["src"] == "b1" else "二手",
        "③高管间" if "r3" in c["rels"] and "r2" not in c["rels"] else ("②上下级" if "r2" in c["rels"] and "r3" not in c["rels"] else "③高管间/②上下级"),
        esc(c["cat"] + "：" + c["val"][:36]))
    for c in CARDS
)
i0 = i0[:insert_at] + "\n" + rows + i0[insert_at:]
open(IDX0, "w", encoding="utf-8").write(i0)
print("00-索引已更新（计数+轮次+关系分层+卡行）")

# ---- 7) 本轮独立笔记（runs/ 新建 md）----
os.makedirs(os.path.join(VAULT, "素材", "icebreaker", "runs"), exist_ok=True)
RUN_NOTE = os.path.join(VAULT, "素材", "icebreaker", "runs", "破冰-2026-08-23-第二十轮-知识卡.md".replace("第二十轮", "第二十一轮"))
n_r3 = sum(1 for c in CARDS if "r3" in c["rels"])
n_r2 = sum(1 for c in CARDS if "r2" in c["rels"])
rn = (
    "---\n"
    "title: 破冰-2026-08-23-第二十一轮-知识卡\n"
    "type: 自动化采集\n"
    "date: 2026-08-23\n"
    "tags: [知识采集, 破冰, 二十一轮]\n"
    "relation: [supervisor, exec]\n"
    "---\n\n"
    "# 破冰 · 第二十一轮补采（2026-08-23，+10）\n\n"
    "- **GitHub Pages 独立页**：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/runs/icebreaker-2026-08-23-r21.html\n"
    "- **本地路径**：`knowledge-collection/icebreaker/runs/icebreaker-2026-08-23-r21.html`\n"
    "- **累计卡片墙（总索引）**：`knowledge-collection/icebreaker/icebreaker.html`（[线上](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/icebreaker.html)）\n"
    "- **覆盖关系档**：③高管间 {0} 卡 / ②上下级 {1} 卡（无①平级；含1张②③双档）\n".format(n_r3, n_r2)
    + "- **乐享团队文件夹**：破冰 子文件夹（f51480b0cfac4857bc28495b151c624f，累计墙+每轮独立页）\n\n"
    "## 本轮新增 10 卡\n\n"
    "| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n"
)
for c in CARDS:
    rel = "高管间" if "r3" in c["rels"] and "r2" not in c["rels"] else ("上下级" if "r2" in c["rels"] and "r3" not in c["rels"] else "高管间/上下级")
    src = "一手" if c["src"] == "b1" else "二手"
    rn += "| {0} | {1} | {2} |\n".format(esc(c["title"]), rel, src)
rn += "\n> 本笔记仅索引，不拷 HTML 副本；完整卡片见上方 GitHub Pages 独立页。\n"
open(RUN_NOTE, "w", encoding="utf-8").write(rn)
print("本轮独立笔记已建:", RUN_NOTE)

# ---- 8) GitHub 同步 ----
sync = os.path.join(os.path.dirname(BASE), "sync_knowledge_github.py")
try:
    rs = subprocess.run(["python", sync], capture_output=True, text=True, timeout=300)
    print("sync_knowledge_github:", rs.returncode, (rs.stdout.strip()[-300:] if rs.stdout else ""), (rs.stderr.strip()[:200] if rs.stderr else ""))
except Exception as e:
    print("\u26a0\ufe0f GitHub 同步异常（告警不阻断）：" + str(e)[:200])

# ---- 9) 乐享上传（whoami 探活；破冰 累计墙 in-place 更新 + 新建每轮独立页）----
MCP_JSON = r"C:/Users/v_yitcai/.workbuddy/mcp.json"
LEXIANG_URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"
FOLDER = "f51480b0cfac4857bc28495b151c624f"  # 破冰 子文件夹（待清洗素材下）
WALL_ENTRY = "637b3b31280140349221fbe6fa4e08ed"
WALL_FILE = "3c5c841631e54e1bb56474afc95af1b6"

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
    if biz.get("code") != 0:
        raise RuntimeError("apply_upload(wall) FAIL {0}".format(biz.get("message")))
    sess = biz["data"]["session"]
    sid = sess.get("session_id") or sess.get("id")
    url = sess.get("upload_url") or sess["objects"][0]["upload_url"]
    st = put_bytes(url, wall_bytes)
    if st != 200: raise RuntimeError("PUT(wall) status " + str(st))
    r2 = mc.call("file_commit_upload", {"session_id": sid})
    biz2 = mc.biz(r2)
    if biz2.get("code") != 0: raise RuntimeError("commit(wall) FAIL " + str(biz2.get("message")))
    print("乐享累计墙 in-place 更新 OK entry_id=", WALL_ENTRY)

    # 9b) 新建本轮独立页
    run_bytes = open(RUN_PATH, "rb").read()
    r = mc.call("file_apply_upload", {"parent_entry_id": FOLDER, "name": RUN_NAME,
                                      "extension":"html", "mime_type":"text/html",
                                      "upload_type":"PRE_SIGNED_URL", "size": str(len(run_bytes))})
    biz = mc.biz(r)
    if biz.get("code") != 0:
        raise RuntimeError("apply_upload(run) FAIL {0}".format(biz.get("message")))
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
    mapf = json.load(open(os.path.join(BASE, "lexiang-entry-map.json"), encoding="utf-8"))
    sm = mapf.setdefault("icebreaker", {"folder_id": FOLDER, "wall": {}, "rounds": []})
    sm["folder_id"] = FOLDER
    sm["wall"] = {"entry_id": WALL_ENTRY, "file_id": WALL_FILE, "name": "icebreaker.html", "note": "R21 累计墙（193卡）in-place 更新"}
    sm["rounds"].append({"date": DATE, "entry_id": rid, "name": RUN_NAME, "note": "轮次页 R21 (+10)"})
    json.dump(mapf, open(os.path.join(BASE, "lexiang-entry-map.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("已回写 lexiang-entry-map.json（wall + rounds）")
except Exception as e:
    print("\u26a0\ufe0f 乐享上传跳过（warning，不中断）：" + str(e)[:300])

print("\n=== R21 完成：新增", added, "卡，墙现", after, "卡 ===")
