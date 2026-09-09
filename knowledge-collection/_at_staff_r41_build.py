# -*- coding: utf-8 -*-
"""员工大会 r41 补采 build：注入 5×③ + 5×② 共 10 张新卡到累计墙，写 tmp 卡文件，追加 index.json。"""
import json, os, re

KC = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(KC, 'staff-meeting', 'staff-meeting.html')
TMP = os.path.join(KC, 'staff-meeting', '.run_newcards.tmp.html')
IDX = os.path.join(KC, 'index.json')
RUN_DATE = '2026-09-10'
ROUND = 'r41'

def card(emoji, title, cat, rel_badge, rel_label, src_badge, src_label, val, exec_txt, url, note):
    return f'''<div class="hl">
      <div class="top"><span class="emoji">{emoji}</span><h3>{title}</h3><span class="cat">{cat}</span><span class="badge {rel_badge}">{rel_label}</span><span class="badge {src_badge}">{src_label}</span></div>
      <p class="val">{val}</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">{exec_txt}</div></details>
      <div class="src">🔗 <a href="{url}" target="_blank">{url}</a></div>
      <div class="note">适用：{note}</div>
    </div>'''

# ---------- ③ 高管间 (5) ----------
c3_1 = card('🗂️', '全员会 时间盒议程模板·七段结构（开场钩子→业务快照→战略聚焦→挑战坦诚→人/文化→Q&A→收尾）', '时间盒议程', 'r3', '高管间', 'b2', '二手',
  '一个可落地的 45-60 分钟全员会时间盒：0:00-0:05 开场钩子（用故事而非数据落地关键信息）、0:05-0:15 业务快照（营收/增长/客户胜仗）、0:15-0:25 战略聚焦（方向/OKR/为何重要）、0:25-0:35 挑战与坦诚（没做成的、在学的、怎么修）、0:35-0:45 人/文化/价值观（组织变化+团队胜仗+领导价值寄语）、0:45-0:55 Q&A（预筛+现场，备 5-7 个硬问题诚实答）、0:55-1:00 收尾（重申关键信息+致谢）。坏消息原则：透明讲挑战，别把坏消息包装成好消息，讲影响、讲修复计划、讲路径信心、邀共创。金字塔信息结构：核心信息→支撑点→证据/故事→行动号召。',
  '想搭一套不跑偏的全员会流程学 openskillindex「七段时间盒+金字塔」：先定单句核心信息（员工离开要记住的那句），再用 3-4 个支撑点展开，每段配具体客户/员工故事而非裸指标；开场用 60 秒故事钩子而非「今天过一下 Q3」，坏消息段坦诚讲影响+修复计划别粉饰；Q&A 提前备 5-7 个可能被问的硬问题、诚实不躲；收尾给一个具体可做的行动号召。适合从 0 搭全员会或重塑现有流程，关键「时间盒逼你做减法，故事比数据留得久」。',
  'https://openskillindex.com/skills/w95-awesome-claude-corporate-skills-executive-communication',
  '③ 高管/内部沟通负责人 × 全员（openskillindex 二手；全员会七段时间盒议程模板+金字塔信息结构，可作流程搭建范本）。')

c3_2 = card('🎯', '高管演讲 Think-Feel-Do 框架（认知→情感→行动·极简PPT）', '演讲框架', 'r3', '高管间', 'b2', '二手',
  '高管在全员会的演讲按「Think（认知）-Feel（情感）-Do（行动）」三段推进：Think 帮听众理解战略优先级（用具体客户/业务语言）；Feel 用接地气的小故事或观察建立情感连接（「我知道这很难听，但每次对话都建信任」）；Do 发出具体、可执行的挑战。配套：Slide 极简（每页一个核心观点、24pt+ 字体、高对比、图胜字）、演讲前走台彩排（timing/语气/转场/技术）、现场互动（设问/快问快答保能量）、真诚（讲人话、从心出发）。结尾用一句有力陈述或一个鼓舞故事留情感余韵。',
  '写全员会高管讲稿学 mosswarner「Think-Feel-Do」：先想清楚要让听众认知到什么战略优先级，再用一个真实小故事/观察触发情感共鸣，最后落到一个具体可做的挑战（「我挑战你们每人都向客户推荐一个顾问式方案」）；PPT 极简——每页一句话观点、24pt 以上字体、图表化、别和演讲者抢戏；上台前走台彩排 timing 与技术；用设问或快互动保能量；结尾一句 bold 陈述或一个故事留余韵。适合高管定稿全员会主旨演讲，关键「认知让人懂、情感让人动、行动让人走」。',
  'https://mosswarner.com/?p=4516',
  '③ 高管/发言人 × 全员（MossWarner 二手；Think-Feel-Do 演讲框架+极简 PPT，可作高管主旨演讲范本）。')

