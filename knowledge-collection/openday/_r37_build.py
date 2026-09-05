# -*- coding: utf-8 -*-
# Open Day r37 (2026-09-06) build: 注入 8 张新卡到累计墙 + 生成独立页 + 更新 index.json + Obsidian 三端
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

DATE='2026-09-06'; ROUND=37

cards = [
 dict(emoji='🏥', title='固原市卫健委2026"政府开放日"·"筑牢分级健康防护网"@固原市人民医院院长座谈',
      cat='卫健政务开放日', rel='r2', src='primary',
      url='https://www.nxgy.gov.cn/zwgk/zfxxgkml/rdhy_39590/rdhy_39591/202608/t20260831_5326968.html',
      val='固原市卫健委2026.9.11办"政府开放日"，主题"筑牢分级健康防护网 敞开卫健服务连心门"，邀人大/政协/企业/群众/职工/学生/网民/媒体代表。现场观摩固原市人民医院慢病管理中心建设与运行（门诊大厅→影像中心→健康管理中心→四楼慢病管理中心→信息中心，1小时动线）；座谈由卫健委分管负责同志主持，院长徐万忠围绕医院职能、特色科室、慢病管理中心运行介绍，征求代表对大病慢病精准救治意见建议，及时回应公众关切。',
      how='把"卫健政务开放日"做成慢病治理实景课——以"院长座谈+慢病管理中心全流程走线"让公众看懂分级诊疗与大病救治体系；诉求现场征集+限期回应闭环；卫健领导以服务者姿态，公众以被服务者身份直面对话。',
      note='② 卫健政务开放日（固原市政府官网一手），卫健委领导与院长以服务者姿态，群众/患者代表参观医院、座谈建言大病慢病救治。',
      summary='主题"筑牢分级健康防护网"：院长徐万忠座谈+慢病管理中心全流程走线，公众诉求现场征集回应闭环'),
 dict(emoji='🩺', title='天门一医2026医院开放日·"寻美汇侨·文润天医"文化为媒连社会',
      cat='医院开放日', rel='r2', src='primary',
      url='https://tmsyy.com/cms/show-10314.html',
      val='天门市第一人民医院2026.3.21办"寻美汇侨·文润天医"主题开放日，邀市文联诗词/摄影/书画协会代表。副市长古玉丽、卫健委副主任桓霞、文联副主席熊维、院党委书记严想元、党委副书记院长魏辉及班子出席。党委书记致辞讲"健康科普进万家"；卫健委呼吁文艺工作者当健康理念传播者；文联提创作联动/空间共建/精神共育三合作。以文化为媒推动医学与文艺交融，彰显公立医院人文温度。',
      how='把"医院开放日"做成人文连接器——以"文化协会代表+院领导+卫健主管"三方同台，用文艺叙事包装医学人文，变"开放参观"为"价值共鸣"；党委书记致辞传发展理念，卫健委/文联共建长效机制。',
      note='② 医院自主开放日（天门一医官网一手），院党委书记/院长以"大家长+文化使者"姿态，文艺界/社会公众以共建者身份参与，凸显公立医院人文温度。',
      summary='"寻美汇侨·文润天医"：院领导+卫健+文联三方同台，以文化叙事包装医学人文，建长效共建'),
 dict(emoji='🔬', title='淮南师范学院生物工程学院2026实验室开放暨公共科普日·500小学生沉浸',
      cat='高校实验室开放日', rel='r2', src='primary',
      url='https://swgc.hnnu.edu.cn/2026/0523/c1280a170133/page.htm',
      val='淮南师范学院生物工程学院2026.5.23办"实验室开放暨公共科普日"，主题"探秘细胞微观世界 解锁健康食品密码"，响应全国科技活动周与中国细胞生物学学会实验室开放日安排。学院党政领导班子+资产与实验室管理处/科研处副处长出席，田家庵区第十六小学、谢家集区第二小学等500余名中小学生走进学院。流程：开幕式致辞→科普展板（腐乳/啤酒发酵/细胞结构/微生物）→科普讲座（猕猴桃蜕变之路）→实验室沉浸式参观（腐乳中试线/啤酒中试线/细胞生物学实验室/动植物标本室，显微观察+标本制作+酿造讲解）→实验产品品鉴（米酒/酸奶）。志愿者全程引导。',
      how='把"高校实验室开放日"做成青少年科学启蒙场——以"院长/处长出席+志愿者科普讲解员+沉浸式实验体验+自制产品品鉴"四段，把专业生命科学变"可看可尝可动手"；校领导以教育者姿态，中小学生以探索者身份近距离接触科研。',
      note='② 高校实验室公众开放日（淮南师院官网一手），学院领导以育人者姿态，中小学生/公众以学习者身份走进实验室、做显微观察与标本制作。',
      summary='"探秘细胞微观世界"：500小学生+志愿者讲解员+沉浸式实验体验+自制产品品鉴，科研变可动手'),
 dict(emoji='🛢️', title='中国石油开放日(华北站)·"五秩华北向未来"华北油田五十周年能源全产业链',
      cat='央企公众开放日', rel='r2', src='primary',
      url='https://www.ccin.com.cn/detail/ecb56676fcdf6eca8f99278221ceff41',
      val='中国石油开放日(华北站)2026.9.1在河北任丘举办，华北油田/华北石化/渤海钻探/河北销售四家单位联合，主题"五秩华北向未来，同心奋进创一流"，邀30余家中央及行业主流媒体与社会公众代表。四家单位党委副书记/工会主席王峰、邢冬强、杜成良、梁威相继致辞，展示绿色转型/数智升级/保供惠民成果。参观路线：河北销售沧州第81加油站（综合能源生态圈+石油科普儿童乐园）→华北石化CCUS装置（碳捕集6万吨）→智慧安全培训→留路油田低碳示范区→苏桥储气库等，展示油气全产业链绿色转型与数智赋能。',
      how='把"央企公众开放日"做成能源科普长廊——以"四家单位联合+党委副书记致辞+全产业链实景走线（加油站→炼化CCUS→储气库）"让公众看懂"一滴油"的绿色旅程；领导以"能源铁军"讲述者姿态，媒体/公众以见证者身份沉浸式探访。',
      note='② 央企公众开放日（中化新网一手），四家单位党委副书记以"能源铁军"讲述者姿态，媒体/公众代表走进能源一线、看绿色转型与数智升级。',
      summary='"五秩华北向未来"：四单位联合+党委副书记致辞+全产业链走线（加油站→CCUS→储气库），一滴油绿色旅程'),
 dict(emoji='⚡', title='南方电网广西新电力全州供电2026社会责任日(国企开放日)·"国之大者铭于心"',
      cat='电网国企开放日', rel='r2', src='secondary',
      url='https://www.toutiao.com/article/7681501481845178921/',
      val='南方电网广西新电力集团全州供电公司2026.9.3办"国之大者铭于心 万家灯火践于行"社会责任日(国企开放日)。通过资料发放、成果宣讲、现场答疑、电力科普等形式搭建企民零距离桥梁。发放《广西电网2025社会责任实践报告》《安全用电宣传笔记》《电力设施保护条例》等60余份；宣讲电网建设/供电服务/民生保电成效，重点讲电动车规范充电、热水器节电、用电隐患排查等实用常识；针对电费缴纳/报装/故障报修等咨询逐一解答。展现"人民电业为人民"央企风貌。',
      how='把"电网国企开放日"做成便民科普台——以"资料发放+成果宣讲+现场答疑+安全用电科普"四件套，把央企履责成效讲成群众听得懂的用电常识；工作人员以服务者姿态，群众以被服务者身份面对面解难题。',
      note='② 电网国企开放日（全州融媒/今日头条二手），供电公司领导/员工以服务者姿态，群众现场咨询电费/报装/隐患、学安全用电。',
      summary='"国之大者铭于心"：资料发放+成果宣讲+现场答疑+安全用电科普，央企履责变群众听得懂的常识'),
 dict(emoji='📈', title='国泰海通2026秋季策略会·"变局寻径,金秋谋远"董事长致辞+总量分论坛',
      cat='券商策略会', rel='r3', src='secondary',
      url='https://www.toutiao.com/article/7682028933311398427/',
      val='国泰海通2026秋季策略会2026.9.2-3北京举办，主题"变局寻径，金秋谋远"，汇聚政策专家、学界学者、上市公司高管、各类机构投资者。党委书记、董事长朱健出席并致辞，讲金融报国初心、投研硬实力与科技赋能双引擎；国务院发展研究中心原副主任王一鸣、人大区域国别研究院翟东升、复旦美国研究中心赵明昊、云知声CEO黄伟等作主论坛演讲；总量分论坛展望宏观经济与A股策略。上市公司高管与机构投资者高层对话产业热点与投资策略。',
      how='把"券商策略会"做成产投高层对话枢纽——以"董事长致辞定调+政策学者+上市公司高管+机构投资负责人同台"把市场热点与投资策略聚到同一开放桌；总量/行业分论坛分层输出，是券商式高管开放合作范本（中国证券报二手）。',
      note='③ 券商秋季策略会（中国证券报/今日头条二手），国泰海通以资本中介姿态，上市公司高管与机构投资者围绕市场热点与投资策略高层对话（企企/投企协作向，非IR证券监管向）。',
      summary='"变局寻径,金秋谋远"：董事长朱健致辞+政策学者+上市公司高管+机构投资人同台，总量分论坛对话'),
 dict(emoji='🌉', title='2026福布斯中国硅谷创新论坛·闭门邀请制·中美商业决策者',
      cat='国际闭门论坛', rel='r3', src='secondary',
      url='https://www.toutiao.com/article/7681358030952350249/',
      val='2026福布斯中国硅谷创新论坛2026.9.19在硅谷计算机历史博物馆启幕，福布斯中国登陆硅谷的重要探索，面向中美及跨市场商业决策者、科创先锋与投资力量的闭门邀请制活动。论坛以"东西汇智，创启新境"为内核，围绕AI突破、科技创新迭代、企业转型实践、未来商业演进展开深入交流。区别于公开大型峰会，采用闭门定向邀请，嘉宾可放下公众表达边界，以理解/共情/务实主义展开跨文化对话，推动高层次信任连接与跨境战略协作。',
      how='把"国际创新论坛"做成闭门信任场——以"闭门定向邀请+跨文化对话+高层次信任连接"把中美商业决策者/科创先锋/投资力量聚到同一桌；放下公众表达边界换深度务实对话，是跨境高管开放合作范本（福布斯/今日头条二手）。',
      note='③ 国际闭门创新论坛（福布斯/今日头条二手），福布斯中国以智力平台姿态，中美商业决策者/科创先锋/投资人闭门对话、建跨境战略链接（高管间同业协作向）。',
      summary='"东西汇智,创启新境"：闭门邀请制+跨文化对话+高层次信任连接，中美商业决策者聚同一桌'),
 dict(emoji='⚖️', title='胡润智榜2026中国企业法商年度峰会·"法商共生"三场圆桌',
      cat='企业法商峰会', rel='r3', src='secondary',
      url='https://new.qq.com/rain/a/20260903A0AYN000',
      val='胡润智榜2026.9.20上海举办《2026中国企业法商年度峰会·法商共生：新周期下企业发展的韧性与力量暨胡润智榜·大中华区卓越法律服务指南发布仪式》。汇聚智能制造、汽车、消费、能源、科技等领域企业高管、总法律顾问、法务及合规负责人与法律行业代表，预计200-300人。胡润主持法商对谈圆桌并发布指南；设置三场法商圆桌，企业嘉宾结合一线实践，围绕"业务该继续加码还是收缩/出海新规这笔账怎么算/AI投了一年回报在哪"三大真实痛点分享判断。',
      how='把"企业法商峰会"做成高管-法总对话场——以"胡润主持对谈+三场法商圆桌+年度指南发布"把企业高管与总法/合规负责人聚到同一开放桌；用"加码or收缩/出海算账/AI回报"三大一线痛点作研讨锚点，是高管间跨界（经营×法律）开放协作范本（腾讯新闻二手）。',
      note='③ 企业法商年度峰会（腾讯新闻二手），胡润以榜单平台姿态，企业高管与总法/合规负责人围绕经营×合规真实痛点圆桌对话（高管间跨界协作为主，非IR向）。',
      summary='"法商共生"：胡润主持对谈+三场法商圆桌，企业高管与总法围绕加码/出海/AI回报痛点对话'),
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
html = html.replace('    <span class="tag">257 卡</span>', '    <span class="tag">%d 卡</span>'% (257+N2), 1)
html = html.replace('    <span class="tag">53 卡</span>', '    <span class="tag">%d 卡</span>'% (53+N3), 1)

# hero 轮次：锚定「三十六轮补采」之后最近的 </p>（hero 段落闭合处）
hero_anchor = '三十六轮补采'
ha = html.rfind(hero_anchor)
assert ha != -1, 'hero 三十六轮 anchor not found'
hep = html.index('</p>', ha)
hero_new = ('｜ 三十七轮补采 2026-09-06(+%d：固原市卫健委/天门一医/淮南师院·政务与医院开放日3②全一手'
            ' ｜ 中国石油华北站/南方电网全州供电·国企开放日2②1一手+1二手'
            ' ｜ 国泰海通秋季策略会/福布斯硅谷创新论坛/胡润法商年度峰会·%d③0一手+%d二手)') % (N, N3, N3)
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
s = s.replace('（共 295 张）','（共 %d 张）'%(295+N),1)
BLOCK = ('\n\n+ **三十七轮补采 2026-09-06(+%d：固原市卫健委/天门一医/淮南师院·政务与医院开放日3②全一手'
         ' ｜ 中国石油华北站/南方电网全州供电·国企开放日2②1一手+1二手'
         ' ｜ 国泰海通秋季策略会/福布斯硅谷创新论坛/胡润法商年度峰会·%d③0一手+%d二手)**') % (N, N3, N3)
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
RUNNOTE = os.path.join(RUNS_DIR, 'OpenDay-2026-09-06-第三十七轮-知识卡.md')
GH = 'https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/runs/openday-2026-09-06-r37.html'
LOC = os.path.join(BASE,'runs','openday-2026-09-06-r37.html')
rtbl=''
for c in cards:
    relt = '②上下级' if c['rel']=='r2' else '③高管间'
    srct = '一手' if c['src']=='primary' else '二手'
    rtbl += '| %s | %s | %s | %s |\n' % (c['title'], srct, relt, c['summary'])
run_md = ('---\ntitle: Open Day 第三十七轮知识卡\n'
'tags: [知识采集, 开放日, 自动化采集, 轮次]\ndate: %s\ntype: 自动化采集\n---\n\n'
'# Open Day 开放日 · 第三十七轮补采（%s）\n\n'
'## 本轮回链\n'
'- GitHub Pages 独立页：%s\n'
'- 本地路径：%s\n'
'- 累计总索引墙：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday.html\n\n'
'## 本轮新增 %d 张（②上下级 %d / ③高管间 %d）\n\n'
'| 卡 | 一手/二手 | 适用关系 | 一句话定位 |\n|---|---|---|---|\n%s\n') % (
    DATE, DATE, GH, LOC, N, N2, N3, rtbl)
open(RUNNOTE,'w',encoding='utf-8').write(run_md)
print('[obs runs] wrote', RUNNOTE)

print('DONE r37 N=%d (②%d/③%d)'%(N,N2,N3))
