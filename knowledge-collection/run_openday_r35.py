# -*- coding: utf-8 -*-
# Open Day 三十五轮补采（r35, 2026-09-04）+11 卡：1 ③高管间(WAIC全球治理) + 10 ②上下级(WAIC市民开放日/税务×3/消防×2/生态环境监测×2/人社×2)
# 全部一手（政府/官方媒体源），零 peer/朋友向；Open Day 域过滤已排除 IR/资本/证券向。
import re, os, json

WS = r"C:\Users\v_yitcai\WorkBuddy\20260728154244"
KC = os.path.join(WS, "knowledge-collection")
HTML = os.path.join(KC, "openday", "openday.html")
IDX = os.path.join(KC, "index.json")
OB_SUM = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\openday\OpenDay-开放日-知识卡汇总.md"
OB_IDX = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
OB_RUN = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\openday\runs\OpenDay-2026-09-04-第三十五轮-知识卡.md"
GH = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday.html"
RUN_DATE = "20260904"
RUN_PAGE = "openday/runs/openday-2026-09-04-r35.html"
GH_RUN = f"https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/{RUN_PAGE}"
MAP = os.path.join(KC, "lexiang-entry-map.json")
TOPIC_TXT = os.path.join(KC, "last-topic.txt")

cards = [
 dict(emoji='🌐', title='2026世界人工智能大会暨人工智能全球治理高级别会议（29国上海签署成立世界人工智能合作组织WAICO·全球治理新体系）', cat='AI全球治理高层开放日',
      rel='r3', src='一手', src_cls='b1',
      url='https://en.ce.cn/main/latest/202607/t20260719_3094765.shtml',
      val='WAIC 2026（7.17-20 上海）以“智能伙伴 共创未来”为主题，首次创办 WAIC Academic 国际学术会议（图灵奖得主姚期智任主席）；闭幕前夕 29 国在沪签署成立世界人工智能合作组织（WAICO），旨在构建基于对话、互信、共担责任的国际 AI 合作新体系。中外嘉宾 1400+（含图灵奖得主、两院院士、科技高管、风投），聚焦全球 AI 治理与安全、世界模型与智能体底层标准、弥合全球数字智能鸿沟、人形机器人与数字资产规范。中国提出《人工智能全球治理行动计划》，倡导以人为本、智能向善，向全球南方输出气象预警 MAZU 等 AI 公共产品。',
      how='把“AI 大会”做成全球治理层开放合作场——以“高级别会议+WAICO 成立+学术会议”三层把国家/国际组织/企业高管聚到同一张开放桌；用“以人为本、智能向善”锚定开放日价值，把技术竞争变可协作的全球公共议题；以“向发展中国家输出 AI 能力”把开放日升级为南南合作平台，是国际组织式高管开放日向范本（中国经济网/新华社一手）。',
      note='③ AI 全球治理高层开放日（中国经济网/新华社一手），大会秘书处以全球治理推动者姿态，29 国政要/国际组织/跨国科技企业高管围绕 AI 安全与治理围坐对话（高管间/政企学协作向，非 IR/证券向）。'),
 dict(emoji='🤖', title='WAIC 2026 公众开放日运营（7.18-20 全时段对公众开放·馆内+街区+全城三级沉浸体验+6条AI城市漫步）', cat='AI展会公众开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.ce.cn/xwzx/gnsz/gdxw/202607/t20260716_3090065.shtml',
      val='2026 WAIC 设论坛会议/展览展示/评奖赛事/应用体验/创新孵化/招才引智六大板块，140 余场论坛、1100+ 企业、3000+ 展品、300+ 全球首发；7.18-7.20 全时段对普通公众开放（展览票 168 元/人，Hi WAIC APP 实名购票）。以“伴游记·我的摩登拍档”为主题构建馆内（世博展览馆全产业链）+街区（张江科学会堂硬核技术）+全城（西岸亲子互动）三级沉浸式体验体系，联合 24 个城市地标推出 6 条 AI 城市漫步主题路线，夜场办青少年 AI 音综；世博/张江/西岸三馆免费接驳巴士互通。外交部人工智能事务协调员提三期待：共促团结、共谋发展、共促行动。',
      how='把“AI 大会”做成市民可逛的开放日——以“三级沉浸体验+全城漫步路线+夜间特色活动”把专业展会变全民科普；用单一官方 APP 实名购票+人脸识别双核验解决大客流安全与黄牛问题；以“免费接驳+分馆分流”降低参与门槛，是大型科技展会公众开放日向可复制模板（中国经济网一手）。',
      note='② AI 展会公众开放日（中国经济网一手），大会主办方以城市服务者姿态，市民/学生/亲子家庭走进 AI 展馆与城市漫步路线、零距离体验前沿科技。'),
 dict(emoji='🧾', title='六安市税务局2026“政府开放日”（税企面对面·办税服务厅沉浸式体验+政策宣讲+座谈纳谏）', cat='税务局政务开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://anhui.chinatax.gov.cn/art/2026/4/13/art_9564_1302544.html',
      val='4.8 裕安区办税服务厅，六安市税务局以“税企面对面 服务零距离”为主题办政府开放日，邀人大代表、政协委员、纳税人及涉税中介代表等 10 余位“体验官”走进大厅，依次走咨询辅导台、自助办税区、综合窗口、征纳互动区，现场看新电子税务局高频业务演示；政策宣讲拆解增值税法及实施条例新变化（税率影响定价、留抵退税现金流红利）；座谈环节企业代表围绕跨区域预缴、农产品收购发票等踊跃提问，税务人员现场逐一解答并记录诉求。搭建税企沟通桥梁、增进互信。',
      how='把“税务开放日”做成税企透明+纳谏闭环——以“实地走+真体验+深座谈”三段式把办税流程变可感可监督；用“体验官”角色让纳税人从被动听变主动查；以“现场答疑+诉求记录”把开放日从展示升级为听意见促遵从，是市级税务局阳光政务范本（安徽税务/皖西日报一手）。',
      note='② 税务局政务开放日（安徽税务/皖西日报一手），税务部门领导以营商环境服务者姿态，人大代表/政协委员/纳税人/中介代表走进办税厅、评议服务。'),
 dict(emoji='🧾', title='泾源县税务局“税务开放日·税费服务体验师”（小微企业/中介沉浸式体验智慧办税）', cat='税务局政务开放日',
      rel='r2', src='一手', src_cls='b1',
      url='http://ningxia.chinatax.gov.cn/art/2026/4/27/art_12063_385843.html',
      val='泾源县税务局开展“税务开放日·税费服务体验师”活动，邀小微企业代表及涉税专业服务机构人员担任“税费服务体验师”走进办税场所，税务干部讲解综合窗口、发票管理、自助办税、咨询辅导、“非接触式”体验区等功能分区；体验师现场观摩并模拟办纳税申报、发票领用、优惠咨询等高频业务，在指导下登录电子税务局完成个税申报、数电票代开等 10 余项操作；围绕政策落实、流程优化提 3 条建议，工作人员现场回应、部分诉求当场协调解决，打通税企沟通“最后一公里”。',
      how='把“税务开放日”做成体验师制度——以“聘任体验师+真上手操作”把纳税人变税务流程的亲历检验员；用“非接触式办税体验区”集中展示线上办便捷；以“现场提建议+当场协调”短闭环提升满意度，是县域税务局税费服务提质范本（宁夏税务官网一手）。',
      note='② 税务局政务开放日（宁夏税务官网一手），税务部门领导以服务者姿态，小微企业/涉税中介体验师走进办税厅、实操并反馈。'),
 dict(emoji='🧾', title='海晏县税务局“税务开放日”（智慧税务零距离·24小时自助区+一日税务体验师+税企面对面）', cat='税务局政务开放日',
      rel='r2', src='一手', src_cls='b1',
      url='http://qinghai.chinatax.gov.cn/hbz/gdtp/202605/a820e1aa441047aaa8f2df4df663684b.shtml',
      val='海晏县税务局邀辖区财务负责人、涉税中介代表走进办税厅，参观“24 小时自助办税区”现场演示代开数电发票、完税证明打印等“非接触式”办理（该局自助渠道可办业务占比 95%、单笔缩至 3-5 分钟）；在“一窗通办”窗口代表化身“一日税务体验师”通过金三系统、慧办平台完成发票审批、额度调整，认识账目清晰对效率的重要性；税企座谈结合税费优惠解答融合场景开票、留抵退税、社保费缴纳等热点，纳税人提 5 条建议。提出把“开放日”转化为“常态日”。',
      how='把“税务开放日”做成常态日雏形——以“24 小时自助区+一日体验师”双场景把智慧税务成果变可触可感；用“一窗通办真操作”让纳税人懂内部严谨流程；以“开放日→常态日”理念把一次性活动变持续服务，是县域税务局智慧税务开放日向范本（青海税务官网一手）。',
      note='② 税务局政务开放日（青海税务官网一手），税务部门领导以服务者姿态，财务负责人/中介代表体验智慧办税、对话优化。'),
 dict(emoji='🚒', title='儋州消防“消防站开放日”（市民家庭零距离·装备讲解+云梯升空+灭火实操+夏季防火普法）', cat='消防站开放日',
      rel='r2', src='一手', src_cls='b1',
      url='http://hi.119.gov.cn/info/1453/37393.htm',
      val='7.17 儋州消防开展“消防站开放日”，迎来辖区市民家庭参观。消防员带看消防车、逐一打开装备舱讲解破拆工具、防蜂衣、捕蛇器等；互动体验环节部分市民在保护下登登高平台云梯车升至数十米高空体验高空救援视角，试穿厚重的灭火防护服；消防员讲灭火器“提拔握压”口诀并演示油盆灭火；结合夏季风险讲电动车防火、楼道清杂物、火场弯腰捂鼻逃生，提醒暑期远离明火牢记 119。以“参观+体验+实操”播下安全意识种子。',
      how='把“消防站开放日”做成亲子安全课——以“装备开舱+云梯升空+灭火实操”三段体验把消防变可触摸的勇敢；用“提拔握压”口诀+油盆真灭火让知识变肌肉记忆；以家庭为单位扩大覆盖面，是海南消防站公众开放日向范本（海南消防官网一手）。',
      note='② 消防站开放日（海南消防官网一手），消防部门领导以公共安全守护者姿态，市民家庭/亲子走进营区、学消防练逃生。'),
 dict(emoji='🚒', title='萍乡消防队站开放日（常态化·面向社会群众/亲子/研学/留守儿童·沉浸式科普+实景教学）', cat='消防站开放日',
      rel='r2', src='一手', src_cls='b1',
      url='http://jx.119.gov.cn/news-show-33732.html',
      val='萍乡支队依托全市消防救援站、文明实践消防宣教阵地常态化开展队站开放日，面向群众、亲子家庭、暑期研学团体、留守儿童群体敞开营区。参观有序走进营区环境、宿舍内务、荣誉展厅感受纪律作风；听消防员讲灭火防护服、空气呼吸器、破拆工具、救援绳索功能用途；互动环节踊跃试穿试戴、亲手操作；宣教人员结合夏季特点讲家庭隐患排查、电动车充电、暑期防火防溺水、初期扑救、疏散逃生，手把手教灭火器/水带规范操作。支队将持续常态化推进、精准对接不同群体需求。',
      how='把“消防站开放日”做成常态化分群课——以“常态化敞开营区+分群定制（亲子/研学/留守儿童）”把一次性活动变持续安全教育；用“内务荣誉展厅+装备讲解+实操”结构建立纪律与专业信任；以“精准对接群体需求”提升覆盖面，是江西消防站公众开放日向可复制模板（江西消防官网一手）。',
      note='② 消防站开放日（江西消防官网一手），消防部门领导以安全守护者姿态，群众/亲子/研学/留守儿童走进队站、学技能强意识。'),
 dict(emoji='🌿', title='安徽省生态环境监测中心“美丽中国我先行 感知监测践低碳”公众开放日（小学生+家长·监测无人机/声级计/水质显色实验）', cat='生态环境监测站开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://sthjt.ah.gov.cn/hbzx/gzdt/stdt/123482671.html',
      val='8.26 安徽省生态环境监测中心办“美丽中国我先行 感知监测践低碳”主题环保设施开放日，合肥湖东小学四年级学生和家长经生态环境部“环保设施向公众开放”小程序预约参与。科普宣讲学《公民生态环境行为规范十条》；重污染天气预报预警中心讲大气污染物、空气质量预报、会商研判；仪器设备观摩展示苏玛罐气体采集、环境监测无人机、风速仪；噪声监测用声级计实时数值讲危害与限值；实验室沉浸式体验总磷显色、酚酞显色、水质酸碱测试等科普实验，学生动手实操；设环保科普竞答颁荣誉证书。让抽象生态知识可视化可感知。',
      how='把“监测站开放日”做成青少年生态实验室——以“科普+观摩+实验+竞答”四段把环境监测变可动手的科学；用“环保设施向公众开放”小程序预约保证有序参与；以“水质显色实验+声级计实时数值”把数据变直观现象，是省级监测中心公众开放日向范本（安徽生态环境厅官网一手）。',
      note='② 生态环境监测站开放日（安徽生态环境厅官网一手），生态环境部门领导以公共科普者姿态，小学生/家长走进监测一线、读懂蓝天碧水数据。'),
 dict(emoji='🌿', title='奉新县生态环境局“政府开放日”（零距离探秘环保设施·走进监测站看总磷/COD快速测定+PH测试）', cat='生态环境监测站开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.fengxin.gov.cn/fxxrmzf/jcdt79/pc/content/2087718499426095104/content_2087718499426095104.html',
      val='8.12 宜春市奉新生态环境局以“凝聚绿色共识，共建美丽奉新——零距离探秘环保设施”为主题办政府开放日，邀社区工作者及居民代表走进生态环境局。业务负责人介绍职能与今年以来生态环保总体情况；围绕空气质量监测、水环境治理、噪声污染防治讲法规与常识，结合蓝天碧水净土保卫成效解读饮用水源保护、垃圾分类、农村污水治理等政策；代表走进奉新生态环境监测站，参观理化实验室、天平室、样品室、大型仪器分析室，工作人员讲总磷/COD 快速测定消解仪原理并演示 PH 计测水样全过程，系统介绍空气废气/水质/噪声监测方法。搭建部门与公众沟通桥梁。',
      how='把“监测站开放日”做成政务公开+科普双课——以“政策宣讲+监测站实地参观”把环保工作从幕后走到台前；用“总磷/COD 快速测定+PH 计实测”让监测数据产生过程可感；以“梳理落实意见建议”短闭环提升透明度，是县域生态环境局政府开放日向范本（奉新县政府官网一手）。',
      note='② 生态环境监测站开放日（奉新县政府官网一手），生态环境部门领导以公共科普者姿态，社区工作者/居民代表走进监测站、读懂环保数据。'),
 dict(emoji='💼', title='昌乐县人社局政府开放日（“春风送岗”·就业综合体集政策展示/实操体验/互动咨询/意见征集）', cat='人社局政务开放日',
      rel='r2', src='一手', src_cls='b1',
      url='http://www.changle.gov.cn/ztzl/zfkfy/hdkzqk/202603/t20260302_715134.html',
      val='昌乐县人社局 2 月“政府开放日”在宝都乐就业综合体办专题开放日，以“春风送岗，服务可感”为主线把传统招聘升级为集政策展示、实操体验、互动咨询于一体的综合平台。设“业务全景展示区”（展板电子屏呈现就业/社保/人才/劳动关系流程成果）、“智慧服务体验区”（专人引导现场操作“码上就业”平台感受数字化便捷）、“技能赋能互动角”（讲师微型技能展示体验教学）、“政策咨询面对面”（就业/工伤/仲裁骨干一对一权威解答）；现场设“意见征集台”当日收有效反馈 10 余条。',
      how='把“人社开放日”做成就业服务综合体——以“展示+体验+咨询+征集”四区把招聘变可感可办的综合场景；用“码上就业平台现场操作”让数字化服务被亲历；以“意见征集台”把开放日变民情直通车，是县人社局政务公开范本（昌乐县政府官网一手）。',
      note='② 人社局政务开放日（昌乐县政府官网一手），人社部门领导以就业服务者姿态，市民/企业代表走进就业综合体、体验人社全流程服务。'),
 dict(emoji='💼', title='青山区人社局“双主任开放日”（打破机关壁垒·主任办公桌搬进社银网点/就业站/商圈·沉浸式办公+面对面解惑）', cat='人社局政务开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.qsq.gov.cn/xwdt/xwdt_bmdt/202605/t20260520_918421.html',
      val='青山区人社局创新“双主任开放日”系列，打破机关办公壁垒，把主任办公桌搬进社银一体化服务网点、家门口就业服务站、商圈，以沉浸式办公、面对面解惑、实打实办事推动人社服务从幕后到台前。社保主任带骨干化身“政策讲解员/业务指导员”靠前接待，围绕灵活就业参保、退休待遇核算、社保关系转移用案例拆解，对老年/行动不便群体一对一帮扶操作自助终端；同步“9 为您服务”就业服务中心主任开放日聚焦就业创业，主任带队联合社区/企业围坐深挖求职意愿与用工难题，现场搭供需对接桥，设政策咨询/岗位推介/技能培训报名区，精准解读创业担保贷款、公益性岗位、技能培训补贴。',
      how='把“人社开放日”做成下沉式主任办公——以“双主任开放日”把领导办公桌搬到社银网点/就业站/商圈，破除机关壁垒；用“沉浸式办公+围坐交流”让政策制定者直面群众诉求；以“适老一对一帮扶+现场供需对接”实打实办事，是区人社局服务前移范本（青山区政府官网一手）。',
      note='② 人社局政务开放日（青山区政府官网一手），人社部门领导以服务者姿态，群众/企业/求职者围坐主任开放日、直诉诉求现场办。'),
]

