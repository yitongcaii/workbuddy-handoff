# -*- coding: utf-8 -*-
# 员工大会 第十五轮补采（+12）卡片构建：追加到 staff-meeting.html 累计墙 + 写 .run_newcards.tmp.html
import re, os

BASE = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(BASE, 'staff-meeting', 'staff-meeting.html')
TMP = os.path.join(BASE, 'staff-meeting', '.run_newcards.tmp.html')

# ---------- 12 张新卡（②③ 向，无①peer）----------
C = []

# A 中航集团(国航)2026年中工作会 一手 dual r3+r2
C.append(('sec3', '''<div class="hl">
  <div class="top"><span class="emoji">🛫</span><h3>中航集团（国航）2026年中工作会（国航官网一手）</h3><span class="cat">央企工作会</span><span class="badge r3">高管间</span><span class="badge r2">上下级</span><span class="badge b1">一手</span></div>
  <p class="val">中航集团7月24日召开2026年年中工作会，董事长作《坚定信心 接续奋斗》总结讲话、总经理作年中工作报告，以视频形式召开、设40个视频分会场，干部职工代表线上同步参会。讲话系统提出建设世界一流企业的「十个一流」（安全/枢纽/规模/资源配置/产品服务/运行控制/MRO/数智化/队伍/文化引领），并把「一流的文化引领」（使命驱动、精神传承、以人为本、和合协同）单列，强调统一文化体系、凝聚员工士气、激发员工活力。真实央企高管↔全员战略沟通+文化落地一手案例。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">高层会议用「主会场+40视频分会场」覆盖全员，董事长亲自讲形势与战略主线、把文化引领作为「十个一流」之一单列部署；把「凝聚员工士气、激发员工活力」写进世界一流要素，让文化从口号变可考核方向；复盘可参考其「总结讲话+工作报告」双文档结构与视频分会场组织方式。</div></details>
  <div class="src">🔗 <a href="https://www.airchinagroup.com/cnah/xwzx/zhxw/07/701262.shtml" target="_blank">airchinagroup.com/cnah/xwzx/zhxw/07/701262.shtml</a></div>
  <div class="note">适用：③ 高管↔全员战略沟通+文化落地一手范式；② 大型集团视频分会场全员覆盖组织法。</div>
</div>'''))

# B 兵器工业集团2026年中工作会 一手 dual r3+r2
C.append(('sec3', '''<div class="hl">
  <div class="top"><span class="emoji">🎖️</span><h3>兵器工业集团2026年中工作会（集团官网一手）</h3><span class="cat">央企工作会</span><span class="badge r3">高管间</span><span class="badge r2">上下级</span><span class="badge b1">一手</span></div>
  <p class="val">兵器工业集团7月23日召开2026年中工作会，党组书记、董事长作《坚定信心 接续奋斗 锚定目标抓落实》工作报告，总经理主持并作会议总结。报告鲜明树立「好于行业水平、好于竞争对手、好于历史同期」工作导向，围绕「核心功能突出、科技创新领先、效率效益优异、产业结构合理、治理能力现代、文化品牌卓越」六项目标推进「136」发展战略；强调把党的政治优势、组织优势转化为企业创新优势、发展优势、竞争优势。现场+视频方式，总部全体员工、各子集团直管单位负责人参会。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">年中工作会采用「董事长报告+总经理总结」双主讲结构，把「三个好于」作为贯穿全年的对标导向；将「文化品牌卓越」纳入战略目标清单，用「把政治/组织优势转化为发展优势」统一全员认知；会后层层传达抓落实（参考其「迅速传达学习贯彻」的闭环要求）。</div></details>
  <div class="src">🔗 <a href="http://www.norincogroup.com.cn/art/2026/7/24/art_84_573850.html" target="_blank">norincogroup.com.cn/art/2026/7/24/art_84_573850.html</a></div>
  <div class="note">适用：③ 军工央企高管战略部署范式；② 全员目标对齐+会后传达闭环。</div>
</div>'''))

