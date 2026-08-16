# -*- coding: utf-8 -*-
# 员工大会 第十七轮补采（+10）卡片构建：追加到 staff-meeting.html 累计墙 + 写 .run_newcards.tmp.html + 追加 index.json
import re, os, json

BASE = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(BASE, 'staff-meeting', 'staff-meeting.html')
TMP = os.path.join(BASE, 'staff-meeting', '.run_newcards.tmp.html')
IDX = os.path.join(BASE, 'index.json')

# ---------- 10 张新卡（②③ 向，无①peer）----------
C = []

# A 中国建材集团 年中工作会 一手 dual r3+r2
C.append(('sec3', '''<div class="hl">
  <div class="top"><span class="emoji">🏭</span><h3>中国建材集团2026年中工作会（官方·董事长讲话+深化改革动员）</h3><span class="cat">央企工作会</span><span class="badge r3">高管间</span><span class="badge r2">上下级</span><span class="badge b1">一手</span></div>
  <p class="val">7月30-31日中国建材在山东泰安召开2026年年中工作会暨进一步深化改革动员部署会，党委书记、董事长周育先作《坚定信心 奋发图强 加快建设世界一流材料产业投资集团》讲话，总经理常张利主持并作工作报告。周育先总结上半年「经营质效稳步提升+四个融合深化」成效，部署下半年五方面：强化战略引领（编制落实十五五规划、全球竞争力）、加快价值创造（第一性原理）、加强创新驱动、深化改革行动（改制度变流程强组织优人员）、夯实党建基础；强调鼓励干部员工坚定「拼」的意志、砥砺「闯」的劲头、涵养「干」的氛围。真实央企一把手战略部署+全员动员范式（官方一手）。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">年中工作会以「董事长讲话（战略定调）+总经理主持报告（经营拆解）」双人主讲，先传达上级研讨班精神统一思想、再讲自身五方面部署；用「第一性原理/四个融合」把战略讲透；会后要求「拼闯干」三字诀层层传导。可借鉴其「战略引领→价值创造→创新→改革→党建」五段式与对干部「拼闯干」精神动员的口语化表达。</div></details>
  <div class="src">🔗 <a href="https://www.cbma.com.cn/cn/report/2608/0002-1.htm" target="_blank">cbma.com.cn/cn/report/2608/0002-1.htm</a></div>
  <div class="note">适用：③ 央企高管战略部署+文化落地范式；② 全员目标对齐+会后层层压实闭环。</div>
</div>'''))

# B 华能 年中工作会 权威媒体 dual r3+r2
C.append(('sec3', '''<div class="hl">
  <div class="top"><span class="emoji">⚡</span><h3>华能集团2026年年中工作会（董事长讲话·雄安新区·权威媒体报道）</h3><span class="cat">央企工作会</span><span class="badge r3">高管间</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">7月23-24日中国华能在雄安新区召开2026年年中工作会，董事长温枢刚作《牢记嘱托 砥砺奋进 以实干担当确保「十五五」实现良好开局》讲话，总经理钟国东作讲话、党组副书记郝金玉作总结。会议贯彻总书记考察讲话精神与央企负责人研讨班精神，总结上半年「双过半」、获2025年度央企负责人经营业绩考核A级；下半年以「六个进一步」（夯实安全保供/加快绿色转型/强化科技创新/深化改革/统筹发展与安全/加强党建）确保高质量完成年度目标。高管↔全员战略沟通+目标分解一手场景（权威媒体纪实）。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">年中工作会先以总书记考察讲话精神定政治站位、再讲「双过半」成绩与A级考核提振信心、后用「六个进一步」拆解下半年；用「十五五良好开局」把年度目标嵌入长期叙事；会后以「六个进一步」对应责任部门层层压实。可借鉴其「政治站位→成绩盘点→六维部署」三段式与对标上级精神的统一表述。</div></details>
  <div class="src">🔗 <a href="https://m.thepaper.cn/newsDetail_forward_33655240" target="_blank">m.thepaper.cn/newsDetail_forward_33655240</a></div>
  <div class="note">适用：③ 央企高管战略部署+目标分解；② 全员对齐+会后六维压实。</div>
</div>'''))

