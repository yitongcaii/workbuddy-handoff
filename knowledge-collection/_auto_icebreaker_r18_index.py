# -*- coding: utf-8 -*-
"""破冰 r18：把 12 张新卡写入 index.json（全局去重表）。"""
import json, os, re

BASE = os.path.dirname(os.path.abspath(__file__))
IDX = os.path.join(BASE, 'index.json')

def norm(s):
    s = s.strip().lower()
    s = re.sub(r'\s+', '', s)
    s = re.sub(r'[（）·，、/:;，。·\-–—–]', '', s)
    return s

new = [
 ("新领导同化 NLA 流程·HR/OD 引导的团队对齐",
  "https://instituteod.com/the-importance-of-new-leader-assimilation-and-how-it-works/3/",
  "secondary","exec",
  "NLA 四步：HR/OD 引导→无领导团队单独会议收真实顾虑→教练式反馈给领导→联合会对齐+共享协议；降低新领导早期失败率"),
 ("领导力入职 30-60-90 框架·听先于领导",
  "https://galleryhr.com/blogs/hr-best-practices-blog/successfully-onboarding-new-leaders-best-practices-leadership-transition",
  "secondary","exec",
  "领导入职四阶段：会前备30-60-90计划→D1-30听先于领导→D30-60定向与速赢→D60-90战略贡献；前30天只听不急着改"),
 ("高管入职 90 天·三阶段建信任不破势",
  "https://www.nextonestaffing.com/blogs/executive-onboarding-strategy/",
  "secondary","exec",
  "高管入职三阶段：听学(D1-30,建心理安全)→对齐沟通(D31-60,可见速赢印证)→领导加速(D61-90)；避第一周大改/低估非正式权力等坑"),
 ("高管退修会 2.0·五步法+团队宪章（新 CEO 百天）",
  "https://www.odgersberndtson.com/en-us/insights/executive-retreats-20-how-ceos-can-achieve-more-when-uniting-teams/",
  "secondary","exec",
  "高影响力高管退修会五步：组织目的→团队目的(宪章)→角色问责→干系人对齐→学习绩效；新CEO前100天借退修会定调，会前诊断定议程"),
 ("高管 Offsite 规划·季度节奏+决策导向",
  "https://www.metavent.io/blog/executive-offsite-planning-that-actually-drives-decisions-in-changing-times",
  "secondary","exec",
  "高管 offsite 议程锚定「必做决策」而非汇报；季度节奏(Q1定方向/Q2评估/Q3重校/Q4复盘)防对齐漂移；领导归属感/信任为隐性产出"),
 ("高管 Offsite·四类挑战+3天结构",
  "https://www.elliottrector.com/offsites",
  "secondary","exec",
  "高管 offsite 面向四类拐点挑战(对齐/高压领导/转型/凝聚力)；3天递进：重对齐→凝聚力与判断→整合承诺；会前诊断+离场后整合成效"),
 ("团队宪章 Team Charter·共创北极星（目的/角色/决策/冲突）",
  "https://www.miro.com/organizational-chart/what-is-a-team-charter/",
  "primary","supervisor",
  "Miro官方：团队宪章五要素(目标/角色/沟通/决策/冲突)；共创五步且全员签署；远程/分布式团队必做，定期回顾成活文档(一手)"),
 ("团队宪章分步指南·中立引导+绿卡/红卡行为",
  "https://growth-space.co.uk/blog/tag/Team+Charter+Template",
  "secondary","supervisor",
  "团队宪章七步：全员参与(中立引导师平衡声音)→定调→走模板(绿卡鼓励/红卡零容忍行为)→提示卡深化→清晰记录→让宪章活→约定回顾"),
 ("团队宪章 Wiki 模板·可复制的协作协议骨架",
  "https://github.com/annepetersen/teams/wiki/Team-charter-template",
  "secondary","supervisor",
  "GitHub开源宪章wiki模板：成员/工作协议/分歧处理/沟通仪式/角色/反馈；把assume good intent翻转为防权力失衡写进协议，新经理拿来即用"),
 ("跨职能团队会议·破筒仓+三 Amigos（心理安全）",
  "https://app.studyraid.com/en/read/50689/2411551/implement-cross-functional-team-meetings",
  "secondary","supervisor",
  "跨职能启动用三Amigos(开发+测试+产品)早协作破筒仓；验收标准/风险写码前定；retro含质量视角；结构化会议使生产bug降约40%"),
 ("项目 Kickoff 议程·RACI+决策日志（虚拟差异）",
  "https://alexberman.com/project-kickoff-agenda",
  "secondary","supervisor",
  "Kickoff议程含RACI；必产决策日志式文档(范围/RACI/决策/行动项)24h内发防争议；虚拟场加ground rules+co-host+实时共享+录像"),
 ("项目 Kickoff 议程·填例+可视化决策（60 分钟）",
  "https://www.laxis.com/blog/project-kickoff-meeting-agenda",
  "secondary","supervisor",
  "60分钟Kickoff十段；真实填例把out-of-scope/依赖/owner钉死；决策可视化记录+每段确认，防周三月翻案；远程共屏实时记录"),
]

d = json.load(open(IDX, encoding='utf-8'))
before = len(d)
existing_url = set()
for e in d:
    u = e.get('url','').strip().lower()
    u = re.sub(r'^https?://','',u); u = re.sub(r'^www\.','',u)
    existing_url.add(u.rstrip('/'))

added = 0
for title, url, st, rel, summ in new:
    u = url.strip().lower(); u = re.sub(r'^https?://','',u); u = re.sub(r'^www\.','',u); u = u.rstrip('/')
    if u in existing_url:
        print('  SKIP dup:', title)
        continue
    d.append({"title": title, "normKey": norm(title), "url": url, "sourceType": st, "relation": rel, "summary": summ})
    existing_url.add(u)
    added += 1

json.dump(d, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('OK index.json | before=%d after=%d added=%d' % (before, len(d), added))
