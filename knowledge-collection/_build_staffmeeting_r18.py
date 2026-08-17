# -*- coding: utf-8 -*-
# 员工大会 第十八轮补采（+11）卡片构建：追加到 staff-meeting.html 累计墙 + 写 .run_newcards.tmp.html + 追加 index.json
import re, os, json

BASE = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(BASE, 'staff-meeting', 'staff-meeting.html')
TMP = os.path.join(BASE, 'staff-meeting', '.run_newcards.tmp.html')
IDX = os.path.join(BASE, 'index.json')

# ---------- 11 张新卡（②③ 向，无①peer）----------
C = []

# 1 QBR 嵌入全员会（customerexperience） dual r3+r2
C.append(('sec3', '''<div class="hl">
  <div class="top"><span class="emoji">📊</span><h3>季度业务回顾（QBR）嵌入全员会（customerexperience·诚实暴露未达标+根因+下一步共创）</h3><span class="cat">业务复盘</span><span class="badge r3">高管间</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">10页框架——Slide4承载会议（scorecard hit/partial/miss，至少一条诚实miss）、Slide6价值卡点（根因+owner）、Slide7「我们做错了什么」（具体日期不遮掩）、Slide9行动项owner+date当场读出、附录从不演示只引用；会前48h发结果、会前写一页recap、会后24h发。把季度业务复盘做成「决策驱动而非数据倾倒」，适用于高管在全员会前面向全员/干部的硬核业务对齐。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">QBR做进全员会：①用10页上限，Slide4必须含至少一条诚实miss（忌藏附录）；②Slide6讲价值卡点带root cause+owner，不甩锅；③Slide7「我们做错了什么」具体不遮掩；④Slide9行动项owner+date当场读出；⑤会前发结果、会前写recap、会后24h发。高管用「诚实miss+根因owner」替代报喜不报忧，比纯战略宣讲更建信任。</div></details>
  <div class="src">🔗 <a href="https://customerexperience.io/blog/quarterly-business-review-qbr-agenda-template-examples" target="_blank">customerexperience.io/blog/quarterly-business-review-qbr-agenda-template-examples</a></div>
  <div class="note">适用：③ 高管季度业务复盘+硬核对齐；② 全员会嵌入QBR、诚实暴露缺口建信任。</div>
</div>'''))

# 2 QBR 执行摘要一页纸（toolkitcafe） r3
C.append(('sec3', '''<div class="hl">
  <div class="top"><span class="emoji">🗂️</span><h3>QBR执行摘要一页纸模板（toolkitcafe·Headline/财务快照/Top3 wins/risks/decisions）</h3><span class="cat">模板</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
  <p class="val">季度工作会/全员会前先出一张「季度Headline（一句话定调）+财务快照（营收vs目标±%、毛利、费用、现金/跑道）+Top3 wins（量化）+Top3 risks（影响+缓解）+必决事项（含背景+建议）」执行摘要；研究称纪律化QBR企业达标率2.5x。把高管在全员会前的「战略定调页」结构化为可复用模板，做开场钩子。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">高管在全员会/工作会前先填一页执行摘要：Headline一句话定调→财务快照（营收/毛利/费用/现金，全带±%）→Top3 wins量化→Top3 risks（影响+缓解）→必决事项（背景+建议）。用它做开场再展开，避免「80页PPT数据倾倒」。纪律化QBR企业年度达标率高2.5x。</div></details>
  <div class="src">🔗 <a href="https://toolkitcafe.com/blog/quarterly-business-review-template" target="_blank">toolkitcafe.com/blog/quarterly-business-review-template</a></div>
  <div class="note">适用：③ 高管季度战略定调页（一页纸模板），会议开场钩子。</div>
</div>'''))

