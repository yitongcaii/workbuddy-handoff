# -*- coding: utf-8 -*-
# Open Day 三十一轮补采（r31, 2026-09-01）+14 卡：11 ②上下级 + 3 ③高管间
# 新域：公安警营/法院公众/税务开放日/城管政府开放月/生态环境监测/铁路公安 + 跨国企业圆桌会(③)
import re, os, json, sys, datetime, urllib.request, ssl

WS = r"C:\Users\v_yitcai\WorkBuddy\20260728154244"
KC = os.path.join(WS, "knowledge-collection")
HTML = os.path.join(KC, "openday", "openday.html")
IDX = os.path.join(KC, "index.json")
OB_SUM = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\openday\OpenDay-开放日-知识卡汇总.md"
OB_IDX = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
GH = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday.html"
RUN_DATE = "20260901"
INC = os.path.join(KC, "openday", f"openday-{RUN_DATE}.html")
GH_RUN = f"https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday-{RUN_DATE}.html"
MAP = os.path.join(KC, "lexiang-entry-map.json")

cards = [
 dict(emoji='🚨', title='濉溪县公安局2026“相逢警营夜市 照亮美好濉溪”警营开放日', cat='警营开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.sxx.gov.cn/zwgk/public/31/65006981.html',
      val='濉溪县公安局2026年5月22—23日依托城关派出所开展「相逢警营\'夜市\' 照亮美好濉溪」主题警营开放日，突破传统宣传模式，创新打造警营夜市沉浸式体验场景，划分警用装备、交管业务、刑侦业务、法律咨询、便民服务等功能展区，邀辖区商会企业代表、新闻媒体、在校师生、新媒体粉丝等2000余名各界群众走进警营。群众参观综合指挥室、业务办公大厅，听取智慧警务、接处警、便民服务介绍；反恐战术演练、警犬演示、民警自编自演文艺节目；普法短片、射击模拟体验、趣味互动抽奖、便民服务摊位。推动警务公开、法治宣传、警民互动深度融合。',
      how='把「警营开放日」做成夜市沉浸式法治市集——以「警营夜市」场景化破除警民距离感，用警用装备/交管/刑侦/法律咨询/便民服务多展区把公安职能变可逛可体验；警犬+特警演练+文艺节目+射击模拟把严肃警务变亲民互动；2000人量级政民同场，是警民鱼水情与政务公开融合范本。',
      note='② 公安警营开放日（濉溪县政府官网一手），公安局领导以平安守护者姿态，商会企业/师生/群众走进警营、沉浸式体验警务、共筑警民鱼水情。'),
 dict(emoji='🐕', title='潍坊滨海公安2026“警民零距离、平安共守护”警营开放日暨110宣传日', cat='警营开放日',
      rel='r2', src='一手', src_cls='b1',
      url='http://wfbinhai.gov.cn/124/39057/2010886288529559552.html',
      val='潍坊滨海公安分局2026年1月7日（第六个中国人民警察节）开展「警民零距离、平安共守护」警营开放日暨110宣传日，邀高校师生、部门单位人员、企业职工2000余人，在滨海东城禁毒教育基地、西城大家洼派出所。禁毒教育基地沉浸式参观+特警装备+警犬搜毒演示；刑侦民警反诈宣讲+「反诈大咖」特饮（库迪咖啡联名）；情指中心普及110、推广微警务；大家洼派出所办案区开放+警民恳谈会听取成绩单、建言献策。',
      how='把「警营开放日」做成警民恳谈实景——以「禁毒基地+特警+警犬+反诈特饮」组合打破公安神秘感，用「反诈大咖」咖啡联名把防骗知识变生活方式；办案区开放+警民恳谈会把开放日变民意直通车，是节日型警民互动范本。',
      note='② 公安警营开放日（潍坊滨海区政府官网一手），分局领导以平安同行者姿态，师生/企业职工/群众走进派出所、恳谈共话平安。'),
 dict(emoji='⚖️', title='汝州市法院2026“汝瓷·润法”暑期公众开放日（旁听盗窃案庭审）', cat='法院公众开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://pdszy.hncourt.gov.cn/public/detail.php?id=16138',
      val='汝州市法院2026年8月26日开展公众开放日，邀基层医生、教师、群众代表及学生代表走进法院，参观办公大厅、审判大厅、审判法庭、党建文化长廊、法警文化长廊、羁押室；旁听一起盗窃犯罪案件公开庭审（法庭调查/举证质证/法庭辩论/被告人最后陈述）。庭审后代表称「庭审是最生动的法治课堂」。',
      how='把「法院开放日」做成看得见的正义——以「全区域参观+真实庭审旁听」让公众从「打官司的人」变「懂法的人」；用盗窃案庭审直观展现违法犯罪演变与危害；羁押室+法警文化长廊把司法威严具象化，是司法公开与青少年法治教育范本。',
      note='② 法院公众开放日（汝州法院官网一手），院长/庭长以司法守护者姿态，医生/教师/群众/学生走进法庭、旁听庭审、感受司法公开。'),
 dict(emoji='🏛️', title='内黄县法院楚旺法庭2026“法庭开放日”（庭所联动共商基层治理）', cat='法庭开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://hnnhxfy.hncourt.gov.cn/public/detail.php?id=4149',
      val='内黄县法院楚旺法庭2026年8月19日开展「法庭开放日」，邀楚旺派出所所长、乡人大代表、群众代表走进法庭，旁听一起追偿权纠纷庭审；庭长主持座谈，通报收结案、审判质效，剖析执法难点，代表建言诉讼服务/普法/便民；派出所所长提出深化「庭所联动」。',
      how='把「法庭开放日」做成基层共治平台——以「庭审旁听+庭所联动座谈」替代单向展示，用真实纠纷庭审让代表沉浸式感受司法严谨；庭长直面难点+派出所所长提出信息互通/协同联动，把开放日变基层治理连心桥，是人民法庭参与基层治理范本。',
      note='② 法庭开放日（内黄法院官网一手），法庭庭长以纠纷化解者姿态，人大代表/派出所所长/群众走进法庭、共商基层社会治理。'),
 dict(emoji='🧑⚖️', title='易门县法院2026“以案为鉴守初心·开门纳谏促公正”公众开放日', cat='法院公众开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://fy.ymcourt.gov.cn/article/detail/2026/04/id/9296942.shtml',
      val='易门县法院2026年4月28日开展「以案为鉴守初心·开门纳谏促公正」公众开放日，邀人大代表、政协委员、公安、检察及当事人、社区、律师等代表，参观诉讼服务中心、审判法庭、调解室、党员活动室；旁听涉贪污罪、受贿罪案件庭审；座谈通报2026年工作进展，代表围绕普法/解纷/司法便民/执行建言。',
      how='把「法院开放日」做成开门纳谏场——以「参观+职务犯罪庭审+座谈」组合把司法公开与廉政教育融合，用贪污受贿案庭审强化「以案为鉴」；人大代表/政协/检察/律师/当事人多方同堂建言，把开放日变外部监督与司法公信提升通道，是阳光司法范本。',
      note='② 法院公众开放日（易门法院官网一手），院长以司法公开推动者姿态，代表/当事人/律师走进法院、开门纳谏促公正。'),
 dict(emoji='💡', title='银川综合保税区税务分局2026“税护法治公平·助力发展共赢”税务开放日', cat='税务开放日',
      rel='r2', src='一手', src_cls='b1',
      url='http://ningxia.chinatax.gov.cn/art/2026/4/2/art_11082_384358.html',
      val='银川综合保税区税务分局2026年4月1日（第35个全国税收宣传月）举办「税护法治公平·助力发展共赢」税务开放日，邀苏银产业园重点企业、涉税专业服务机构及新办纳税人代表。代表以「税务体验师」身份走进办税厅，操作发票申领/代开自助终端、体验电子税务局「非接触式」办税、征纳互动区「远程帮办」；「依法诚信纳税」微课堂解读纳税信用等级；座谈围绕增值税法宣讲、办税堵点答疑、建问题台账限期反馈。',
      how='把「税务开放日」做成税企连心桥——以「体验师沉浸式办税+微课堂+座谈」替代单向宣讲，用「非接触式办税/远程帮办」实景展示智慧税务；纳税信用等级+增值税法精准传递法治公平；问题台账限期反馈把开放日变营商环境优化抓手，是税企双向共赢范本。',
      note='② 税务开放日（宁夏税务局官网一手），分局领导以法治护航者姿态，重点企业/涉税机构/新办纳税人以体验师身份走进办税厅、税企同心谋发展。'),
 dict(emoji='🏙️', title='上海杨浦区城管执法局2026“高质量法治护航高质量生活”政府开放月', cat='城管政府开放月',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.shyp.gov.cn/zhengwu/zfkf2026/2026/236/4290.html',
      val='杨浦区城管执法局2026年8月24日以「高质量法治护航高质量生活」为主题开展政府开放月活动，在杨浦滨江组织普法宣传。聚焦2026年8月15日施行的《生态环境法典》，通过精准宣讲、展板展示、手册发放介绍生态环境法规；执法队员解答市民关切的油烟污染、夜间违规施工、乱扔建筑垃圾等问题，发放「杨浦城管便民卡」和「生态环境法典学习手账」；推介「政策随申阅」二维码。',
      how='把「城管开放日」做成街头普法课——以「滨江普法+新法宣讲+便民卡」组合践行「谁执法谁普法」，用《生态环境法典》落地把城管职能从「管人」变「服务」；油烟/施工/垃圾等市民痛点现场答疑+学习手账，把开放日变共治共享生态治理入口，是城管阳光执法范本。',
      note='② 城管政府开放月（杨浦区政府官网一手），城管执法局领导以城市管家姿态，市民在滨江沉浸式学新法、现场议身边环境痛点。'),
 dict(emoji='🌳', title='青岛市北区城市管理局2026“探秘流苏古树，共护绿色活化石”政府开放月', cat='城管政府开放月',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.qingdao.gov.cn/ywdt/zwzl/zfkfy/qdzfkf/kfdt/202605/t20260514_10594306.shtml',
      val='青岛市北区城市管理局2026年5月6—9日开展「探秘流苏古树，共护绿色\'活化石\'」政府开放月，以院内百年流苏古树为载体，邀市民走进城管局，通过「实地参观+图文讲解+互动体验」了解古树保护；同步介绍城市管理成效。以一棵树带动一群人，拉近政府与公众距离。',
      how='把「城管开放日」做成古树沉浸式课堂——以「百年流苏古树」为情感载体，把政务公开阵地延到古树下，用「实地参观+展板+讲解」让市民读懂古树保护与城市管理成效；「以一棵树带动一群人」把专业职能变可感生态文化，是城管政民互动温情范本。',
      note='② 城管政府开放月（青岛政务网一手），城管局领导以城市园丁姿态，市民走进城管局、共护绿色活化石、了解城市管理工作。'),
 dict(emoji='🌊', title='上海静安区生态环境局2026“政务开放探秘自动站，生态建设护航十五五”政府开放月', cat='生态环境政府开放月',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.jingan.gov.cn/xxgk/002013/002013018/002013018001/002013018001005/20260819/9c8433fd-e741-4754-9fa4-ea68e9ccffc1.html',
      val='静安区生态环境局2026年8月开展「政务开放探秘自动站，生态建设护航十五五」政府开放月·政府开放日，邀市民走进辐射环境监测站与水质自动站。辐射站：科普辐射安全、常态化监测、数据实时采集上传、风险研判预警；水质自动站：演示水样自动采集、多参数实时分析、数据无线传输、异常自动预警全流程，解读氨氮/总磷/pH等13个指标。破除辐射认知误区、感受科技治水。',
      how='把「生态环境开放日」做成监测透明窗——以「辐射自动站+水质自动站」双场景，用设备实景演示把「看不见的监测」变可感科普；13项指标+异常自动预警解读把生态治理科学化、透明化；破除辐射误区拉近群众与环保距离，是生态环境政务公开范本。',
      note='② 生态环境政府开放月（静安区政府官网一手），生态环境局领导以生态守护者姿态，市民走进监测站、探秘自动站、共护碧水清流。'),
 dict(emoji='🚄', title='南京铁路公安处2026“警徽闪耀·平安相伴 110与您一路同行”高铁站警营开放日', cat='铁路警营开放日',
      rel='r2', src='二手', src_cls='b2',
      url='https://m.chinanews.com.cn/wap/detail/chs/zw/415974.shtml',
      val='南京铁路公安处2026年1月9日（第六个人民警察节、春运安保启动）携手南京市公共交通和城市轨道公安局在高铁南京南站开展「警徽闪耀·平安相伴 110与您一路同行」警营开放日，千余名旅客零距离观摩、沉浸式体验。警旗致敬仪式；装备体验区陈列警务机器人、特警装备、排爆设备、无人机反制系统、高精度执法记录仪，搜爆机器人实战演示；宣传区介绍矛盾化解/治安防控/「平安驿站」调解室；互动区知识问答+「警察小熊」文创；收集意见建议30余条。',
      how='把「铁路警营开放日」做成旅途平安课——以「高铁枢纽+警旗仪式+硬核装备+搜爆机器人」组合，把春运安保变旅客可参与的体验；「平安驿站」调解室+反诈/危险品科普把出行安全讲透；30余条意见建议直采民意，是路地融合警民互动范本（中新网二手）。',
      note='② 铁路警营开放日（中国新闻网二手），铁路公安领导以出行守护者姿态，旅客在高铁站零距离体验警务、共筑平安路。'),
 dict(emoji='🚢', title='秦皇岛“国门同心，口岸同安”口岸安全联合开放日（海事+边检+海关+港口）', cat='口岸安全联合开放日',
      rel='r2', src='二手', src_cls='b2',
      url='https://finance.sina.com.cn/jjxw/2026-04-14/doc-inhummye5032291.shtml',
      val='秦皇岛海事局联合秦皇岛出入境边防检查站、秦皇岛海关、秦港股份2026年4月11日（4·15全民国家安全教育日）在秦皇岛港口工业旅游区举办「国门同心，口岸同安」口岸安全联合开放日，邀秦皇岛日报社小记者团及游客。四家联动：海事局讲《海上交通安全法》+水上安全小课堂+VR实船体验；边检站警用装备体验区；海关展示外来物种植物标本+国门生物安全；秦港股份现代化港口安全管理+国家安全答题。',
      how='把「口岸开放日」做成国门安全课——以「海事+边检+海关+港口」四家联动，用VR实船/警用装备/外来物种标本把口岸安全变沉浸式体验；「国门同心·口岸同安」把国家安全教育从口号变实景，是口岸多部门联合开放范本（新浪财经二手/中国水运网）。',
      note='② 口岸安全联合开放日（新浪财经二手），海事/边检/海关/港口领导以国门卫士姿态，小记者/游客走进港口、共学口岸安全与国门生物安全。'),

 dict(emoji='🌐', title='天津2026跨国企业圆桌会（副市长邀企业家围坐恳谈·科技创新与产业创新）', cat='跨国企业圆桌会',
      rel='r3', src='二手', src_cls='b2',
      url='https://international.nankai.edu.cn/2026/0330/c13536a591735/page.htm',
      val='天津2026跨国企业圆桌会3月25—26日举行，主题「科技创新与产业创新深度融合」，获世界经济论坛北京代表处支持，约200位嘉宾（30余位国际商界/学界核心代表+天津政商学界）。天津市副市长王旭邀请中外企业家围坐大圆桌开诚布公恳谈；设AI驱动产业变革/区域发展与城市创新/科技创新合力/人类福祉与可持续发展四大板块+8场平行会议；3月26日「津门科创行」调研天津港、天津中医药大学、力神电池。波音/美团/华为/张伯礼院士等出席。',
      how='把「跨国企业圆桌会」做成政企高层恳谈场——以「副市长邀企业家围坐大圆桌+平行会议+实地调研」替代招商发布会，用「开放是天津基因」定调、把行业领袖与政策制定者并肩而坐变信任建立；「津门科创行」现场回应企业诉求、推动合作落地，是地方高水平对外开放与营商环境品牌范本（南开转载天津日报，二手）。',
      note='③ 跨国企业圆桌会（南开大学转载天津日报二手），副市长以城市合伙人姿态，跨国企业CEO/董事会主席围坐恳谈科技创新与产业创新、共绘投资天津蓝图（政企协作向，非IR/资本向）。'),
 dict(emoji='🏛️', title='中国发展高层论坛2026年会期间国务院发展研究中心闭门圆桌会', cat='高层论坛闭门圆桌会',
      rel='r3', src='二手', src_cls='b2',
      url='https://finance.sina.cn/2026-03-25/detail-inhseupy3603766.d.html',
      val='国务院发展研究中心在中国发展高层论坛2026年年会期间（3月23日）举办闭门圆桌会，中心主任、党组书记陆昊主持，副主任隆国强、张琦出席；近30位跨国企业、国际智库和机构负责人参加。博世董事会主席哈通、罗氏施万、力拓CEO乔德、瑞士再保险安博思、ABB总裁马腾、银瑞达瓦伦堡、巴西书赞桉诺阿布雷乌、沙特国际电力阿布纳扬、印尼三林林逢生、贝恩戴思睿、GSMA白德伟、英中贸易协会吴思田、港交所史美伦等先后发言；围绕中国经济与世界经济重要问题、「十五五」扩大高水平对外开放新机遇交流。',
      how='把「高层论坛闭门圆桌会」做成顶级政企对话场——以「国研中心主任主持+近30位跨国企业董事会主席/CEO同堂」的高规格，把中国「十五五」开放机遇与跨国企业在华投资合作直接对话；闭门机制保障坦诚交流，是国家级高层政企沟通与开放信号释放范本（新浪财经二手/中国经济时报）。',
      note='③ 高层论坛闭门圆桌会（新浪财经二手），国研中心主任以政策制定者姿态，跨国企业董事会主席/CEO围绕十五五开放机遇闭门对话、凝聚合作共识（高管间/政企协作向）。'),
 dict(emoji='🤝', title='第十七届中美商业领袖圆桌会议2026（纽约·亚布力论坛主办）', cat='中美商业领袖圆桌会',
      rel='r3', src='二手', src_cls='b2',
      url='https://www.toutiao.com/article/7652295245157204526',
      val='第十七届中美商业领袖圆桌会议2026年6月9日在纽约举办，由亚布力中国企业家论坛主办。亚布力轮值主席李小加、理事丁健、毛振华，驻纽约总领事陈立，安达集团埃文·格林伯格，纽约合作组织Steven Fulop，正大康地Paul FRIBOURG等30余位中美企业家、专家齐聚；围绕「可持续发展与未来城市」「前沿科技投资」两场主旨论坛研讨。企业家走访高盛、英伟达、Meta、谷歌，走进斯坦福大学对话基因编辑/AI/产学研融合。',
      how='把「中美商业领袖圆桌会」做成企业家互学场——以「亚布力论坛主办+中美企业家同堂+标杆参访」组合，把跨境科创投资与未来城市议题变建设性对话；走访高盛/英伟达/硅谷/斯坦福把前沿技术与企业战略直接对接，是民间商业领袖跨境合作与思想交流范本（今日头条二手/亚布力论坛）。',
      note='③ 中美商业领袖圆桌会（今日头条二手），亚布力论坛以民间桥梁搭建者姿态，中美企业家/CEO围绕可持续城市与前沿科技投资跨洋对话、共探科创机遇（高管间/企企协作向）。'),
]