# C 中国中化2026年中工作会 权威报道 dual r3+r2 (二手)
C.append(('sec3', '''<div class="hl">
  <div class="top"><span class="emoji">🌱</span><h3>中国中化2026年中工作会（能源新闻网权威报道）</h3><span class="cat">央企工作会</span><span class="badge r3">高管间</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">中国中化7月27-28日召开2026年中工作会，董事长作《把方向、管大局、保落实》讲话，总经理传达中央企业负责人研讨班精神并作年中报告。上半年经营性利润总额「优于年度预算、优于去年同期、优于行业平均」，提出从十个方面「把方向、管大局、保落实」：以「十五五」规划为战略指引、以新一轮改革化解重大风险、发挥创新主体作用推动科技与产业创新融合等。真实央企高管战略沟通一手案例（权威媒体逐字报道）。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">高管讲话以「把方向、管大局、保落实」三动作统领全员会主线，用「三个优于」先以数据稳住全员预期；把「十五五」规划作为目标驱动、把「科技创新与产业创新深度融合」作为抓手，让战略可拆解；参考其「传达上级研讨班精神+本单位报告」的双层议程。</div></details>
  <div class="src">🔗 <a href="https://cpnn.com.cn/news/nyqy/202607/t20260729_1905184.html" target="_blank">cpnn.com.cn/news/nyqy/202607/t20260729_1905184.html</a></div>
  <div class="note">适用：③ 化工央企高管战略沟通范式；② 用「三个优于」数据稳住预期+战略拆解。</div>
</div>'''))

# D 小米 核心干部千人大会 价值观八条 一手 r2
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">📱</span><h3>小米核心干部千人大会：价值观「真诚 热爱」八条诠释</h3><span class="cat">价值观对齐</span><span class="badge r2">上下级</span><span class="badge b1">一手</span></div>
  <p class="val">2023年9月小米召开千人大会（集团核心干部大会），公布新十年战略目标（大规模投资底层核心技术、成为全球新一代硬核技术领导者），并对价值观「真诚 热爱」作八条新诠释：和用户交朋友、工程师思维、主人翁精神、信任第一（坦诚沟通、所有事摊桌上说）、共创共识（决策后充分沟通让相关团队知道为什么）、结果导向、坚韧乐观、持续成长（敢于自我批评）。把「坦诚沟通、所有事情都能摊在桌面上说」写进价值观，是高管↔干部公开对齐文化的一手样本。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">用一场千人核心干部大会集中发布「新十年战略+价值观八条诠释」，把抽象价值观落成可执行的八条（信任第一=坦诚沟通摊桌上说、共创共识=决策后充分沟通why）；对齐后要求「决策之后充分沟通让相关团队每个人知道为什么并坚定执行」，避免只宣贯不闭环。</div></details>
  <div class="src">🔗 <a href="https://web.vip.miui.com/page/info/mio/mio/detail?postId=42451434" target="_blank">web.vip.miui.com/page/info/mio/mio/detail?postId=42451434</a></div>
  <div class="note">适用：② 核心干部大会做价值观对齐+战略发布的一手范式（上下级文化传导）。</div>
