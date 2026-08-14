# -*- coding: utf-8 -*-
import os, json

BASE = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(BASE, 'icebreaker', 'icebreaker.html')
TMP = os.path.join(BASE, 'icebreaker', '.run_newcards.tmp.html')
IDX = os.path.join(BASE, 'index.json')

# ---------- ③ 高管间 cards ----------
C1 = '''  <div class="hl">
      <div class="top"><span class="emoji">🏞️</span><h3>高管战略静修设计·40%工作/30%体验/30%留白 + 中立引导师</h3><span class="cat">高管静修</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
      <p class="val">企业高管团队静修（CEO onboarding / 董事冲突 / 五年战略）须专业交付：①需求评估定 3 个可交付物；②选址匹配目标（敏感重组用私密 lodge）；③议程 40% 结构化工作（战略/工作坊/引导讨论）+30% 体验式（CSR/户外解难/帆船）+30% 留白（spa/晚餐/反思）；④必请外部中立引导师——内部 HR/CEO 带活动会保留权力动态、让 junior 怯场；⑤收尾建 30/90 天行动问责。核心：静修价值在返岗后习惯转化，非现场热闹。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">高管静修用「40/30/30 结构 + 外部中立引导师 + 30/90 天问责」；绝不靠内部人带活动；把洞察落为带责任人/截止日的行动计划。</div></details>
      <div class="src">🔗 <a href="https://teambuildingkenya.co.ke/executive-team-building-in-kenya" target="_blank">teambuildingkenya.co.ke/executive-team-building-in-kenya</a></div>
      <div class="note">适用：③ 高管/CEO 团队战略静修——专业设计替代团建游戏，中立引导师 hold 敏感对话，返岗问责闭环。</div>
    </div>'''

C2 = '''  <div class="hl">
      <div class="top"><span class="emoji">🧩</span><h3>核心领导团队凝聚力工作坊·克服团队协作五项障碍（Lencioni 中国化）</h3><span class="cat">高管团队</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
      <p class="val">企赢（qywin.cn）基于兰西奥尼《克服团队协作五项障碍》为 CEO+CXO/VP 级「第一团队」定制：导入团队协作评测→Day1 信任重建（个人领导力画像+团队信任练习）+良性冲突契约（围绕组织真实现状展开，拒绝无效妥协）→Day2 责任共担（组织阶段目标+协同规则）+战略共识（战略记分板+个人目标承诺）。收益：突破表面和谐建基于弱点的深度信任、掌握战略争议良性冲突、战略穿透一致。安踏/赛默飞等标杆验证；封闭式私密场域保高管坦诚。典型场景：新组建/空降高管团队、战略转型期。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">高管「第一团队」用 Lencioni 五项障碍框架——先建基于弱点的信任→定良性冲突契约→责任共担→战略共识；闭环输出个人承诺与协同规则，私密场域保坦诚。</div></details>
      <div class="src">🔗 <a href="https://www.qywin.cn/product/product8856.html" target="_blank">qywin.cn/product/product8856.html</a></div>
      <div class="note">适用：③ 核心领导团队（CEO+CXO/VP）凝聚力——兰西奥尼模型中国化，信任→冲突→责任→战略四步闭环，空降/转型期首选。</div>
    </div>'''

# ---------- ② 上下级 cards ----------
C3 = '''  <div class="hl">
      <div class="top"><span class="emoji">🤝</span><h3>新经理首场团队会·先建信任不画愿景（FranklinCovey）</h3><span class="cat">新经理破冰</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">FranklinCovey 权威指南：新经理首会目标不是宣布愿景/变革，而是建信任定基调。五步：①建信任不画图——团队对你天然存疑，先赢得信任再谈方向；②了解团队并记笔记——问 get-to-know-you 问题、记下来日后用（如生日带冰淇淋）；③分享真实自己——领导理念/初心/价值观而非简历成就，占比≤25%；④亮明「学习模式」——承认你才是新人里知最少者、你是海绵；⑤问 2-4 个深度 probe 问题（想改变什么/禁忌话题/最大挫败/如何收反馈）。会前会后必排 1:1。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">新经理首会以「建信任」为唯一目标：分享真实领导理念+亮明学习模式（示弱）+问深度问题+记笔记；会前会后排 1:1，绝不首会就宣布变革。</div></details>
      <div class="src">🔗 <a href="https://www.franklincovey.vn/resources/article/new-managers-heres-how-to-run-your-first-team-meeting" target="_blank">franklincovey.vn/.../new-managers-heres-how-to-run-your-first-team-meeting</a></div>
      <div class="note">适用：② 新任/接手经理首场团队会——FranklinCovey 权威范式，先信任后方向，示弱建信任。</div>
    </div>'''

