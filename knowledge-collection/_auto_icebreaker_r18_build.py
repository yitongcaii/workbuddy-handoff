# -*- coding: utf-8 -*-
"""破冰 r18 构建：把 12 张新卡（6③+6②）注入 icebreaker.html 累计墙，并写 .run_newcards.tmp.html。"""
import os, io

BASE = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(BASE, 'icebreaker', 'icebreaker.html')
TMP  = os.path.join(BASE, 'icebreaker', '.run_newcards.tmp.html')

# ---------- 12 张新卡（墙 CSS 格式，与既有 <div class="hl"> 一致）----------
cards = []

# ===== ③ 高管间 (exec) 6 张 =====
cards.append('''  <div class="hl">
      <div class="top"><span class="emoji">🤝</span><h3>新领导同化 NLA 流程·HR/OD 引导的团队对齐</h3><span class="cat">新领导融入</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
      <p class="val">Institute of OD 的 New Leader Assimilation（NLA）是加速新领导融入、降低 18 个月内失败率的结构化流程。四步：①准备——HR/OD 先与新领导 1:1 了解风格与顾虑；②团队单独会议（领导不在场）——用结构化问题收集「团队优势/对未来的担忧/需要新领导提供什么/我们的协作方式」，保密汇总；③反馈给领导——教练式对话呈现团队输入，领导反思并准备建设性回应；④联合会议——领导回应反馈、澄清意图、共同制定共享协议与行动项；⑤数周后跟进复盘。核心价值：把「彼此期望」摆到台面，信任与对齐从第一天建立，而非靠新领导自行摸索。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">NLA 由 HR/OD 中立引导；先做无领导的团队单独会议收真实顾虑→教练式反馈给领导→联合会对齐+共享协议；数周跟进防回落。</div></details>
      <div class="src">🔗 <a href="https://instituteod.com/the-importance-of-new-leader-assimilation-and-how-it-works/3/" target="_blank">instituteod.com/.../new-leader-assimilation</a></div>
      <div class="note">适用：③ 空降/新任领导（尤其高管）融入团队——NLA 结构化流程替代「自行摸索」，降低早期失败率。</div>
    </div>''')

cards.append('''  <div class="hl">
      <div class="top"><span class="emoji">🗺️</span><h3>领导力入职 30-60-90 框架·听先于领导</h3><span class="cat">新领导入职</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
      <p class="val">Gallery HR 的领导力入职框架强调「标准员工入职 ≠ 领导入职」：领导要对接战略优先级、建立可信度、摸清表层之下的文化与非正式权力结构。四阶段：会前（技术/文档/干系人简报就绪，起草 30-60-90 计划）；D1-30 听先于领导（与所有直属 1:1、跨职能会议、观察文化，周度与上级对齐）；D30-60 确立方向与早期速赢（沟通机制常态化、设定绩效目标）；D60-90 战略贡献（参与战略规划、完成 90 天复盘、长期发展计划）。引用 HBR：被留任自行摸索的领导最终也能搞懂，但组织付出士气/决策延误的代价。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">领导入职分「会前→听(D1-30)→定向(D30-60)→贡献(D60-90)」四段；前 30 天只听不急着改；会前就备好 30-60-90 计划与干系人简报。</div></details>
      <div class="src">🔗 <a href="https://galleryhr.com/blogs/hr-best-practices-blog/successfully-onboarding-new-leaders-best-practices-leadership-transition" target="_blank">galleryhr.com/.../onboarding-new-leaders</a></div>
      <div class="note">适用：③ 新任/空降领导 90 天融入——听先于领导，避免 premature action 反噬信任。</div>
    </div>''')

cards.append('''  <div class="hl">
      <div class="top"><span class="emoji">🎯</span><h3>高管入职 90 天·三阶段建信任不破势</h3><span class="cat">高管入职</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
      <p class="val">Next One Staffing 的高管入职策略：近 40% 新任高管 18 个月内未达预期，根因是「缺乏有意的入职」而非能力。三阶段：①听与学（D1-30）——与直属/平级/关键干系人 1:1、审现有目标与数据、识别显性与隐性文化规范、多问少给方案，建立心理安全感；②对齐与沟通（D31-60）——透明分享初步观察与优先级、与团队共创短期目标（非下令）、建立沟通节奏（会议/更新/反馈环）、用 1-2 个可见速赢印证价值而不颠覆系统、结盟非正式意见领袖；③领导与加速（D61-90）——向干系人做 90 天复盘、在已有认同上推更大举措、固化团队结构。常见坑：第一周就大改（显不信任）、低估非正式权力、忽略向上关系管理、跳过文化尽调。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">高管入职三阶段「听学→对齐沟通→领导加速」；前 30 天建立心理安全；D31-60 用可见速赢印证而非颠覆；必做向上关系管理与文化尽调。</div></details>
      <div class="src">🔗 <a href="https://www.nextonestaffing.com/blogs/executive-onboarding-strategy/" target="_blank">nextonestaffing.com/.../executive-onboarding-strategy</a></div>
      <div class="note">适用：③ C-suite/VP 新任入职——三阶段建信任不破势，避开「第一周大改」等四类坑。</div>
    </div>''')

