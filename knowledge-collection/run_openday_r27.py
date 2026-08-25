# -*- coding: utf-8 -*-
# Open Day 二十七轮补采（r27, 2026-08-26）+10 卡：8 ②上下级 + 2 ③高管间
# 新域：上海国企开放日城市级 campaign / 中科院脑智中心·脑机接口 / 核能安全所核科普 /
#       固体所材料之美 / 成都智算中心 AI 科普 / 数博会公众开放日分层 /
#       信通院智算生态开放日 / 知音湖北超级文旅日 / 中宁工业园区营商环境闭环 / 章贡吐槽大会(政企)
import re, os, json, sys

WS = r"C:\Users\v_yitcai\WorkBuddy\20260728154244"
KC = os.path.join(WS, "knowledge-collection")
HTML = os.path.join(KC, "openday", "openday.html")
TMP  = os.path.join(KC, "openday", ".run_newcards.tmp.html")
CACHE= os.path.join(KC, "openday", ".rows_cache.json")
IDX  = os.path.join(KC, "index.json")
OB_SUM = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\openday\OpenDay-开放日-知识卡汇总.md"
OB_IDX = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
OB_RUN = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\openday\runs\OpenDay-20260826-第二十七轮-知识卡.md"
GH = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday.html"
GH_RUN = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/runs/openday-20260826-r27.html"

