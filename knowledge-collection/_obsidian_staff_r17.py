# -*- coding: utf-8 -*-
# Obsidian 落库（员工大会 R17）：汇总笔记追加段 + 00索引追加行 + 新建独立笔记
import os

SUMMARY = r'C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\staff-meeting\员工大会-知识卡汇总.md'
IDX00   = r'C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md'
RUNS    = r'C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\staff-meeting\runs'

# (title, relation_display_summary, source_display, oneliner, relation_display_idx, summary_idx)
CARDS = [
 ("中国建材集团2026年中工作会（官方·董事长讲话+深化改革动员）", "②+③", "一手",
  "中国建材7/30-31泰安年中工作会暨深化改革动员：董事长讲话定调+总经理报告拆解，五方面部署（战略引领/价值创造/创新/改革/党建）+拼闯干动员，央企战略部署一手。",
  "②上下级 / ③高管间", "中国建材集团官网：2026年中工作会暨深化改革动员，董事长讲话定调+总经理报告拆解，五方面部署+拼闯干动员（一手）"),
 ("华能集团2026年年中工作会（董事长讲话·雄安新区·权威媒体报道）", "②+③", "二手",
  "华能7/23-24雄安年中工作会：董事长讲话+六个进一步部署，双过半+A级考核提振信心，高管↔全员战略沟通纪实。",
  "②上下级 / ③高管间", "澎湃新闻：华能2026年中工作会雄安新区召开，董事长讲话+六个进一步部署，双过半+A级考核（权威媒体）"),
 ("中远海运集团2026年工作会议（官方·二届五次职代会·十五五蓝图）", "②+③", "一手",
  "中远海运1/26沪上2026工作会+二届五次职代会：十五五五方面部署（产业体系/AI+/全球通道/改革/安全）+三个作用排头兵，一把手年度战略部署一手。",
  "②上下级 / ③高管间", "中远海运官网：2026工作会+二届五次职代会，十五五五方面部署（AI+/全球通道）+三个作用排头兵（一手）"),
 ("中汽中心党委扩大会暨2026中期工作会（官方·视频分会场+工作回顾片）", "②+③", "一手",
  "中汽中心7/27津中期工作会：现场+视频分会场近500人+回顾片暖场，对标七个深刻学习领会+实字当头干字为先，tech/format范式一手。",
  "②上下级 / ③高管间", "中汽中心官网：中期工作会现场+视频分会场近500人+回顾片暖场，对标七个深刻学习领会（一手）"),
 ("企业Town Hall最佳实践（climbtheladder·议程/主持/坦诚/跟进）", "②+③", "二手",
  "climbtheladder 全员会执行框架：会前限时议程+技术彩排、moderator控场、share the stage、会后摘要含未答问题；避四类失灵。",
  "②上下级 / ③高管间", "climbtheladder：全员会执行框架，会前议程+技术彩排、moderator控场、share the stage、会后摘要含未答问题（二手）"),
 ("Town Hall会议全指南（议题库+Q&A主持+最佳实践·thedetroitbureau）", "②上下级", "二手",
  "thedetroitbureau 全员会全指南：议题五类+Q&A成败关键（moderator控流/共情诚实/问答摘要）+互动含字幕+会后反馈。",
  "②上下级", "thedetroitbureau：全员会议题五类+Q&A成败关键（moderator控流/共情诚实/问答摘要）+互动含字幕（二手）"),
 ("如何办好全员会（granola·异步纪要+限时+远程激活+问责）", "②上下级", "二手",
  "granola 全员会运营：会后24h recap（决策+行动项owner/deadline+未答Q&A）、死保Q&A时间块、开场问责、远程激活。",
  "②上下级", "granola：全员会运营，会后24h recap（决策+行动项owner/deadline+未答Q&A）、死保Q&A、开场问责、远程激活（二手）"),
 ("全员会最佳实践2026（teamflect·混合包容+议程+认可）", "②上下级", "二手",
  "teamflect 混合全员会Remote-First三招（齐眼平线/先答远程/同步投票）+议程菜单+月度季度节奏。",
  "②上下级", "teamflect：混合全员会Remote-First三招（齐眼平线/先答远程/同步投票）+议程菜单+节奏（二手）"),
 ("混合团队全员会2026指南（gable·5大失误+5种原型+议程模板）", "②+③", "二手",
  "gable 混合全员会5大失误+5种原型（对齐/表彰/透明Q&A/战略转型/复盘）+60/30min模板，重大变革沟通与混合执行双覆盖。",
  "②上下级 / ③高管间", "gable：混合全员会5大失误+5种原型（对齐/表彰/透明Q&A/战略转型/复盘）+60/30min模板（二手）"),
 ("高管炉边谈话（Fireside Chat）怎么跑（haystack·信任连接范式）", "③高管间", "二手",
  "haystack 高管炉边谈话：moderator一对一引导替代宣讲，town hall做对齐透明+fireside做信任连接双轨并用。",
  "③高管间", "haystack：高管炉边谈话moderator一对一引导替代宣讲，town hall对齐透明+fireside信任连接双轨（二手）"),
]

