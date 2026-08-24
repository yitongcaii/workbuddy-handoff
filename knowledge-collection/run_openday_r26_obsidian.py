# -*- coding: utf-8 -*-
# Open Day r26 — Obsidian + gen_run_page + github sync (wall/index/cache already done by run_openday_r26.py)
import os, json, subprocess

WS = r"C:\Users\v_yitcai\WorkBuddy\20260728154244"
KC = os.path.join(WS, "knowledge-collection")
HTML = os.path.join(KC, "openday", "openday.html")
TMP  = os.path.join(KC, "openday", ".run_newcards.tmp.html")
OB_SUM = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\openday\OpenDay-开放日-知识卡汇总.md"
OB_IDX = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
OB_RUN = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\openday\runs\OpenDay-20260825-第二十六轮-知识卡.md"
GH = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday.html"
GH_RUN = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/runs/openday-20260825-r26.html"
GH_R25 = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday-20260824.html"

# compact card view (title/src/rel/note + url) — matches the 6 cards injected into the wall
cards = [
 dict(emoji='🍺', title='乌苏啤酒 40 周年品牌开放日（董事长率队·酒厂全景透明）', rel='r2', src='二手',
      url='https://dy.163.com/article/L4FIAGU30514R9KE.html',
      note='② 企业公众开放日（中国日报网/网易二手），企业领导（董事长姜涛）以品牌共建者姿态，消费者/媒体/行业协会代表走进酒厂，零距离感受 40 年酿造匠心与智造实力。'),
 dict(emoji='🔬', title='江南造船研究院首届「实验室开放日」（5G 智造·11 批次近 500 人）', rel='r2', src='二手',
      url='https://www.sohu.com/a/1032266186_120407443',
      note='② 科研院所员工开放日（搜狐二手），研究院领导以科创引路人姿态，员工及受邀代表走进实验室参与机器人科普与智创建言，凝聚科创共识（非家属/非 IR 向）。'),
 dict(emoji='📡', title='中国联通黑龙江省分公司 2026 国企开放日（科创体验中心+巡检机器狗）', rel='r2', src='一手',
      url='https://fdz.fendoui.org.cn/detailArticle/28391019_71601_fdzzs.html',
      note='② 国企开放日（奋斗杂志社一手/准官方），分公司领导以科技赋能者姿态，政府/媒体/高校/政企客户/合作伙伴代表走进联通看数智成果，政企连接+科创叙事。'),
 dict(emoji='🏛️', title='威海市博物馆 2026 政府开放日（流动博物馆进社区+智能机器人+夜间延时）', rel='r2', src='一手',
      url='https://www.weihai.gov.cn/art/2026/8/7/art_75803_5034.html',
      note='② 政府开放日/文博（威海市政府官网一手），文旅/博物馆部门领导以文化共建者姿态，市民代表走进博物馆、参与流动展览与政民座谈，政务公开+文化惠民。'),
 dict(emoji='🏭', title='于都县科工信局「走进阳光科工信 共话发展新蓝图」政企开放日（政策闭环）', rel='r3', src='一手',
      url='https://www.yudu.gov.cn/yudu/gzqk/202607/7d52362b847e4ad8bac124e463b6a281.shtml',
      note='③ 政企开放日（于都县政府官网一手），科工信局领导以产业发展服务者姿态，县域重点工业企业代表走进机关共话发展，政企对话+惠企政策闭环（高管间/政企协作向，非 IR/资本向）。'),
 dict(emoji='💡', title='济南市民营经济发展局「活力民营」开放日（全年四场·拆三堵墙）', rel='r3', src='二手',
      url='https://hb.dzwww.com/p/p2MGjJET4G5.html',
      note='③ 政企开放日（海报新闻二手），民营经济局领导以民企服务者姿态，人大代表/政协委员企业家/民企标杆代表走进机关共话活力民营，政企信任拆墙+闭环交办（高管间/政企协作向，非 IR/资本向）。'),
]

def rel_short(c):
    return '②上下级' if c['rel']=='r2' else '③高管间'
def one_line(c):
    one = c['note'].split('：',1)[1].rstrip('）。').strip() if '：' in c['note'] else c['note']
    return one
def row_md(c):
    return f'| {c["title"]}（openday.html） | 4 | {c["src"]} | {rel_short(c)} | {one_line(c)} |'

# ---- source-badge counts from UPDATED wall (each card has exactly one b1/b2) ----
html = open(HTML, encoding='utf-8').read()
b1c = html.count('badge b1"')
b2c = html.count('badge b2"')
total = html.count('class="hl"')
assert b1c + b2c == total, (b1c, b2c, total)
print(f'wall total={total} (b1={b1c} 一手 / b2={b2c} 二手); r2+r3 counts={html.count(chr(34)+"hl"+chr(34))}')

