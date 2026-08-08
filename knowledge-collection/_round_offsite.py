import json, re, os, html

BASE = r"C:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection"
idx_path = os.path.join(BASE, "index.json")

def norm(t):
    return re.sub(r"[\s\W_]+", "", t)

with open(idx_path, encoding="utf-8") as f:
    data = json.load(f)

old = len(data)
urls = {e["url"] for e in data}
norms = {e.get("normKey", "") for e in data}

new_entries = [
    {
        "title": "Strategy Offsite Facilitation 路线图（规划到执行）",
        "url": "https://www.sorenkaplan.com/strategy-offsite-facilitation/",
        "sourceType": "secondary",
        "relation": "exec,supervisor",
        "summary": "战略 offsite 引导从规划到执行路线图：会前定清晰目标+受众画像(角色/经验/人际动态/沟通风格)+pre-offsite survey/interview；议程=开场对齐+keynote+breakout+group discussion+closing，平衡聚焦工作与团建；用破冰挑战/角色扮演/创意工坊做团队建设，success 看会后行动与结果"
    },
    {
        "title": "Leadership Retreat 完整分步指南（70/30 法则）",
        "url": "https://www.offsite.com/blog/how-to-plan-a-leadership-retreat",
        "sourceType": "secondary",
        "relation": "exec,supervisor",
        "summary": "领导力 retreat 完整分步指南：70/30 法则(70%战略工作+30%关系建设)，议程按 90-120min 区块+10-15min break+混合模态+显式决策点；外部引导师($8-30k)用于敏感/冲突/新团队话题让 CEO 全程参与；pre-reading 提前 10-14 天；20% flex time"
    },
    {
        "title": "Executive Retreat 规划框架（HBR 2.2x 数据）",
        "url": "https://theoffsiteco.com/news/how-do-you-plan-an-executive-retreat",
        "sourceType": "secondary",
        "relation": "exec",
        "summary": "高管 retreat 规划框架：先答3问(解决什么战略挑战/可衡量产出/需改变哪些领导行为)再选场地；HBR 研究目标清晰公司 top-quartile 概率 2.2x；面对面沟通比数字 34x 有效；venue 按保密/深度工作/庄重感评估而非预算 proximity"
    },
    {
        "title": "尚普「战略决策赋能工作坊」模式",
        "url": "https://survey.cu-market.com.cn/yjywz/qypx3/8794.html",
        "sourceType": "secondary",
        "relation": "supervisor,exec",
        "summary": "尚普『战略决策赋能工作坊』：会前对齐(战略简报→互动预习包+关键问题投票+产出契约)+会中催化(战略意图画布/逆向规划推演/承诺检查公开化责任)+把培训与引导植入战略会议，决策无缝转可执行行动计划，规避『听起来美做起来难』"
    },
    {
        "title": "开好三会：务虚会+解码会+经营分析会（DSTE 中文体系）",
        "url": "https://chinacpx.com/opencourse/2025265708.shtm",
        "sourceType": "secondary",
        "relation": "supervisor,exec",
        "summary": "开好三会体系：战略务虚会(五看三定·定方向凝共识)+战略解码会(战略地图/OGSM-T/PBC·责任互锁)+经营分析会(一报一会·刀刃向内)；务虚定→解码拆→经分调，DSTE/BLM 中文落地框架，华为/中集案例"
    },
    {
        "title": "Designing a Strategy Offsite That Leads to Action（30-60-90）",
        "url": "https://ldnmag.com/innovation/designing-a-strategy-offsite-that-leads-to-action/",
        "sourceType": "secondary",
        "relation": "exec",
        "summary": "设计『导向行动』的战略 offsite：会前个人独立思考防群体思维/结构化参与收集更佳信息/超越表面的 SWOT/室内当场定 owner(不接受就说明未就绪)/30-60-90 节奏(30天书面更新+60天跨团队依赖+90天全面复盘)让承诺成硬约束"
    },
    {
        "title": "Executive Offsite Follow-Through（48h 决策日志）",
        "url": "https://consultclarity.org/post/executive-offsite-follow-through",
        "sourceType": "secondary",
        "relation": "exec",
        "summary": "高管 offsite 落地闭环机制：48 小时内出决策日志、每条承诺一个 owner+一个日期、周度而非季度节奏、CEO 自身 follow-through 可见；90 天仍由原 owner 推进=真正有效的唯一诚实指标，两周后从不被设计是失败根因"
    },
    {
        "title": "腾讯「科技向善」总办务虚会真实案例（陈春花引导）",
        "url": "https://www.yuque.com/kshare/2019/05cb3513-1803-4902-bfc4-654f8520ffac",
        "sourceType": "secondary",
        "relation": "exec",
        "summary": "腾讯总办『科技向善』务虚会真实案例：4.5 小时平等对话(Pony 先听后说)，把业务放一边回到价值观反复拉回；身价极高的一群人全程无手机投入，里程碑式文化务虚会，外部引导师(陈春花)讲课式催化"
    },
    {
        "title": "阿里战略务虚会→规划会→沟通会（上下同欲真实案例）",
        "url": "https://m.trjcn.com/news/detail_8875.html",
        "sourceType": "secondary",
        "relation": "exec",
        "summary": "阿里战略务虚方法论真实案例：『看10年定3年干1年半年1复盘』；战略务虚会明方向→战略规划会确立业务/组织/人才调整→战略沟通会(KO)向全员说清意图上下同欲；曾鸣 MVO 模型提决策质量"
    },
    {
        "title": "新成员高管团队 Offsite（Forming 信任先于战略）",
        "url": "https://consultclarity.org/post/how-to-executive-team-offsite-new-team-members",
        "sourceType": "secondary",
        "relation": "exec",
        "summary": "新成员高管团队 offsite：Tuckman Forming/Storming，新配置重置团队阶段→信任先于战略、基础先于执行；诊断新人比例/关系/摩擦；重排议程(信任建设在前)、重构 pre-work 与 90 天跟进；McKinsey 对齐团队财务表现近 2x"
    },
]

added, skipped = [], []
for e in new_entries:
    e["normKey"] = norm(e["title"])
    if e["url"] in urls:
        skipped.append(("url", e["title"]))
    elif e["normKey"] in norms:
        skipped.append(("norm", e["title"]))
    else:
        data.append(e)
        urls.add(e["url"]); norms.add(e["normKey"])
        added.append(e["title"])

with open(idx_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# card counts in each HTML
htmls = {
    "staff-meeting": "staff-meeting/staff-meeting.html",
    "offsite": "offsite/offsite.html",
    "icebreaker": "icebreaker/icebreaker.html",
    "award": "award/award.html",
    "openday": "openday/openday.html",
    "afternoontea": "afternoontea/afternoontea.html",
}
counts = {}
for k, p in htmls.items():
    try:
        with open(os.path.join(BASE, p), encoding="utf-8") as f:
            counts[k] = f.read().count('class="hl"')
    except Exception as ex:
        counts[k] = f"ERR {ex}"

print("index.json OLD:", old, "NEW:", len(data), "ADDED:", len(added), "SKIPPED:", len(skipped))
for s in skipped:
    print("  skip:", s)
print("HTML card counts:", counts)
print("TOTAL cards:", sum(v for v in counts.values() if isinstance(v, int)))
