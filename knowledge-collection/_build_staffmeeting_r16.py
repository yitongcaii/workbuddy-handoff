# -*- coding: utf-8 -*-
# 员工大会 第十六轮补采（+11）卡片构建：追加到 staff-meeting.html 累计墙 + 写 .run_newcards.tmp.html
import re, os

BASE = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(BASE, 'staff-meeting', 'staff-meeting.html')
TMP = os.path.join(BASE, 'staff-meeting', '.run_newcards.tmp.html')

# ---------- 11 张新卡（②③ 向，无①peer）----------
C = []

# A 南方电网2026年中工作会 二手 dual r3+r2
C.append(('sec3', '''<div class="hl">
  <div class="top"><span class="emoji">⚡</span><h3>南方电网2026年中工作会（腾讯新闻现场报道）</h3><span class="cat">央企工作会</span><span class="badge r3">高管间</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">8月1日南方电网召开2026年年中工作会，董事长钱朝阳作讲话、总经理季明彬主持并讲话，以习近平新时代中国特色社会主义思想为指导，传达全国党建座谈会与中央企业负责人研讨班精神，锚定「十五五」航向部署下半年。钱朝阳提出立足「国家战略贯彻者/能源强国建设者/现代产业引领者/改革创新先行者/万家灯火守护者」五定位，聚焦「建设能源强国/一流企业/科技产业创新/六网协同/全面深化改革」五方向，强调「一张蓝图干到底、改革大道走到底」；季明彬要求把「两个一以贯之」融入全过程、层层压实责任、一级抓一级。真实央企高管↔全员战略沟通一手场景（权威媒体报道）。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">年中工作会以「董事长讲话+总经理主持讲话」双主讲，先传达上级研讨班精神统一思想、再讲自身战略五定位五方向；用「一张蓝图干到底」把战略连续性讲透；会后要求「深学细悟+层层压实+一级抓一级」抓落实闭环。可借鉴其「现场+视频」全员覆盖与「三大责任/三个作用/三个排头兵」的对外对内统一表述。</div></details>
  <div class="src">🔗 <a href="https://new.qq.com/rain/a/20260803A04REY00" target="_blank">new.qq.com/rain/a/20260803A04REY00</a></div>
  <div class="note">适用：③ 央企高管战略部署+文化落地范式；② 全员目标对齐+会后层层压实闭环。</div>
</div>'''))

# B 字节跳动CEO梁汝波全员信 二手 dual r2+r3
C.append(('sec3', '''<div class="hl">
  <div class="top"><span class="emoji">📧</span><h3>字节跳动CEO梁汝波全员信：刷新文化+10条领导力原则（2026）</h3><span class="cat">文化对齐</span><span class="badge r2">上下级</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
  <p class="val">2026年6月29日梁汝波时隔四年再发全员信，全面更新适配AI变革与组织发展的公司文化与领导力准则：使命仍为「激发创造，丰富生活」，但补上「从推荐时代到AI时代，践行使命方法一致——通过计算换智能、通过智能提升创造力与体验」；管理理念沉淀为业务战略/组织管理/人才策略/公共事务四部分；新版10条领导力原则补充「做有高度的事」「敢于设定高目标」、把「有危机感保持外部视角」「深入一线」列为独立条目、强调「Context over Control」；原则纳入管理者晋升与年度考核，脱离业务一线的管理层同步调整权责。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">用一封全员信集中刷新「使命+管理理念+领导力原则」三层文化体系，并明确把原则纳入晋升/考核硬约束；强调「Context over Control」替代层层管控、要求中高层「常态化下沉一线直面真实业务」；管理者不能只看短期流水、须锚定长期高价值赛道主动突破。文化传导靠「信+考核绑定」双保险。</div></details>
  <div class="src">🔗 <a href="https://caifuhao.eastmoney.com/news/20260630153230934220020" target="_blank">caifuhao.eastmoney.com/news/20260630153230934220020</a></div>
  <div class="note">适用：② 高管↔干部文化对齐+领导力准则落地（上下级传导）；③ 一把手亲自定调组织文化方向。</div>
</div>'''))

