# -*- coding: utf-8 -*-
# 员工大会 第十九轮补采（+11）卡片构建：追加到 staff-meeting.html 累计墙 + 写 .run_newcards.tmp.html + 追加 index.json
import re, os, json

BASE = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(BASE, 'staff-meeting', 'staff-meeting.html')
TMP = os.path.join(BASE, 'staff-meeting', '.run_newcards.tmp.html')
IDX = os.path.join(BASE, 'index.json')

# ---------- 11 张新卡（②③ 向，无①peer；本轮源均二手）----------
C = []

# 1 happeo CEO真实感沟通（sec3 r3）
C.append(('sec3', '''<div class="hl">
  <div class="top"><span class="emoji">🗣️</span><h3>CEO真实感沟通：从「倡导」到「询问」+You Said/We Did（happeo·Nadella/Bitzer案例）</h3><span class="cat">高管沟通</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
  <p class="val">高管把全员会当成「双向对话」而非「我讲你听」：①从advocacy转inquiry——每场town hall留最后30分钟真实live Q&A，会前收匿名提问；②季度小范围listening tour（8-10人）问开放式「什么在挡着你/我们该停掉什么/我今天哪点没讲清」，比念PPT更建信任；③重大调研后发「You Said / We Did」对照表，能改就改、不能改就解释为什么——透明讲约束比沉默更攒信任；④把战略翻成「so what对我日常工作意味着什么」，否则员工听完仍懵。用真实感（Nadella分享自身学习历程、Whirlpool的Bitzer用iPhone录每周无剪辑员工Q&A）替代官腔。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">高管沟通三招：①每场town hall留足真实Q&A（会前匿名收问，忌只念稿）；②季度做8-10人小范围listening tour，问「什么挡着你/该停掉什么/我哪点没讲清」而非宣讲；③调研后发「You Said/We Did」对照，能改即改、不能改说明约束；④战略必答「so what对你意味着什么」。真实感&gt;官腔，Nadella/Bitzer为证。</div></details>
  <div class="src">🔗 <a href="https://happeo.com/blog/ceo-communication-with-employees" target="_blank">happeo.com/blog/ceo-communication-with-employees</a></div>
  <div class="note">适用：③ 高管把全员会做成双向对话+真实感沟通范式。</div>
</div>'''))

# 2 businessplusai AI全员会模板（sec3 r3+r2 双）
C.append(('sec3', '''<div class="hl">
  <div class="top"><span class="emoji">🤖</span><h3>AI 全员会模板：直面岗位焦虑·再培训·诚实Q&A（businessplusai·信任在Q&A赚或失）</h3><span class="cat">变革沟通</span><span class="badge r3">高管间</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">当下最棘手的全员会场景之一——向全员讲AI。模板四段：①讲清AI战略与「为什么现在做」（与业务挂钩，不空谈）；②坦诚影响——哪些岗位/技能仍关键、公司在再培训上投什么（内部upskilling、AI工具workshop、师徒结对、内部流动通道、各部门AI答疑对接人）；③开放Q&A（全场最关键25分钟）——用中立主持控流、把相似问题归类、不知就明说并给跟进时限、结尾归纳 emerged 主题显「真被听见」；④收尾给具体承诺而非鸡汤——下周发纪要、各负责人两周内开小会、设专用邮箱。预设高频硬问题（「我的岗位会不会没？」「谁做的决定、员工有没有被咨询？」「怎么衡量AI是好是坏？」）提前备诚实答案。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">AI全员会落地：①先讲「为什么现在做AI」挂钩业务；②坦诚哪些技能仍关键+再培训投入（upskilling/workshop/师徒/流动通道/部门AI对接人）；③Q&A用中立主持、归类相似问、不知明说+给时限、结尾归纳主题；④收尾给具体承诺（纪要/小会/邮箱）而非「美好旅程」。预设「岗位会不会没/谁决定/怎么衡量」硬问题备诚实答案。</div></details>
  <div class="src">🔗 <a href="https://www.businessplusai.com/blog/ai-town-hall-template-how-to-address-workforce-concerns-and-build-employee-trust" target="_blank">businessplusai.com/blog/ai-town-hall-template-how-to-address-workforce-concerns-and-build-employee-trust</a></div>
  <div class="note">适用：③ 高管向全员做AI变革沟通；② 各部门AI答疑对接人+再培训落地。</div>
</div>'''))

