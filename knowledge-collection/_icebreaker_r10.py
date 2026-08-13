# -*- coding: utf-8 -*-
"""破冰 第十轮补采 (R10, 2026-08-14): 追加 12 张新卡到累计墙 + 写临时卡文件。"""
import os, io

BASE = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(BASE, 'icebreaker', 'icebreaker.html')
TMP  = os.path.join(BASE, 'icebreaker', '.run_newcards.tmp.html')

# ---- 12 张新卡 (③ exec x6 在前, ② supervisor x6 在后) ----
def card(emoji, title, cat, rel, rel_txt, src_level, src_txt, val, howto, src, disp, note):
    return (
        '    <div class="hl">\n'
        f'      <div class="top"><span class="emoji">{emoji}</span><h3>{title}</h3>'
        f'<span class="cat">{cat}</span><span class="badge {rel}">{rel_txt}</span>'
        f'<span class="badge {src_level}">{src_txt}</span></div>\n'
        f'      <p class="val">{val}</p>\n'
        '      <details class="exec"><summary>怎么做</summary>'
        f'<div class="inner">{howto}</div></details>\n'
        f'      <div class="src">🔗 <a href="{src}" target="_blank">{disp}</a></div>\n'
        f'      <div class="note">适用：{note}</div>\n'
        '    </div>'
    )

cards = []
# ===== ③ 高管间 (exec) x6 =====
cards.append(card('🪂', '空降当高管,千万别急着"烧三把火"·90天信任重建计划', '空降高管融合', 'r3', '高管间', 'b2', '二手',
    '12年领导力培训实战（服务腾讯/阿里/OPPO）：空降高管第一道坎不是能力是距离，90%阵亡因信任没建立。90天信任重建计划：第一个月少说多听，先当学生再当先生——了解运作/性格/业务逻辑，不发表意见不改任何事；第二个月找痛点做小事建立初步信任——从团队反映最多最迫切但无人解决的小痛点切入；第三个月深度参与带团队打一场小胜仗——目的不是证明你厉害，而是证明「我们一起可以」，胜仗是最好的粘合剂。三个坑：急于证明、用前公司经验压人、只改不听。',
    '空降高管破局用「90天信任重建」——月1少说多听(当学生)/月2小痛点切入建初步信任/月3带团队打小胜仗粘合；避开急于证明、拿前公司经验压人、只改不听三坑。',
    'https://m.toutiao.com/article/7645692712221475328',
    'toutiao.com/article/7645692712221475328',
    '③ 空降高管/空降C-level融合——90天信任重建(听→小痛点→小胜仗)，胜仗是最好的粘合剂，避开急于证明与经验碾压。'))

cards.append(card('🎯', '空降高管·德鲁克"新官上任100天"法则·百日三部曲', '空降高管上任', 'r3', '高管间', 'b2', '二手',
    '遵循德鲁克「管理是关于人的，信任靠赢得而非职位赋予」思想。空降面对复杂局面、观望下属、挑剔上级，需「立信」计划。百日三部曲：第一个月倾听与诊断(不要烧火)——大量一对一，问三问「哪里做得最好/最大挑战障碍/若由你改一件是什么」，建信任摸脉络；第二个月寻找速赢(点燃第一把火)——基于诊断找快速见效、阻力小、展价值的切入点，集中资源打漂亮小胜仗立威信；第三个月推动关键变革(亮蓝图)——在信任威信基础上提方向/结构/流程变革，此时意见更有分量。',
    '空降高管用「德鲁克百日三部曲」——月1倾听诊断(三问摸底)/月2速赢立威/月3关键变革亮蓝图；先融入再改变，信任是渐进「立信」计划。',
    'https://m.toutiao.com/w/1855006227167244/',
    'toutiao.com/w/1855006227167244',
    '③ 空降高管百日融入——德鲁克思想(信任靠赢得)，倾听诊断→速赢立威→关键变革，先融入再改变。'))

