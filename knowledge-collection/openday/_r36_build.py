# -*- coding: utf-8 -*-
# Open Day r36 (2026-09-05) build: 注入 8 张新卡到累计墙 + 生成独立页 + 更新 index.json + Obsidian 三端
import os, re, json, subprocess, sys

BASE = os.path.dirname(os.path.abspath(__file__))          # knowledge-collection/openday
KC   = os.path.dirname(BASE)                               # knowledge-collection
HTML = os.path.join(BASE, 'openday.html')
TMP  = os.path.join(BASE, '.run_newcards.tmp.html')
GEN  = os.path.join(KC, 'gen_run_page.py')
IDX  = os.path.join(KC, 'index.json')
VAULT = r'C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库'
SUM   = os.path.join(VAULT, '素材', 'openday', 'OpenDay-开放日-知识卡汇总.md')
IDX00 = os.path.join(VAULT, '00-知识采集索引.md')
RUNS_DIR = os.path.join(VAULT, '素材', 'openday', 'runs')

DATE='2026-09-05'; ROUND=36

cards = [
 dict(emoji='🏛️', title='寻甸县政务服务中心“政府开放日”·“今天我当办事员”沉浸式走流程+局长坐诊',
      cat='政务开放日', rel='r2', src='primary', url='http://www.kmxd.gov.cn/c/2026-09-01/7175358.shtml',
      val='寻甸县政务服务中心2026.9.16办“政府开放日”，主题“换个视角看政务——今天我当‘办事员’”，邀企业/个体户/群众约20人。五环节：实地参观（大厅布局/综窗/惠企专区/“办不成事”窗口）→政策解读（2026十件惠企实事+一卡通）→沉浸式“走流程”（e办通终端+综窗模拟办公司设立/劳动能力鉴定）→“局长坐诊接诉”一对一解难题（主要领导坐诊，现场答/限期办）→座谈建言。把开放日升级为群众当办事员的实景演练。',
      how='把“政府开放日”做成沉浸式办事演练——用“今天我当办事员”角色互换打破神秘感；“局长坐诊接诉”把领导从台上请到台下一对一解难题；e办通终端+综窗模拟让政策“看得懂用得上”；诉求限期办结闭环。',
      note='② 政务服务开放日（寻甸县政府官网一手），政务服务局领导以“坐诊接诉”姿态，企业/群众代表当“办事员”走流程、现场解难题。',
      summary='主题“今天我当办事员”：e办通终端+综窗模拟走流程+局长坐诊一对一解难题，诉求限期办结闭环'),
 dict(emoji='📋', title='平阴县2026年9月政府开放活动预告·多镇街“透明政务零距离”集中发布',
      cat='政务开放日', rel='r2', src='primary', url='http://www.pingyin.gov.cn/gongkai/site_pingyinxianxzfbgsb/channel_jkf_pingyinxianxzfbgsb_68f731ce9837b20f0a44894f/doc_6a9542943cb420bffbad1748.html',
      val='平阴县政府办公室统一预告2026年9月4场“政府开放日”：榆山街道“政务开放零距离”（便民服务中心+退役军人站，讲医保社保就业创业育儿补贴+自助终端演示）、东阿镇“透明政务·零距离”（镇政府+便民中心，面对面答民生）、孔村镇“解锁政务零距离”（机关干部+村支书+群众代表，讲办事流程+矛盾处置案例）、县行政审批局“解读惠企政策解实际问题”。以“五公开”增进政民互信，统一预告让参与可预期。',
      how='把分散的镇街开放日做成“月度集中预告”机制——县政府办统一发布活动清单（主题/时间/地点/报名/简介），降低群众参与门槛；多镇街同月铺开形成规模效应；“五公开”叙事统一对外。',
      note='② 县级政府开放日（平阴县政府官网一手），各镇街领导以服务者姿态，群众/企业/代表参观便民中心、面对面答民生。',
      summary='县政府办月度集中预告4场镇街开放日，统一清单降低参与门槛，“五公开”增进政民互信'),
 dict(emoji='🔍', title='吴忠市监局红寺堡区分局“政府开放日”·跟随执法人员走真实检查四环节',
      cat='市场监管开放日', rel='r2', src='primary', url='https://www.hongsibu.gov.cn/zzb/tzgg/202608/t20260819_5318033.html',
      val='吴忠市监局红寺堡区分局2026.9.4办“政府开放日”，主题“走进执法一线感受监管温度”，邀消费者/社区居民、食品生产经营/药店/电梯使用方负责人、媒体。按执法人员日常检查真实流程，带群众依次走四点位：①查食品生产企业（资质/环境/投料记录/添加剂）②查超市（流通/临期管理/价格计量）③查药店（证照/执业药师在岗/储存养护/处方药凭方）④互动体验+座谈（讲重点工作+热点回应）。把监管从“幕后”搬到“台前”。',
      how='把“市场监管开放日”做成执法实景课——严格按日常检查真实动线带群众走四环节，让“监管温度”可感；点位覆盖生产-流通-用药全链条；座谈专设回应环节听意见闭环。',
      note='② 市场监管开放日（红寺堡区政府官网一手），市监领导以监管者姿态，消费者/企业/媒体跟随执法人员走真实检查动线、懂食药安全。',
      summary='按日常检查真实动线带群众走食品生产/商超/药店四环节，监管从幕后到台前'),
 dict(emoji='🔬', title='新余市科技局“政府开放日”·走进2026科普讲解大赛',
      cat='科技开放日', rel='r2', src='primary', url='https://kjj.xinyu.gov.cn/kjj/gggs/2026-09/01/content_af33d769b5e54462bf61632d7608420e.shtml',
      val='新余市科技局2026.9.11办“政府开放日”，主题“奋进‘十五五’ 科技谱新篇——走进新余市科普讲解大赛”，邀20名市民+人大/政协/媒体/专家/企业。三阶段：参观办公场所（科技项目管理/高企申报/技术交易补助业务）→现场观摩2026科普讲解大赛（选手自主命题讲解、感受科技工作者风采）→座谈+政务公开讲（讲职能/重点/科技创新政策+问卷）。把部门开放日与科普赛事结合，让公众“看懂科技局在干什么”。',
      how='把“部门开放日”做成科普体验场——用“参观办公+观摩科普大赛+座谈宣讲”三段式让公众理解科技管理职能；以科普讲解大赛作亮点提升参与感；小规模化（20人）保深度互动。',
      note='② 科技局政务开放日（新余市科技局官网一手），科技部门领导以科普推动者姿态，市民/代表参观办公、观摩科普大赛、议科技创新政策。',
      summary='参观办公+观摩科普讲解大赛+座谈宣讲三段式，让公众看懂科技局在干什么'),
 dict(emoji='🚗', title='中汽中心第六届职工家属开放日·家企同心硬核科技亲子参观',
      cat='职工家属开放日', rel='r2', src='primary', url='https://www.catarc.ac.cn/detailDJ/9e678d6be1a4490187470cf7d07df1b9',
      val='中国汽车技术研究中心2026.6.6办第六届职工家属开放日（天津主院区），党委书记/董事长安铁成等高管出席。开场才艺+抽奖暖场；硬核科技参观：职工及家属分批走进碰撞试验室、NVH实验室、风洞中心、信息安全研究中心、新能源科创基地，近距离看实车碰撞、探秘噪声振动测试、了解智能网联安全；“十四五”成果展+儿童独立营（小家属独立打卡展廊/实验室/听工程师科普）；亲子游戏+NPC闯关+特色小吃街，联合医院/消防做儿童义诊与消防科普。工会牵头的最大规模企业文化品牌活动。',
      how='把“职工家属开放日”做成家企同心纽带——高管出席致辞传递“与职工共同成长”承诺；硬核实验室参观让家属看见亲人工作的科技分量；专设儿童独立营+亲子游戏把“小家”与“企业大家”情感联结；工会牵头成规模最大品牌活动。',
      note='② 职工家属开放日（中汽中心官网一手），企业高管以“大家长”姿态，职工携家属沉浸式参观研发硬核实力、共建家企信任。',
      summary='高管出席+硬核实验室参观+儿童独立营+亲子游戏，家企同心最大规模品牌活动'),
 dict(emoji='💹', title='广发证券2026秋季资本论坛暨上市公司闭门交流会·800+上市公司4000机构',
      cat='资本论坛闭门会', rel='r3', src='secondary', url='https://xxsb.gz-cmc.com/pages/2026/09/04/95f04cb48fbd49a5baf50bee1989888c.html',
      val='广发证券2026.9.1-3在上海办“穿越长波”秋季资本论坛暨上市公司闭门交流会，围绕AI/创新药/消费/汽车/出海及大类资产、固收、量化，设1主论坛+10分论坛，邀800余家上市公司、超4000名公募/保险/银行/私募/海外机构投资者。副总经理张威致辞谈长波周期产业变革；清华AI研究院孙茂松讲大模型产业落地；首席经济学家郭磊提“宏观四个相对速度”；策略首席刘晨明作AH秋季展望。闭门交流会是券商与上市公司/机构投资者的高层对话场。',
      how='把“资本论坛”做成产投高层对话枢纽——以“主论坛+多分论坛+闭门交流”三层把上市公司实控人/机构投资负责人聚到同一开放桌；用长波周期/AI落地/资产配置作共识主线；闭门环节保障坦诚深度对话，是券商式高管开放合作范本（信息时报二手报道）。',
      note='③ 资本论坛闭门交流会（信息时报二手报道），广发证券以资本中介姿态，上市公司高管与机构投资者围绕产业趋势/资产配置闭门对话（企企/投企协作向，非IR证券监管向）。',
      summary='主论坛+10分论坛+闭门交流，800+上市公司与4000机构高层对话，长波周期共识'),
 dict(emoji='🖥️', title='2026秋季央国企CIO及数科公司高管峰会（第十九届）·AI落地场景与ROI',
      cat='央国企CIO高管峰会', rel='r3', src='secondary', url='https://www.cet.com.cn/wzsy/cyzx/10538795.shtml',
      val='2026秋季央国企CIO及数科公司高管峰会（第十九届）2026.9.13北京举办，国资委商业科技质量中心指导、企业网D1net与信众智主办，主题“AI落地场景&ROI”。定向邀约100-120位央国企/大型集团信息中心主任、CIO、IT负责人、数科公司高管，覆盖能源电网/石化/建筑/冶金/军工/粮油/金融/物流全主流赛道。四大亮点：政策导向权威聚焦实战、汇聚“国家队”数字化决策核心圈层、双主线（AI场景落地+投资回报ROI）覆盖全技术链条、可量化可复盘实战方案。',
      how='把“CIO高管峰会”做成央国企数字化决策层闭门对话场——以“AI+专项行动”政策为导向、直击ROI失衡/场景难落地/数据合规/算力成本痛点；定向邀约百人级CIO/数科一把手保障对话层级；双主线（场景+回报）输出可复用实战方案，是高管智库式开放合作范本（中国经济新闻网二手）。',
      note='③ 央国企CIO高管峰会（中国经济新闻网二手），主办以行业智力平台姿态，各家央企CIO/数科高管围绕AI规模化落地与ROI围坐共创（高管间同业协作为主，非IR向）。',
      summary='定向邀约百人级央国企CIO/数科一把手，双主线AI场景落地+ROI实战共创'),
 dict(emoji='🤖', title='2026企业智能化转型闭门研讨会·长沙站·CIO/CTO探营五八智谷',
      cat='企业数智化闭门研讨', rel='r3', src='secondary', url='https://www.cdiac.cn/active/detail?id=341',
      val='中国软件行业协会CIO分会主办“AI+场景实战·共创落地新路径”企业智能化转型闭门研讨会·长沙站2026.9.4举办，邀企业CIO/CTO/数智化负责人、行业专家30-50人，特设标杆企业沉浸式参访五八智谷城市AI中心。日程：探营参观→湖南数字经济促进会/协会领导致辞→中联重科首席专家讲AI规模化落地顶层设计→腾讯云+AI全域赋能→澳优乳业AI场景实操→合合信息数据治理→蓝凌智能办公→深度研讨（打通业财产供销售数据链路/单据自动化/弹性数字基建/AI投入产出评估）。聚焦从“试点”到“规模化价值落地”。',
      how='把“数智化闭门研讨”做成CIO/CTO实战共创场——以“探营标杆+案例分享+深度研讨”三段把企业数智一把手聚到同一开放桌；用真实痛点（数据链路/单据自动化/ROI评估）作研讨锚点；协办机构+头部企业双致辞提升层级，是CIO社群式高管开放合作范本（中国软件行业协会二手）。',
      note='③ 企业数智化闭门研讨会（中国软件行业协会二手），协会以CIO智力平台姿态，企业CIO/CTO围绕AI规模化落地路径围坐共创（高管间同业协作为主，非IR向）。',
      summary='探营标杆+案例分享+深度研讨三段，CIO/CTO围绕AI规模化落地路径共创'),
]

