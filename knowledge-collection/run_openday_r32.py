# -*- coding: utf-8 -*-
# Open Day 三十二轮补采（r32, 2026-09-02）+6 卡：3 ②上下级 + 3 ③高管间
# 新域：中医医院/中医药沉浸式开放日、人社(社保经办+劳动仲裁)政府开放日、人社就业创业招聘会开放日
#       ＋ 进博会上海会议活动(百场边会·闭门会占比提升)、第九届虹桥国际经济论坛、夏季达沃斯天津城市会客厅
import re, os, json, sys, subprocess, datetime, urllib.request, urllib.error, ssl

WS = r"C:\Users\v_yitcai\WorkBuddy\20260728154244"
KC = os.path.join(WS, "knowledge-collection")
HTML = os.path.join(KC, "openday", "openday.html")
IDX = os.path.join(KC, "index.json")
OB_SUM = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\openday\OpenDay-开放日-知识卡汇总.md"
OB_IDX = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
OB_RUN = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\openday\runs\OpenDay-2026-09-02-第三十二轮-知识卡.md"
GH = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday.html"
RUN_DATE = "20260902"
RUN_PAGE = f"openday-2026-09-02-r32.html"
GH_RUN = f"https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/runs/{RUN_PAGE}"
MAP = os.path.join(KC, "lexiang-entry-map.json")
TMP = os.path.join(KC, "openday", ".run_newcards.tmp.html")

