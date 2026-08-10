# -*- coding: utf-8 -*-
"""破冰 第七轮补采 (+7)：注入 2 张③高管间 + 5 张②上下级 到 icebreaker.html，
更新 hero/标签计数，写 .run_newcards.tmp.html 供 gen_run_page.py。"""
import io, os

BASE = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(BASE, 'icebreaker', 'icebreaker.html')
TMP  = os.path.join(BASE, 'icebreaker', '.run_newcards.tmp.html')

# ---------------- ③ 高管间 (2) ----------------
C3_1 = '''    <div class="hl">
      <div class="top"><span class="emoji">🏛️</span><h3>企业文化共创工作坊·高管横向联结+纵向同频</h3><span class="cat">文化共创</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
      <p class="val">参与者=企业高管(十几人)、时长两天、目标=深化文化理解+加强部门连接协同+产出价值观行为准则成文化手册。设计理念双轴：①横向联结——从与场域联结/与人联结/与事联结三维度提升沟通品质；②纵向同频——从心智模式/能力模型/行为标准层面具身化换位思考。流程：第一天团队破冰(趣味身心游戏+个人故事分享+企业文化剧场即兴小剧场)→团队聆听(文化故事/吐槽小会释放情绪)→团队下潜(呈现真实动力游戏+复盘)→看见团队(未来展望+结束圈高能量仪式)；第二天暖场回顾→价值观行为共识→文化手册产出。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">高管文化共创=先用趣味破冰+个人故事+文化剧场打开(非游戏幼稚)，再用「吐槽小会」释放真实情绪、用「团队下潜」呈现真实动力，最后把价值观落成行为准则手册；避免只宣讲不走心。</div></details>
      <div class="src">🔗 <a href="https://www.qywin.cn/tjkt/tjkt4995.html" target="_blank">qywin.cn/tjkt/tjkt4995.html</a></div>
      <div class="note">适用：③ 高管团队文化共创(两天/十几人)——横向联结+纵向同频双轴，把价值观共识落成可行为准则手册，破冰段用故事+剧场而非幼稚游戏。</div>
    </div>'''

C3_2 = '''    <div class="hl">
      <div class="top"><span class="emoji">🚀</span><h3>新任高管前 90 天·听先于宣布+跨职能信任+运营节奏</h3><span class="cat">高管上任</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
      <p class="val">Saiyō 基于大量高管安置的实证模型。新领导前 90 天决定成败，最忌两错：未理解文化就推变革(显不信任)、建计划却孤立(跨职能摩擦)。高绩效 SaaS 领导做法：①听先于宣布——客户/团队/利益方访谈+产品沉浸+文化观察，先建尊重；②快速建跨职能信任——主动见市场/产品/工程/财务/客户成功/销售/CEO，问「什么在运转/什么不/你对我角色有何期待/我怎么早期支持你」，造共享目标；③清晰公开定义成功——讲清首聘/变更/指标/什么不变，降焦虑稳团队；④建立运营节奏——周领导力sync/QBR/路线图评审/升级仪式/沟通回路，增透明减意外；⑤早赢不越界——小可见改进建信心不颠覆；⑥强化中层——一线经理/组长能力缺口是scale最大障碍，主动评估补强；⑦以行代言建模文化(transparent/direct/humble/accountable)。90天框架：P1学(1-30听与看)、P2对齐(31-60建信任定成功)、P3执行(61-90显势不颠覆)。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">高管上任=先 1:1 听(客户/各职能/CEO)再宣布；主动建跨职能信任(问「我怎么早期支持你」)；早定成功标准+运营节奏(周sync/QBR)；早赢不颠覆；重点补强中层经理能力。</div></details>
      <div class="src">🔗 <a href="https://saiyo.io/insights/what-high-performing-saas-leaders-do-differently-in-the-first-90-days" target="_blank">saiyo.io/.../what-high-performing-saas-leaders-do-differently-in-the-first-90-days</a></div>
      <div class="note">适用：③ 新任高管/空降C-level上任90天——听先于宣布、跨职能信任、运营节奏、强化中层，把「权威」变「被信任」，避免上任即推变革毁信任。</div>
    </div>'''