# 3 追觅俞浩 高调战略/全员透明（x-techcon） dual r3+r2
C.append(('sec3', '''<div class="hl">
  <div class="top"><span class="emoji">🔓</span><h3>追觅俞浩「高调战略」：全员信息透明·信息直达末梢（m.x-techcon·每层级损耗20%）</h3><span class="cat">高管实践</span><span class="badge r3">高管间</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">追觅创始人兼CEO俞浩阐释频繁对外披露目标的深层动因：传统管理战略仅限少数高管、每经一层信息至少损耗20%，基层既不知其然又不敢直问高层，形成信息壁垒；他自公司2000人起推行全员信息透明——所有员工可参与战略会、各事业部月例会对其他部门开放、本人新想法第一时间发全员大群；随公司从2万扩至20万，把战略目标公之于众成为更高效治理方式。高管用「透明」破解层级信息损耗、建全员对齐（中国科技CEO真实实践）。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">借鉴俞浩做法：①把「战略信息损耗20%/层」当治理问题而非沟通细节；②扩大信息开放半径——战略会允许员工参与、事业部月例会对跨部门开放；③一把手新想法第一时间发全员群，绕开层级衰减；④组织扩张期更需「对外透明」替代层层传达。用透明降本建全员对齐，比保密式管理更适合快速扩张组织。</div></details>
  <div class="src">🔗 <a href="https://m.x-techcon.com/article/106221.html" target="_blank">m.x-techcon.com/article/106221.html</a></div>
  <div class="note">适用：③ 科技CEO战略透明治理范式；② 全员信息直达、破层级壁垒。</div>
</div>'''))

# 4 iM金融 黄秉宇 CEO Town Hall（digitaltoday） r3
C.append(('sec3', '''<div class="hl">
  <div class="top"><span class="emoji">🤝</span><h3>iM金融黄秉宇董事长CEO Town Hall（digitaltoday·与百名员工面对面+互动公益+不限题QA）</h3><span class="cat">高管实践</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
  <p class="val">iM金融控股董事长Hwang Byung-woo在iM Bank第二总部办「与CEO同行 iM P.R.O捐赠挑战」Town Hall，与约100名员工围绕集团经营方向、组织文化及新工作方式「iM P.R.O」面对面交流、听一线意见；现场设特产堆塔、传统游戏接力等互动带动参与并转化为公益捐赠，设不限主题QA、现场颁「iM PRO优秀员工」奖。CEO把Town Hall当常态化沟通+文化建设载体（韩国金融集团真实案例）。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">CEO Town Hall落地：①一把手与约百名员工面对面、听一线而非宣讲；②用轻互动（游戏/公益挑战）破冰带动参与、顺带做社会责任；③设不限主题QA+现场颁奖把认可做进大会；④将其定位为「常态化沟通+文化载体」而非偶发活动。高管用「面对面+轻互动+不限题」建立亲和与信任。</div></details>
  <div class="src">🔗 <a href="https://www.digitaltoday.co.kr/cn/view/27532/hwang-byeong-woo-im-financial-chairman-holds-townhall-meeting-with-employees" target="_blank">digitaltoday.co.kr/cn/view/27532/hwang-byeong-woo-im-financial-chairman-holds-townhall-meeting-with-employees</a></div>
  <div class="note">适用：③ 金融集团CEO Town Hall常态沟通+文化建设范式。</div>
</div>'''))

# 5 员工倾听策略 Town Hall + Skip-level（vantagecircle） dual r3+r2
C.append(('sec3', '''<div class="hl">
  <div class="top"><span class="emoji">👂</span><h3>员工倾听策略：Town Hall + Skip-level（vantagecircle·跨越直属上级的倾听）</h3><span class="cat">倾听机制</span><span class="badge r3">高管间</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">把Town Hall列为十大倾听方式之一（定议程/提前沟通/开放对话/视觉辅助/控时/鼓励参与/透明回应/会后摘要/收反馈），并强调 Skip-level meeting 是必做项——更高层管理者直接对话不向其汇报的员工、绕开直属上级，获取未被过滤的一线洞察、显「高层真在乎」；另含360反馈、正确倾听工具选择（单一工具避免数据过载）。高管用Town Hall+Skip-level组合打通「全员+越级」双通道倾听。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">倾听组合拳：①Town Hall做全员开放对话（议程/提前沟通/透明回应/会后摘要闭环）；②必做Skip-level——高管直接对话不向其汇报的员工、绕开直属上级拿未过滤一线洞察；③配360反馈与单一倾听工具（避免多工具数据过载）。用「全员Town Hall+越级Skip-level」双通道，比只听直属层更近现场。</div></details>
  <div class="src">🔗 <a href="https://blog.vantagecircle.com/en/blog/employee-listening-strategy/" target="_blank">blog.vantagecircle.com/en/blog/employee-listening-strategy</a></div>
  <div class="note">适用：③ 高管越级倾听（Skip-level）；② 全员Town Hall倾听+反馈闭环。</div>
</div>'''))