# C 中远海运 2026工作会议 一手 dual r3+r2
C.append(('sec3', '''<div class="hl">
  <div class="top"><span class="emoji">🚢</span><h3>中远海运集团2026年工作会议（官方·二届五次职代会·十五五蓝图）</h3><span class="cat">央企工作会</span><span class="badge r3">高管间</span><span class="badge r2">上下级</span><span class="badge b1">一手</span></div>
  <p class="val">1月26日中远海运在沪召开2026年工作会议暨二届五次职代会，董事长万敏代表党组讲话、总经理朱碧新作工作报告。会议回顾重组成立十年两次历史性发展，系统部署十五五：构建现代化航运产业体系、加快高水平科技自立自强（全面实施「AI+」行动、推进「货船人」三大平台）、加速全球通道布局、深化企业改革、统筹发展与安全；明确以「四稳」为目标、发挥「三个作用」、争当「三个排头兵」。一把手年度工作会+职代会合一的央企战略部署范式（官方一手，含职工代表民主参与）。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">年度工作会与职代会合一，先回顾十年两次跨越式发展阶段凝聚共识、再系统部署十五五五方面、用「AI+/货船人平台」把科技自立讲具体；以「四稳+三个作用+三个排头兵」对外对内统一表述。可借鉴其「历史阶段叙事→十五五系统部署→科技具象化」结构与职代会民主参与形式。</div></details>
  <div class="src">🔗 <a href="https://seafarer.coscoshipping.com/col/col10978/art/2026/art_6ca31739197d4719b765ee72da02c6e6.html" target="_blank">seafarer.coscoshipping.com/col/col10978/art/2026/art_6ca31739197d4719b765ee72da02c6e6.html</a></div>
  <div class="note">适用：③ 央企一把手年度战略部署（职代会合一）；② 全员目标对齐+十五五落地。</div>
</div>'''))

# D 中汽中心 中期工作会 一手 dual r3+r2 (格式角度：视频分会场+回顾片)
C.append(('sec3', '''<div class="hl">
  <div class="top"><span class="emoji">🚗</span><h3>中汽中心党委扩大会暨2026中期工作会（官方·视频分会场+工作回顾片）</h3><span class="cat">央企工作会</span><span class="badge r3">高管间</span><span class="badge r2">上下级</span><span class="badge b1">一手</span></div>
  <p class="val">7月27日中汽中心在津召开党委扩大会暨2026中期工作会，党委书记、董事长安铁成作《坚定信心 乘势而上 坚决打好「十五五」开局之战》讲话，总经理龚进峰作报告；采用「现场+视频会议」结合，总部主会场+外埠基地分会场，近500人出席，会前集体观看上半年工作回顾视频。安铁成强调对标「七个深刻学习领会」、锚定十五五战略宏图、以进一步深化改革为主线增强核心功能提升核心竞争力、坚持「实字当头、干字为先」。央企中期工作会「视频分会场全覆盖+回顾片暖场」的 tech/format 范式（官方一手）。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">中期工作会用「现场主会场+外埠视频分会场」实现异地全员同频；会前播自制工作回顾片暖场聚神；讲话以「对标七个深刻学习领会→锚定十五五→改革主线→实字当头干字为先」四段推进；近500人规模靠视频分会场降本提覆盖。可借鉴其「回顾片暖场+视频分会场全覆盖」的现场组织法与「实/干」口语化动员。</div></details>
  <div class="src">🔗 <a href="https://www.catarc.ac.cn/detail/25110f53f38446e4a4c503b180dbb7f7" target="_blank">catarc.ac.cn/detail/25110f53f38446e4a4c503b180dbb7f7</a></div>
  <div class="note">适用：③ 央企中期战略部署；② 视频分会场全覆盖+回顾片暖场的现场组织范式。</div>
</div>'''))