c3_3 = card('🔐', '高管「不能全透明时」如何保信任·目的性透明（法律/战略/未定/个人四克制）', '透明边界', 'r3', '高管间', 'b2', '二手',
  '全员会上「目的性透明」原则：透明≠和盘托出，而是有目的地分享员工需要的信息以保知情、对齐、被尊重。四类须克制：①法律/保密（HR 调查、绩效动作、未决诉讼）；②战略保护（产品路线图、定价、安全、商业秘密）；③未定决策（重组/预算/可能裁员，早说易生谣言且被迫改口）；④保护个人（不暴露会伤人或损声誉的私人情况）。不能全说时仍可信的做法：解释「为什么现在不能说」（法律/隐私/谈判约束）而非沉默；讲清决策怎么定、何时补信息；明确方向、指导原则与保持不变的事。总透明反而坏事——过早说制造恐惧、泄露战略、分散执行、制造法律风险。',
  '全员会遇到「还不能说」的信息学 cleindy「目的性透明」：先分四类克制——法律/保密、战略保护、未定决策、保护个人；真不能说时解释约束原因（「受法律/隐私/谈判限制，此刻不能展开，但会在 X 时补」）而非回避沉默；同步讲清决策机制与补信息的时间点；明确大方向、指导原则与不变的事，让团队在不确定中仍可对齐。适合重组/并购/降本等敏感全员会，关键「选择性透明不是减信任，是展现判断力的负责任领导」。',
  'https://cleindy.com/good-leadership-keeping-trust-with-purposeful-transparency/',
  '③ 高管/HRBP × 全员（The Center for Leadership Excellence 二手；目的性透明边界，可作敏感全员会沟通范本）。')

c3_4 = card('🪟', '全员会「有目的的透明」四支柱（沟通/问责/反馈/认可·透明≠过度分享）', '透明四支柱', 'r3', '高管间', 'b2', '二手',
  '职场透明四支柱是全员会信任底座：①沟通——固定节奏的 all-hands+已发布的决策日志+清晰升级路径，是 cadence 不是一次性事件；②问责——战略转向时员工知道谁定的、考虑了什么、期望什么结果，杜绝「上面某个地方定了」文化；③反馈——匿名 pulse/360/开门政策且真实闭环（建议进黑洞最伤人）；④认可——公开解释难决策理由的管理者被表彰，透明成文化规范。透明≠过度分享：可分享目标/战略/决策「为什么」，但保护个人 HR 事项、未决法律/财务风险、个人薪酬；边界由「相关性」定义——帮员工自信行动就分享，可能伤人或组织就保护。Gen Z 把透明当基线（85% 希望了解决策如何产生）。',
  '把全员会当透明底座学 predictiveindex「四支柱」：沟通上建可预期的 all-hands 节奏+决策日志（不是一次性喊话）；问责上每个战略转向都挂 visible owner+考量+期望结果；反馈上开匿名 pulse/开门政策并真的闭环（提了不理最伤）；认可上公开表彰「愿意解释难决策理由」的管理者。同时守边界——分享目标/战略/决策 why，保护个人 HR/未决法律风险/个人薪酬；用「相关性」判边界：帮人自信行动就分享，可能伤人/组织就保护。适合 HR/高管建高信任文化，关键「透明是 cadence 不是事件，闭环比发声更重要」。',
  'https://www.predictiveindex.com/blog/transparency-in-the-workplace/',
  '③ 高管/HR 负责人 × 全员（Predictive Index 二手；职场透明四支柱+边界，可作高信任文化范本）。')

