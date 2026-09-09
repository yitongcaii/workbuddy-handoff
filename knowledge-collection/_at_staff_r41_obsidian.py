# -*- coding: utf-8 -*-
"""员工大会 r41 Obsidian 同步：汇总笔记插块 + 00-索引追加 10 行 + 新建 runs 笔记。
（本轮 10 张：5③高管间 + 5②上下级，全二手；初选撞重 URL 已剔除以保唯一，净 +10）"""
import os

VAULT = r'C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库'
SUMMARY = os.path.join(VAULT, '素材', 'staff-meeting', '员工大会-知识卡汇总.md')
INDEX = os.path.join(VAULT, '00-知识采集索引.md')
RUNS_DIR = os.path.join(VAULT, '素材', 'staff-meeting', 'runs')

# ---- r41 块（汇总笔记，插在最前）----
R41_BLOCK = '''## 轮次 20260910-r41（+10）

| 卡 | 适用关系 | 一手/二手 |
|---|---|---|
| 全员会 时间盒议程模板·七段结构（开场钩子→业务快照→战略聚焦→挑战坦诚→人/文化→Q&A→收尾） | 高管间 | 二手 |
| 高管演讲 Think-Feel-Do 框架（认知→情感→行动·极简PPT） | 高管间 | 二手 |
| 高管「不能全透明时」如何保信任·目的性透明（法律/战略/未定/个人四克制） | 高管间 | 二手 |
| 全员会「有目的的透明」四支柱（沟通/问责/反馈/认可·透明≠过度分享） | 高管间 | 二手 |
| 新CEO首次全员会致辞结构（背景→愿景→3焦点→直面大象→透明承诺） | 高管间 | 二手 |
| 坏消息坦诚沟通·七字段框架（fact/impact/解读/决策/owner/未知/下次更新） | 上下级 | 二手 |
| 全员会 主持人/引导师分工（head chef/sous chef/station chefs/notetaker） | 上下级 | 二手 |
| 混合全员会 remote-first 包容设计（一屏一人/聊天大使/轮转时区/录制存档） | 上下级 | 二手 |
| 全员会 会后 recap 闭环邮件（24h内·决策+负责人+日期·≤200词） | 上下级 | 二手 |
| 全员会 互动化·现场投票/词云/emoji（打破单向广播·安全感刻意造） | 上下级 | 二手 |

'''