C4 = '''  <div class="hl">
      <div class="top"><span class="emoji">🧭</span><h3>新团队启动四部议程·Why/Who/How/What（Lencioni 三问连人）</h3><span class="cat">新经理破冰</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">高管教练 Scott Eblin 的四词议程适用于任何首次团队会：Why（团队为何存在/对组织与客户的意义）→Who（连接与信任：用 Lencioni 三问——在哪长大/童年几个孩子/最大挑战，人人都曾是孩子，快速连人）→How（你想要的协作规则+让他们说出行为证据以便相互问责）→What（定义 30-90 天成功样貌建势头）。核心：首次会是你定义目的、建信任、立规则、排优先级的唯一机会，用四词结构替代冗长 PPT。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">新团队首会用「Why→Who→How→What」四词议程；Who 环节用 Lencioni 三问（成长地/童年手足/最大挑战）快速连人；What 落在 30-90 天具体成功标记。</div></details>
      <div class="src">🔗 <a href="https://www.linkedin.com/pulse/how-get-your-new-team-off-strong-start-scott-eblin" target="_blank">linkedin.com/pulse/.../how-get-your-new-team-off-strong-start-scott-eblin</a></div>
      <div class="note">适用：② 新经理/空降 leader 启动新团队——四词议程+Lencioni 三问，首会即连人定规则。</div>
    </div>'''

C5 = '''  <div class="hl">
      <div class="top"><span class="emoji">🔗</span><h3>跨职能团队信任建设·背景介绍+团队规范前置</h3><span class="cat">跨职能信任</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">跨职能团队（不同汇报线/职责）信任建设四法：①让人放松——首会前安排 coffee/晚餐破冰，leader 介绍并融入；②了解背景——即便熟人也让每人讲「我代表谁/带来什么经验/你该找我解决什么」，配对互介或白板三问；③共建团队规范（norms）——首会就对齐运营原则（会议/决策/沟通/冲突处理），便利贴归类成「我们同意…我们将…」，规范须反映多元视角；④提前直面难题——预判分歧点并鼓励开放坦诚。信任须贯穿全程、早期建立。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">跨职能团队首会做三件事——放松破冰+轮流讲背景价值（我代表谁/带来什么）+共建 norms（会议/决策/冲突规则）；提前点明可能的分歧降防备。</div></details>
      <div class="src">🔗 <a href="http://engagingpotential.com.au/creating-a-high-performance-team-the-building-of-trust/" target="_blank">engagingpotential.com.au/.../creating-a-high-performance-team-the-building-of-trust</a></div>
      <div class="note">适用：② 跨职能/项目团队 leader——用背景互介+norms 前置+提前直面冲突建信任，替代游戏。</div>
    </div>'''