c3_5 = card('👑', '新CEO首次全员会致辞结构（背景→愿景→3焦点→直面大象→透明承诺）', '新CEO首秀', 'r3', '高管间', 'b2', '二手',
  '新 CEO 首次全员会致辞可套「背景→愿景→3 焦点→直面房间里的大象→透明承诺」结构：开头讲自己背景与为何接 this 位（致敬团队天赋与奉献）；愿景用简单但有野心的一句话（成为客户数字化转型的首选伙伴）；聚焦 3 个领域（创新/客户中心/员工发展）各给具体动作（建创新实验室、加客户 face time、推培训与导师制）；主动点掉「传闻中的裁员」——澄清 mass layoff 不在计划、聚焦增长、把月度 town hall+开门政策作为透明标志；结尾强调每个人对成功的关键、共启新章。全文以「透明与开放沟通将是领导标志」收束。',
  '新 CEO 首秀全员会学 speecheshq「五段结构」：①背景与致谢（点名团队已有天赋与奉献，降防御）；②一句有野心的愿景（不堆形容词）；③3 个聚焦领域各给具体动作（创新实验室/客户 face time/培训导师）；④主动点掉「房间里的大象」（传闻中的裁员等），澄清边界、把月度 town hall+开门政策作为透明承诺；⑤强调每个人关键、共启新章。全程以「透明开放沟通是领导标志」贯穿。适合新 leader 首秀，关键「先降防御再给方向，直面传闻比回避更建信任」。',
  'https://speecheshq.com/?p=129',
  '③ 新任高管/CEO × 全员（Speeches HQ 二手；新 CEO 首秀致辞五段结构，可作履新沟通范本）。')

# ---------- ② 上下级 (5) ----------
c2_1 = card('📰', '坏消息坦诚沟通·七字段框架（fact/impact/解读/决策/owner/未知/下次更新）', '坏消息沟通', 'r2', '上下级', 'b2', '二手',
  '全员会讲坏消息用「七字段框架」强制高管准备：fact（发生了什么）、impact（多严重）、current interpretation（当下判断）、decision（已定什么）、owner（谁负责）、uncertainty（还不知道什么）、next update（何时回）。把事实与解读分层——事实是发生的事，解读是当下判断，调查是还在学，行动是下一步；混层会让员工分不清已知与假设。用 plain language 别用 headwinds/softness/reprioritization 等 euphemism（委婉不降恐惧反增自我解读）；明确哪些必须保密及为什么。CEO/责任人须点明「这一刻公司如何对待未达标/质量/裁员/客户流失/安全/战略反转」的文化标准。假确定（overstate control）比诚实命名不确定更伤信任。',
  '全员会要讲坏消息学 antoinebuteau「七字段+事实/解读分层」：先逼自己填 fact/impact/当下判断/已定决策/owner/还不知什么/下次更新时间；把事实与解读分开讲（事实=发生、解读=当下判断、调查=还在学），别让员工分不清已知与假设；用 plain language 直说（"营收差预期 15%"），别用 headwinds/优化等 euphemism；明确哪些须保密及原因；CEO 点明「这一刻公司如何对待未达标」的文化标准。跟进须兑现 revisit。适合未达标/质量/安全/战略反转全员会，关键「坏消息的目标不是情绪完美，是压力下有用」。',
  'https://www.antoinebuteau.com/all-hands-meetings-that-actually-run-the-company-series-6-how-to-talk-about-bad-news/',
  '② 领导/内部沟通 × 全员（Antoine Buteau 二手；坏消息七字段坦诚框架，可作危机/未达标全员会范本）。')

c2_2 = card('🎙️', '全员会 主持人/引导师分工（head chef/sous chef/station chefs/notetaker）', '主持人分工', 'r2', '上下级', 'b2', '二手',
  '大型全员会（40 人×1 小时=一整周工时）需「厨房团队」：head chef=主持人（moderator）负责引入与转场演讲者、看时钟、鼓励参与、应对意外，是必备技能；sous chef 至少 1 名，回应员工问题、提醒主持人技术故障；station chefs 若干，分管沟通 backchannel 与视频会议聊天框；另设 notetaker 会后整理洞察成 office-wide summary。会前做 practice run（至少和所有演讲者/chef 过一遍议程），宁可在朋友面前翻车也别在 500 人面前。每段写明目标与时段，砍掉「因为一直这么做」的环节。高管更新要短、可拆成多段由不同人讲。',
  '办大型全员会学 digital.gov「厨房团队分工」：设主持人（引入/转场/看钟/鼓励参与/应意外）+ 至少 1 名副主持（回问题/报技术故障）+ 若干 station chef（管聊天框/backchannel）+ notetaker（会后出 office-wide summary）；会前必做 practice run（和所有演讲者过议程，宁可朋友面前翻车）；每段写清目标+时段、砍掉「历来如此」的环节；高管更新要短、可拆多段由不同人讲；保持大团体「人人被服务」的规划感。适合 40+ 人全员会，关键「大会议像厨房，食材/准备/执行决定体验」。',
  'https://digital.gov/2020/06/30/bringing-our-humanity-work-5-ingredients',
  '② 活动/内部沟通负责人 × 全员（Digital.gov 二手；全员会主持人/引导师分工模型，可作大型会务范本）。')