</div>'''))

# E 华为 心声社区 吐槽大会 二手 dual r3+r2
C.append(('sec3', '''<div class="hl">
  <div class="top"><span class="emoji">🗣️</span><h3>华为心声社区「吐槽大会」与自我批判机制（人民日报案例）</h3><span class="cat">民主监督</span><span class="badge r3">高管间</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">任正非公开倡导「心声社区」作为内部吐槽与建言平台——员工骂公司照登不误、不查马甲、不删尖锐批评，98%以上在职中方员工访问过；高层以身作则公开自我批评（承认早期股权分配错误、「任正非十宗罪」蓝军报告公开发心声社区并把错误揽自己身上）。辅以民主生活会、《管理优化报》形成「让吐槽大点声、让错误暴露、让矛盾释放」的闭环，用自由批评建立内部信任。案例来自《企业管理》/人民日报人民号。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">建「心声社区」式内部匿名发声渠道（不删帖不追查），让真话浮出；高层公开自我批评以身作则（蓝军批判直接发全员+揽责）；配民主生活会+限时回复督办闭环，把「吐槽」转改进；各级管理层置于民主监督氛围，用开放包容换组织信任。</div></details>
  <div class="src">🔗 <a href="https://www.peopleapp.com/rmharticle/30020505549" target="_blank">peopleapp.com/rmharticle/30020505549</a></div>
  <div class="note">适用：③ 高管以身作则建信任+自我批判文化；② 民主监督/员工发声渠道设计（上下级信任不越界）。</div>
</div>'''))

# F exec.com 主持人控场 二手 dual r3+r2
C.append(('sec3', '''<div class="hl">
  <div class="top"><span class="emoji">🎙️</span><h3>Town Hall 主持人/控场：一致口径·坏消息·敏感问题</h3><span class="cat">主持控场</span><span class="badge r3">高管间</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">Exec 的 town hall 主持指南：主持/moderator 须擅长传达口径、管理或 deflect 难题（尤其有媒体/公众在场）；会前系统规划议程、预演挑战性问题与应答；开场用几分钟定调（温暖欢迎+明确目的+是否开放Q&amp;A）；用「现场+视频」打破部门孤岛、让高管直面员工建信任；会议须录制、纪要全员可查，作为下次会议跟进起点。坏消息场景：保持积极、用必要变革解释「为什么」、给希望。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">指定有控场能力的主持人，会前列出「最可能棘手的问题+标准应答」；开场明确调性（是否开放Q&amp;A、何时答）；用「现场+视频」让高管直连一线；敏感/政治性问题由主持人统一口径 deflect，避免高管即兴踩雷；会后发纪要+录音，全员可溯。</div></details>
  <div class="src">🔗 <a href="http://www.exec.com/learn/town-hall-meeting" target="_blank">exec.com/learn/town-hall-meeting</a></div>
  <div class="note">适用：③ 高管出场时主持人的口径管理与敏感问题控场；② 全员会主持人角色设计。</div>
</div>'''))

# G predictiveindex 指定主持人/远程代言人/游戏化 二手 r2
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">🎯</span><h3>高效全员会：指定主持人·远程代言人·游戏化参与</h3><span class="cat">主持与参与</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">Predictive Index 全员会完整指南：会前固定日期+提前发邀请与提醒+结构议程+物料统一存放+指定 moderator 控屏控时+与 AV/IT 同步+为远程团队设 champion（转达遗漏信息、作远程声音）；会中真实（承认不完美、用故事连接、给远程者 grace）、游戏化参与（抛球鼓励提问/小奖品/问答工具 Mentimeter）、让多部门负责人上台；会后24h内发书面总结（关键指标+决策+Top问答）。覆盖从准备到跟进的全流程。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">设单一 moderator 统一控屏控时；为远程团队指派 champion 作「远程声音」；用 Mentimeter/小奖品游戏化提问；多个部门负责人轮番上台避免「一直讲的CEO」；会后24h书面总结回扣承诺，远程者靠录制+纪要补课。</div></details>
  <div class="src">🔗 <a href="https://dev.predictiveindex.com/blog/the-complete-guide-to-leading-effective-all-hands-meetings" target="_blank">dev.predictiveindex.com/blog/the-complete-guide-to-leading-effective-all-hands-meetings</a></div>
  <div class="note">适用：② 全员会主持人/远程平权/游戏化参与的完整执行清单。</div>
</div>'''))