cards.append(card('🔑', '空降高管存活率提升300%·三阶融合密码', '空降高管融合', 'r3', '高管间', 'b2', '二手',
    '牛企老板俱乐部调研：空降高管阵亡率70%，文化排斥68%/权力真空54%/资源饥渴43%。三阶融合密码：阶段一蜜月期(1-30天)文化解码——制《组织密码本》(非书面规则/决策暗线/人脉图谱)+3场咖啡会谈(高管与跨部门骨干非正式)+破冰工程(创始人带高管参加基层团建，如深夜烧烤摊浮出技术瓶颈)；阶段二攻坚期(31-90天)权力重构——双轨决策权(重大事项联席审批逐步过渡)+战功积分榜(短期成果立威)+老臣赋能(元老任高管导师)；阶段三融合期(91-180天)生态共建——三三制会议(主持跨三部门联席)+文化翻译官(双向认同员工作桥梁)+组织记忆工程(方法论植入知识库)。存活率可提至行业3倍。',
    '空降高管融合用「三阶密码」——蜜月期文化解码(组织密码本+咖啡会谈+破冰工程)/攻坚期权力重构(双轨决策+战功积分+老臣赋能)/融合期生态共建(三三制会议+文化翻译官+组织记忆)。',
    'https://www.niuqiclub.com/news/331921.html',
    'niuqiclub.com/news/331921.html',
    '③ 空降高管(老板视角)组织融合——三阶密码从文化解码到权力重构到生态共建，存活率可提至行业3倍。'))

cards.append(card('🧩', '空降高管水土不服·破局六步融合法', '空降高管融合', 'r3', '高管间', 'b2', '二手',
    '牛企老板俱乐部127家上市公司案例：空降高管三大坑——资源孤岛(跨部门难调动)、文化排异、被架空。破局六步：①文化解码90天(10场非正式茶话会+研读大事记+绘隐形权力地图，如CEO食堂轮桌摸清决策链)②信任账户3-3-3模型(3速赢+3关键人物+3次深度倾听)③跨维沟通密码——向上用数据说话每月预期管理报告、平行发起跨部门创新实验室、向下设「跟我学」开放周④文化嫁接术(保留工匠精神内核接变革)⑤变革缓冲带(6-9月过渡期双轨制)⑥融合温度计(每月测决策效率/协作指数/人才稳定)。董事会护航：避免救世主幻觉、设文化适配KPI(权重30%)。',
    '空降高管破局用「六步融合」——文化解码90天+信任3-3-3模型+跨维沟通(向上数据/平行实验室/向下开放周)+文化嫁接+双轨缓冲+融合温度计；董事会设文化适配KPI。',
    'https://www.niuqiclub.com/news/292489.html',
    'niuqiclub.com/news/292489.html',
    '③ 空降高管融合——六步法从文化解码到跨维沟通到董事会护航，避资源孤岛/文化排异/被架空三坑。'))

cards.append(card('🚀', 'The First 100 Days · 新任高管结构化入职框架', '高管入职', 'r3', '高管间', 'b2', '二手',
    '高管招聘顾问机构(JR Partners)前100天入职框架：Pre-Day-One综合战略简报+角色范围与成功指标+关键引见；Days1-30倾听之旅与利益相关者映射——与直接下属/同侪高管/跨职能一对一，识别外部伙伴客户监管，映射权力结构与关键决策者，观察团队动态与不成文规则(积极倾听的高管成功概率高4倍)；Days31-60诊断——整合倾听与文档数据做SWOT、定优先中高影响举措(初期战略错配致30%失败)；Days61-100早期胜利与100天路线图——交付速赢、内外沟通成功、发布12-18月战略路线图；Day100+正式评审+360反馈(结构化评审提升成功率25%)。',
    '新任高管入职用「100天框架」——Pre准备+首30天倾听之旅画权力图+31-60诊断SWOT+61-100速赢与路线图+第100天360评审；积极倾听的高管成功率高4倍。',
    'https://www.jrgpartners.com/first-100-days-how-onboard-new-executive-success',
    'jrgpartners.com/.../first-100-days-how-onboard-new-executive-success',
    '③ 新任高管/C-level入职——100天结构化框架(倾听→诊断→速赢→路线图→评审)，首月积极倾听者成功率高4倍。'))