# 6 全员会参与度度量与ROI（airmeet） r2
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">📈</span><h3>全员会参与度度量与ROI（Airmeet·KPI/情绪/sentiment·会前会中会后三段）</h3><span class="cat">度量体系</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">反对只看出席率（登录≠参与≠认同）；要给可量化KPI——75%投票参与、80%清晰度、30%培训报名增长、eNPS、留存率、session retention；会前兴趣信号→会中实时参与（watch-time/互动分析）→会后情绪与行为影响，三段追踪；用实时pulse survey抓新鲜反馈、用情绪分析补定量盲区；设基准（如70%出席/60%投票/75%好心情）跨场对比。把全员会从「信息会」升级为「战略对齐度量工具」。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">全员会度量三招：①弃「出席率=参与」误区，改盯投票参与/清晰度/eNPS/留存等KPI；②会前兴趣→会中实时互动→会后情绪行为，三段追踪；③会后用pulse survey抓新鲜反馈+情绪分析补定量盲区，并设基准跨场对比。用数据证明全员会ROI，向高管汇报更有底气。</div></details>
  <div class="src">🔗 <a href="https://www.airmeet.com/hub/blog/measuring-employee-engagement-in-townhalls-and-internal-events" target="_blank">airmeet.com/hub/blog/measuring-employee-engagement-in-townhalls-and-internal-events</a></div>
  <div class="note">适用：② 全员会参与度度量体系+ROI，向高管汇报用。</div>
</div>'''))

# 7 Slido for Teams 一站式互动 r2
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">💬</span><h3>Slido for Microsoft Teams 一站式互动（blog.slido·投票/匿名QA/词云·远程与现场同权）</h3><span class="cat">互动工具</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">Slido 嵌入 Teams 会议侧边栏，全员会可直接跑实时投票/调查/匿名Q&A/词云/测验，参与人不下载不登录、主持端几分钟配好；43%远程员工觉不被包含，Slido让远程与现场用同一种方式参与（线上用Teams app、现场手机链接）；会前/中/后都能收集输入包容跨时区；含Meeting analytics与导出（参与率/QA情绪）。把「20%时间给Q&A」的Slido法则落到Teams原生互动。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">全员会互动落地：①在Teams日历会议加Slido标签，主持端准备投票/匿名Q&A/词云；②远程与现场同权——线上用Teams app、现场扫手机链接，破除room bias；③会前收问/会中实时/会后导出analytics（参与率+QA情绪）；④用「至少20%时间给Q&A+匿名」提真话率。工具原生集成，免切换屏幕。</div></details>
  <div class="src">🔗 <a href="https://www.slido.com/microsoft-teams-powerpoint" target="_blank">slido.com/microsoft-teams-powerpoint</a></div>
  <div class="note">适用：② 全员会 Teams 原生互动（投票/匿名QA/词云），远程现场同权。</div>
</div>'''))

# 8 Vevox × Teams 匿名投票问答 r2
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">🗳️</span><h3>Vevox × Microsoft Teams 匿名投票问答（vevox·侧边栏集成·免切换屏幕）</h3><span class="cat">互动工具</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">Vevox 直接集成 Teams，会议/频道/聊天中跑匿名投票、测验、调查与Q&A，不离开会议不切屏；匿名参与促更诚实频繁互动，Q&A支持upvote排序、moderation开关、按最赞/最新排序、回复/归档；参与人点Vevox标签即可投票/提问/填调查，或vevox.app九位码加入；免费层即用、桌面移动皆支持、含Teams webinar。给全员会一个「匿名+零切换」的互动底座。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">全员会匿名互动：①Teams会议加Vevox标签，会前/中会中建投票/词云/排名/匿名Q&A；②开匿名+upvote，让硬问题浮上来、安静人也能问；③moderation开关控流、按最赞排序显重视；④参与人点侧栏标签或扫九位码加入，零下载。与Slido二选一作互动底座，关键是「匿名+不切屏」。</div></details>
  <div class="src">🔗 <a href="https://vevox.zendesk.com/hc/en-us/articles/360009153397-Using-Vevox-with-Microsoft-Teams" target="_blank">vevox.zendesk.com/hc/en-us/articles/360009153397-Using-Vevox-with-Microsoft-Teams</a></div>
  <div class="note">适用：② 全员会匿名投票/Q&A（Vevox×Teams），零切换。</div>