# ---------------- ② 上下级 (5) ----------------
C2_1 = '''    <div class="hl">
      <div class="top"><span class="emoji">💬</span><h3>团队会议破冰·非尴尬问题+互换介绍+5-things工作流</h3><span class="cat">会议破冰</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">Atlassian(团队效能权威)：会议是建心理安全感的频繁可靠出口，好破冰让人「在个人层面相熟」从而建信任，而非信任摔/人结/荒岛问。新/新近团队会议破冰：①几枚不尴尬的破冰问题(让成员会前提交问题掌握分享主动权——最感激的事/想拥有的品质/僵尸末日抓三物)；②快速 show-and-tell(带一物件讲为何重要，远程更易)；③互换介绍(让人介绍他人而非自己，配对的更亮眼);④分享照片(主题如最爱假期/宠物);动机类：⑤planful agenda(会前发议程+轮换发言人+会前收Q&A+会后takeaways)；⑥celebrate wins(用进度原则开场提气)；⑦5-things workflow(每人说2在做的+2将做的+1别人以为你做但你没做的，切噪音)；⑧encourage fidgeting(动起来助专注)。强调：破冰问题避开敏感、不超会议10%、按熟悉度由浅入深。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">经理用 Atlassian 会议破冰=会前发议程+收Q&A；开场用非尴尬问题(或互换介绍/show-and-tell)建心理安全；用 5-things workflow 切噪音、celebrate wins 提气；破冰不超会议10%、避敏感。</div></details>
      <div class="src">🔗 <a href="https://www.atlassian.com/blog/teamwork/team-meeting-ideas" target="_blank">atlassian.com/blog/teamwork/team-meeting-ideas</a></div>
      <div class="note">适用：② 经理开新/新近团队会议——非尴尬破冰问题+互换介绍+5-things workflow+庆功，把例会变心理安全感基地，避信任摔/荒岛类幼稚破冰。</div>
    </div>'''

C2_2 = '''    <div class="hl">
      <div class="top"><span class="emoji">🧩</span><h3>团队融合与凝聚力·塔可曼阶段+乔哈里窗+鲜花拳头反馈</h3><span class="cat">团队融合</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">对象=经理/高级经理+核心成员(≤10人)。理论打底：塔可曼团队发展阶段(形成/风暴/规范/执行)帮助识别团队所处阶段与机遇；乔哈里窗(公开/盲点/隐藏/未知)强调反馈价值=信任建立。体验活动：①充分破冰——选卡牌代表当前团队状态+阶段模型评估；②鲜花拳头活动——安全环境给/收「鲜花(建设性肯定)」与「拳头(建设性批评)」，练反馈技巧、体验积极反馈力量；③生命故事·高峰低谷——讲个人生命高峰与低谷，建相互理解(不同经历塑价值观/协作态度)；现场促动：优势共享与组合+价值观融合+下一步行动计划，把学习变行动。特点：理论+体验结合，在安全环境练反馈而非游戏。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">经理带团队融合工作坊=先用塔可曼+乔哈里窗讲透理论，再用「鲜花拳头」在安全环境练给/收反馈、用「生命故事高峰低谷」建深层理解；最后优势组合+价值观融合+行动计画落地。</div></details>
      <div class="src">🔗 <a href="http://www.mingketang.com/nxk/43632.html" target="_blank">mingketang.com/nxk/43632.html</a></div>
      <div class="note">适用：② 经理带中小团队(≤10)融合工作坊——塔可曼+乔哈里窗理论打底、鲜花拳头练反馈、生命故事建理解，在安全环境练反馈而非幼稚游戏。</div>
    </div>'''