# 3 commswith.ai 全员公告写作结构（sec3 r3+r2 双）
C.append(('sec3', '''<div class="hl">
  <div class="top"><span class="emoji">📣</span><h3>全员公告写作结构（commswith.ai·All-Staff Update Format：钩子/背景/变什么/对你意味什么/时间线/下一步）</h3><span class="cat">书面沟通</span><span class="badge r3">高管间</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">全员会前的书面全员公告（邮件/内网/视频配音皆可）结构化模板：①主题行=结果+时间窗+核心宣布；②开头钩子——第一句就抛最重要/最有冲击的信息，别埋；③背景3-4句——帮不熟悉的人懂来龙去脉；④「变什么」3-5条具体变化；⑤「对你意味着什么」按受众分段（工程/客户面/职能/全员）；⑥时间线表（日期→里程碑）；⑦下一步与如何参与（答疑会链接/内推/详版deck位置/匿名调研）；⑧结尾乐观+致谢。原则：平衡正式与可读、讲「为什么他们该关心」、自然留提问入口。把「领导要说什么」在做全员会前先沉淀成可复用公告骨架。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">全员公告骨架：①主题行=结果+时间+核心宣布；②开头第一句抛最重要信息（别埋）；③背景3-4句；④「变什么」3-5条；⑤「对你意味着什么」按工程/客户面/职能/全员分段；⑥时间线表；⑦下一步（答疑会/详版deck/匿名调研）；⑧结尾致谢。正式但readable，讲「为什么你该关心」，自然留提问口。</div></details>
  <div class="src">🔗 <a href="https://www.commswith.ai/library/content/all-staff-update-format" target="_blank">commswith.ai/library/content/all-staff-update-format</a></div>
  <div class="note">适用：③ 高管全员公告定调；② HRBP/内部沟通写全员通知骨架。</div>
</div>'''))

# 4 wp.me + linkedin CEO亲临一线（sec3 r3）
C.append(('sec3', '''<div class="hl">
  <div class="top"><span class="emoji">👋</span><h3>CEO 亲临一线：三班倒专场+2分钟视频+「人来了」效应（wp.me/linkedin·无桌员工触达）</h3><span class="cat">高管实践</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
  <p class="val">80%全球劳动力是无桌/一线员工（工厂、仓配、门店、医护），他们常无公司邮箱、难触达。破局靠一把手「在场」：①CEO按三班倒开三场town hall（含夜班11点、早班7点），「老板出现并直接讲话」本身就有压倒性正面效应——「人来了」这件事比内容更打动人；②多地点录2分钟CEO视频，经经理会议/休息区屏幕/员工手机分发；③配合移动消息App、休息区数字标牌、印刷品（甚至厕所 newsletter）多通道补位。核心：非桌员工靠「人到场+短平快视频+物理触点」而非长邮件触达，CEO亲临是把战略和一线对齐的最强信号。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">一线触达一把手打法：①按三班倒开三场town hall（含夜班/早班），「人来了」效应&gt;内容；②多地点录2分钟CEO视频，经经理会议/休息区屏/员工手机分发；③移动App+休息区数字标牌+印刷品（含厕所newsletter）多通道补位。无桌员工靠「在场+短视频+物理触点」而非长邮件；CEO亲临=战略与一线对齐最强信号。</div></details>
  <div class="src">🔗 <a href="https://wp.me/pectHZ-3r" target="_blank">wp.me/pectHZ-3r</a></div>
  <div class="note">适用：③ 一把手面向一线/无桌员工的「在场」沟通范式。</div>
</div>'''))