# ---------- 1) 汇总笔记：追加 R17 段 + 改 167→177 ----------
s = open(SUMMARY, encoding='utf-8').read()
sec = "\n## 轮次 20260816（十七轮补采 +10）\n\n| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n"
for t, rd, sd, _, _, _ in CARDS:
    sec += "| %s | %s | %s |\n" % (t, rd, sd)
anchor = "## 适用与备注"
assert anchor in s, "summary note missing anchor"
s = s.replace(anchor, sec + "\n" + anchor, 1)
s = s.replace("全量 167 张见卡片墙 HTML", "全量 177 张见卡片墙 HTML", 1)
s = s.replace("（含本轮 +11）", "（含本轮 +10）", 1)
open(SUMMARY, 'w', encoding='utf-8').write(s)
print("summary note updated (+10 section, 167->177)")

# ---------- 2) 00 索引：在 "## 模板规范" 前追加 10 行 ----------
i0 = open(IDX00, encoding='utf-8').read()
rows = ""
for t, _, sd, _, rdisp, summ in CARDS:
    rows += "| %s（staff-meeting.html） | 4 | %s | %s | %s |\n" % (t, sd, rdisp, summ)
TEMPLATE = "## 模板规范"
assert TEMPLATE in i0, "00 index missing template anchor"
i0 = i0.replace("\n" + TEMPLATE, "\n" + rows + "\n" + TEMPLATE, 1)
open(IDX00, 'w', encoding='utf-8').write(i0)
print("00 index updated (+10 rows)")

# ---------- 3) 新建第十七轮独立笔记 ----------
os.makedirs(RUNS, exist_ok=True)
n3 = sum(1 for c in CARDS if '③' in c[1])
n2 = sum(1 for c in CARDS if '②' in c[1])
runnote = '''---
title: 员工大会-2026-08-16-第十七轮-知识卡
type: 自动化采集
date: 2026-08-16
tags: [知识采集, 员工大会, 十七轮]
relation: [supervisor, exec]
---

# 员工大会 · 第十七轮补采知识卡（2026-08-16，+10）

> 本轮独立页（GitHub Pages）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/runs/staff-meeting-2026-08-16-r17.html
> 本地路径：`knowledge-collection/staff-meeting/runs/staff-meeting-2026-08-16-r17.html`
> 累计总索引（卡片墙）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/staff-meeting.html

## 本轮 10 张卡（③高管间 5 / ②上下级 5，按受众关系分层，剔除①平级/朋友向）

| 卡 | 适用关系 | 一手/二手 | 一句话定位 |
|---|---|---|---|
'''
for t, rd, sd, ol, _, _ in CARDS:
    runnote += "| %s | %s | %s | %s |\n" % (t, rd, sd, ol)
runnote += '''
## 本轮侧重
- ③ 高管间：央企年中/年度工作会一手战略部署范式（中国建材「五方面+拼闯干」、中远海运「十五五五方面+职代会合一」、中汽中心「视频分会场+回顾片暖场」）+ 高管信任连接新载体（haystack 炉边谈话 vs town hall 双轨）。
- ② 上下级：全员会执行框架与运营体系（climbtheladder 议程/主持/坦诚/跟进、granola 异步纪要+限时+问责、teamflect 混合包容、gable 5原型+议程模板）+ 议题菜单与 Q&A 主持（thedetroitbureau）。
- 硬约束已落实：剔除①平级/朋友向、家庭日/家属开放日、投资者/资本市场/IR 域；relation 仅 supervisor/exec。
'''
path = os.path.join(RUNS, '员工大会-2026-08-16-第十七轮-知识卡.md')
open(path, 'w', encoding='utf-8').write(runnote)
print("round note created:", path, "| n3=%d n2=%d" % (n3, n2))