# ---- dedup guard against index.json urls ----
idx_data = json.load(open(IDX, encoding='utf-8'))
existing_urls = set()
for x in idx_data:
    u = x.get('url')
    if u: existing_urls.add(u.strip().lower().replace('https://','').replace('http://','').replace('&amp;','&').rstrip('/'))
before = len(idx_data)
kept, dropped = [], []
for c in cards:
    nu = c['url'].strip().lower().replace('https://','').replace('http://','').replace('&amp;','&').rstrip('/')
    if nu in existing_urls:
        dropped.append(c['title']); print('DEDUP drop:', c['title'])
    else:
        kept.append(c)
cards = kept
print('dedup: kept=%d dropped=%d' % (len(cards), len(dropped)))

def card_html(c):
    url_disp = c['url'].replace('https://','').replace('http://','')
    rel_text = '上下级' if c['rel']=='r2' else '高管间'
    return (f'    <div class="hl">\n'
            f'      <div class="top"><span class="emoji">{c["emoji"]}</span><h3>{c["title"]}</h3>'
            f'<span class="cat">{c["cat"]}</span><span class="badge {c["rel"]}">{rel_text}</span>'
            f'<span class="badge {c["src_cls"]}">{c["src"]}</span></div>\n'
            f'      <p class="val">{c["val"]}</p>\n'
            f'      <details class="exec"><summary>怎么做</summary><div class="inner">{c["how"]}</div></details>\n'
            f'      <div class="src">🔗 <a href="{c["url"]}" target="_blank">{url_disp}</a></div>\n'
            f'      <div class="note">适用：{c["note"]}</div>\n'
            f'    </div>')