C6 = '''  <div class="hl">
      <div class="top"><span class="emoji">🛠️</span><h3>10 个专业团队信任活动·红旗轮/优势互认/决策复盘/承诺上墙</h3><span class="cat">团队信任</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">咨询机构精选 10 个非游戏信任活动：①红旗轮——周会首问「一个风险/顾虑」，让升级成常态而非 career risk；②优势互认——具体命名他人贡献（非空泛「你真棒」）；③决策复盘——回顾真实决策的信息/参与者/取舍/改进，提升决策透明度；④承诺上墙——会末每人声明一个 checkpoint 前承诺并可视化，下会 review 不羞辱；⑤配对走访——设计 lead 与现场主管等不常并肩者同走现场，软化假设；⑥求助练习——「未来两周我需要团队一件事…」；⑦事后复盘四问（发生/有用/更难/改变）。可靠性靠小可见履约累积。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">用「红旗轮+承诺上墙+决策复盘+优势互认」替代破冰游戏；领导对红旗好奇而非批评，把履约变可见习惯。</div></details>
      <div class="src">🔗 <a href="https://connectiveconsultinggrp.com/best-team-trust-building-activities" target="_blank">connectiveconsultinggrp.com/best-team-trust-building-activities</a></div>
      <div class="note">适用：② 经理带跨职能/有张力团队——10 个专业信任活动，靠可见履约与早期升级建信任。</div>
    </div>'''

C7 = '''  <div class="hl">
      <div class="top"><span class="emoji">🤲</span><h3>经理建立协作与信任文化·以身作则/停止甩锅/匿名信任问卷</h3><span class="cat">信任文化</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">管理者建协作信任文化七法：团队建设加速凝聚、办内部活动降参与壁垒、任务与关系并重（HBR：最高产创新团队由 task+relationship 双导向 leader 带）、以身作则示范协作、停止甩锅（指责羞辱是失信团队特征）、谈信任问题（匿名问卷找失信源、只报整体不曝个人）、明确信任是协作第一要务。核心：没有信任的团队只是「恰巧被凑一起的个体」，真协作必先建信任。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">经理建信任文化——task+relationship 双导向以身作则、遇挫不甩锅、用匿名问卷定位失信源并整体反馈；把信任设为协作第一要务。</div></details>
      <div class="src">🔗 <a href="https://online.usca.edu/articles/mba/creating-a-culture-of-collaboration.aspx" target="_blank">online.usca.edu/articles/mba/creating-a-culture-of-collaboration.aspx</a></div>
      <div class="note">适用：② 经理/中层建团队信任文化——以身作则+停止指责+匿名信任诊断，双导向领导。</div>
    </div>'''

C8 = '''  <div class="hl">
      <div class="top"><span class="emoji">📡</span><h3>90 天远程信任计划·基线调研/快赢/仪式/度量</h3><span class="cat">远程信任</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">分布式团队领导者的周度 90 天远程信任蓝图：诊断（10 题基线调研，量清晰度/可靠性/包容/认可/心理安全，找最大缺口）→快赢（D0-30：公开目标角色+公共看板、周度 20min 1:1 脚本、同伴 shoutout+月度 impact、新成员 72h 打卡+30 天清单）→系统仪式（D30-60：async 站会/周报/双周 demo、决策登记、跨区结对、领导发反思笔记与决策理由）→嵌入文化（D60-90：导师制）→30/60/90 复测并公布行动。一致短频 check-in 是远程信任最快杠杆。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">远程团队用「基线调研→快赢（透明+1:1+认可）→系统仪式（决策登记/async）→30/60/90 复测」90 天蓝图；可预测沟通+可见进度+公平认可是核心。</div></details>
      <div class="src">🔗 <a href="https://www.upscend.com/blogs/90-day-remote-trust-building-plan-for-managers-leaders" target="_blank">upscend.com/blogs/90-day-remote-trust-building-plan-for-managers-leaders</a></div>
      <div class="note">适用：② 分布式/远程团队经理——90 天结构化信任计划，诊断→快赢→仪式→度量闭环。</div>
    </div>'''

