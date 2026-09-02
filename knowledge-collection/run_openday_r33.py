# -*- coding: utf-8 -*-
# Open Day 三十三轮补采（r33, 2026-09-03）+6 卡：4 ③高管间 + 2 ②上下级
# 新域（③高管间稀疏缺口补采）：第四届链博会公众开放日+APEC工商领导人中国论坛联动、第十三届服贸会公众开放日、
#       2026世界互联网大会乌镇峰会、第七届跨国公司领导人青岛峰会（政企/企企高层对话向）
#       ②上下级新源：六安市地震局政务开放日、银川住房公积金管理中心政务开放日
import re, os, json, sys, subprocess, datetime, urllib.request, urllib.error, ssl

WS = r"C:\Users\v_yitcai\WorkBuddy\20260728154244"
KC = os.path.join(WS, "knowledge-collection")
HTML = os.path.join(KC, "openday", "openday.html")
IDX = os.path.join(KC, "index.json")
OB_SUM = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\openday\OpenDay-开放日-知识卡汇总.md"
OB_IDX = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
OB_RUN = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\openday\runs\OpenDay-2026-09-03-第三十三轮-知识卡.md"
GH = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday.html"
RUN_DATE = "20260903"
RUN_PAGE = f"openday-2026-09-03-r33.html"
GH_RUN = f"https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/runs/{RUN_PAGE}"
MAP = os.path.join(KC, "lexiang-entry-map.json")
TMP = os.path.join(KC, "openday", ".run_newcards.tmp.html")
TOPIC_TXT = os.path.join(KC, "last-topic.txt")

