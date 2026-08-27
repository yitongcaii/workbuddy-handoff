# -*- coding: utf-8 -*-
"""Obsidian 三处落库：汇总笔记(append) / 00-索引(append 15行) / 本轮独立笔记(new)。"""
VAULT = 'C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库'
WALL_URL = 'https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/staff-meeting.html'
RUN_URL = 'https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/runs/staff-meeting-2026-08-27-r28.html'
RUN_HREF = '（[staff-meeting.html](%s)）' % WALL_URL

# (title, rel, score, source, index_summary, run_loc)
CARDS = [
 ('CEO 在不确定时期的全员会该说什么·致辞内容范式','③高管间',4,'二手',
  '不确定时期 CEO 全员会致辞：坦诚优先于粉饰，先承认现实再给可执行下一步与承诺，用具体故事替代口号。',
  '③ 高管（chartwellspeakers 二手）；不确定时期 CEO 致辞——先承认现实再给可执行下一步，坦诚优先于粉饰。'),
 ('用全员会（Town Hall）加固团队信任·CEO 信任杠杆','③高管间',4,'二手',
  '把 town hall 当信任账户：CEO 现身+真 Q&A+48h 内公开未答，连续兑现累积信任，读稿早退一次透支。',
  '③ 高管（jennyreilly 二手）；town hall 信任账户——CEO 亲答+48h 公开未答，连续兑现累积信任。'),
 ('办一场真正"连得起来"的全员会·高管主持心法','③高管间',4,'二手',
  '高管主持从播报转向连接：开放问题暖场+故事对话+一线案例+亲答尖锐题，承认盲点拉近距离。',
  '③ 高管（zohocloud 二手）；高管主持从播报转连接——开放问题暖场+一线案例+亲答尖锐题。'),
 ('远程环境下高管 Town Hall 沟通最佳实践','③高管间',4,'二手',
  '远程全员会三提前一公平全闭环：议程材料提前 24h、异地现场同权提问、纪要+未答覆盖所有时区。',
  '③ 跨国高管/全球 HR（therepuationagency 二手）；远程全员会三提前一公平全闭环，异步信息公平。'),
 ('把 CEO 沟通变成真实员工参与·多位高管教练的范式转向','③高管间',5,'二手',
  'Forbes 教练共识：从播报转共创，每场一问+7 天闭环+个人化表达，把推送重构为双向意义共建。',
  '③ 高管/HR 负责人（Forbes Coaches Council 二手）；CEO 沟通从播报转共创——每场一问+7 天闭环。'),
 ('直播全员会·现场 Live Q&A 平滑运行制片指南','③高管间',4,'二手',
  '直播 Q&A 制片：预征集+独立 moderator+复述问题+结构化提交投票同权，纯聊天框不适合高管场。',
  '③ 直播/混合全员会（jasperpictures 二手）；现场 Live Q&A 制片——预征集+独立 moderator+同权投票。'),
 ('下次全员会现代剧本·目标/节奏/角色/互动全设计','②上下级',5,'二手',
  '全员会现代 playbook：北极星目标先行+三角色(主持/主讲/Q&A facilitator)分工+会前造势会中互动会后延续。',
  '② HR/中层（weekblast 二手）；全员会现代剧本——目标先行+三角色分工+三段互动。'),
 ('改进全员会的 7 个实操点·透明/远程/反馈','②上下级',4,'二手',
  '改进全员会 7 点：计时员+新锐露脸+提前征集 Q&A+100% 透明+远程同权+即时 pulse+固定节奏。',
  '② HR/中层（reflektive 二手）；改进全员会 7 清单——透明、远程同权、即时反馈。'),
 ('企业全员会（Town Hall）全流程最佳实践·筹备到跟进','②上下级',5,'二手',
  'town hall 完整 SOP：筹备故事线+心理安全+会后 48h 公开所有 Q&A（含未答），把议程当故事讲。',
  '② HR/行政（communitycivicampus 二手）；town hall 全流程 SOP——筹备到跟进 48h 公开所有 Q&A。'),
 ('办一场员工"真想去"的全员会·把最关心的事放最前','②上下级',4,'二手',
  '提升出席意愿：内容优先（最关心的事放开场）+多元声音上台+会后对话空间，不做又一个强制会。',
  '② 中层/HR（kewgardens 二手）；办员工真想去的会——内容优先+多元声音+会后对话空间。'),
 ('全员会最该避开的 6 件事·主持人与会后闭环','②上下级',4,'二手',
  '全员会避坑：独立 host+开场互动+核心消息前置+15-20min Q&A+会后发 summary 补答未答。',
  '② HR/中层（mentimeter 二手）；全员会避坑 6 件——独立 host+核心前置+会后闭环。'),
 ('用实时投票+结构化 Q&A 跑通 60 分钟全员会·含样例议程','②上下级',5,'二手',
  '匿名投票戳破沉默+60min 样例议程+ranked queue Q&A+会后导出未答，把沉默大多数变可见信号。',
  '② HR/中层（pollqr 二手）；实时投票+结构化 Q&A——含可直接抄的 60min 议程与 ranked queue。'),
 ('为什么传统全员会 Q&A 失灵·匿名参与的心理学与 2-4 倍提效','②上下级',5,'二手',
  '仅 27% 问真问题；架构级匿名把参与率拉高 2-4 倍、问题更具体、基层声音获与高管同等权重。',
  '② HR/中层（hushwork 二手）；匿名 Q&A 心理学——27% 失灵率，架构级匿名提效 2-4 倍。'),
 ('职工大会互动提问环节怎么排·互动工具方实操建议','②上下级',4,'二手',
  '国内职工大会手机端互动：扫码提问+匿名+热度排序+大屏滚动+会后留痕，比举麦民主且可追溯。',
  '② 国内职工大会（淘气互动 二手）；手机端互动提问——扫码+匿名+热度排序+大屏滚动。'),
 ('全员会标准议程模板·60 分钟时间盒与分工','②上下级',4,'二手',
  '拿来即用的 60min 全员会议程时间盒与分工模板：开场→战略→团队亮点→故事→投票→Q&A→行动项。',
  '② HR/中层（monday 二手）；全员会议程模板——60min 时间盒与分工，拿来即用。'),
]