# H tettra 讲故事七元素+财务透明 二手 r2
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">📖</span><h3>全员会讲故事：七元素结构 + 财务透明消除模糊厌恶</h3><span class="cat">叙事与透明</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">Tettra 全员会指南：①展现人性面（开头轻松、适度个人化拉近距离）；②讲清「当前战略为何存在」——故事让大脑神经活跃5倍、触发催产素，用故事的七要素（背景/触发事件/递进难题/转折/危机/高潮/结局）讲战略；③披露财务表现（人对模糊的厌恶&gt;对风险的厌恶，藏着不说员工会自动想最坏的鲨鱼，透明如救生艇稳住安全感）；④揭开未来计划（结尾讲，留期待）；⑤留Q&amp;A；⑥录制。把「故事+透明财务」作为对抗走神的核心。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">开场用轻松人性面暖场；用「七要素故事」替代罗列数据讲战略why；主动披露财务健康（哪怕不理想）消除模糊焦虑；未来计划放结尾造期待；全程留Q&amp;A+录制回放。</div></details>
  <div class="src">🔗 <a href="https://tettra.com/article/all-hands-meeting" target="_blank">tettra.com/article/all-hands-meeting</a></div>
  <div class="note">适用：② 全员会用故事化+财务透明提升吸收率与安全感。</div>
</div>'''))

# I productboard 四幕 town hall 叙事框架 二手 r3
C.append(('sec3', '''<div class="hl">
  <div class="top"><span class="emoji">🎬</span><h3>Town Hall 四幕叙事框架（产品高管版）</h3><span class="cat">叙事框架</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
  <p class="val">Productboard 的 town hall 叙事结构：开场用客户故事/市场现实/被忽略的挑战「定调」（别用「感谢到场」开场）；第一幕 Reality Check（诚实说在哪、什么在起作用、什么难）；第二幕 Strategy/Direction（不是路线图幻灯片，而是「基于现实我们决定X，理由Y，对你工作意味着Z，我们不再做W」）；第三幕 Team Story（点名具体人/团队的具体贡献）；第四幕 The Ask/号召（留一个具体action）；Q&amp;A 用「大家最怕公开问的问题」seed+示范脆弱；结尾用「我为何对前方兴奋」收。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">town hall 用四幕叙事替代「议题清单」：定调→现实核对（诚实）→战略方向（讲reasoning与trade-off）→点名团队故事→明确号召；Q&amp;A 主动抛「最难的问题」并诚实答（不知就说「我去查」）；结尾给一句值得记住的使命钩子。</div></details>
  <div class="src">🔗 <a href="https://www.productboard.com/product-management-prompts-library/product-town-hall-narrative/" target="_blank">productboard.com/product-management-prompts-library/product-town-hall-narrative</a></div>
  <div class="note">适用：③ 高管主导 town hall 的叙事化议程设计（讲why与trade-off，非念稿）。</div>
</div>'''))

# J findskills 全员会PPT模板+no-BS+会后24h 二手 r2
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">🧾</span><h3>全员会 PPT 模板 +「不装问题」技术 + 会后24h总结</h3><span class="cat">模板与跟进</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">findskills 的内部叙事/全员会模板：月度全员会6页结构——①公司状态（一句话诚实定位+3个指标vs目标色块）；②季度Rock进展（owner+状态，红色须一句「什么变了+在做什么」）；③我们骄傲的事（具体故事+点名+绑价值观）；④我们学到/没做成的（诚实一句，教组织「诚实被重视」）；⑤接下来30天（可行动的三件事）；⑥Q&amp;A（匿名提交常开，CEO规则：答所问/「不知我去查」+同问题问三遍=沟通缺口去修）。末尾留「no-BS questions」：最后5分钟匿名收最怕问的问题当众答，比45分钟精美PPT更建信任；会后24h内书面总结。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">用6页固定模板（状态/进展/骄傲/没做成/接下来/Q&amp;A）让全员会可复用；设「no-BS questions」匿名收最难问题当众诚实答；CEO 答所问、不知就承诺时限去查；同问题反复出现=沟通缺口去修；会后24h书面总结回扣承诺。</div></details>
  <div class="src">🔗 <a href="https://findskills.co/skills/internal-narrative" target="_blank">findskills.co/skills/internal-narrative</a></div>
  <div class="note">适用：② 全员会标准化模板+匿名难题+会后24h闭环（上下级透明）。</div>
</div>'''))

