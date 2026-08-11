# -*- coding: utf-8 -*-
import re, os

BASE = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(BASE, 'icebreaker', 'icebreaker.html')
TMP = os.path.join(BASE, 'icebreaker', '.run_newcards.tmp.html')

# card builder
def card(emoji, title, cat, rel, src, val, how, url, disp, note):
    badge = 'r3' if rel == 'exec' else 'r2'
    return f'''    <div class="hl">
      <div class="top"><span class="emoji">{emoji}</span><h3>{title}</h3><span class="cat">{cat}</span><span class="badge {badge}">{"高管间" if rel=="exec" else "上下级"}</span><span class="badge b2">二手</span></div>
      <p class="val">{val}</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">{how}</div></details>
      <div class="src">🔗 <a href="{url}" target="_blank">{disp}</a></div>
      <div class="note">{note}</div>
    </div>
'''

cards = []

# ===== ③ exec (5) =====
cards.append(card('👑', 'Centering the C-Suite · 5 活动筑牢高管团队信任与对齐', '高管信任', 'exec',
  'http://www.choosetheperk.com/blog/executive-leadership-team-meeting-ideas', 'choosetheperk.com/blog/executive-leadership-team-meeting-ideas',
  '为 ELT 会议/高管静修设计的活动，目标不是团建游戏而是把 C-suite 围绕使命/价值观/战略对齐：(1)两个反思问题——"你希望人不在场时别人怎么评你？""你在场时希望他们有什么感受？"；(2)ELT 读书会聚焦"怎样建立/破坏信任"；(3)Leadership Origin Story——最好的领导者是谁、他做了什么、如何影响你的领导观；(4)Pre-experience success——设想年底庆功倒推"我们做了什么/要成为谁/保持什么/停止什么"；(5)卡牌(团队/价值观卡)随机抽问。核心：让高管彼此了解价值观与意图，而非强制趣味。',
  '选"两个反思问题 + Leadership Origin Story"开场，配读书会/Pre-experience 收尾；务必由 CEO 先示范脆弱，避免变成汇报。',
  'http://www.choosetheperk.com/blog/executive-leadership-team-meeting-ideas',
  '适用：③ 高管团队(ELT/C-suite)信任与战略对齐——用价值观反思与叙事替代游戏。'))

cards.append(card('🎯', 'Executive Retreat Activities That Actually Drive Alignment', '高管静修', 'exec',
  'https://www.dmpcreative.llc/resources/executive-retreat-activities-that-drive-alignment', 'dmpcreative.llc/resources/executive-retreat-activities-that-drive-alignment',
  '明确"跳过信任摔和密室逃脱"，按对齐产出分三类：(信任)Leadership Journey Maps(职业时间轴标转折)/Formative Experiences Dialogue(配对讲塑造领导观的经历+替对方介绍)/Strengths & Blindspots Exchange(自评+匿名同伴反馈)/Values Auction(用"静修美元"竞拍价值观暴露真实优先级)；(战略)Strategy Mapping 上墙/客户旅程沉浸/资源分配模拟/Pre-Mortem/竞品战争推演；(沟通)Decision Autopsy 复盘重大决策。原则：高管活动要尊重智商、连接战略现实、产出真洞察。',
  '先排信任类(前半天)，再上战略类；Values Auction/Pre-Mortem 用真实议题；请中立引导师 hold 场。',
  'https://www.dmpcreative.llc/resources/executive-retreat-activities-that-drive-alignment',
  '适用：③ 高管静修/ELT offsite——用结构化脆弱+战略模拟替代"强制欢乐"。'))