# 5 forbes + firstup 一线/无桌员工触达框架（sec3 r3+r2 双）
C.append(('sec3', '''<div class="hl">
  <div class="top"><span class="emoji">🏭</span><h3>一线/无桌员工触达框架：经理级联+Town Hall直连+数字标牌+观看派对（forbes/firstup·80%员工无桌）</h3><span class="cat">触达策略</span><span class="badge r3">高管间</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">面向制造/零售/医护/仓配等一线员工的town hall设计：①人肉渠道&gt;数字渠道——经理级联（pre-shift huddle发toolkit让经理讲清+答准）+高管Town Hall直连（让一线直接听顶层、懂自己角色如何支撑全局）最有效；②重大变革让CEO在Town Hall宣布、再让经理补细节（备talking points/FAQ/视频保证口径一致）；③数字标牌零动作触达（休息区/食堂轮播）、移动App推送、按需点播录像；④组织「观看派对」让各地站点一起看、破时区/排班、造共同体验；⑤会前用pulse/参与度调研找战略沟通缺口、微调议程。把「80%无桌员工也能同频」当成治理问题而非沟通细节。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">一线town hall设计：①人肉渠道优先——经理级联（toolkit+pre-shift huddle）+高管Town Hall直连顶层；②重大变革CEO先宣布、经理补细节（备talking points/FAQ/视频保口径一致）；③数字标牌+移动App推送+点播录像零动作补位；④「观看派对」造跨站点共同体验；⑤会前pulse调研找缺口调议程。无桌员工同频是治理问题。</div></details>
  <div class="src">🔗 <a href="https://www.forbes.com/sites/forbescommunicationscouncil/2022/09/20/the-best-and-worst-ways-to-reach-front-line-employees/" target="_blank">forbes.com/sites/forbescommunicationscouncil/2022/09/20/the-best-and-worst-ways-to-reach-front-line-employees</a></div>
  <div class="note">适用：③ 高管面向一线宣布变革+直连；② 经理级联toolkit+数字标牌触达。</div>
</div>'''))

# 6 betterat.work 异步全员会模板（sec2 r2）
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">⏳</span><h3>异步全员会模板：pre-read文档把低价值内容前移·现场只留能量/认可/Q&A（betterat.work）</h3><span class="cat">会议结构</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">100人开会一小时极贵，能异步的全异步。模板：领导者提前填好「使命/价值观/北极星/当前目标+KR进度」（这些场间基本不变，须常驻置顶），再加CEO更新、Big Wins、公告提醒、各部门KR进度链接；会前全员读/看。现场议程只需：欢迎2分→CEO更新8分（讲文档里没的要点，非复述）→公告2分→新人20秒×N→针对文档的Q&A15分→后半场跨团队social/workshop（breakout游戏或深度分享）。参与靠：多开breakout、chat/Slido收问、提前招募志愿主持、最佳问题给奖。把「信息搬运」挪到会前，现场只干「只有同场才能干」的事。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">异步全员会：①领导者提前填使命/价值观/目标/KR进度常驻文档+CEO更新/Big Wins/公告/部门进度链接，会前全员读；②现场只做欢迎2+CEO更新8（讲文档外的，不复述）+公告2+新人20s×N+Q&A15+跨团队social/workshop；③参与靠breakout多开、Slido收问、招募志愿主持、最佳问题奖。信息搬运前移，现场留「只能同场干」的。</div></details>
  <div class="src">🔗 <a href="https://betterat.work/tool/all-hands-meetings" target="_blank">betterat.work/tool/all-hands-meetings</a></div>
  <div class="note">适用：② 组织者把全员会低价值内容异步化、现场聚焦能量/认可/Q&A。</div>
