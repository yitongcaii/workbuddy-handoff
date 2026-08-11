# -*- coding: utf-8 -*-
import json, re, os
BASE = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(BASE, 'index.json')
d = json.load(open(P, encoding='utf-8'))

def norm(t):
    t = t.lower()
    t = re.sub(r'[^一-鿿a-z0-9]', '', t)
    return t

new = [
 ("Centering the C-Suite · 5 活动筑牢高管团队信任与对齐","http://www.choosetheperk.com/blog/executive-leadership-team-meeting-ideas","exec",
  "为 ELT/高管静修设计的 5 个活动：两个反思问题、ELT 读书会(信任)、Leadership Origin Story、Pre-experience success、价值观卡牌；用价值观反思与叙事把 C-suite 围绕使命/战略对齐，非游戏。"),
 ("Executive Retreat Activities That Actually Drive Alignment","https://www.dmpcreative.llc/resources/executive-retreat-activities-that-drive-alignment","exec",
  "高管静修活动按对齐产出分三类：信任(Leadership Journey Maps/Formative Experiences Dialogue/Strengths&Blindspots/Values Auction)、战略(Strategy Mapping/客户旅程/资源分配/Pre-Mortem/竞品推演)、沟通(Decision Autopsy)；跳过信任摔与密室逃脱。"),
 ("Building a Healthy & Aligned Executive Team · 一日工作坊议程","https://theorg.com/iterate/building-a-healthy-and-aligned-executive-team-in-one-day","exec",
  "基于 Lencioni 五 dysfunction 的一日高管工作坊议程：Personal History/MBTI review/Personal Plan/Conflict profiling/Commitment clarity/Accountability；脆弱从顶层开始。"),
 ("高管信任升级与协同突围 · 阿里裸心会工作坊","http://www.youjiangshi.com/training/385487.html","exec",
  "面向高管融合/信任危机/战略转型工作坊：生命年轮(情感共鸣)+乔哈里窗(盲区)+阿里裸心会铁律(不评判/不打断/不记录)；从矛盾收集到公约签署；HRD/HRBP 全程参与。"),
 ("Leadership Team Building That Actually Works · 7 个无游戏练习","https://www.unicornlabs.ca/blog/leadership-team-building-that-works","exec",
  "7 个不靠绳索场的领导力团建练习(铁律:永远 debrief)：How to Work With Me 手册/Failure Résumé/Personal Histories/Pasta Tower/Mining for Conflict/Clearing Round/Pre-Mortem；脆弱循环+建设性冲突替代信任摔。"),
 ("Skip-Level Meeting Questions · 30 个建信任提问","https://gowindmill.com/resources/lists/skip-level-meeting-questions","supervisor",
  "高管与隔两级下属 1:1 的 30 个 skip-level 提问，六类组织；绕过管理层收集团队健康/经理效能/文化反馈；从非威胁性优先级问题建 rapport 再进敏感话题。"),
 ("The Skip-Level Meeting Playbook · 工程负责人实操手册","https://www.questworks.io/blog/skip-level-meeting-playbook","supervisor",
  "面向工程负责人的 skip-level 实操手册：心理安全感/经理效能/战略对齐/跟进协议四组；HBR 原则高管只说 30%；5 大失败模式；24h 致谢+1 周聚合主题+2 周与中层 debrief。"),
 ("Skip-Level Questionnaire · 8 套模板（含心理安全感量表）","https://www.hypescribe.com/blog/skip-level-meeting-questionnaire","supervisor",
  "8 套 skip-level 问卷模板：价值观型/心理安全感 Skip-Level 量表/360 模型/同伴文化与包容/职业成长/公司对齐；弱信任时先日常工作问题，必有升级规则。"),
 ("跨部门协作 5 策略 · 打破谷仓效应","https://pilotrunapp.com/blog/cross-department-collaboration","supervisor",
  "5 个打破部门 silo 策略：角色互换工作坊(影子日+迷你挑战)/一起解真实公司问题(破冰→定义→发想→提案→认领执行)/经营弱连接(随机午餐/技能交换/微型专案)；持续小动作胜一年一次大活动。"),
 ("Align Cross-Functional Teams · 3 个实证做法","https://victuspeople.com/how-to-align-cross-functional-teams-3-proven-practices-for-multinational-teams/","supervisor",
  "跨国/跨职能团队对齐 3 法：Timeline Activity(起源故事，仿 Lencioni，经理示弱拉高心理安全)/Daily Huddles(15 分钟共享现实)/Quarterly Themes(追一个 Critical Number)；2-3 周见效。"),
 ("KPI-Driven Team Building · 把协调问题变可测实验","https://sandmerit.com/top-kpi-driven-team-building-ideas-for-your-group/","supervisor",
  "把团建当技能演练，每个活动绑 1-2 个 KPI：依赖映射工作坊/角色 mini-charter/决策规则；一词结果对齐(词云暴露分歧)/会议卫生重置；根因 drill(无指责+五 why)/模式命名。"),
]

existing_urls = {e.get('url') for e in d}
added = 0
for title, url, rel, summ in new:
    if url in existing_urls:
        print('SKIP dup:', url)
        continue
    d.append({
        "title": title,
        "normKey": norm(title),
        "url": url,
        "sourceType": "secondary",
        "relation": rel,
        "topic": "icebreaker",
        "summary": summ,
    })
    added += 1

json.dump(d, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('appended:', added, '| total:', len(d))
ib = [e for e in d if e.get('topic')=='icebreaker']
from collections import Counter
print('icebreaker total:', len(ib), '| relations:', Counter(e.get('relation') for e in ib))
