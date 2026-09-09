# -*- coding: utf-8 -*-
"""员工大会 r40 Obsidian 同步：汇总笔记插块 + 00-索引追加 7 行 + 新建 runs 笔记。
（airmeet 度量卡与既有 staff-meeting 卡 URL 撞重，已剔除以保唯一；本轮净 +7）"""
import os

VAULT = r'C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库'
SUMMARY = os.path.join(VAULT, '素材', 'staff-meeting', '员工大会-知识卡汇总.md')
INDEX = os.path.join(VAULT, '00-知识采集索引.md')
RUNS_DIR = os.path.join(VAULT, '素材', 'staff-meeting', 'runs')

# ---- r40 块（汇总笔记，倒序插在最前）----
R40_BLOCK = '''## 轮次 20260909-r40（+7）

| 卡 | 适用关系 | 一手/二手 |
|---|---|---|
| AI 数字人 CEO 视频内通·高频常规更新（危机/重大变革须真人） | 高管间 | 二手 |
| 高管 Q&A 难问题/敌意问题·四步应答（acknowledge→substance→constraints→next） | 高管间 | 二手 |
| 高管全员会 临场气场·肢体语言（占空间+眼神+能量先于内容） | 高管间 | 二手 |
| 全员会 频率/节奏 决策（月度理想·季度大·危机周更·Q&A≥30%） | 高管间 | 二手 |
| RTO 返office 全员会沟通·live forum 而非邮件+先听后推+区分两类体验 | 上下级 | 二手 |
| IPO 里程碑全员会·org meeting 当日 townhall+quiet period+只谈业务不谈发行 | 上下级 | 二手 |
| 全员会 Q&A 准备模板·message themes+likely/sensitive questions+follow-up | 上下级 | 二手 |

'''

# ---- 00-索引 7 行 ----
ROWS = [
  '| AI 数字人 CEO 视频内通·高频常规更新（危机/重大变革须真人）（二手）（staff-meeting.html） | 5 | 二手 | ③高管间 | KHABY AI：CEO 高保真数字分身按脚本生成内部视频，填补高频小更新空白（周更业务摘要/政策解读/多地同步，2-3 倍文字邮件参与）；信息类可用、危机/重大变革/文化里程碑须真人；治理三基线：肖像授权+内容范围限定+高管审签+AI 披露。 |',
  '| 高管 Q&A 难问题/敌意问题·四步应答（二手）（staff-meeting.html） | 5 | 二手 | ③高管间 | Winning Presentations：四步法——承认情绪不认框架+60 秒实质（结论→理由→约束）+点出未尽+给下一步；敌意问题误判是 over-explain 像 filibuster；虚拟场读聊天队列、每步前停 2 秒。 |',
  '| 高管全员会 临场气场·肢体语言（二手）（staff-meeting.html） | 4 | 二手 | ③高管间 | Mazterpiece：可信度开场前由身体判定；占住空间再拿麦（用满台边角非只站中央）、持续眼神接触、能量先于内容；姿势是可训练杠杆非性格天赋。 |',
  '| 全员会 频率/节奏 决策（二手）（staff-meeting.html） | 4 | 二手 | ③高管间 | RoamJobs：频率按规模与变革速度——初创剧变周更、成熟月度、超大季更+部门补；锁 45 分钟、议程 3-4 题、Q&A≥30%；随意取消=释放「沟通只在有事时重要」信号。 |',
  '| RTO 返office 全员会沟通·live forum 而非邮件+先听后推+区分两类体验（二手）（staff-meeting.html） | 5 | 二手 | ②上下级 | Ragan(Stellantis)：RTO 考验是员工是否觉得被理解；现场全员会而非邮件、推前做调研焦点小组真去听、承认「常驻 office」与「习惯远程」是两种体验、宣布后领导物理在场。 |',
  '| IPO 里程碑全员会·org meeting 当日 townhall+quiet period+只谈业务不谈发行（二手）（staff-meeting.html） | 5 | 二手 | ②上下级 | New Street IR/Gilmartin：IPO 以 org meeting 起跑、当日开全员 townhall 讲为何上市/意味着什么/对外唯一联系人；HR 提前做内幕交易培训；S-1 翻转后静默期+FAQ+townhall；全程只谈业务不谈估值/时间表/发行。 |',
  '| 全员会 Q&A 准备模板·message themes+likely/sensitive questions+follow-up（二手）（staff-meeting.html） | 4 | 二手 | ②上下级 | HogoNext：可复用 Q&A 准备 doc——message themes+likely questions(为何问+草稿+数据+负责人)+sensitive questions(安全边界+法务/HR 审+bridge)+over-answering 禁区+follow-up plan。 |',
]

