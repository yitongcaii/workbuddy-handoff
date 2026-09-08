# -*- coding: utf-8 -*-
"""r41 Obsidian 落库：汇总笔记(改覆盖) + runs独立笔记 + 00-索引追加。仅写到 vault 子目录。"""
import os, re, json

VAULT = r"C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库"
WALL  = r"C:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection/openday/openday.html"
SUMM  = os.path.join(VAULT, "素材", "openday", "OpenDay-开放日-知识卡汇总.md")
IDX0  = os.path.join(VAULT, "00-知识采集索引.md")
RUNS_NOTE = os.path.join(VAULT, "素材", "openday", "runs", "OpenDay-2026-09-09-第四十一轮-知识卡.md")

RUN_PAGE = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday-20260909.html"
WALL_PAGE = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday.html"
LOCAL = r"C:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection\openday\openday-20260909.html"

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
s=re.sub(r'(date:\s*)\d{4}-\d{2}-\d{2}', r'\g<1>2026-09-09', s, count=1)
# count
s=s.replace('共 327 张','共 337 张',1)
# insert r41 round block before '## 卡片总表'
RB='+ **四十一轮补采 2026-09-09(+10：茌平区/泰安市/吴忠市/荣县·政务与政企开放日4②全一手 ｜ 联通智网科技"一核五维"国企开放日·1②二手 + 《财富》领军者论坛澳门/2026鼓浪屿论坛·世界商业领袖/太原能源低碳发展论坛/WBCSD Two Lakes Dialogue 武汉/新加坡AI高管午餐会·5③1一手+4二手)**'
assert '## 卡片总表' in s, "summary 卡片总表 anchor missing"
s=s.replace('## 卡片总表', RB+'\n## 卡片总表',1)
# regenerate table
m=re.search(r'\| 卡 \| 质量分 \| 一手/二手 \| 适用关系 \| 一句话定位 \|\n\|---+\|', s)
assert m, "summary table header not found"
hdr_end=m.end()
new_table=s[:hdr_end]+'\n'+'\n'.join(rows)+'\n'
open(SUMM,'w',encoding='utf-8').write(new_table)
print("SUMM updated ->", SUMM, "| rows:", len(rows))

# ---- 2. runs note ----
run_rows=[
 ("茌平区2026年9月份政府开放活动预告（民政/行政审批/便民/文化书院/人社五场）","一手","②上下级","聊城市茌平区整合民政/行政审批/博平镇/人社五场活动,每场固定现场参观+业务讲解+互动答疑,把政务公开变双向沟通"),
 ("泰安市2026年9月份政府开放活动计划（街道便民/科技金融政银企/税务/医保多板块）","一手","②上下级","泰安旅游经开区按街道/部门拆分主题各做专场,用『我陪群众走流程』把领导/骨干变陪办员,从你来讲变我陪办"),
 ("吴忠市审批服务管理局·公共资源交易中心2026年『政府开放日』（零距离体验审批·见证阳光交易）","一手","②上下级","吴忠市审批+交易双现场透明课,政务大厅+开评标区双动线,座谈征集建议并限期反馈,把开放日变阳光政府信任工程"),
 ("荣县科技和经济信息化局2026年『政务开放日』（政企同心·向新而行·走进智造企业）","一手","②上下级","荣县工科局『走进企业+政策宣讲+圆桌恳谈』三段式,以新质生产力/设备更新/高企认定切入,县级工科部门政务公开可复制模板"),
 ("联通智网科技2026年国企开放日『一核五维』体系（5G智能网联示范基地+跨界沙龙+科技兴农）","二手","②上下级","以高质量党建为核心,五维落地;5G智能网联示范基地做可体验实景场,以跨界沙龙+产教融合+科技兴农三路延伸到课堂与田野"),
 ("《财富》领军者论坛 Fortune Leaders Forum 澳门开幕（百位商界领袖·复杂时代的领导力）","二手","③高管间","《财富》与澳娱合办,百位商界领袖围绕融合与复杂时代下的领导力对话,聚焦大湾区机遇+AI基础设施+能源转型+数字金融"),
 ("2026鼓浪屿论坛·世界商业领袖共话全球投资（企业出海非商业类风险防控）","二手","③高管间","投洽会配套,驻华大使/龙头CEO/投资机构同台,主旨演讲+高端对话+签约全链条,围绕出海合规与跨国投资风险共创"),
 ("2026年太原能源低碳发展论坛（双碳引领·5场国际会议+外商投资企业圆桌+大使茶座）","二手","③高管间","外交部/能源局/山西省政府合办,设投资中国对话山西外企圆桌+大使茶座,把开放日变招商引资与国际合作入口"),
 ("WBCSD Two Lakes Dialogue 2026·武汉（CEO/C-suite 气候与碳市场高管对话）","一手","③高管间","WBCSD主办,资格限CEO/董事会主席/C-suite,执行层圆桌+私下会谈保证深度,议题直击碳市场/绿色供应链/ESG出海"),
 ("新加坡亚洲云与AI基础设施展·AI高管午餐会（从AI试点到企业影响力·闭门圆桌）","二手","③高管间","新加坡高级技术与商业领袖闭门午餐会,按技术/部署/伙伴关系三维结构化探讨,把AI从试点推向企业规模化能力"),
]
md=f"""---
title: Open Day 第四十一轮知识卡
tags: [知识采集, 开放日, 自动化采集, 轮次]
date: 2026-09-09
type: 自动化采集
---

# Open Day 开放日 · 第四十一轮补采（2026-09-09）

## 本轮回链
- GitHub Pages 独立页：{RUN_PAGE}
- 本地路径：{LOCAL}
- 累计总索引墙：{WALL_PAGE}

## 本轮新增 10 张（②上下级 5 / ③高管间 5）

| 卡 | 一手/二手 | 适用关系 | 一句话定位 |
|---|---|---|---|
"""
for t,st,rel,one in run_rows:
    md+=f"| {t} | {st} | {rel} | {one} |\n"
os.makedirs(os.path.dirname(RUNS_NOTE), exist_ok=True)
open(RUNS_NOTE,'w',encoding='utf-8').write(md)
print("RUNS NOTE ->", RUNS_NOTE)

# ---- 3. 00-索引 append 10 rows at EOF ----
idx_rows=[]
for t,st,rel,one in run_rows:
    idx_rows.append(f"| {t}（openday.html） | 4 | {st} | {rel} | {one} |")
with open(IDX0,'a',encoding='utf-8') as f:
    f.write('\n'+'\n'.join(idx_rows)+'\n')
print("IDX0 appended 10 rows at EOF")
print("DONE obsidian r41")
