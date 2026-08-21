# -*- coding: utf-8 -*-
# Open Day 二十二轮补采（r22, 2026-08-22）+5 卡，全②上下级，全一手
# 新域：档案馆/方志馆开放日 / 美术馆·艺术馆开放日 / 疾控中心实验室开放日 /
#       政务服务中心·市民中心开放日 / 融媒体中心·广电总台开放日
import re, os, json

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, 'openday.html')
TMP  = os.path.join(BASE, '.run_newcards.tmp.html')
CACHE= os.path.join(BASE, '.rows_cache.json')
IDX  = os.path.join(os.path.dirname(BASE), 'index.json')

OB_SUM = 'C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库/素材/openday/OpenDay-开放日-知识卡汇总.md'
OB_IDX = 'C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库/00-知识采集索引.md'
OB_RUN = 'C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库/素材/openday/runs/OpenDay-2026-08-22-第二十二轮-知识卡.md'

html = open(HTML, encoding='utf-8').read()

cards = [
 dict(emoji='🗂️', title='高淳区档案馆（党史办·地方志办）2026 国际档案日「档案馆开放日」', cat='档案馆/方志馆开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.njgc.gov.cn/jrgc/gsgg/202606/t20260603_5851143.html',
      val='高淳区档案馆(党史办、地方志办)借第19个国际档案日(2026.6.8-12)办「档案馆开放日」：参观档案史料展示中心解读馆藏珍贵档案+高淳地情人文+红色革命文化；现场体验长三角异地跨馆查档等便民服务，为市民提供结婚纪念结婚证存根彩色复印件塑封服务；赠阅革命故事连环画/地情资料/家庭档案相册；馆内文化空间展播地方党史视频；邀业务协作单位青年读城座谈交流。个人凭身份证/学生证登记、团体提前预约即可走进档案馆。',
      how='把「库房重地」变成「可进可感的文化客厅」——以国际档案日为固定节点，用史料展+异地查档体验+结婚证塑封等便民彩蛋+赠书+读城座谈组合；用「个人登记即进、团体预约导览」降低门槛；把方志/党史从书架搬到市民眼前，厚植在地归属感。',
      note='② 档案/方志系统公众开放日（政府官网一手），档案馆以文化服务者姿态，市民/学生/团体零距离接触馆藏档案与地情文化，增强城市认同。'),
 dict(emoji='🎨', title='成都市美术馆 2026 国际博物馆日系列活动（跨界走秀+文学对谈+科技讲座+夜游延时）', cat='美术馆/艺术馆开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://cdwglj.chengdu.gov.cn/cdwglj/c133208/2026-05/15/content_518b5498e3394397913158b5f2ddfa1b.shtml',
      val='成都市美术馆呼应2026国际博物馆日「博物馆：联结世界的桥梁」，5.15-18开启跨界系列活动并在5.18(周一)不闭馆延时至夜间七点；两大重磅展——全球251位艺术家「烟火指数·成都双年展」与数字技术活化唐代壁画的「壁绘千年」；联动四川电影电视学院打造「跨界走秀」把T台延伸进展厅；茅盾文学奖得主金宇澄与双年展总策展人吴洪亮围绕「烟火回响」对谈图文互译；四川大学苟马玲教授以「3D仿生结构之美」讲自然与数字技术共生；每日四场公益导览+「丝路蜀锦」手作体验。',
      how='把美术馆开放日做成「展览+跨界+对谈+手作+夜游」复合体——用国际博物馆日节点不闭馆延时聚人气；用时尚走秀/文学对谈/科技讲座把静态展变成多维对话场；公益导览+非遗手作降低参与门槛，让艺术从「看」变成「聊、做、夜游」。',
      note='② 公共美术馆开放日（市文旅局官网一手），美术馆以公共文化供给者姿态，市民/游客/艺术爱好者沉浸式参与，艺术惠民+城市文化名片。'),
 dict(emoji='🧫', title='新余市卫健委 2026「政府开放日」（探秘疾控·急救·采供血全流程）', cat='疾控中心实验室开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://wjw.xinyu.gov.cn/wjw/gggs/2026-06/08/content_2f3f45cd6c734ec1a718b025bd90fed7.shtml',
      val='新余市卫健委2026.6.17「政府开放日」主题「政务公开零距离，探秘疾控、急救、采供血全流程」，邀10名市民代表(含人大代表/政协委员/媒体)：第一阶段市疾控中心——实地参观了解职能、观摩布病检测静脉采血/标本处理/无菌操作/血清分离/标本封存的标化全流程、开展布病防控政务公开宣讲纠正认知误区；第二阶段市紧急救援中心——参观负压救护车+120调度；第三阶段市中心血站——观摩血液加工离心分离、实验室传染病/血型血清学检测；第四阶段座谈答疑征集建议。',
      how='把「疾控实验室」从封闭后台变成透明科普前台——以政府开放日为载体，用「实地参观+标准化操作观摩+专题宣讲+座谈」四段式，把传染病检测、急救调度、血液安全等专业流程讲给市民听；限额邀约+代表结构多元(群众/代表/媒体)保证沟通质量，闭环答疑收集民意。',
      note='② 卫健/疾控系统公众开放日（政府卫健委官网一手），疾控以公共卫生服务者姿态，市民零距离了解疾病防控与血液安全全流程，破除专业黑箱、增进信任。'),
 dict(emoji='🏛️', title='鹰潭市行政审批局 2026「政务开放日」（鹰办尽办·政务服务体验日）', cat='政务服务中心/市民中心开放日',
      rel='r2', src='一手', src_cls='b1',
      url='http://www.yingtan.gov.cn/art/2026/8/18/art_12979_1607810.html',
      val='鹰潭市行政审批局2026.8.25「政府开放日」主题「鹰办尽办」政务服务体验日，在市政务服务中心邀不超20名市民代表(含人大代表/政协委员/企业代表/媒体)：参观通用综合窗口、帮办代办服务区等，了解「一窗综办」服务模式及政务服务智能化信息化便利化建设；现场演示制证中心工作流程，近距离了解「一键出证」机制，感受从受理、审批到制证全过程。报名表邮箱提交、截止8.21。',
      how='把「政务大厅」从办事场所变成「可体验的透明窗口」——以政务开放日为节点，用「参观一窗综办+帮办代办区+现场演示一键出证」让市民亲见审批到制证全流程；限额邀约+多元代表+座谈答疑形成「体验-反馈」闭环；可复制为各地行政审批局常态开放范式。',
      note='② 政务服务/行政审批系统开放日（政府官网一手），行政审批局以阳光政务姿态，企业/群众代表零距离体验「一窗综办+一键出证」，优化营商环境感知。'),
 dict(emoji='📺', title='中央广播电视总台 TVCC 向公众开放 + 2026CMG 暑期视听嘉年华开放日', cat='融媒体中心/广电开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://1118.cctv.com/2026/06/09/ARTIJHGwmLzm4ob21sQw5jMU260609.shtml',
      val='中央广播电视总台：① 电视文化中心(TVCC，央视大楼配套)集文创展示/艺术展览/专业剧场/艺术影院于一体，2026.4.29启用后正式向公众开放，市民可参观艺术大师作品展、文创商店、咖啡厅；② 2026CMG暑期视听嘉年华(6.10)首次把150余家品牌企业的300余位合作伙伴邀请进总台光华路园区，八条线路探访台史馆/E01演播室(2000㎡)/央视频办公区/TVCC，节目制作人与主持人现场交流，主活动11大节目中心集中发布百余部精品力作。',
      how='把「媒体总部」从荧幕后走到公众/伙伴眼前——TVCC以「文创+展览+剧场+影院」复合文化空间常态化向公众开放；CMG嘉年华用「园区探营+演播室彩排观摩+主持人面对面+内容发布」把媒体融合转型具象化，以「越开放越共赢」链接伙伴；可借鉴为地方融媒体中心「开放日+内容市集」范式。',
      note='② 融媒体/广电机构开放日（央视官网一手），总台以开放共生姿态，公众/合作伙伴零距离感受媒体融合与文化服务，城市级媒体IP走近大众。'),
]