cards = [
 dict(emoji='🔗', title='第四届中国国际供应链促进博览会2026（6.22-26北京·社会公众免费开放+APEC工商领导人中国论坛同期）', cat='链博会公众开放日',
      rel='r3', src='一手', src_cls='b1',
      url='https://www.ccpit.org/a/20260522/20260522h3nx.html',
      val='第四届中国国际供应链促进博览会6月22-26日在北京中国国际展览中心（顺义馆）举办，由中国贸促会主办，是全球首个以供应链为主题的国家级展会，主题“链接世界，共创未来”。设置“6链1展区”（数智科技链、先进制造链、绿色农业链、健康生活链、智能汽车链、清洁能源链+供应链服务展区），已有676家中外企业确认参展、实际参展商有望破1200家，外资参展商占36.5%、世界500强及行业龙头占65%+。展期22日下午至24日面向专业观众、25-26日面向社会公众免费注册入场；开幕前一天（6.21）在京举办2026年APEC工商领导人中国论坛（APEC“中国年”工商领域标志性活动）；展期60多场工商交流活动，发布2026版《全球供应链促进报告》；跨国企业独创“找朋友”模式升级至4.0（线上线下/国内国外/展前展后），澳大利亚任主宾国、安徽/海南任主宾省。',
      how='把“链博会公众开放日”做成国家级开放平台双向对话场——以“公众免费开放+跨国CEO闭门对话+APEC论坛联动”组合，用“6链1展区”把供应链上下游/大中小企业/产学研用系统呈现；以世界500强高管+多国官员同台制造高规格对话；“找朋友”4.0模式把会展流量变长期伙伴，是国家级开放平台政企/企企高层交流范本（中国贸促会/链博会官网一手）。',
      note='③ 第四届链博会公众开放日+APEC工商领导人中国论坛联动（中国贸促会官网一手），贸促会以开放合作推动者姿态，世界500强高管/多国官员/APEC工商界围坐对话供应链与亚太合作（政企/企企协作向，非IR/资本向）。'),
 dict(emoji='🌐', title='2026年中国国际服务贸易交易会（第十三届服贸会·9.9-13北京首钢园·专业观众日+公众开放日）', cat='服贸会公众开放日',
      rel='r3', src='一手', src_cls='b1',
      url='https://www.ciftis.org/',
      val='2026年中国国际服务贸易交易会（第十三届服贸会）9月9-13日在北京首钢园举办，主题“全球服务，互惠共享”，实行全员实名制线上预约。分专业观众日（9.9-11，单日票20元/三日通票50元）与公众开放日（9.12-13，实名预约免费参观）两大时段；设置九大专题展（电信计算机和信息服务、金融服务、文旅服务、教育服务、体育服务、运输和商务服务、工程咨询与建筑服务、健康卫生服务、环境与能源服务）及国别展、省区市及港澳台展；首钢园“会展小镇”全新亮相，全新增设“出海专区”“中小企业专区”“出海服务推介路演区”，近70家企业带来百余项创新“首发”；配套活动含投融资对接（金融之夜、投资石景山等）、消费市集、体育赛事、文艺演出等。',
      how='把“服贸会公众开放日”做成国际经贸盛会双段运营范本——以“专业观众日/公众开放日分段+实名预约+九大专题展分区”替代单一开放，用“会展小镇+出海专区+中小企业专区”把服务贸易变可逛可谈场景；以投融资对接（金融之夜/投资石景山）制造政企/企企高层对话入口，是国家级国际经贸盛会开放运营与开放合作范本（服贸会官网一手）。',
      note='③ 服贸会公众开放日+出海/投融资对接（服贸会官网一手），首都会展集团以开放合作推动者姿态，跨国企业/金融机构/中小企业围绕服务贸易与出海围坐对接（政企/企企协作向，非IR/资本向）。'),
 dict(emoji='💻', title='2026世界互联网大会乌镇峰会（全球互联网领域最高层级国际盛会·政商学界高端对话）', cat='乌镇峰会开放对话',
      rel='r3', src='一手', src_cls='b1',
      url='https://www.wicinternet.org/',
      val='世界互联网大会（WIC）是2022年成立于北京的国际组织，乌镇峰会为其旗舰活动，是全球互联网领域最高层级国际盛会。2026年乌镇峰会筹备工作推进中（8.24秘书处召开分论坛第一次筹备工作会议），历届设置“携手构建网络空间命运共同体”精品案例发布、“领先科技奖”、“互联网之光”博览会、“直通乌镇”全球互联网大赛、全球青年领军者计划、杰出贡献奖等板块；大会汇聚全球政要、国际组织负责人、跨国企业CEO、顶尖学者，围绕人工智能治理、数字创新、网络安全、数字经济等前沿议题开展高端对话，是世界观察数字中国与全球网络空间治理的重要窗口。',
      how='把“乌镇峰会”做成全球数字治理高层对话场——以“精品案例发布+领先科技奖+互联网之光博览会+全球大赛”组合，把网络空间命运共同体理念变可参与的国际公共产品；用政要/跨国CEO/顶尖学者同台闭门与分论坛对话，制造政企/学跨界高端协作入口，是国家级国际组织平台高层对话范本（世界互联网大会官网一手）。',
      note='③ 乌镇峰会（世界互联网大会官网一手），大会秘书处以全球数字治理推动者姿态，政要/跨国企业CEO/顶尖学者围绕AI治理与数字经济闭门与分论坛对话（高管间/政企学协作向）。'),
 dict(emoji='🌏', title='第七届跨国公司领导人青岛峰会2026（6.15-17·“携手十五五 向新向未来”·357家跨国企业）', cat='青岛峰会政企对话',
      rel='r3', src='一手', src_cls='b1',
      url='https://www.mncsummit.org.cn/lbt/811253471486021.html',
      val='第七届跨国公司领导人青岛峰会6月15-17日在青岛举办，由商务部、山东省政府共同举办，紧扣“携手‘十五五’ 向新向未来”主题，是面向跨国公司的重大机制性活动。开幕式及主论坛、会见会谈、平行论坛三大板块共29场活动，确认参会企业嘉宾435人（境外跨国公司355人来自36国和地区、境内80人多为世界500强及行业领军企业领导人）；平行论坛23场涵盖投资促进、贸易对接、行业交流、区域合作四类；举办国际城市合伙人对话会（路易达孚、阿斯利康、采埃孚、埃森哲、贝卡尔特等参与）、跨国科创论坛、山东港口全球供应链大会、“中国康湾”对接会；继续发布《跨国公司在中国》研究报告，首次在高质量发展论坛介绍“十五五”知识产权保护政策安排，形成“政策解读—诉求收集—精准回应”闭环。',
      how='把“跨国公司领导人青岛峰会”做成城市级政企高层对话场——以“开幕式主论坛+国际城市合伙人对话会+跨国科创论坛”组合，用世界500强领导人围坐共话“十五五”开放政策，把城市产业优势变全球合作入口；以“政策解读—诉求收集—精准回应”闭环把开放日变成务实合作，是地方嵌入国家级政企高层对话范本（青岛峰会官网/商务部一手）。',
      note='③ 跨国公司领导人青岛峰会（青岛峰会官网/商务部一手），山东省/青岛市领导以城市合伙人姿态，世界500强企业领导人围绕“十五五”开放与深度投资围坐对话（政企/企企协作向，非IR/证券向）。'),

 dict(emoji='🌍', title='六安市地震局2026“政府开放日”暨“防灾减灾日”活动（市人大代表/政协委员走进地震监测一线）', cat='地震局政务开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.luan.gov.cn/xxgk/ztzl/zfkfr/sjzfkfr/10765097.html',
      val='5月12日第18个全国防灾减灾日，六安市地震局联合市科协、六安地震监测中心站举办2026年“政府开放日”暨“防灾减灾日”活动，由市地震局党组成员、总工程师李建厅主持，邀请市人大代表、政协委员走进地震监测一线。代表们实地参观地震台院内监测设施、监测大楼及预警终端设备，工作人员详解监测网络布局、仪器运行、数据处理与预警发布；在市地震科普馆通过实景模拟、互动展项、实物模型直观了解地震成因、建筑抗震设防，沉浸式学应急避险与自救互救；六安地震监测中心站专家开展专题科普讲座，结合案例讲应急处置、科学避险、谣言识别、家庭应急物资储备。活动搭建政府与群众沟通桥梁，展现防震减灾工作成效与科技实力。',
      how='把“地震局政府开放日”做成政务透明+科普沉浸课——以“监测一线实地参观+科普馆互动+专家讲座”三段式，把防震减灾专业工作变可感可学；用市人大代表/政协委员作为首批体验者，把政务公开从“向社会公布”升级为“请代表走进一线监督”；紧扣防灾减灾日节点，是地震系统政务开放日向范本（六安市政府官网一手）。',
      note='② 地震局政务开放日（六安市政府官网一手），市地震局领导以公共安全服务者姿态，人大代表/政协委员走进地震监测一线、读懂防震减灾全流程。'),
 dict(emoji='🏦', title='银川住房公积金管理中心2026“政府开放日”（“惠民公积金 服务暖人心——阳光政务·携手同行”）', cat='公积金政务开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://gjj.yinchuan.gov.cn/info/1288/32738.htm',
      val='银川住房公积金管理中心2026年8月20日以“惠民公积金 服务暖人心——阳光政务·携手同行”为主题举办“政府开放日”，通过电话报名及单位推荐邀请约10名市民代表、企业代表及缴存职工代表参加。代表们走进金凤分中心服务大厅，现场观摩受委托银行窗口受理审核及复审区复审工作全流程，“零距离”体验公积金业务从申请到审批的规范运作；座谈会上中心党组成员、副主任付文侠通报2026年上半年工作成效，归集管理科、住房信贷科负责人深度解读购房首付提取、“一人购房全家帮”、租房提取增效、退役军人贷款额度上浮、多子女家庭贷款支持、灵活就业人员缴存补贴等惠民利企政策，并现场演示网上服务大厅功能；与会代表围绕政银数据共享、联合政策宣传、常态化沟通机制提建议，中心逐条梳理吸纳。',
      how='把“公积金政府开放日”做成民生政策透明窗——以“服务大厅实景观摩+政策深度解读+座谈纳谏”组合，把提取/贷款/网办等抽象政策变可感知服务；用“一人购房全家帮”“灵活就业缴存补贴”等具体惠民条款具象化政务公开；现场演示“数字公积金”把数字化转型变直观体验，是公积金系统阳光政务范本（银川公积金中心官网一手）。',
      note='② 公积金管理中心政务开放日（银川公积金中心官网一手），中心领导以惠民服务者姿态，市民/企业/缴存职工代表走进服务大厅、读懂公积金惠民政策全流程。'),
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

# hero append 三十三轮 segment after 三十二轮 tail
HERO_ANCHOR = '三十二轮补采 2026-09-02(+6，抚州市中医医院/文登区人社局/浔阳区人社局开放日向·3②，3一手 ｜ 2026进博会上海会议活动/第九届虹桥国际经济论坛/夏季达沃斯天津城市会客厅·3③，2一手+1二手)'
assert HERO_ANCHOR in html, 'hero r32 tail not found'
seg_r33 = ('｜ 三十三轮补采 2026-09-03(+6：第四届链博会公众开放日/APEC工商领导人中国论坛/第十三届服贸会/乌镇峰会/跨国公司领导人青岛峰会·4③，4一手 ｜ '
           '六安市地震局/银川公积金中心政务开放日·2②，2一手)')
html = html.replace(HERO_ANCHOR, HERO_ANCHOR + seg_r33, 1)

foot_ok = html.count('📌 本页由 yitong 沉淀整理')
assert foot_ok >= 1, 'footer missing'
open(HTML, 'w', encoding='utf-8').write(html)
b1c = html.count('badge b1"')
b2c = html.count('badge b2"')
print(f'OK wall updated: ②={cur2+n2} ③={cur3+n3} (hl now {html.count(chr(34)+"hl"+chr(34))}), footer={foot_ok}, b1={b1c} b2={b2c}')

# ===== 2) incremental page via gen_run_page.py =====
open(TMP, 'w', encoding='utf-8').write('\n'.join(card_html(c) for c in cards))
print(f'OK tmp cards file: {TMP}')
gp = os.path.join(KC, "gen_run_page.py")
cmd = [sys.executable, gp, "--topic", "openday", "--topic-name", "Open Day 开放日",
       "--date", "2026-09-03", "--round", "33", "--cards-file", TMP]
r = subprocess.run(cmd, capture_output=True, text=True)
print('gen_run_page stdout:', r.stdout.strip())
if r.returncode != 0:
    print('gen_run_page stderr:', r.stderr.strip())
    raise SystemExit('gen_run_page failed')
INC = os.path.join(KC, "openday", "runs", RUN_PAGE)
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
    rows += f'| {c["title"]}（openday.html） | 4 | {c["src"]} | {relt} | 三十三轮新增 |\n'
ob_idx = ob_idx[:hi2] + rows + ob_idx[hi2:]
open(OB_IDX, 'w', encoding='utf-8').write(ob_idx)
print('OK 00 index appended %d card rows' % len(cards))

# ===== 5) Obsidian summary note =====
ob_sum = open(OB_SUM, encoding='utf-8').read()
anchor32 = '三十二轮补采 2026-09-02(+6：抚州市中医医院/文登区人社局/浔阳区人社局开放日向·3② + 2026进博会上海会议活动/第九届虹桥国际经济论坛/夏季达沃斯天津城市会客厅·3③，5一手+1二手)**'
assert anchor32 in ob_sum, 'round32 note not found'
round_note = ('\n\n+ **三十三轮补采 2026-09-03(+6：第四届链博会公众开放日/APEC工商领导人中国论坛/第十三届服贸会/乌镇峰会/跨国公司领导人青岛峰会·4③ '
              '+ 六安市地震局/银川公积金中心政务开放日·2②，6一手+0二手)**')
ob_sum = ob_sum.replace(anchor32, anchor32 + round_note, 1)
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
# stats
ob_sum = ob_sum.replace('（共 263 张）', '（共 270 张）')
ob_sum = ob_sum.replace('**263 卡**', '**270 卡**')
ob_sum = ob_sum.replace('一手 151 + 二手 112', '一手 158 + 二手 112')
ob_sum = ob_sum.replace('②上下级 236 卡 / ③高管间 42 卡', '②上下级 238 卡 / ③高管间 47 卡')
open(OB_SUM, 'w', encoding='utf-8').write(ob_sum)
print('OK summary note updated (摘要 +6 rows, 适用&备注 stats)')

# ===== 5b) Obsidian runs independent note =====
os.makedirs(os.path.dirname(OB_RUN), exist_ok=True)
run_lines = [f'# Open Day 开放日 · 第三十三轮补采（2026-09-03）独立笔记', '']
run_lines.append(f'- 独立页 GitHub Pages：{GH_RUN}')
run_lines.append(f'- 本地路径：`{INC}`')
run_lines.append(f'- 累计卡片墙：`{GH}`')
run_lines.append('')
run_lines.append(f'本轮新增 **{len(cards)}** 张（②上下级 {n2} · ③高管间 {n3}，6 一手 + 0 二手）：')
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
    round_rec['note'] = '轮次页 R33 (+%d)｜乐享待补传(whoami 探活失败/未连通，待重连后补传并回填 entry_id)' % len(cards)
else:
    round_rec['note'] = '轮次页 R33 (+%d)｜乐享已上传' % len(cards)
mapp['openday']['rounds'].append(round_rec)
json.dump(mapp, open(MAP,'w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('OK lexiang-entry-map updated (entry_id=%s)' % eid)

# ===== 7) advance topic pointer =====
open(TOPIC_TXT, 'w', encoding='utf-8').write('下午茶研讨\n')
print('OK last-topic.txt -> 下午茶研讨')

print('\n==== RUN SUMMARY ====')
print('主题: Open Day 开放日 (r33, 2026-09-03)')
print('覆盖关系档: 仅 上下级(②) / 高管间(③)，已剔除 平级/朋友向(①)')
print('新增 N=%d (②=%d, ③=%d) | 去重删 M=%d' % (len(cards), n2, n3, len(dropped)))
print('增量独立页: %s' % INC)
print('汇总墙: %s' % HTML)
print('GitHub Pages 独立页: %s' % GH_RUN)
print('乐享 entry_id=%s (%s)' % (eid, lmsg))
