# -*- coding: utf-8 -*-
"""员工大会 r12：把 13 张新卡写入 index.json（带 URL 去重）。"""
import json, re

IDX = 'index.json'

# (title, url, relation, source, summary)
NEW = [
 ("新CEO上任·内部传播四轨作战（沟通顾问）",
  "https://www.comm-ext.com/the-rise-of-rizz-what-ceo-transitions-teach-us-about-executive-communications",
  "exec", "comm-ext",
  "沟通顾问 comm-ext 拆解新CEO上任内部传播四轨：全员Town Hall用对话式无PPT（资深主持访谈）、新领导首周all-hands可见性、前90天Listening Tour（焦点小组+脉冲调研）、四大审计（文化/战略/领导力/财务）。核心是\"先倾听后广播\"，给管理者配工具包成为主传播渠道。"),
 ("扭亏CEO首日Town Hall：透明·清晰·紧迫（PE实战）",
  "https://chiefexecutive.net/how-to-lead-through-a-turnaround",
  "exec", "chiefexecutive",
  "Chief Executive 刊载PE扭亏案例：新CEO首场全员Town Hall直面焦虑，公开大胆5年目标并用公开信讲清\"我们在哪·去哪·怎么走\"，再框定战略（ELT重聚/聚焦客户/简化运营）。动荡期员工要的是透明、清晰、紧迫三件套。"),
 ("并购后CEO·月度全员会沟通计划模板",
  "https://www.searchfundmarket.com/en/templates/100-day-plan",
  "exec", "searchfundmarket",
  "Search Fund Market 的100天模板含员工全员会（月度30分钟Town Hall）：业务更新、亮点与认可（点名到人）、在做什么、开放Q&A（无禁区）。Q&A最重要；先沟通稳定再谈战略（员工先要饭碗安全才关心愿景）。"),
 ("新领导前100天·沟通即战略（故事化）",
  "https://www.linkedin.com/pulse/your-first-100-days-everything-start-communicating-dean-foust",
  "exec", "linkedin",
  "前高管沟通顾问Dean Foust：新领导前100天\"沉默即信号\"。要点：映射利益相关方、把20%时间给员工Town Hall、用故事化讯息（Satya Nadella用儿子故事连接微软包容使命）、建思想领导力平台、展现真实谦逊脆弱。HBR：百日内首发战略讲话股价正向效应最强。"),
 ("领导更替为何失败（不是战略，是沟通）",
  "https://www.stimulus.co/insights/whyleadershiptransitionsfail",
  "exec", "stimulus",
  "Stimulus：领导更替成败常不取决于战略，而取决于能否把愿景\"讲进人心、促成行动\"。5步：发现与倾听、重塑公司叙事、建领导者品牌、规划前100天及之后、度量并校准。HBR\"为影响而投入\"是卓越CEO标志。"),
 ("CEO更替·CCO作战框架（八大原则）",
  "https://page.org/knowledge-base/a-framework-for-successful-ceo-transitions-insights-from-ceo-transitions-learning-share-out/",
  "exec", "page",
  "Page（CEO传播官网络）提炼CEO更替八大原则：弄清董事会任命使命、保护CEO时间、拉同级高管共进信息开发、Day1\"内容盛宴\"、稳定来自节奏（路上明信片）、有意放下该放的、邀同事声音、100天后复盘承诺兑现。"),
 ("全员会60分钟议程模板（出席率65%→94%案例）",
  "https://www.tinyteam.io/blog/team-meeting-agenda-template",
  "supervisor", "tinyteam",
  "Tiny Team 给出可复制全员会60分钟议程：公司更新10/部门spotlight20/员工认可10/开放Q&A15/下一步5。案例：40人电商把CEO开场从30min砍到10min、加现场Q&A与具体人认可，出席率65%→94%。"),
 ("2026全员会指南：三大产出+Q&A为王",
  "https://recordmeeting.com/blog/all-hands-meeting",
  "supervisor", "recordmeeting",
  "RecordMeeting 2026指南：有效全员会三产出——领导层直传决策/战略、以认可强化想重复行为、开放论坛建信任。议程四段、Q&A最关键。频率快变期月度、稳定期季度；会后2h内发录制+文字摘要并按日期归档。"),
 ("全员会详解：月度/季度议程模板+常见坑",
  "https://woahtech.com/all-hands-meetings-explained-agenda-templates-best-practices-and-common-mistakes",
  "supervisor", "woahtech",
  "WoahTech 详解全员会：45min月度与60min季度两套议程模板。常见坑：只报喜不报忧、slide过多、不给员工声音、不跟进。最佳实践：提前发议程、匿名提问、平衡坦诚与信心、记录归档。"),
 ("高效全员会：最佳实践与常见错误",
  "https://wpwebify.com/blog/how-to-run-an-effective-all-hands-meeting-agenda-best-practices-and-common-mistakes",
  "supervisor", "wpwebify",
  "WP Webify 总结全员会实践与雷区：每议程项服务明确目的、多speaker、数据+故事平衡、提前brief、无障碍、鼓励参与、会后跟进；雷区为太长/只报喜/slide堆积/不给声音/不跟进（承诺不兑现损信任）。"),
 ("会后情绪调研模板（测单场Town Hall）",
  "https://www.mangoapps.com/templates/surveys/post-town-hall-sentiment-survey-2",
  "supervisor", "mangoapps",
  "MangoApps 会后情绪调研模板测\"单场领导沟通事件\"而非整体敬业度——聚焦讯息清晰度、关切是否被听见、对领导方向可信度。5点Likert+开放追问，默认匿名，由HR/内部沟通/办会领导共拥并路由跟进。"),
 ("员工Town Hall议程指南+成效度量",
  "https://contacts.plenitudeconsulting.com/plenitudeconsulting-news/employee-town-hall-agenda-your-guide-1764803340",
  "supervisor", "plenitudeconsulting",
  "Plenitude Consulting 指南：办会前先定目的、慎选speaker并充分brief（含技术彩排）、Q&A预设诚实答案并跟进、议程提前发。成效度量多维：会后短调研、出席/参与率、Q&A量与锐度、领导反馈、行为变化、情绪时序追踪。"),
 ("企业主持/控场 moderator 角色拆解",
  "https://www.futuristsspeakers.com/corporate-moderator-emcee-host-facilitator",
  "supervisor", "futuristsspeakers",
  "企业 moderator 聚焦讨论质量/提问/辩论/节奏管理，把演讲变互动；适用员工Town Hall/高管论坛/公司会议。准备：研究组织与受众、建问题框架、规划过渡句。最佳实践：准备而非背稿、多听少说、问具体不泛、以takeaway收尾。"),
]

def norm(u):
    u = u.strip().lower()
    u = re.sub(r'^https?://', '', u)
    u = re.sub(r'^www\.', '', u)
    return u.rstrip('/')

d = json.load(open(IDX, encoding='utf-8'))
existing = {norm(e['url']) for e in d}
before = len(d)
added = 0
for title, url, rel, src, summ in NEW:
    if norm(url) in existing:
        print('[skip dup]', url)
        continue
    d.append({
        "title": title, "normKey": title, "url": url,
        "sourceType": "secondary", "relation": rel,
        "summary": summ, "topic": "staff-meeting", "source": src,
    })
    existing.add(norm(url))
    added += 1

json.dump(d, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'index.json: before={before} -> after={len(d)} | added={added}')