cards.append('''  <div class="hl">
      <div class="top"><span class="emoji">🏛️</span><h3>高管退修会 2.0·五步法+团队宪章（新 CEO 百天）</h3><span class="cat">高管退修设计</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
      <p class="val">Odgers Berndtson（高管寻聘权威）的 Executive Retreats 2.0：传统退修会常沦为后勤或表层战略，高影响力退修会从「集体领导力潜力」出发。五步：①组织目的——把董事会/外部干系人视角翻译成共享领导议程；②团队目的——共创团队宪章、工作原则、角色清晰度（新 CEO 尤关键）；③团队角色与问责——欣赏式探询 surfacing 隐性张力、建立挑战与建设性冲突的规范；④干系人对齐——映射客户/伙伴/内部职能关系，明确各自 champion；⑤团队学习与绩效——把洞察转行动、承诺发展路径。新 CEO 前 100 天是建信任定节奏的关键窗口。强调会前诊断（访谈/调研/pulse）再定议程，否则易窄化为「为董事会备 plan」。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">高影响力高管退修会五步「组织目的→团队目的(宪章)→角色问责→干系人对齐→学习绩效」；会前诊断定议程；新 CEO 前 100 天借退修会定调。</div></details>
      <div class="src">🔗 <a href="https://www.odgersberndtson.com/en-us/insights/executive-retreats-20-how-ceos-can-achieve-more-when-uniting-teams/" target="_blank">odgersberndtson.com/.../executive-retreats-2.0</a></div>
      <div class="note">适用：③ 高管退修会设计（尤其新 CEO 百天）——五步法+团队宪章，避免退修会只出战术 plan。</div>
    </div>''')

cards.append('''  <div class="hl">
      <div class="top"><span class="emoji">🔁</span><h3>高管 Offsite 规划·季度节奏+决策导向</h3><span class="cat">高管Offsite规划</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
      <p class="val">Metavent 的高管 offsite 规划观：offsite 不是「昂贵团建」，而是为更好思考/决策/更健康领导团队创造条件的「工作场」。成本不在花费，而在不做的代价——错位拖延、决策停滞、领导各自为战。核心做法：①议程围绕「房间里必须做出的几个决策」设计（少场次、长块、清晰产出），而非幻灯片汇报；②季度节奏最佳——战略不再一年一定，Q1 定方向/Q2 评估调整/Q3 重校/Q4 复盘规划，一致性才不会立刻漂移；③环境服务目标（近便则省旅费保精力，远则助跳出运营心智）；④领导健康也是产出——offsite 重建「并非独自扛」的归属感与信任。后勤须隐形，注意力留在对话。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">高管 offsite 议程锚定「必须做出的决策」而非汇报；采用季度节奏防对齐漂移；把领导归属感/信任当作隐性产出；后勤隐形。</div></details>
      <div class="src">🔗 <a href="https://www.metavent.io/blog/executive-offsite-planning-that-actually-drives-decisions-in-changing-times" target="_blank">metavent.io/.../executive-offsite-planning</a></div>
      <div class="note">适用：③ 高管 Offsite 规划——决策导向+季度节奏，把「不做的代价」显性化。</div>
    </div>''')

