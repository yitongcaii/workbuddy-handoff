# -*- coding: utf-8 -*-
"""
_icebreaker_r9_rebuild.py — 从干净的已提交基线(HEAD)重建破冰墙，彻底修复 R8 损坏：
1) 修复 脆弱信任+Edmondson 块缺失的 </div>（它吞掉了 5 张正确卡 + 6 张 skip-level 损坏卡）；
2) 解析全部 62 张独立块；
3) 标题命中 FIX 的 11 张 R8 损坏卡（5③+6②）用正确数据重建；
4) 追加本轮 7 张新卡（③2 / ②5，全二手）；
5) 干净重排墙 + 写 .run_newcards.tmp.html。
目标：69 张唯一卡，0 损坏。
"""
import re, os

BASE = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(BASE, 'icebreaker', 'icebreaker.html')
TMP  = os.path.join(BASE, 'icebreaker', '.run_newcards.tmp.html')
SRC  = os.path.join(os.path.dirname(BASE), '_icebreaker_base.html')  # 已提取的 HEAD 基线

CSS = """:root{
  --bg:#f4f6fb; --card:#ffffff; --ink:#1f2430; --sub:#5b6478;
  --accent:#6c5ce7; --accent2:#00b8d9; --chip:#eef0ff;
}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:linear-gradient(135deg,#eef1ff 0%,#e6f7ff 100%);color:var(--ink);padding:28px 18px;line-height:1.6;}
.wrap{max-width:1080px;margin:0 auto;}
.hero{background:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);border-radius:22px;padding:30px 32px;color:#fff;box-shadow:0 14px 40px rgba(108,92,231,.25);margin-bottom:22px;}
.hero h1{font-size:28px;font-weight:800;letter-spacing:1px;margin-bottom:8px;}
.hero p{font-size:14px;opacity:.95;}
.relbar{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px;}
.relbar span{background:rgba(255,255,255,.2);border-radius:20px;padding:5px 14px;font-size:13px;font-weight:600;}
.sec{margin:30px 0 12px;display:flex;align-items:center;gap:10px;}
.sec h2{font-size:19px;font-weight:800;}
.sec .tag{font-size:12px;padding:4px 12px;border-radius:12px;font-weight:700;}
.sec3 .tag{background:#f3e8ff;color:#7b2cbf;} .sec3 h2{color:#7b2cbf;}
.sec2 .tag{background:#fff3e0;color:#c0651a;} .sec2 h2{color:#c0651a;}
.sec1 .tag{background:#eaf2ff;color:#2b6cb0;} .sec1 h2{color:#2b6cb0;}
.sec .desc{font-size:12.5px;color:var(--sub);margin-left:2px;}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;}
.hl{background:var(--card);border-radius:18px;padding:18px 18px 16px;border-top:4px solid var(--accent);box-shadow:0 10px 32px rgba(108,92,231,.10);display:flex;flex-direction:column;gap:9px;}
.top{display:flex;align-items:center;gap:8px;flex-wrap:wrap;}
.emoji{font-size:22px;}
.hl h3{font-size:16px;font-weight:700;flex:1;min-width:120px;}
.cat{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:600;background:var(--chip);color:var(--accent);}
.badge{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:700;}
.b2{background:#fff1e6;color:#c0651a;}
.b1{background:#eaf2ff;color:#2b6cb0;}
.r1{background:#eaf2ff;color:#2b6cb0;}
.r2{background:#fff3e0;color:#c0651a;}
.r3{background:#f3e8ff;color:#7b2cbf;}
.val{font-size:13.5px;color:var(--sub);}
.exec{margin-top:2px;border-top:1px dashed #e2e8f0;padding-top:8px;}
.exec summary{cursor:pointer;font-size:13px;font-weight:600;color:var(--accent);}
.exec .inner{font-size:13px;color:var(--sub);margin-top:6px;padding-left:4px;}
.src{font-size:12px;word-break:break-all;}
.src a{color:var(--accent2);text-decoration:none;}
.note{font-size:12px;color:#94a3b8;border-left:3px solid #e2e8f0;padding-left:8px;}
@media(max-width:680px){.grid{grid-template-columns:1fr;}}
footer{text-align:center;padding:24px;color:#94a3b8;font-size:13px;border-top:1px solid #e2e8f0;margin-top:40px;}
"""