# ---------- 1. 汇总笔记 append ----------
summary_path = f'{VAULT}/素材/staff-meeting/员工大会-知识卡汇总.md'
sec = '\n## 轮次 2026-08-27（+15）\n\n| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n'
for t, rel, sc, src, idxs, loc in CARDS:
    sec += f'| {t} | {rel} | {src} |\n'
with open(summary_path, 'a', encoding='utf-8') as f:
    f.write(sec)
print('summary appended:', len(CARDS), 'rows')

# ---------- 2. 00-索引 append 15 行 ----------
idx_path = f'{VAULT}/00-知识采集索引.md'
rows = ''
for t, rel, sc, src, idxs, loc in CARDS:
    rows += f'| {t}{RUN_HREF} | {sc} | {src} | {rel} | {idxs} |\n'
with open(idx_path, 'a', encoding='utf-8') as f:
    f.write(rows)
print('index appended:', len(CARDS), 'rows')

# ---------- 3. 本轮独立笔记 new ----------
runs_path = f'{VAULT}/素材/staff-meeting/runs/员工大会-2026-08-27-第二十八轮-知识卡.md'
n_exec = sum(1 for c in CARDS if c[1]=='③高管间')
n_sup = sum(1 for c in CARDS if c[1]=='②上下级')
body = f'''---
title: 员工大会 第二十八轮知识卡
tags: [知识采集, 员工大会, 自动化采集, 轮次]
date: 2026-08-27
type: 自动化采集
---

# 员工大会 · 第二十八轮补采（2026-08-27）

- 本轮新增 **{len(CARDS)} 卡**（②上下级 {n_sup} · ③高管间 {n_exec}），0 peer（硬约束）
- 一手 0 / 二手 {len(CARDS)}（本轮源均为媒体/机构/工具方二手，公司内部官方一手源稀缺）
- 累计墙：staff-meeting.html（主集 ② 207 / ③ 103）+ 当轮独立页
- 新域：CEO 不确定期致辞 / 信任账户 / 高管主持连接 / 远程沟通 / CEO 沟通转型 / 直播 Q&A 制片 / 现代剧本 / 7 实操点 / 全流程 SOP / 真想去 / 避坑 6 件 / 实时投票议程 / 匿名心理学 / 职工大会互动 / 议程模板
- 硬排除：平级/朋友向（①）内容（用户硬约束）；安全HRBP文化知识库源（采集禁令）

## 本轮卡片

| 卡 | 质量分 | 一手/二手 | 适用关系 | 一句话定位 |
|---|---|---|---|---|
'''
for t, rel, sc, src, idxs, loc in CARDS:
    body += f'| {t}{RUN_HREF} | {sc} | {src} | {rel} | {loc} |\n'
body += f'''
## 链接
- 累计卡片墙：{WALL_URL}
- 当轮独立页：{RUN_URL}
- 主题汇总笔记：[[知识采集库/素材/staff-meeting/员工大会-知识卡汇总|员工大会-知识卡汇总]]
'''
with open(runs_path, 'w', encoding='utf-8') as f:
    f.write(body)
print('runs note written:', runs_path)
