# -*- coding: utf-8 -*-
"""员工大会 r12 注入：把 13 张新卡（6 r3 + 7 r2）追加进累计墙，并写 .run_newcards.tmp.html。"""
import os, re

WALL = 'staff-meeting/staff-meeting.html'
TMP = 'staff-meeting/.run_newcards.tmp.html'

# ③ 高管间（6 张，纯 r3）
r3 = [
 dict(emoji='🔄', title='新CEO上任·内部传播四轨作战（沟通顾问）', cat='领导更替',
      url='https://www.comm-ext.com/the-rise-of-rizz-what-ceo-transitions-teach-us-about-executive-communications',
      val='沟通顾问 comm-ext 拆解新CEO上任内部传播四轨：Track1 全员Town Hall（现场+Zoom，对话式、无PPT，由前任CEO/HR负责人/董事做访谈主持，展现真实人格）；Track2 新领导可见性（首周all-hands）；Track3 Listening Tour（前90天倾听，焦点小组+脉冲调研）；Track4 四大审计（文化/战略/领导力/财务）。核心是"先倾听后广播"，让管理者成为主传播渠道（Manager Toolkit含会议指南/FAQ/升级路径）。',
      how='上任首场Town Hall用"对话"而非"宣讲"（配资深主持）；给各级管理者配工具包（关键信息+FAQ+升级路径），别只靠CEO单向发声；前90天以倾听为主，后90天再领导。',
      note='适用：③ 新CEO/高管更替期内部沟通总框架，强调对话式Town Hall+管理者下沉传播。'),
 dict(emoji='🚀', title='扭亏CEO首日Town Hall：透明·清晰·紧迫（PE实战）', cat='变革领导',
      url='https://chiefexecutive.net/how-to-lead-through-a-turnaround',
      val='Chief Executive 刊载PE扭亏案例：新CEO首场全员Town Hall直面焦虑。Step1 定并公开大胆5年目标（如25亿美元营收/高双位数毛利），用公开信讲清"我们在哪·去哪·怎么走"；Step2 框定战略（ELT重聚、聚焦客户细分、简化运营）；Step3 建结构；Step4 启动行动。核心理念：动荡期员工要的是透明、清晰、紧迫三件套，而非回避。',
      how='上任前用公开信同步"坏消息+目标"建立可信；首场Town Hall把"现状有多难"讲透再给路径；目标作北极星，先"赢得增长权"再扩张。',
      note='适用：③ 危机/扭亏/变革期新CEO首场全员会，强调坦诚定调。'),
 dict(emoji='📅', title='并购后CEO·月度全员会沟通计划模板', cat='并购整合',
      url='https://www.searchfundmarket.com/en/templates/100-day-plan',
      val='Search Fund Market 的100天模板：员工全员会（月度30分钟Town Hall，线上/线下）——业务更新（关键指标）、亮点与认可（点名到人/团队）、在做什么（优先级）、开放Q&A（"无禁区"）。要点：Q&A最重要，"员工不问是真在走廊问"；先沟通稳定再谈战略（员工先要"饭碗安全"才关心愿景）；别忽视文化、别跳过客户走访。',
      how='并购后固定月度Town Hall节奏；Q&A留足时间、鼓励尖锐问题；前30天先讲" continuity（团队/服务/承诺不变）"再画新战略。',
      note='适用：③ 并购/收购后新CEO对内沟通节奏，稳定优先于愿景。'),
 dict(emoji='📣', title='新领导前100天·沟通即战略（故事化）', cat='领导叙事',
      url='https://www.linkedin.com/pulse/your-first-100-days-everything-start-communicating-dean-foust',
      val='前高管沟通顾问Dean Foust：新领导前100天"沉默即信号（焦虑/不确定/冷漠）"。五大要点：① 映射利益相关方（员工要听"你怎么带"而非现成战略）；② 把20%时间给员工Town Hall；③ 用故事化讯息（简单/无 jargon/类比/量化收益），Satya Nadella用脑瘫儿子故事连接"真正看见一个人"→微软包容使命；④ 建思想领导力平台；⑤ 展现真实、谦逊、脆弱。HBR：新CEO百日内首发战略讲话，股价正向效应最强。',
      how='别用"倾听 tour"当拖延借口，前100天必须发声；用1个真实个人故事连接公司使命；员工不期待你Day1有答案，但期待你展现"怎么带"。',
      note='适用：③ 新CEO/高管上任沟通总纲，故事化+脆弱感建立信任。'),
 dict(emoji='🧭', title='领导更替为何失败（不是战略，是沟通）', cat='变革沟通',
      url='https://www.stimulus.co/insights/whyleadershiptransitionsfail',
      val='Stimulus：领导更替成败常不取决于战略，而取决于能否把愿景"讲进人心、促成行动"。5步玩法：① 发现与倾听（360°+脉冲调研，找激励点）；② 重塑公司叙事（连接愿景与使命，邀请参与）；③ 建领导者品牌（语气/承诺/风格一致锚点）；④ 规划前100天及之后（day-one到Q&A到小组会，混合触达）；⑤ 度量并校准（追踪参与度/情绪，反馈驱动改变）。HBR"为影响而投入（engaging for impact）"是卓越CEO标志。',
      how='把沟通当战略工具而非事后补丁；先听再播；每个触点（致辞/Town Hall/小会）都强化同一领导者品牌；用脉冲调研校准而非凭感觉。',
      note='适用：③ 高管更替/转型期，沟通→信念→行动链路。'),
 dict(emoji='🏛️', title='CEO更替·CCO作战框架（八大原则）', cat='高管传播治理',
      url='https://page.org/knowledge-base/a-framework-for-successful-ceo-transitions-insights-from-ceo-transitions-learning-share-out/',
      val='Page（CEO传播官网络）协作会提炼CEO更替八大原则：① 弄清董事会任命使命（增长/转型/修复）；② 时间是最贵资源（保护CEO日历、用短视频/内部Q&A提效）；③ 别忘了同级高管（让C-suite共参与信息开发，避免信号冲突）；④ Day1"内容盛宴"（视频/长信/视觉，先让员工见人再见稿）；⑤ 稳定来自节奏（Mondelez"路上明信片"系列）；⑥ 有意放下该放的（用象征性"第一"重置文化）；⑦ 邀同事声音共写下一章；⑧ 100天后复盘承诺兑现。',
      how='CCO/HR牵头做100天计划，先听后播；给CEO配"内容盛宴"首印象包；把同级高管拉进信息开发防信号打架；用"路上明信片"等轻量节奏建熟悉感。',
      note='适用：③ 高管更替治理层框架，CCO/HR如何编排CEO对内传播。'),
]