REL_BADGE={'r2':('r2','上下级'),'r3':('r3','高管间')}
SRC_BADGE={'primary':('b1','一手'),'secondary':('b2','二手')}

def card_html(c):
    rb,rt = REL_BADGE[c['rel']]; sb,st = SRC_BADGE[c['src']]
    return (
'    <div class="hl">\n'
'      <div class="top"><span class="emoji">%s</span><h3>%s</h3><span class="cat">%s</span>'
'<span class="badge %s">%s</span><span class="badge %s">%s</span></div>\n'
'      <p class="val">%s</p>\n'
'      <details class="exec"><summary>怎么做</summary><div class="inner">%s</div></details>\n'
'      <div class="src">🔗 <a href="%s" target="_blank">%s</a></div>\n'
'      <div class="note">%s</div>\n'
'    </div>\n' % (c['emoji'], c['title'], c['cat'], rb, rt, sb, st, c['val'], c['how'], c['url'], c['url'], c['note'])
    )

cards2 = ''.join(card_html(c) for c in cards if c['rel']=='r2')
cards3 = ''.join(card_html(c) for c in cards if c['rel']=='r3')
all_cards = cards2 + cards3
N = len(cards); N2 = sum(1 for c in cards if c['rel']=='r2'); N3 = N-N2

