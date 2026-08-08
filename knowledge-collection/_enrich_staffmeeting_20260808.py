# -*- coding: utf-8 -*-
"""员工大会(staff-meeting) 二次补采 enrichment：往 index.json 追加本轮新采集条目。
自动化知识采集 · 2026-08-08 轮询（主题=员工大会）。
规则：URL 完全相同 / normKey 归一化相似 → 视为重复，跳过（记录删 M）；否则追加（记录新增 N）。
"""
import json, os, re

BASE = os.path.dirname(os.path.abspath(__file__))
IDX = os.path.join(BASE, "index.json")

def norm(s):
    s = (s or "").lower().strip()
    s = re.sub(r"[\s\-_/.,:：，。、()（）\[\]【】]+", "", s)
    return s

with open(IDX, encoding="utf-8") as f:
    data = json.load(f)

existing_urls = {d.get("url", "") for d in data}
existing_norm = {norm(d.get("normKey", "")) for d in data}

new_entries = [
    {
        "title": "供销大集 2025 年度工作会议（官方复盘）",
        "normKey": "供销大集2025年度工作会议官方复盘",
        "url": "http://www.gongxiaodaji.com/index.php?id=22163",
        "sourceType": "primary",
        "relation": "supervisor",
        "summary": "央企背景上市公司年度工作会：董事长提「三点要求」(危机感动员/强化中心/卧薪尝胆归属感)+总裁工作报告+2024先进集体与个人表彰(专项奖/安全奖/管理精英奖/变革先锋奖)发言；领导↔员工战略对齐+表彰真实案例"
    },
    {
        "title": "华神药业 2025 总结会暨 2026 全员大会（官方）",
        "normKey": "华神药业2025总结会暨2026全员大会官方",
        "url": "https://www.huasungrp.com/news_view.aspx?nid=2&typeid=4&id=1066",
        "sourceType": "primary",
        "relation": "supervisor",
        "summary": "三天结构(拓展训练破隔阂→团拜联欢暖人心→总结会立状明责)；董事长讲十年规划长期主义+责任书签署立状+专业培训+省区复盘；全员大会「复盘-规划-能力-责任」闭环样板"
    },
    {
        "title": "宝光集团 2025 年会总结表彰大会（官方）",
        "normKey": "宝光集团2025年会总结表彰大会官方",
        "url": "http://ahbgjc.com/newscentre/info.aspx?itemid=204",
        "sourceType": "primary",
        "relation": "supervisor",
        "summary": "总裁年度报告(风控体系/CRM上线/增长目标)+优秀总经理经验分享+四大管理中心复盘；表彰含「十年老员工功勋奖」(999纯金35万)+晋升任命+12家子公司目标责任状+董事长寄语+高管发红包；以奋斗者为本样板"
    },
    {
        "title": "恒丰 2025 总结表彰大会暨 2026 新春年会（官方）",
        "normKey": "恒丰2025总结表彰大会暨2026新春年会官方",
        "url": "http://hf-chem.cn/Shownews.asp?BigClass=公司新闻&ID=294",
        "sourceType": "primary",
        "relation": "supervisor",
        "summary": "总经理报告提出「四个转变」战略(管理→经营/成本定价→价值定价/量本利→价本利/恶性→良性竞争)+「三不相信/三马精神」；表彰先进集体与个人+「风雨同舟奖」(20年老员工)；钢铁行业逆势突围真实案例"
    },
    {
        "title": "新疆龙海达 2025 年度总结暨表彰大会（官方）",
        "normKey": "新疆龙海达2025年度总结暨表彰大会官方",
        "url": "http://xjlhdjt.com/articles/show/96",
        "sourceType": "primary",
        "relation": "supervisor",
        "summary": "四大篇章(复盘蓄能/使命必达/风采飞扬/星耀龙海)；13位负责人汇报+董事长部署四核心方向+「星火人才战略」(年投300万)；15位负责人签目标责任状(战书)+团队风采展示；多业态集团全员大会样板"
    },
    {
        "title": "全员沟通大会(All-Hands)怎么开（商业新知）",
        "normKey": "全员沟通大会allhands怎么开",
        "url": "https://www.shangyexinzhi.com/article/16642625.html",
        "sourceType": "secondary",
        "relation": "supervisor",
        "summary": "三段式全体大会：①战略回顾+关键战役里程碑(树立信心)②优秀实践分享(15min脱敏成果+方法心得)③Q&A占25%(预先问卷投票+即兴问答，负责人答/难问题承诺内网回)；把单向传递变双向连接"
    },
    {
        "title": "强力 Town Hall 实操指南（AgileLAB·大厂仪式）",
        "normKey": "强力townhall实操指南agilelab大厂仪式",
        "url": "https://agilelab.de/blog/how-to-run-powerful-town-hall-meetings",
        "sourceType": "secondary",
        "relation": "supervisor,exec",
        "summary": "分步指南：目的定义→员工参与议程(Slido/Forms征集+upvote)→故事化议程(欢迎+领导更新+客户/员工故事+Q&A+仪式)→教练领导(平衡事实情绪/承认失败/人性化)→心理安全(欢迎尖锐问题)；附 Google TGIF/Amazon 6页memo/Meta AMA/Microsoft 包容 大厂仪式对照表；会后24h发录像+FAQ"
    },
    {
        "title": "Asana 全员会议议程模板（60 分钟样例）",
        "normKey": "asana全员会议议程模板60分钟样例",
        "url": "https://asana.com/templates/all-company-meeting",
        "sourceType": "secondary",
        "relation": "supervisor",
        "summary": "工具官方模板：议程七要素(开场icebreaker/业务更新指标/项目团队更新/认可庆祝/团队spotlight/Q&A/行动项)+60分钟样例分配(欢迎5/业务10/项目15/认可5/spotlight5/Q&A15/收尾5)；强调提前发议程+轮换发言人+会前收集Q&A+会后takeaways"
    },
    {
        "title": "远程全员大会 60 分钟议程（TeamRally·只做现场三件事）",
        "normKey": "远程全员大会60分钟议程teamrally",
        "url": "https://teamrally.app/blog/all-hands-meeting-agenda-remote",
        "sourceType": "secondary",
        "relation": "supervisor",
        "summary": "远程专属：全员大会只配现场三件事——能量/认可/无脚本Q&A，其余异步；60分钟分段(开场赢5/业务脉搏10/单点深潜20/认可5/Q&A15/收尾5)；匿名优先征集真实问题、录制必发、跨时区轮换时段、chat作第二舞台；警惕读幻灯片/跳过认可/无预采问题"
    },
    {
        "title": "Gatheround 8 类全员会议模板（分类框架）",
        "normKey": "gatheround8类全员会议模板分类框架",
        "url": "https://valimail.gatheround.com/blog/essential-all-hands-templates",
        "sourceType": "secondary",
        "relation": "supervisor",
        "summary": "八类模板覆盖不同场景：Meeting/Retrospective/Town Hall(重Q&A)/Fireside Chat(轻松问高管)/Business Review(财务KPI)/Cross-Team Sync(破silo)/Celebration/Pulse Check(关系健康)；按会议目的选模板，降低规划成本、提参与度"
    },
]

added, skipped = 0, 0
for e in new_entries:
    if e["url"] in existing_urls or norm(e["normKey"]) in existing_norm:
        skipped += 1
        print(f"[SKIP dup] {e['title']}")
        continue
    data.append(e)
    existing_urls.add(e["url"])
    existing_norm.add(norm(e["normKey"]))
    added += 1
    print(f"[ADD] {e['title']}")

with open(IDX, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n=== 员工大会 enrichment 完成 ===")
print(f"原有条目: {len(data)-added}  →  新增 N={added}  /  去重删 M={skipped}  →  现有总计: {len(data)}")