cards = [
 dict(emoji='🌿', title='抚州市卫健委2026“政府开放日”走进市中医医院（沉浸式中医药体验·针灸热敏灸推拿）', cat='中医医院开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://wjw.jxfz.gov.cn/art/2026/6/26/art_4094_4457273.html',
      val='抚州市卫生健康委2026年“政府开放日”6.24在市中医医院赣东大道院区举行，邀社会各界代表走进医院、走近中医药，以零距离观摩、面对面交流、沉浸式体验了解“一站式”中医治未病健康服务模式。现场设中医药成果展示、健康知识讲座、中医药特色互动体验区；市民踊跃体验针灸、热敏灸、中医推拿等特色诊疗，亲身尝试耳部刮痧、四肢刮痧、耳穴压豆等中医特色护理项目；沉浸式实操让市民直观认知中医药防病治病优势。卫健委旨在通过零距离互动倾听意见建议，精准对接群众健康需求，以群众监督推动医疗服务持续优化升级。',
      how='把“中医医院开放日”做成中医药文化沉浸课——以“政府开放日+委直医院”双主体把卫健部门与群众距离拉近；用针灸/热敏灸/推拿/刮痧/耳穴压豆等可上手体验替代说教；把“治未病”理念变可感知的实操，是卫健系统政务公开与中医药文化普及融合范本（抚州市卫健委官网一手）。',
      note='② 中医医院/卫健开放日（抚州市卫健委官网一手），卫健委领导以健康服务者姿态，市民沉浸式体验中医药特色诊疗、共话医疗服务提升。'),
 dict(emoji='🏢', title='威海市文登区人社局2026“阳光政务 与民同行”政府开放日（社保智能经办+劳动争议仲裁庭）', cat='人社政务开放日',
      rel='r2', src='一手', src_cls='b1',
      url='http://www.wendeng.gov.cn/art/2026/8/25/art_78545_6567625.html',
      val='文登区人社局2026.8.21以“阳光政务 与民同行”为主题举办政府开放日，邀企业代表、特约人员走进人社一线。现场观摩人社综合服务大厅、维权调解中心、劳动争议仲裁庭三大功能区：社保经办窗口演示“免填表”智能经办、服务监管系统，体验“数据多跑路、群众少跑腿”智慧人社；维权调解中心展示“仲裁-监察联办”机制与劳动维权全流程；仲裁庭实地观摩庭审布局与审理流程。座谈由分管领导、各业务科室负责人介绍就业创业、社保扩面、人才引育、劳动关系成效，并专题解读2026.7.1施行的《超龄劳动者基本权益保障暂行规定》。',
      how='把“人社开放日”做成民生政策透明窗——以“三大功能区实景观摩+座谈+专题政策解读”组合，把社保智能经办、劳动仲裁、维权调解等抽象职能变可感流程；用“免填表”智能经办与仲裁庭庭审具象化法治政府建设；专题解读新规章打通政策落地“最后一公里”，是人社系统阳光政务范本（文登区政府官网一手）。',
      note='② 人社政务开放日（威海市文登区政府官网一手），人社局领导以民生服务者姿态，企业代表/特约人员走进人社一线、读懂社保经办与劳动维权全流程。'),
 dict(emoji='💼', title='九江浔阳区人社局2026“就业创业服务招聘会暨政府开放日”（招聘现场沉浸式体验就业服务）', cat='人社就业开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.xunyang.gov.cn/zwzx/ztzl/rdzt/2026zfkfr/2026zfkfrhdbd/t_7291476.html',
      val='浔阳区人社局2026.7.9以“浔阳区2026年就业创业服务招聘会暨政府开放日”为主题在烟水亭广场举办政府开放日，辖区群众、企业用工代表受邀走进户外招聘服务现场，近距离沉浸式了解人社就业创业服务全流程。群众现场领取就业创业、社保维权宣传手册与办事指南，走访各企业招聘展位，实地了解岗位发布、供需对接、求职登记一站式就业服务；参观人社政策宣传展区，系统学习就业补贴、社保经办、创业担保贷款、劳动维权等惠民政策；业务负责人围绕就业帮扶、惠企政策现场讲解、巡回答疑。',
      how='把“人社开放日”办进招聘现场——以“招聘会+政府开放日”双场景融合，把政务公开阵地前移到求职一线；用“宣传手册+展位走访+政策展区+巡回答疑”把就业补贴/社保/创业贷款/劳动维权政策变可感服务；破除就业服务信息壁垒、打通服务群众“政务一公里”，是人社系统沉浸式政务公开范本（浔阳区官方网一手）。',
      note='② 人社就业开放日（浔阳区政府官网一手），人社局领导以就业服务者姿态，群众/企业用工代表在招聘现场零距离体验就业创业全流程服务。'),

 dict(emoji='🌐', title='2026进博会上海会议活动（约百场边会·小型研讨/闭门会/圆桌会占比显著提升）', cat='进博会边会闭门会',
      rel='r3', src='一手', src_cls='b1',
      url='https://www.ciie.org/zbh/cn/2024/medium-item1/people/20260817/63598.html',
      val='2026进博会上海会议活动11.6-9启幕，以“对话·破局·共生”为主题，锚定“十五五”开局，构建“1+2+X”体系（上海城市投资推介大会+浦东虹桥分论坛+约100场边会）。今年突出五提升：聚焦对外开放/企业出海/贸易创新/绿色发展/消费潜能/人工智能六大议题；汇聚全球政产学研，多家国际机构、多国政府官员、世界500强高管、两院院士同台；为促深度交流，50人以下小型研讨、闭门会、圆桌会占比明显提升，并设“上海会议活动”小程序支持一对一洽谈、会见预约；提供“管家式”服务（专属联络官、多语翻译、接驳专线、VIP停车），持进博会证件“无感入场”。',
      how='把“进博会边会”做成高管深度对话场——以“百场边会+小型闭门会/圆桌会占比提升”替代大会宣讲，用“1+2+X”体系把城市投资推介、分论坛、边会分层；以世界500强高管+多国官员+院士同台制造高规格对话；“管家式”服务+一对一洽谈小程序把会展流量变务实合作，是国家级开放平台政企/企企高层交流范本（中国国际进口博览局官网一手）。',
      note='③ 进博会上海会议活动边会/闭门会（进博局官网一手），城市主官/进博局以开放合作推动者姿态，世界500强高管/多国官员/院士围坐闭门圆桌、共探企业出海与开放新机遇（政企/企企协作向，非IR/资本向）。'),
 dict(emoji='🤝', title='第九届虹桥国际经济论坛2026（主题“稳定合作 共建开放型世界经济”·1+4板块含闭门会）', cat='虹桥国际经济论坛',
      rel='r3', src='一手', src_cls='b1',
      url='https://www.ifnews.com/news.html?aid=854028&cid=45',
      val='第九届虹桥国际经济论坛与2026进博会同期举办，7.27发布主题“稳定合作 共建开放型世界经济”，分论坛及闭门会延续“1+4”板块：“1”即报告发布暨国际研讨会（发布《世界开放报告2026》、世界开放指数、首发的《出口中国能力发展报告》双旗舰报告）；“4”即开放合作（坚守多边主义）、开放创新（科技新动能）、开放发展（绿色可持续全球化）、开放共享（可信赖的中国·政商对话）四大分论坛。商务部副部长鄢东、联合国驻华协调员等致辞，国内外知名学者、会员企业高管前瞻性解读，定位为国际政商学界高端对话平台、促进全球开放完善全球经济治理的国际公共产品。',
      how='把“虹桥论坛”做成顶级政商对话场——以“1+4”板块把报告发布、多边主义、科技新动能、绿色全球化、政商对话分层；用双旗舰报告+四大分论坛把中国开放实践与全球治理议题系统呈现；会员企业高管与多国官员同堂闭门/分论坛对话，是进博会框架下国家级高层政企沟通与开放信号释放范本（国际金融报/进博局一手信源）。',
      note='③ 虹桥国际经济论坛（IFNews/进博局一手信源），论坛秘书处/商务部以全球经济治理推动者姿态，跨国企业高管/多国官员/学者围绕开放型世界经济闭门与分论坛对话（高管间/政企协作向）。'),
 dict(emoji='🏙️', title='天津城市会客厅亮相2026夏季达沃斯（30+国家120+位代表·“展望智能经济新形态”）', cat='达沃斯城市会客厅',
      rel='r3', src='二手', src_cls='b2',
      url='http://www.ln.xinhua.org/20260625/39cd01f4f9eb429cbbe9ec2033e22926/c.html',
      val='天津城市会客厅活动在2026新领军者年会（夏季达沃斯）期间于大连举办，来自30余个国家和地区120余位国际组织代表、企业负责人、专家学者及创新机构代表齐聚，共话智能经济发展新趋势、共谋创新合作新机遇。活动以“展望智能经济新形态”为主题，设“天津机遇图景”“智能经济展望”“科技创新路演”“治城贤友对话”4环节，聚焦人工智能、超级计算、具身智能、脑机接口、生物制造等前沿领域，搭建国际交流合作平台，展示天津推动科技创新与产业创新深度融合、培育新质生产力的实践成果。天津市副市长李文海致辞。',
      how='把“城市会客厅”做成城市级高管对话场——以“达沃斯期间城市主题边会+四环节（机遇图景/智能经济展望/科创路演/治城贤友对话）”替代招商发布会，用副市长邀国际企业负责人/学者围坐共话智能经济，把城市产业优势变全球合作入口；以“城市会客厅”IP沉淀城市开放品牌，是地方在顶级国际论坛嵌入高管对话的范本（新华网二手/天津发布）。',
      note='③ 夏季达沃斯·天津城市会客厅（新华网二手），天津市领导以城市合伙人姿态，国际组织代表/跨国企业负责人/学者围坐对话智能经济与城市创新合作（政企/企企协作向，非IR/资本向）。'),
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

# hero append 三十二轮 segment after 三十一轮 tail
HERO_ANCHOR = '中美商业领袖圆桌会·3③，0一手+3二手)'
assert HERO_ANCHOR in html, 'hero r31 tail not found'
seg_r32 = ('｜ 三十二轮补采 2026-09-02(+6，抚州市中医医院/文登区人社局/浔阳区人社局开放日向·3②，3一手 ｜ '
           '2026进博会上海会议活动/第九届虹桥国际经济论坛/夏季达沃斯天津城市会客厅·3③，2一手+1二手)')
html = html.replace(HERO_ANCHOR, HERO_ANCHOR + seg_r32, 1)

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
       "--date", "2026-09-02", "--round", "32", "--cards-file", TMP]
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
    rows += f'| {c["title"]}（openday.html） | 4 | {c["src"]} | {relt} | 三十二轮新增 |\n'