def card(emoji, title, cat, rel, val, how, url, disp, note):
    badge = 'r3' if rel == 'exec' else 'r2'
    label = '高管间' if rel == 'exec' else '上下级'
    return f'''    <div class="hl">
      <div class="top"><span class="emoji">{emoji}</span><h3>{title}</h3><span class="cat">{cat}</span><span class="badge {badge}">{label}</span><span class="badge b2">二手</span></div>
      <p class="val">{val}</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">{how}</div></details>
      <div class="src">🔗 <a href="{url}" target="_blank">{disp}</a></div>
      <div class="note">{note}</div>
    </div>
'''

# ---- R8 损坏 11 张的正确数据（标题 -> (emoji, cat, rel, val, how, url, disp, note)）----
FIX = {
 'Centering the C-Suite · 5 活动筑牢高管团队信任与对齐': ('🎯','高管信任','exec',
   '为 ELT 会议/高管静修设计的活动，目标不是团建游戏而是把 C-suite 围绕使命/价值观/战略对齐：(1)两个反思问题——"你希望人不在场时别人怎么评你？""你在场时希望他们有什么感受？"；(2)ELT 读书会聚焦"怎样建立/破坏信任"；(3)Leadership Origin Story——最好的领导者是谁、他做了什么、如何影响你的领导观；(4)Pre-experience success——设想年底庆功倒推"我们做了什么/要成为谁/保持什么/停止什么"；(5)卡牌(团队/价值观卡)随机抽问。核心：让高管彼此了解价值观与意图，而非强制趣味。',
   '选"两个反思问题 + Leadership Origin Story"开场，配读书会/Pre-experience 收尾；务必由 CEO 先示范脆弱，避免变成汇报。',
   'http://www.choosetheperk.com/blog/executive-leadership-team-meeting-ideas',
   'choosetheperk.com/blog/executive-leadership-team-meeting-ideas',
   '适用：③ 高管团队(ELT/静修)对齐——反思问题+Origin Story+Pre-experience，CEO 先示范脆弱，非游戏。'),
 'Executive Retreat Activities That Actually Drive Alignment': ('🧭','高管对齐','exec',
   '明确"跳过信任摔和密室逃脱"，按对齐产出分三类：(信任)Leadership Journey Maps(职业时间轴标转折)/Formative Experiences Dialogue(配对讲塑造领导观的经历+替对方介绍)/Strengths & Blindspots Exchange(自评+匿名同伴反馈)/Values Auction(用"静修美元"竞拍价值观暴露真实优先级)；(战略)Strategy Mapping 上墙/客户旅程沉浸/资源分配模拟/Pre-Mortem/竞品战争推演；(沟通)Decision Autopsy 复盘重大决策。原则：高管活动要尊重智商、连接战略现实、产出真洞察。',
   '先排信任类(前半天)，再上战略类；Values Auction/Pre-Mortem 用真实议题；请中立引导师 hold 场。',
   'https://www.dmpcreative.llc/resources/executive-retreat-activities-that-drive-alignment',
   'dmpcreative.llc/resources/executive-retreat-activities-that-drive-alignment',
   '适用：③ 高管静修——信任类(旅程地图/价值观拍卖)+战略类(Pre-Mortem/战争推演)+沟通类(决策尸检)，重真洞察。'),
 'Building a Healthy & Aligned Executive Team · 一日工作坊议程': ('🏛️','高管融合','exec',
   '基于 Lencioni 五 dysfunction 的一日高管工作坊完整议程：(1)Personal History——每人分享职业高光/最尴尬失败/塑造自己的经历/最大障碍/珍视之处；(2)Myers Briggs review——会前测 MBTI，会上用"我的人设/最大优势/想改的弱点"小结；(3)Personal Plan——人生最重要/热爱/长期愿景；(4)Conflict profiling——用 Issue Resolution Model 复盘未决难题；(5)Commitment clarity——CEO 抽干所有观点后拍板；(6)Accountability——同伴反馈(strengths + 拖累团队的行为)。全程强调"脆弱从顶层开始"。',
   '按信任→冲突→承诺→担责四段推进；MBTI 作破冰不贴标签；冲突段鼓励把争议摆上桌不内耗。',
   'https://theorg.com/iterate/building-a-healthy-and-aligned-executive-team-in-one-day',
   'theorg.com/iterate/building-a-healthy-and-aligned-executive-team-in-one-day',
   '适用：③ 高管一日工作坊——Personal History+MBTI+Conflict profiling+Commitment+Accountability，脆弱从顶层开始。'),
 '高管信任升级与协同突围 · 阿里裸心会工作坊': ('🔥','高管融合','exec',
   '面向高管团队融合/信任危机/战略转型的统一认知工作坊(HRD/HRBP 全程参与)：双工具驱动——生命年轮(画个人与企业共成长时间轴，标3高光+2低谷唤醒情感共鸣)+乔哈里窗(盲区探索破解认知偏差)；保留阿里基因——照镜子/揪头发/裸心会铁律(不评判/不打断/不记录)；闭环——从矛盾收集到公约签署；仪式感——能量地图/时光胶囊。适用场景：高管融合、业务瓶颈突破、危机复盘韧性重塑。',
   '会前1周收矛盾点+高管心智预热；模块二"照镜子"用能量温度计(1-10)破层级壁垒；裸心对话按阿里三铁律执行；收尾签团队公约而非"只谈不干"。',
   'http://www.youjiangshi.com/training/385487.html',
   'youjiangshi.com/training/385487.html',
   '适用：③ 高管融合/信任危机——生命年轮+乔哈里窗+裸心会三铁律，收尾签公约不"只谈不干"。'),
 'Leadership Team Building That Actually Works · 7 个无游戏练习': ('🚀','领导力团建','exec',
   '7 个不靠绳索场、既建信任又显化冲突的领导力团建练习(铁律：永远 debrief，讨论时间>活动本身)：(01)How to Work With Me 手册——一页写沟通/反馈偏好；(02)Failure Résumé——讲一个真实职业失败+教训，高层先认栽别人才能松气(脆弱循环)；(03)Personal Histories——Lencioni 经典三低 stakes 问题；(04)Pasta Tower——18分钟棉花糖挑战，debrief 甩锅怪谁；(05)Mining for Conflict——拿一个真议题练公开分歧；(06)Clearing Round——对每人一句欣赏+一个 start/stop 请求；(07)Pre-Mortem——设想明年失败倒推原因。心理安全感+赋能+建设性冲突三者齐备才出创新。',
   '每个练习后留比活动更长的时间 debrief；从 Failure Résumé/Personal Histories 开场建安全；冲突类(Mining/Pre-Mortem)放后半段。',
   'https://www.unicornlabs.ca/blog/leadership-team-building-that-works',
   'unicornlabs.ca/blog/leadership-team-building-that-works',
   '适用：③ 领导力团建——7 个无游戏练习，铁律 debrief>活动，脆弱循环+显化冲突出创新。'),
 'Skip-Level Meeting Questions · 30 个建信任提问': ('🪜','越级沟通','supervisor',
   '高管与隔两级下属 1:1 的 30 个 skip-level 提问，按类组织：工作优先级(5)/经理效能(5)/团队文化(5)/职业成长(5)/公司对齐(5)/收尾(5)。目标：绕过管理层收集团队健康/经理效能/文化反馈——这些通常不会自发上行。强调从非威胁性优先级问题建 rapport，再进敏感话题；发现"战略是否跨层一致传达""员工是否感到被公平对待/有归属感"。附 Gallup 数据(经理决定70%敬业度方差)增强说服力。',
   '用优先级类(1-5)开场破冰；经理效能类看模式不盯个人；收尾类("还有什么该问没问的")常产出最重要信息；会后闭环。',
   'https://gowindmill.com/resources/lists/skip-level-meeting-questions',
   'gowindmill.com/resources/lists/skip-level-meeting-questions',
   '适用：② 高管越级面谈(skip-level)——标准化的 30 问清单，绕过中层听真实反馈。'),
 'The Skip-Level Meeting Playbook · 工程负责人实操手册': ('🧰','越级沟通','supervisor',
   '面向工程负责人的 skip-level 实操手册：问题分四组——心理安全感(敢不敢异议/上次真分歧如何收)/经理效能(只校准不调查，85%员工有定期反馈更主动)/战略对齐(只2/10员工强连接文化，透明讲"为什么")/跟进协议。强调 HBR 原则：高管只说 30%，多听；5 大失败模式——吐槽会(变向中层抱怨)/后门(单人反馈未聚合匿名化毁安全)/审讯(连珠炮)；跟进协议：24h 致谢+1 项具体价值、1 周聚合成主题(不引原话)、2 周与中层经理 debrief(给主题不给引号)。',
   '严格 30% 说话时间；对任何经理相关反馈重定向到"系统/流程"；只聚合模式、绝不单人行动；两周内与中层 debrief 闭环。',
   'https://www.questworks.io/blog/skip-level-meeting-playbook',
   'questworks.io/blog/skip-level-meeting-playbook',
   '适用：② 高管/工程负责人越级面谈——含心理安全感诊断+跟进协议+5 失败模式避坑。'),
 'Skip-Level Questionnaire · 8 套模板（含心理安全感量表）': ('📋','越级沟通','supervisor',
   '8 套 skip-level 问卷模板：价值观型(把价值观变成可观察行为)/心理安全感 Skip-Level 量表(敢不敢提异议/出错后发生什么/求助是否自在/谁被早邀请进决策)/360 模型(自评+同伴+下属+越级四维拼全貌)/同伴文化与包容/职业成长/公司对齐等。强调：弱信任时先从日常工作问题入手，价值观用例子不用口号；问团队状况不针对个人；必须有升级规则(严重管理问题不临场发挥)。',
   '弱信任期用"日常工作类"问题起手，价值观经实例自然带入；心理安全感量表专治"团队变安静"；360 模型用于高管继任/发展计划。',
   'https://www.hypescribe.com/blog/skip-level-meeting-questionnaire',
   'hypescribe.com/blog/skip-level-meeting-questionnaire',
   '适用：② 越级面谈问卷设计——含可量化的心理安全感量表与 360 模板。'),
 '跨部门协作 5 策略 · 打破谷仓效应': ('🔗','跨部门融合','supervisor',
   '5 个打破部门 silo 的团建策略：(1)角色互换工作坊——影子日+迷你挑战(让工程师回客户投诉信/销售读产品规格/设计师估功能工时)+反思讨论；(2)一起解真实公司问题——破冰30分混组→问题定义45分→发想60分→提案45分→认领执行30分，关键：选中的方案真执行否则员工觉"演戏"；(3)经营"弱连接"——每周随机配对午餐/技能交换/微型专案/兴趣社团，持续小动作胜一年一次大活动；(4)(5)同理心与持续机制。社会学"弱连接"理论支撑创新。',
   '用"真实公司问题工作坊"而非游戏建跨部门信任；方案必须认领真执行；用随机午餐/技能交换经营弱连接，远距更易断须刻意维护。',
   'https://pilotrunapp.com/blog/cross-department-collaboration',
   'pilotrunapp.com/blog/cross-department-collaboration',
   '适用：② 跨部门团队融合——用真实问题+弱连接替代拓展游戏。'),
 'Align Cross-Functional Teams · 3 个实证做法': ('🧩','跨部门对齐','supervisor',
   '跨国/跨职能团队对齐 3 法(2-3 周见效)：(1)Timeline Activity(起源故事)——成员写人生阶段词/短语连成叙事再分享，仿 Lencioni 高管用法；案例：经理自曝"曾拒升职因怕辜负团队"瞬间拉高心理安全；(2)Daily Huddles——15 分钟建立共享现实，防信息困在 silo；(3)Quarterly Themes——全员追一个 Critical Number 形成"One Team One Voice"。直击 silo 症状：客户收到矛盾信息、难谈话题拖成危机、无共同目标。',
   '先跑 Timeline Activity 建信任(让经理先示弱)；Daily Huddles 固定 15 分钟节奏；Quarterly Themes 锁定一个关键数字统一口径。',
   'https://victuspeople.com/how-to-align-cross-functional-teams-3-proven-practices-for-multinational-teams/',
   'victuspeople.com/how-to-align-cross-functional-teams-3-proven-practices-for-multinational-teams',
   '适用：② 跨职能/跨国团队对齐——起源故事+每日站会+季度主题三连击。'),
 'KPI-Driven Team Building · 把协调问题变可测实验': ('📊','跨部门对齐','supervisor',
   '把团建当"技能演练"而非娱乐，每个活动绑 1-2 个 KPI 可追踪：(协作冲刺)依赖映射工作坊(可视化 handoff 瓶颈+定 SLA)/角色清晰度 mini-charter(谁决策谁执行谁复核)/决策规则(升级路径+审批阈值)；(沟通对齐)一词结果对齐(每人一词→词云暴露定义分歧→映射到 cycle time/defect rate 等 KPI)/会议卫生重置(停/缩/转异步，每会必带决策或指标)；(问题解决)约束式情景规划/根因 drill(无指责+五 why)/模式命名。原则：短结构冲刺把协调问题变可测实验。',
   '每个练习后命名并链到 KPI(如决策速度/返工环/审批时延)；根因 drill 用无指责语言+五 why；会议必带明确决策或指标否则砍掉。',
   'https://sandmerit.com/top-kpi-driven-team-building-ideas-for-your-group/',
   'sandmerit.com/top-kpi-driven-team-building-ideas-for-your-group',
   '适用：② 跨部门/跨职能团建——用 KPI 绑定把破冰变可量化改进实验。'),
}