cards.append('''  <div class="hl">
      <div class="top"><span class="emoji">⛰️</span><h3>高管 Offsite·四类挑战+3天结构</h3><span class="cat">高管Offsite结构</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
      <p class="val">ElliottRector 的高管 offsite 定位：面向扩张/接班/不确定性/战略漂移等拐点，问题很少是智力或努力，而是「对齐」。四大典型挑战：①对齐与战略一致性（优先级与权衡、隐性张力、重建决策架构）；②高压下的领导（高风险下用框架替代反应）；③转型与转折点（接班/并购/快速变化，命名结束、整合不确定、重建共享节奏）；④凝聚力与执行（把各自为战的高管变系统）。3 天结构：D1 战略重对齐（澄清方向、显性张力、共享理解）；D2 领导凝聚力与判断（关系信任、决策架构、瓶颈）；D3 整合与承诺（所有权/排序/可度量下一步）。重视会前诊断（访谈+评估）与离场后整合跟进，让对齐在体验外持续。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">高管 offsite 围绕四类拐点挑战设计；3 天「重对齐→凝聚力/判断→整合承诺」；必做会前诊断+离场后整合，否则对齐不持久。</div></details>
      <div class="src">🔗 <a href="https://www.elliottrector.com/offsites" target="_blank">elliottrector.com/offsites</a></div>
      <div class="note">适用：③ 高管 Offsite 结构——四类领导力挑战映射+3 天递进，拐点期领导团队对齐。</div>
    </div>''')

# ===== ② 上下级 (supervisor) 6 张 =====
cards.append('''  <div class="hl">
      <div class="top"><span class="emoji">📜</span><h3>团队宪章 Team Charter·共创北极星（目的/角色/决策/冲突）</h3><span class="cat">团队宪章</span><span class="badge r2">上下级</span><span class="badge b1">一手</span></div>
      <p class="val">Miro 官方指南：团队宪章是定义团队目的、目标、角色与协作协议的「活文档」，尤其适合远程/分布式/跨时区团队对齐。五大要素：团队目标、角色职责、沟通方式、决策机制、冲突解决。共创五步：①context——谁领导/干系人期待/每人带来什么；②愿景与目标——成功长什么样、里程碑映射使命；③角色职责——谁为谁做什么、检查平衡；④让全员签署承诺（打印签名象征 commitment）；⑤定期回顾（人进退出，宪章随组织生长）。关键：自上而下由管理层起草的宪章无效，必须人人贡献才能 buy-in。远程团队尤需把 norms 写下来。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">团队宪章五要素（目标/角色/沟通/决策/冲突）；共创五步且全员签署；远程/分布式团队必做，定期回顾成「活文档」。</div></details>
      <div class="src">🔗 <a href="https://www.miro.com/organizational-chart/what-is-a-team-charter/" target="_blank">miro.com/.../what-is-a-team-charter</a></div>
      <div class="note">适用：② 新团队/跨地团队组建——用团队宪章把隐性规则显性化，替代「靠默契」（Miro 官方文档·一手）。</div>
    </div>''')

cards.append('''  <div class="hl">
      <div class="top"><span class="emoji">🧱</span><h3>团队宪章分步指南·中立引导+绿卡/红卡行为</h3><span class="cat">团队宪章</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">Growth Space 的团队宪章实操指南：宪章（或称 team agreement / ways of working）是把「目的/角色/行为/协作方式」显式的简单工具，提升信任、对齐与绩效。七步：①让全员（非仅领导）参与共创，必要时请外部中立引导师平衡声音、surface 假设；②定调——解释为何、建 ground rules（积极倾听/建设性挑战）；③走模板——我们是谁/目的/目标与度量/价值观行为（绿卡鼓励·红卡零容忍）/风险挑战/操作系统（会议·沟通·决策·工作节奏·反馈）；④用提示卡深化（客户是谁/什么让团队伟大/如何贡献组织成功）；⑤清晰记录（一页、团队自己的话、可视化）；⑥让宪章「活」——新人 onboarding 引用、冲突时引用、复盘时问「我们活出宪章了吗」、链接绩效；⑦约定回顾周期（季度或重大变化后）。提示：绿卡/红卡行为清单让「信任什么、不容什么」一目了然。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">团队宪章七步，关键请中立引导师平衡声音；用「绿卡鼓励/红卡零容忍」行为清单显式价值观；宪章须链接 onboarding/冲突/复盘才「活」。</div></details>
      <div class="src">🔗 <a href="https://growth-space.co.uk/blog/tag/Team+Charter+Template" target="_blank">growth-space.co.uk/.../Team+Charter+Template</a></div>
      <div class="note">适用：② 团队组建/重组——宪章分步指南+绿红卡行为，把假设变共识。</div>
    </div>''')