C2_3 = '''    <div class="hl">
      <div class="top"><span class="emoji">🌐</span><h3>远程入职 5C 框架·Connection→Culture→Clarity→Capability→Celebration</h3><span class="cat">远程入职</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">远程新人跨时区入职的最大坑=把信息投递当 checklist，缺「关系构建」。5C 框架把散乱信号变清晰人性体验：①Connection Before First Day——入职前私人欢迎信(引其背景)+经理15分钟视频通话+首周可视化地图，让人「未开屏已被看见」；②Culture Transmission——把文化嵌进日程(跨职能 peer 虚拟咖啡聊+公司叙事仪式直播+共享歌单)，至少首周1次、首月每周；③Clarity——入职前出「角色宪章」(主要产出/关键协作者/成功指标)，首周对齐通话+30天3个可衡量里程碑；④Capability——结构化学习(为每个角色定top3技能+短视频教程+微项目练手+导师反馈闭环)；⑤Celebration——标记首周/首交付/首演示等里程碑公开认可(虚拟徽章/团队huddle/领导手写条)，把任务流变共享故事。核心洞察：让远程新人「被看见」先于「看见屏」。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">经理/HR 远程入职=Connection(入职前私人信+经理15分钟视频+首周地图)→Culture(嵌文化触点)→Clarity(角色宪章+30天里程碑)→Capability(结构化学习+导师)→Celebration(里程碑公开认可)；把「被看见」放第一位。</div></details>
      <div class="src">🔗 <a href="https://blog.workhint.com/blog/the-5-cs-of-remote-onboarding" target="_blank">blog.workhint.com/blog/the-5-cs-of-remote-onboarding</a></div>
      <div class="note">适用：② 经理/HR 远程跨时区新人入职——5C 框架(连接/文化/清晰/能力/庆祝)，把信息投递变关系构建，远程新人「未开屏已被看见」建信任。</div>
    </div>'''

C2_4 = '''    <div class="hl">
      <div class="top"><span class="emoji">🤝</span><h3>远程团队建信任·停陈词滥调破冰+Buddy+watercooler频道</h3><span class="cat">远程信任</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">远程团队信任靠「非奶酪破冰」+系统化机制而非偶然。要点：#1 停止套路破冰——「周末怎么过」已被问烂，改用揭示新奇面的非陈词滥调问题(内疚小癖好/最近爱做的菜/在读什么/想瞬间学会的技能/最钦佩的人/最爱quote/超预期影视/10年前最爱乐队/最早记忆)；首次1:1 尤其关键——问「入职头两周最沮丧的是什么/什么不清/想要更多教练的是什么/明年最骄傲的一件事」。#2 投资 buddy system——51%远程公司这么做；给新人官方mentor(周/双周1:1)+每周随机配对2-3人非工作视频聊。#3 设专用非工作聊天频道——watercooler/宠物频道，补缺失的随意闲聊。#4 给非工作视频聊机会——看见表情听笑声建情感信任(affective trust)。底层：远程信任=持续1:1+非工作连接+可见关怀，非一次性游戏。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">远程团队信任=弃「周末怎么过」套路、用揭示面的非陈词滥调问题；建 buddy system(官方mentor+随机配对视频聊)；开 watercooler/宠物频道补闲聊；多给非工作视频聊建情感信任。</div></details>
      <div class="src">🔗 <a href="https://canopy.is/blog/2020/05/10/virtual-team-building-how-to-build-trust-in-a-remote-team/" target="_blank">canopy.is/blog/2020/05/10/virtual-team-building-how-to-build-trust-in-a-remote-team/</a></div>
      <div class="note">适用：② 远程/混合团队经理——停陈词滥调破冰、建 buddy system、开非工作频道、给视频聊，把远程信任变系统化机制而非靠游戏。</div>
    </div>'''