</div>'''))

# 7 openculturebot 员工该问领导的25问框架（sec2 r2）
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">❓</span><h3>员工该问领导的25问框架（openculturebot·按战略/财务/产品/文化/人才分组+不问得像炫技）</h3><span class="cat">提问设计</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">解决「Any questions?→冷场」。给员工一套按主题分组的战略级提问清单：战略方向（哪根支柱让你睡不着/市场转差先暂停哪招）、财务健康（最大成本压力/债务再融资怎么读）、产品创新（哪款 sunset 最可惜/自建还是收购）、文化价值观（哪行为体现/违背价值观/混合会议如何嵌心理安全）、人才职业（系统低估了哪类技能/高潜到晋升平均多久）。提问纪律：用「能分享下…背后的思考吗」替代「为什么」；为全场问非为己；开放优于是非题；好奇优于对抗；先肯定已取得的再问挑战；用「我们」不用「我」；避开四害（个人薪酬/零食WiFi/甩锅/机密M&A）。Edelman 2023：常问战略问题的员工感到「被听见被重视」的可能性高2.4倍。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">给员工提问清单：按战略/财务/产品/文化/人才5组（如「哪根支柱让你睡不着」「最大成本压力」「哪款sunset最可惜」「哪行为违背价值观」「高潜到晋升多久」）。纪律：用「分享…背后思考」替「为什么」；为全场问；开放题；好奇非对抗；先肯定再问；用「我们」；避四害（薪酬/零食/甩锅/机密）。常问战略问题者感「被听见」高2.4倍（Edelman23）。</div></details>
  <div class="src">🔗 <a href="https://www.openculturebot.com/blog/questions-to-ask-leadership-ceo-in-a-town-hall" target="_blank">openculturebot.com/blog/questions-to-ask-leadership-ceo-in-a-town-hall</a></div>
  <div class="note">适用：② 组织者/HRBP给员工备提问清单、激活冷场Q&A。</div>
</div>'''))

# 8 india.aonmeetings 线上Town Hall主持与彩排（sec2 r2）
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">🎙️</span><h3>线上Town Hall主持与彩排：排练人非仅技术·给提问真实位置·24h内发纪要（india.aonmeetings）</h3><span class="cat">现场制作</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">线上全员会容易「内容对、体验翻车」。要点：①无障碍从一开始——字幕+可读slide，关键意义不只在图表/颜色/小截图；②「排练人，不只排练技术」——让每位讲者练首30秒、到下一位的过渡、最可能被问的那一题，删掉像书面报告的句子、把内部缩写翻成大白话、两位领导重复同点就留一个讲透；③给提问真实位置——会前+会中收问，主持把相似主题归并再答（比按序念每题更清晰），诚实说明「现场答/会后写/二者皆有」，不能答就明说「还没有答案」并给预期；④当天冷静节奏——早开房、制作组私聊通道、准时开始、producer盯钟+技术、moderator盯问与chat、主讲只管讲，出故障静默切备用；⑤会内一个工作日内发录像+关键决策短摘要+待办owner。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">线上town hall：①无障碍从一开始（字幕+可读slide，关键意义不只在图）；②排练人非仅技术——讲者练首30秒/过渡/最可能一题，删书面腔、缩写翻大白话、重复同点留一个；③给提问真实位置——会前+会中收问、主持归类再答、诚实说明答法、不能答明说+给预期；④当天早开房/私聊通道/准时/producer盯钟+技术/moderator盯问；⑤工作日内发录像+决策摘要+待办owner。</div></details>
  <div class="src">🔗 <a href="https://india.aonmeetings.com/online-town-hall-meeting" target="_blank">india.aonmeetings.com/online-town-hall-meeting</a></div>
  <div class="note">适用：② 内部沟通/HRBP主持线上全员会+彩排+纪要闭环。</div>