C9 = '''  <div class="hl">
      <div class="top"><span class="emoji">💻</span><h3>虚拟团队建设·小胜轮/玫瑰-荆棘-苞/伙伴制/30 天打卡</h3><span class="cat">远程信任</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">远程团队建设按场景落地：①例会快活动——小胜轮（每人分享一周小赢，让进度可见）、单问题破冰（本周帮你工作的工具?学到了什么?）、玫瑰-荆棘-苞（顺/难/潜力，快速读士气）；②新远程员工 onboarding——结构化介绍（我是谁/角色/合作者/可问谁）+首周 buddy（非替代经理，答非正式问题讲清潜规则）+async「认识团队」笔记（角色/拥有/沟通偏好/时区）+首月 30 天打卡（清晰?困惑?和谁合作多?文档缺口?）。避免过度私人问题。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">远程团队周会用「小胜轮+玫瑰荆棘苞+单问题破冰」低成本暖场；新员工配 30 天 buddy+async 团队档案+首月打卡，让新人第一天就可见。</div></details>
      <div class="src">🔗 <a href="https://www.hirebasis.com/blog/virtual-team-building" target="_blank">hirebasis.com/blog/virtual-team-building</a></div>
      <div class="note">适用：② 远程/虚拟团队经理——例会轻量暖场+新员工结构化 onboarding（buddy/档案/30 天打卡）替代强制团建。</div>
    </div>'''

C10 = '''  <div class="hl">
      <div class="top"><span class="emoji">🔐</span><h3>数字信任远程团队·公开表扬私下教练/失误常态化/异步仪式</h3><span class="cat">远程信任</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">远程团队数字信任策略：用好奇替自我——问更好问题、coaching 而非求完美；公开护短（对 stakeholder 护成员不背锅）；建「失误」线程/仪式把教训变共享；及时反馈（公开夸/私下具体 coach）；对齐沟通节奏（office hours/AMA/周报）可预测包容；用清晰结果替微管。onboarding 加速关系：首日 buddy+「工作在哪」地图+启动项目早赢+早期领导 check-in。度量三领先指标：会议/async 参与度、按时履约、跨团队交接无返工。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">远程数字信任——公开表扬+私下具体 coach、建「失误」 ritual 降恐惧、buddy+早赢+领导 check-in 加速 onboarding；用可预测仪式链反馈与真实产出。</div></details>
      <div class="src">🔗 <a href="https://smartkeys.org/digital-trust-remote-teams" target="_blank">smartkeys.org/digital-trust-remote-teams</a></div>
      <div class="note">适用：② 远程团队经理——数字信任靠公开护短+失误常态化+异步仪式，onboarding 用 buddy/早赢/check-in 加速连接。</div>
    </div>'''

C11 = '''  <div class="hl">
      <div class="top"><span class="emoji">🎴</span><h3>高管/跨职能视觉引导·双镜头/承诺阶梯/勇敢对话彩排</h3><span class="cat">高管引导</span><span class="badge r2">上下级</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
      <p class="val">面向高管与跨职能团队的视觉引导三游戏（领导力教练机构）：①双镜头——每人选「他人怎么看这事」与「自己怎么看」两张图，先讲他者镜头消解防御、建同理，再讲个人；引导者收尾问「我们优化什么/愿 trade off 什么」，把争论变价值抉择；②承诺阶梯——三轮选图（想要更多的行为/拉走它的/最小 next action），每人以「I will」开局，定 check-in 点；③勇敢对话彩排——选「一直没说的事」图，2 分钟倾诉+同伴镜像一句，转身问「什么让它更安全」，转团队协议。带高管时靠框架/节奏/决策三件事保可信，落点必是业务语言（对齐/所有权/决策质量）。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">带高管/跨职能用视觉引导——双镜头消解防御建同理、承诺阶梯从洞察到行为、勇敢对话彩排安全练 candor；每活动必 debrief 落成决策（谁/何时/做什么）。</div></details>
      <div class="src">🔗 <a href="https://points-of-you.com/visual-training-games-for-teams" target="_blank">points-of-you.com/visual-training-games-for-teams</a></div>
      <div class="note">适用：②+③ 高管/跨职能团队引导——视觉游戏替代幼稚破冰，以业务语言 framing+决策收尾保高管可信。</div>
    </div>'''

sec3_cards = [C1, C2]
sec2_cards = [C3, C4, C5, C6, C7, C8, C9, C10, C11]
all_cards = sec3_cards + sec2_cards

# write tmp run-page cards
open(TMP, 'w', encoding='utf-8').write('\n'.join(all_cards))
print('tmp cards written:', len(all_cards))