# K linkedin 7 things great all-hands 二手 r2
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">✅</span><h3>好的全员会做对的7件事（LinkedIn 框架）</h3><span class="cat">效果框架</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">Amy Gibson 的 LinkedIn 框架（高赞）：好的全员会不是信息宣读而是信任建设——①锚定现场（公司在哪+连大局）；②亮记分牌（目标vs实际色块+每数一句背景）；③把外部请进来（真实客户故事提醒为何重要）；④点名一个赢（具体人+具体事，胜过「团队辛苦了」）；⑤说出难事（诚实两分钟胜一年精美更新）；⑥一起向前看（预览下季+让人有准备）；⑦开放提问（匿名+现场，48h内跟未答）。强调「参与」而非「出席」，人记得的是连接感而非每个指标。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">全员会照「锚定→记分牌→客户故事→点名赢→说难事→向前看→开放提问」七步；难事诚实两分钟比精美更新更可信；点名具体人与事；匿名+现场双通道提问、48h内跟未答；把「让人走出门觉得『幸好我是这团队一员』」当成功标准。</div></details>
  <div class="src">🔗 <a href="https://www.linkedin.com/posts/amy-l-g_all-hands-comes-from-the-old-maritime-call-activity-7472981494429499394-9Ewk" target="_blank">linkedin.com/posts/amy-l-g_all-hands-comes-from-the-old-maritime-call-...</a></div>
  <div class="note">适用：② 全员会效果自评七步框架（上下级连接感设计）。</div>
</div>'''))

# L imasons 全球 town hall 多时区 二手 dual r3+r2
C.append(('sec3', '''<div class="hl">
  <div class="top"><span class="emoji">🌐</span><h3>全球 Town Hall 多时区同步策略（行业协会样本）</h3><span class="cat">跨国同步</span><span class="badge r3">高管间</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">iMasons 首次全球 Town Hall（2026-08）把分散各大洲的社区一次聚齐，给出全球统一 start times 表（新加坡22:00/迪拜18:00/巴黎16:00/伦敦15:00/纽约10:00/芝加哥9:00/洛杉矶7:00），覆盖战略进展、财务更新、参与方式。样本说明跨国全员会的核心不是「找一个大家都方便的时间」，而是把同一场会议按时区铺开、配同声传译/录制补课，让分布团队共享同一叙事。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">跨国全员会给出「全球统一 start times」表（各时区本地时间一目了然）；无法同刻到场的用录制+同声传译（Wordly 类）补课；议程全球一致（战略/财务/参与方式），让分散团队共享同一叙事而非各自解读。</div></details>
  <div class="src">🔗 <a href="https://imasons.org/activity/imasons-global-town-hall" target="_blank">imasons.org/activity/imasons-global-town-hall</a></div>
  <div class="note">适用：③ 跨国集团高管同步多地；② 全球员工平权参会（时区+传译+录制）。</div>
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
html = html.replace('采集于 2026-08-14（十四轮补采 +11）',
                    '采集于 2026-08-15（十五轮补采 +%d）' % (n3+n2))

# 写回
open(WALL, 'w', encoding='utf-8').write(html)

# 写临时新卡文件（供 gen_run_page.py）
tmp = ''.join(h for s,h in C)
open(TMP, 'w', encoding='utf-8').write(tmp)

# 页脚校验
assert '📌 本页由 yitong 沉淀整理 · 文化活动知识库' in html
print('OK wall updated + tmp written. cards total =', n3+n2)
