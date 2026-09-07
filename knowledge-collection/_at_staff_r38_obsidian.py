# -*- coding: utf-8 -*-
"""员工大会 r38 Obsidian 同步：汇总笔记插块 + 00-索引追加 8 行 + 新建 runs 笔记。"""
import os

VAULT = r'C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库'
SUMMARY = os.path.join(VAULT, '素材', 'staff-meeting', '员工大会-知识卡汇总.md')
INDEX = os.path.join(VAULT, '00-知识采集索引.md')
RUNS_DIR = os.path.join(VAULT, '素材', 'staff-meeting', 'runs')

# ---- r38 块（汇总笔记，倒序插在最前）----
R38_BLOCK = '''## 轮次 20260908-r38（+8）

| 卡 | 适用关系 | 一手/二手 |
|---|---|---|
| 高管 AI 数字分身出席内部会议·替代领导参与常规同步 | 高管间 | 二手 |
| 股权激励启动会·创始人讲 Why+HR 讲规则+坦诚 Q&A+授予仪式 | 高管间 | 一手 |
| Purpose 渗透全员会·组织目的叙事+叠加个人目的 | 高管间 | 二手 |
| 用全员会驱动 CSR 内部倡导·高管以身作则+月度 Impact Chats | 高管间 | 二手 |
| 多语全员会引导技巧·提前定语言+术语库+80%语速+转录锚点 | 上下级 | 二手 |
| 全员会实时翻译·两种模式不打断对话流 | 上下级 | 二手 |
| 全息 3D 远程在场·Google Beam 缩混合办公包容鸿沟 | 上下级 | 二手 |
| ESG 主题内部大会·ESG 评估+影响度量+数据说话 | 上下级 | 二手 |

'''

# ---- 00-索引 8 行 ----
ROWS = [
  '| 高管 AI 数字分身出席内部会议·替代领导参与常规同步（二手）（staff-meeting.html） | 5 | 二手 | ③高管间 | Meta 据 FT 开发 CEO 实时 3D 写实 AI 分身，可代表本人出席部分内部会议、答常规问题；治理红线=透明标注+对话留痕+人工升级通道。 |',
  '| 股权激励启动会·创始人讲 Why+HR 讲规则+坦诚 Q&A+授予仪式（一手）（staff-meeting.html） | 5 | 一手 | ③高管间 | 笛杨咨询原创：启动会四段=创始人亲讲 Why/HR 大白话+案例演算讲规则/创始人坦诚答战略 Q&A/CEO 亲手发授予通知书仪式。 |',
  '| Purpose 渗透全员会·组织目的叙事+叠加个人目的（二手）（staff-meeting.html） | 4 | 二手 | ③高管间 | CrossFields 2026：别发金字塔图，改讲公司过去-现在-未来单一故事让员工共情，再给员工渠道叠加个人 My-Purpose。 |',
  '| 用全员会驱动 CSR 内部倡导·高管以身作则+月度 Impact Chats（二手）（staff-meeting.html） | 4 | 二手 | ③高管间 | CSR Connect：领导以身作则+CEO 开月度 Impact Chats 收点子+spotlight 表彰，远程用 Slack 频道+虚拟 town hall 轮值主持。 |',
  '| 多语全员会引导技巧·提前定语言+术语库+80%语速+转录锚点（二手）（staff-meeting.html） | 5 | 二手 | ②上下级 | LecSync：会前 48h 发多语议程+上传术语表；会中讲者降速 80%、关键点停顿、实时转录投屏当锚点、鼓励任意语言贡献。 |',
  '| 全员会实时翻译·两种模式不打断对话流（二手）（staff-meeting.html） | 5 | 二手 | ②上下级 | OLVA：两模式=被动 participant-side(不打断不塞 bot)/共享 meeting-level(字幕流全员同视)；四原则=节奏不被打断/理解>逐字/可控/同意隐私。 |',
  '| 全息 3D 远程在场·Google Beam 缩混合办公包容鸿沟（二手）（staff-meeting.html） | 4 | 二手 | ②上下级 | UC Today：Google Beam 用 65 寸光场屏+6 摄像头让远端以真人尺寸入会、空间音频定位发言，较网格视频社会连接+50%、贡献感+21%。 |',
  '| ESG 主题内部大会·ESG 评估+影响度量+数据说话（二手）（staff-meeting.html） | 4 | 二手 | ②上下级 | First Event 2026：聚曼城 Etihad 球场融合战略/可持续/engagement；会前 ESG 评估、Impact Report 度量；会后目标理解+51%、100% 签 ESG Charter。 |',
]