# ---- 1. 注入累计墙 ----
html = open(HTML, encoding='utf-8').read()
assert html.count('<div class="sec sec2">')==1 and html.count('<div class="sec sec3">')==1

# ② 注入到 sec2 的 grid 内
i = html.index('<div class="sec sec2">')
g = html.index('<div class="grid">', i)
gtag_end = html.index('>', g) + 1
html = html[:gtag_end] + '\n' + cards2 + html[gtag_end:]

# ③ 注入到 sec3 div 之后（sec3 无 grid 包裹，hl 直挂）
i3 = html.index('<div class="sec sec3">')
s3end = html.index('>', i3) + 1
html = html[:s3end] + '\n' + cards3 + html[s3end:]

# tag 计数
html = html.replace('    <span class="tag">252 卡</span>', '    <span class="tag">%d 卡</span>'% (252+N2), 1)
html = html.replace('    <span class="tag">50 卡</span>', '    <span class="tag">%d 卡</span>'% (50+N3), 1)

# hero 轮次：锚定「三十五轮补采」之后最近的 </p>（hero 段落闭合处）
hero_anchor = '三十五轮补采'
ha = html.rfind(hero_anchor)
assert ha != -1, 'hero 三十五轮 anchor not found'
hep = html.index('</p>', ha)
hero_new = ('｜ 三十六轮补采 2026-09-05(+%d：寻甸县/平阴县/红寺堡市监/新余科技·政务开放日%d②全一手'
            ' ｜ 广发证券资本论坛闭门会/央国企CIO高管峰会/企业数智化闭门研讨·%d③0一手+%d二手)') % (N, N2, N3, N3)