</div>'''))

# 9 全员会互动技巧2026（AhaSlides） r2
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">✨</span><h3>全员会互动技巧2026（AhaSlides·匿名QA 74%、24h纪要、200人拆分组）</h3><span class="cat">互动设计</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">开场2分钟用实时投票/词云破冰显参与；每10-15分钟用投票/举手/换讲者重置注意力；匿名Q&A——74%员工称匿名才更愿给真话，open mic偏袒外向与高管；硬问题直答，答不了给时限；超200人用分组讨论产出更高质量问题；会后24h发书面recap（更新/问答/决策/待办owner+时限），常比会议本身更有用；虚拟优先测技术、录播、混合专用远程moderator。把「结构化互动」做进议程而非末尾点缀。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">全员会互动落地：①开场实时投票/词云破冰；②每10-15分钟插投票/换讲者重置注意力；③匿名Q&A（74%更愿说真话），硬问题直答、答不了给时限；④200人以上拆小组产出高质量问题；⑤会后24h发recap（含待办owner+时限）。互动做进议程全程，不堆末尾。</div></details>
  <div class="src">🔗 <a href="https://ahaslides.com/blog/town-hall-meeting-guide/" target="_blank">ahaslides.com/blog/town-hall-meeting-guide</a></div>
  <div class="note">适用：② 全员会全程结构化互动+匿名Q&A+24h纪要。</div>
</div>'''))

# 10 全员会 production 制胜（event.com.sg） r2
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">🎬</span><h3>全员会 production 制胜（event.com.sg·音频/直播制作/混合平权/技术彩排）</h3><span class="cat">现场制作</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">多数全员会败在体验而非内容：音频是第一要素（听不清一切白搭）、直播多机位/稳定编码/干净feed、舞台屏与可读slide、直播投票与远程参与、全员技术彩排。混合最难——须给远程与现场同等强体验（专用远程moderator、远程问题进同一Q&A池、会话中至少两次点名远程）；议程先定目标再保互动时间（建议5欢迎/20领导更新/15业务/20Q&A/10认可/5收尾≈75min），Q&A与认可须与领导宣讲同权重规划。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">全员会制作清单：①音频优先（听不清=全盘输）；②直播多机位+稳定编码+干净feed；③技术彩排走全套；④混合专用远程moderator、远程问题进同一Q&A池、会话中≥2次点名远程；⑤议程按目标定、Q&A与认可与领导宣讲同权重，不为宣讲挤压。内容好但体验差仍失败，制作须早规划。</div></details>
  <div class="src">🔗 <a href="https://event.com.sg/blog/how-to-plan-a-town-hall-meeting" target="_blank">event.com.sg/blog/how-to-plan-a-town-hall-meeting</a></div>
  <div class="note">适用：② 全员会现场制作+混合平权，避免「体验翻车」。</div>