</div>'''))

# 9 icvdm 7个能拿到承诺的CEO提问（sec2 r2）
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">🎯</span><h3>7个能拿到承诺的CEO提问（icvdm·要指标/owner/时间线·非泛泛而谈+制作视角run-of-show）</h3><span class="cat">提问设计</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">给组织者/主持的「高质量提问」清单，目标是逼出可执行的承诺而非泛泛表态：①未来12个月公司最重要优先级是什么→要CEO盯的一个指标；②战略进度怎么衡量→更新节奏与owner；③竞位什么让你睡不着→具体缺口+本季第一步；④公司在员工发展上投什么→要项目名/预算/时间线；⑤我的团队明年成功长啥样→1-2个可写进团队目标的结果；⑥市场/技术变了战略怎么调→对IT/产品资源的影响；⑦员工今天能做的最有价值的一件事→一个可立即对齐的行为。配套制作视角：至少一次全员AV彩排、确认音频/直播/字幕/录制交接备份、演讲准备时对齐相机机位与 moderator 提示、上线前就关键承诺取得高管审批、定义Q&A如何文档化（字幕/FAQ/行动项owner+日期）。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">7个拿承诺的提问：①12个月最重要优先级→要盯的指标；②进度怎么衡量→节奏+owner；③竞位什么让你睡不着→缺口+本季第一步；④员工发展投什么→项目名/预算/时间线；⑤我的团队明年成功长啥样→可写目标的结果；⑥市场变了战略怎么调→资源影响；⑦员工今天最该做啥→可对齐行为。制作：AV彩排、音频/直播/字幕/录制备份、机位对齐、承诺先批、Q&A文档化（行动项owner+日期）。</div></details>
  <div class="src">🔗 <a href="https://icvdm.com/questions-to-ask-the-ceo-during-a-corporate-town-hall-meeting" target="_blank">icvdm.com/questions-to-ask-the-ceo-during-a-corporate-town-hall-meeting</a></div>
  <div class="note">适用：② 组织者备「逼出承诺」的高质量提问+run-of-show制作清单。</div>
</div>'''))

# 10 verifyed 会议认可系统化（sec2 r2）
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">🏅</span><h3>会议认可系统化：固定议程段live shout-out+同侪提名模板+跨部门可见（verifyed·持续可预测>偶发）</h3><span class="cat">认可设计</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">把认可做进会议常驻议程而非末尾点缀：①团队会/全员会固定留「Today's Recognitions」段——读top kudos、颁同侪奖，每周固定5分钟比偶发更有文化惯性；②同侪提名模板结构化（被提名人/具体行为/对团队影响/契合哪条价值观+经理或HR审批流），让「同事夸同事」可规模复制；③跨部门可见——市场听到工程的创新解法、客服成就公司级被看见，建跨职能欣赏与协作；④多渠道适配不同性格（会议口头/书面私信/数字徽章/内刊/同侪提名系统）；⑤一致性最关键——研究指持续可预测的认可比偶发更能稳士气、驱动参与。把「领导公开致谢」与「同侪提名」双轨并进。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">会议认可系统化：①固定议程段「Today's Recognitions」（读kudos/颁同侪奖），每周5分钟&gt;偶发；②同侪提名模板（被提名人/具体行为/影响/价值观+经理HR审批）可规模复制；③跨部门可见——工程/客服成就公司级被看见，建跨职能欣赏；④多通道适配性格（口头/书面/徽章/内刊/提名系统）；⑤一致性最关键，持续可预测&gt;偶发。</div></details>
  <div class="src">🔗 <a href="https://www.verifyed.io/blog/budget-employee-appreciation-gifts" target="_blank">verifyed.io/blog/budget-employee-appreciation-gifts</a></div>
  <div class="note">适用：② HRBP/组织者把认可做进会议常驻议程+同侪提名机制。</div>