cards.append(card('🧭', 'Building a Healthy & Aligned Executive Team · 一日工作坊议程', '高管工作坊', 'exec',
  'https://theorg.com/iterate/building-a-healthy-and-aligned-executive-team-in-one-day', 'theorg.com/iterate/building-a-healthy-and-aligned-executive-team-in-one-day',
  '基于 Lencioni 五 dysfunction 的一日高管工作坊完整议程：(1)Personal History——每人分享职业高光/最尴尬失败/塑造自己的经历/最大障碍/珍视之处；(2)Myers Briggs review——会前测 MBTI，会上用"我的人设/最大优势/想改的弱点"小结；(3)Personal Plan——人生最重要/热爱/长期愿景；(4)Conflict profiling——用 Issue Resolution Model 复盘未决难题；(5)Commitment clarity——CEO 抽干所有观点后拍板；(6)Accountability——同伴反馈(strengths + 拖累团队的行为)。全程强调"脆弱从顶层开始"。',
  '按信任→冲突→承诺→担责四段推进；MBTI 作破冰不贴标签；冲突段鼓励把争议摆上桌不内耗。',
  'https://theorg.com/iterate/building-a-healthy-and-aligned-executive-team-in-one-day',
  '适用：③ 高管团队一日对齐工作坊——Lencioni 框架落地的可照搬议程。'))

cards.append(card('🪞', '高管信任升级与协同突围 · 阿里裸心会工作坊', '高管裸心会', 'exec',
  'http://www.youjiangshi.com/training/385487.html', 'youjiangshi.com/training/385487.html',
  '面向高管团队融合/信任危机/战略转型的统一认知工作坊(HRD/HRBP 全程参与)：双工具驱动——生命年轮(画个人与企业共成长时间轴，标3高光+2低谷唤醒情感共鸣)+乔哈里窗(盲区探索破解认知偏差)；保留阿里基因——照镜子/揪头发/裸心会铁律(不评判/不打断/不记录)；闭环——从矛盾收集到公约签署；仪式感——能量地图/时光胶囊。适用场景：高管融合、业务瓶颈突破、危机复盘韧性重塑。',
  '会前1周收矛盾点+高管心智预热；模块二"照镜子"用能量温度计(1-10)破层级壁垒；裸心对话按阿里三铁律执行；收尾签团队公约而非"只谈不干"。',
  'http://www.youjiangshi.com/training/385487.html',
  '适用：③ 高管团队融合/信任危机——阿里裸心会体系(生命年轮+乔哈里窗+照镜子)本土化落地。'))

cards.append(card('🛠️', 'Leadership Team Building That Actually Works · 7 个无游戏练习', '领导力团建', 'exec',
  'https://www.unicornlabs.ca/blog/leadership-team-building-that-works', 'unicornlabs.ca/blog/leadership-team-building-that-works',
  '7 个不靠绳索场、既建信任又显化冲突的领导力团建练习(铁律：永远 debrief，讨论时间>活动本身)：(01)How to Work With Me 手册——一页写沟通/反馈偏好；(02)Failure Résumé——讲一个真实职业失败+教训，高层先认栽别人才能松气(脆弱循环)；(03)Personal Histories——Lencioni 经典三低 stakes 问题；(04)Pasta Tower——18分钟棉花糖挑战，debrief 甩锅怪谁；(05)Mining for Conflict——拿一个真议题练公开分歧；(06)Clearing Round——对每人一句欣赏+一个 start/stop 请求；(07)Pre-Mortem——设想明年失败倒推原因。心理安全感+赋能+建设性冲突三者齐备才出创新。',
  '每个练习后留比活动更长的时间 debrief；从 Failure Résumé/Personal Histories 开场建安全；冲突类(Mining/Pre-Mortem)放后半段。',
  'https://www.unicornlabs.ca/blog/leadership-team-building-that-works',
  '适用：③ 领导力/高管团队——用"脆弱循环+建设性冲突"替代信任摔与破冰游戏。'))

# ===== ② supervisor (6) =====
cards.append(card('🪜', 'Skip-Level Meeting Questions · 30 个建信任提问', '越级沟通', 'supervisor',
  'https://gowindmill.com/resources/lists/skip-level-meeting-questions', 'gowindmill.com/resources/lists/skip-level-meeting-questions',
  '高管与隔两级下属 1:1 的 30 个 skip-level 提问，按类组织：工作优先级(5)/经理效能(5)/团队文化(5)/职业成长(5)/公司对齐(5)/收尾(5)。目标：绕过管理层收集团队健康/经理效能/文化反馈——这些通常不会自发上行。强调从非威胁性优先级问题建 rapport，再进敏感话题；发现"战略是否跨层一致传达""员工是否感到被公平对待/有归属感"。附 Gallup 数据(经理决定70%敬业度方差)增强说服力。',
  '用优先级类(1-5)开场破冰；经理效能类看模式不盯个人；收尾类("还有什么该问没问的")常产出最重要信息；会后闭环。',
  'https://gowindmill.com/resources/lists/skip-level-meeting-questions',
  '适用：② 高管越级面谈(skip-level)——标准化的 30 问清单，绕过中层听真实反馈。'))