# ② 上下级（7 张，纯 r2）
r2 = [
 dict(emoji='📋', title='全员会60分钟议程模板（出席率65%→94%案例）', cat='议程模板',
      url='https://www.tinyteam.io/blog/team-meeting-agenda-template',
      val='Tiny Team 给出可复制全员会60分钟议程：① 公司更新10min（CEO/创始人：关键胜仗+财务健康+战略方向）；② 部门 spotlight 20min（每部门5min）；③ 员工认可10min（经理提名+里程碑）；④ 开放Q&A 15min（现场+匿名预提交）；⑤ 下一步5min。案例：40人电商公司用此模板把CEO开场从30min砍到10min、加现场Q&A与具体人认可，出席率65%→94%。',
      how='严格限时（CEO开场≤10min）；Q&A必须保护时间；认可点名到人而非只念数字；议程提前24h发出；结尾5min固定收行动项。',
      note='适用：② 常规月度/季度全员会议程骨架，数据驱动出席率提升。'),
 dict(emoji='🎯', title='2026全员会指南：三大产出+Q&A为王', cat='会议设计',
      url='https://recordmeeting.com/blog/all-hands-meeting',
      val='RecordMeeting 2026指南：有效全员会达成三产出——① 领导层直传决策/战略（消除层级失真）；② 以认可强化想重复的行为；③ 开放论坛建信任。议程四段（公司亮点10/战略更新15/团队spotlight10/开放Q&A15），Q&A最关键、砍slide补Q&A会丢信任。频率：快变期月度、稳定期季度；分布式团队默认虚拟、混合需额外facilitation。会后2小时内发录制+文字摘要，按日期归档可回溯战略演变。',
      how='会前48h开共享文档/Slack收问；把难问题答案提前备好（别临场糊弄）；会后2h内发录制+要点；用短期调研征集反馈并公示"下次改什么"。',
      note='适用：② 全员会目标设定与运营节奏，强调Q&A与录制归档。'),
 dict(emoji='🗂️', title='全员会详解：月度/季度议程模板+常见坑', cat='议程模板',
      url='https://woahtech.com/all-hands-meetings-explained-agenda-templates-best-practices-and-common-mistakes',
      val='WoahTech 详解全员会：45min月度模板（开场3/业绩8/战略10/部门highlight10/认可5/现场Q&A8/收尾1）；60min季度模板（CEO开场/业绩复盘/经验教训/下季优先级/团队spotlight/认可/Q&A）。常见坑：只报喜不报忧（损可信）、slide过多、不给员工声音、不跟进。最佳实践：提前发议程+讲"为什么重要"、匿名提问、平衡坦诚与信心、记录归档。',
      how='月度聚焦更新与认可、季度加深战略复盘；轮换speaker避免单场 overcrowd；平衡"承认挑战+给计划"建可信；Q&A用主持人分组+匿名。',
      note='适用：② 月度/季度全员会差异化议程，避坑清单。'),
 dict(emoji='⚠️', title='高效全员会：最佳实践与常见错误', cat='会议治理',
      url='https://wpwebify.com/blog/how-to-run-an-effective-all-hands-meeting-agenda-best-practices-and-common-mistakes',
      val='WP Webify 总结全员会最佳实践与雷区。实践：每议程项服务明确目的、多speaker（领导/经理/员工）、数据+故事平衡、提前brief演讲者、无障碍（字幕/录制/时区）、鼓励参与（投票/喊话/匿名）、会后跟进。雷区：太长（>60min易走神）、只报喜、slide堆积、不给员工声音、不跟进（承诺不兑现损信任）。样例议程：欢迎5/业绩10/战略10/highlight10/认可10/Q&A15/收尾5。',
      how='议程项"无公司级价值就下放小会/书面"；演讲者提前知时限与核心信息；承诺的答复/行动项会后必交付；匿名+现场混用Q&A。',
      note='适用：② 全员会运营清单（做/不做），适合PM/HR办会自检。'),
 dict(emoji='📊', title='会后情绪调研模板（测单场Town Hall）', cat='效果度量',
      url='https://www.mangoapps.com/templates/surveys/post-town-hall-sentiment-survey-2',
      val='MangoApps 会后情绪调研模板：测的是"单场领导沟通事件"而非整体敬业度——聚焦讯息清晰度、关切是否被听见、对领导方向的可信度。5点Likert+开放追问；默认匿名（员工才敢讲管理层讯息/未答关切/心理安全）；由HR/内部沟通/办会领导共拥，一人汇总主题再分派给对应领导。可跨场趋势对比，按主题（重组/战略/政策）微调问法。',
      how='会后立刻发短调研（留响应率）；默认匿名；专人汇总主题并路由给对应领导跟进；用"清晰但不可信"信号识别"讯息懂了但没解决不确定/没兑现"的缺口。',
      note='适用：② 单场Town Hall效果度量，区别于整体敬业度调研。'),
 dict(emoji='📈', title='员工Town Hall议程指南+成效度量', cat='效果度量',
      url='https://contacts.plenitudeconsulting.com/plenitudeconsulting-news/employee-town-hall-agenda-your-guide-1764803340',
      val='Plenitude Consulting 指南：办会前先定"目的"（无目的就取消）；慎选speaker并充分brief（含技术彩排、备份方案）；Q&A预设诚实答案、"不知道但会查"须跟进；议程提前发。成效度量多维：会后短调研（1-5+开放）、出席/参与率、Q&A量与锐度、领导反馈、行为变化、情绪时序追踪、对标初始目标。核心：连续改进，用数据 refinement 下一场。',
      how='会前明确单一目的；speaker全场彩排+技术双保险；Q&A备诚实答案并跟进未答项；用"出席率+问量+调研分+行为变化"组合度量而非只看人头。',
      note='适用：② Town Hall筹备清单与成效度量组合拳。'),
 dict(emoji='🎤', title='企业主持/控场 moderator 角色拆解', cat='主持控场',
      url='https://www.futuristsspeakers.com/corporate-moderator-emcee-host-facilitator',
      val='企业主持人（moderator）vs 主播（host）vs facilitators 拆解：moderator 聚焦讨论质量/提问/辩论/洞察/节奏管理，把演讲变互动。适用场景含员工Town Hall/高管论坛/公司会议/投资人宣讲。准备：研究组织与受众、建问题框架（开场/追问/过渡/观众/收尾）、规划过渡句。最佳实践：准备而非背稿、多听少说、问具体不泛（"哪个领导决策改变了你对创新的看法"而非"讲讲领导力"）、鼓励多视角、以takeaway收尾。',
      how='大型全员会配专业moderator管Q&A与节奏；提前建问题框架（含敏感题预案）；moderator不抢戏、把speaker和观众连起来；用过渡句保流畅、以关键takeaway收尾。',
      note='适用：② 大型全员会/高管论坛主持控场，moderator职责与避坑。'),
]