html = html[:hep] + hero_new + html[hep:]

open(HTML, 'w', encoding='utf-8').write(html)
print('[wall] injected +%d cards (②+%d / ③+%d); size=%d' % (N, N2, N3, len(html.encode('utf-8'))))

# ---- 2. 临时新卡文件 ----
open(TMP, 'w', encoding='utf-8').write(all_cards)
print('[tmp] wrote %d cards' % N)

# ---- 3. 生成独立页 ----
r = subprocess.run([sys.executable, GEN, '--topic','openday','--topic-name','Open Day 开放日',
                    '--date',DATE,'--round',str(ROUND),'--cards-file',TMP], capture_output=True, text=True)
print('[runpage]', r.stdout.strip(), r.stderr.strip())

# ---- 4. index.json ----
data = json.load(open(IDX, encoding='utf-8'))
have = {e.get('url','').rstrip('/').lower() for e in data}
added=0
for c in cards:
    u=c['url']
    if u.rstrip('/').lower() in have: 
        print('[idx skip dup]', u); continue
    data.append(dict(
        title=c['title'],
        normKey=re.sub(r'\s+','',c['title']),
        url=u,
        sourceType=c['src'],
        relation=('supervisor' if c['rel']=='r2' else 'exec'),
        summary=c['summary'],
    ))
    have.add(u.rstrip('/').lower()); added+=1