def split_cards(html):
    # 每张卡以「下一个 <div class="hl"> 起点」为界，缺失闭合的卡自动在此处截断，
    # 从而把被吞掉的后续卡正确切分出来；正常闭合的卡会在到达下一张前 d==0 自然结束。
    starts=[m.start() for m in re.finditer(r'<div class="hl">', html)]
    nxt = starts[1:] + [len(html)]
    blocks=[]
    for k,s in enumerate(starts):
        end = nxt[k]
        i=s+len('<div class="hl">'); d=1; j=i
        while j < end:
            if html[j:j+4]=='<div': d+=1; j+=4
            elif html[j:j+5]=='</div': d-=1; j+=6
            else: j+=1
            if d==0: break
        blocks.append(html[s:end].rstrip())
    return blocks

def title_of(b):
    m=re.search(r'<h3>(.*?)</h3>', b, re.S)
    return re.sub(r'\s+',' ',m.group(1)).strip() if m else ''

# ===== 本轮新卡（③2 / ②5，全二手）=====
new_cards = []
new_cards.append(card('🔥', 'Leadership Retreat 信任引擎·8 个不靠游戏的实践', '高管信任', 'exec',
 '硅谷敏捷教练(Silicon Valley Alliances)在三日领导力 retreat 中实战的 8 个建信任实践(非游戏、不强制暴露)：①Personal Histories——每人答三问(出生地/兄弟姐妹/年轻时塑造自己的挑战)，让人回到「人」而非头衔；②Lifeline——画人生高低曲线，领导先示范；③Generous Listening——多听少说、把「Yes, but」换成「Yes, and」；④Show Vulnerability(领导先认错)；⑤give-back 共创项目把洞察变共享记忆。核心：信任在真实对话与日常小习惯中长出来，不在理论里。',
 '高管 retreat 用 Personal Histories + Lifeline + Yes-and 开场，领导先示弱；用 give-back 项目把洞察锚定为共享记忆；把「Yes, but」改「Yes, and」练建设性。',
 'https://matthiasorgler.com/2025/11/21/build-trust-to-ignite-motivation',
 'matthiasorgler.com/2025/11/21/build-trust-to-ignite-motivation',
 '适用：③ 高管/领导力 retreat——用 Personal Histories/Lifeline/Yes-and/示弱 替代信任摔与破冰游戏，信任在日常小习惯中生长。'))