# ---- runs 笔记 ----
RUN_NOTE = '''---
title: 员工大会-2026-09-09-第四十轮-知识卡
type: 自动化采集
date: 2026-09-09
tags: [知识采集, 员工大会, 第四十轮]
relation: [supervisor, exec]
---

# 员工大会 · 第四十轮补采（2026-09-09，+7）

> 本轮独立页（GitHub Pages）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/runs/staff-meeting-2026-09-09-r40.html
> 本地路径：C:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection/staff-meeting/runs/staff-meeting-2026-09-09-r40.html
> 累计总索引墙：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/staff-meeting.html

## 本轮新增 7 卡（关系分层）

### ③ 领导↔领导（高管间 · exec）— 4 卡
- AI 数字人 CEO 视频内通·高频常规更新（危机/重大变革须真人）〔二手〕
- 高管 Q&A 难问题/敌意问题·四步应答（acknowledge→substance→constraints→next）〔二手〕
- 高管全员会 临场气场·肢体语言（占空间+眼神+能量先于内容）〔二手〕
- 全员会 频率/节奏 决策（月度理想·季度大·危机周更·Q&A≥30%）〔二手〕

### ② 领导↔员工（上下级 · supervisor）— 3 卡
- RTO 返office 全员会沟通·live forum 而非邮件+先听后推+区分两类体验〔二手〕
- IPO 里程碑全员会·org meeting 当日 townhall+quiet period+只谈业务不谈发行〔二手〕
- 全员会 Q&A 准备模板·message themes+likely/sensitive questions+follow-up〔二手〕

## 六维评估
相关度 / 权威性 / 时效性 / 去重度 / 可落地 / 关系适配度 均 ≥3，全部过线。本轮初选 8 张，其中「全员会效果度量 KPI（Airmeet）」与既有 staff-meeting 卡 URL 撞重（index.json 已正确 skip），剔除以保唯一，净 +7。其余补稀缺子域：AI 数字人内通、Q&A 难问题四步应答、高管临场气场肢体语言、全员会频率节奏决策、RTO 返岗沟通、IPO 里程碑全员会、Q&A 准备模板。7 张全部为二手（方法论/案例来源），URL 经去重无重复入库。

## 一手/二手
本轮 7 张均为二手（外部方法论/案例/技术来源），无平级（peer）内容，符合「仅②③」硬约束。
'''

# ===== 1. 汇总笔记：插 r40 块到最前（# 员工大会 标题之后、首个 ## 轮次 之前）=====
s = open(SUMMARY, encoding='utf-8').read()
marker = '# 员工大会 · 知识卡汇总（2026-08-07 自动化采集）'
idx = s.index(marker) + len(marker)
head = s[:idx]
tail = s[idx:]
if '轮次 20260909-r40' not in s:
    new_s = head + '\n' + R40_BLOCK + tail
    open(SUMMARY, 'w', encoding='utf-8').write(new_s)
    print('SUMMARY: r40 block inserted')
else:
    print('SUMMARY: r40 block already present, skip')

# ===== 2. 00-索引：段头加四十轮 + 段尾插 7 行 =====
idx_txt = open(INDEX, encoding='utf-8').read()
# 2a 段头
old_hdr = '｜ 三十九轮 enrich 2026-09-08(+8)）'
new_hdr = '｜ 三十九轮 enrich 2026-09-08(+8)｜ 四十轮 enrich 2026-09-09(+7)）'
if old_hdr in idx_txt:
    idx_txt = idx_txt.replace(old_hdr, new_hdr, 1)
    print('INDEX: header updated')
else:
    print('INDEX: header pattern NOT found, skip header update')

# 2b 段尾插 7 行（在 ## 主题：Offsite 团建务虚（2026-08-07）之前）
offsec = '## 主题：Offsite 团建务虚（2026-08-07）'
if offsec in idx_txt and '四十轮 enrich 2026-09-09' not in idx_txt.split(offsec)[0][-200:]:
    rows_block = '\n'.join(ROWS) + '\n\n'
    idx_txt = idx_txt.replace(offsec, rows_block + offsec, 1)
    print('INDEX: 7 rows appended before Offsite section')
else:
    print('INDEX: Offsite section not found or rows already present, skip row append')

open(INDEX, 'w', encoding='utf-8').write(idx_txt)

# ===== 3. runs 笔记 =====
os.makedirs(RUNS_DIR, exist_ok=True)
run_path = os.path.join(RUNS_DIR, '员工大会-2026-09-09-第四十轮-知识卡.md')
if not os.path.exists(run_path):
    open(run_path, 'w', encoding='utf-8').write(RUN_NOTE)
    print('RUN NOTE: created', run_path)
else:
    print('RUN NOTE: already exists, skip')
