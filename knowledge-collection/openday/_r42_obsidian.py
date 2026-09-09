# -*- coding: utf-8 -*-
"""r42 Obsidian 落库：汇总笔记(覆盖式计数+轮次段+尾插10行) + runs独立笔记 + 00-索引EOF追加10行。仅写到 vault 子目录。"""
import os, re

VAULT = r"C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库"
SUMM  = os.path.join(VAULT, "素材", "openday", "OpenDay-开放日-知识卡汇总.md")
IDX0  = os.path.join(VAULT, "00-知识采集索引.md")
RUNS_NOTE = os.path.join(VAULT, "素材", "openday", "runs", "OpenDay-2026-09-09-第四十二轮-知识卡.md")

RUN_PAGE = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday-20260909b.html"
WALL_PAGE = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday.html"
LOCAL = r"C:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection\openday\openday-20260909b.html"

# ===== 本轮回增 10 张固定列表（②5: 3一手+2二手 / ③5: 4一手+1二手） =====
new_rows = [
  ("安庆大观区法院『法院开放日』：旁听庭审变身『法治公开课』（分众化普法·公职人员/青少年/社区）", "一手", "②上下级",
   "大观区法院将真实庭审变鲜活『法治公开课』,按受众拆三套剧本,庭审后加法官互动答疑,以常态化开放积累公信力"),
  ("永丰县公安局『政府开放日』暨警营开放日：派出所+警务站+训练基地+特警大队全动线", "二手", "②上下级",
   "永丰公安用五站串联做多场景透明动线,以座谈+局长直面答疑把你看变你说,构建和谐警民关系"),
  ("临沂沂河新区综保区『政府开放日』：开放综保·共赢未来——聚焦通关便利助力企业", "二手", "②上下级",
   "临沂综保区用展厅+卡口+一网通办动线,以问题台账+限时办结把开放日变政企连心桥"),
  ("上海税务『政府开放月』：办税服务厅+纳税人学堂+『小小税官』体验日（优化营商环境）", "一手", "②上下级",
   "上海税务按对象拆三档办税体验+柔性触达企业,是税务系统政务公开+营商优化可复制模板"),
  ("景德镇市图书馆『政府开放日』：365天免费开放+陶瓷文献馆+城市书房+智慧图书馆全景体验", "一手", "②上下级",
   "景德镇文旅局以导览动线+互动让市民看懂文化惠民,以问卷征集把开放日变服务优化入口"),
  ("2025世界互联网大会乌镇峰会·互联网企业家论坛：创新驱动 智启未来（300余位企业代表政商学界同台）", "二手", "③高管间",
   "乌镇峰会以主旨演讲+圆桌对话让CEO围绕AI演进/产业融合/安全治理共创,是互联网高管对话模板"),
  ("第八届虹桥国际经济论坛『合规与全球制造业共赢发展』：工信部/商务部主办·中外制造企业合规出海", "一手", "③高管间",
   "进博国家级平台抬升规格,让部长与央企/龙头董事长同台议合规出海/标准互认/风险管理"),
  ("2025夏季达沃斯论坛（天津·第十六届新领军者年会）：新时代企业家精神（1800嘉宾·近200分论坛）", "一手", "③高管间",
   "以新时代企业家精神为命题,五大方向分论坛+民营企业沙龙+投资中国对接,顶级经济领袖年会模板"),
  ("中国发展高层论坛2025年会：全面释放发展动能·共促全球经济稳定增长（80+外企高管·CDF）", "一手", "③高管间",
   "以全面释放发展动能锚定,部长与跨国CEO同台议合作,以新质合作共识替代零和,最高规格政企对话"),
  ("博鳌亚洲论坛2025年会：在世界变局中共创亚洲未来（60+国家1500嘉宾·多边主义与全球治理）", "一手", "③高管间",
   "以在世界变局中共创亚洲未来锚定,多轨分论坛让总统/总理/国际组织负责人/CEO同台,区域多边主义模板"),
]

# ---- 1. summary note ----
s = open(SUMM, encoding='utf-8').read()
# count
assert '共 337 张' in s, "summary count 337 not found"
s = s.replace('共 337 张', '共 347 张', 1)
# insert r42 round block before '## 卡片总表'
RB = '+ **四十二轮补采 2026-09-09(+10：大观区法院/永丰县警营/沂河新区综保区海关/上海税务/景德镇市图书馆·政府开放日向·5②3一手+2二手 ｜ 乌镇峰会2025互联网企业家论坛/第八届虹桥论坛/2025夏季达沃斯天津/中国发展高层论坛2025/博鳌亚洲论坛2025·5③4一手+1二手)**'
assert '## 卡片总表' in s, "summary 卡片总表 anchor missing"
s = s.replace('## 卡片总表', RB + '\n## 卡片总表', 1)
# append 10 new rows at EOF (table is last block)
table_rows = [f"| {t}（openday.html） | 4 | {st} | {rel} | {one} |" for t, st, rel, one in new_rows]
if not s.endswith('\n'):
    s += '\n'
s += '\n'.join(table_rows) + '\n'
open(SUMM, 'w', encoding='utf-8').write(s)
print("SUMM updated -> 共 347 张 | rows appended:", len(table_rows))

# ---- 2. runs note ----
md = f"""---
title: Open Day 第四十二轮知识卡
tags: [知识采集, 开放日, 自动化采集, 轮次]
date: 2026-09-09
type: 自动化采集
---

# Open Day 开放日 · 第四十二轮补采（2026-09-09）

## 本轮回链
- GitHub Pages 独立页：{RUN_PAGE}
- 本地路径：{LOCAL}
- 累计总索引墙：{WALL_PAGE}

## 本轮新增 10 张（②上下级 5 / ③高管间 5）

| 卡 | 一手/二手 | 适用关系 | 一句话定位 |
|---|---|---|---|
"""
for t, st, rel, one in new_rows:
    md += f"| {t} | {st} | {rel} | {one} |\n"
os.makedirs(os.path.dirname(RUNS_NOTE), exist_ok=True)
open(RUNS_NOTE, 'w', encoding='utf-8').write(md)
print("RUNS NOTE ->", RUNS_NOTE)

# ---- 3. 00-索引 append 10 rows at EOF ----
idx_rows = [f"| {t}（openday.html） | 4 | {st} | {rel} | {one} |" for t, st, rel, one in new_rows]
with open(IDX0, 'a', encoding='utf-8') as f:
    f.write('\n' + '\n'.join(idx_rows) + '\n')
print("IDX0 appended 10 rows at EOF")
print("DONE obsidian r42")