</div>'''))

# ---------- HTML 墙插入 ----------
def find_grid_close(h, sec_marker):
    i = h.index(sec_marker)
    g = h.index('<div class="grid">', i)
    depth = 1
    j = g + len('<div class="grid">')
    while j < len(h):
        if h[j:j+4] == '<div':
            depth += 1; j += 4
        elif h[j:j+6] == '</div>':
            depth -= 1; j += 6
            if depth == 0:
                return j
        else:
            j += 1
    return -1

html = open(WALL, encoding='utf-8').read()

# 解析当前计数（从 tag span）
def cur_count(h, sec):
    m = re.search(r'<div class="sec %s">.*?<span class="tag">(\d+) 卡</span>' % sec, h, re.S)
    return int(m.group(1))

old_n3 = cur_count(html, 'sec3')
old_n2 = cur_count(html, 'sec2')
assert old_n3 == 60 and old_n2 == 128, (old_n3, old_n2)

sec3_close = find_grid_close(html, '<div class="sec sec3">')
sec2_close = find_grid_close(html, '<div class="sec sec2">')
assert sec3_close > 0 and sec2_close > 0, (sec3_close, sec2_close)

A3 = sum(1 for s, _ in C if s == 'sec3')
A2 = sum(1 for s, _ in C if s == 'sec2')
assert A3 == 5 and A2 == 5, (A3, A2)

sec3_cards = ''.join(h for s, h in C if s == 'sec3')
sec2_cards = ''.join(h for s, h in C if s == 'sec2')
assert sec3_cards.count('<div class="hl">') == 5
assert sec2_cards.count('<div class="hl">') == 5

html = html[:sec3_close] + sec3_cards + html[sec3_close:]
sec2_close += len(sec3_cards)
html = html[:sec2_close] + sec2_cards + html[sec2_close:]

NEW_N3 = old_n3 + A3   # 65
NEW_N2 = old_n2 + A2   # 134
html = re.sub(r'(<div class="sec sec3">.*?<span class="tag">)\d+( 卡</span>)',
              lambda m: m.group(1) + str(NEW_N3) + m.group(2), html, count=1, flags=re.S)
html = re.sub(r'(<div class="sec sec2">.*?<span class="tag">)\d+( 卡</span>)',
              lambda m: m.group(1) + str(NEW_N2) + m.group(2), html, count=1, flags=re.S)
html = html.replace('采集于 2026-08-17（十八轮补采 +188）｜',
                    '采集于 2026-08-18（十九轮补采 +%d）｜' % (NEW_N3 + NEW_N2))
assert '📌 本页由 yitong 沉淀整理 · 文化活动知识库' in html
open(WALL, 'w', encoding='utf-8').write(html)
open(TMP, 'w', encoding='utf-8').write(''.join(h for s, h in C))
print('OK wall updated: sec3=%d sec2=%d total=%d (+%d)' % (NEW_N3, NEW_N2, NEW_N3 + NEW_N2, A3 + A2))

# ---------- index.json 追加 ----------
def normkey(t):
    return re.sub(r'[^a-z0-9一-鿿]', '', t.lower())

def title_of(block):
    return block.split('<h3>')[1].split('</h3>')[0]

def rel_of(block):
    r = []
    if 'badge r3' in block: r.append('exec')
    if 'badge r2' in block: r.append('supervisor')
    return ','.join(r)

def note_of(block):
    return block.split('<div class="note">适用：')[1].split('</div>')[0]

idx = json.load(open(IDX, encoding='utf-8'))
existing_urls = set()
for d in idx:
    u = d.get('url', '')
    existing_urls.add(re.sub(r'^https?://', '', u).lower().rstrip('/'))

NEW_INDEX = []
for s, block in C:
    t = title_of(block)
    url = re.search(r'href="([^"]+)"', block).group(1)
    norm_u = re.sub(r'^https?://', '', url).lower().rstrip('/')
    assert norm_u not in existing_urls, "DUP in index: " + norm_u
    NEW_INDEX.append({
        "title": t, "normKey": normkey(t), "url": url,
        "sourceType": "secondary", "relation": rel_of(block),
        "summary": note_of(block)
    })

before = len(idx)
idx.extend(NEW_INDEX)
json.dump(idx, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
urls = [e['url'] for e in NEW_INDEX]
assert len(urls) == len(set(urls)), "batch url duplicate!"
print('index.json before=%d after=%d (+%d)' % (before, len(idx), len(idx) - before))