# ---- 00-索引 10 行 ----
ROWS = [
  '| 全员会 时间盒议程模板·七段结构（开场钩子→业务快照→战略聚焦→挑战坦诚→人/文化→Q&A→收尾）（二手）（staff-meeting.html） | 5 | 二手 | ③高管间 | openskillindex：45-60min 全员会七段时间盒（开场钩子用故事/业务快照/战略聚焦/挑战坦诚/人文化/QA/收尾）+ 金字塔信息结构（核心信息→支撑点→证据故事→行动号召）；坏消息透明讲影响+修复计划不粉饰、邀共创。 |',
  '| 高管演讲 Think-Feel-Do 框架（认知→情感→行动·极简PPT）（二手）（staff-meeting.html） | 5 | 二手 | ③高管间 | MossWarner：高管全员会演讲按 Think(认知优先级)-Feel(小故事情感连接)-Do(具体挑战) 三段；PPT 极简（每页一观点/24pt+/图胜字）、走台彩排、现场互动、真诚；结尾一句 bold 或故事留余韵。 |',
  '| 高管「不能全透明时」如何保信任·目的性透明（法律/战略/未定/个人四克制）（二手）（staff-meeting.html） | 5 | 二手 | ③高管间 | The Center for Leadership Excellence：目的性透明——透明≠和盘托出；四类须克制（法律保密/战略保护/未定决策/保护个人）；不能说时解释约束原因而非沉默、讲清决策机制与补信息时点、明确方向不变的事；总透明反制造恐惧/泄露战略/法律风险。 |',
  '| 全员会「有目的的透明」四支柱（沟通/问责/反馈/认可·透明≠过度分享）（二手）（staff-meeting.html） | 5 | 二手 | ③高管间 | Predictive Index：透明四支柱=沟通(all-hands节奏+决策日志)/问责(战略转向挂 visible owner)/反馈(匿名pulse真实闭环)/认可(表彰解释难决策的管理者)；透明≠过度分享，保护个人HR/未决法律风险/个人薪酬，边界由相关性定；Gen Z 85% 视透明为基线。 |',
  '| 新CEO首次全员会致辞结构（背景→愿景→3焦点→直面大象→透明承诺）（二手）（staff-meeting.html） | 5 | 二手 | ③高管间 | Speeches HQ：新CEO首秀五段——背景致谢降防御+一句野心愿景+3聚焦领域各给具体动作+主动点掉传闻中的裁员并承诺月度town hall/开门政策+强调每人关键共启新章；以透明开放沟通为领导标志贯穿。 |',
  '| 坏消息坦诚沟通·七字段框架（fact/impact/解读/决策/owner/未知/下次更新）（二手）（staff-meeting.html） | 5 | 二手 | ②上下级 | Antoine Buteau：全员会坏消息七字段框架（fact/impact/当下判断/已定决策/owner/还不知什么/下次更新）；事实与解读分层、plain language 别用euphemism、明确保密边界、CEO点明文化标准；假确定比诚实命名不确定更伤信任。 |',
  '| 全员会 主持人/引导师分工（head chef/sous chef/station chefs/notetaker）（二手）（staff-meeting.html） | 4 | 二手 | ②上下级 | Digital.gov：大型全员会「厨房团队」——主持人(引入/转场/看钟/鼓励参与/应意外)+副主持(回问题/报故障)+station chef(管聊天框)+notetaker(会后summary)；会前practice run；每段写清目标时段、砍掉历来如此的环节；高管更新短且拆多段。 |',
  '| 混合全员会 remote-first 包容设计（一屏一人/聊天大使/轮转时区/录制存档）（二手）（staff-meeting.html） | 4 | 二手 | ②上下级 | Innovative Human Capital：混合全员会 remote-first——在场也每人一屏接入、指派chat/Q&A主持人点名远程、跨时区轮转会议时间、每场录制存档、建沟通规范+facilitator培训+标准模板；案例Anthropic全远程固定议程文档化+对镜头讲+同步聊天频道。 |',
  '| 全员会 会后 recap 闭环邮件（24h内·决策+负责人+日期·≤200词）（二手）（staff-meeting.html） | 5 | 二手 | ②上下级 | RecordMeeting：全员会 recap 24h内(高利害当日)发；结构=一句话头条+已宣布决策+行动项(负责人+任务+日期)+下次会议；纯信息同步会砍行动表聚焦宣布了什么；≤200词、主动语态点名owner、一封发全体保记录一致；recap是会议延伸。 |',
  '| 全员会 互动化·现场投票/词云/emoji（打破单向广播·安全感刻意造）（二手）（staff-meeting.html） | 4 | 二手 | ②上下级 | StreamAlive：全员会改单向广播为双向——会前2周收+置顶投票问题、开场quick poll破冰、每10-15分钟换形式、实时字幕翻译保包容、moderator均衡线上线下(>250人必设)、匿名Q&A浮热门、会后发录制+Q&A摘要到hub；74%员工匿名才敢说，安全感须刻意造。 |',
]

