# -*- coding: utf-8 -*-
import os, json

BASE = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(BASE, 'icebreaker', 'icebreaker.html')
TMP = os.path.join(BASE, 'icebreaker', '.run_newcards.tmp.html')
IDX = os.path.join(BASE, 'index.json')

# ---------- ③ 高管间 cards ----------
C1 = '''  <div class="hl">
      <div class="top"><span class="emoji">🧩</span><h3>资深领导团队建设·20 个高浓度活动（桥接构建/脆弱循环/逆向头脑风暴/5 分钟 CEO/高管鲨鱼 Tank）</h3><span class="cat">高管团队</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
      <p class="val">资深领导团队建设不同于普通团建——目标在信任、坦诚与对齐，而非技能。重点活动：①Bridge Build（非语言搭桥，两半合体照出对齐差距）；②Vulnerability Loop（结构化脆弱分享，建立基于弱点的信任）；③Reverse Brainstorming（先想怎么搞砸、再反向找解法，激发异想）；④5-Minute CEO（限时 elevator pitch 战略，练高管表达与决策）；⑤Executive Shark Tank（内部路演真实业务挑战，练快速决策与谈判）。关键：用「结构性」替代游戏，反馈用 Start/Stop/Continue 保持建设性；远程可走共享文档。价值在可衡量业务结果与行为改变。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">资深领导团队用「桥接构建+脆弱循环+逆向头脑风暴+5 分钟 CEO+高管鲨鱼 Tank」等高浓度结构化活动替代团建游戏；以 Start/Stop/Continue 收尾保建设性，远程改共享文档。</div></details>
      <div class="src">🔗 <a href="https://kapable.club/blog/senior-leadership/20-best-senior-leadership-team-building-activities" target="_blank">kapable.club/blog/senior-leadership/20-best-senior-leadership-team-building-activities</a></div>
      <div class="note">适用：③ 核心领导团队（CXO/VP）凝聚力——高浓度结构化活动替代团建游戏，脆弱循环建信任、逆向头脑风暴激异想。</div>
    </div>'''

C2 = '''  <div class="hl">
      <div class="top"><span class="emoji">🎯</span><h3>高管信任加速器·同侪教练圈/即兴剧场/作战室模拟/工作风格工作坊</h3><span class="cat">高管信任</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
      <p class="val">面向高管团队的高浓度信任设计：①Peer Coaching Circle——每人带一个真实难题、小组轮转 hot seat 结构化教练（限时轮次防变成吐槽会，旋转 hot seat 拉平权力）；②Leadership Improv Intensive——即兴表演剥掉高管盔甲、练临场镇定与倾听，CEO 出丑大笑本身就是心理安全教材；③War-Room Simulation——把团队丢进虚构危机限时联合决策，彩排「压力下如何协作」，暴露沟通断点；④Working-Style Workshop——用共享框架讲清每人真实运作方式，给摩擦一个通用语言；⑤Pre/Post Pulse Survey——会前会后可比三问（联结/信任/推荐度）量化是否有效。硬规则：高管活动「结构>练习」，须有经验引导师。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">高管团队用「同侪教练圈(hot seat 轮换)+即兴剧场(剥盔甲)+作战室模拟(压力决策彩排)+工作风格工作坊」；配会前会后可比 Pulse 三问量化，必请有高管经验的引导师。</div></details>
      <div class="src">🔗 <a href="https://www.fusion-events.ca/resources/corporate-team-building-activities" target="_blank">fusion-events.ca/resources/corporate-team-building-activities</a></div>
      <div class="note">适用：③ 高管团队信任与决策协同——高浓度活动+量化验证，替代会议式务虚，引导师 hold 现场。</div>
    </div>'''