# E climbtheladder town hall best practices dual r3+r2
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">📋</span><h3>企业Town Hall最佳实践（climbtheladder·议程/主持/坦诚/跟进）</h3><span class="cat">执行框架</span><span class="badge r3">高管间</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">climbtheladder 把全员会定义为「靠准备与执行，从信息倾倒变参与事件」：会前发限时议程（主题/主讲/时长）设预期、测音视频防翻车；高管用简洁大白话讲业务影响而非术语；设 moderator 公平分配发言时间、专业控场Q&A；领导「share the stage」让跨部门声音上台显协作；会后速发录制+书面摘要（含未答问题清单）。避坑：回避难题显不真诚（裁员/业绩下滑须直面）、变抱怨场、技术翻车、承诺不兑现最伤信任——领袖须「真双向沟通、听且行」。全员会执行框架（②③通用）。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">全员会按「会前限时议程+技术彩排→高管大白话讲影响→moderator 控场Q&A→领导 share the stage→会后录制+摘要(含未答问题)」五步；裁员/业绩下滑等硬话题一把手须直面不绕；承诺必显式跟进兑现。警惕「回避难题/变抱怨场/技术翻车/承诺不兑现」四类失灵。</div></details>
  <div class="src">🔗 <a href="https://climbtheladder.com/what-is-a-town-hall-meeting-in-business-best-practices" target="_blank">climbtheladder.com/what-is-a-town-hall-meeting-in-business-best-practices</a></div>
  <div class="note">适用：② 全员会标准化执行框架；③ 高管坦诚沟通+信任建设。</div>
</div>'''))

# F thedetroitbureau comprehensive guide r2
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">📚</span><h3>Town Hall会议全指南（议题库+Q&A主持+最佳实践·thedetroitbureau）</h3><span class="cat">议题菜单</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">thedetroitbureau 给出全员会完整指南：议题五类——公司更新（业绩/新举措/战略）、部门概览（各负责人讲成就与计划）、员工认可（月度之星/晋升/亮点）、Q&A反馈、行业趋势；Q&A是「成败关键」——会前预判问题备答、设 neutral moderator 控流、敏感话题以共情+诚实回应、答不了就承诺跟进并发问答摘要；最佳实践覆盖目标定义/受众分析/议程开发/视觉辅助/互动元素(poll/投票)/技术测试含字幕/会后摘要与反馈。全员会议题菜单+Q&A主持手册（②）。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">从议题五类（公司更新/部门概览/员工认可/Q&A/行业趋势）搭议程；Q&A 设 neutral moderator 控流、敏感话题共情+诚实回应、答不了承诺跟进并发摘要；用 poll/投票等互动元素、会议含字幕保无障碍、会后发摘要+收反馈迭代。</div></details>
  <div class="src">🔗 <a href="https://www.thedetroitbureau.com/today-report/town-hall-meetings-a-comprehensive-guide-and-examples-1764798024" target="_blank">thedetroitbureau.com/today-report/town-hall-meetings-a-comprehensive-guide-and-examples-1764798024</a></div>
  <div class="note">适用：② 全员会议题菜单+Q&A主持手册。</div>
</div>'''))

# G granola.ai great all-hands r2
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">⏱️</span><h3>如何办好全员会（granola·异步纪要+限时+远程激活+问责）</h3><span class="cat">运营体系</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">granola 的实操要点：会后24h内发结构化 recap（更新摘要+决策+带责任人与 deadline 的行动项+未答Q&A书面回复+全文转录链接）→建可搜索的 all-hands 档案成组织记忆；严护Q&A时间块——某段超时就砍该段幻灯片而非砍Q&A（否则员工觉「领导更新比问题重要」）；行动项无owner/deadline立即贬值，每场开场先播「上次承诺进展」问责；45min拆解（胜果5/指标8/路线图10/互认5/Q&A12/收尾5）；远程激活用开场实时投票/点名远程同事/专用chat收Q&A/首尾5分钟开视频；用预置2-3题破Q&A冷场。全员会运营与问责体系（②）。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">全员会三板斧：①会后24h发 recap（决策+行动项带owner/deadline+未答Q&A+转录）；②死保Q&A时间块、超时就砍幻灯片；③开场先播「上次承诺进展」做问责、用预置题破冷场。远程靠实时投票+点名+专用chat+首尾开视频提参与。</div></details>
  <div class="src">🔗 <a href="https://www.granola.ai/blog/how-to-run-a-great-all-hands-meeting" target="_blank">granola.ai/blog/how-to-run-a-great-all-hands-meeting</a></div>
  <div class="note">适用：② 全员会会后问责+异步纪要+远程激活运营体系。</div>