# ============ Obsidian: summary note ============
sum_txt = open(OB_SUM, encoding='utf-8').read()
assert '（共 191 张）' in sum_txt
sum_txt = sum_txt.replace('（共 191 张）', '（共 197 张）', 1)
AB = '2026-08-24(+11：政法/警营/金融/交通枢纽/乡村振兴/税务开放日向·8②+3③，10一手+1二手)**。'
assert AB in sum_txt
sum_txt = sum_txt.replace(AB,
    '2026-08-24(+11：政法/警营/金融/交通枢纽/乡村振兴/税务开放日向·8②+3③，10一手+1二手)**'
    ' + **二十六轮补采 2026-08-25(+6：啤酒40周年/造船实验室/联通黑龙江科创/威海博物馆/于都政企/济南活力民营·4②2③，2一手+4二手)**。', 1)
WALL_HDR = '## 卡片墙（HTML 交互版）'
assert WALL_HDR in sum_txt
sum_txt = sum_txt.replace(WALL_HDR, '\n'.join(row_md(c) for c in cards) + '\n' + WALL_HDR, 1)
R24_LINK = '当轮独立页（第二十四轮）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday-20260823.html'
assert R24_LINK in sum_txt
sum_txt = sum_txt.replace(R24_LINK,
    R24_LINK + '\n'
    f'- 当轮独立页（第二十五轮）：{GH_R25}\n'
    f'- 当轮独立页（第二十六轮）：{GH_RUN}', 1)
assert '**157 卡**' in sum_txt
sum_txt = sum_txt.replace('**157 卡**', f'**{total} 卡**', 1)
assert '一手 76 + 二手 74' in sum_txt
sum_txt = sum_txt.replace('一手 76 + 二手 74', f'一手 {b1c} + 二手 {b2c}', 1)
open(OB_SUM, 'w', encoding='utf-8').write(sum_txt)
print(f'OK summary note (count 197={sum_txt.count("共 197 张")}, r26 seg={sum_txt.count("二十六轮补采 2026-08-25")}, stale fixed={sum_txt.count("157 卡")==0})')

# ============ Obsidian: 00-index ============
idx_txt = open(OB_IDX, encoding='utf-8').read()
HDR_TAIL = ('二十四轮补采 +6（国企开放日城市级/企业公众开放日/工厂游方法论/'
            '车企工业旅游/政府开放月水务/高管间闭门可持续转型·5②1③）')
assert HDR_TAIL in idx_txt
idx_txt = idx_txt.replace(HDR_TAIL,
    HDR_TAIL + '｜ 2026-08-25 二十六轮补采 +6（啤酒40周年/造船实验室/联通黑龙江科创/威海博物馆/于都政企/济南活力民营·4②2③）', 1)
PTR = '📄 主题汇总笔记：[[知识采集库/素材/openday/OpenDay-开放日-知识卡汇总|OpenDay-开放日-知识卡汇总]]'
assert PTR in idx_txt
new_rows = '\n'.join(
    f'| {c["title"]}（openday.html） | 4 | {c["src"]} | {rel_short(c)} | 二十六轮新增 |'
    for c in cards) + '\n'
idx_txt = idx_txt.replace(PTR, new_rows + PTR, 1)
open(OB_IDX, 'w', encoding='utf-8').write(idx_txt)
print(f'OK 00-index (r26 header={idx_txt.count("二十六轮补采 +6")}, r26 rows={idx_txt.count("二十六轮新增")})')

# ============ Obsidian: runs note ============
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
    run_md += f'| {c["title"]}（[openday.html]({GH})） | 4 | {c["src"]} | {rel_short(c)} | {one_line(c)} |\n'
run_md += f'''
## 链接
- 累计卡片墙：{GH}
- 当轮独立页：{GH_RUN}
- 主题汇总笔记：[[知识采集库/素材/openday/OpenDay-开放日-知识卡汇总|OpenDay-开放日-知识卡汇总]]
'''
open(OB_RUN, 'w', encoding='utf-8').write(run_md)
print(f'OK runs note: {OB_RUN} ({os.path.getsize(OB_RUN)}B)')

# ============ gen_run_page.py -> runs/openday-20260825-r26.html ============
r = subprocess.run(
    ["C:/Users/v_yitcai/.workbuddy/binaries/python/versions/3.13.12/python.exe",
     os.path.join(KC, "gen_run_page.py"),
     "--topic", "openday", "--topic-name", "Open Day 开放日",
     "--date", "2026-08-25", "--round", "26",
     "--cards-file", TMP,
     "--out", os.path.join(KC, "openday", "runs", "openday-20260825-r26.html")],
    capture_output=True, text=True)
print("gen_run_page:", r.returncode, r.stdout.strip(), r.stderr.strip()[:300])

# ============ sync_knowledge_github.py ============
s = subprocess.run(
    ["C:/Users/v_yitcai/.workbuddy/binaries/python/versions/3.13.12/python.exe",
     os.path.join(KC, "sync_knowledge_github.py")],
    capture_output=True, text=True)
print("sync_github:", s.returncode, s.stdout.strip()[-400:], s.stderr.strip()[:300])
print('DONE r26 obsidian+sync.')