cards = [
 dict(emoji='🏙️', title='2026「上海国企开放日」集中开放活动（城市级 80+ 场·四大主题周）', cat='国企开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.gzw.sh.gov.cn/shgzw_zxzx_gqdt/20260706/1ff64acadaa3479ba4711ef5498146ed.html',
      val='2026 年「上海国企开放日」集中开放活动由上海市国资委主办，7.6—8.30 跨暑期推出四大主题周：回望红色历史、探索创新科技、打卡文化空间、体验优质服务，累计 80+ 场活动轮番登场；推出专属路线一次打卡多个点位，覆盖老市府大楼、国家级非遗乐器、青少年健康、小小金融家、马术中心、盾构装备、计量探秘等宝藏点位，面向市民/青少年/亲子公开报名。',
      how='把「城市级国企开放日」做成文旅化公众 campaign——以四大主题周（红色/科技/文化/服务）制造持续热度而非单场活动；用「专属路线+多点位打包」降低参与门槛、提升打卡完成率；国企主动敞开老厂房/实验室/文化空间做城市名片；报名走官方公众号+线上平台双通道，名额限时抢。',
      note='② 城市级国企开放日（上海市国资委官网一手），国资监管部门领导以城市服务者姿态，市民/青少年/亲子公众走进国企空间感受硬核科技与海派文化（整体为公众/市民向，非家庭日）。'),
 dict(emoji='🧠', title='中科院脑智卓越中心 2026「脑智擘未来」公众科学日（脑机接口·VR·科普市集）', cat='科研院所开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://cebsit.cas.cn/cxwh/kphd/202605/t20260518_8203753.html',
      val='中科院脑科学与智能技术卓越创新中心在第二十二届公众科学日，以「脑智擘未来」为主题，通过科普市集、科学家精神演讲、实验室开放、科普报告进校园、实验室探访直播等，把脑科学前沿转化为可感可参与的科普体验；公众在「脑电对抗」「意念球场」「假手错觉」中体验专注力可视化，佩戴 VR 漫游「脑中森林」、操作荧光标记与共聚焦成像，中小学生按「提出问题—设计实验—采集—分析」完整流程像科学家一样思考。',
      how='把「科研院所开放日」做成沉浸式科学启蒙——用科普市集+互动实验（脑机接口/VR/荧光成像）把高深神经科学变可动手参与；以「完整科研流程」引导青少年像科学家思考而非走马观花；科学家精神演讲把报国情怀融入体验；B 站等平台直播把线下数百人扩展到数百万覆盖。',
      note='② 科研院所公众开放日（中科院官网一手），研究中心领导以科学引路人姿态，中小学生/公众走进实验室体验脑机接口与 VR 神经漫游，科创启蒙+精神传承。'),
 dict(emoji='☢️', title='中科院核能安全所 2026 公众科学日（液态金属回路·辐射真相·核科普）', cat='科研院所开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.inest.cas.cn/new/xwdt/jqyw/202605/t20260519_838285.html',
      val='中科院合肥物质院核能安全技术研究所公众科学日，以「赴科学之约，赋未来之翼」为主题，通过实验室开放、专题科普报告、互动体验普及核能安全知识；公众分组步入液态金属回路与材料技术综合实验平台，听讲解员讲液态金属冷却与材料相容性，感叹「比书本直观得多」；四场循环报告《辐射的真相与防护》《先进能源，「核」平开「辐」》等理性解读辐射与核电安全，微堆核电源缩比模型旁科研志愿者驻场讲解。',
      how='把「核科普开放日」做成理性破误解场——用大型液态金属回路实景装置建立直观认知，替代照本宣科；四场循环科普报告（辐射真相/核电安全/航天核电源）兼顾科学深度与生活趣味，现场答疑消除常见恐惧；知识问答+缩比模型互动把深奥核科学变可感可触，青少年心中播下科学种子。',
      note='② 科研院所公众开放日（中科院官网一手），核能安全所领导以科普使者姿态，公众/青少年零距离探秘先进核能装置、理性认识辐射与核电安全。'),
 dict(emoji='💎', title='中科院固体所 2026 公众科学日（材料之美·气凝胶·微结构摄影）', cat='科研院所开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://issp.cas.cn/gts/xwzx/zhxw/202605/t20260518_838189.html',
      val='中科院合肥物质院固体物理研究所公众科学日，以「解锁科学奥秘 感受材料之美」为主题，通过开放实验室、趣味实验、微结构摄影展献上沉浸式科学盛宴；资源创新中心展示废弃物资绿色资源化利用关键技术，服务国家资源安全战略；趣味实验（火山爆发/水力发电/静电感应）让小朋友动手领悟原理；副研究员讲《探秘物质的大与小》、博士后讲《世界上最轻的固体——气凝胶》，微结构摄影《石墨羚跃苍穹》等以显微视角呈现结构之美。',
      how='把「材料所开放日」做成艺术+科学融合体验——用微结构摄影展（显微视角+艺术命名）把科研图像变可欣赏的美学作品，拉近公众与材料科学距离；趣味小实验+通俗报告（气凝胶/纳米材料）让深奥概念易懂；废弃物资绿色循环展区绑定国家资源安全战略，科普即责任传达。',
      note='② 科研院所公众开放日（中科院官网一手），固体所领导以科研摆渡人姿态，公众/中小学生看材料之美、动手悟科学原理、读懂绿色循环战略。'),
 dict(emoji='🤖', title='成都智算中心「探秘智算·启迪未来」开放日（青少年 AI 算力科普·分年级场次）', cat='科技/AI 开放日',
      rel='r2', src='二手', src_cls='b2',
      url='https://www.toutiao.com/article/7621004724006896174',
      val='成都智算中心（国家新一代人工智能公共算力开放创新平台、西南首家获科技部批复）举办「探秘智算·启迪未来」开放日，面向 1—9 年级中小学生分 4 场次、按年级设专业讲解；青少年穿越 AI 时空隧道看全球算力格局，近距离参观 HCSO 机房、Atlas 机房及电力模块间，了解服务器集群部署与算力运行逻辑，走进冷冻站与柴发楼理解大型智算平台稳定高效运行，约 200 名学生参与。',
      how='把「AI 算力中心开放日」做成青少年科普入口——以「分年级场次+专属讲解」保证不同学段获得感；用机房/冷冻站/柴发楼实景把抽象「算力」变可触可感；时空隧道展陈全球算力格局与中美对比，建立宏观认知；定位国家公共算力平台做常态化科普，持续为 AI 人才梯队播种。',
      note='② 科技/AI 公众开放日（成都高新/今日头条二手），智算中心运营方以科普教育者姿态，中小学生走进「最强大脑」机房理解 AI 算力基础设施（非 IR/资本向）。'),
 dict(emoji='📊', title='2026 数博会设置公众开放日（专业观众日+公众开放日分层·AI 互动）', cat='展会公众开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.guiyang.gov.cn/jdhy/xinwenfabuhui_new/2026/2026zggjdsjcyblhzyzlxwfbhmttqy/mtbd/202607/t20260710_90606759.html',
      val='2026 中国国际大数据产业博览会专业展览设置公众开放日（共三天）：第一天为专业观众日，面向企业从业者、行业专家、政企采购负责人，打造安静专注的深度洽谈环境；后三日面向全体市民、学生群体开放，聚焦数字科技科普、AI 互动体验，向大众普及大数据与人工智能知识；展期推出打卡互动、展区直播、「数博有礼」、媒体交流区等，做到产业专业性与科普普惠性双向兼顾。',
      how='把「大型展会开放日」做成专业/公众分层——用「专业观众日+公众开放日」双时段既保商务洽谈深度、又做大众科普普惠，避免两类人群互相干扰；定向邀约产业链上下游/政企采购组专属观展团配领队+讲解员提对接效率；公众日主打 AI 互动体验+打卡传播，把展会声量放大到社交平台。',
      note='② 展会公众开放日（贵阳市政府官网一手），展会主办以城市服务者姿态，市民/学生/政企采购分层参与，数字科普+商务洽谈双兼顾（非 IR/资本向）。'),
 dict(emoji='🧩', title='2026「众智」大模型开放智算生态协同高级别开放日（信通院·软硬件协同中心首开放）', cat='AI 生态开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://so.html5.qq.com/page/real/search_news?docid=70000021_6636a4ba09972052',
      val='中国信通院主办的 2026「众智」大模型开放智算生态协同高级别开放日活动，人工智能软硬件协同创新与适配验证中心首次面向全社会开放参观，设生态监测区、算力实验区、适配实验区、实测验证区、开源布道区、产学研共创区，覆盖产业研究、测试验证、供需对接、生态培育全环节，当日 300 余人次现场参观；同步启动第三届「兴智杯」全国人工智能创新应用大赛云智专项赛，邀中国电信、华为昇腾、无问芯穹、浪潮、北大、智源等专家分享。',
      how='把「AI 生态开放日」做成产学研共创窗口——以软硬件协同创新中心首次全社会开放，把测试验证/适配/供需对接全环节可视化；用「生态监测+算力实验+开源布道+产学研共创」多区组合展示开放智算体系进展；借高级别开放日+大赛启动聚合电信/华为/高校院所，把开放日变生态连接与人才发现场。',
      note='② AI 生态公众/行业开放日（中国信通院 CAICT 一手），信通院领导以生态组织者姿态，产业界/学界/公众走进软硬件协同创新中心看国产智算生态（行业开放日向，非 IR/资本向）。'),
 dict(emoji='🎭', title='2026 首场「知音湖北 超级文旅日」暨第五届湖北非遗嘉年华（省级文旅 IP·消费券·国际会客厅）', cat='文旅/非遗开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.mct.gov.cn/gtb/index.jsp?url=https%3A%2F%2Fwww.mct.gov.cn%2Fwhzx%2Fqgwhxxlb%2Fhb_7730%2F202601%2Ft20260119_964176.htm',
      val='文化和旅游部报道：2026 首场「知音湖北 超级文旅日」暨第五届湖北非遗嘉年华在武汉启幕，作为省级文旅战略品牌下创新 IP，汇聚近 200 个非遗项目、500 余位非遗传承人、3000 余款非遗精品与特色文旅产品集中展销；集文化展陈、技艺交流、沉浸体验、惠民消费于一体，发布 6000 万元消费礼包、3000 万元票根礼遇、2400 万元文旅消费券；「荆楚非遗国际会客厅」揭牌，「一带一路」商协会与湖北非遗企业达成多项合作，中英双语宣传册经 50 余国商协会分发。',
      how='把「文旅开放日」做成省级 IP+惠民消费组合——以「超级文旅日」省级品牌串联非遗嘉年华，用近 200 项非遗+沉浸体验+惠民消费券把文化资源转化为可参与可带走的文旅消费；设国际会客厅+双语宣传册把荆楚文化推向海外；消费礼包/票根礼遇做流量转化，文旅融合+全民共享。',
      note='② 文旅/非遗公众开放日（文化和旅游部官网一手），文旅主管部门领导以文化共建者姿态，市民游客/非遗传承人/海外商协会同场，非遗活化+惠民消费+国际传播（非家庭日）。'),
 dict(emoji='🏭', title='中宁工业园区 2026「政府开放日」（园区管委会·7 工作日闭环处置）', cat='政企开放日',
      rel='r3', src='一手', src_cls='b1',
      url='https://www.znzf.gov.cn/xxgk/zfxxgkml/zfkfr/hdfa/202608/t20260813_5312756.html',
      val='中宁工业园区管委会 2026 年「政府开放日」以「开放共享，共创未来」为主题，面向园区企业、职工、群众代表（40 人以内）开放；核心三板块：全域工作宣讲解读（组织架构/招商引资/安全监管/生态治理）、民意诉求征集与闭环处置、沉浸式实地观摩（走进政务机关+政务服务场地+会议会务场所）；活动后第一时间逐条梳理意见建议、建档登记、专题研讨，确保在 7 个工作日内完成采纳与处置情况公示公开。',
      how='把「园区政企开放日」做成营商环境闭环工程——以「宣讲+观摩+座谈」全景展示园区履职，破除政务信息壁垒；用「7 工作日闭环处置+公示公开」把企业/群众诉求从收集转实质解决，忌单向宣讲；限定代表覆盖行业/群体保广泛性，是园区级政企对话与助企纾困可复制模板。',
      note='③ 园区政企开放日（中宁县政府官网一手），园区管委会领导以产业服务者姿态，入驻企业/职工/群众代表走进机关共商营商环境，政企协作+7 日闭环（高管间/政企协作向，非 IR/资本向）。'),
 dict(emoji='🗣️', title='章贡区 2026 政府开放日+营商环境「吐槽大会」（园区企业专场·区领导现场办公）', cat='政企开放日',
      rel='r3', src='一手', src_cls='b1',
      url='https://www.zgq.gov.cn/zgqzf/c105773/202606/90bbf85b22bb405a8fedf401cd763731.shtml',
      val='章贡区 2026 年政府开放日+营商环境「吐槽大会」——园区企业专场在章贡高新区举行，区领导出席，邀虔东稀土、方大智造、开源自动化、佳腾电业等 10 家企业代表，区金融服务中心、科技局、城管局、交管大队、交通运输局等 8 个单位现场倾听；会前企业代表走进管委会看展厅与政务服务大厅，感受营商环境成效；「吐槽大会」环节 10 家企业围绕人才引进、融资贷款、交通物流、要素保障、政策兑现坦诚「吐槽」建言，相关单位现场逐一回应、能解决的明路径、需协调的限时反馈。',
      how='把「政企开放日」做成诉求现场办公——以「吐槽大会」形式让企业代表直言痛点堵点，区领导+多部门现场接招、当场交办，把「槽点」变「亮点」、「难点」变「支点」；会前参观管委会建信任、会中坦诚对话破隔阂、会后限时反馈成闭环，是政企同心「双向奔赴」的高管间沟通范式。',
      note='③ 政企开放日（章贡区政府官网一手），区领导以发展服务者姿态，重点企业负责人走进高新区管委会「吐槽」建言、多部门现场办公，政企高管对话+营商环境闭环（高管间/政企协作向，非 IR/资本向）。'),
]

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