cards.append(card('📋', 'The Ultimate Executive Onboarding Checklist · 入职清单', '高管入职', 'r3', '高管间', 'b2', '二手',
    '高管寻聘机构(Decipher Group)入职清单，引用麦肯锡(3/4高管因入职不足感准备不足)与HBR(应视为「integration」而非onboarding，可缩短1/3达产时间)。阶段：Pre-boarding(接offer即启动，meet-and-greets/介绍call)+First Day(关系建立为主，Quelch主张首90小时听尽所需)+First 30天learn&listen路演(roadshow面对面走访多地)+skip-level会议(无直属经理在场听洞察)+焦点小组(focus groups)+识别支持者与高潜+First 60/90/100天角色宪章(role charter)与100天计划(按月拆解)+6/12月小胜与360评估。远程入职靠全员会+反馈机制建透明。',
    '高管入职用「清单」——接offer即pre-boarding+首30天roadshow走访+skip-level与焦点小组听洞察+首60天出角色宪章+100天计划按月拆+6/12月360评估；视入职为integration而非orientation。',
    'https://deciphergroup.co.nz/blogs/the-ultimate-executive-onboarding-checklist',
    'deciphergroup.co.nz/.../the-ultimate-executive-onboarding-checklist',
    '③ 新任高管入职(组织/HR视角)——结构化清单(roadshow+skip-level+角色宪章+100天计划)，视入职为integration，缩短达产时间。'))

# ===== ② 上下级 (supervisor) x6 =====
cards.append(card('🧭', '新任主管最常犯的7个带人错误与修正', '新主管上任', 'r2', '上下级', 'b2', '二手',
    '台湾 HR 顾问：新任主管处在组织连接点，既转译策略又带回一线风险。7错：①只管部属不管向上对齐②跨部合作先怪人③在部属前抱怨上级④一次改所有事⑤前30天否定前任⑥为展魄力大幅改组⑦不授权变瓶颈。90天存活指南：1-30天先理解再调整(与上/每位部属/跨部门伙伴一对一访谈，完成角色期待清单+团队盘点+90天目标)；31-60天建管理节奏(固定1:1/会议/追踪/反馈，明确决策权与授权，选1-2小问题改善)；61-90天交付并培养可持续(标准化有效做法、授权代理人)。四问评估：团队知最重要目标?每人清责任权限?问题能早提出?主管暂离仍运转?',
    '新任主管用「90天指南」——1-30天倾听盘点(上/部属/跨部门一对一+三产出)/31-60天建节奏(1:1+反馈+小改善)/61-90天交付授权；避开7错(只管部属/一次改全/否定前任/不授权)。',
    'https://lucentheart.tw/new-manager-common-mistakes',
    'lucentheart.tw/new-manager-common-mistakes',
    '② 新任/新晋升主管上任——90天三阶段(理解→节奏→交付)，避开7个带人错误，先对齐上级与跨部门再谈改革。'))

cards.append(card('👂', 'New Manager 90-Day Plan · Listening Tour 优先', '新经理上任', 'r2', '上下级', 'b2', '二手',
    'SaaS 流程工具团队：新经理独特挑战——同时学环境又担领导责，50%外部高层招聘18月内失败(Leadership IQ)。首30天铁律：别领导，先听。Listening Tour——每直属下属首两周45-60分钟结构化一对一，五问「什么在运转良好/最挫的事/希望我懂的/该知道的/改一件是什么」；Meet 关键跨职能干系人；Review OKR与绩效数据；建周1:1节奏；不做重大决策。31-60天综合对齐(与己上级对齐+2-3速赢+澄清团队规范)；61-90天执行(速赢+个人职业对话+会议节奏)。权威来自四源：能力信号/跟进兑现/公平流程/透明。',
    '新经理用「倾听优先」——首30天Listening Tour(每下属45-60分五问+跨职能干系人+不决策)/31-60综合对齐+61-90执行速赢；权威靠能力信号+跟进兑现+公平+透明。',
    'https://checkflow.io/blog/90-day-onboarding-plan',
    'checkflow.io/blog/90-day-onboarding-plan',
    '② 新任经理上任——Listening Tour 优先于领导，首30天听透团队再改，权威靠兑现与公平而非职位。'))