def card_html(c):
    url_disp = c['url'].replace('https://','').replace('http://','')
    return f'''    <div class="hl">
      <div class="top"><span class="emoji">{c['emoji']}</span><h3>{c['title']}</h3><span class="cat">{c['cat']}</span><span class="badge {c['rel']}">上下级</span><span class="badge {c['src_cls']}">{c['src']}</span></div>
      <p class="val">{c['val']}</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">{c['how']}</div></details>
      <div class="src">🔗 <a href="{c['url']}" target="_blank">{url_disp}</a></div>
      <div class="note">适用：{c['note']}</div>
    </div>'''

new_blocks = '\n'.join(card_html(c) for c in cards)
n = len(cards)
assert n == 5, n

# write temp file for run page
open(TMP, 'w', encoding='utf-8').write(new_blocks + '\n')

# 1) insert before sec3 header
marker = '  <div class="sec sec3">'
idx = html.find(marker)
assert idx != -1, 'sec3 marker not found'
html = html[:idx] + new_blocks + '\n' + html[idx:]

# 2) update sec2 tag count dynamically
m = re.search(r'(<div class="sec sec2">.*?<span class="tag">)(\d+)( 卡</span>)', html, re.S)
assert m, 'sec2 count not found'
old = int(m.group(2))
new = old + n
assert new == 161, (old, new)
html = html[:m.start()] + m.group(1) + str(new) + m.group(3) + html[m.end():]