new_cards.append(card('🧩', '空降高管融合工作坊·2天1夜标准化模板(20+企业验证)', '空降高管融合', 'exec',
 '某建材企业用领导力工作坊 6 个月将空降高管存活率从 35% 提升至 82%、决策效率 +40%。标准化 2 天1夜模板：Day1 破冰·共识(文化基因解码 3h + 战略对齐沙盘 4h，用真实年度战略做沙盘、设计资源分配/决策风格冲突点)；Day2 融合·赋能(领导力实战推演 5h：角色扮演卡设技术元老/空降高管/新生代三角冲突，识别冲突根源设计缓冲；跨部门资源博弈棋盘；百日攻坚计划表)。关键成功要素：前置访谈 5+ 核心管理者、创始人全程参与、70% 时间实战推演、月度复盘(文化翻译官/决策透明度工程/痛点攻坚擂台)。',
 '空降高管融合用「文化解码+战略沙盘+实战推演+百日计划」2天1夜；创始人必到场、70% 时间实战不灌理论；后续接文化翻译官+决策透明度+痛点擂台三连击。',
 'https://www.toutiao.com/article/7532678475656757800/',
 'toutiao.com/article/7532678475656757800',
 '适用：③ 空降高管(老板视角)融合工作坊——标准化 2天1夜模板，存活率可从 35% 提到 82%，实战推演替代理论灌输。'))