# C CEO并购沟通框架 二手 r3
C.append(('sec3', '''<div class="hl">
  <div class="top"><span class="emoji">🤝</span><h3>CEO如何向员工沟通并购（不引发恐慌的7步）</h3><span class="cat">变革沟通</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
  <p class="val">straighttalk 的并购/收购员工沟通框架：①快且透明——签约即宣布（或法律允许范围内尽早），说已知、承认未知、承诺定期更新，沉默=secrecy；②讲战略故事而非仅头条——why（增长/新市场/创新）、对公司/对员工（职业成长/更稳定）的好处，避免空谈「synergies」；③正面回应岗位安全与文化——员工第一反应是「我还会在吗」，诚实讲重组/汇报变化、别讲「一切不变」；④CEO亲自发声——全员town hall/视频会+团队级答疑+远程录播；⑤给下一步与渠道——本周/本月/本季动作、定期节奏、匿名Q&amp;A；⑥示文化尊重——用「走到一起」而非「接管」，突出共享价值观；⑦高频跟进——周/双周更新（哪怕「仍在评估」）+庆祝小胜。核心是「塑造员工对未来的感受」，做错先失人才。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">并购宣布CEO必须亲自上town hall，先快讲事实（签约/时间线）再讲why与对员工的好处；第一时间直面岗位安全（不回避、不谎称不变）；设匿名Q&amp;A+固定更新节奏消化焦虑；用「走到一起」语言尊重被并购方文化；首宣定调后靠周更+小胜庆祝建信任。</div></details>
  <div class="src">🔗 <a href="https://www.straighttalk.marketing/post/how-ceos-should-communicate-an-acquisition-to-employees-without-sparking-panic" target="_blank">straighttalk.marketing/post/how-ceos-should-communicate-an-acquisition-to-employees-without-sparking-panic</a></div>
  <div class="note">适用：③ 高管主导并购/重大变革全员沟通（CEO亲自、透明、直面岗位安全）。</div>
</div>'''))

# D RaganMcGill All-Hands&Town Hall Design playbook 二手 dual r3+r2
C.append(('sec3', '''<div class="hl">
  <div class="top"><span class="emoji">🎯</span><h3>All-Hands/Town Hall 设计实践（领导力沟通 playbook）</h3><span class="cat">沟通设计</span><span class="badge r3">高管间</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">RaganMcGill 把全员会/ town hall 定义为「刻意设计成双向参与、而非广播」的领导力实践：会前问「听众最需理解什么/最担心什么/我们需从他们那听到什么」，至少留30-40%时间给问答与对话而非演讲；用匿名提交让不敢公开问的真问题浮出；领导者为硬问题备诚实直答、不回避；会后速发书面摘要含跟进承诺。演进：每场后短调研「有用吗/怎么更好」；轮换主讲/主持避免绑定一人风格；大群体用实时投票或分组讨论提参与。成功信号：出席高且认为值；硬问题被诚实回答；会上的承诺被可见兑现；员工「被通知」变「被理解（知其所以然）」。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">把全员会当领导力实践来设计——30-40%时间留给Q&amp;A、匿名收真问题、硬问题诚实直答不绕；轮换主讲/主持防风格固化；每场后短调研迭代；会后书面摘要+兑现承诺建问责。警惕「45分钟宣讲+5分钟Q&amp;A到不了真问题」「答非所问」「永远正面无坏消息」三类失灵。</div></details>
  <div class="src">🔗 <a href="https://raganmcgill.co.uk/c4e/leadership/Practice/practice-all-hands-and-town-hall-design" target="_blank">raganmcgill.co.uk/c4e/leadership/Practice/practice-all-hands-and-town-hall-design</a></div>
  <div class="note">适用：③ 高管把全员会当信任建设实践设计；② 双向对话+匿名Q&amp;A+会后问责执行框架。</div>
</div>'''))

# E Slab 三段式议程+Etsy开场 二手 r2
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">🗂️</span><h3>全员会三段式议程（Community/Business/Q&amp;A）+ Etsy开场秀</h3><span class="cat">议程结构</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">Slab 的全员会议程分三段：I.Community（占10-15%）——开场非结构时间（讲个笑话/趣事暖场，Etsy用「opening act」让员工表演才艺、制造脆弱 exchange 与开放连接感）、新人介绍+趣事、里程碑/生日庆祝、按价值观点名 shoutout；II.Business（55-65%）——重申公司 purpose（不讲PPT，改请团队讲解决难题/请客户讲价值/请投资者讲为何投）、讲关键指标（请团队讲 initiative 如何直接关联指标）；III.Live Q&amp;A（20-25%）——匿名提交（Google Forms）、远程团队同权答、用 Slack 建会后追问 channel。并建议轮换演讲者、提前测 tech。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">固定「Community→Business→Q&amp;A」三段比例（10-15%/55-65%/20-25%）；开场用轻松非结构时间/Etsy式才艺暖场建连接；Business 段把「念PPT」换成「团队讲难题/客户讲价值/投资者讲理由」；Q&amp;A 留足20-25%、匿名提交+远程同权+Slack 会后追问。</div></details>
  <div class="src">🔗 <a href="https://slab.com/blog/all-hands-meetings" target="_blank">slab.com/blog/all-hands-meetings</a></div>
  <div class="note">适用：② 全员会标准化议程结构（社区暖场+业务+Q&amp;A比例分配）。</div>