cards.append('''  <div class="hl">
      <div class="top"><span class="emoji">🛠️</span><h3>团队宪章 Wiki 模板·可复制的协作协议骨架</h3><span class="cat">团队宪章</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">GitHub 开源团队宪章 wiki 模板，可直接复制填充：成员（姓名/代词/角色/时区/工时）、伙伴团队、对接人；总体工作协议（如「沟通各自日程/不做私下小群/把 retro 行动项上看板/让每人被听见/翻转 assume good intent 防权力失衡」）；分歧处理（决策矩阵）；沟通与仪式（standup/周同步/复盘/coworking）；核心工时；与伙伴团队的沟通规范与无障碍需求；工具（Zoom/Teams/看板）；笔记与文档落点；角色（擅长/想做/不愿做）；反馈机制（正式/非正式频率）；「你还想让队友知道的」。模板把「我们如何一起工作」结构化，适合新经理直接拿去带团队共创。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">直接复制 wiki 模板填充：成员/工作协议/分歧处理/沟通仪式/角色/反馈；把「assume good intent 翻转为防权力失衡」写进协议；新人 onboarding 即引用。</div></details>
      <div class="src">🔗 <a href="https://github.com/annepetersen/teams/wiki/Team-charter-template" target="_blank">github.com/annepetersen/teams/wiki/Team-charter-template</a></div>
      <div class="note">适用：② 新经理带新团队——拿来即用的宪章骨架，把协作假设变书面协议。</div>
    </div>''')

cards.append('''  <div class="hl">
      <div class="top"><span class="emoji">🧩</span><h3>跨职能团队会议·破筒仓+三 Amigos（心理安全）</h3><span class="cat">跨职能启动</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">StudyRaid 的跨职能会议实践：定期把开发/测试/产品/设计聚到一起从一开始就协作，打破「抛墙式」筒仓。典型「三 Amigos」会议（开发+测试+产品）：①功能 Kick-off——PO 讲用户故事与业务价值；②澄清提问——全队挖歧义、边界、验收标准；③测试场景头脑风暴——测试主导，开发即时看到代码将如何被验证；④技术规划——开发讲实现，团队早识别风险依赖。格式扩展：backlog refinement（测试定可测验收标准）、daily standup（含测试进度）、retro（质量视角复盘）。数据：结构化跨职能会议使关键生产 bug 降约 40%。底座是心理安全感——让人敢问「蠢问题」、尊重挑战。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">跨职能启动用「三 Amigos」早协作破筒仓；把验收标准/风险在写码前定；retro 含质量视角；心理安全是底座。</div></details>
      <div class="src">🔗 <a href="https://app.studyraid.com/en/read/50689/2411551/implement-cross-functional-team-meetings" target="_blank">app.studyraid.com/.../cross-functional-team-meetings</a></div>
      <div class="note">适用：② 跨职能/项目启动会——破筒仓+三 Amigos+心理安全，降生产 bug 约 40%。</div>
    </div>''')

cards.append('''  <div class="hl">
      <div class="top"><span class="emoji">📋</span><h3>项目 Kickoff 议程·RACI+决策日志（虚拟差异）</h3><span class="cat">项目Kickoff</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">Alex Berman 的复制即用 Kickoff 议程：欢迎介绍→项目背景→目标与范围（含 out-of-scope）→角色与 RACI→时间线与里程碑→沟通计划→预算→风险与假设→Q&A 与下一步（owner+日期）。核心产出是「Kickoff 文档」：项目概述/成功标准/范围定义/RACI 表/里程碑/风险假设日志/已做决策/行动项，1-3 页、24 小时内发出，成为后续范围争议的「决策日志」（week6 有人声称「不知道 deadline」，翻文档即可）。虚拟 Kickoff 差异：开场定 ground rules（chat/举手/Q&A 时机）、设 co-host 管 chat、共享屏幕实时展示而非只讲、记录+录像双备份、跟进比线下更快。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">Kickoff 必产「决策日志」式文档（范围/RACI/决策/行动项），24h 内发；虚拟场加 ground rules+co-host+实时共享+录像；决策写定稿句而非讨论摘要。</div></details>
      <div class="src">🔗 <a href="https://alexberman.com/project-kickoff-agenda" target="_blank">alexberman.com/project-kickoff-agenda</a></div>
      <div class="note">适用：② 项目/跨部门 Kickoff——RACI+决策日志防「从没说过」，虚拟场加三规矩。</div>
    </div>''')