</div>'''))

# 11 互动目标→形式匹配（event.com.sg ideas） r2
C.append(('sec2', '''<div class="hl">
  <div class="top"><span class="emoji">🎯</span><h3>互动目标→形式匹配（event.com.sg·先定目标再选互动·避为花样而花样）</h3><span class="cat">互动设计</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">互动不是堆花样：先定义全员会目标（领导沟通/员工认可/文化建设/变革管理/知识共享…），再选匹配形式——领导沟通配live Q&A、认可配spotlight/里程碑/同侪赞赏、文化配storytelling、变革配匿名Q&A、知识配poll/quiz。匹配时强化信息、为花样而花样则分散。具体互动：live polling（实时read on the room）、匿名Q&A（去恐惧）、实时survey（边讨论边量情绪并直播回放）、互动quiz、观众投票、open mic；认可最强——spotlight/里程碑/同侪提名/奖项时刻/领导公开致谢。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">全员会互动设计：①先写「这场会主要为啥」（领导沟通/认可/文化/变革/知识）；②按目标选形式（沟通→live Q&A、认可→spotlight+同侪提名、变革→匿名Q&A、知识→poll/quiz），不为新颖而加；③认可段留给员工记忆点（领导公开致谢>书面）；④混合用统一app把现场远程拉平。目标-形式对齐，互动才有用。</div></details>
  <div class="src">🔗 <a href="https://event.com.sg/blog/town-hall-event-ideas-for-employee-engagement" target="_blank">event.com.sg/blog/town-hall-event-ideas-for-employee-engagement</a></div>
  <div class="note">适用：② 全员会互动「目标→形式」匹配设计，拒为花样而花样。</div>
</div>'''))

# ---------- HTML 墙插入（使用正确的 find_grid_close）----------
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
sec3_close = find_grid_close(html, '<div class="sec sec3">')
sec2_close = find_grid_close(html, '<div class="sec sec2">')
assert sec3_close > 0 and sec2_close > 0, (sec3_close, sec2_close)

sec3_cards = ''.join(h for s, h in C if s == 'sec3')
sec2_cards = ''.join(h for s, h in C if s == 'sec2')
assert sec3_cards.count('<div class="hl">') == 5
assert sec2_cards.count('<div class="hl">') == 6

html = html[:sec3_close] + sec3_cards + html[sec3_close:]
sec2_close += len(sec3_cards)
html = html[:sec2_close] + sec2_cards + html[sec2_close:]

# 真实新计数
NEW_N3 = 25 + 5   # 30
NEW_N2 = 82 + 6   # 88
html = re.sub(r'(<div class="sec sec3">.*?<span class="tag">)\d+( 卡)</span>',
              lambda m: m.group(1) + str(NEW_N3) + m.group(2), html, count=1, flags=re.S)
html = re.sub(r'(<div class="sec sec2">.*?<span class="tag">)\d+( 卡)</span>',
              lambda m: m.group(1) + str(NEW_N2) + m.group(2), html, count=1, flags=re.S)
html = html.replace('采集于 2026-08-16（十七轮补采 +177）',
                    '采集于 2026-08-17（十八轮补采 +%d）' % (NEW_N3 + NEW_N2))
assert '📌 本页由 yitong 沉淀整理 · 文化活动知识库' in html
open(WALL, 'w', encoding='utf-8').write(html)
open(TMP, 'w', encoding='utf-8').write(''.join(h for s, h in C))
print('OK wall updated: sec3=%d sec2=%d total=%d' % (NEW_N3, NEW_N2, NEW_N3 + NEW_N2))

# ---------- index.json 追加 ----------
def normkey(t):
    return re.sub(r'[^a-z0-9一-鿿]', '', t.lower())

def title_of(block):
    return block.split('<h3>')[1].split('</h3>')[0]

NEW_INDEX = []
for s, block in C:
    t = title_of(block)
    url = re.search(r'href="([^"]+)"', block).group(1)
    rel = 'supervisor,exec' if 'badge r3' in block and 'badge r2' in block else (
          'exec' if 'badge r3' in block else 'supervisor')
    summ = re.search(r'<div class="note">适用：([^<]+)</div>', block).group(1)
    NEW_INDEX.append({
        "title": t, "normKey": normkey(t), "url": url,
        "sourceType": "secondary", "relation": rel, "summary": summ
    })

idx = json.load(open(IDX, encoding='utf-8'))
before = len(idx)
idx.extend(NEW_INDEX)
json.dump(idx, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
urls = [e['url'] for e in NEW_INDEX]
assert len(urls) == len(set(urls)), "batch url duplicate!"
print('index.json before=%d after=%d (+%d)' % (before, len(idx), len(idx) - before))