ob_idx = ob_idx[:hi2] + rows + ob_idx[hi2:]
open(OB_IDX, 'w', encoding='utf-8').write(ob_idx)
print('OK 00 index appended %d card rows' % len(cards))

# ===== 5) Obsidian summary note =====
ob_sum = open(OB_SUM, encoding='utf-8').read()
anchor31 = '三十一轮补采 2026-09-01'
assert anchor31 in ob_sum, 'round31 note not found'
round_note = ('\n\n+ **三十二轮补采 2026-09-02(+6：抚州市中医医院/文登区人社局/浔阳区人社局开放日向·3② '
              '+ 2026进博会上海会议活动/第九届虹桥国际经济论坛/夏季达沃斯天津城市会客厅·3③，5一手+1二手)**')
ob_sum = ob_sum.replace(anchor31, anchor31 + round_note, 1)
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
ob_sum = ob_sum.replace('（共 255 张）', '（共 263 张）')
ob_sum = ob_sum.replace('**257 卡**', '**263 卡**')
ob_sum = ob_sum.replace('②上下级 233 卡 / ③高管间 39 卡', '②上下级 236 卡 / ③高管间 42 卡')
ob_sum = ob_sum.replace('一手 143 + 二手 114', '一手 148 + 二手 115')
open(OB_SUM, 'w', encoding='utf-8').write(ob_sum)
print('OK summary note updated (摘要 +6 rows, 适用&备注 stats)')