html = open(HTML, encoding='utf-8').read()
cur2 = html.count('badge r2">上下级<')
cur3 = html.count('badge r3">高管间<')
print(f'current wall: ②={cur2} ③={cur3} (hl divs={html.count(chr(34)+"hl"+chr(34))})')

# inject ② at end of sec2 grid (before sec3 marker)
marker = '  <div class="sec sec3">'
idx = html.find(marker)
assert idx != -1, 'sec3 marker not found'
html = html[:idx] + '\n'.join(card_html(c) for c in cards2) + '\n' + html[idx:]
# inject ③ at top of sec3 grid
j = html.find('<div class="sec sec3">')
k = html.find('<div class="hl">', j)
assert k != -1, 'no hl in sec3'
html = html[:k] + '\n'.join(card_html(c) for c in cards3) + '\n' + html[k:]

# update sec2 / sec3 tag counts
m2 = re.search(r'(<div class="sec sec2">.*?<span class="tag">)(\d+)( 卡</span>)', html, re.S)
assert m2, 'sec2 tag not found'
html = html[:m2.start()] + m2.group(1) + str(cur2+n2) + m2.group(3) + html[m2.end():]
m3 = re.search(r'(<div class="sec sec3">.*?<span class="tag">)(\d+)( 卡</span>)', html, re.S)
assert m3, 'sec3 tag not found'
html = html[:m3.start()] + m3.group(1) + str(cur3+n3) + m3.group(3) + html[m3.end():]

