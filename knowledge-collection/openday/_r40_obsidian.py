# -*- coding: utf-8 -*-
"""r40 Obsidian 落库：汇总笔记(改覆盖) + runs独立笔记 + 00-索引追加。仅写到 vault 子目录。"""
import os, re, json

VAULT = r"C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库"
WALL  = r"C:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection/openday/openday.html"
SUMM  = os.path.join(VAULT, "素材", "openday", "OpenDay-开放日-知识卡汇总.md")
IDX0  = os.path.join(VAULT, "00-知识采集索引.md")
RUNS_NOTE = os.path.join(VAULT, "素材", "openday", "runs", "OpenDay-2026-09-08-第四十轮-知识卡.md")

RUN_PAGE = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/runs/openday-2026-09-08-r40.html"
WALL_PAGE = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday.html"
LOCAL = r"C:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection\openday\runs\openday-2026-09-08-r40.html"

# ---- parse wall cards ----
html = open(WALL, encoding='utf-8').read()
def split_cards(h):
    out=[]
    for m in re.finditer(r'<div class="hl">', h):
        s=m.start(); i=m.end(); d=1; j=i
        while j<len(h):
            if h[j:j+4]=='<div': d+=1; j+=4
            elif h[j:j+6]=='</div>': d-=1; j+=6
            else: j+=1
            if d==0: break
        out.append(h[s:j])
    return out
cards=split_cards(html)

def parse(c):
    t=re.search(r'<h3>(.*?)</h3>', c, re.S).group(1).strip()
    rel='②上下级' if 'badge r2' in c else '③高管间'
    st='一手' if 'badge b1' in c else '二手'
    val=re.search(r'<p class="val">(.*?)</p>', c, re.S)
    val=re.sub(r'\s+','',val.group(1)) if val else ''
    return t, rel, st, val

rows=[]
for c in cards:
    t,rel,st,val=parse(c)
    one=val[:92]+'…' if len(val)>92 else val
    rows.append(f"| {t}（openday.html） | 4 | {st} | {rel} | {one} |")

print("wall cards parsed:", len(rows))

# ---- 1. summary note ----
s=open(SUMM,encoding='utf-8').read()
# frontmatter date
s=re.sub(r'(date:\s*)\d{4}-\d{2}-\d{2}', r'\g<1>2026-09-08', s, count=1)
# count
s=s.replace('共 319 张','共 327 张',1)
# insert r40 round block before '## 卡片总表'
RB='+ **四十轮补采 2026-09-08(+8：平罗县/聊城市/青岛科普畅游月/重庆西部科学城/天津生物智造·政务与科普开放日5②全一手 ｜ 37国AI能力建设圆桌/WGL全球本土化大会/可持续发展商业大会·3②3③，5一手+3二手)**'
assert '## 卡片总表' in s, "summary 卡片总表 anchor missing"
s=s.replace('## 卡片总表', RB+'\n## 卡片总表',1)
# regenerate table: keep everything up to the header separator line, then append rows
head, sep, rest = s.partition('| 卡 | 质量分')
# head includes everything up to start of header row; sep is the header row text
# find the full header block: '| 卡 | 质量分 | 一手/二手 | 适用关系 | 一句话定位 |\n|---|---|---|---|---|'
m=re.search(r'\| 卡 \| 质量分 \| 一手/二手 \| 适用关系 \| 一句话定位 \|\n\|---+\|', s)
assert m, "summary table header not found"
hdr_end=m.end()
new_table=s[:hdr_end]+'\n'+'\n'.join(rows)+'\n'
open(SUMM,'w',encoding='utf-8').write(new_table)
print("SUMM updated ->", SUMM, "| rows:", len(rows))

# ---- 2. runs note ----
run_rows=[
 ("平罗县2026年『政府开放日』系列活动（四主题分场次走进政务现场）","一手","②上下级","平罗县分主题分场次(农改/发改/水利/医保),四段闭环观摩—座谈—问卷—宣讲,政务公开升级共建共治"),
 ("聊城市2026年9月政府开放活动预告（多部门整合·含『工地业主开放日』）","一手","②上下级","聊城聚合公安/住建/水利/审批多部门预告,『工地业主开放日』工程师带队讲规划材料工艺、意见整改闭环"),
 ("青岛科普场馆畅游月·18家高校院所向公众开放（省内首次聚合）","一手","②上下级","青岛科协牵头18家院所集中开放,覆盖海洋/AI/生命/天文等数十学科,免费讲解+分场次预约降低门槛"),
 ("重庆西部科学城科技节·10处真实科研实验室面向中小学生开放","一手","②上下级","重庆西部科学城开放10处真实科研机构,体验营+会客厅+手工坊+科学短视频四步,首席科学家互动讲座"),
 ("天津『生物智造·聚力未来』科普开放日（面向小学生免费）","一手","②上下级","合成生物国家技术创新中心联动多科普基地,产品展示区+动手实验区双区,把国家战略变青少年可感好奇"),
 ("37国代表在京共探全球人工智能能力建设研讨班·全球合作圆桌","二手","③高管间","外交部主办北大承办,37国政府高官+AI政策制定者,讲座+参访+圆桌三段式,产学研服同台议全球治理规则"),
 ("WGL 2026第八届全球本土化大会·深圳（平台高管与品牌操盘者同场）","二手","③高管间","WaveGlocal主办深圳全球化大会,Meta/Google/Shopify等平台高管+品牌CXO同场,指数报告首发+三大论坛圆桌共创"),
 ("2026可持续发展商业大会·上海（两场战略圆桌+智库产业资本签约）","二手","③高管间","上海可持续商业大会设新质生产力/企业国际竞争力双圆桌,吕建中阐释复合价值新型战略,智库产业资本签约转化合作"),
]
md=f"""---
title: Open Day 第四十轮知识卡
tags: [知识采集, 开放日, 自动化采集, 轮次]
date: 2026-09-08
type: 自动化采集
---

# Open Day 开放日 · 第四十轮补采（2026-09-08）

## 本轮回链
- GitHub Pages 独立页：{RUN_PAGE}
- 本地路径：{LOCAL}
- 累计总索引墙：{WALL_PAGE}

## 本轮新增 8 张（②上下级 5 / ③高管间 3）

| 卡 | 一手/二手 | 适用关系 | 一句话定位 |
|---|---|---|---|
"""
for t,st,rel,one in run_rows:
    md+=f"| {t} | {st} | {rel} | {one} |\n"
os.makedirs(os.path.dirname(RUNS_NOTE), exist_ok=True)
open(RUNS_NOTE,'w',encoding='utf-8').write(md)
print("RUNS NOTE ->", RUNS_NOTE)

# ---- 3. 00-索引 append 8 rows at EOF ----
idx_lines=open(IDX0,encoding='utf-8').read().splitlines()
# build 8 rows (title matches summary table minus '（openday.html）' suffix? keep same style with （openday.html）)
idx_rows=[]
for t,st,rel,one in run_rows:
    idx_rows.append(f"| {t}（openday.html） | 4 | {st} | {rel} | {one} |")
with open(IDX0,'a',encoding='utf-8') as f:
    f.write('\n'+'\n'.join(idx_rows)+'\n')
print("IDX0 appended 8 rows at EOF")
print("DONE obsidian r40")
