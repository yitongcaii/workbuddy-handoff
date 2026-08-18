# -*- coding: utf-8 -*-
# Obsidian 落库（员工大会 R19）：汇总笔记追加段 + 00索引追加行 + 新建独立笔记
import os

SUMMARY = r'C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\staff-meeting\员工大会-知识卡汇总.md'
IDX00   = r'C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md'
RUNS    = r'C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\staff-meeting\runs'

# (title, relation_display_summary, source_display, oneliner, relation_display_idx, summary_idx)
CARDS = [
 ("CEO真实感沟通：从「倡导」到「询问」+You Said/We Did（happeo·Nadella/Bitzer案例）", "③", "二手",
  "happeo：高管把全员会做成双向对话——每场留30分钟真实Q&A+会前匿名收问、季度8-10人listening tour、调研后发You Said/We Did、战略必答so what，真实感>官腔（Nadella/Bitzer为证）。",
  "③高管间", "happeo：CEO真实感沟通，从倡导到询问+You Said/We Did（Nadella/Bitzer案例）（二手）"),
 ("AI 全员会模板：直面岗位焦虑·再培训·诚实Q&A（businessplusai·信任在Q&A赚或失）", "②+③", "二手",
  "businessplusai：AI全员会四段——讲清为什么做AI+坦诚再培训投入+25分钟中立主持Q&A(归类/不知明说/结尾归纳)+具体承诺收尾；预设岗位/决定/衡量硬问题备诚实答案。",
  "②上下级 / ③高管间", "businessplusai：AI全员会模板，直面岗位焦虑+再培训+诚实Q&A（二手）"),
 ("全员公告写作结构（commswith.ai·All-Staff Update Format：钩子/背景/变什么/对你意味什么/时间线/下一步）", "②+③", "二手",
  "commswith.ai：全员公告骨架——主题行=结果+时间+核心宣布、开头抛最重要信息、背景3-4句、变什么3-5条、对你意味着什么按受众分段、时间线表、下一步+提问口。",
  "②上下级 / ③高管间", "commswith.ai：全员公告写作结构（All-Staff Update Format）（二手）"),
 ("CEO 亲临一线：三班倒专场+2分钟视频+「人来了」效应（wp.me/linkedin·无桌员工触达）", "③", "二手",
  "wp.me/linkedin：80%劳动力无桌，CEO按三班倒开三场town hall（含夜班）、多地点录2分钟视频、配合移动App+数字标牌+印刷品——「人来了」效应>内容，CEO亲临=战略与一线对齐最强信号。",
  "③高管间", "wp.me：CEO亲临一线，三班倒专场+2分钟视频+人来了效应（无桌员工触达）（二手）"),
 ("一线/无桌员工触达框架：经理级联+Town Hall直连+数字标牌+观看派对（forbes/firstup·80%员工无桌）", "②+③", "二手",
  "forbes/firstup：一线town hall——经理级联(toolkit+pre-shift huddle)+高管Town Hall直连顶层、重大变革CEO先宣布经理补细节、数字标牌+移动App+点播录像补位、观看派对造共同体验、会前pulse找缺口。",
  "②上下级 / ③高管间", "forbes：一线/无桌员工触达框架（经理级联+Town Hall直连+数字标牌+观看派对）（二手）"),
 ("异步全员会模板：pre-read文档把低价值内容前移·现场只留能量/认可/Q&A（betterat.work）", "②", "二手",
  "betterat.work：100人开会极贵，能异步全异步——领导者提前填使命/目标/KR进度常驻文档+CEO更新等，会前读；现场只做欢迎/CEO更新(讲文档外)/公告/新人/Q&A/跨团队social。",
  "②上下级", "betterat.work：异步全员会模板，pre-read文档把低价值内容前移（二手）"),
 ("员工该问领导的25问框架（openculturebot·按战略/财务/产品/文化/人才分组+不问得像炫技）", "②", "二手",
  "openculturebot：给员工25问清单（战略/财务/产品/文化/人才5组）+提问纪律（用分享背后思考替为什么、为全场问、开放题、避四害）；常问战略问题者感被听见高2.4倍。",
  "②上下级", "openculturebot：员工该问领导的25问框架（按主题分组+提问纪律）（二手）"),
 ("线上Town Hall主持与彩排：排练人非仅技术·给提问真实位置·24h内发纪要（india.aonmeetings）", "②", "二手",
  "india.aonmeetings：线上全员会——无障碍从一开始(字幕+可读slide)、排练人非仅技术、给提问真实位置(归类再答/诚实说明答法)、当天冷静节奏、工作日内发录像+决策摘要+待办owner。",
  "②上下级", "india.aonmeetings：线上Town Hall主持与彩排（排练人+提问真实位置+24h纪要）（二手）"),
 ("7个能拿到承诺的CEO提问（icvdm·要指标/owner/时间线·非泛泛而谈+制作视角run-of-show）", "②", "二手",
  "icvdm：7个逼出承诺的提问（要盯的指标/节奏+owner/缺口+第一步/项目名预算/可写目标的结果/资源影响/可对齐行为）+制作视角(AV彩排/备份/机位/承诺先批/Q&A文档化)。",
  "②上下级", "icvdm：7个能拿到承诺的CEO提问（要指标/owner/时间线+制作视角）（二手）"),
 ("会议认可系统化：固定议程段live shout-out+同侪提名模板+跨部门可见（verifyed·持续可预测>偶发）", "②", "二手",
  "verifyed：认可做进常驻议程——固定Today's Recognitions段+同侪提名模板(被提名人/行为/影响/价值观+审批)、跨部门可见建跨职能欣赏、多通道适配性格、一致性最关键。",
  "②上下级", "verifyed：会议认可系统化（固定议程段+同侪提名模板+跨部门可见）（二手）"),
]