C3 = '''  <div class="hl">
      <div class="top"><span class="emoji">👑</span><h3>新任 CEO 前 90 天·先听后定（1-30 听 / 31-60 诊断对齐 / 61-90 建节奏）</h3><span class="cat">高管入职</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
      <p class="val">新 CEO 前 90 天决定能否建立可信度与长期影响。三阶段：①Days1-30 倾听先于行动——听董事会、领导团队、关键客户、财务数据，不急于宣布战略变更；②Days31-60 诊断对齐——按下一阶段要求评估每位高管、60 天内做必要人事调整（拖延会复利失信）、对齐领导团队；③Days61-90 承诺执行——建立运营节奏（周领导力同步/月业务复盘/季 OKR），节奏本身传递组织将如何运行。董事会责任：首月每周≥2 小时陪跑、亲自引荐关键干系人、保护其免陷入救火、早期给清晰反馈。过早宣布变革=摧毁可信度。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">新 CEO 90 天用「1-30 倾听（董事会/领导团队/客户/财务）→31-60 诊断对齐（评估高管+必要人事+运营节奏）→61-90 承诺执行（周同步/月复盘/季 OKR）」；董事会须陪跑引荐保护，绝不错峰宣布变革。</div></details>
      <div class="src">🔗 <a href="https://www.majhigroup.com/first-90-days-ceo.html" target="_blank">majhigroup.com/first-90-days-ceo.html</a></div>
      <div class="note">适用：③ 新任 CEO 与既有高管团队融合——先听后定建信任，运营节奏信号组织运行方式，董事会陪跑不可缺。</div>
    </div>'''

# ---------- ② 上下级 cards ----------
C4 = '''  <div class="hl">
      <div class="top"><span class="emoji">🚀</span><h3>新团队 credibility 30 天框架·倾听冲刺/知识致谢/早赢/透明锚/履约证</h3><span class="cat">新经理信任</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">新经理用 30 天五阶段框架快速建立可信度（关系性而非职位性）：①倾听冲刺(D1-7)——80% 听 20% 说，与每人 30 分钟 1:1，三问（该保护什么/最大挫败/若全权会改什么），记笔记复述不急着给方案；②知识致谢(D5-10)——首次团队会公开肯定团队已有认知（「我 impressed by 你们对 X 的理解」），证明你真听了、不摆救世主姿态；③早赢(D10-20)——选一个可见、两周内可解、直击日常痛点的问题去解（如冗余审批），早赢须解他们的题而非秀你的议程；④透明锚(D15-25)——坦诚分享一个真实挑战/约束/你尚不知的事（79% 员工把透明列为新领导最重要特质）；⑤履约证(D20-30)——团队心里有本承诺账，你每条是否跟进。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">新经理首月用「倾听冲刺(80/20+三问+记笔记)→知识致谢(公开肯定团队已有认知)→早赢(解他们的痛点≠秀议程)→透明锚(坦诚未知/约束)→履约证(每条承诺跟进)」五阶段建可信度。</div></details>
      <div class="src">🔗 <a href="https://www.confidenceplaybook.org/blog/how-to-establish-credibility-with-a-new-team-fast" target="_blank">confidenceplaybook.org/blog/how-to-establish-credibility-with-a-new-team-fast</a></div>
      <div class="note">适用：② 新任/接手经理首 30 天——credibility 是关系货币，靠倾听+早赢+透明+履约累积，非头衔。</div>
    </div>'''

C5 = '''  <div class="hl">
      <div class="top"><span class="emoji">🤝</span><h3>新经理首 30 天·四步建信任 + 每日五习惯</h3><span class="cat">新经理信任</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">HR 领导者视角：首 30 天定调一切。四步：①建关系——明确角色与标准、讲清优先级、问团队需要你做什么；②懂工作——shadow 团队、问卡点在哪/什么耗能/什么赋能；③强 1:1——周度结构化 1:1 显可靠、挖阻塞与成长；④造小赢——首月聚焦稳定/观察/小可见赢、拉团队设微目标。每日五习惯：主动倾听、早给反馈、造小赢、言行一致、坦诚（含艰难时刻）。核心：领导是特权不是 smartest person，信任才是你赢得的货币；resist「prove everything at once」。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">新经理首月「建关系(明确标准+问所需)→懂工作(shadow+问卡点)→强 1:1(周度结构化)→造小赢(稳定观察+微目标)」四步，配每日五习惯(倾听/早反馈/小赢/一致/坦诚)。</div></details>
      <div class="src">🔗 <a href="https://www.linkedin.com/pulse/how-build-trust-leader-your-first-30-days-silvia-toth-qqj3e" target="_blank">linkedin.com/pulse/how-build-trust-leader-your-first-30-days-silvia-toth-qqj3e</a></div>
      <div class="note">适用：② 新任经理首 30 天——领导是特权非头衔，信任靠关系+理解+1:1+小赢逐步建。</div>
    </div>'''

