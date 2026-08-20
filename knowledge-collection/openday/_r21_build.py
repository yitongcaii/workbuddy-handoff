# -*- coding: utf-8 -*-
# Open Day 二十一轮补采（r21, 2026-08-21）+5 卡，全②上下级
# 新域：航天公众开放日 / 清洁能源(光伏风电)电站公众开放日 / 三峡水利枢纽国企开放日 / 司法行政戒毒所禁毒警示教育开放日 / 通信运营商5G体验开放日
import re, os, json

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, 'openday.html')
TMP  = os.path.join(BASE, '.run_newcards.tmp.html')
CACHE= os.path.join(BASE, '.rows_cache.json')
IDX  = os.path.join(os.path.dirname(BASE), 'index.json')

OB_SUM = 'C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库/素材/openday/OpenDay-开放日-知识卡汇总.md'
OB_IDX = 'C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库/00-知识采集索引.md'
OB_RUN = 'C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库/素材/openday/runs/OpenDay-2026-08-21-第二十一轮-知识卡.md'

html = open(HTML, encoding='utf-8').read()

cards = [
 dict(emoji='🚀', title='文昌航天观礼中心 开放日（航天文旅科普·观礼+小课堂）', cat='航天科普开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://wenchang.hainan.gov.cn/wenchang/jrwc/202509/9cb84e501e294dc8b7a0ca09bd1b72b4.shtml',
      val='文昌航天观礼中心国庆/五一假期对外开放，每日安排专业讲师多场航天小课堂，设航天主题打卡点、互动小游戏、宇航服换装体验及水火箭制作，覆盖观赏/娱乐/实践多维；市民游客登观礼平台远眺文昌航天发射场与海南商业航天发射场全景；2026年天舟九号发射时近2000名游客在瑶光观礼平台「追火箭」，融合火箭观礼+非遗手作+星空派对+航天专家「纸杯返回舱实验」，构建「硬核科技+文化传承+沉浸体验」交流模式；香港共创明「teen」青年学子交流团现场感受大国重器腾飞。',
      how='把「发射场观礼」做成常态化开放的文旅科普产品（假期每日开放+专业讲师小课堂）；用观礼平台+航天科普展区+VR星际体验+9D影院把「看火箭」升级为「懂航天」；设置水火箭DIY/宇航服换装/航天小游戏等低门槛互动，覆盖亲子/学生/航天爱好者全龄段；联动景区票务+文创，把大国重器变成可亲近的国民科普IP。',
      note='② 航天文旅科普公众开放日，地方政府+文旅平台以开放透明姿态，市民/游客/青少年/港澳青年零距离感受航天文化与大国重器，激发科学兴趣与民族自豪。'),
 dict(emoji='📡', title='中国移动 5G 通信公众体验开放日（返乡学子/市民·数字科普）', cat='通信科普开放日',
      rel='r2', src='二手', src_cls='b2',
      url='https://www.sohu.com/a/985344920_122616369',
      val='中国移动河池分公司举办「返乡学子走进5G通信开放日」，专业讲解5G高速率/低时延/广连接特性；现场设体验环节，学子亲手操作感受5G云游戏流畅度、体验VR设备震撼视觉；河北移动/通辽移动在5·17世界电信日把5G体验厅对市民开放，360度VR直播、16路高清点播、5G+AI猜拳机器人、5G无人机VR回传等「可接触可体验」项目揭开5G应用面纱；广西移动曾设13个体验场景含5G远程驾驶/无人车/云VR/远程医疗。',
      how='把「技术参数」翻译成「可触摸体验」——云游戏/VR/远程驾驶/猜拳机器人等低门槛互动项目让市民亲手感受5G；以「返乡学子/市民」为对象做人才回流与数字科普双目标；5·17电信日固定为公众体验开放节点，形成年度品牌。',
      note='② 通信运营商公众体验开放日，央企分公司领导/技术以数字科普姿态，返乡学子/市民/青少年零距离了解5G如何改变生活，破除「5G只是快」的认知偏差。'),
 dict(emoji='☀️', title='华电新能源 光伏/风电电站公众开放日（清洁能源科普·校企共建）', cat='清洁能源科普开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://big5.china.com.cn/gate/big5/slzg.china.com.cn/2026-05/21/content_43432090.htm',
      val='陕西华电新能源公司「度度关爱 点亮未来」520公众开放日暨品牌体验系列活动，联动本部及安康/咸阳/渭南三片区，邀中小学生/园区职工子女/高校学子走进新能源产业一线；汉阴县双乳镇小学师生走进安康片区龙寨沟光伏电站，志愿者通俗讲解发电原理、现场观摩项目运作实景；渭南片区在陕西省首个全光伏屋面产业园区开绿色工厂探秘，面向职工子女设安全用电课堂+电力趣味游戏；咸阳片区云端直播带网友云游土桥风电场、讲风电知识；本部邀西安交大/西安理工60余名师生参观太平镇农光互补示范项目、生产指挥调控中心。',
      how='打造「参观+科普+互动+云传播」一体化体验场景，让绿色科普走出展厅；针对不同群体定制（小学生现场观摩/职工子女安全用电课堂/高校师生产学研）；用「志愿者讲解+实景观摩+云端直播」扩大绿色能源科普影响力；常态化为公众开放+校企共建，传递央企绿色责任。',
      note='② 清洁能源央企公众开放日，华电新能源领导/志愿者以科普透明姿态，中小学生/职工子女/高校学子走进光伏电站/风电场，直观了解清洁能源转换与「双碳」意义。'),
 dict(emoji='🌊', title='三峡工程 国企开放日（大国重器·水利枢纽公众开放）', cat='水利枢纽开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://cpc.people.com.cn/BIG5/n1/2021/0427/c64387-32089054.html',
      val='国务院国资委、水利部、三峡集团在三峡坝区共同举行以「百年奋斗路 世纪三峡情」为主题的国企开放日活动，系三峡工程首次全方位对公众开放；三峡大坝坝顶、三峡电厂、长江珍稀鱼类保育中心首次向公众开放；160余位专家/央企代表/帮扶地区干部群众/库区移民/西藏班师生代表走进三峡大坝、三峡电厂、三峡工程博物馆、长江珍稀鱼类保育中心、三峡珍稀植物研究所，近距离感受建设成就与综合效益；三峡集团表示将进一步完善「国企开放日」机制。',
      how='以「重走总书记考察之路」为叙事主线，把大国重器开放与爱国主义/科普教育结合；首次开放的坝顶/电厂/珍稀鱼类保育中心制造稀缺体验钩子；用博物馆+珍稀物种保护（中华鲟放流504万尾/珍稀植物1256种）把工程成就转化为生态责任故事；形成「国企开放日」常态化机制让更多公众走进。',
      note='② 水利枢纽央企国企开放日，三峡集团领导以开放自信姿态，公众/师生/移民群众/专家代表零距离感受大国重器防洪发电航运生态综合效益，增强国家认同与工程信任。'),
 dict(emoji='🛡️', title='强制隔离戒毒所 禁毒警示教育开放日（青少年法治教育·现身说法+亲情帮教）', cat='司法警示开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.moj.gov.cn/pub/sfbgw/jgsz/jgszjgtj/jgtjjdglj/jdgljtjxw/202606/t20260626_536869.html',
      val='山东省司法行政戒毒系统「6·26」国际禁毒日举办「向党和人民报告」全省司法行政戒毒系统开放日活动，邀「两代表一委员」参加；各戒毒所开展防范药物滥用专题讲座、文体活动；北京/郴州等地在强制隔离戒毒所举办警营开放日，74组家庭+师生+媒体走进戒毒所，参观禁毒警示教育基地（仿真毒品模型/吸毒前后人体器官对比）、戒毒人员生活区、橄榄叶心理工作室，戒毒人员现身说法+亲属亲情接见；郴州所将防毒知识融入原创文学讲座，打破校园禁毒教育「一堂课讲到底」单一路径。',
      how='以「现身说法+亲情帮教+沉浸认知」替代说教——仿真毒品模型/器官对比模型直观警示、戒毒人员真实悔恨讲述最具冲击力、家属亲情接见室搭建帮教平台；针对青少年用「禁毒趣味游戏+集章打卡+文学叙事」把防毒知识入脑入心；司法行政戒毒系统（区别于公安机关）以开放日创新禁毒预防教育模式，常态化面向青少年。',
      note='② 司法行政戒毒系统警示教育开放日（区别于公安警营开放日），戒毒所领导/民警以法治教育姿态，青少年/家庭/社会公众沉浸式接受禁毒警示教育，提升识毒防毒拒毒能力。'),
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

# write temp file for run page
open(TMP, 'w', encoding='utf-8').write(new_blocks + '\n')

# 1) insert before sec3 header
marker = '  <div class="sec sec3">'
idx = html.find(marker)
assert idx != -1, 'sec3 marker not found'
html = html[:idx] + new_blocks + '\n' + html[idx:]

# 2) update sec2 tag count (151 -> 156)
html = re.sub(r'(<div class="sec sec2">.*?<span class="tag">)\d+ 卡(</span>)',
              lambda m: m.group(1) + str(151 + n) + ' 卡' + m.group(2),
              html, count=1, flags=re.S)

# 3) update hero p: append r21 segment
seg = '｜ 二十一轮补采 2026-08-21(+5，航天公众开放日/清洁能源光伏风电电站/三峡水利枢纽国企开放日/司法戒毒所禁毒警示教育/运营商5G体验开放日向·全②上下级，4 一手+1 二手)'
html = html.replace('</div>\n  <div class="sec sec2">',
                    seg + '</div>\n  <div class="sec sec2">', 1)

open(HTML, 'w', encoding='utf-8').write(html)
print(f'OK inserted {n} cards | sec2 now {151+n} | tmp={TMP}')

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
t = t.replace('共 157 张', '共 162 张', 1)
seg_sum = ' + **二十一轮补采 2026-08-21(+5：航天公众开放日/清洁能源光伏风电电站/三峡水利枢纽国企开放日/司法戒毒所禁毒警示教育/运营商5G体验开放日向·全②上下级，4 一手+1 二手）**。'
t = t.replace(' + **二十轮补采 2026-08-20(+7：', seg_sum + ' + **二十轮补采 2026-08-20(+7：', 1)
# append table rows (insert before line 94 blank / heading 卡片墙 at 95)
lines = t.split('\n')
last_tbl = 93
new_rows = []
for c in cards:
    new_rows.append(f"| {c['title']}（openday.html） | 4 | {c['src']} | {c['rel']=='r2' and '②上下级' or '③高管间'} | {c['note'][3:c['note'].find('，')] if '，' in c['note'] else c['note'][3:20]} |")
lines = lines[:94] + new_rows + lines[94:]
t = '\n'.join(lines)
# append 二十一轮 narrative at end
narr = ('\n二十一轮补采（2026-08-21）新增聚焦五大未覆盖子域（全②上下级，4 一手+1 二手）：'
        '「航天公众开放日」（文昌航天观礼中心，观礼平台+航天小课堂+水火箭DIY+宇航服换装+VR星际体验，假期常态化开放、天舟九号近2000人「追火箭」）、'
        '「清洁能源光伏/风电电站公众开放日」（华电新能源520公众开放日，光伏电站实景观摩+风电场云端直播+农光互补示范+校企共建）、'
        '「三峡水利枢纽国企开放日」（大国重器首次全方位公众开放，坝顶/电厂/珍稀鱼类保育中心首开+生态责任叙事）、'
        '「司法行政戒毒所禁毒警示教育开放日」（区别于公安警营，现身说法+亲情帮教+仿真毒品模型警示+青少年文学叙事防毒）、'
        '「通信运营商5G体验开放日」（移动返乡学子/市民5G体验厅，云游戏/VR/远程驾驶/猜拳机器人把技术变可触摸体验）。'
        '硬排除：家庭日/家属开放日、投资者/资本市场/IR/证监局开放日（非 HRBP 企业文化活动向）。\n')
t = t.rstrip('\n') + narr
open(OB_SUM, 'w', encoding='utf-8').write(t)
print('OK obsidian summary updated')

# ---- 00 索引 ----
lines = open(OB_IDX, encoding='utf-8').read().split('\n')
# update heading
lines[214] = lines[214].rstrip('）') + '｜ 2026-08-21 二十一轮补采 +5（航天公众开放日/清洁能源光伏风电电站/三峡水利枢纽国企开放日/司法戒毒所禁毒警示教育/运营商5G体验开放日向））'
# insert 5 table rows at end of openday table (after last openday.html row = 999)
od_rows = []
for c in cards:
    od_rows.append(f"| {c['title']}（openday.html） | 4 | {c['src']} | ②上下级 | 二十一轮新增 |")
ins = 1000
lines = lines[:ins] + od_rows + lines[ins:]
open(OB_IDX, 'w', encoding='utf-8').write('\n'.join(lines))
print('OK 00-index updated')

# ---- runs 独立笔记 ----
gh = 'https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/runs/openday-2026-08-21-r21.html'
local = 'knowledge-collection/openday/runs/openday-2026-08-21-r21.html'
rows_md = '\n'.join(f"| {c['emoji']} {c['title']} | {c['src']} | ②上下级 | {c['url']} |" for c in cards)
note = f'''---
title: Open Day 二十一轮补采知识卡
tags: [知识采集, 开放日, 自动化采集, 轮次]
date: 2026-08-21
type: 自动化采集
---

## Open Day 开放日 · 第 21 轮补采（2026-08-21，+5 卡）

- 线上独立页（GitHub Pages）：{gh}
- 本地路径：{local}
- 累计总索引（卡片墙）：`knowledge-collection/openday/openday.html`

### 本轮新增卡表（全②上下级，4 一手 + 1 二手）

| 卡 | 一手/二手 | 适用关系 | 来源 URL |
|---|---|---|---|
{rows_md}

### 本轮侧重
五大未覆盖子域：航天公众开放日 / 清洁能源光伏风电电站公众开放日 / 三峡水利枢纽国企开放日 / 司法行政戒毒所禁毒警示教育开放日 / 通信运营商 5G 体验开放日。
硬排除：家庭日/家属开放日、投资者/资本市场/IR/证监局开放日（非 HRBP 企业文化活动向）。
'''
os.makedirs(os.path.dirname(OB_RUN), exist_ok=True)
open(OB_RUN, 'w', encoding='utf-8').write(note)
print('OK runs note:', OB_RUN)