cards2 = [c for c in cards if c['rel']=='r2']
cards3 = [c for c in cards if c['rel']=='r3']
n2, n3 = len(cards2), len(cards3)
assert n2+n3 == len(cards), (n2,n3,len(cards))
print(f'cards total={len(cards)} | ②={n2} ③={n3}')

# ===== 1) summary wall openday.html =====
html = open(HTML, encoding='utf-8').read()
cur2 = html.count('badge r2">上下级<')
cur3 = html.count('badge r3">高管间<')
print(f'current wall: ②={cur2} ③={cur3} (hl divs={html.count(chr(34)+"hl"+chr(34))})')

marker = '<div class="sec sec3">'
idx = html.find(marker)
assert idx != -1, 'sec3 marker not found'
html = html[:idx] + '\n'.join(card_html(c) for c in cards2) + '\n' + html[idx:]
j = html.find('<div class="sec sec3">')
k = html.find('<div class="hl">', j)
assert k != -1, 'no hl in sec3'
html = html[:k] + '\n'.join(card_html(c) for c in cards3) + '\n' + html[k:]

m2 = re.search(r'(<div class="sec sec2">.*?<span class="tag">)(\d+)( 卡</span>)', html, re.S)
assert m2, 'sec2 tag not found'
html = html[:m2.start()] + m2.group(1) + str(cur2+n2) + m2.group(3) + html[m2.end():]
m3 = re.search(r'(<div class="sec sec3">.*?<span class="tag">)(\d+)( 卡</span>)', html, re.S)
assert m3, 'sec3 tag not found'
html = html[:m3.start()] + m3.group(1) + str(cur3+n3) + m3.group(3) + html[m3.end():]