c2_3 = card('🌐', '混合全员会 remote-first 包容设计（一屏一人/聊天大使/轮转时区/录制存档）', '混合包容', 'r2', '上下级', 'b2', '二手',
  '混合/远程全员会落「remote-first」设计避免两 tier 文化：①在场也每人一屏（即便同会议室也各自设备接入），远程同事才能见脸、读聊天、平等参与，而非看一间屋子的广角镜头；②指派 chat/Q&A 主持人，把远程声音读出来并点名致谢；③跨时区轮转会议时间，别总让同一地区扛深夜场；④每场都录并存档；⑤建清晰沟通规范（摄像头/参与/排障/礼仪）、给 facilitator 培训、定虚拟会议标准模板、领导以身作则。案例：Anthropic 全远程，每周全员会固定议程提前写在文档、演讲者对镜头讲、同步开聊天频道收问题。',
  '做混合全员会学 innovativehumancapital「remote-first」：在场也每人一屏接入（别挤一个会议室镜头），让远程同事见脸读聊天平等参与；指派 chat/Q&A 主持人把远程问题读出来点名；跨时区轮转会议时间显公平；每场录制存档；建沟通规范+facilitator 培训+虚拟会议标准模板、领导以身作则。可借鉴 Anthropic：固定议程提前文档化、演讲者对镜头讲、同步开聊天频道收问题。适合混合/分布式团队，关键「先为远程设计，在场体验通常不损」。',
  'https://www.innovativehumancapital.com/article/how-hybrid-work-has-changed-meetings-the-rise-of-virtual-collaboration',
  '② 领导/HRBP × 全员（Innovative Human Capital 二手；混合全员会 remote-first 包容设计，可作分布式团队范本）。')

c2_4 = card('📧', '全员会 会后 recap 闭环邮件（24h内·决策+负责人+日期·≤200词）', '会后跟进', 'r2', '上下级', 'b2', '二手',
  '全员会价值一半在会后：recap 邮件 24 小时内发（高利害当日发），让记忆未散就强化共同理解。结构：一句话摘要（高管只看这句）+ 已宣布的决策 + 行动项（负责人+具体任务+日期，缺任一就是愿望不是承诺）+ 下次会议。全员会类若目的是信息同步、无行动项，就砍掉行动表、聚焦「宣布了什么决策+去哪看细节」。忌太长（超 200 词没人读）、忌被动语态（"Sarah 批准了新定价" 而非 "经决定…"）、忌无 owner。同一封发给所有参会者保记录一致；recap 是会议的延伸不是补充。',
  '全员会会后闭环学 recordmeeting「24h recap」：会后立即（≤24h，高利害当日）发摘要邮件，结构=一句话头条+已宣布决策+行动项（每项是 负责人+任务+日期，无 owner 不是承诺）+下次会议；若纯信息同步会无行动项，砍掉行动表、聚焦宣布了什么+细节入口；控制 200 词内、用主动语态点名 owner、一封发全体保记录一致。可配 Granola/AI 纪要从录音直出初稿。适合向全员/管理层证明沟通闭环，关键「recap 是会议的延伸，发得越早你的版本越成为公认版本」。',
  'http://recordmeeting.com/blog/meeting-recap-email-template',
  '② 内部沟通/HR × 全员（RecordMeeting 二手；全员会 recap 闭环邮件，可作会后跟进范本）。')