cards.append('''  <div class="hl">
      <div class="top"><span class="emoji">🖊️</span><h3>项目 Kickoff 议程·填例+可视化决策（60 分钟）</h3><span class="cat">项目Kickoff</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">Laxis 的 60 分钟复制即用 Kickoff 议程（5-12 人）：欢迎介绍(5)→项目目的与目标(10)→范围与 out-of-scope(8)→角色与 RACI(10)→时间线与里程碑(8)→风险与依赖(7)→沟通计划(5)→成功指标(3)→Q&A(2)→下一步与 owner(2)。亮点：给「Atlas 客户门户」填好的真实样例——out-of-scope 写具体（SSO/移动端本版不做）、Legal 依赖钉死 8/8 日期、每个下一步都挂人名；强调「把决策写在大屏上大家看着定稿，事后难翻案」，每段结束 pause 确认「我们同意 X 在范围、Y 不在——对吗」。远程用共屏文档实时记录。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">60 分钟 Kickoff 十段；用真实填例把 out-of-scope/依赖/owner 钉死；决策可视化记录+每段确认，防周三月翻案。</div></details>
      <div class="src">🔗 <a href="https://www.laxis.com/blog/project-kickoff-meeting-agenda" target="_blank">laxis.com/blog/project-kickoff-meeting-agenda</a></div>
      <div class="note">适用：② 项目 Kickoff——填例+可视化决策+逐段确认，落地性强。</div>
    </div>''')

# ---------- 拆分 ③ / ② ----------
cards_exec = cards[:6]
cards_sup  = cards[6:]
assert len(cards_exec) == 6 and len(cards_sup) == 6, (len(cards_exec), len(cards_sup))

def grid_close(html, start):
    """返回从 start('<div class="grid">') 起匹配的 grid 闭合 </div> 位置。"""
    end_of_open = html.index('>', start) + 1
    depth = 1
    i = end_of_open
    while i < len(html):
        no = html.find('<div', i)
        nc = html.find('</div>', i)
        if nc == -1:
            break
        if no != -1 and no < nc:
            depth += 1
            i = no + 4
        else:
            depth -= 1
            i = nc + 6
            if depth == 0:
                return nc
    return -1

html = io.open(WALL, encoding='utf-8').read()

# sec3 头位置 -> 第一个 grid
pos_sec3 = html.find('<div class="sec sec3">')
pos_sec2 = html.find('<div class="sec sec2">')
g3_open = html.find('<div class="grid">', pos_sec3)
g2_open = html.find('<div class="grid">', pos_sec2)
c3 = grid_close(html, g3_open)
c2 = grid_close(html, g2_open)
assert c3 != -1 and c2 != -1, (c3, c2)
# 确保 sec3 grid 在 sec2 之前
assert c3 < pos_sec2, (c3, pos_sec2)

# 注入：③ 卡插在 sec3 grid 末尾（闭合前），② 卡插在 sec2 grid 末尾
ins3 = '\n'.join(cards_exec) + '\n'
ins2 = '\n'.join(cards_sup) + '\n'
html = html[:c3] + ins3 + html[c3:]
# 插入 ② 后整体偏移，重新定位 c2
c2 += len(ins3)
html = html[:c2] + ins2 + html[c2:]

# 计数更新
html = html.replace('>52 卡<', '>58 卡<')
html = html.replace('>104 卡<', '>110 卡<')

# hero p 追加 r18 段
r18note = (' ｜ 十八轮补采 +12（2026-08-20）：团队宪章共创(Miro官方·一手)/分步指南(growth-space)/Wiki模板(GitHub)'
           '（②③）；新领导同化 NLA 流程(InstituteOD)/领导入职30-60-90(GalleryHR)/高管入职90天三阶段(NextOne)（③）；'
           '高管退修会2.0五步+团队宪章(Odgers)/季度节奏决策导向(Metavent)/四类挑战3天结构(ElliottRector)（③）；'
           '跨部门启动破筒仓(StudyRaid)/项目Kickoff RACI+决策日志(AlexBerman)/可视化决策(Laxis)（②）')
p_close = html.find('</p>')
assert p_close != -1
html = html[:p_close] + r18note + html[p_close:]

io.open(WALL, 'w', encoding='utf-8').write(html)

# tmp 文件：全部 12 卡（供 gen_run_page 拆分）
tmp = '\n'.join(cards) + '\n'
io.open(TMP, 'w', encoding='utf-8').write(tmp)

# 校验
n_hl = html.count('<div class="hl">')
print('OK wall updated | total <div class="hl"> =', n_hl, '(expect 168)')
print('tmp cards =', tmp.count('<div class="hl">'), '(expect 12)')
print('sec3 tag present:', '>58 卡<' in html, '| sec2 tag present:', '>110 卡<' in html)