cards.append(card('🤝', '7 Things New Managers Should Know · 赢得团队信任7杠杆', '新经理建信任', 'r2', '上下级', 'b2', '二手',
    '新经理赢得团队信任7杠杆：①清晰(角色清晰度)②可预测(跟进兑现率)③公平(申诉率)④能力(客观影响)⑤可得性(响应SLA)⑥互惠(同伴NPS)⑦校准(晋升准确度)。实操：用「Decision/Why/Alternatives/Monitoring」模板做透明决策 framing 减事后猜疑；从年度叙事转3月微评(每10周数据包)；首周蓝图(5场30分1:1+系统走查+公开「意图变更」备忘)；8-30天校准retro(经理抛团队假设邀纠正)；60-90天文档化发展计划+透明晋升节奏；失误恢复四步(公开承认+纠正时限+跟进+记录)。每杠杆可链HR KPI。',
    '新经理建信任用「7杠杆」——清晰/可预测/公平/能力/可得性/互惠/校准；决策用DWAM模板透明framing、首周5场1:1+公开意图备忘、失误公开恢复四步；每杠杆链HR KPI。',
    'https://leadershippublishing.com/7-things-new-managers-should-know',
    'leadershippublishing.com/.../7-things-new-managers-should-know',
    '② 新任经理建团队信任——7信任杠杆+DWAM透明决策+首周倾听蓝图+失误公开恢复，可量化成HR KPI。'))

cards.append(card('🏛️', '新晋管理者如何快速胜任新角色', '新晋管理者', 'r2', '上下级', 'b2', '二手',
    '内训课框架：①建立影响力联盟3关键——找关键盟友/用共同利益凝聚/逐步扩影响圈(新总监3月建全公司联盟案例)；②规避5大隐性问题——不急于否定前任/不唯表面数据/不让团队觉「空降指挥」(先听后行)/不回避难沟通者/只说不做；③双向协调5法——上到下翻译目标、下到上传声、内到外破部门墙、知到行确保传达、议到决有责任人；④STARS模型评估组织(初创/转型/加速/重组/维持)；⑤3R文化融入(Respect尊重/Recognize识别/Reshape重塑，空降3月融老牌文化案例)；⑥5项对话避期望陷阱(与上级/团队/平级/客户/自己)。',
    '新晋管理者用「影响力联盟+STARS+3R」——找关键盟友扩影响圈、STARS评组织阶段、3R文化融入(尊重/识别/重塑)、5项对话对齐期望(上级/团队/平级/客户/己)；不急于否定前任、先听后行。',
    'https://www.qiyingschool.com/neixunke/447312.html',
    'qiyingschool.com/neixunke/447312.html',
    '② 新晋管理者胜任新角——影响力联盟+STARS诊断+3R文化融入+5项期望对话，先听后行不空降指挥。'))

cards.append(card('🌱', '空降HRM打破孤立困局·四步破局', '空降融入', 'r2', '上下级', 'b2', '二手',
    'HR 实战答疑案例：空降HRM进家族色彩小团体文化公司被孤立。破局四步：一建立信任融入为先——深解历史/文化/关键人背景，日常同理沟通，从小事(解员工小问题/参团队活动)展价值；二精准向上管理——与顶头上司(老板妹妹)深度1:1明确期望与优先级，提方案附带实施+效果+挑战应对显专业；三逐步推进柔性变革——小步快跑选1-2部门试点成功再推广，正面激励为主；四建团队聚共识——午餐茶歇一对一破隔阂，策划拓展/主题分享增凝聚。核心：耐心+智慧+策略，先信任再变革。',
    '空降管理者破孤立用「四步」——建立信任(同理+小事展价值)/精准向上管理(深度1:1明确期望+带方案)/小步试点柔性变革/一对一+团建聚共识；先融入再变革。',
    'https://www.hrloo.com/rz/14756918.html',
    'hrloo.com/rz/14756918.html',
    '② 空降管理者(尤HR/职能岗)破孤立——建立信任+向上管理+小步试点+一对一聚共识，先信任再变革。'))