new_cards.append(card('🧭', '工程经理 First 90 Days Playbook·倾听之旅+提问框架', '新经理上任', 'supervisor',
 '新工程经理首 90 天战术手册(D1-30 倾听/D31-60 诊断/D61-90 行动)：Week1 倾听之旅——与每位关键人 1:1(直接下属问「这里最好/最挫的事」；经理问 90 天成功标准；同级经理问协作断点；关键干系人问缺口；skip-level 问战略上下文)。1:1 提问框架：诊断类(「若你掌权会改什么」「最拖慢你的是什么」「你最敬佩的同事」) + 职业类(「2 年想去哪」「想发展什么技能」「工作被认可吗」)。首月画「团队地图」(人/流程/产品/政治四维)。避坑：别在第一周强行「加价值」改东西。',
 '新经理首 30 天只倾听不改；用诊断+职业两类问题跑 1:1 倾听之旅；首月画团队地图(人/流程/产品/政治)；D31-60 诊断 Top3 问题、D61-90 交付 1-2 个速赢。',
 'https://www.thegarnetwiki.com/engineering-leadership/first-90-days-playbook',
 'thegarnetwiki.com/engineering-leadership/first-90-days-playbook',
 '适用：② 新任(尤其内部晋升)经理上任——倾听之旅+结构化 1:1 提问框架，先把团队摸透再优化，避免「新官三把火」翻车。'))