# ---------- 1) 汇总笔记：追加 R19 段 + 计数对齐 ----------
s = open(SUMMARY, encoding='utf-8').read()
sec = "\n## 轮次 20260818（十九轮补采 +10）\n\n| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n"
for t, rd, sd, _, _, _ in CARDS:
    sec += "| %s | %s | %s |\n" % (t, rd, sd)
anchor = "## 适用与备注"
assert anchor in s, "summary note missing anchor"
s = s.replace(anchor, sec + "\n" + anchor, 1)
s = s.replace("全量 188 张见卡片墙 HTML", "全量 198 张见卡片墙 HTML", 1)
s = s.replace("（含本轮 +11）", "（含本轮 +10）", 1)
s = s.replace("③ 领导↔领导（高管间 · exec）— 60 卡", "③ 领导↔领导（高管间 · exec）— 65 卡", 1)
s = s.replace("② 领导↔员工（上下级 · supervisor）— 128 卡", "② 领导↔员工（上下级 · supervisor）— 133 卡", 1)
open(SUMMARY, 'w', encoding='utf-8').write(s)
print("summary note updated (R19 section, 188->198, subheads 65/133)")

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

# ---------- 3) 新建第十九轮独立笔记 ----------
os.makedirs(RUNS, exist_ok=True)
n3 = sum(1 for c in CARDS if '③' in c[1])
n2 = sum(1 for c in CARDS if '②' in c[1])
runnote = '''---
title: 员工大会-2026-08-18-第十九轮-知识卡
type: 自动化采集
date: 2026-08-18
tags: [知识采集, 员工大会, 十九轮]
relation: [supervisor, exec]
---

# 员工大会 · 第十九轮补采知识卡（2026-08-18，+10）

> 本轮独立页（GitHub Pages）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/runs/staff-meeting-2026-08-18-r19.html
> 本地路径：`knowledge-collection/staff-meeting/runs/staff-meeting-2026-08-18-r19.html`
> 累计总索引（卡片墙）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/staff-meeting.html

## 本轮 10 张卡（③高管间 5 / ②上下级 5，按受众关系分层，剔除①平级/朋友向）

| 卡 | 适用关系 | 一手/二手 | 一句话定位 |
|---|---|---|---|
'''
for t, rd, sd, ol, _, _ in CARDS:
    runnote += "| %s | %s | %s | %s |\n" % (t, rd, sd, ol)
runnote += '''
## 本轮侧重
- ③ 高管间：补齐「真实感沟通」与「一线/无桌员工触达」两块高管实践——happeo 把全员会做成双向对话（倡导→询问、You Said/We Did、Nadella/Bitzer 真实案例）+ wp.me/linkedin CEO 亲临一线（三班倒专场+2分钟视频+「人来了」效应）+ forbes/firstup 一线触达框架（经理级联+高管Town Hall直连+数字标牌+观看派对）；另含 AI 全员会模板（businessplusai 直面岗位焦虑+再培训+诚实Q&A）、全员公告写作结构（commswith.ai 钩子/背景/变什么/对你意味什么/时间线/下一步）。
- ② 上下级：会议工程化补强——异步全员会模板（betterat.work pre-read 把低价值内容前移、现场只留能量/认可/Q&A）、员工提问力（openculturebot 25问框架+提问纪律、icvdm 7个拿承诺提问+run-of-show）、线上主持与彩排（india.aonmeetings 排练人非仅技术+提问真实位置+24h纪要）、会议认可系统化（verifyed 固定议程段+同侪提名模板+跨部门可见）。
- 硬约束已落实：剔除①平级/朋友向、家庭日/家属开放日、投资者/资本市场/IR 域；relation 仅 supervisor/exec；本轮全为二手权威源（外部方法论/媒体案例/工具官方），一手源稀缺。
'''
path = os.path.join(RUNS, '员工大会-2026-08-18-第十九轮-知识卡.md')
open(path, 'w', encoding='utf-8').write(runnote)
print("round note created:", path, "| n3=%d n2=%d" % (n3, n2))