# 3) update hero p: append r22 segment
seg = '｜ 二十二轮补采 2026-08-22(+5，档案馆/方志馆/美术馆艺术馆/疾控中心实验室/政务服务中心市民中心/融媒体中心广电总台开放日向·全②上下级，全一手)'
assert '</div>\n  <div class="sec sec2">' in html
html = html.replace('</div>\n  <div class="sec sec2">', seg + '</div>\n  <div class="sec sec2">', 1)

open(HTML, 'w', encoding='utf-8').write(html)
print(f'OK inserted {n} cards | sec2 now {new} | tmp={TMP}')

# ---- index.json 追加 5 条 openday 条目 ----
idx_data = json.load(open(IDX, encoding='utf-8'))
assert isinstance(idx_data, list)
before = len(idx_data)
for c in cards:
    idx_data.append({
        'title': c['title'],
        'normKey': c['title'],
        'url': c['url'],
        'sourceType': 'primary' if c['src'] == '一手' else 'secondary',
        'relation': 'supervisor',
        'summary': c['val'][:120],
        'topic': 'openday',
    })
json.dump(idx_data, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'OK index.json {before} -> {len(idx_data)} (+{len(cards)})')

# ---- .rows_cache.json 追加 5 行 ----
cache = json.load(open(CACHE, encoding='utf-8'))
for c in cards:
    cache.append([c['title'], c['src'], '②上下级', c['val']])
