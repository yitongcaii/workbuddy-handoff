# -*- coding: utf-8 -*-
"""员工大会 r37 Obsidian 落库：① 汇总笔记 prepend r37 block ② 00-索引追加 8 行+轮次段 ③ runs 独立笔记新建。"""
import os

VAULT = 'C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库'
SM = os.path.join(VAULT, '素材', 'staff-meeting', '员工大会-知识卡汇总.md')
IDX = os.path.join(VAULT, '00-知识采集索引.md')
RUNS_DIR = os.path.join(VAULT, '素材', 'staff-meeting', 'runs')
RUN_NOTE = os.path.join(RUNS_DIR, '员工大会-2026-09-07-第三十七轮-知识卡.md')

GH = 'https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/runs/staff-meeting-2026-09-07-r37.html'
LOCAL = 'C:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection/staff-meeting/runs/staff-meeting-2026-09-07-r37.html'
WALL = 'https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/staff-meeting.html'

# ---------- ① 汇总笔记：prepend r37 block ----------
block = '''## 轮次 20260907-r37（+8）

| 卡 | 适用关系 | 一手/二手 |
|---|---|---|
| 高管变革沟通·用「执行叙事」把战略讲成故事（before/now/soon 三幕） | 高管间 | 二手 |
| 领导讲故事的结构·张力→转折→新现实 | 高管间 | 二手 |
| 高管故事力四支柱·叙事智力+情绪校准+真实存在感+数据×情感 | 高管间 | 二手 |
| 高管叙事「3C」框架·挑战·选择·改变 | 高管间 | 二手 |
| 全员会会后闭环·Recap+反馈调研+行动跟进+ROI 度量 | 上下级 | 二手 |
| Town Hall 本质与避坑·5段议程+远程优先+3大常见错误 | 上下级 | 二手 |
| 企业全员大会组织技巧·30天倒计时/风险预案/AV/分级通知 | 上下级 | 二手 |
| 多渠道宣贯策略·提升员工大会参与度 | 上下级 | 二手 |

'''
sm = open(SM, encoding='utf-8').read()
marker = '## 轮次 20260906-r36（+7）'
assert marker in sm, 'summary marker not found'
sm = sm.replace(marker, block + marker, 1)
open(SM, 'w', encoding='utf-8').write(sm)
print('SM updated; r37 block prepended.')

# ---------- ② 00-索引：追加 8 行 + 更新 header ----------
idx = open(IDX, encoding='utf-8').read()

# header 追加本轮段
hdr_old = '会后脉冲调研））'
hdr_new = '会后脉冲调研）｜ 三十七轮 enrich 2026-09-07(+8)）'
assert hdr_old in idx, 'header tail not found'
idx = idx.replace(hdr_old, hdr_new, 1)

# 在 staff-meeting 段末（最后一张卡行）后插入 8 行
last_row = '| 管理者沟通工具包·5 要点+FAQ+级联模板（二手）（staff-meeting.html） | 4 | 二手 | ②上下级 | 管理者沟通工具包（5要点+FAQ+级联模板），让经理提前有答案而非最后才知会。 |'
assert last_row in idx, 'last row not found'
new_rows = '''| 高管变革沟通·用「执行叙事」把战略讲成故事（二手）（staff-meeting.html） | 5 | 二手 | ③高管间 | 高管变革用 before/now/soon 三幕执行叙事把战略讲成故事，个人故事拉近距离、会后度量效果。 |
| 领导讲故事的结构·张力→转折→新现实（二手）（staff-meeting.html） | 5 | 二手 | ③高管间 | 领导故事三段=张力→转折→新现实，先找故事再找slide，越具体越可信。 |
| 高管故事力四支柱·叙事智力+情绪校准+真实存在感+数据×情感（二手）（staff-meeting.html） | 5 | 二手 | ③高管间 | 高管故事力四支柱（叙事智力/情绪校准/真实存在感/激进清晰），Gartner 列为核心特质。 |
| 高管叙事「3C」框架·挑战·选择·改变（二手）（staff-meeting.html） | 5 | 二手 | ③高管间 | 高管3C叙事（挑战/选择/改变），叙事先于决策，沉默会被他人填认知空白。 |
| 全员会会后闭环·Recap+反馈调研+行动跟进+ROI 度量（二手）（staff-meeting.html） | 5 | 二手 | ②上下级 | 全员会会后闭环（24h recap+调研ROI+行动owner），会议价值在会后才发生。 |
| Town Hall 本质与避坑·5段议程+远程优先+3大常见错误（二手）（staff-meeting.html） | 5 | 二手 | ②上下级 | Town Hall 重双向对话+Q&A，5段议程+远程优先，3大错误+书面recap。 |
| 企业全员大会组织技巧·30天倒计时/风险预案/AV/分级通知（二手）（staff-meeting.html） | 4 | 二手 | ②上下级 | 企业全员大会30天倒计时SOP+12类风险预案+200+物资矩阵+分级通知。 |
| 多渠道宣贯策略·提升员工大会参与度（二手）（staff-meeting.html） | 4 | 二手 | ②上下级 | 多渠道宣贯（内网/邮件/社交+奖励+口碑）提升员工大会参与度。 |
'''
idx = idx.replace(last_row, last_row + '\n' + new_rows.rstrip('\n'), 1)
open(IDX, 'w', encoding='utf-8').write(idx)
print('00-INDEX updated; 8 rows appended + header round段.')

# ---------- ③ runs 独立笔记 ----------
os.makedirs(RUNS_DIR, exist_ok=True)
note = f'''---
title: 员工大会-2026-09-07-第三十七轮-知识卡
type: 自动化采集
date: 2026-09-07
tags: [知识采集, 员工大会, 第三十七轮]
relation: [supervisor, exec]
---

# 员工大会 · 第三十七轮补采（2026-09-07，+8）

> 本轮独立页（GitHub Pages）：{GH}
> 本地路径：{LOCAL}
> 累计总索引墙：{WALL}

## 本轮新增 8 卡（关系分层）

### ③ 领导↔领导（高管间 · exec）— 4 卡
- 高管变革沟通·用「执行叙事」把战略讲成故事（before/now/soon 三幕）〔二手〕
- 领导讲故事的结构·张力→转折→新现实〔二手〕
- 高管故事力四支柱·叙事智力+情绪校准+真实存在感+数据×情感〔二手〕
- 高管叙事「3C」框架·挑战·选择·改变〔二手〕

### ② 领导↔员工（上下级 · supervisor）— 4 卡
- 全员会会后闭环·Recap+反馈调研+行动跟进+ROI 度量〔二手〕
- Town Hall 本质与避坑·5段议程+远程优先+3大常见错误〔二手〕
- 企业全员大会组织技巧·30天倒计时/风险预案/AV/分级通知〔二手〕
- 多渠道宣贯策略·提升员工大会参与度〔二手〕

## 六维评估
相关度 / 权威性 / 时效性 / 去重度 / 可落地 / 关系适配度 均 ≥3，全部过线。本次为饱和主题补稀缺子域：高管叙事框架（执行叙事/故事结构/故事力四支柱/3C）、会后闭环与ROI度量、Town Hall 双向对话避坑、大会组织30天SOP、会前多渠道宣贯。

## 一手/二手
本轮 8 张全为二手（方法论/思想领导力来源），无重复 URL 入库。
'''
open(RUN_NOTE, 'w', encoding='utf-8').write(note)
print('RUN NOTE created:', RUN_NOTE)