C2_5 = '''    <div class="hl">
      <div class="top"><span class="emoji">🔗</span><h3>跨部门团队 6 模板·Team Canvas+契约+个人用户手册</h3><span class="cat">跨部门破冰</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">跨部门协作难在沟通差/不信任/不对齐/动态乱，经理须先建 camaraderie 地基。Miro 6 模板(非游戏、专业框架)：①Team Canvas(90-120min)——对齐人/角色/目的/目标/价值观/需求/行动点，防对齐失导致项目失败；②Team Contract(1h)——讨论并议定团队规则与行为(什么in/out)，建心理安全；③Cross-Functional Team Setup(30min/人)——每人建含工作+轻松面的档案+技能可视化图，异步完成；④Fika DNA(30min/对)——瑞典咖啡聊天法，两人配对聊熟再为对方建 Fika 档案，可重复混搭配对；⑤Personal User Manual(30-60min/人)——分享沟通偏好/工作风格/价值观/趣事，让彼此尊重差异高效协作；⑥会议开场破冰(15-30min)——忘信任摔/荒岛问，用 Evolve Partners 10 个独特破冰(画图/Pictionary/最佳GIF)。强调：跨部门破冰用「理解彼此如何工作」替代私生活暴露。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">跨部门项目经理/经理=用 Team Canvas 对齐基础、Team Contract 定规则建心理安全、Personal User Manual 共享工作偏好、Fika 配对深聊；会议开场用轻破冰但弃信任摔类。</div></details>
      <div class="src">🔗 <a href="https://miro.com/blog/6-activities-templates-unite-cross-functional-team/" target="_blank">miro.com/blog/6-activities-templates-unite-cross-functional-team/</a></div>
      <div class="note">适用：② 经理/项目负责人带跨部门团队——Team Canvas+契约+个人用户手册+Fika，用「理解彼此如何工作」建信任对齐，弃荒岛/信任摔幼稚破冰。</div>
    </div>'''

NEW_3 = '\n'.join([C3_1, C3_2])
NEW_2 = '\n'.join([C2_1, C2_2, C2_3, C2_4, C2_5])

html = open(WALL, encoding='utf-8').read()

# 1) 注入③到 sec3 grid 关闭前
anchor3 = '    </div>\n\n  <!-- ============ ② 上下级 ============ -->'
assert anchor3 in html, 'sec3 anchor not found'
html = html.replace(anchor3, '    ' + NEW_3 + '\n    </div>\n\n  <!-- ============ ② 上下级 ============ -->', 1)

# 2) 注入②到 sec2 grid 关闭前
anchor2 = '    </div>\n\n  <footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>'
assert anchor2 in html, 'sec2 anchor not found'
html = html.replace(anchor2, '    ' + NEW_2 + '\n    </div>\n\n  <footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>', 1)

# 3) 更新 hero 与标签计数
html = html.replace('采集于 2026-08-10 ｜ 六轮补采 +9（03:06）',
                    '采集于 2026-08-10 ｜ 七轮补采 +7（21:50）', 1)
html = html.replace('<span class="tag">12 卡</span>', '<span class="tag">14 卡</span>', 1)
html = html.replace('<span class="tag">32 卡</span>', '<span class="tag">37 卡</span>', 1)

open(WALL, 'w', encoding='utf-8').write(html)

# 4) 写 run_newcards.tmp.html（先③后②，供 gen_run_page 分组）
run_tmp = '\n'.join([C3_1, C3_2, C2_1, C2_2, C2_3, C2_4, C2_5])
open(TMP, 'w', encoding='utf-8').write(run_tmp)

# 5) 校验
import re
cards = re.findall(r'<div class="hl">', html)
r3 = html.count('badge r3">高管间')
r2 = html.count('badge r2">上下级')
print('TOTAL_CARDS', len(cards), 'R3', r3, 'R2', r2)
print('footer_ok', '📌 本页由 yitong 沉淀整理 · 文化活动知识库' in html)
print('WROTE', WALL)
print('WROTE', TMP)