</div>'''))

# F Lattice 当代全员会环节库+Sli.do 二手 r2
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">🧩</span><h3>当代全员会环节库（客户聚焦/Sli.do问答/文化故事/月度数据）</h3><span class="cat">环节设计</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">Lattice 列了高人气全员会环节：Customer spotlight（新客户是谁/为何选我们，建客户同理心）、Photo of the month（远程工位/客户现场/美食，拉近距离）、Leadership Q&amp;A（用 Sli.do 或 Slack 提前收问题+员工 upvote 排序，须定「是否匿名」政策）、Culture stories（团队/个人体现文化最佳面向的故事）、Anniversaries（周年员工讲故事+老照片）、Data of the month（一张简单图表+有人讲，帮员工跳出日常看成功新维度）。强调「会一开完就该规划下一届」、用 Airtable 建内容管理结构、一次只改一个点并收集反馈增量迭代。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">从环节库挑搭（客户聚焦/照片月/领导Q&amp;A/文化故事/周年/月度数据）；Q&amp;A 用 Sli.do 提前收+upvote 排序、明定匿名政策；会后即启动下一届规划、用 Airtable 管内容；每次只改一个点、收反馈增量迭代，避免大改翻车。</div></details>
  <div class="src">🔗 <a href="https://lattice.com/de/articles/how-to-organize-a-more-successful-contemporary-all-hands-meeting" target="_blank">lattice.com/de/articles/how-to-organize-a-more-successful-contemporary-all-hands-meeting</a></div>
  <div class="note">适用：② 全员会环节菜单+匿名/投票Q&amp;A+增量迭代运营法。</div>
</div>'''))

# G HubSpot 全员会指南 二手 r2
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">🧭</span><h3>HubSpot 式全员会指南（节奏+议程+匿名Q&amp;A）</h3><span class="cat">执行模板</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">consultevo 提炼的 HubSpot 式全员会：目标=战略更新（讲why非仅结论）+亮点与教训（庆祝进展也own失策）+强化文化（用故事非口号）+双向通道（live+异步提问）。节奏：月度全员（成长期）、季度深潜（战略/结果）、临时 town hall（重大发布/并购/危机）。议程模板：欢迎定调(5m)→指标进展(10-15m)→产品/项目聚焦(10m)→客户与员工故事(10m)→表彰shoutout(5-10m)→开放Q&amp;A(10-20m)→收尾下一步(5m)。Q&amp;A：匿名表单+公开投票+直播chat（远程由moderator监控），会前发链接分组相似问题；答最upvote的、不知就承诺跟进、会后书面汇总。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">按「可预测节奏（月/季/临时）」办全员会，用固定议程模板（定调→指标→聚焦→故事→表彰→Q&amp;A→收尾）；Q&amp;A 会前发匿名表单+upvote、会中 moderation、会后书面汇总；讲「why」与「own失策」并行，把文化讲成故事。</div></details>
  <div class="src">🔗 <a href="https://consultevo.com/hubspot-all-hands-meeting-guide" target="_blank">consultevo.com/hubspot-all-hands-meeting-guide</a></div>
  <div class="note">适用：② 全员会可复用节奏+议程模板+匿名Q&amp;A闭环。</div>