C6 = '''  <div class="hl">
      <div class="top"><span class="emoji">💡</span><h3>新组队首 30 天·建立信任五法（透明/识人/履约/开放沟通/共庆小赢）</h3><span class="cat">新团队信任</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">新团队组建首 30 天信任最关键：①以透明与清晰开局——公开沟通期望/目标/优先级（不确定生焦虑、清晰生信心）；②把人当个体了解——知其优势/经验/目标（「你最爱哪类工作、想往哪成长」）；③兑现承诺——说到做到，小行动影响最大（「我说周五跟进，这是更新」）；④尽早鼓励开放沟通——从第一天欢迎提问/顾虑/点子，心理安全是信任地基；⑤共庆小赢——认可进展/努力/协作。要点：信任不靠团建游戏，靠一致行动、诚实沟通与日常互动。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">新团队首月「透明清晰开局+把人当个体了解+说到做到兑现承诺+尽早鼓励开放沟通(心理安全)+共庆小赢」五法建信任；信任靠日常一致行动非游戏。</div></details>
      <div class="src">🔗 <a href="https://www.linkedin.com/posts/tru-art-hr_leadershipdevelopment-teambuilding-peoplemanagement-activity-7477416369198620674-Cm14" target="_blank">linkedin.com/posts/tru-art-hr.../5-ways-build-trust-new-team-30-days</a></div>
      <div class="note">适用：② 新组建/接手团队 leader——首 30 天定文化，透明+识人+履约+开放+小赢建信任。</div>
    </div>'''

C7 = '''  <div class="hl">
      <div class="top"><span class="emoji">🌱</span><h3>带领新/演进中团队·五步（意向倾听/澄清期望/心理安全/适配个体/促联结）</h3><span class="cat">新团队领导</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">接手新团队或大幅扩编时，领导者的倾听与理解定调文化：①意向倾听——首几周与每人 1:1，问「想让我知道团队什么/什么能让你更成功」，观察谁发言谁沉默，记笔记找主题，不打断；②澄清期望——先问团队对优先级的看法再定自己的，共同定义成功样貌与行为准则，透明讲清决策方式与反馈偏好；③建心理安全——公开承认变化、示范示弱（「我还在熟悉 X，有洞察欢迎告诉我」）、鼓励提问并以感恩回应批评；④适配个体——问反馈偏好/支持方式，早识别并认可每人优势；⑤促成员间联结——团队午餐/虚拟咖啡/协作脑暴，推动 peer 反馈与认可，强化共享目标。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">带新/演进中团队「意向倾听(1:1+观察+记主题)→澄清期望(共定成功+透明决策风格)→建心理安全(承认变化+示范示弱)→适配个体(问偏好+认可优势)→促成员联结(午餐/咖啡/peer 反馈)」五步。</div></details>
      <div class="src">🔗 <a href="https://liveoakleadership.com/blog/leading-a-new-or-evolving-team" target="_blank">liveoakleadership.com/blog/leading-a-new-or-evolving-team</a></div>
      <div class="note">适用：② 新任/扩编团队 leader——先听后定、建心理安全、适配个体、促成员间联结，定长期文化基调。</div>
    </div>'''