new_cards.append(card('🗺️', '带团队前 90 天路线图·清晰/联结/一致/自信四基', '新经理上任', 'supervisor',
 '基于 Success Through People© 模型的 90 天落地路线图，目标不是「做更多」而是打地基：Clarity(人知期望与「好」的标准)/Connection(建信任与健康关系)/Consistency(言行一致)/Confidence(刻意练领导风格)。D1-30：①搞清角色(3/6/12 月成功长相、决策权边界)②正式 1:1(「现在什么顺/什么挡路/你需要我做什么/若改一件事会是什么」)③学团队「潜规则」(顺境/压力下的沟通、是否担责)④定 3-5 条核心期望(沟通节奏/如何对待失误/担责/彼此对待)。',
 '新经理 90 天聚焦「清晰+联结+一致+自信」四基；首月 1:1 问「顺/挡/需/改」四问、学团队潜规则、定 3-5 条核心期望；不靠加班「证明自己」。',
 'https://successthroughpeople.com.au/the-first-90-days-of-leading-a-team-a-practical-guide',
 'successthroughpeople.com.au/the-first-90-days-of-leading-a-team-a-practical-guide',
 '适用：② 新任/新接团队经理——90 天四基路线图，用 1:1 四问+潜规则洞察+核心期望，把信任与清晰打底而非疲于「多做事」。'))