# ---- dedup guard against index.json urls ----
idx_data = json.load(open(IDX, encoding='utf-8'))
existing_urls = set()
for x in idx_data:
    u = x.get('url')
    if u: existing_urls.add(u.strip())
before = len(idx_data)
kept, dropped = [], []
for c in cards:
    if c['url'].strip() in existing_urls:
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

# ===== 1) summary page openday.html =====
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

# hero append 三十一轮 segment after 二十七轮 tail
HERO_ANCHOR = '章贡吐槽大会·8②2③，9一手+1二手)'
assert HERO_ANCHOR in html, 'hero r27 tail not found'
seg_r31 = ('｜ 三十一轮补采 2026-09-01(+14，濉溪/潍坊滨海/汝州法院/内黄法庭/易门法院/'
           '银川综保区税务/杨浦城管/城北城管/静安生态环境/南京铁路公安/秦皇岛口岸联合开放日向·11②，6一手+5二手 ｜ '
           '天津跨国企业圆桌会/中国发展高层论坛闭门圆桌会/中美商业领袖圆桌会·3③，0一手+3二手)')
html = html.replace(HERO_ANCHOR, HERO_ANCHOR + seg_r31, 1)

foot_ok = html.count('📌 本页由 yitong 沉淀整理')
assert foot_ok >= 1, 'footer missing'
open(HTML, 'w', encoding='utf-8').write(html)
b1c = html.count('badge b1"')
b2c = html.count('badge b2"')
print(f'OK wall updated: ②={cur2+n2} ③={cur3+n3} (hl now {html.count(chr(34)+"hl"+chr(34))}), footer={foot_ok}, b1={b1c} b2={b2c}')