C8 = '''  <div class="hl">
      <div class="top"><span class="emoji">📈</span><h3>新经理前 90 天·清晰+节奏+系统（听先于改 / 一页 how-we-work / 运营节奏 / GROW 教练）</h3><span class="cat">新经理90天</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">新经理前 90 天建三地基：清晰（优先级与标准）、信任（稳定履约+冷静沟通）、操作系统（1:1/执行/决策节奏）。五战术：①听先于改——用三问（什么在运转/什么坏了/什么永不变）做倾听 1:1 并画系统地图，防解错问题；②定清晰期望——发一页「我们怎么工作」（优先级/质量/响应/决策归属），会议邀反馈；③建可见节奏——周 25 分钟 1:1+10 分钟站会+20 分钟周复盘，决策记录下周 revisit；④造早赢——从倾听挑一个痛点 30 天内解，前后对比并谢提的人；⑤可重复教练+护心理安全——1:1 用 GROW（目标/现实/选项/路径），早谢风险上报、批评私下具体。案例：7 人工程团队首月只听+文档+周 1:1+决策笔记，次月澄清角色+WIP 限+周复盘，D90 交付更稳、升级更少。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">新经理 90 天「听先于改(三问+系统地图)→一页 how-we-work 定清晰→周 1:1/站会/复盘建节奏→挑痛点造早赢→GROW 教练+护心理安全」，做可预测有用的 leader 非喧哗者。</div></details>
      <div class="src">🔗 <a href="https://learn-leadership-net.kit.com/posts/the-first-90-days-as-a-new-manager" target="_blank">learn-leadership-net.kit.com/posts/the-first-90-days-as-a-new-manager</a></div>
      <div class="note">适用：② 新任经理首 90 天——团队要可预测的非完美的 leader，清晰+节奏+系统先于自我证明。</div>
    </div>'''

C9 = '''  <div class="hl">
      <div class="top"><span class="emoji">📋</span><h3>团队章程 / 协作契约模板·使命/价值观/工作协议/决策权/反馈规范（工程师实例）</h3><span class="cat">团队章程</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">团队章程（Team Charter / Ways of Working）是「团队怎么一起工作」的契约，非项目章程。结构：①团队使命与目标（对齐组织）；②核心价值观（稳定优先于新奇/透明/无聊是好）；③工作协议（如「重要决策写进共享日志」「每倡议一个责任 owner」）；④沟通规范（渠道+响应时限）；⑤决策权分层（低影响执行者定/中影响书面提案/高影响团队会+文档权衡）；⑥反馈规范（私下给建设性反馈、以好奇非防御接收、用数据解技术分歧）；⑦角色职责；⑧工具平台。落地：专会共创、用自己话改写、人人署名承诺、每几月在 retro 复盘演化。附两个工程师团队实例（内部平台/产品应用），可直接套。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">新团队首会共创「团队章程」：使命+价值观+工作协议+沟通规范+决策权分层(低/中/高影响)+反馈规范+角色；人人署名承诺、retro 定期演化，变活参考非摆设。</div></details>
      <div class="src">🔗 <a href="https://leadshift.dev/engineering-team-charter-template-and-examples" target="_blank">leadshift.dev/engineering-team-charter-template-and-examples</a></div>
      <div class="note">适用：② 新经理/新组队——用团队章程把「怎么协作」显式契约化，降歧义/减冲突/加速新人融入，补 Atlassian Working Agreements。</div>
    </div>'''

sec3_cards = [C1, C2, C3]
sec2_cards = [C4, C5, C6, C7, C8, C9]
all_cards = sec3_cards + sec2_cards

# write tmp run-page cards
open(TMP, 'w', encoding='utf-8').write('\n'.join(all_cards))
print('tmp cards written:', len(all_cards))

# ---------- update wall ----------
html = open(WALL, encoding='utf-8').read()

old_hero = ('<p>采集于 2026-08-14 ｜ R11 轮补采 +11（仅②③、0 peer）｜ 六维评估（含关系适配度）｜ 一手/二手标注 ｜ 历史去重 ｜ 受众关系分层（仅②上下级 / ③高管间）'
            '｜ 本期新开：高管静修 40/30/30 设计、核心领导团队 Lencioni 工作坊、新经理首会建信任范式、跨职能/远程团队信任建立</p>')
new_hero = ('<p>采集于 2026-08-15 ｜ R12 轮补采 +9（仅②③、0 peer）｜ 六维评估（含关系适配度）｜ 一手/二手标注 ｜ 历史去重 ｜ 受众关系分层（仅②上下级 / ③高管间）'
            '｜ 本期新开：资深领导团队高浓度活动、高管信任加速器（同侪教练圈/作战室模拟）、新任 CEO 前 90 天、新经理 30 天 credibility 框架与团队章程模板</p>')