</div>'''))

# H teamflect all-hands r2
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">🌐</span><h3>全员会最佳实践2026（teamflect·混合包容+议程+认可）</h3><span class="cat">包容设计</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">teamflect 强调全员会的「包容性」是成败尺：混合场景须「Remote-First」——数字参与者与现场前排享有同等提问/实时反应/分组权；hybrid 包容三招：Equalize the Screen（摄像头齐眼平线让远程觉被对话非围观）、Digital-First Q&A（永远先答远程同事问题显重视）、Synchronized Engagement（用双方手机/电脑同可访问的投票工具）；议程含破冰/新人介绍/业务结果/邀专家/成功故事/员工认可/价值观/反馈；月度或季度为理想节奏。把全员会当「远程优先的平等连接」设计（②）。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">混合全员会照「Remote-First」三招落地：摄像头齐眼平线（Equalize the Screen）、永远先答远程问题（Digital-First Q&A）、双方同可访问投票工具（Synchronized Engagement）；议程从破冰/新人/业务/专家/故事/认可/价值观/反馈搭；按月或季办。让远程同事与现场前排享有同等权利，防 room bias。</div></details>
  <div class="src">🔗 <a href="https://teamflect.com/blog/employee-engagement/all-hands-meetings" target="_blank">teamflect.com/blog/employee-engagement/all-hands-meetings</a></div>
  <div class="note">适用：② 混合/远程全员会的包容性设计与议程菜单。</div>
</div>'''))

# I gable.to hybrid all-hands dual r2+r3
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">🧭</span><h3>混合团队全员会2026指南（gable·5大失误+5种原型+议程模板）</h3><span class="cat">原型框架</span><span class="badge r2">上下级</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
  <p class="val">gable 指出多数混合全员会失败在三点：纯广播（CEO讲45min）、room bias（远程成旁观）、零跟进；列五大失误（无明确目的/room bias/音频忽视/零互动/无跟进）与五种原型——Alignment（战略对齐，重战略轻战术）/Celebration（表彰能量，短）/Transparency Q&A（最难也最值钱，直面不躲）/Strategic shift（重组/RTO/转型，讲why再讲what）/Post-mortem（出错后诚实复盘不甩锅）；给60min与30min两套议程模板；按远程占比选「现场+直播/混合默认/全虚拟」三格式。重大变革沟通（③战略转型原型）与混合执行（②）双覆盖。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">办全员会先定原型（对齐/表彰/透明Q&A/战略转型/复盘），一次最多混两种；避五大失误——无目的/room bias/音频差/零互动/无跟进；战略转型类务必「先讲why再讲what」并做好透明Q&A；按远程占比选格式、用60/30min模板控节奏。</div></details>
  <div class="src">🔗 <a href="https://www.gable.to/blog/post/all-hands-meeting" target="_blank">gable.to/blog/post/all-hands-meeting</a></div>
  <div class="note">适用：② 混合全员会原型框架+议程模板；③ 战略转型/重组类重大变革沟通。</div>
</div>'''))

# J haystackteam executive fireside chat r3
C.append(('sec3', '''<div class="hl">
  <div class="top"><span class="emoji">🔥</span><h3>高管炉边谈话（Fireside Chat）怎么跑（haystack·信任连接范式）</h3><span class="cat">信任沟通</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
  <p class="val">haystack 区分 town hall 与 fireside chat：前者领导定议程、对大群广播对齐；后者是「由 moderator 引导的一对一对话」，靠访谈者引出坦诚故事与洞察、员工提问塑方向，专长为建个人连接与信任。最佳实践：30-45min moderated 对话+留现场员工提问；设舒适座椅、无讲台、对话语气（信号「这是对话非宣讲」）；混合/远程用带 chat 侧栏的直播视频；问题混「大图（行业什么让你失眠）」与「个人（最好职业建议）」。最强内部沟通项目「town hall 做对齐透明 + fireside 做信任连接」双轨并用。高管↔干部/员工信任建设范式（③）。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">炉边谈话用「moderator 一对一引导+员工提问」替代宣讲：舒适座椅无讲台、对话语气；问题混大图战略与个人故事；混合用带chat侧栏直播。与 town hall 双轨——town hall 做对齐透明、fireside 做信任连接，尤其高管新上任/变革期建个人信任时更有效。</div></details>
  <div class="src">🔗 <a href="https://www.haystackteam.com/blog/how-to-run-an-executive-fireside-chat" target="_blank">haystackteam.com/blog/how-to-run-an-executive-fireside-chat</a></div>
  <div class="note">适用：③ 高管↔干部/员工信任连接范式（炉边谈话 vs 全员会双轨）。</div>