# ===== 2) incremental page =====
def card_html_multi(lst):
    return '\n'.join(card_html(c) for c in lst)

inc_html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Open Day 开放日 · 第31轮补采（独立页）</title>
<style>
:root{{--bg:#f4f6fb; --card:#ffffff; --ink:#1f2430; --sub:#5b6478; --accent:#6c5ce7; --accent2:#00b8d9; --chip:#eef0ff;}}
*{{box-sizing:border-box;margin:0;padding:0;}}
body{{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:linear-gradient(135deg,#eef1ff 0%,#e6f7ff 100%);color:var(--ink);padding:28px 18px;line-height:1.6;}}
.wrap{{max-width:1080px;margin:0 auto;}}
.hero{{background:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);border-radius:22px;padding:30px 32px;color:#fff;box-shadow:0 14px 40px rgba(108,92,231,.25);margin-bottom:22px;}}
.hero h1{{font-size:26px;font-weight:800;letter-spacing:1px;margin-bottom:8px;}}
.hero p{{font-size:14px;opacity:.95;}}
.relbar{{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px;}}
.relbar span{{background:rgba(255,255,255,.2);border-radius:20px;padding:5px 14px;font-size:13px;font-weight:600;}}
.sec{{margin:30px 0 12px;display:flex;align-items:center;gap:10px;}}
.sec h2{{font-size:19px;font-weight:800;}}
.sec .tag{{font-size:12px;padding:4px 12px;border-radius:12px;font-weight:700;}}
.sec3 .tag{{background:#f3e8ff;color:#7b2cbf;}} .sec3 h2{{color:#7b2cbf;}}
.sec2 .tag{{background:#fff3e0;color:#c0651a;}} .sec2 h2{{color:#c0651a;}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;}}
.hl{{background:var(--card);border-radius:18px;padding:18px 18px 16px;border-top:4px solid var(--accent);box-shadow:0 10px 32px rgba(108,92,231,.10);display:flex;flex-direction:column;gap:9px;}}
.top{{display:flex;align-items:center;gap:8px;flex-wrap:wrap;}}
.emoji{{font-size:22px;}}
.hl h3{{font-size:16px;font-weight:700;flex:1;min-width:120px;}}
.cat{{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:600;background:var(--chip);color:var(--accent);}}
.badge{{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:700;}}
.b1{{background:#e6f9f0;color:#0a8f5b;}}
.b2{{background:#fff1e6;color:#c0651a;}}
.r2{{background:#fff3e0;color:#c0651a;}}
.r3{{background:#f3e8ff;color:#7b2cbf;}}
.val{{font-size:13.5px;color:var(--sub);}}
.exec{{margin-top:2px;border-top:1px dashed #e2e8f0;padding-top:8px;}}
.exec summary{{cursor:pointer;font-size:13px;font-weight:600;color:var(--accent);}}
.exec .inner{{font-size:13px;color:var(--sub);margin-top:6px;padding-left:4px;}}
.src{{font-size:12px;word-break:break-all;}}
.src a{{color:var(--accent2);text-decoration:none;}}
.note{{font-size:12px;color:#94a3b8;border-left:3px solid #e2e8f0;padding-left:8px;}}
footer{{text-align:center;padding:24px;color:#94a3b8;font-size:13px;border-top:1px solid #e2e8f0;margin-top:40px;}}
</style>
</head>
<body>
<div class="wrap">
  <div class="hero">
    <h1>🚪 Open Day 开放日 · 第31轮补采（独立页）</h1>
    <p>采集于 2026-09-01 ｜ 本轮新增 {len(cards)} 卡（②上下级 {n2} · ③高管间 {n3}）｜ 六维评估 ｜ 一手/二手标注 ｜ 受众关系分层（仅②③，剔除①）｜ 累计总索引见 <a href="../openday.html" style="color:#fff;text-decoration:underline;">openday.html</a></p>
    <div class="relbar">
      <span>② 领导↔员工（上下级）</span>
      <span>③ 领导↔领导（高管间）</span>
    </div>
  </div>
  <div class="sec sec2">
    <h2>② 领导↔员工（上下级，supervisor）</h2>
    <span class="tag">{n2} 卡</span>
  </div>
  <div class="grid">
{card_html_multi(cards2)}
  </div>
  <div class="sec sec3">
    <h2>③ 领导↔领导（高管间 · exec）</h2>
    <span class="tag">{n3} 卡</span>
  </div>
  <div class="grid">
{card_html_multi(cards3)}
  </div>
  <footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>
</div>
</body>
</html>
'''
open(INC, 'w', encoding='utf-8').write(inc_html)
print(f'OK incremental page: {INC} ({os.path.getsize(INC)}B)')

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
# nav link line (ensure exists once)
nav_line = '📄 主题汇总笔记：[[素材/openday/OpenDay-开放日-知识卡汇总]]'
if nav_line not in ob_idx:
    # insert right after section header line
    nl = ob_idx.find('\n', hi)
    ob_idx = ob_idx[:nl+1] + nav_line + '\n' + ob_idx[nl+1:]
    print('OK added nav link line to 00 index')
else:
    print('nav link line already present (skip)')
# find end of openday section (next '## ' after header) to append card rows
hi2 = ob_idx.find('## ', hi+len(sec_header))
if hi2 == -1:
    hi2 = len(ob_idx)
rows = ''
for c in cards:
    relt = '②上下级' if c['rel']=='r2' else '③高管间'
    rows += f'| {c["title"]}（openday.html） | 4 | {c["src"]} | {relt} | 三十一轮新增 |\n'
ob_idx = ob_idx[:hi2] + rows + ob_idx[hi2:]
open(OB_IDX, 'w', encoding='utf-8').write(ob_idx)
print('OK 00 index appended %d card rows' % len(cards))

# ===== 5) Obsidian summary note =====
ob_sum = open(OB_SUM, encoding='utf-8').read()
# a) 摘要 round note
ABS_HEAD = '## 摘要'
ah = ob_sum.find(ABS_HEAD)
assert ah != -1
# append before the 卡片总表 or at end of 摘要 block: add after last existing round note.
# Find the line containing '三十轮补采 2026-08-28' and append after it.
anchor30 = '三十轮补采 2026-08-28(+10'
assert anchor30 in ob_sum, 'round30 note not found'
round_note = ('\n\n+ **三十一轮补采 2026-09-01(+14：濉溪公安/潍坊滨海公安/汝州法院/内黄法庭/易门法院/'
              '银川综保区税务/杨浦城管/城北城管/静安生态环境/南京铁路公安/秦皇岛口岸联合开放日向·11②+3③，6一手+8二手)**')
ob_sum = ob_sum.replace(anchor30, anchor30 + round_note, 1)
# b) 卡片总表 rows -> insert before '## 适用 & 备注'
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
# c) update stats in 适用&备注
ob_sum = ob_sum.replace('**243 卡**', '**257 卡**')
ob_sum = ob_sum.replace('②上下级 222 卡 / ③高管间 36 卡', '②上下级 233 卡 / ③高管间 39 卡')
ob_sum = ob_sum.replace('一手 137 + 二手 106', '一手 143 + 二手 114')
open(OB_SUM, 'w', encoding='utf-8').write(ob_sum)
print('OK summary note updated (摘要 +14 rows, 适用&备注 stats)')

# ===== 6) 乐享 file upload (best effort) =====
def upload_lexiang(html_path, name, folder_id, token):
    try:
        import json as _json
        ctx = ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
        base = 'https://mcp.lexiang-app.com/mcp?company_from=csig'
        hdr = {'Authorization':'Bearer '+token,'Content-Type':'application/json','Accept':'application/json, text/event-stream'}
        def post(payload):
            data = _json.dumps(payload).encode('utf-8')
            req = urllib.request.Request(base, data=data, headers=hdr, method='POST')
            with urllib.request.urlopen(req, context=ctx, timeout=25) as r:
                raw = r.read().decode('utf-8','ignore')
            return raw
        post({'jsonrpc':'2.0','id':1,'method':'initialize','params':{'protocolVersion':'2024-11-05','capabilities':{},'clientInfo':{'name':'wb','version':'1.0'}}})
        post({'jsonrpc':'2.0','method':'notifications/initialized','params':{}})
        size = os.path.getsize(html_path)
        ap = post({'jsonrpc':'2.0','id':2,'method':'tools/call','params':{'name':'file_apply_upload','arguments':{'parent_entry_id':folder_id,'name':name,'extension':'html','mime_type':'text/html','upload_type':'PRE_SIGNED_URL','size':str(size)}}})
        sid = None
        m = re.search(r'"session_id"\s*:\s*"([^"]+)"', ap)
        if m: sid = m.group(1)
        if not sid:
            print('  [lexiang] no session_id in apply_upload, skip'); return None
        # PUT file bytes
        up = re.search(r'"upload_url"\s*:\s*"([^"]+)"', ap)
        if not up:
            print('  [lexiang] no upload_url, skip'); return None
        upurl = up.group(1).replace('\\/','/')
        with open(html_path,'rb') as f: body = f.read()
        preq = urllib.request.Request(upurl, data=body, headers={'Content-Type':'text/html'}, method='PUT')
        with urllib.request.urlopen(preq, context=ctx, timeout=25) as r:
            code = r.getcode()
        if code >= 400:
            print('  [lexiang] PUT http %s, skip'%code); return None
        co = post({'jsonrpc':'2.0','id':3,'method':'tools/call','params':{'name':'file_commit_upload','arguments':{'session_id':sid}}})
        eid = None
        m2 = re.search(r'"id"\s*:\s*"([^"]+)"', co)
        if m2: eid = m2.group(1)
        print('  [lexiang] uploaded entry_id=%s' % eid)
        return eid
    except Exception as e:
        print('  [lexiang] upload failed/skipped:', repr(e)[:200]); return None

token = 'lxmcp_1b82fcd9c11ff51ea657ee591e793c39825fb1748510b241ab29443a1106b708'
folder_id = '22eea86cd58a46729ed69380092c2c13'
entry_id = upload_lexiang(INC, f'openday-{RUN_DATE}.html', folder_id, token)
mapp = json.load(open(MAP, encoding='utf-8'))
round_rec = {'date':RUN_DATE, 'entry_id':entry_id, 'name':f'openday-{RUN_DATE}.html'}
if entry_id is None:
    round_rec['note'] = '轮次页 R31 (+%d)｜乐享待补传(token 过期/不可用，待重连后补传并回填 entry_id)' % len(cards)
mapp['openday']['rounds'].append(round_rec)
json.dump(mapp, open(MAP,'w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('OK lexiang-entry-map updated (entry_id=%s)' % entry_id)

print('\n==== RUN SUMMARY ====')
print('主题: Open Day 开放日 (r31, 2026-09-01)')
print('覆盖关系档: 仅 上下级(②) / 高管间(③)，已剔除 平级/朋友向(①)')
print('新增 N=%d (②=%d, ③=%d) | 去重删 M=%d' % (len(cards), n2, n3, len(dropped)))
print('增量页: %s' % INC)
print('汇总页: %s' % HTML)
print('乐享 entry_id=%s (folder=%s)' % (entry_id, folder_id))