def card_html(c):
    rel_badge = '<span class="badge r3">高管间</span>' if c in r3 else '<span class="badge r2">上下级</span>'
    disp = c['url'].replace('https://', '').replace('http://', '')
    return f'''    <div class="hl">
      <div class="top"><span class="emoji">{c['emoji']}</span><h3>{c['title']}</h3><span class="cat">{c['cat']}</span>{rel_badge}<span class="badge b2">二手</span></div>
      <p class="val">{c['val']}</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">{c['how']}</div></details>
      <div class="src">🔗 <a href="{c['url']}" target="_blank">{disp}</a></div>
      <div class="note">{c['note']}</div>
    </div>'''

html = open(WALL, encoding='utf-8').read()

n_r3 = len(r3); n_r2 = len(r2)
sec2_marker = '<div class="sec sec2"'
footer_marker = '<footer'

# 1) 注入 6 张 r3 卡进 sec3 grid（插在 sec2 之前，即 sec3 网格闭合前）
assert sec2_marker in html, 'sec2 marker missing'
html = html.replace(sec2_marker, '\n'.join(card_html(c) for c in r3) + '\n' + sec2_marker, 1)

# 2) 注入 7 张 r2 卡进 sec2 grid（插在 footer 之前，即 sec2 网格闭合前）
assert footer_marker in html, 'footer missing'
html = html.replace(footer_marker, '\n'.join(card_html(c) for c in r2) + '\n' + footer_marker, 1)

# 3) 更新 tag 计数：sec3 25->31, sec2 82->89
html = html.replace('<span class="tag">25 卡</span>', '<span class="tag">31 卡</span>', 1)
html = html.replace('<span class="tag">82 卡</span>', '<span class="tag">89 卡</span>', 1)

open(WALL, 'w', encoding='utf-8').write(html)

# 4) 写当轮新卡临时文件（供 gen_run_page.py）
all_cards = [card_html(c) for c in r3] + [card_html(c) for c in r2]
open(TMP, 'w', encoding='utf-8').write('\n'.join(all_cards))

# 校验
new_r3 = html.count('badge r3')
new_r2 = html.count('badge r2')
print('WALL updated:', WALL)
print('  new card count (hl):', html.count('class="hl"'))
print('  badge r3:', new_r3, '| badge r2:', new_r2)
print('  tmp cards:', len(all_cards))
print('  tag counts now:', re.findall(r'<span class="tag">(\d+) 卡</span>', html))