c2_5 = card('📊', '全员会 互动化·现场投票/词云/emoji（打破单向广播·安全感刻意造）', '互动技术', 'r2', '上下级', 'b2', '二手',
  '把全员会从单向广播改成双向交流：会前 2 周预收+置顶投票问题、开场用 quick poll/quiz 破冰并定调参与；每 10-15 分钟换形式（故事/多媒体/聚光员工成就）重拉注意；用实时字幕/翻译照顾全球与听障受众；指派 host/moderator 均衡两个渠道（"在线同事有疑问吗？"防室内喧宾夺主），>250 人必须 moderator 过滤优先级；用匿名 Q&A/投票浮出热门；会后发录制/幻灯片/Q&A 摘要到公共 hub、发满意度短调研、看投票参与率/掉线时间点调下场。74% 员工若真匿名会更敢说——刻意设计安全感。',
  '让全员会「活」起来学 streamalive「双向设计」：会前 2 周收+置顶问题并让员工投票、开场 quick poll/quiz 破冰；每 10-15 分钟换形式（故事/视频/聚光员工成就）防走神；全球/听障用实时字幕翻译保包容；指派 moderator 均衡线上线下渠道（主动点名远程）、>250 人必设；匿名 Q&A/投票浮热门；会后发录制+Q&A 摘要到 hub、发满意度短调研、盯掉线时间点调下场。关键「设计成双向交换而非广播，74% 员工匿名才敢说，安全感要刻意造」。',
  'https://www.streamalive.com/blog/why-employees-engagement-matters-in-town-halls',
  '② 内部沟通/活动 × 全员（StreamAlive 二手；全员会互动化与包容设计，可作参与提升范本）。')

cards_3 = [c3_1, c3_2, c3_3, c3_4, c3_5]
cards_2 = [c2_1, c2_2, c2_3, c2_4, c2_5]
all_cards = cards_3 + cards_2

# ---------- 注入累计墙 ----------
html = open(WALL, encoding='utf-8').read()

# sec3 grid
i3 = html.index('<div class="sec sec3">')
g3 = html.index('<div class="grid">', i3)
insert_3 = ''.join(cards_3)
html = html[:g3+len('<div class="grid">')] + '\n' + insert_3 + html[g3+len('<div class="grid">'):]

# sec2 grid
i2 = html.index('<div class="sec sec2">')
g2 = html.index('<div class="grid">', i2)
insert_2 = ''.join(cards_2)
html = html[:g2+len('<div class="grid">')] + '\n' + insert_2 + html[g2+len('<div class="grid">'):]

# 计数更新：144→149 / 270→275
html = html.replace('    <span class="tag">144 卡</span>', '    <span class="tag">149 卡</span>', 1)
html = html.replace('    <span class="tag">270 卡</span>', '    <span class="tag">275 卡</span>', 1)

# hero 追加本轮段
html = html.replace('四十轮 enrich 2026-09-09(+7)</p>', '四十轮 enrich 2026-09-09(+7)｜ 四十一轮 enrich 2026-09-10(+10)</p>', 1)

# 顶部增量页链接 r40→r41
html = html.replace('runs/staff-meeting-2026-09-09-r40.html', 'runs/staff-meeting-2026-09-10-r41.html', 1)

open(WALL, 'w', encoding='utf-8').write(html)
print('WALL updated. len=', len(html))

# ---------- tmp 卡文件（供 gen_run_page.py）----------
open(TMP, 'w', encoding='utf-8').write(''.join(all_cards))
print('TMP written. cards=', len(all_cards))

# ---------- index.json 追加 ----------
def normkey(t):
    t = t.lower()
    t = re.sub(r'[^\w\u4e00-\u9fff]', '', t)
    return t

idx = json.load(open(IDX, encoding='utf-8'))
before = len(idx)