cards.append(card('🧰', 'The Skip-Level Meeting Playbook · 工程负责人实操手册', '越级沟通', 'supervisor',
  'https://www.questworks.io/blog/skip-level-meeting-playbook', 'questworks.io/blog/skip-level-meeting-playbook',
  '面向工程负责人的 skip-level 实操手册：问题分四组——心理安全感(敢不敢异议/上次真分歧如何收)/经理效能(只校准不调查，85%员工有定期反馈更主动)/战略对齐(只2/10员工强连接文化，透明讲"为什么")/跟进协议。强调 HBR 原则：高管只说 30%，多听；5 大失败模式——吐槽会(变向中层抱怨)/后门(单人反馈未聚合匿名化毁安全)/审讯(连珠炮)；跟进协议：24h 致谢+1 项具体价值、1 周聚合成主题(不引原话)、2 周与中层经理 debrief(给主题不给引号)。',
  '严格 30% 说话时间；对任何经理相关反馈重定向到"系统/流程"；只聚合模式、绝不单人行动；两周内与中层 debrief 闭环。',
  'https://www.questworks.io/blog/skip-level-meeting-playbook',
  '适用：② 高管/工程负责人越级面谈——含心理安全感诊断+跟进协议+5 失败模式避坑。'))

cards.append(card('📋', 'Skip-Level Questionnaire · 8 套模板（含心理安全感量表）', '越级沟通', 'supervisor',
  'https://www.hypescribe.com/blog/skip-level-meeting-questionnaire', 'hypescribe.com/blog/skip-level-meeting-questionnaire',
  '8 套 skip-level 问卷模板：价值观型(把价值观变成可观察行为)/心理安全感 Skip-Level 量表(敢不敢提异议/出错后发生什么/求助是否自在/谁被早邀请进决策)/360 模型(自评+同伴+下属+越级四维拼全貌)/同伴文化与包容/职业成长/公司对齐等。强调：弱信任时先从日常工作问题入手，价值观用例子不用口号；问团队状况不针对个人；必须有升级规则(严重管理问题不临场发挥)。',
  '弱信任期用"日常工作类"问题起手，价值观经实例自然带入；心理安全感量表专治"团队变安静"；360 模型用于高管继任/发展计划。',
  'https://www.hypescribe.com/blog/skip-level-meeting-questionnaire',
  '适用：② 越级面谈问卷设计——含可量化的心理安全感量表与 360 模板。'))

cards.append(card('🔗', '跨部门协作 5 策略 · 打破谷仓效应', '跨部门融合', 'supervisor',
  'https://pilotrunapp.com/blog/cross-department-collaboration', 'pilotrunapp.com/blog/cross-department-collaboration',
  '5 个打破部门 silo 的团建策略：(1)角色互换工作坊——影子日+迷你挑战(让工程师回客户投诉信/销售读产品规格/设计师估功能工时)+反思讨论；(2)一起解真实公司问题——破冰30分混组→问题定义45分→发想60分→提案45分→认领执行30分，关键：选中的方案真执行否则员工觉"演戏"；(3)经营"弱连接"——每周随机配对午餐/技能交换/微型专案/兴趣社团，持续小动作胜一年一次大活动；(4)(5)同理心与持续机制。社会学"弱连接"理论支撑创新。',
  '用"真实公司问题工作坊"而非游戏建跨部门信任；方案必须认领真执行；用随机午餐/技能交换经营弱连接，远距更易断须刻意维护。',
  'https://pilotrunapp.com/blog/cross-department-collaboration',
  '适用：② 跨部门团队融合——用真实问题+弱连接替代拓展游戏。'))