# hero append r27 segment
HERO_ANCHOR = ('二十六轮补采 2026-08-25(+6，啤酒40周年/造船实验室/联通黑龙江科创/威海博物馆/于都政企/'
               '济南活力民营·4②2③)')
assert HERO_ANCHOR in html, 'hero r26 tail not found'
seg_r27 = ('｜ 二十七轮补采 2026-08-26(+10，上海国企开放日城市级/脑智中心脑机接口/核能安全所核科普/'
           '固体所材料之美/成都智算AI/数博会公众开放日/信通院智算生态/知音湖北文旅/'
           '中宁工业园区闭环/章贡吐槽大会·8②2③，9一手+1二手)')
html = html.replace(HERO_ANCHOR, HERO_ANCHOR + seg_r27, 1)

open(HTML, 'w', encoding='utf-8').write(html)
b1c = html.count('badge b1"')
b2c = html.count('badge b2"')
print(f'OK wall updated: ②={cur2+n2} ③={cur3+n3} (hl now {html.count(chr(34)+"hl"+chr(34))}), footer={html.count("本页由 yitong 沉淀整理")}, b1={b1c} b2={b2c}')

# .run_newcards.tmp.html
with open(TMP, 'w', encoding='utf-8') as f:
    for c in cards:
        f.write(card_html(c) + '\n')
