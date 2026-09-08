# -*- coding: utf-8 -*-
"""员工大会 r39 Obsidian 同步：汇总笔记插块 + 00-索引追加 8 行 + 新建 runs 笔记。"""
import os

VAULT = r'C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库'
SUMMARY = os.path.join(VAULT, '素材', 'staff-meeting', '员工大会-知识卡汇总.md')
INDEX = os.path.join(VAULT, '00-知识采集索引.md')
RUNS_DIR = os.path.join(VAULT, '素材', 'staff-meeting', 'runs')

# ---- r39 块（汇总笔记，倒序插在最前）----
R39_BLOCK = '''## 轮次 20260908-r39（+8）

| 卡 | 适用关系 | 一手/二手 |
|---|---|---|
| 新领导首次全员会操盘·目标先行+会前邀员工参与+会后闭环 | 高管间 | 二手 |
| 变革沟通计划·高管叙事与员工落地分开写+多渠道矩阵 | 高管间 | 二手 |
| 变革期领导沟通·会前会+会后会+故事化+过度沟通 | 高管间 | 二手 |
| 职工大会领导讲话稿·受众分层翻译+我们叙事+三段式 | 高管间 | 二手 |
| 虚拟 town hall 直播制作·全球可达+省 50% 成本+合规归档 | 上下级 | 二手 |
| Town Hall 影响力 4 策略·会前预热+经理翻译+会后跟进 | 上下级 | 二手 |
| 武装传声筒·变革成败在中间层经理（授权而非转发管道） | 上下级 | 二手 |
| 全员会 3 个范式转移·从议题到效果/推送变拉动/一刀切变个性化 | 上下级 | 二手 |

'''

# ---- 00-索引 8 行 ----
ROWS = [
  '| 新领导首次全员会操盘·目标先行+会前邀员工参与+会后闭环（二手）（staff-meeting.html） | 5 | 二手 | ③高管间 | Justworks：首次全员会=团队对齐仪式；会前数周用调研收集员工心声塑议程、用「愿景→部门更新→战果与挑战→Q&A」结构、会后 recap+收反馈+兑现承诺、指定制片人管时序。 |',
  '| 变革沟通计划·高管叙事与员工落地分开写+多渠道矩阵（二手）（staff-meeting.html） | 5 | 二手 | ③高管间 | Changeadaptive：受众切高管/员工分别写；渠道矩阵 Town Hall+邮件+内网+领导视频+面谈+调研 Q&A；高管讲 Why、经理讲 So-what。 |',
  '| 变革期领导沟通·会前会+会后会+故事化+过度沟通（二手）（staff-meeting.html） | 5 | 二手 | ③高管间 | HFMA(Jill Geisler)：会前先与受信任影响者 1:1 透风、会后会领导走场一对一、把信息当货币宁可过度沟通、用 master narrative 讲真实故事。 |',
  '| 职工大会领导讲话稿·受众分层翻译+我们叙事+三段式（二手）（staff-meeting.html） | 4 | 二手 | ③高管间 | 人人文库：对基层讲收入/技能/通道、对管理讲效能/荣誉分开写；用「我们」替代「我/你们」；结构=开场破冰→主体分层→结尾升华。 |',
  '| 虚拟 town hall 直播制作·全球可达+省 50% 成本+合规归档（二手）（staff-meeting.html） | 5 | 二手 | ②上下级 | webcasting：专业直播让全球/远程/混合员工同场参与；实时投票+审核 Q&A+聊天；省场地差旅最高 50%；会后点播归档用于 onboarding 与合规。 |',
  '| Town Hall 影响力 4 策略·会前预热+经理翻译+会后跟进（二手）（staff-meeting.html） | 4 | 二手 | ②上下级 | Oxeon Cross：会前 2 周征集/投票议题多触点造期待；给中坚经理工具包翻译信息；会后 recap+承诺记录+未答 Q 解答+数周进度更新。 |',
  '| 武装传声筒·变革成败在中间层经理（授权而非转发管道）（二手）（staff-meeting.html） | 5 | 二手 | ②上下级 | Leadership Story Bank：员工从直属经理听变革；给经理早获取信息+提问空间+FAQ 工具包+情绪空间+反馈回路，当共创者非传声筒。 |',
  '| 全员会 3 个范式转移·从议题到效果/推送变拉动/一刀切变个性化（二手）（staff-meeting.html） | 4 | 二手 | ②上下级 | Gathering Effect：从议题→效果(用效果筛议程)；从推送→拉动(给员工角色/问题开场/共创)；从一刀切→个性化(会前讲为何此刻重要/会后 after-show/收尾总结)。 |',
]

