# -*- coding: utf-8 -*-
# Open Day 三十四轮补采（r34, 2026-09-04）+9~10 卡：6 ②上下级 + 3 ③高管间（剔除 peer/朋友向 与 IR/资本市场开放日）
# 新域（②上下级·政务/国企/央企公众开放日向）：梅江区检法开放日 / 分宜县气象局政府开放日 / 桐城市气象局政府开放日 /
#       上海国企开放日"企妙星期五" / 首都国企开放日142条线路 / 中国石化2026公众开放日
#       ③高管间·政企/企企高层对话向：博鳌亚洲论坛2026"投资中国,共享未来"圆桌 / "投资未来:准备好了吗?"高端对话 / 华商领袖与华人智库圆桌
import re, os, json, sys, subprocess, datetime, urllib.request, urllib.error, ssl

WS = r"C:\Users\v_yitcai\WorkBuddy\20260728154244"
KC = os.path.join(WS, "knowledge-collection")
HTML = os.path.join(KC, "openday", "openday.html")
IDX = os.path.join(KC, "index.json")
OB_SUM = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\openday\OpenDay-开放日-知识卡汇总.md"
OB_IDX = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
OB_RUN = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\openday\runs\OpenDay-2026-09-04-第三十四轮-知识卡.md"
GH = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday.html"
RUN_DATE = "20260904"
RUN_PAGE = "openday-20260904.html"
GH_RUN = f"https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/{RUN_PAGE}"
MAP = os.path.join(KC, "lexiang-entry-map.json")
TOPIC_TXT = os.path.join(KC, "last-topic.txt")