assert old_hero in html, 'hero not found'
html = html.replace(old_hero, new_hero)

# sec3 count 34 -> 37
html = html.replace('③ 领导↔领导（高管间 · exec）</h2><span class="tag">34 卡</span>',
                    '③ 领导↔领导（高管间 · exec）</h2><span class="tag">37 卡</span>')
anchor3 = '</div>\n\n<div class="sec sec2">'
assert anchor3 in html, 'anchor3 not found'
html = html.replace(anchor3, '\n'.join(sec3_cards) + '\n</div>\n\n<div class="sec sec2">', 1)

# sec2 count 63 -> 69
html = html.replace('② 领导↔员工（上下级 · supervisor）</h2><span class="tag">63 卡</span>',
                    '② 领导↔员工（上下级 · supervisor）</h2><span class="tag">69 卡</span>')
anchor2 = '</div>\n<footer>'
assert anchor2 in html, 'anchor2 not found'
html = html.replace(anchor2, '\n'.join(sec2_cards) + '\n</div>\n<footer>', 1)

open(WALL, 'w', encoding='utf-8').write(html)
print('wall updated')

# ---------- update index.json ----------
data = json.load(open(IDX, encoding='utf-8'))

def norm(s):
    return ''.join(ch for ch in s if ch.isalnum())

