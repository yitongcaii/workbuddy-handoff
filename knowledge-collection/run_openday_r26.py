# -*- coding: utf-8 -*-
# Open Day 二十六轮补采（r26, 2026-08-25）+6 卡：4 ②上下级 + 2 ③高管间
# 新域：啤酒40周年公众开放日 / 科研院所实验室开放日 / 国企科创开放日 / 政府文博开放日 / 县域政企开放日（高管间·政策闭环）/ 民营政企开放日（高管间·信任拆墙）
import re, os, json, subprocess, sys

WS = r"C:\Users\v_yitcai\WorkBuddy\20260728154244"
KC = os.path.join(WS, "knowledge-collection")
HTML = os.path.join(KC, "openday", "openday.html")
TMP  = os.path.join(KC, "openday", ".run_newcards.tmp.html")
CACHE= os.path.join(KC, "openday", ".rows_cache.json")
IDX  = os.path.join(KC, "index.json")
OB_SUM = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\openday\OpenDay-开放日-知识卡汇总.md"
OB_IDX = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
OB_RUN = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\openday\runs\OpenDay-20260825-第二十六轮-知识卡.md"
GH = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday.html"
GH_RUN = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/runs/openday-20260825-r26.html"
GH_R25 = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday-20260824.html"

cards = [
 dict(emoji='🍺', title='乌苏啤酒 40 周年品牌开放日（董事长率队·酒厂全景透明）', cat='企业公众开放日',
      rel='r2', src='二手', src_cls='b2',
      url='https://dy.163.com/article/L4FIAGU30514R9KE.html',
      val='乌苏啤酒迎来 40 周年，举办品牌开放日，董事长姜涛与消费者、媒体、行业协会代表一同走进乌鲁木齐酒厂，通过品牌展示区、生产车间、品质实验室等环节，呈现 40 年酿造匠心与品质体系；以「40 周年」节点把企业历史、产线透明与品牌温度串联，公众从「喝乌苏」到「懂乌苏」零距离感受智造实力。',
      how='把企业 40 周年庆做成「公众开放日」——用品牌展示区+生产车间+品质实验室三段式动线把酿造全流程透明化；以周年节点制造情感记忆点，让消费者/媒体/行业协会代表从旁观者变品牌共建者；用董事长亲临+行业协会背书提升公信力，把开放日变成品牌信任场景。',
      note='② 企业公众开放日（中国日报网/网易二手），企业领导（董事长姜涛）以品牌共建者姿态，消费者/媒体/行业协会代表走进酒厂，零距离感受 40 年酿造匠心与智造实力。'),
 dict(emoji='🔬', title='江南造船研究院首届「实验室开放日」（5G 智造·11 批次近 500 人）', cat='科研院所开放日',
      rel='r2', src='二手', src_cls='b2',
      url='https://www.sohu.com/a/1032266186_120407443',
      val='江南造船研究院首届「实验室开放日」，依托 5G 智能制造创新实验室，面向员工及受邀代表举办，累计 11 批次近 500 人参与；以「机器人技术与未来」为主题，设科普讲解、互动问答、智创建言奖、文创周边等环节，把前沿科研场景转化为可感可参与的科创启蒙，凝聚员工科创共识。',
      how='把「实验室开放日」做成员工科创共识场——以 5G 智能制造创新实验室为实景课堂，用「科普讲解+互动问答+智创建言奖+文创」组合把前沿技术变可亲可感；以多批次小规模（11 批近 500 人）控质量、广覆盖；把开放日与员工建言、科创文化绑定，沉淀组织创新氛围。',
      note='② 科研院所员工开放日（搜狐二手），研究院领导以科创引路人姿态，员工及受邀代表走进实验室参与机器人科普与智创建言，凝聚科创共识（非家属/非 IR 向）。'),
 dict(emoji='📡', title='中国联通黑龙江省分公司 2026 国企开放日（科创体验中心+巡检机器狗）', cat='国企开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://fdz.fendoui.org.cn/detailArticle/28391019_71601_fdzzs.html',
      val='中国联通黑龙江省分公司 2026 国企开放日，主题「联通未来 创启新程」，邀请政府、媒体、高校、政企客户及合作伙伴等 50 余人走进联通，参观科创体验中心、智慧农业军团、智能计算实验室等，现场演示巡检机器狗等数智成果，以开放姿态展示央企科技创新与产业赋能能力。',
      how='把「国企开放日」做成科技创新展示窗口——以「联通未来 创启新程」主题串联科创体验中心+智慧农业军团+智能计算实验室等场景，用巡检机器狗等可互动成果制造科技惊喜；定向邀请政府/媒体/高校/政企客户/合作伙伴五类代表，把开放日变为政企产学研连接场。',
      note='② 国企开放日（奋斗杂志社一手/准官方），分公司领导以科技赋能者姿态，政府/媒体/高校/政企客户/合作伙伴代表走进联通看数智成果，政企连接+科创叙事。'),
 dict(emoji='🏛️', title='威海市博物馆 2026 政府开放日（流动博物馆进社区+智能机器人+夜间延时）', cat='政府开放日/文博',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.weihai.gov.cn/art/2026/8/7/art_75803_5034.html',
      val='威海市博物馆 2026「政府开放日」以「阳光透明·公开入威」为主题，将「流动博物馆」送进社区，配套智能机器人沉浸式体验、夜间延时开放、政民座谈等环节，把馆藏资源与公共服务下沉到市民身边，以透明开放增进政民互信。',
      how='把「政府开放日」做成文博惠民+政务公开组合——以「阳光透明·公开入威」主题，用「流动博物馆进社区+智能机器人沉浸体验+夜间延时开放」把馆藏资源送到市民身边；以政民座谈收集诉求形成闭环；用夜间延时打破时间门槛，让公共文化服务可感可参与。',
      note='② 政府开放日/文博（威海市政府官网一手），文旅/博物馆部门领导以文化共建者姿态，市民代表走进博物馆、参与流动展览与政民座谈，政务公开+文化惠民。'),
 dict(emoji='🏭', title='于都县科工信局「走进阳光科工信 共话发展新蓝图」政企开放日（政策闭环）', cat='政企开放日',
      rel='r3', src='一手', src_cls='b1',
      url='https://www.yudu.gov.cn/yudu/gzqk/202607/7d52362b847e4ad8bac124e463b6a281.shtml',
      val='于都县科工信局举办「走进阳光科工信 共话发展新蓝图」政府开放日，邀请县域重点工业企业代表走进机关，参观办公运转、宣讲惠企政策、现场答疑解惑，构建「参观—宣讲—答疑」闭环，以开放姿态拉近政企距离、共谋产业发展。',
      how='把「政企开放日」做成政策直达闭环——以「走进机关+惠企政策宣讲+现场答疑」三段式，让企业代表零距离看政府运转、当面听政策、现场提诉求；用「参观—宣讲—答疑」闭环把开放日变政企对话与问题解决通道，忌单向宣讲、纯招商话术。',
      note='③ 政企开放日（于都县政府官网一手），科工信局领导以产业发展服务者姿态，县域重点工业企业代表走进机关共话发展，政企对话+惠企政策闭环（高管间/政企协作向，非 IR/资本向）。'),
 dict(emoji='💡', title='济南市民营经济发展局「活力民营」开放日（全年四场·拆三堵墙）', cat='政企开放日',
      rel='r3', src='二手', src_cls='b2',
      url='https://hb.dzwww.com/p/p2MGjJET4G5.html',
      val='济南市民营经济发展局「活力民营」开放日全年规划四场，聚焦「拆认知、拆沟通、拆信任」三堵墙；每场邀请不同圈层代表（首场人大代表，二场政协委员企业家，三场华熙生物等民企标杆）走进机关，以参观+恳谈+闭环收集交办反馈的机制，把政企沟通做深做实。',
      how='把「政企开放日」做成信任拆墙工程——以全年四场节奏、每场换圈层代表（人大代表→政协委员企业家→民企标杆），用「参观+恳谈+闭环收集交办反馈」把开放日变成可持续的政企信任通道；聚焦拆「认知/沟通/信任」三堵墙，忌一次性走过场、纯政策朗读。',
      note='③ 政企开放日（海报新闻二手），民营经济局领导以民企服务者姿态，人大代表/政协委员企业家/民企标杆代表走进机关共话活力民营，政企信任拆墙+闭环交办（高管间/政企协作向，非 IR/资本向）。'),
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

# ---- dynamic current counts ----
cur2 = html.count('badge r2">上下级<')
cur3 = html.count('badge r3">高管间<')
print(f'current wall: ②={cur2} ③={cur3} (hl divs={html.count(chr(34)+"hl"+chr(34))})')

# ---- inject ② cards at end of sec2 grid (before sec3 marker) ----
marker = '  <div class="sec sec3">'
idx = html.find(marker)
assert idx != -1, 'sec3 marker not found'
new2_blocks = '\n'.join(card_html(c) for c in cards2)
html = html[:idx] + new2_blocks + '\n' + html[idx:]

# ---- inject ③ card at top of sec3 grid ----
j = html.find('<div class="sec sec3">')
k = html.find('<div class="hl">', j)
assert k != -1, 'no hl in sec3'
new3_blocks = '\n'.join(card_html(c) for c in cards3)
html = html[:k] + new3_blocks + '\n' + html[k:]

# ---- update sec2 / sec3 tag counts (dynamic) ----
m2 = re.search(r'(<div class="sec sec2">.*?<span class="tag">)(\d+)( 卡</span>)', html, re.S)
assert m2, 'sec2 tag not found'
html = html[:m2.start()] + m2.group(1) + str(cur2+n2) + m2.group(3) + html[m2.end():]
m3 = re.search(r'(<div class="sec sec3">.*?<span class="tag">)(\d+)( 卡</span>)', html, re.S)
assert m3, 'sec3 tag not found'
html = html[:m3.start()] + m3.group(1) + str(cur3+n3) + m3.group(3) + html[m3.end():]

# ---- hero append r25 (fix missing) + r26 segments (inside hero <p>, before </div>) ----
seg_r25 = '二十五轮补采 2026-08-24(+11：政法/警营/金融/交通枢纽/乡村振兴/税务开放日向·8②3③，10一手+1二手)'
seg_r26 = '二十六轮补采 2026-08-25(+6，啤酒40周年/造船实验室/联通黑龙江科创/威海博物馆/于都政企/济南活力民营·4②2③)'
HERO_ANCHOR = ('二十四轮补采 2026-08-23(+6，国企开放日城市级/企业公众开放日/工厂游方法论/'
               '车企工业旅游/政府开放月水务/高管间闭门可持续转型·5②1③)</div>')
assert HERO_ANCHOR in html, 'hero r24 tail not found'
html = html.replace(HERO_ANCHOR, HERO_ANCHOR + '｜ ' + seg_r25 + seg_r26, 1)

open(HTML, 'w', encoding='utf-8').write(html)
print(f'OK wall updated: ②={cur2+n2} ③={cur3+n3} (hl divs now {html.count(chr(34)+"hl"+chr(34))}), footer={html.count("本页由 yitong 沉淀整理")}')

# ============ .run_newcards.tmp.html (for gen_run_page.py) ============
with open(TMP, 'w', encoding='utf-8') as f:
    for c in cards:
        f.write(card_html(c) + '\n')
print(f'OK {TMP} written ({os.path.getsize(TMP)}B)')

# ============ index.json ============
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

# ============ .rows_cache.json ============
cache = json.load(open(CACHE, encoding='utf-8'))
for c in cards:
    cache.append([c['title'], c['src'], '②上下级' if c['rel']=='r2' else '③高管间', c['val']])
json.dump(cache, open(CACHE, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'OK rows_cache.json {len(cache)-len(cards)} -> {len(cache)}')

# ============ Obsidian: summary note ============
def rel_short(c):
    return '②上下级' if c['rel']=='r2' else '③高管间'
def row_md(c):
    # 一句话定位 = note 截断
    one = c['note']
    if '：' in one: one = one.split('：',1)[1]
    one = one.rstrip('）。').strip()
    return f'| {c["title"]}（openday.html） | 4 | {c["src"]} | {rel_short(c)} | {one} |'

sum_txt = open(OB_SUM, encoding='utf-8').read()
# 1) abstract count 191 -> 197
assert '（共 191 张）' in sum_txt, 'abstract count 191 not found'
sum_txt = sum_txt.replace('（共 191 张）', '（共 197 张）', 1)
# 2) abstract append r26 segment
AB = '2026-08-24(+11：政法/警营/金融/交通枢纽/乡村振兴/税务开放日向·8②+3③，10一手+1二手)**。'
assert AB in sum_txt, 'abstract r25 tail not found'
sum_txt = sum_txt.replace(AB,
    '2026-08-24(+11：政法/警营/金融/交通枢纽/乡村振兴/税务开放日向·8②+3③，10一手+1二手)**'
    ' + **二十六轮补采 2026-08-25(+6：啤酒40周年/造船实验室/联通黑龙江科创/威海博物馆/于都政企/济南活力民营·4②2③，2一手+4二手)**。', 1)
# 3) append 6 table rows before 卡片墙 header
WALL_HDR = '## 卡片墙（HTML 交互版）'
assert WALL_HDR in sum_txt
table_rows = '\n'.join(row_md(c) for c in cards) + '\n'
sum_txt = sum_txt.replace(WALL_HDR, table_rows + WALL_HDR, 1)
# 4) append r25 + r26 independent-page links (after r24 link)
R24_LINK = '当轮独立页（第二十四轮）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday-20260823.html'
assert R24_LINK in sum_txt
sum_txt = sum_txt.replace(R24_LINK,
    R24_LINK + '\n'
    f'- 当轮独立页（第二十五轮）：{GH_R25}\n'
    f'- 当轮独立页（第二十六轮）：{GH_RUN}', 1)
# 5) fix stale line 226 count (157 卡 / 一手76+二手74) -> accurate from updated wall
b1c = html.count('badge b1"')
b2c = html.count('badge b2"')
assert b1c + b2c == cur2+n2 + cur3+n3, (b1c, b2c, cur2+n2, cur3+n3)
assert '**157 卡**' in sum_txt, 'stale 157 卡 not found'
sum_txt = sum_txt.replace('**157 卡**', f'**{b1c + b2c} 卡**', 1)
assert '一手 76 + 二手 74' in sum_txt, 'stale 一手/二手 not found'
sum_txt = sum_txt.replace('一手 76 + 二手 74', f'一手 {b1c} + 二手 {b2c}', 1)
open(OB_SUM, 'w', encoding='utf-8').write(sum_txt)
print(f'OK summary note updated (count {sum_txt.count("共 197 张")} , r26 seg {sum_txt.count("二十六轮补采 2026-08-25")})')

# ============ Obsidian: 00-index ============
idx_txt = open(OB_IDX, encoding='utf-8').read()
# header append r26 segment
HDR_TAIL = ('二十四轮补采 +6（国企开放日城市级/企业公众开放日/工厂游方法论/'
            '车企工业旅游/政府开放月水务/高管间闭门可持续转型·5②1③）')
assert HDR_TAIL in idx_txt, '00-index header r24 tail not found'
idx_txt = idx_txt.replace(HDR_TAIL,
    HDR_TAIL + '｜ 2026-08-25 二十六轮补采 +6（啤酒40周年/造船实验室/联通黑龙江科创/威海博物馆/于都政企/济南活力民营·4②2③）', 1)
# insert 6 rows before summary-note pointer
PTR = '📄 主题汇总笔记：[[知识采集库/素材/openday/OpenDay-开放日-知识卡汇总|OpenDay-开放日-知识卡汇总]]'
assert PTR in idx_txt, '00-index summary pointer not found'
new_rows = '\n'.join(row_md(c).replace('（openday.html）','（openday.html）').replace(' | 4 ',' | 4 ').replace(' | ',' | ').replace('二十六轮新增','二十六轮新增') for c in cards)
# ensure tag "二十六轮新增"
new_rows = '\n'.join(
    f'| {c["title"]}（openday.html） | 4 | {c["src"]} | {rel_short(c)} | 二十六轮新增 |'
    for c in cards) + '\n'
idx_txt = idx_txt.replace(PTR, new_rows + PTR, 1)
open(OB_IDX, 'w', encoding='utf-8').write(idx_txt)
print(f'OK 00-index updated (r26 rows {idx_txt.count("二十六轮新增")})')

# ============ Obsidian: runs note (new) ============
run_md = f'''---
title: Open Day 开放日 第二十六轮知识卡
tags: [知识采集, 开放日, 自动化采集, 轮次]
date: 2026-08-25
type: 自动化采集
---

# Open Day 开放日 · 第二十六轮补采（2026-08-25）

- 本轮新增 **6 卡**（②上下级 4 · ③高管间 2），0 peer（硬约束）
- 一手 2 / 二手 4
- 累计墙：openday.html 191 → 197 卡（② 184 / ③ 25）
- 新域：啤酒 40 周年公众开放日 / 科研院所实验室开放日 / 国企科创开放日 / 政府文博开放日 / 县域政企开放日（高管间·政策闭环）/ 民营政企开放日（高管间·信任拆墙）
- 硬排除：家庭日/家属开放日、投资者关系/证券监管/资本市场/财经媒体类开放日（命中资本市场/IR/证监局即跳过）

## 本轮卡片

| 卡 | 质量分 | 一手/二手 | 适用关系 | 一句话定位 |
|---|---|---|---|---|
'''
for c in cards:
    one = c['note'].split('：',1)[1].rstrip('）。').strip() if '：' in c['note'] else c['note']
    run_md += f'| {c["title"]}（[openday.html]({GH})） | 4 | {c["src"]} | {rel_short(c)} | {one} |\n'
run_md += f'''
## 链接
- 累计卡片墙：{GH}
- 当轮独立页：{GH_RUN}
- 主题汇总笔记：[[知识采集库/素材/openday/OpenDay-开放日-知识卡汇总|OpenDay-开放日-知识卡汇总]]
'''
open(OB_RUN, 'w', encoding='utf-8').write(run_md)
print(f'OK runs note: {OB_RUN} ({os.path.getsize(OB_RUN)}B)')

print('DONE pipeline core.')