# ---- runs 笔记 ----
RUN_NOTE = '''---
title: 员工大会-2026-09-08-第三十八轮-知识卡
type: 自动化采集
date: 2026-09-08
tags: [知识采集, 员工大会, 第三十八轮]
relation: [supervisor, exec]
---

# 员工大会 · 第三十八轮补采（2026-09-08，+8）

> 本轮独立页（GitHub Pages）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/runs/staff-meeting-2026-09-08-r38.html
> 本地路径：C:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection/staff-meeting/runs/staff-meeting-2026-09-08-r38.html
> 累计总索引墙：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/staff-meeting.html

## 本轮新增 8 卡（关系分层）

### ③ 领导↔领导（高管间 · exec）— 4 卡
- 高管 AI 数字分身出席内部会议·替代领导参与常规同步〔二手〕
- 股权激励启动会·创始人讲 Why+HR 讲规则+坦诚 Q&A+授予仪式〔一手〕
- Purpose 渗透全员会·组织目的叙事+叠加个人目的〔二手〕
- 用全员会驱动 CSR 内部倡导·高管以身作则+月度 Impact Chats〔二手〕

### ② 领导↔员工（上下级 · supervisor）— 4 卡
- 多语全员会引导技巧·提前定语言+术语库+80%语速+转录锚点〔二手〕
- 全员会实时翻译·两种模式不打断对话流〔二手〕
- 全息 3D 远程在场·Google Beam 缩混合办公包容鸿沟〔二手〕
- ESG 主题内部大会·ESG 评估+影响度量+数据说话〔二手〕

## 六维评估
相关度 / 权威性 / 时效性 / 去重度 / 可落地 / 关系适配度 均 ≥3，全部过线。本次为饱和主题补稀缺子域：高管 AI 数字分身治理、股权激励启动会四段式、Purpose 渗透叙事、CSR 内部倡导、多语会议引导、实时翻译两模式、全息 3D 远程在场、ESG 主题内部大会度量。

## 一手/二手
本轮 8 张中 1 张一手（股权激励启动会·笛杨原创实务）、7 张二手（方法论/技术/案例来源），无重复 URL 入库。
'''

# ===== 1. 汇总笔记：插 r38 块到最前（# 员工大会 标题之后、首个 ## 轮次 之前）=====
s = open(SUMMARY, encoding='utf-8').read()
marker = '# 员工大会 · 知识卡汇总（2026-08-07 自动化采集）'
idx = s.index(marker) + len(marker)
# 插在标题行之后、下一行之前
head = s[:idx]
tail = s[idx:]
if '轮次 20260908-r38' not in s:
    new_s = head + '\n' + R38_BLOCK + tail
    open(SUMMARY, 'w', encoding='utf-8').write(new_s)
    print('SUMMARY: r38 block inserted')
else:
    print('SUMMARY: r38 block already present, skip')

# ===== 2. 00-索引：段头加三十八轮 + 段尾插 8 行 =====
idx_txt = open(INDEX, encoding='utf-8').read()
# 2a 段头
old_hdr = '｜ 三十七轮 enrich 2026-09-07(+8)）'
new_hdr = '｜ 三十七轮 enrich 2026-09-07(+8)｜ 三十八轮 enrich 2026-09-08(+8)）'
if old_hdr in idx_txt:
    idx_txt = idx_txt.replace(old_hdr, new_hdr, 1)
    print('INDEX: header updated')
else:
    print('INDEX: header pattern NOT found, skip header update')

# 2b 段尾插 8 行（在 ## 主题：Offsite 之前）
offsec = '## 主题：Offsite 团建务虚（2026-08-07）'
if offsec in idx_txt and '三十八轮 enrich 2026-09-08' not in idx_txt.split(offsec)[0][-200:]:
    rows_block = '\n'.join(ROWS) + '\n\n'
    idx_txt = idx_txt.replace(offsec, rows_block + offsec, 1)
    print('INDEX: 8 rows appended before Offsite section')
else:
    print('INDEX: Offsite section not found or rows already present, skip row append')

open(INDEX, 'w', encoding='utf-8').write(idx_txt)

# ===== 3. runs 笔记 =====
os.makedirs(RUNS_DIR, exist_ok=True)
run_path = os.path.join(RUNS_DIR, '员工大会-2026-09-08-第三十八轮-知识卡.md')
if not os.path.exists(run_path):
    open(run_path, 'w', encoding='utf-8').write(RUN_NOTE)
    print('RUN NOTE: created', run_path)
else:
    print('RUN NOTE: already exists, skip')