new_entries = [
    {"title":"资深领导团队建设·20 个高浓度活动（桥接构建/脆弱循环/逆向头脑风暴/5 分钟 CEO/高管鲨鱼 Tank）","normKey":"资深领导团队建设20个高浓度活动桥接构建脆弱循环逆向头脑风暴5分钟ceo高管鲨鱼tank","url":"https://kapable.club/blog/senior-leadership/20-best-senior-leadership-team-building-activities","sourceType":"secondary","relation":"exec","summary":"资深领导团队建设目标在信任/坦诚/对齐而非技能：Bridge Build(非语言搭桥照出对齐差距)、Vulnerability Loop(结构化脆弱建信任)、Reverse Brainstorming(逆向激异想)、5-Minute CEO(练表达决策)、Executive Shark Tank(内部路演练谈判)；Start/Stop/Continue 收尾保建设性。","topic":"icebreaker"},
    {"title":"高管信任加速器·同侪教练圈/即兴剧场/作战室模拟/工作风格工作坊","normKey":"高管信任加速器同侪教练圈即兴剧场作战室模拟工作风格工作坊","url":"https://www.fusion-events.ca/resources/corporate-team-building-activities","sourceType":"secondary","relation":"exec","summary":"高管团队高浓度信任设计：Peer Coaching Circle(hot seat 轮换结构化教练)、Leadership Improv(剥盔甲练倾听)、War-Room Simulation(压力决策彩排)、Working-Style Workshop(给摩擦通用语言)、Pre/Post Pulse 三问量化；高管活动结构>练习须引导师。","topic":"icebreaker"},
    {"title":"新任 CEO 前 90 天·先听后定（1-30 听 / 31-60 诊断对齐 / 61-90 建节奏）","normKey":"新任ceo前90天先听后定130听3160诊断对齐6190建节奏","url":"https://www.majhigroup.com/first-90-days-ceo.html","sourceType":"secondary","relation":"exec","summary":"新 CEO 前 90 天三阶段：1-30 倾听(董事会/领导团队/客户/财务)不急于宣布变革、31-60 诊断对齐(评估高管+必要人事+运营节奏)、61-90 承诺执行(周同步/月复盘/季 OKR)；董事会须陪跑引荐保护，过早宣布变革摧毁可信度。","topic":"icebreaker"},
    {"title":"新团队 credibility 30 天框架·倾听冲刺/知识致谢/早赢/透明锚/履约证","normKey":"新团队credibility30天框架倾听冲刺知识致谢早赢透明锚履约证","url":"https://www.confidenceplaybook.org/blog/how-to-establish-credibility-with-a-new-team-fast","sourceType":"secondary","relation":"supervisor","summary":"新经理 30 天五阶段建可信度(关系性非职位性)：倾听冲刺(80/20+三问+记笔记)、知识致谢(公开肯定团队已有认知)、早赢(解他们的痛点≠秀议程)、透明锚(坦诚未知/约束，79%员工视透明为最重要特质)、履约证(每条承诺跟进)。","topic":"icebreaker"},
    {"title":"新经理首 30 天·四步建信任 + 每日五习惯","normKey":"新经理首30天四步建信任每日五习惯","url":"https://www.linkedin.com/pulse/how-build-trust-leader-your-first-30-days-silvia-toth-qqj3e","sourceType":"secondary","relation":"supervisor","summary":"新经理首 30 天四步：建关系(明确标准+问所需)、懂工作(shadow+问卡点)、强 1:1(周度结构化)、造小赢(稳定观察+微目标)；每日五习惯：主动倾听/早给反馈/造小赢/言行一致/坦诚。领导是特权非头衔，信任靠逐步建。","topic":"icebreaker"},
    {"title":"新组队首 30 天·建立信任五法（透明/识人/履约/开放沟通/共庆小赢）","normKey":"新组队首30天建立信任五法透明识人履约开放沟通共庆小赢","url":"https://www.linkedin.com/pulse/leadershipdevelopment-teambuilding-peoplemanagement-activity-7477416369198620674-Cm14","sourceType":"secondary","relation":"supervisor","summary":"新团队首 30 天五法建信任：透明清晰开局、把人当个体了解、说到做到兑现承诺、尽早鼓励开放沟通(心理安全)、共庆小赢；信任不靠团建游戏，靠一致行动与日常互动。","topic":"icebreaker"},
    {"title":"带领新/演进中团队·五步（意向倾听/澄清期望/心理安全/适配个体/促联结）","normKey":"带领新演进中团队五步意向倾听澄清期望心理安全适配个体促联结","url":"https://liveoakleadership.com/blog/leading-a-new-or-evolving-team","sourceType":"secondary","relation":"supervisor","summary":"接手新/扩编团队五步：意向倾听(1:1+观察+记主题)、澄清期望(共定成功+透明决策风格)、建心理安全(承认变化+示范示弱)、适配个体(问偏好+认可优势)、促成员联结(午餐/咖啡/peer 反馈)。","topic":"icebreaker"},
    {"title":"新经理前 90 天·清晰+节奏+系统（听先于改 / 一页 how-we-work / 运营节奏 / GROW 教练）","normKey":"新经理前90天清晰节奏系统听先于改一页howwework运营节奏grow教练","url":"https://learn-leadership-net.kit.com/posts/the-first-90-days-as-a-new-manager","sourceType":"secondary","relation":"supervisor","summary":"新经理 90 天建三地基(清晰/信任/操作系统)：听先于改(三问+系统地图)、一页 how-we-work 定清晰、周 1:1/站会/复盘建节奏、挑痛点造早赢、GROW 教练+护心理安全；团队要可预测的非完美的 leader。","topic":"icebreaker"},
    {"title":"团队章程 / 协作契约模板·使命/价值观/工作协议/决策权/反馈规范（工程师实例）","normKey":"团队章程协作契约模板使命价值观工作协议决策权反馈规范工程师实例","url":"https://leadshift.dev/engineering-team-charter-template-and-examples","sourceType":"secondary","relation":"supervisor","summary":"团队章程(Team Charter/Ways of Working)是『团队怎么一起工作』的契约：使命+价值观+工作协议+沟通规范+决策权分层(低/中/高影响)+反馈规范+角色；专会共创、人人署名、retro 演化，补 Atlassian Working Agreements。","topic":"icebreaker"},
]

existing_urls = set(e.get('url', '').lower().rstrip('/') for e in data)
added = 0
for e in new_entries:
    key = e['url'].lower().rstrip('/')
    if key in existing_urls:
        print('SKIP dup url', e['url'])
        continue
    data.append(e)
    existing_urls.add(key)
    added += 1
print('index added:', added, 'total:', len(data))

json.dump(data, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('index.json written')