json.dump(cache, open(CACHE, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'OK rows_cache.json {len(cache)-n} -> {len(cache)}')

# ---- Obsidian 汇总笔记 ----
t = open(OB_SUM, encoding='utf-8').read()
t = t.replace('共 162 张', '共 167 张', 1)

# 5 张表行插入到「卡片墙」小节之前
new_rows = []
for c in cards:
    one = c['note'][3:c['note'].find('，')] if '，' in c['note'] else c['note'][3:20]
    new_rows.append(f"| {c['title']}（openday.html） | 4 | {c['src']} | ②上下级 | {one} |")
rows_md = '\n'.join(new_rows)
assert '\n\n## 卡片墙（HTML 交互版）' in t
t = t.replace('\n\n## 卡片墙（HTML 交互版）', '\n' + rows_md + '\n\n## 卡片墙（HTML 交互版）', 1)

# r22 独立页链接（接在第十九轮之后）
t = t.replace(
    '- 当轮独立页（第十九轮）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/runs/openday-2026-08-19-r19.html',
    '- 当轮独立页（第十九轮）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/runs/openday-2026-08-19-r19.html\n- 当轮独立页（第二十二轮）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/runs/openday-2026-08-22-r22.html',
    1)

# r22 叙事追加到结尾
narr = ('\n二十二轮补采（2026-08-22）新增聚焦五大未覆盖子域（全②上下级，全一手政府/官方源）：'
        '「档案馆/方志馆开放日」（高淳区档案馆国际档案日，史料展+长三角异地跨馆查档体验+结婚证塑封便民彩蛋+读城座谈）、'
        '「美术馆/艺术馆开放日」（成都市美术馆国际博物馆日，跨界走秀+文学对谈+科技讲座+丝路蜀锦手作+夜游延时）、'
        '「疾控中心实验室开放日」（新余市卫健委政府开放日，探秘疾控标本标化全流程+布病防控宣讲+急救调度+血液安全检测，四段式透明科普）、'
        '「政务服务中心/市民中心开放日」（鹰潭市行政审批局「鹰办尽办」体验日，一窗综办+一键出证全流程现场演示）、'
        '「融媒体中心/广电开放日」（中央广播电视总台TVCC向公众开放+2026CMG暑期视听嘉年华园区探营，媒体融合转型具象化）。'
        '硬排除：家庭日/家属开放日、投资者/资本市场/IR/证监局开放日（非 HRBP 企业文化活动向）。\n')
t = t.rstrip('\n') + narr
open(OB_SUM, 'w', encoding='utf-8').write(t)
print('OK obsidian summary updated')

# ---- 00 索引 ----
lines = open(OB_IDX, encoding='utf-8').read().split('\n')
# 更新 heading（接在二十一轮之后）
head_repl = ('运营商5G体验开放日向）｜ 2026-08-22 二十二轮补采 +5'
             '（档案馆方志馆/美术馆艺术馆/疾控中心实验室/政务服务中心市民中心/融媒体中心广电总台开放日向·全②上下级，全一手））')
for i, ln in enumerate(lines):
    if ln.startswith('## 主题：Open Day 开放日') and ln.rstrip().endswith('）'):
        lines[i] = ln.rstrip('）') + '｜ 2026-08-22 二十二轮补采 +5（档案馆方志馆/美术馆艺术馆/疾控中心实验室/政务服务中心市民中心/融媒体中心广电总台开放日向·全②上下级，全一手）'
        break
# 插入 5 张表行（接在最后一个「二十一轮新增」之后）
od_rows = []
for c in cards:
    od_rows.append(f"| {c['title']}（openday.html） | 4 | {c['src']} | ②上下级 | 二十二轮新增 |")
last = max(i for i, ln in enumerate(lines) if '二十一轮新增' in ln)
lines = lines[:last+1] + od_rows + lines[last+1:]
open(OB_IDX, 'w', encoding='utf-8').write('\n'.join(lines))
print('OK 00-index updated')

# ---- runs 独立笔记 ----
gh = 'https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/runs/openday-2026-08-22-r22.html'
local = 'knowledge-collection/openday/runs/openday-2026-08-22-r22.html'
rows_md2 = '\n'.join(f"| {c['emoji']} {c['title']} | {c['src']} | ②上下级 | {c['url']} |" for c in cards)
note = f'''---
title: Open Day 二十二轮补采知识卡
tags: [知识采集, 开放日, 自动化采集, 轮次]
date: 2026-08-22
type: 自动化采集
---

## Open Day 开放日 · 第 22 轮补采（2026-08-22，+5 卡）

- 线上独立页（GitHub Pages）：{gh}
- 本地路径：{local}
- 累计总索引（卡片墙）：`knowledge-collection/openday/openday.html`

### 本轮新增卡表（全②上下级，全一手政府/官方源）

| 卡 | 一手/二手 | 适用关系 | 来源 URL |
|---|---|---|---|
{rows_md2}

### 本轮侧重
五大未覆盖子域：档案馆/方志馆开放日 / 美术馆·艺术馆开放日 / 疾控中心实验室开放日 / 政务服务中心·市民中心开放日 / 融媒体中心·广电总台开放日。
硬排除：家庭日/家属开放日、投资者/资本市场/IR/证监局开放日（非 HRBP 企业文化活动向）。
'''
os.makedirs(os.path.dirname(OB_RUN), exist_ok=True)
open(OB_RUN, 'w', encoding='utf-8').write(note)
print('OK runs note:', OB_RUN)