# ---------- update wall ----------
html = open(WALL, encoding='utf-8').read()

old_hero = ('<p>采集于 2026-08-14 ｜ R10 轮 enrich +7（仅②③、0 peer；已清退上轮误产 12 张重复卡）'
            '｜ 六维评估（含关系适配度）｜ 一手/二手标注 ｜ 历史去重 ｜ 受众关系分层（仅②上下级 / ③高管间）'
            '｜ 本轮回修 R8 注入的 11 张损坏卡 + 脆弱信任缺失闭合</p>')
new_hero = ('<p>采集于 2026-08-14 ｜ R11 轮补采 +11（仅②③、0 peer）｜ 六维评估（含关系适配度）'
            '｜ 一手/二手标注 ｜ 历史去重 ｜ 受众关系分层（仅②上下级 / ③高管间）'
            '｜ 本期新开：高管静修 40/30/30 设计、核心领导团队 Lencioni 工作坊、新经理首会建信任范式、跨职能/远程团队信任建立</p>')
assert old_hero in html, 'hero not found'
html = html.replace(old_hero, new_hero)

# sec3 count 32 -> 34
html = html.replace('③ 领导↔领导（高管间 · exec）</h2><span class="tag">32 卡</span>',
                    '③ 领导↔领导（高管间 · exec）</h2><span class="tag">34 卡</span>')
# insert sec3 cards inside sec3 grid (before its closing </div> that precedes sec2)
anchor3 = '</div>\n\n<div class="sec sec2">'
assert anchor3 in html, 'anchor3 not found'
html = html.replace(anchor3, '\n'.join(sec3_cards) + '\n</div>\n\n<div class="sec sec2">', 1)

# sec2 count 54 -> 63
html = html.replace('② 领导↔员工（上下级 · supervisor）</h2><span class="tag">54 卡</span>',
                    '② 领导↔员工（上下级 · supervisor）</h2><span class="tag">63 卡</span>')