cards.append(card('🪜', '"空降兵"如何管理新团队·向上管理先于向下', '空降融入', 'r2', '上下级', 'b2', '二手',
    '民企「空降兵」失败率超75%。破局从向上管理开始——很多空降兵一到岗就大动干戈，恰是最大阻碍。向上管理：清晰了解老板意图、确认职责目标，入职前多次确认预期，量化阶段目标/节点/核验，管理老板预期(实事求是评估避免不切实际期望)，非正式沟通(电梯食堂见缝插针汇报)让老板有掌控感；向下管理：让员工对目标共识、对规则清晰认知，知人善任合理分配。案例：营销副总张总入职前确认预期+入职后深入沟通量化目标+非正式汇报，半年即融入带队打胜仗。',
    '空降兵管理新团队——先向上管理(确认老板意图/量化目标/管理预期/非正式汇报)再向下管理(目标共识+规则清晰+知人善任)；第一件事不是向下而是向上。',
    'http://www.gcmag.cn/web/news/?4602.html',
    'gcmag.cn/web/news/?4602.html',
    '② 空降管理者接管新团队——向上管理(对齐老板预期)先于向下管理(目标共识规则)，避开一到岗就大动干戈。'))

sec3_block = '\n'.join(cards[0:6])
sec2_block = '\n'.join(cards[6:12])
all_block  = '\n'.join(cards)

# ---- 读墙 ----
html = io.open(WALL, encoding='utf-8').read()
existing_r3 = html.count('badge r3')
existing_r2 = html.count('badge r2')

# 追加 ③ 到 sec3 grid (在 <div class="sec sec2"> 之前的最后一个 </div> 内)
before_sec2, after_sec2 = html.split('<div class="sec sec2">', 1)
idx = before_sec2.rfind('</div>')
new_before_sec2 = before_sec2[:idx] + '\n' + sec3_block + '\n  ' + before_sec2[idx:]
html2 = new_before_sec2 + '<div class="sec sec2">' + after_sec2

# 追加 ② 到 sec2 grid (在 <footer> 之前的最后一个 </div> 内)
before_footer, after_footer = html2.split('<footer>', 1)
idx2 = before_footer.rfind('</div>')
new_before_footer = before_footer[:idx2] + '\n' + sec2_block + '\n  ' + before_footer[idx2:]
html3 = new_before_footer + '<footer>' + after_footer

# 更新 sec3 / sec2 标签计数（第一个 tag=sec3, 第二个=sec2）
import re
def repl_tag(m, seen=[0]):
    seen[0]+=1
    if seen[0]==1:
        return f'<span class="tag">{existing_r3+6} 卡</span>'
    else:
        return f'<span class="tag">{existing_r2+6} 卡</span>'
html3 = re.sub(r'<span class="tag">\d+ 卡</span>', repl_tag, html3)

# 更新 hero 行
html3 = html3.replace('采集于 2026-08-13 ｜ 九轮补采 +7（R9）｜',
                      '采集于 2026-08-14 ｜ 十轮补采 +12（R10）｜')

io.open(WALL, 'w', encoding='utf-8').write(html3)

# 写临时卡文件
io.open(TMP, 'w', encoding='utf-8').write(all_block)

# 校验
new_r3 = html3.count('badge r3')
new_r2 = html3.count('badge r2')
print(f'OK wall updated: r3 {existing_r3}->{new_r3}, r2 {existing_r2}->{new_r2}, total {existing_r3+existing_r2}->{new_r3+new_r2}')
print(f'TMP written: {len(all_block)} bytes, cards={all_block.count(chr(60)+"div class=\"hl\""+chr(62))}')