print(f'OK {TMP} written ({os.path.getsize(TMP)}B)')

# index.json
idx_data = json.load(open(IDX, encoding='utf-8'))
before = len(idx_data)
for c in cards:
    idx_data.append({
        'title': c['title'],
        'normKey': c['title'],
        'url': c['url'],
        'sourceType': 'primary' if c['src']=='一手' else 'secondary',
        'relation': 'supervisor' if c['rel']=='r2' else 'exec',
        'summary': c['val'][:120],
        'topic': 'openday',
    })
json.dump(idx_data, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'OK index.json {before} -> {len(idx_data)} (+{len(cards)})')

# .rows_cache.json
cache = json.load(open(CACHE, encoding='utf-8'))
for c in cards:
    cache.append([c['title'], c['src'], '②上下级' if c['rel']=='r2' else '③高管间', c['val']])
json.dump(cache, open(CACHE, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'OK rows_cache.json {len(cache)-len(cards)} -> {len(cache)}')

# ---------- Obsidian summary note ----------
def rel_short(c): return '②上下级' if c['rel']=='r2' else '③高管间'
def one_line(c):
    one = c['note']
    if '：' in one: one = one.split('：',1)[1]
    return one.rstrip('）。').strip()

sum_txt = open(OB_SUM, encoding='utf-8').read()
assert '（共 197 张）' in sum_txt, 'abstract 197 not found'
sum_txt = sum_txt.replace('（共 197 张）', '（共 207 张）', 1)
AB = '二十六轮补采 2026-08-25(+6：啤酒40周年/造船实验室/联通黑龙江科创/威海博物馆/于都政企/济南活力民营·4②2③，2一手+4二手)**。'
assert AB in sum_txt, 'abstract r26 tail not found'
sum_txt = sum_txt.replace(AB,
    '二十六轮补采 2026-08-25(+6：啤酒40周年/造船实验室/联通黑龙江科创/威海博物馆/于都政企/济南活力民营·4②2③，2一手+4二手)**'
    ' + **二十七轮补采 2026-08-26(+10：上海国企开放日城市级/脑智中心脑机接口/核能安全所核科普/固体所材料之美/成都智算AI/数博会公众开放日/信通院智算生态/知音湖北文旅/中宁工业园区闭环/章贡吐槽大会·8②2③，9一手+1二手)**。', 1)
WALL_HDR = '## 卡片墙（HTML 交互版）'
assert WALL_HDR in sum_txt
table_rows = '\n'.join(
    f'| {c["title"]}（openday.html） | 4 | {c["src"]} | {rel_short(c)} | {one_line(c)} |'
    for c in cards) + '\n'
sum_txt = sum_txt.replace(WALL_HDR, table_rows + WALL_HDR, 1)
R26_LINK = '当轮独立页（第二十六轮）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/runs/openday-20260825-r26.html'
assert R26_LINK in sum_txt
sum_txt = sum_txt.replace(R26_LINK, R26_LINK + '\n' + f'- 当轮独立页（第二十七轮）：{GH_RUN}', 1)
# line 234 stale counts
assert '**197 卡**' in sum_txt, 'stale 197 卡 not found'
sum_txt = sum_txt.replace('**197 卡**', f'**{b1c + b2c} 卡**', 1)
assert '一手 110 + 二手 87' in sum_txt, 'stale 一手/二手 not found'
sum_txt = sum_txt.replace('一手 110 + 二手 87', f'一手 {b1c} + 二手 {b2c}', 1)
old_split = '②上下级 151 卡 / ③高管间 18 卡（含 12 张双档 ②+③）'
if old_split in sum_txt:
    sum_txt = sum_txt.replace(old_split, f'②上下级 {cur2+n2} 卡 / ③高管间 {cur3+n3} 卡（含双档 ②+③）')
open(OB_SUM, 'w', encoding='utf-8').write(sum_txt)
print(f'OK summary note updated (count 207={sum_txt.count("共 207 张")}, r27 seg={sum_txt.count("二十七轮补采 2026-08-26")})')

# ---------- Obsidian 00-index ----------
idx_txt = open(OB_IDX, encoding='utf-8').read()
HDR_TAIL = ('2026-08-25 二十六轮补采 +6（啤酒40周年/造船实验室/联通黑龙江科创/'
            '威海博物馆/于都政企/济南活力民营·4②2③）')
assert HDR_TAIL in idx_txt, '00-index header r26 tail not found'
idx_txt = idx_txt.replace(HDR_TAIL,
    HDR_TAIL + '｜ 2026-08-26 二十七轮补采 +10（上海国企开放日城市级/脑智中心脑机接口/核能安全所核科普/固体所材料之美/成都智算AI/数博会公众开放日/信通院智算生态/知音湖北文旅/中宁工业园区闭环/章贡吐槽大会·8②2③）', 1)
PTR = '📄 主题汇总笔记：[[知识采集库/素材/openday/OpenDay-开放日-知识卡汇总|OpenDay-开放日-知识卡汇总]]'
assert PTR in idx_txt, '00-index summary pointer not found'
new_rows = '\n'.join(
    f'| {c["title"]}（openday.html） | 4 | {c["src"]} | {rel_short(c)} | 二十七轮新增 |'
    for c in cards) + '\n'
idx_txt = idx_txt.replace(PTR, new_rows + PTR, 1)
open(OB_IDX, 'w', encoding='utf-8').write(idx_txt)
print(f'OK 00-index updated (r27 rows {idx_txt.count("二十七轮新增")})')

# ---------- Obsidian runs note ----------
run_md = f'''---
title: Open Day 开放日 第二十七轮知识卡
tags: [知识采集, 开放日, 自动化采集, 轮次]
date: 2026-08-26
type: 自动化采集
---

# Open Day 开放日 · 第二十七轮补采（2026-08-26）

- 本轮新增 **10 卡**（②上下级 8 · ③高管间 2），0 peer（硬约束）
- 一手 9 / 二手 1
- 累计墙：openday.html 197 → 207 卡（② {cur2+n2} / ③ {cur3+n3}）
- 新域：上海国企开放日城市级 campaign（80+场四大主题周）/ 中科院脑智中心脑机接口 / 核能安全所核科普 / 固体所材料之美 / 成都智算中心 AI 科普 / 数博会公众开放日分层 / 信通院智算生态开放日 / 知音湖北超级文旅日 / 中宁工业园区营商环境 7 日闭环 / 章贡吐槽大会（政企现场办公）
- 硬排除：家庭日/家属开放日、投资者关系/证券监管/资本市场/财经媒体类开放日（命中资本市场/IR/证监局即跳过）

## 本轮卡片

| 卡 | 质量分 | 一手/二手 | 适用关系 | 一句话定位 |
|---|---|---|---|---|
'''
for c in cards:
    run_md += f'| {c["title"]}（[openday.html]({GH})） | 4 | {c["src"]} | {rel_short(c)} | {one_line(c)} |\n'
run_md += f'''
## 链接
- 累计卡片墙：{GH}
- 当轮独立页：{GH_RUN}
- 主题汇总笔记：[[知识采集库/素材/openday/OpenDay-开放日-知识卡汇总|OpenDay-开放日-知识卡汇总]]
'''
os.makedirs(os.path.dirname(OB_RUN), exist_ok=True)
open(OB_RUN, 'w', encoding='utf-8').write(run_md)
print(f'OK runs note: {OB_RUN} ({os.path.getsize(OB_RUN)}B)')

print('DONE pipeline core.')