</div>'''))

# H Forbes Council 19招 二手 r2
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">💡</span><h3>让大型内部会议更吸引人的19招（Forbes Council）</h3><span class="cat">参与设计</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">Forbes 商业委员会19位成员的方法：以客户/患者故事开场连使命；把会议当「迷你学习市集」（贡献者在不同station轮转讲解）；像电视节目分「Good News Network/Behind the Scenes/AMA」三段保能量；提前给议题让团队带着贡献来；加趣味主题（如Back to the Future租DeLorean+ costumes讲转型）；互动元素（live Q&amp;A/投票/故事）；任命有感染力的leader当host创体验；聚焦「驱动使命的人」做spotlight；用故事把工作连到真实的人；把KPI连回对人的影响（15%增长→保岗位/新项目）；请使命一致的外部分享者破信息茧房。共识：别只读数据，show how it connects to real impact。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">大型内部会照「客户故事开场+学习市集/电视分段+趣味主题+互动+spotlight人+故事化KPI+外部声音」组合；任命有感染力的host而非只念稿的CEO；KPI必连「对人的影响」（保岗/新项目），别扔裸数字；提前发议题让团队带贡献来、结尾给action items。</div></details>
  <div class="src">🔗 <a href="https://www.forbes.com/councils/forbesbusinesscouncil/2025/02/26/how-companies-can-make-large-scale-internal-meetings-more-engaging" target="_blank">forbes.com/councils/forbesbusinesscouncil/2025/02/26/how-companies-can-make-large-scale-internal-meetings-more-engaging</a></div>
  <div class="note">适用：② 大型全员会/内部会的参与感与趣味化设计菜单。</div>
</div>'''))

# J 麦当劳董事长的一封信 二手 r2
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">✉️</span><h3>麦当劳（台湾）董事长年度员工信：真诚+危机后交心</h3><span class="cat">坦诚沟通</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">台湾麦当劳历任最高负责人每年农历年后给全员写一封信，2018年起由董事长李昌霖接续。2025年初在经历震撼品牌事件后，他的信直白写道：「麦当劳是由25000名麦胞共同打造的企业…应用最高标准守护每位伙伴，确保安全透明、能带来快乐希望的职场；对于让麦胞担心、让粉丝失望，我们没有任何借口，必须彻底检讨并有具体改革作为」——已责成全面检视职场安全/申诉流程/身心照护，并请益专业非营利组织。把「慇懃款待/真心诚意」内化为「不自满→将真诚落实日常」。一把手以信交心、危机后坦诚担责，是上下级信任修复样本。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">一把手以「年度信/全员信」做固定交心仪式，平时讲愿景与感谢、危机时第一时间坦诚担责（不找借口、点名具体改革动作）；把价值观（如「真诚」）落到「不自满+日常内化」；危机后明确「已责成X部门、请益第三方、进度持续对内沟通」，用具体动作替代空话重建上下级信任。</div></details>
  <div class="src">🔗 <a href="https://news.mcdonalds.com.tw/news/20250203/index.html" target="_blank">news.mcdonalds.com.tw/news/20250203/index.html</a></div>
  <div class="note">适用：② 一把手年度信交心+危机后坦诚担责（上下级信任修复，非幼稚表达）。</div>
</div>'''))

# K TalentHub Glints What is All Hands 二手 r2
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">📣</span><h3>全员会是什么·目的收益与常见误区（Glints）</h3><span class="cat">认知框架</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">Glints 对全员会的定义与最佳实践：目的=让全员同步方向、知角色、有提问反馈论坛；用清晰可达语言（避免 jargon/未解释财务术语/技术堆砌）、请不同演讲者（部门负责人/项目负责人/客户face员工）、互动（live poll/短调查/员工presentation/提前提问）、留足Q&amp;A（答不了就承认并承诺跟进）、诚实讲难题（岗位安全/财务/决策/薪酬/组织变化，机密或待定就明说而非含糊）、包容性（全球/混合团队考虑时区/语言/字幕/录制）、会后跟进（发含决策/行动项/未答问题的摘要+录制+材料）。常见误区：信息过载、单向广播、只讲正面、用会场做细分团队详审、不回应反馈、无明确目的。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">全员会按「同步方向→清晰语言→多演讲者→互动→留Q&amp;A→诚实讲难题→包容→会后摘要」八步；难题（岗位/财务/薪酬/组织变化）不回避、机密就明说；全球/混合团队配字幕/录制/交替时段；会后发决策+行动项+未答问题摘要，让信息不止存在于直播。</div></details>
  <div class="src">🔗 <a href="https://talenthub.glints.com/en-sg/blog/all-hands-meeting" target="_blank">talenthub.glints.com/en-sg/blog/all-hands-meeting</a></div>
  <div class="note">适用：② 全员会目的/收益/八步最佳实践+七大误区避坑。</div>
</div>'''))