entries = [
  ('全员会 时间盒议程模板·七段结构（开场钩子→业务快照→战略聚焦→挑战坦诚→人/文化→Q&A→收尾）', 'https://openskillindex.com/skills/w95-awesome-claude-corporate-skills-executive-communication', 'secondary', 'exec', 'openskillindex：45-60min 全员会七段时间盒（开场钩子用故事/业务快照/战略聚焦/挑战坦诚/人文化/QA/收尾）+ 金字塔信息结构（核心信息→支撑点→证据故事→行动号召）；坏消息透明讲影响+修复计划不粉饰、邀共创。'),
  ('高管演讲 Think-Feel-Do 框架（认知→情感→行动·极简PPT）', 'https://mosswarner.com/?p=4516', 'secondary', 'exec', 'MossWarner：高管全员会演讲按 Think(认知优先级)-Feel(小故事情感连接)-Do(具体挑战) 三段；PPT 极简（每页一观点/24pt+/图胜字）、走台彩排、现场互动、真诚；结尾一句 bold 或故事留余韵。'),
  ('高管「不能全透明时」如何保信任·目的性透明（法律/战略/未定/个人四克制）', 'https://cleindy.com/good-leadership-keeping-trust-with-purposeful-transparency/', 'secondary', 'exec', 'The Center for Leadership Excellence：目的性透明——透明≠和盘托出；四类须克制（法律保密/战略保护/未定决策/保护个人）；不能说时解释约束原因而非沉默、讲清决策机制与补信息时点、明确方向不变的事；总透明反制造恐惧/泄露战略/法律风险。'),
  ('全员会「有目的的透明」四支柱（沟通/问责/反馈/认可·透明≠过度分享）', 'https://www.predictiveindex.com/blog/transparency-in-the-workplace/', 'secondary', 'exec', 'Predictive Index：透明四支柱=沟通(all-hands节奏+决策日志)/问责(战略转向挂 visible owner)/反馈(匿名pulse真实闭环)/认可(表彰解释难决策的管理者)；透明≠过度分享，保护个人HR/未决法律风险/个人薪酬，边界由相关性定；Gen Z 85% 视透明为基线。'),
  ('新CEO首次全员会致辞结构（背景→愿景→3焦点→直面大象→透明承诺）', 'https://speecheshq.com/?p=129', 'secondary', 'exec', 'Speeches HQ：新CEO首秀五段——背景致谢降防御+一句野心愿景+3聚焦领域各给具体动作+主动点掉传闻中的裁员并承诺月度town hall/开门政策+强调每人关键共启新章；以透明开放沟通为领导标志贯穿。'),
  ('坏消息坦诚沟通·七字段框架（fact/impact/解读/决策/owner/未知/下次更新）', 'https://www.antoinebuteau.com/all-hands-meetings-that-actually-run-the-company-series-6-how-to-talk-about-bad-news/', 'secondary', 'supervisor', 'Antoine Buteau：全员会坏消息七字段框架（fact/impact/当下判断/已定决策/owner/还不知什么/下次更新）；事实与解读分层、plain language 别用euphemism、明确保密边界、CEO点明文化标准；假确定比诚实命名不确定更伤信任。'),
  ('全员会 主持人/引导师分工（head chef/sous chef/station chefs/notetaker）', 'https://digital.gov/2020/06/30/bringing-our-humanity-work-5-ingredients', 'secondary', 'supervisor', 'Digital.gov：大型全员会「厨房团队」——主持人(引入/转场/看钟/鼓励参与/应意外)+副主持(回问题/报故障)+station chef(管聊天框)+notetaker(会后summary)；会前practice run；每段写清目标时段、砍掉历来如此的环节；高管更新短且拆多段。'),
  ('混合全员会 remote-first 包容设计（一屏一人/聊天大使/轮转时区/录制存档）', 'https://www.innovativehumancapital.com/article/how-hybrid-work-has-changed-meetings-the-rise-of-virtual-collaboration', 'secondary', 'supervisor', 'Innovative Human Capital：混合全员会 remote-first——在场也每人一屏接入、指派chat/Q&A主持人点名远程、跨时区轮转会议时间、每场录制存档、建沟通规范+facilitator培训+标准模板；案例Anthropic全远程固定议程文档化+对镜头讲+同步聊天频道。'),
  ('全员会 会后 recap 闭环邮件（24h内·决策+负责人+日期·≤200词）', 'http://recordmeeting.com/blog/meeting-recap-email-template', 'secondary', 'supervisor', 'RecordMeeting：全员会 recap 24h内(高利害当日)发；结构=一句话头条+已宣布决策+行动项(负责人+任务+日期)+下次会议；纯信息同步会砍行动表聚焦宣布了什么；≤200词、主动语态点名owner、一封发全体保记录一致；recap是会议延伸。'),
  ('全员会 互动化·现场投票/词云/emoji（打破单向广播·安全感刻意造）', 'https://www.streamalive.com/blog/why-employees-engagement-matters-in-town-halls', 'secondary', 'supervisor', 'StreamAlive：全员会改单向广播为双向——会前2周收+置顶投票问题、开场quick poll破冰、每10-15分钟换形式、实时字幕翻译保包容、moderator均衡线上线下(>250人必设)、匿名Q&A浮热门、会后发录制+Q&A摘要到hub；74%员工匿名才敢说，安全感须刻意造。'),
]

existing_urls = set(e.get('url','') for e in idx)
added = 0
for title, url, st, rel, summ in entries:
    if url in existing_urls:
        print('SKIP dup url:', url)
        continue
    idx.append({
        'title': title, 'normKey': normkey(title), 'url': url,
        'sourceType': st, 'relation': rel, 'summary': summ,
        'topic': '员工大会', 'slug': 'staff-meeting', 'round': ROUND, 'date': RUN_DATE,
    })
    added += 1

json.dump(idx, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'INDEX: before={before} added={added} after={len(idx)}')