# ===== 5b) Obsidian runs independent note =====
os.makedirs(os.path.dirname(OB_RUN), exist_ok=True)
run_lines = [f'# Open Day 开放日 · 第三十二轮补采（2026-09-02）独立笔记', '']
run_lines.append(f'- 独立页 GitHub Pages：{GH_RUN}')
run_lines.append(f'- 本地路径：`{INC}`')
run_lines.append(f'- 累计卡片墙：`{GH}`')
run_lines.append('')
run_lines.append(f'本轮新增 **{len(cards)}** 张（②上下级 {n2} · ③高管间 {n3}，5 一手 + 1 二手）：')
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
        # whoami OK -> upload run page as new entry + wall update (best-effort)
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
    round_rec['note'] = '轮次页 R32 (+%d)｜乐享待补传(whoami 探活失败/未连通，待重连后补传并回填 entry_id)' % len(cards)
else:
    round_rec['note'] = '轮次页 R32 (+%d)｜乐享已上传' % len(cards)
mapp['openday']['rounds'].append(round_rec)
json.dump(mapp, open(MAP,'w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('OK lexiang-entry-map updated (entry_id=%s)' % eid)

print('\n==== RUN SUMMARY ====')
print('主题: Open Day 开放日 (r32, 2026-09-02)')
print('覆盖关系档: 仅 上下级(②) / 高管间(③)，已剔除 平级/朋友向(①)')
print('新增 N=%d (②=%d, ③=%d) | 去重删 M=%d' % (len(cards), n2, n3, len(dropped)))
print('增量独立页: %s' % INC)
print('汇总墙: %s' % HTML)
print('GitHub Pages 独立页: %s' % GH_RUN)
print('乐享 entry_id=%s (%s)' % (eid, lmsg))