json.dump(data, open(IDX,'w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('[index] +%d entries (total %d)' % (added, len(data)))

# ---- 5. Obsidian 汇总笔记 ----
os.makedirs(os.path.dirname(SUM), exist_ok=True)
s = open(SUM, encoding='utf-8').read()
s = s.replace('（共 287 张）','（共 %d 张）'%(287+N),1)
BLOCK = ('\n\n+ **三十六轮补采 2026-09-05(+%d：寻甸县/平阴县/红寺堡市监/新余科技·政务开放日%d②全一手'
         ' ｜ 广发证券资本论坛闭门会/央国企CIO高管峰会/企业数智化闭门研讨·%d③0一手+%d二手)**') % (N,N2,N3,N3)
s = s.replace('\n## 卡片总表', BLOCK+'\n## 卡片总表',1)
# 追加表行
rows=''
for c in cards:
    relt = '②上下级' if c['rel']=='r2' else '③高管间'
    srct = '一手' if c['src']=='primary' else '二手'
    rows += '| %s（openday.html） | 4 | %s | %s | %s |\n' % (c['title'], srct, relt, c['summary'])
s = s.rstrip()+'\n'+rows
open(SUM,'w',encoding='utf-8').write(s)
print('[obs sum] updated, +%d rows'%N)

# ---- 6. 00-索引 追加 8 行 ----
os.makedirs(os.path.dirname(IDX00), exist_ok=True)
r0=''
for c in cards:
    relt = '②上下级' if c['rel']=='r2' else '③高管间'
    srct = '一手' if c['src']=='primary' else '二手'
    r0 += '| %s（openday.html） | 4 | %s | %s | %s |\n' % (c['title'], srct, relt, c['summary'])
with open(IDX00,'a',encoding='utf-8') as f:
    f.write(r0)
print('[obs 00] appended +%d rows'%N)

# ---- 7. runs 独立笔记 ----
os.makedirs(RUNS_DIR, exist_ok=True)
RUNNOTE = os.path.join(RUNS_DIR, 'OpenDay-2026-09-05-第三十六轮-知识卡.md')
GH = 'https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/runs/openday-2026-09-05-r36.html'
LOC = os.path.join(BASE,'runs','openday-2026-09-05-r36.html')
rtbl=''
for c in cards:
    relt = '②上下级' if c['rel']=='r2' else '③高管间'
    srct = '一手' if c['src']=='primary' else '二手'
    rtbl += '| %s | %s | %s | %s |\n' % (c['title'], srct, relt, c['summary'])
run_md = ('---\ntitle: Open Day 第三十六轮知识卡\n'
'tags: [知识采集, 开放日, 自动化采集, 轮次]\ndate: %s\ntype: 自动化采集\n---\n\n'
'# Open Day 开放日 · 第三十六轮补采（%s）\n\n'
'## 本轮回链\n'
'- GitHub Pages 独立页：%s\n'
'- 本地路径：%s\n'
'- 累计总索引墙：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday.html\n\n'
'## 本轮新增 %d 张（②上下级 %d / ③高管间 %d）\n\n'
'| 卡 | 一手/二手 | 适用关系 | 一句话定位 |\n|---|---|---|---|\n%s\n') % (
    DATE, DATE, GH, LOC, N, N2, N3, rtbl)
open(RUNNOTE,'w',encoding='utf-8').write(run_md)
print('[obs runs] wrote', RUNNOTE)

print('DONE r36 N=%d (②%d/③%d)'%(N,N2,N3))