# hero append 三十五轮 segment after 三十四轮 tail
HERO_ANCHOR = '三十四轮补采 2026-09-04(+7：梅江区检法开放日/分宜县气象局政府开放日/桐城市气象局政府开放日/上海国企开放日"企妙星期五"·4② + 博鳌亚洲论坛2026"投资中国,共享未来"圆桌/"投资未来:准备好了吗?"高端对话/华商领袖与华人智库圆桌·3③，4一手+3二手)'
assert HERO_ANCHOR in html, 'hero r34 tail not found'
seg_r35 = ('｜ 三十五轮补采 2026-09-04(+11：WAIC2026全球治理高级别会议暨世界人工智能合作组织WAICO成立/WAIC2026市民AI体验开放日·1③+1②，全一手 ｜ '
           '六安市税务局/泾源县税务局/海晏县税务局政府开放日·3② + 儋州消防/萍乡消防站开放日·2② + 安徽省生态环境监测中心/奉新县生态环境监测站公众开放日·2② + 昌乐县人社局就业综合体/青山区人社局"双主任开放日"·2②，全一手)')
html = html.replace(HERO_ANCHOR, HERO_ANCHOR + seg_r35, 1)

foot_ok = html.count('📌 本页由 yitong 沉淀整理')
assert foot_ok >= 1, 'footer missing'
open(HTML, 'w', encoding='utf-8').write(html)
b1c = html.count('badge b1"')
b2c = html.count('badge b2"')
print(f'OK wall updated: ②={cur2+n2} ③={cur3+n3} (hl now {html.count(chr(34)+"hl"+chr(34))}), footer={foot_ok}, b1={b1c} b2={b2c}')