# ---- runs 笔记 ----
RUN_NOTE = '''---
title: 员工大会-2026-09-08-第三十九轮-知识卡
type: 自动化采集
date: 2026-09-08
tags: [知识采集, 员工大会, 第三十九轮]
relation: [supervisor, exec]
---

# 员工大会 · 第三十九轮补采（2026-09-08，+8）

> 本轮独立页（GitHub Pages）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/runs/staff-meeting-2026-09-08-r39.html
> 本地路径：C:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection/staff-meeting/runs/staff-meeting-2026-09-08-r39.html
> 累计总索引墙：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/staff-meeting.html

## 本轮新增 8 卡（关系分层）

### ③ 领导↔领导（高管间 · exec）— 4 卡
- 新领导首次全员会操盘·目标先行+会前邀员工参与+会后闭环〔二手〕
- 变革沟通计划·高管叙事与员工落地分开写+多渠道矩阵〔二手〕
- 变革期领导沟通·会前会+会后会+故事化+过度沟通〔二手〕
- 职工大会领导讲话稿·受众分层翻译+我们叙事+三段式〔二手〕

### ② 领导↔员工（上下级 · supervisor）— 4 卡
- 虚拟 town hall 直播制作·全球可达+省 50% 成本+合规归档〔二手〕
- Town Hall 影响力 4 策略·会前预热+经理翻译+会后跟进〔二手〕
- 武装传声筒·变革成败在中间层经理（授权而非转发管道）〔二手〕
- 全员会 3 个范式转移·从议题到效果/推送变拉动/一刀切变个性化〔二手〕

## 六维评估
相关度 / 权威性 / 时效性 / 去重度 / 可落地 / 关系适配度 均 ≥3，全部过线。本次为饱和主题补稀缺子域：新领导首会操盘、变革沟通计划矩阵、HFMA 会前会/会后会、职工大会讲话稿受众分层、虚拟 town hall 直播制作、Town Hall 影响力 4 策略、中间层经理赋能、全员会范式转移。8 张全部为二手（方法论/技术/案例来源），URL 经去重无重复入库。

## 一手/二手
本轮 8 张均为二手（外部方法论/案例/技术来源），无平级（peer）内容，符合「仅②③」硬约束。
'''

# ===== 1. 汇总笔记：插 r39 块到最前（# 员工大会 标题之后、首个 ## 轮次 之前）=====
s = open(SUMMARY, encoding='utf-8').read()
marker = '# 员工大会 · 知识卡汇总（2026-08-07 自动化采集）'
idx = s.index(marker) + len(marker)
head = s[:idx]
tail = s[idx:]
if '轮次 20260908-r39' not in s:
    new_s = head + '\n' + R39_BLOCK + tail
    open(SUMMARY, 'w', encoding='utf-8').write(new_s)
    print('SUMMARY: r39 block inserted')
else:
    print('SUMMARY: r39 block already present, skip')

# ===== 2. 00-索引：段头加三十九轮 + 段尾插 8 行 =====
idx_txt = open(INDEX, encoding='utf-8').read()
# 2a 段头
old_hdr = '｜ 三十八轮 enrich 2026-09-08(+8)）'
new_hdr = '｜ 三十八轮 enrich 2026-09-08(+8)｜ 三十九轮 enrich 2026-09-08(+8)）'
if old_hdr in idx_txt:
    idx_txt = idx_txt.replace(old_hdr, new_hdr, 1)
    print('INDEX: header updated')
else:
    print('INDEX: header pattern NOT found, skip header update')

# 2b 段尾插 8 行（在 ## 主题：Offsite 之前）
offsec = '## 主题：Offsite 团建务虚（2026-08-07）'
if offsec in idx_txt and '三十九轮 enrich 2026-09-08' not in idx_txt.split(offsec)[0][-200:]:
    rows_block = '\n'.join(ROWS) + '\n\n'
    idx_txt = idx_txt.replace(offsec, rows_block + offsec, 1)
    print('INDEX: 8 rows appended before Offsite section')
else:
    print('INDEX: Offsite section not found or rows already present, skip row append')

open(INDEX, 'w', encoding='utf-8').write(idx_txt)

# ===== 3. runs 笔记 =====
os.makedirs(RUNS_DIR, exist_ok=True)
run_path = os.path.join(RUNS_DIR, '员工大会-2026-09-08-第三十九轮-知识卡.md')
if not os.path.exists(run_path):
    open(run_path, 'w', encoding='utf-8').write(RUN_NOTE)
    print('RUN NOTE: created', run_path)
else:
    print('RUN NOTE: already exists, skip')