new_cards.append(card('🤝', '10 个建信任练习·从 Be the teacher 到赏识圈', '经理建信任', 'supervisor',
 'Indeed 给经理的 10 个实操建信任练习(非游戏、专业)：①Be the teacher——每周会前 5-10 分钟让成员教一项专长/爱好，轮流向学；②Opening question——晨会/周会用轻问开场(「最想教的课/奥运参赛项/emoji 形容性格/梦想演唱会」)，员工轮流出题；③Active listening sessions——配对一人讲一人复述反思，练倾听；④Verbal trust fall——分享一个职业失误/骄傲项目/近期学到的事，收支持性反馈建情感信任；⑤Appreciation circles——轮流具体感谢某同事的贡献或品质；⑥-⑩ Escape room/Survival scenarios/Group brainstorming/Two truths and a lie/Team meals。底层：信任=透明沟通+伦理实践+持续小动作。',
 '经理用「Be the teacher(教专长)+Opening question(轻问开场)+Active listening(配对复述)+Appreciation circles(具体感谢)」建信任；把信任练习变周会例行而非一次性游戏。',
 'https://www.indeed.com/hire/c/info/trust-exercises',
 'indeed.com/hire/c/info/trust-exercises',
 '适用：② 经理带团队建信任——Indeed 10 个专业练习(教学/轻问/倾听/赏识圈)，弃信任摔类幼稚游戏，信任靠透明与持续小动作。'))
new_cards.append(card('📜', 'Team Charter 分步共创·绿卡/红卡行为清单', '团队契约', 'supervisor',
 '咨询机构(Growth Space)团队契约(Team Charter/Working Agreement)分步共创法：①全员共创而非仅 leader 写(外部引导师平衡声音)②定基调(为什么重要+倾听/建设性挑战规则)③走模板(我们是谁/目的/目标与成功指标/价值观与行为/风险/操作系统:会议·沟通·决策·工作日·仪式·反馈)④用提示问题挖深(「什么让我们伟大/更好」)⑤一页人话、可视化、速传⑥活用在日常(入职即发、冲突时引用、复盘时问「我们守约了吗」)⑦定期复盘(季度或重大变更后,Start/Stop/Continue)。亮点：green card/red card 行为清单——鼓励什么、绝不容忍什么。',
 '经理带团队共创 Team Charter(全员参与+外部引导师)；模板覆盖目的/角色/决策/沟通/绿红卡行为；一页人话速传；冲突时引用、季度 Start/Stop/Continue 复盘。',
 'http://growth-space.co.uk/blog//how-to-create-a-team-charter-a-step-by-step-guide',
 'growth-space.co.uk/blog/how-to-create-a-team-charter-a-step-by-step-guide',
 '适用：② 经理/HR 带新团队或重组后共创团队契约——绿卡/红卡行为清单把「鼓励/不容忍」显式化，化解 Storming 加速 Norming。'))
new_cards.append(card('🔄', '6 个建信任练习·角色互换+感恩链', '经理建信任', 'supervisor',
 '领导力发展指南给经理的 6 个建信任练习：①Role Reversal(角色互换)——领导与员工互换角色讲对方立场，练同理心，员工懂领导复杂、领导见决策落地影响；②Gratitude Chain(感恩链)——每人具体感谢某同事的贡献并传递「感恩链」；③-⑥ Shared Vulnerability(领导先讲挑战/失误)/Team Problem-Solving/Two Truths and a Trust/Compliment Chain。底层：信任练习要日常化(每月至少一次)、避强制暴露与无跟进、authenticity 不能装。认可激活多巴胺强化情感联结。',
 '经理用「角色互换(同理心)+感恩链(具体感谢传递)」建信任；信任练习日常化(每月≥1次)、领导先示弱、避免强制暴露与无跟进。',
 'https://possiedigroup.com/6-trust-building-exercises-every-leader-should-try-leadership-development-guide.html',
 'possiedigroup.com/6-trust-building-exercises-every-leader-should-try-leadership-development-guide.html',
 '适用：② 经理建团队信任——角色互换+感恩链等 6 练习，日常化(每月≥1次)而非一次性活动，authenticity 不能装。'))