# ===== 2) incremental standalone page (runs dir, avoid same-day name collision) =====
def inc_page():
    body = []
    body.append('<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>Open Day 开放日 · 第三十五轮补采 2026-09-04</title>\n<style>\n')
    body.append(open(HTML, encoding='utf-8').read().split('<style>')[1].split('</style>')[0])
    body.append('\n</style>\n</head>\n<body>\n<div class="wrap">\n')
    body.append('  <div class="hero">\n    <h1>🚪 Open Day 开放日 · 第三十五轮补采（2026-09-04）</h1>\n')
    body.append('    <p>本轮新增 %d 张（②上下级 %d · ③高管间 %d，%d 一手 + %d 二手）｜ 受众关系分层（仅上下级 / 高管间，已剔除平级/朋友向）｜ 累计卡片墙：<a href="%s" style="color:#fff;text-decoration:underline" target="_blank">openday.html</a></p>\n' % (len(cards), n2, n3, sum(1 for c in cards if c['src']=='一手'), sum(1 for c in cards if c['src']=='二手'), GH))
    body.append('    <div class="relbar"><span>② 领导↔员工（上下级，supervisor）</span><span>③ 领导↔领导（高管间，exec）</span></div>\n  </div>\n')
    body.append('  <div class="grid">\n')
    body.append('\n'.join(card_html(c) for c in cards))
    body.append('\n  </div>\n')
    body.append('  <footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>\n</div>\n</body>\n</html>\n')
    return ''.join(body)