</div>'''))

# ---------- HTML 墙插入 ----------
html = open(WALL, encoding='utf-8').read()

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

sec3_close = find_grid_close(html, '<div class="sec sec3">')
sec2_close = find_grid_close(html, '<div class="sec sec2">')
assert sec3_close > 0 and sec2_close > 0, (sec3_close, sec2_close)

sec3_cards = ''.join(h for s,h in C if s == 'sec3')
sec2_cards = ''.join(h for s,h in C if s == 'sec2')

html = html[:sec3_close] + sec3_cards + html[sec3_close:]
sec2_close += len(sec3_cards)
html = html[:sec2_close] + sec2_cards + html[sec2_close:]

def count_in(sec_marker):
    i = html.index(sec_marker)
    g = html.index('<div class="grid">', i)
    close = find_grid_close(html, sec_marker)
    return html[g:close].count('<div class="hl">')

n3 = count_in('<div class="sec sec3">')
n2 = count_in('<div class="sec sec2">')
print('NEW sec3 placed:', sec3_cards.count('<div class="hl">'), '| NEW sec2 placed:', sec2_cards.count('<div class="hl">'))
print('TOTAL sec3:', n3, 'sec2:', n2, 'ALL:', n3+n2)

html = re.sub(r'(<div class="sec sec3">.*?<span class="tag">)\d+( 卡)</span>',
              lambda m: m.group(1) + str(n3) + m.group(2), html, count=1, flags=re.S)
html = re.sub(r'(<div class="sec sec2">.*?<span class="tag">)\d+( 卡)</span>',
              lambda m: m.group(1) + str(n2) + m.group(2), html, count=1, flags=re.S)
html = html.replace('采集于 2026-08-16（十六轮补采 +11）',
                    '采集于 2026-08-16（十七轮补采 +%d）' % (n3+n2))

open(WALL, 'w', encoding='utf-8').write(html)
tmp = ''.join(h for s,h in C)
open(TMP, 'w', encoding='utf-8').write(tmp)
assert '📌 本页由 yitong 沉淀整理 · 文化活动知识库' in html
print('OK wall updated + tmp written. cards total =', n3+n2)

# ---------- index.json 追加 ----------
def normkey(t):
    return re.sub(r'[^a-z0-9一-鿿]', '', t.lower())

NEW_INDEX = [
  {"title": C[0][1].split('<h3>')[1].split('</h3>')[0], "normKey": normkey(C[0][1].split('<h3>')[1].split('</h3>')[0]),
   "url": "https://www.cbma.com.cn/cn/report/2608/0002-1.htm", "sourceType": "firsthand", "relation": "supervisor,exec",
   "summary": "中国建材年中工作会：董事长讲话定调+总经理报告拆解，五方面部署（战略引领/价值创造/创新/改革/党建）+拼闯干动员"},
  {"title": C[1][1].split('<h3>')[1].split('</h3>')[0], "normKey": normkey(C[1][1].split('<h3>')[1].split('</h3>')[0]),
   "url": "https://m.thepaper.cn/newsDetail_forward_33655240", "sourceType": "secondary", "relation": "supervisor,exec",
   "summary": "华能年中工作会：雄安新区召开，董事长讲话+六个进一步部署，双过半+A级考核提振信心"},
  {"title": C[2][1].split('<h3>')[1].split('</h3>')[0], "normKey": normkey(C[2][1].split('<h3>')[1].split('</h3>')[0]),
   "url": "https://seafarer.coscoshipping.com/col/col10978/art/2026/art_6ca31739197d4719b765ee72da02c6e6.html", "sourceType": "firsthand", "relation": "supervisor,exec",
   "summary": "中远海运2026工作会+二届五次职代会：十五五五方面部署（产业体系/AI+/全球通道/改革/安全）+三个作用排头兵"},
  {"title": C[3][1].split('<h3>')[1].split('</h3>')[0], "normKey": normkey(C[3][1].split('<h3>')[1].split('</h3>')[0]),
   "url": "https://www.catarc.ac.cn/detail/25110f53f38446e4a4c503b180dbb7f7", "sourceType": "firsthand", "relation": "supervisor,exec",
   "summary": "中汽中心中期工作会：现场+视频分会场近500人+回顾片暖场，对标七个深刻学习领会+实字当头干字为先"},
  {"title": C[4][1].split('<h3>')[1].split('</h3>')[0], "normKey": normkey(C[4][1].split('<h3>')[1].split('</h3>')[0]),
   "url": "https://climbtheladder.com/what-is-a-town-hall-meeting-in-business-best-practices", "sourceType": "secondary", "relation": "supervisor,exec",
   "summary": "全员会最佳实践：会前限时议程+技术彩排、moderator控场、share the stage、会后摘要含未答问题；避四类失灵"},
  {"title": C[5][1].split('<h3>')[1].split('</h3>')[0], "normKey": normkey(C[5][1].split('<h3>')[1].split('</h3>')[0]),
   "url": "https://www.thedetroitbureau.com/today-report/town-hall-meetings-a-comprehensive-guide-and-examples-1764798024", "sourceType": "secondary", "relation": "supervisor",
   "summary": "全员会全指南：议题五类+Q&A成败关键（moderator控流/共情诚实/问答摘要）+互动含字幕+会后反馈"},
  {"title": C[6][1].split('<h3>')[1].split('</h3>')[0], "normKey": normkey(C[6][1].split('<h3>')[1].split('</h3>')[0]),
   "url": "https://www.granola.ai/blog/how-to-run-a-great-all-hands-meeting", "sourceType": "secondary", "relation": "supervisor",
   "summary": "全员会运营：会后24h recap(决策+行动项owner/deadline+未答Q&A)、死保Q&A时间块、开场问责、远程激活"},
  {"title": C[7][1].split('<h3>')[1].split('</h3>')[0], "normKey": normkey(C[7][1].split('<h3>')[1].split('</h3>')[0]),
   "url": "https://teamflect.com/blog/employee-engagement/all-hands-meetings", "sourceType": "secondary", "relation": "supervisor",
   "summary": "混合全员会Remote-First三招（齐眼平线/先答远程/同步投票）+议程菜单+月度季度节奏"},
  {"title": C[8][1].split('<h3>')[1].split('</h3>')[0], "normKey": normkey(C[8][1].split('<h3>')[1].split('</h3>')[0]),
   "url": "https://www.gable.to/blog/post/all-hands-meeting", "sourceType": "secondary", "relation": "supervisor,exec",
   "summary": "混合全员会5大失误+5种原型（对齐/表彰/透明Q&A/战略转型/复盘）+60/30min模板"},
  {"title": C[9][1].split('<h3>')[1].split('</h3>')[0], "normKey": normkey(C[9][1].split('<h3>')[1].split('</h3>')[0]),
   "url": "https://www.haystackteam.com/blog/how-to-run-an-executive-fireside-chat", "sourceType": "secondary", "relation": "exec",
   "summary": "高管炉边谈话：moderator一对一引导替代宣讲，town hall做对齐透明+fireside做信任连接双轨"},
]

idx = json.load(open(IDX, encoding='utf-8'))
before = len(idx)
idx.extend(NEW_INDEX)
json.dump(idx, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('index.json before=%d after=%d (+%d)' % (before, len(idx), len(idx)-before))
# 校验无重复 URL（本批）
urls = [e['url'] for e in NEW_INDEX]
assert len(urls) == len(set(urls))
print('batch url unique check OK')