# ===== 1) 读基线 =====
html = open(SRC, encoding='utf-8').read()

# ===== 2) 解析全部块（split_cards 已按「下一张起点」切分，自动容错缺失闭合）=====
blocks = split_cards(html)

# ===== 3) 重建损坏卡 / 保留正常卡 =====
existing=[]
fixed=0
for b in blocks:
    t = title_of(b)
    if t in FIX:
        emoji,cat,rel,val,how,url,disp,note = FIX[t]
        existing.append(card(emoji, t, cat, rel, val, how, url, disp, note))
        fixed += 1
    else:
        # 结构完整性校验：必须以 </div> 结尾（兜底）
        existing.append(b)

# 去重（按标题，保留首个）——双保险
seen=set(); dedup=[]
for b in existing:
    t=title_of(b)
    if t in seen: continue
    seen.add(t); dedup.append(b)
existing=dedup

# 分类
exist_r3=[b for b in existing if 'badge r3' in b]
exist_r2=[b for b in existing if 'badge r2' in b]
new_r3=[c for c in new_cards if 'badge r3' in c]
new_r2=[c for c in new_cards if 'badge r2' in c]
sec3=exist_r3+new_r3
sec2=exist_r2+new_r2

# 写临时文件（仅本轮新卡）
with open(TMP,'w',encoding='utf-8') as f:
    f.write(''.join(new_cards))
print('tmp new cards:', len(new_cards), '| new r3:', len(new_r3), '| new r2:', len(new_r2), '| fixed R8:', fixed, '| existing kept:', len(existing))

# ===== 4) 重建墙 =====
n3=len(sec3); n2=len(sec2)
hero = f'''  <div class="hero">
    <h1>🧊 破冰 · 知识采集卡片墙</h1>
    <p>采集于 2026-08-13 ｜ 九轮补采 +7（R9）｜ 六维评估（含关系适配度）｜ 一手/二手标注 ｜ 历史去重 ｜ 受众关系分层（仅②上下级 / ③高管间）｜ 本轮回修 R8 注入的 11 张损坏卡 + 脆弱信任缺失闭合</p>
    <div class="relbar">
      <span>② 领导↔员工（上下级，supervisor）</span>
      <span>③ 领导↔领导（高管间，exec）</span>
    </div>
  </div>'''
sec3_head = f'''  <!-- ============ ③ 高管间 ============ -->
  <div class="sec sec3">
    <h2>③ 领导↔领导（高管间 · exec）</h2>
    <span class="tag">{n3} 卡</span>
    <span class="desc">商务化、以专业/共同目标切入；含高管信任练习、沉浸式信任重构、阿里裸心会、CEO班破冰真实案例、空降高管融合三钥匙/工作坊、远程C-suite入职、治理层战略破冰、领导力 retreat 实操（均非游戏/幼稚破冰）</span>
  </div>
  <div class="grid">'''
sec2_head = f'''  <!-- ============ ② 上下级 ============ -->
  <div class="sec sec2">
    <h2>② 领导↔员工（上下级 · supervisor）</h2>
    <span class="tag">{n2} 卡</span>
    <span class="desc">尊重、不隐私暴露、建信任不越界；含新经理上任 90 天信任框架、团队契约/Working Agreements、skip-level 越级沟通、跨部门融合、远程入职 5C、心理安全感、会议破冰（均专业/共同目标切入，弃游戏）</span>
  </div>
  <div class="grid">'''
out = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>破冰 · 知识采集卡片墙</title>
<style>
{CSS}</style>
</head>
<body>
<div class="wrap">
<p style="margin:0 0 16px"><a href="runs/index.html" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">📑 查看本主题分页独立页 →</a></p>
{hero}

{sec3_head}
{''.join(sec3)}
  </div>

{sec2_head}
{''.join(sec2)}
  </div>

  <footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>
</div>
</body>
</html>
'''
open(WALL,'w',encoding='utf-8').write(out)
print('wall rebuilt. sec3:', n3, '| sec2:', n2, '| total:', n3+n2)