# L PeopleWiseHR 8要素 二手 r2
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">🌟</span><h3>让全员会更有影响力的8个要素（PeopleWiseHR）</h3><span class="cat">效果框架</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">PeopleWiseHR 的8要素：①明确目的（更新/庆祝/攻坚，知why聚焦内容）；②建透明（公开讲成绩与挑战、分享绩效指标/新举措/待改进，让员工有知情权与投入感）；③跨团队亮点（点名个人/团队成就，boost士气也促他人效仿）；④留双向空间（live或预提交Q&amp;A给员工发声）；⑤保持参与感（互动投票/视频/团建时刻，虚拟用breakout room）；⑥聚焦愿景文化（提醒bigger picture与贡献意义）；⑦倡导福祉（从顶部强调work-life balance与心理健康，支持文化自上而下）；⑧会后跟进（摘要邮件/录制保要点留存、显领导 commitment）。核心：透明+参与+双向，把会议变对齐/激励/文化载体。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">全员会照「明确目的→透明讲成绩与挑战→点名跨团队亮点→留双向Q&amp;A→互动保参与→重申愿景文化→自上而下倡导福祉→会后摘要跟进」八要素；把「福祉/心理健康」由高管在台上倡导（支持文化自上而下）；会后摘要/录制让要点留存、显领导 commitment。</div></details>
  <div class="src">🔗 <a href="https://peoplewisehr.com/post/maximizing-the-impact-of-all-hands-meetings" target="_blank">peoplewisehr.com/post/maximizing-the-impact-of-all-hands-meetings</a></div>
  <div class="note">适用：② 全员会八要素效果框架（含福祉倡导与会后跟进）。</div>
</div>'''))

# ---------- 插入逻辑 ----------
html = open(WALL, encoding='utf-8').read()

def find_grid_close(html, sec_marker):
    i = html.index(sec_marker)
    g = html.index('<div class="grid">', i)
    depth = 1
    j = g + len('<div class="grid">')
    while j < len(html):
        if html[j:j+4] == '<div':
            depth += 1; j += 4
        elif html[j:j+6] == '</div>':
            depth -= 1; j += 6
            if depth == 0:
                return j
        else:
            j += 1
    return -1

sec3_close = find_grid_close(html, '<div class="sec sec3">')
sec2_close = find_grid_close(html, '<div class="sec sec2">')
assert sec3_close > 0 and sec2_close > 0, (sec3_close, sec2_close)

sec3_cards = ''.join(h for s,h in C if s == 'sec3')
sec2_cards = ''.join(h for s,h in C if s == 'sec2')

# 在各自 grid 闭合 </div> 之前插入
html = html[:sec3_close] + sec3_cards + html[sec3_close:]
# sec2_close 偏移（sec3 插入后位置后移）
sec2_close += len(sec3_cards)
html = html[:sec2_close] + sec2_cards + html[sec2_close:]

# 重算各 section 卡数
def count_in(sec_marker):
    i = html.index(sec_marker)
    g = html.index('<div class="grid">', i)
    close = find_grid_close(html, sec_marker)
    seg = html[g:close]
    return seg.count('<div class="hl">')

n3 = count_in('<div class="sec sec3">')
n2 = count_in('<div class="sec sec2">')
print('NEW sec3 cards placed:', sec3_cards.count('<div class="hl">'))
print('NEW sec2 cards placed:', sec2_cards.count('<div class="hl">'))
print('TOTAL sec3:', n3, 'sec2:', n2, 'ALL:', n3+n2)

# 更新 section tag 计数
html = re.sub(r'(<div class="sec sec3">.*?<span class="tag">)\d+( 卡)</span>',
              lambda m: m.group(1) + str(n3) + m.group(2), html, count=1, flags=re.S)
html = re.sub(r'(<div class="sec sec2">.*?<span class="tag">)\d+( 卡)</span>',
              lambda m: m.group(1) + str(n2) + m.group(2), html, count=1, flags=re.S)

# 更新 hero 行（采集日期 + 轮次 + 新增数）
html = html.replace('采集于 2026-08-15（十五轮补采 +12）',
                    '采集于 2026-08-16（十六轮补采 +%d）' % (n3+n2))

# 写回
open(WALL, 'w', encoding='utf-8').write(html)

# 写临时新卡文件（供 gen_run_page.py）
tmp = ''.join(h for s,h in C)
open(TMP, 'w', encoding='utf-8').write(tmp)

# 页脚校验
assert '📌 本页由 yitong 沉淀整理 · 文化活动知识库' in html
print('OK wall updated + tmp written. cards total =', n3+n2)