# insert sec2 cards inside sec2 grid (before its closing </div> that precedes <footer>)
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
    {"title":"高管战略静修设计·40%工作/30%体验/30%留白 + 中立引导师","normKey":"高管战略静修设计40工作30体验30留白中立引导师","url":"https://teambuildingkenya.co.ke/executive-team-building-in-kenya","sourceType":"secondary","relation":"exec","summary":"高管团队静修专业交付：需求评估定3交付物、40%结构化工作+30%体验+30%留白、必请外部中立引导师、收尾30/90天行动问责；价值在返岗习惯转化。","topic":"icebreaker"},
    {"title":"核心领导团队凝聚力工作坊·克服团队协作五项障碍（Lencioni 中国化）","normKey":"核心领导团队凝聚力工作坊克服团队协作五项障碍lencioni中国化","url":"https://www.qywin.cn/product/product8856.html","sourceType":"secondary","relation":"exec","summary":"基于兰西奥尼五项障碍为CEO+CXO/VP定制：信任重建+良性冲突契约+责任共担+战略共识，安踏/赛默飞验证，私密场域保坦诚。","topic":"icebreaker"},
    {"title":"新经理首场团队会·先建信任不画愿景（FranklinCovey）","normKey":"新经理首场团队会先建信任不画愿景franklincovey","url":"https://www.franklincovey.vn/resources/article/new-managers-heres-how-to-run-your-first-team-meeting","sourceType":"secondary","relation":"supervisor","summary":"FranklinCovey范式：首会以建信任为唯一目标——分享真实领导理念+亮明学习模式示弱+问深度问题+记笔记，绝不首会宣布变革。","topic":"icebreaker"},
    {"title":"新团队启动四部议程·Why/Who/How/What（Lencioni 三问连人）","normKey":"新团队启动四部议程whywhohowwhatlencioni三问连人","url":"https://www.linkedin.com/pulse/how-get-your-new-team-off-strong-start-scott-eblin","sourceType":"secondary","relation":"supervisor","summary":"高管教练四词议程：Why(目的)→Who(Lencioni三问快速连人)→How(协作规则+行为证据)→What(30-90天成功样貌)。","topic":"icebreaker"},
    {"title":"跨职能团队信任建设·背景介绍+团队规范前置","normKey":"跨职能团队信任建设背景介绍团队规范前置","url":"http://engagingpotential.com.au/creating-a-high-performance-team-the-building-of-trust/","sourceType":"secondary","relation":"supervisor","summary":"跨职能团队信任四法：放松破冰+轮流讲背景价值+首会共建norms(会议/决策/冲突规则)+提前直面分歧。","topic":"icebreaker"},
    {"title":"10 个专业团队信任活动·红旗轮/优势互认/决策复盘/承诺上墙","normKey":"10个专业团队信任活动红旗轮优势互认决策复盘承诺上墙","url":"https://connectiveconsultinggrp.com/best-team-trust-building-activities","sourceType":"secondary","relation":"supervisor","summary":"10个非游戏信任活动：红旗轮(早期升级)、优势互认、决策复盘、承诺上墙、配对走访、求助练习、事后复盘四问。","topic":"icebreaker"},
    {"title":"经理建立协作与信任文化·以身作则/停止甩锅/匿名信任问卷","normKey":"经理建立协作与信任文化以身作则停止甩锅匿名信任问卷","url":"https://online.usca.edu/articles/mba/creating-a-culture-of-collaboration.aspx","sourceType":"secondary","relation":"supervisor","summary":"管理者建信任文化七法：task+relationship双导向以身作则、遇挫不甩锅、匿名问卷定位失信源、把信任设协作第一要务。","topic":"icebreaker"},
    {"title":"90 天远程信任计划·基线调研/快赢/仪式/度量","normKey":"90天远程信任计划基线调研快赢仪式度量","url":"https://www.upscend.com/blogs/90-day-remote-trust-building-plan-for-managers-leaders","sourceType":"secondary","relation":"supervisor","summary":"分布式团队90天信任蓝图：基线调研→快赢(透明+1:1+认可)→系统仪式(决策登记/async)→30/60/90复测。","topic":"icebreaker"},
    {"title":"虚拟团队建设·小胜轮/玫瑰-荆棘-苞/伙伴制/30 天打卡","normKey":"虚拟团队建设小胜轮玫瑰荆棘苞伙伴制30天打卡","url":"https://www.hirebasis.com/blog/virtual-team-building","sourceType":"secondary","relation":"supervisor","summary":"远程团队建设：例会小胜轮+玫瑰荆棘苞+单问题破冰暖场；新员工结构化onboarding(buddy/async档案/首月30天打卡)。","topic":"icebreaker"},
    {"title":"数字信任远程团队·公开表扬私下教练/失误常态化/异步仪式","normKey":"数字信任远程团队公开表扬私下教练失误常态化异步仪式","url":"https://smartkeys.org/digital-trust-remote-teams","sourceType":"secondary","relation":"supervisor","summary":"远程数字信任：公开护短+私下具体coach、建失误ritual降恐惧、buddy+早赢+领导check-in加速onboarding。","topic":"icebreaker"},
    {"title":"高管/跨职能视觉引导·双镜头/承诺阶梯/勇敢对话彩排","normKey":"高管跨职能视觉引导双镜头承诺阶梯勇敢对话彩排","url":"https://points-of-you.com/visual-training-games-for-teams","sourceType":"secondary","relation":"supervisor,exec","summary":"视觉引导三游戏：双镜头消解防御建同理、承诺阶梯从洞察到行为、勇敢对话彩排安全练candor；带高管以业务语言framing保可信。","topic":"icebreaker"},
]

existing_urls = set(e.get('url','').lower() for e in data)
added = 0
for e in new_entries:
    if e['url'].lower() in existing_urls:
        print('SKIP dup url', e['url'])
        continue
    data.append(e)
    existing_urls.add(e['url'].lower())
    added += 1
print('index added:', added, 'total:', len(data))

json.dump(data, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('index.json written')