# ---- runs 笔记 ----
RUN_NOTE = '''---
title: 员工大会-2026-09-10-第四十一轮-知识卡
type: 自动化采集
date: 2026-09-10
tags: [知识采集, 员工大会, 第四十一轮]
relation: [supervisor, exec]
---

# 员工大会 · 第四十一轮补采（2026-09-10，+10）

> 本轮独立页（GitHub Pages）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/runs/staff-meeting-2026-09-10-r41.html
> 本地路径：C:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection/staff-meeting/runs/staff-meeting-2026-09-10-r41.html
> 累计总索引墙：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/staff-meeting.html

## 本轮新增 10 卡（关系分层）

### ③ 领导↔领导（高管间 · exec）— 5 卡
- 全员会 时间盒议程模板·七段结构（开场钩子→业务快照→战略聚焦→挑战坦诚→人/文化→Q&A→收尾）〔二手〕
- 高管演讲 Think-Feel-Do 框架（认知→情感→行动·极简PPT）〔二手〕
- 高管「不能全透明时」如何保信任·目的性透明（法律/战略/未定/个人四克制）〔二手〕
- 全员会「有目的的透明」四支柱（沟通/问责/反馈/认可·透明≠过度分享）〔二手〕
- 新CEO首次全员会致辞结构（背景→愿景→3焦点→直面大象→透明承诺）〔二手〕

### ② 领导↔员工（上下级 · supervisor）— 5 卡
- 坏消息坦诚沟通·七字段框架（fact/impact/解读/决策/owner/未知/下次更新）〔二手〕
- 全员会 主持人/引导师分工（head chef/sous chef/station chefs/notetaker）〔二手〕
- 混合全员会 remote-first 包容设计（一屏一人/聊天大使/轮转时区/录制存档）〔二手〕
- 全员会 会后 recap 闭环邮件（24h内·决策+负责人+日期·≤200词）〔二手〕
- 全员会 互动化·现场投票/词云/emoji（打破单向广播·安全感刻意造）〔二手〕

## 六维评估
相关度 / 权威性 / 时效性 / 去重度 / 可落地 / 关系适配度 均 ≥4，全部过线。本轮初选多张与既有 staff-meeting 卡 URL 撞重（poweredby 裁员决策、gable.to 混合指南、pulserevops 新CEO/全员会演讲、ivolver 等共 4+ 张），已剔除以保唯一；换入 openskillindex 七段时间盒、MossWarner Think-Feel-Do、Cleindy 目的性透明、Predictive Index 透明四支柱、SpeechesHQ 新CEO首秀、AntoineButeau 坏消息七字段、Digital.gov 厨房团队分工、Innovative Human Capital remote-first、RecordMeeting recap 邮件、StreamAlive 互动化等 10 张稀缺子域卡。

## 一手/二手
本轮 10 张均为二手（外部方法论/案例来源），无平级（peer）内容，符合「仅②③」硬约束。
'''

# ===== 1. 汇总笔记：插 r41 块到最前（# 员工大会 标题之后、首个 ## 轮次 之前）=====
s = open(SUMMARY, encoding='utf-8').read()
marker = '# 员工大会 · 知识卡汇总（2026-08-07 自动化采集）'
idx = s.index(marker) + len(marker)
head = s[:idx]
tail = s[idx:]
if '轮次 20260910-r41' not in s:
    new_s = head + '\n' + R41_BLOCK + tail
    open(SUMMARY, 'w', encoding='utf-8').write(new_s)
    print('SUMMARY: r41 block inserted')
else:
    print('SUMMARY: r41 block already present, skip')

# ===== 2. 00-索引：段头加四十一轮 + 段尾插 10 行 =====
idx_txt = open(INDEX, encoding='utf-8').read()
# 2a 段头
old_hdr = '｜ 四十轮 enrich 2026-09-09(+7)）'
new_hdr = '｜ 四十轮 enrich 2026-09-09(+7)｜ 四十一轮 enrich 2026-09-10(+10)）'
if old_hdr in idx_txt:
    idx_txt = idx_txt.replace(old_hdr, new_hdr, 1)
    print('INDEX: header updated')
else:
    print('INDEX: header pattern NOT found, skip header update')

# 2b 段尾插 10 行（在 ## 主题：Offsite 团建务虚（2026-08-07）之前）
offsec = '## 主题：Offsite 团建务虚（2026-08-07）'
if offsec in idx_txt and '四十一轮 enrich 2026-09-10' not in idx_txt.split(offsec)[0][-200:]:
    rows_block = '\n'.join(ROWS) + '\n\n'
    idx_txt = idx_txt.replace(offsec, rows_block + offsec, 1)
    print('INDEX: 10 rows appended before Offsite section')
else:
    print('INDEX: Offsite section not found or rows already present, skip row append')

open(INDEX, 'w', encoding='utf-8').write(idx_txt)

# ===== 3. runs 笔记 =====
os.makedirs(RUNS_DIR, exist_ok=True)
run_path = os.path.join(RUNS_DIR, '员工大会-2026-09-10-第四十一轮-知识卡.md')
if not os.path.exists(run_path):
    open(run_path, 'w', encoding='utf-8').write(RUN_NOTE)
    print('RUN NOTE: created', run_path)
else:
    print('RUN NOTE: already exists, skip')