cards.append(card('🧩', 'Align Cross-Functional Teams · 3 个实证做法', '跨部门对齐', 'supervisor',
  'https://victuspeople.com/how-to-align-cross-functional-teams-3-proven-practices-for-multinational-teams/', 'victuspeople.com/how-to-align-cross-functional-teams-3-proven-practices-for-multinational-teams',
  '跨国/跨职能团队对齐 3 法(2-3 周见效)：(1)Timeline Activity(起源故事)——成员写人生阶段词/短语连成叙事再分享，仿 Lencioni 高管用法；案例：经理自曝"曾拒升职因怕辜负团队"瞬间拉高心理安全；(2)Daily Huddles——15 分钟建立共享现实，防信息困在 silo；(3)Quarterly Themes——全员追一个 Critical Number 形成"One Team One Voice"。直击 silo 症状：客户收到矛盾信息、难谈话题拖成危机、无共同目标。',
  '先跑 Timeline Activity 建信任(让经理先示弱)；Daily Huddles 固定 15 分钟节奏；Quarterly Themes 锁定一个关键数字统一口径。',
  'https://victuspeople.com/how-to-align-cross-functional-teams-3-proven-practices-for-multinational-teams/',
  '适用：② 跨职能/跨国团队对齐——起源故事+每日站会+季度主题三连击。'))

cards.append(card('📊', 'KPI-Driven Team Building · 把协调问题变可测实验', '跨部门对齐', 'supervisor',
  'https://sandmerit.com/top-kpi-driven-team-building-ideas-for-your-group/', 'sandmerit.com/top-kpi-driven-team-building-ideas-for-your-group',
  '把团建当"技能演练"而非娱乐，每个活动绑 1-2 个 KPI 可追踪：(协作冲刺)依赖映射工作坊(可视化 handoff 瓶颈+定 SLA)/角色清晰度 mini-charter(谁决策谁执行谁复核)/决策规则(升级路径+审批阈值)；(沟通对齐)一词结果对齐(每人一词→词云暴露定义分歧→映射到 cycle time/defect rate 等 KPI)/会议卫生重置(停/缩/转异步，每会必带决策或指标)；(问题解决)约束式情景规划/根因 drill(无指责+五 why)/模式命名。原则：短结构冲刺把协调问题变可测实验。',
  '每个练习后命名并链到 KPI(如决策速度/返工环/审批时延)；根因 drill 用无指责语言+五 why；会议必带明确决策或指标否则砍掉。',
  'https://sandmerit.com/top-kpi-driven-team-building-ideas-for-your-group/',
  '适用：② 跨部门/跨职能团建——用 KPI 绑定把破冰变可量化改进实验。'))

# split by relation
sec3 = ''.join(c for c in cards if 'badge r3' in c)
sec2 = ''.join(c for c in cards if 'badge r2' in c)

# write temp file (all cards, used by gen_run_page)
with open(TMP, 'w', encoding='utf-8') as f:
    f.write(''.join(cards))
print('tmp cards:', len(cards), '| sec3:', sec3.count('<div class="hl">'), '| sec2:', sec2.count('<div class="hl">'))

# update wall
html = open(WALL, encoding='utf-8').read()

# insert sec3 cards before sec2 section (inside sec3 grid)
html = html.replace('  <div class="sec sec2">', sec3 + '  <div class="sec sec2">', 1)
# insert sec2 cards before grid close that precedes footer (last card's </div> then grid/wrap </div>)
html = html.replace('    </div>\n    </div>\n\n  <footer>', '    </div>\n' + sec2 + '    </div>\n\n  <footer>', 1)

# update tag counts
html = html.replace('<span class="tag">14 卡</span>', '<span class="tag">19 卡</span>', 1)
html = html.replace('<span class="tag">37 卡</span>', '<span class="tag">43 卡</span>', 1)

# update hero p
html = re.sub(r'<p>采集于 2026-08-10 ｜ 七轮补采 \+7（21:50）｜[^<]*</p>',
              '<p>采集于 2026-08-12 ｜ 八轮补采 +11（04:32）｜ 六维评估（含关系适配度）｜ 一手/二手标注 ｜ 历史去重 ｜ 受众关系分层（仅②上下级 / ③高管间）</p>',
              html, count=1)

open(WALL, 'w', encoding='utf-8').write(html)
print('wall updated. sec3 tag & sec2 tag updated, hero updated.')