INC = os.path.join(KC, RUN_PAGE)
os.makedirs(os.path.dirname(INC), exist_ok=True)
open(INC, 'w', encoding='utf-8').write(inc_page())
assert os.path.exists(INC), 'run page not generated'
print(f'OK incremental run page: {INC} ({os.path.getsize(INC)}B)')

# ===== 3) index.json =====
for c in cards:
    idx_data.append(dict(
        title=c['title'],
        normKey=c['title'],
        url=c['url'].strip(),
        sourceType='primary' if c['src']=='一手' else 'secondary',
        relation='supervisor' if c['rel']=='r2' else 'exec',
        summary=c['val'],
        topic='openday',
    ))
json.dump(idx_data, open(IDX,'w',encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'OK index.json appended: {before} -> {len(idx_data)} (+{len(cards)})')

# ===== 4) Obsidian 00 index =====
ob_idx = open(OB_IDX, encoding='utf-8').read()
sec_header = '## 主题：Open Day 开放日'
hi = ob_idx.find(sec_header)
assert hi != -1, 'openday section not found in 00 index'
nav_line = '📄 主题汇总笔记：[[素材/openday/OpenDay-开放日-知识卡汇总]]'
if nav_line not in ob_idx:
    nl = ob_idx.find('\n', hi)
    ob_idx = ob_idx[:nl+1] + nav_line + '\n' + ob_idx[nl+1:]
    print('OK added nav link line to 00 index')
else:
    print('nav link line already present (skip)')
hi2 = ob_idx.find('## ', hi+len(sec_header))
if hi2 == -1:
    hi2 = len(ob_idx)
rows = ''
for c in cards:
    relt = '②上下级' if c['rel']=='r2' else '③高管间'
    rows += f'| {c["title"]}（openday.html） | 4 | {c["src"]} | {relt} | 三十五轮新增 |\n'
ob_idx = ob_idx[:hi2] + rows + ob_idx[hi2:]
open(OB_IDX, 'w', encoding='utf-8').write(ob_idx)
print('OK 00 index appended %d card rows' % len(cards))

# ===== 5) Obsidian summary note (programmatic stats increment) =====
ob_sum = open(OB_SUM, encoding='utf-8').read()
def inc_stat(pat, grp, add):
    m = re.search(pat, ob_sum)
    assert m, 'stat not found: '+pat
    new = int(m.group(grp)) + add
    return m, new
m_tot, new_tot = inc_stat(r'（共\s*(\d+)\s*张）', 1, len(cards))
ob_sum = ob_sum[:m_tot.start()] + '（共 %d 张）' % new_tot + ob_sum[m_tot.end():]
m_r2r3, new_r2 = inc_stat(r'②上下级\s*(\d+)\s*卡', 1, n2)
ob_sum = ob_sum[:m_r2r3.start()] + '②上下级 %d 卡' % new_r2 + ob_sum[m_r2r3.end():]
m_r2r3b, new_r3 = inc_stat(r'③高管间\s*(\d+)\s*卡', 1, n3)
ob_sum = ob_sum[:m_r2r3b.start()] + '③高管间 %d 卡' % new_r3 + ob_sum[m_r2r3b.end():]
m_b, new_b1 = inc_stat(r'一手\s*(\d+)\s*\+', 1, sum(1 for c in cards if c['src']=='一手'))
ob_sum = ob_sum[:m_b.start()] + '一手 %d +' % new_b1 + ob_sum[m_b.end():]
m_s, new_b2 = inc_stat(r'\+\s*二手\s*(\d+)', 1, sum(1 for c in cards if c['src']=='二手'))
ob_sum = ob_sum[:m_s.start()] + '+ 二手 %d' % new_b2 + ob_sum[m_s.end():]
ob_sum = ob_sum.replace('**276 卡**', '**%d 卡**' % (276+len(cards)))
# append round block after 三十四轮 bullet
lines = ob_sum.split('\n')
ti = next((i for i,l in enumerate(lines) if '三十四轮补采' in l), -1)
assert ti != -1, 'round34 note not found'
round_bullet = ('+ **三十五轮补采 2026-09-04(+11：WAIC2026全球治理高级别会议暨世界人工智能合作组织WAICO成立/WAIC2026市民AI体验开放日·1③+1②，全一手 ｜ '
               '六安市税务局/泾源县税务局/海晏县税务局政府开放日·3② + 儋州消防/萍乡消防站开放日·2② + 安徽省生态环境监测中心/奉新县生态环境监测站公众开放日·2② + 昌乐县人社局就业综合体/青山区人社局"双主任开放日"·2②，全一手)**')
lines.insert(ti+1, round_bullet)
ob_sum = '\n'.join(lines)
# card table before 适用&备注
TABLE_END = '## 适用 & 备注'
te = ob_sum.find(TABLE_END)
assert te != -1, '卡片总表 end marker not found'
trows = ''
for c in cards:
    relt = '②上下级' if c['rel']=='r2' else '③高管间'
    loc = c['val']
    if len(loc) > 240: loc = loc[:240] + '…'
    trows += f'| {c["title"]}（openday.html） | 4 | {c["src"]} | {relt} | {loc} |\n'
ob_sum = ob_sum[:te] + trows + ob_sum[te:]
open(OB_SUM, 'w', encoding='utf-8').write(ob_sum)
print('OK summary note updated (round block +%d rows, stats %d/%d/%d, 一手%d 二手%d)' % (len(cards), new_tot, new_r2, new_r3, new_b1, new_b2))

# ===== 5b) Obsidian runs independent note =====
os.makedirs(os.path.dirname(OB_RUN), exist_ok=True)
run_lines = [f'# Open Day 开放日 · 第三十五轮补采（2026-09-04）独立笔记', '']
run_lines.append(f'- 独立页 GitHub Pages：{GH_RUN}')
run_lines.append(f'- 本地路径：`{INC}`')
run_lines.append(f'- 累计卡片墙：`{GH}`')
run_lines.append('')
run_lines.append(f'本轮新增 **{len(cards)}** 张（②上下级 {n2} · ③高管间 {n3}，{sum(1 for c in cards if c["src"]=="一手")} 一手 + {sum(1 for c in cards if c["src"]=="二手")} 二手）：')
run_lines.append('')
run_lines.append('| 卡片 | 关系档 | 一手/二手 | 来源 |')
run_lines.append('| --- | --- | --- | --- |')
for c in cards:
    relt = '②上下级' if c['rel']=='r2' else '③高管间'
    run_lines.append(f'| {c["title"]} | {relt} | {c["src"]} | {c["url"]} |')
run_lines.append('')
run_lines.append('> 说明：本笔记为当轮独立页索引，不拷贝 HTML 副本；卡片正文见上方 GitHub Pages 独立页与累计墙。')
open(OB_RUN, 'w', encoding='utf-8').write('\n'.join(run_lines))
print('OK runs independent note: %s' % OB_RUN)

# ===== 6) 乐享 sync (whoami probe; skip on failure, non-blocking) =====
def lexiang_probe_and_upload():
    try:
        cfg = json.load(open(os.path.expanduser("~/.workbuddy/mcp.json"), encoding='utf-8'))
        token = cfg["mcpServers"]["lexiang"]["headers"]["Authorization"]
    except Exception as e:
        return None, 'no lexiang token in mcp.json: %s' % repr(e)[:120]
    try:
        ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
        base = 'https://mcp.lexiang-app.com/mcp?company_from=csig'
        hdr = {'Authorization':token,'Content-Type':'application/json','Accept':'application/json, text/event-stream'}
        def post(payload, timeout=15):
            data = json.dumps(payload).encode('utf-8')
            req = urllib.request.Request(base, data=data, headers=hdr, method='POST')
            with urllib.request.urlopen(req, context=ctx, timeout=timeout) as r:
                return r.read().decode('utf-8','ignore')
        post({'jsonrpc':'2.0','id':1,'method':'initialize','params':{'protocolVersion':'2024-11-05','capabilities':{},'clientInfo':{'name':'wb','version':'1.0'}}})
        post({'jsonrpc':'2.0','method':'notifications/initialized','params':{}})
        who = post({'jsonrpc':'2.0','id':2,'method':'tools/call','params':{'name':'whoami','arguments':{}}}, timeout=20)
        if ('401' in who) or ('Unauthorized' in who) or ('error' in who and 'token' in who.lower()):
            return None, 'whoami returned auth error (token expired)'
        folder_id = '5106d5b2decc442780c1cae5014c6fb6'
        def upload(html_path, name):
            size = os.path.getsize(html_path)
            ap = post({'jsonrpc':'2.0','id':3,'method':'tools/call','params':{'name':'file_apply_upload','arguments':{'parent_entry_id':folder_id,'name':name,'extension':'html','mime_type':'text/html','upload_type':'PRE_SIGNED_URL','size':str(size)}}})
            sid = re.search(r'"session_id"\s*:\s*"([^"]+)"', ap)
            if not sid: return None
            up = re.search(r'"upload_url"\s*:\s*"([^"]+)"', ap)
            if not up: return None
            upurl = up.group(1).replace('\\/','/')
            with open(html_path,'rb') as f: body = f.read()
            preq = urllib.request.Request(upurl, data=body, headers={'Content-Type':'text/html'}, method='PUT')
            with urllib.request.urlopen(preq, context=ctx, timeout=25) as r: code = r.getcode()
            if code >= 400: return None
            co = post({'jsonrpc':'2.0','id':4,'method':'tools/call','params':{'name':'file_commit_upload','arguments':{'session_id':sid.group(1)}}})
            m = re.search(r'"id"\s*:\s*"([^"]+)"', co)
            return m.group(1) if m else None
        eid = upload(INC, os.path.basename(RUN_PAGE))
        return eid, 'uploaded' if eid else 'upload failed'
    except Exception as e:
        return None, 'lexiang probe/upload failed: %s' % repr(e)[:160]

eid, lmsg = lexiang_probe_and_upload()
print('[lexiang] %s' % lmsg)
mapp = json.load(open(MAP, encoding='utf-8'))
round_rec = {'date':RUN_DATE, 'entry_id':eid, 'name':os.path.basename(RUN_PAGE)}
if eid is None:
    round_rec['note'] = '轮次页 R35 (+%d)｜乐享待补传(whoami 探活失败/未连通，待重连后补传并回填 entry_id)' % len(cards)
else:
    round_rec['note'] = '轮次页 R35 (+%d)｜乐享已上传' % len(cards)
mapp['openday']['rounds'].append(round_rec)
json.dump(mapp, open(MAP,'w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('OK lexiang-entry-map updated (entry_id=%s)' % eid)

# ===== 7) advance topic pointer =====
open(TOPIC_TXT, 'w', encoding='utf-8').write('下午茶研讨\n')
print('OK last-topic.txt -> 下午茶研讨')

print('\n==== RUN SUMMARY ====')
print('主题: Open Day 开放日 (r35, 2026-09-04)')
print('覆盖关系档: 仅 上下级(②) / 高管间(③)，已剔除 平级/朋友向(①)')
print('新增 N=%d (②=%d, ③=%d) | 去重删 M=%d' % (len(cards), n2, n3, len(dropped)))
print('增量独立页: %s' % INC)
print('汇总墙: %s' % HTML)
print('GitHub Pages 独立页: %s' % GH_RUN)
print('乐享 entry_id=%s (%s)' % (eid, lmsg))