cards = [
 dict(emoji='⚖️', title='梅江区人民检察院·区人民法院“检法零距离 携手向未来”主题检法开放日（六一·人大代表/政协委员/师生走进检法一线）', cat='政法开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.gdmeijiang.jcy.gov.cn/jcdt/gzdt/t20260527_1677.htm',
      val='梅江区人民检察院联合梅江区人民法院在六一国际儿童节来临之际开展“检法零距离 携手向未来”主题检法开放日，邀请区人大代表、政协委员及芹洋学校师生代表走进检法机关，近距离观摩司法工作、接受法治教育。代表委员和师生依次参观12309检察服务中心、案件管理中心、听证室与办案区，检察官详解检察便民服务流程、窗口职责、听证制度意义及办案区规范化建设；未检法治微课堂讲未成年人检察职能与特殊优先保护；随后旁听帮助信息网络犯罪活动罪案件庭审，法官结合案例拆解日常违法风险、纠正“讲江湖义气”等错误观念。活动搭建司法机关与青少年、社会各界的良性沟通桥梁。',
      how='把“检法开放日”做成司法透明+青少年法治教育双课——以“检察院+法院联合开放”把法律监督与审判两条线一次看全；用人大代表/政协委员作为首批体验者把政务公开升级为“请代表走进一线监督”；以“参观+微课堂+旁听庭审+精准普法”四段式把抽象司法变可感可学；紧扣六一节点，是基层检法机关政务开放日向范本（梅江区检察院官网一手）。',
      note='② 政法开放日（梅江区检察院官网一手），检法机关领导以司法守护者姿态，人大代表/政协委员/师生代表零距离走进检法一线、读懂司法全流程。'),
 dict(emoji='🏛️', title='易门县人民法院2026“公众开放日暨开门纳谏”活动（以案为鉴守初心·开门纳谏促公正）', cat='法院开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://fy.ymcourt.gov.cn/article/detail/2026/04/id/9296942.shtml',
      val='易门县人民法院4.28开展“公众开放日暨开门纳谏”活动，主题“以案为鉴守初心·开门纳谏促公正”，邀人大代表、政协委员、公安、检察及当事人、社区、律师等社会各界代表走进法院。各界代表依次参观审判大楼诉讼服务中心、审判法庭、调解室、党员活动室，实地观摩、现场交流，全方位了解法院建设情况与司法服务举措；随后全体人员旁听涉贪污罪、受贿罪案件庭审，“沉浸式”感受司法威严；座谈会通报县法院2026年以来工作进展与成效，与会代表围绕普法宣传、基层解纷、司法便民、执行工作建言献策。',
      how='把“法院开放日”做成司法公开+开门纳谏闭环——以“参观+旁听庭审+座谈纳谏”三段式把法院工作变可感可监督；用“开门纳谏”把开放日从“展示”升级为“听意见、促公正”；以涉职务犯罪庭审作警示教育教材，是县级法院阳光司法与民主监督结合范本（易门法院官网一手）。',
      note='② 法院开放日（易门法院官网一手），法院领导以司法为民姿态，人大代表/政协委员/当事人/社区/律师代表走进法院、评议司法工作。'),
 dict(emoji='🌤️', title='分宜县气象局2026“政府开放日”（携手缩小预警差距·开放国家基本气象站+气象台科普）', cat='气象局政务开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.fenyi.gov.cn/fenyi/hdyg/2026-06/30/content_df7e1962f9564779b2f8fe34fe3adfd9.shtml',
      val='分宜县气象局依《新余市常态化政府开放日通知》于2026.6.18开展“政府开放日”，主题“携手缩小预警差距”，邀10名市民代表+适当邀请人大代表/政协委员/媒体/专家/企业。开放分宜国家基本气象站，展示气象综合观测现代化仪器设备；在气象台聆听专家讲解气象科普、解答气象热点、观看科普宣传片、发放手册；流程含浏览介绍（设备用途/预警信号科普）、观摩体验（办公运行+天气预报制作过程）。突出政民互动，提升群众对政府工作知晓度、参与度、满意度。',
      how='把“气象局政府开放日”做成减灾科普沉浸课——以“观测站开放+气象台专家讲解+预警信号科普”三段式把专业气象工作变可感可学；用“携手缩小预警差距”主题锚定防灾减灾公共价值；小规模化（10人）+代表邀请保证沟通深度，是县级气象部门政务开放日向范本（分宜县政府官网一手）。',
      note='② 气象局政务开放日（分宜县政府官网一手），气象部门领导以公共安全服务者姿态，市民/代表/专家走进气象站、读懂预警与天气预报。'),
 dict(emoji='🌦️', title='桐城市气象局2026“政府开放日”（人人讲安全 个个会应急·探秘+体验+交流+科普四维）', cat='气象局政务开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.tongcheng.gov.cn/public/2000002371/2024570125.html',
      val='桐城市气象局2026.5.10开展“政府开放日”，主题“人人讲安全、个个会应急——提高防灾减灾救灾能力”，邀30名市民代表。围绕“探秘+体验+交流+科普”四维：实地探秘（专业人员带参观观测场、气象台，观察仪器、讲原理用途）；流程体验（现场观摩天气预报制作全流程，含数值预报分析、卫星云图解读、雷达回波研判、气象服务信息发布）；互动交流（介绍重点工作、解预报准确性/灾害防御疑问、收意见建议）；科普学习（播科普片、普及气象基础与灾害性天气防范）。后续持续畅通沟通渠道。',
      how='把“气象局政府开放日”做成四维体验课——以“探秘+体验+交流+科普”结构化设计把气象观测与预报全流程系统呈现；用“人人讲安全、个个会应急”主题把专业气象变全民防灾能力；30人规模兼顾广度与体验，是县级气象部门政务开放日向可复制模板（桐城市政府官网一手）。',
      note='② 气象局政务开放日（桐城市政府官网一手），气象部门领导以公共安全服务者姿态，市民代表沉浸式体验气象观测与预报全流程。'),
 dict(emoji='🏙️', title='上海国企开放日“企妙星期五”（2026.9-2027.6·50余点位每周五轮开·国缆检测/粮储文化馆/英雄文创等）', cat='国企开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.gzw.sh.gov.cn/shgzw_zxzx_gqdt/20260902/d971e1a1160b4515999e3a9ecf2c5a5e.html',
      val='上海市国资委2026.9启动“企妙星期五”国企开放日：2026年9月至2027年6月，50余个开放点位轮流在每个星期五（法定节假日除外）开放。2026年9月首月有9个点位亮相，如国缆检测企业展厅（8模块展现线缆检测实力）、闵行粮储文化展示馆（上海首家粮食储备主题馆，老粮库改建）、英雄文创精品馆（百年民族品牌国货故事）。以“特定时段集中开放+常态化开放”双轨，支持企业打造全年不间断可体验场景，通过“国资京京”官微及专属小程序一键查线路地图、点位名录、接待容量。',
      how='把“国企开放日”做成常态化市民打卡机制——以“企妙星期五”固定周期（每周五）把国企大门变市民可预期的开放场景；用50余点位轮开+“一企一特色”避免同质化；以“集中开放+常态化开放”双轨让国企文化深度融入城市生活；数字化小程序一键查，是地方国资系统品牌化开放日向范本（上海市国资委官网一手）。',
      note='② 国企开放日（上海市国资委官网一手），上海国企领导以城市服务者姿态，市民/师生/行业代表每周五走进国企展厅与生产线。'),
 dict(emoji='🏛️', title='“首都国企开放日”2026（45家国企·142条线路·常态化开放贯穿2026.4-2027.3）', cat='国企开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://bj.people.com.cn/BIG5/n2/2026/0527/c14540-41592437.html',
      val='北京市国资委2026年启动“首都国企开放日”，45家首都国企共推142条线路（点位）向市民开放，聚焦文商旅体展融合，塑造“一企一特色、一线一亮点”。市民、师生、行业代表、媒体可走进展厅、生产车间、研发实验室、重点工程现场，感受首都国企在文化传承、民生保障、科技创新的硬核担当。自2016年创办，今年首次突破集中模式，贯穿2026.4-2027.3长效开放；创新“特定时段集中开放+常态化开放”双轨，联动国庆/中秋/阅读季等排布场次；通过“国资京京”官微及专属小程序一键查。',
      how='把“国企开放日”做成城市级长效开放平台——以142条线路+45家国企规模制造“国企大门常开”声势；用“一企一特色、一线一亮点”避免千企一面；以“集中+常态化”双轨把开放日变全年可参与场景；数字化小程序降低参与门槛，是直辖市国资系统开放日向标杆（人民网北京/北京市国资委一手）。',
      note='② 国企开放日（人民网北京/北京市国资委一手），首都国企领导以城市共建者姿态，市民/师生/媒体代表走进国企博物馆与生产线。'),
 dict(emoji='🛢️', title='中国石化2026公众开放日（世界地球日启动·100余企业百余城市同步开放·探秘智慧能源）', cat='央企公众开放日',
      rel='r2', src='二手', src_cls='b2',
      url='https://sd.people.com.cn/BIG5/n2/2026/0423/c166188-41560975.html',
      val='中国石化2026.4.22第57个世界地球日在胜利油田启动2026年公众开放日，发布《绿色脉动》环保主题系列视频；所属100余家企业在全国百余座城市同步开放，近万名公众入厂参观，沉浸式体验石化产业链绿色魅力。以“探秘智慧能源”为主题：胜利油田CCUS示范基地、镇海炼化白鹭共生、茂名石化生态果园、广东石油爱跑98绿色工艺、新疆石油春耕保供等，同步直播“云开放”。累计举办超5500场次、接待超28万人、线上云游览破2亿人次，是我国工业领域规模最大、央企首个品牌化公众开放活动。',
      how='把“央企公众开放日”做成工业透明+绿色品牌双课——以“探秘智慧能源”把封闭石化产业链变可逛可体验；用CCUS/白鹭共生/生态果园等鲜活故事讲绿色低碳转型；100余企业同步+云开放放大声量；以品牌化（主题曲/吉祥物/海外主会场）沉淀为工业开放标杆，是企业与社会公众沟通桥梁范本（人民网山东二手报道）。',
      note='② 央企公众开放日（人民网山东二手报道），中国石化管理层以绿色能源提供者姿态，公众/媒体/客户/学生走进厂区读懂石化与环保。'),

 dict(emoji='🌐', title='博鳌亚洲论坛2026年会“投资中国,共享未来”圆桌论坛（龙永图/跨国CEO/商会领袖对话外资新机遇）', cat='博鳌政企高层对话',
      rel='r3', src='二手', src_cls='b2',
      url='https://finance.sina.com.cn/jjxw/2026-03-25/doc-inhsffcs6767364.shtml',
      val='博鳌亚洲论坛2026年会3.25举行“投资中国,共享未来”圆桌，CGTN主持，邀中国入世首席代表龙永图、中国贸促会原副会长张少刚、英中贸易协会CEO白彼得、中电集团高级副总裁陈涛、BCG中国区执行合伙人吴淳、葡中工商会秘书长、中国意大利商会会长、加中贸易理事会首代等围绕外资在华新机遇新挑战对话。龙永图强调完整制造业体系与人才红利；张少刚指“十五五”规划是了解中国最佳密码；陈涛“能在中国竞争就能在任何市场竞争”；共识是中国从“世界工厂”转向“世界创新中心”，外资从“分享未来”到“成为未来的一部分”。',
      how='把“博鳌投资中国圆桌”做成国家级政企/企企高层对话场——以“前部长+贸促会+跨国CEO+商会领袖”同台把中国开放政策变可对话的公共议题；用“十五五”规划作共识锚点，把外资疑虑变合作机遇；以“分享未来→成为未来”叙事升级开放日话语，是高层开放合作与外商信心建设范本（新浪财经二手侧记）。',
      note='③ 博鳌政企高层对话（新浪财经二手侧记），论坛与中国贸促会以开放合作推动者姿态，前政要/跨国企业CEO/商会领袖围绕外资在华机遇围坐对话（政企/企企协作向，非IR/证券向）。'),
 dict(emoji='🤝', title='博鳌亚洲论坛2026“投资未来:准备好了吗?”高端对话（前政府首脑/经济官员/商业领袖论合作）', cat='博鳌政企高层对话',
      rel='r3', src='二手', src_cls='b2',
      url='http://english.people.cn/n3/2026/0326/c98649-20440223.html',
      val='博鳌亚洲论坛2026年会高端对话“投资未来:准备好了吗?”汇聚前政府首脑、高级经济官员与领军商业人物。印尼国家经济委员会副主席Pangestu倡“协调一致单边主义”、以区域合作对冲关税冲击；法国前总理拉法兰警示法治弱化、呼吁中欧“朝同一方向看”；意大利前总理/前欧委会经济委员Gentiloni主张守住WTO/IMF等现有制度架构；Fortescue执行主席Forrest以算术论证绿能转型（全球首座全绿矿山明年上线、绿铁成本62亿美元vs化石180亿）；共识是“携手合作或各自落后”。',
      how='把“博鳌高端对话”做成全球治理层对话场——以“前政府首脑+经济官员+商业领袖”组合把地缘不确定性变可讨论的协作议程；用绿色能源/区域合作/制度架构三大主线凝共识；以“携手合作或各自落后”收束开放日叙事，是国际组织平台高层对话范本（人民网英文版二手）。',
      note='③ 博鳌政企高层对话（人民网英文二手），论坛秘书处以全球治理推动者姿态，前政要/经济官员/跨国企业领袖围绕绿色转型与区域合作闭门与分论坛对话（高管间/政企学协作向）。'),
 dict(emoji='🌏', title='博鳌亚洲论坛2026“华商领袖与华人智库圆桌会议”（国侨办主任+26位华商/智库·把握新机遇实现新发展）', cat='博鳌政企高层对话',
      rel='r3', src='二手', src_cls='b2',
      url='https://news.qq.com/rain/a/20260326A02O9400',
      val='博鳌亚洲论坛2026年会3.25举行“华商领袖与华人智库圆桌会议”，国务院侨办主任陈旭出席讲话，来自13个国家和地区26位华商代表、民营企业家和智库专家出席，主题“把握新机遇 实现新发展”，围绕“‘十五五’时期中国经济发展与华商机遇”“AI加速产业变革：企业应对之策”“应对变局挑战,助推中外友好”3个分议题研讨。正大集团资深董事长谢国民、金鹰集团执行董事陈昱廷等发言，呼吁华商抓住中国高质量发展与AI创新机遇、助力中国式现代化与中外友好。',
      how='把“华商领袖圆桌”做成政企/侨企高层对话场——以“国侨办主任+跨国华商领袖+智库”同台把华侨华人独特优势变开放合作资源；用“十五五”+AI产业变革作共识锚点；以“把握新机遇、实现新发展”叙事把侨力转化为中外友好与高质量发展合力，是高层开放日政企协作范本（腾讯新闻二手）。',
      note='③ 博鳌政企高层对话（腾讯新闻二手），国侨办以民族复兴推动者姿态，华商领袖/民营企业家/智库专家围绕“十五五”机遇与AI变革围坐对话（政企/企企协作向）。'),
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

# hero append 三十四轮 segment after 三十三轮 tail
HERO_ANCHOR = '三十三轮补采 2026-09-03(+6：第四届链博会公众开放日/APEC工商领导人中国论坛/第十三届服贸会/乌镇峰会/跨国公司领导人青岛峰会·4③，4一手 ｜ 六安市地震局/银川公积金中心政务开放日·2②，2一手)'
assert HERO_ANCHOR in html, 'hero r33 tail not found'
seg_r34 = ('｜ 三十四轮补采 2026-09-04(+10：梅江区检法开放日/分宜县气象局政府开放日/桐城市气象局政府开放日/上海国企开放日"企妙星期五"/首都国企开放日142条线路/中国石化2026公众开放日·7② + '
           '博鳌亚洲论坛2026"投资中国,共享未来"圆桌/"投资未来:准备好了吗?"高端对话/华商领袖与华人智库圆桌·3③，5一手+4二手)')
html = html.replace(HERO_ANCHOR, HERO_ANCHOR + seg_r34, 1)

foot_ok = html.count('📌 本页由 yitong 沉淀整理')
assert foot_ok >= 1, 'footer missing'
open(HTML, 'w', encoding='utf-8').write(html)
b1c = html.count('badge b1"')
b2c = html.count('badge b2"')
print(f'OK wall updated: ②={cur2+n2} ③={cur3+n3} (hl now {html.count(chr(34)+"hl"+chr(34))}), footer={foot_ok}, b1={b1c} b2={b2c}')

# ===== 2) incremental standalone page openday-20260904.html =====
def inc_page():
    body = []
    body.append('<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>Open Day 开放日 · 第三十四轮补采 2026-09-04</title>\n<style>\n')
    body.append(open(HTML, encoding='utf-8').read().split('<style>')[1].split('</style>')[0])
    body.append('\n</style>\n</head>\n<body>\n<div class="wrap">\n')
    body.append('  <div class="hero">\n    <h1>🚪 Open Day 开放日 · 第三十四轮补采（2026-09-04）</h1>\n')
    body.append('    <p>本轮新增 %d 张（②上下级 %d · ③高管间 %d，%d 一手 + %d 二手）｜ 受众关系分层（仅上下级 / 高管间，已剔除平级/朋友向）｜ 累计卡片墙：<a href="%s" style="color:#fff;text-decoration:underline" target="_blank">openday.html</a></p>\n' % (len(cards), n2, n3, sum(1 for c in cards if c['src']=='一手'), sum(1 for c in cards if c['src']=='二手'), GH))
    body.append('    <div class="relbar"><span>② 领导↔员工（上下级，supervisor）</span><span>③ 领导↔领导（高管间，exec）</span></div>\n  </div>\n')
    body.append('  <div class="grid">\n')
    body.append('\n'.join(card_html(c) for c in cards))
    body.append('\n  </div>\n')
    body.append('  <footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>\n</div>\n</body>\n</html>\n')
    return ''.join(body)
INC = os.path.join(KC, "openday", RUN_PAGE)
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
    rows += f'| {c["title"]}（openday.html） | 4 | {c["src"]} | {relt} | 三十四轮新增 |\n'
ob_idx = ob_idx[:hi2] + rows + ob_idx[hi2:]
open(OB_IDX, 'w', encoding='utf-8').write(ob_idx)
print('OK 00 index appended %d card rows' % len(cards))

# ===== 5) Obsidian summary note =====
ob_sum = open(OB_SUM, encoding='utf-8').read()
# append round block as new bullet after the line containing 三十三轮补采
lines = ob_sum.split('\n')
ti = next((i for i,l in enumerate(lines) if '三十三轮补采' in l), -1)
assert ti != -1, 'round33 note not found'
round_bullet = ('+ **三十四轮补采 2026-09-04(+10：梅江区检法开放日/分宜县气象局政府开放日/桐城市气象局政府开放日/上海国企开放日"企妙星期五"/首都国企开放日142条线路/中国石化2026公众开放日·7② + '
               '博鳌亚洲论坛2026"投资中国,共享未来"圆桌/"投资未来:准备好了吗?"高端对话/华商领袖与华人智库圆桌·3③，5一手+4二手)**')
lines.insert(ti+1, round_bullet)
ob_sum = '\n'.join(lines)
# card table
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
# stats (authoritative current: 269 / 一手157+二手112 / ②238+③46)
ob_sum = ob_sum.replace('（共 269 张）', '（共 %d 张）' % (269+len(cards)))
ob_sum = ob_sum.replace('**269 卡**', '**%d 卡**' % (269+len(cards)))
ob_sum = ob_sum.replace('一手 157 + 二手 112', '一手 %d + 二手 %d' % (157+sum(1 for c in cards if c['src']=='一手'), 112+sum(1 for c in cards if c['src']=='二手')))
ob_sum = ob_sum.replace('②上下级 238 卡 / ③高管间 46 卡', '②上下级 %d 卡 / ③高管间 %d 卡' % (238+n2, 46+n3))
open(OB_SUM, 'w', encoding='utf-8').write(ob_sum)
print('OK summary note updated (round block +%d rows, stats)' % len(cards))

# ===== 5b) Obsidian runs independent note =====
os.makedirs(os.path.dirname(OB_RUN), exist_ok=True)
run_lines = [f'# Open Day 开放日 · 第三十四轮补采（2026-09-04）独立笔记', '']
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
        eid = upload(INC, RUN_PAGE)
        return eid, 'uploaded' if eid else 'upload failed'
    except Exception as e:
        return None, 'lexiang probe/upload failed: %s' % repr(e)[:160]

eid, lmsg = lexiang_probe_and_upload()
print('[lexiang] %s' % lmsg)
mapp = json.load(open(MAP, encoding='utf-8'))
round_rec = {'date':RUN_DATE, 'entry_id':eid, 'name':RUN_PAGE}
if eid is None:
    round_rec['note'] = '轮次页 R34 (+%d)｜乐享待补传(whoami 探活失败/未连通，待重连后补传并回填 entry_id)' % len(cards)
else:
    round_rec['note'] = '轮次页 R34 (+%d)｜乐享已上传' % len(cards)
mapp['openday']['rounds'].append(round_rec)
json.dump(mapp, open(MAP,'w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('OK lexiang-entry-map updated (entry_id=%s)' % eid)

# ===== 7) advance topic pointer =====
open(TOPIC_TXT, 'w', encoding='utf-8').write('下午茶研讨\n')
print('OK last-topic.txt -> 下午茶研讨')

print('\n==== RUN SUMMARY ====')
print('主题: Open Day 开放日 (r34, 2026-09-04)')
print('覆盖关系档: 仅 上下级(②) / 高管间(③)，已剔除 平级/朋友向(①)')
print('新增 N=%d (②=%d, ③=%d) | 去重删 M=%d' % (len(cards), n2, n3, len(dropped)))
print('增量独立页: %s' % INC)
print('汇总墙: %s' % HTML)
print('GitHub Pages 独立页: %s' % GH_RUN)
print('乐享 entry_id=%s (%s)' % (eid, lmsg))
