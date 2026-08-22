# -*- coding: utf-8 -*-
"""Offsite 团建务虚 二十三轮补采 (2026-08-23) — 渲染增量 + 追加进累计墙 + 更新 index.json + Obsidian + 乐享上传
仅 ②上下级 / ③高管间，0 peer。本论增量页 offsite-2026-08-23-r23.html。
乐享：Offsite 主题在乐享仅以「每轮独立页」落库（累计墙 offsite.html 不在乐享，map['offsite']['wall']=None），故本轮只新建独立页条目，不更新累计墙。"""
import json, os, re, subprocess, urllib.request, urllib.error

BASE = os.path.dirname(os.path.abspath(__file__))
AT_DIR = os.path.join(BASE, "offsite")
CUM = os.path.join(AT_DIR, "offsite.html")
IDX = os.path.join(BASE, "index.json")
DATE = "2026-08-23"
RUN_NAME = "offsite-2026-08-23-r23.html"
RUN_PATH = os.path.join(AT_DIR, "runs", RUN_NAME)
TMP = os.path.join(AT_DIR, ".run_newcards.tmp.html")
ROUND = 23

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---- 本轮新增卡（仅 ②上下级 / ③高管间，0 peer；10张全 NEW，URL 均经 dedup 校验未命中 index/wall）----
# 关系档：③高管间 6 张（全二手）+ ②上下级 4 张（全二手）
CARDS = [
    {
        "emoji": "\U0001F4CB",
        "title": "10 套经评分验证的高管 Offsite 议程模板（2026）",
        "cat": "议程模板库",
        "rel": "r3", "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "ConsultClarity 汇总 10 套高管 Offsite 议程模板（2026）：首日开场 20 分钟连接轮让远程先暖场，再进入 45 分钟诊断/选项块，次日辩论-决策-激活，收尾每人把承诺打进共享文档实时留痕。混合场需加「远程专用 facilitator」角色盯频道、每问先请远程发言。强主张：好议程由可复用「会话积木」拼装——开场（个人史/ stakes）/诊断（环境扫描/内审/行为映射）/决策（选项+预亡/决策模型）/承诺（90天路线图+RACI+会议审计+反馈轮+收尾承诺）。预工决定成败：会前 1:1 访谈摸隐藏议程与政治，敏感/高价值场必请能挑战 CEO 的外部引导师。",
        "how": "办高管 offsite，学 ConsultClarity「积木式议程+会前1:1访谈」：把开场/诊断/决策/承诺四类会话积木按真问题拼装，而非硬套模板；混合场专设远程 facilitator 防静音；会前 1:1 摸隐藏议程，敏感场请外部引导师。核心是「议程为决策服务，不为填时间」。",
        "url": "http://consultclarity.org/post/executive-offsite-agenda-templates",
        "note": "适用：③ 高管团队 offsite（咨询机构二手；10套模板+会话积木库+混合场远程facilitator+会前1:1，可作议程设计弹药库）。",
    },
    {
        "emoji": "\U0001F30F",
        "title": "AI Vision Quest·芬兰拉普兰领导力静修（AI转型×荒野）",
        "cat": "AI战略静修",
        "rel": "r3", "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "AetherLink 案例：高管领导力静修叠加 AI 转型。荒野去掉组织地位游戏，让高管 peer 学习；AI Lead Architecture 框架把抽象战略变成可操作思维工具。产出：CTO 带回可用原型+90天落地计划，6个月后识别 €2.3M 自动化 ROI、运维 AI 采纳率 72%（基线18%）、部署发票/需求预测智能体（省65%人力/降12%库存），零裁员转岗。90天计划：月1内部对齐拿预算治理、月2训团队、月3试点度量。最大变量：地理隔绝逼出真战略思考+peer 问责。",
        "how": "设计高管 AI offsite，学 AetherLink「荒野隔绝+Golden Prompt Stack+90天计划」：离开办公室去安静处剥离地位游戏；让高管带着可运行 AI 智能体与90天计划离场（非证书）；用季度咨询续接防「静修宿醉」。把 AI 采纳从听课变交付物。",
        "url": "https://aetherlink.ai/en/blog/ai-vision-quest-in-finnish-lapland-leadership-retreat-meets-ai-transformation-rotterdam",
        "note": "适用：③ 高管/CEO 级 AI 转型静修（服务商案例二手；荒野认知放大+智能体交付+90天续接，可作技术转型期 offsite 新角度）。",
    },
    {
        "emoji": "\U0001F9F3",
        "title": "Connect–Reflect–Align（C-R-A）转型静修框架",
        "cat": "转型框架",
        "rel": "r3", "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "NiaDelta 以 Connect–Reflect–Align（C-R-A）框架设计转型静修：连接（跨地域/职能建关系重连使命）→反思（讲故事/小组对话/引导对话，挖假设与战略转向意味）→对齐（澄清成功样貌与角色行为如何演进）。真实案例 MEDA（70年国际发展组织）把年度公司会议做成 C-R-A 静修：虚拟团建预热→区域全球团队连接→反思过去假设→对齐新战略方向；内容质量4.45/5、引导4.58/5、整体92%满意，会后战略对齐与跨职能协作明显增强。主张：静修不是奖励而是文化/战略杠杆。",
        "how": "做转型期高管静修，学 NiaDelta「C-R-A 三段」：先跨边界连接重建关系与使命感，再反思挖假设，最后对齐角色行为与战略；虚拟预热+现场小组对话降低防御。把「年度会」重做成「战略催化剂」而非流程仪式。",
        "url": "https://www.niadelta.com/blogs/beyond-the-break-why-retreats-are-strategic-moments-not-just-a-luxury",
        "note": "适用：③ 高管/跨国领导团队转型静修（咨询机构二手；C-R-A 框架+MEDA 案例，可作连接-反思-对齐范式）。",
    },
    {
        "emoji": "\U0001F4CA",
        "title": "两天高管团队加速器·从「个人」到「操作系统」",
        "cat": "团队对齐案例",
        "rel": "r3", "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "Perpetual 案例：北美某全球食材企业高管团队两天 Executive Leadership Team Accelerator。开场每人命名最重要期待（信任/协作/清晰/聚焦/对齐/纪律/简化）， honesty 拉满。框架组合：个人纹章练习（抱负/优势/恐惧/最佳状态符号→把驱动变数据）→信任可测构造→Relationship Bank Account + FIRO 理论（包容/控制/开放三货币）→影响力九策略（ Inspiration 驱动承诺90%，Pressure 仅个位数）。第二天用 strategy-on-a-page 把15个战略优先级收敛，CASPER 给每「大石头」派 accountable leader。离场时从「高胜任个体」走向「共享操作系统」。",
        "how": "带高管团队 offsite，学 Perpetual「纹章+FIRO+影响力杠杆+strategy-on-a-page」：用个人纹章把隐性驱动变可数据；以 Relationship Bank Account/FIRO 建信任共同词汇；影响力用 Inspiration 而非 Pressure；15优先级收敛成单页+每石头派 accountable owner。把「各管各的」变「同一底盘」。",
        "url": "https://beperpetual.com/insights/articles/when-a-leadership-team-stops-performing-as-individuals/",
        "note": "适用：③ 高管团队对齐/信任（咨询机构二手；纹章+FIRO+影响力九策略+CASPER，可作 ELT 加速器案例）。",
    },
    {
        "emoji": "\U0001F3F7",
        "title": "战略静修引导师·两天产出决策 + 60天跟进协议",
        "cat": "引导师模板",
        "rel": "r3", "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "Promptolis 给出「真产出决策的两天战略静修」完整剧本：Day1 发散（开场定调/战略复盘/3-4项决策+书面承诺/午餐处理承诺/下午执行规划）→Day2 收敛（每项承诺派 owner+首30天+90天里程碑+风险+跨职能依赖）。引导技术：强问题（「什么会让这失败」「我们没说的什么」「若押公司命我们赌吗」）、结构化异议（红队/多票/盲投/强制「本块结束必决X」）、群体动力管理（礼貌切断主导声/引出安静声/冲突=好个人攻击=停）。60天跟进：周1 COS 发决策摘要、周2-4 每周30分检查、日30/日60/日90复盘。",
        "how": "请/做战略静修引导，学 Promptolis「两天决策剧本+60天协议」：Day1发散Day2收敛，每项承诺现场读 aloud 派 owner+日期；用红队/盲投/强制决策块逼收敛；COS 拥有60天跟进（周检+30/60/90复盘）。把「激动离场」变「可追踪承诺」。",
        "url": "https://promptolis.com/originals/strategic-retreat-facilitator",
        "note": "适用：③ 高管战略静修（引导师模板二手；两天决策剧本+60天跟进协议，可作外部引导/内部CEO办范本）。",
    },
    {
        "emoji": "\U0001F4B0",
        "title": "高管战略 Offsite 模板（Series B 实战案例）",
        "cat": "战略模板",
        "rel": "r3", "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "BestMeetingPlanner 高管战略 Offsite 模板：半天 State-of-Business→全员辩论选3-5战略优先级→执行规划派 executive owner+90天里程碑+资源。用例：80人 Series B 创业公司（ARR 600万）面临「上探企业市场 vs 横向相邻扩张」抉择；CFO 用数据（头部10%客户占45%ARR、企业赢率升但周期3倍）、CRO 调研信号、分组建模两路径，最终选「两季度横向+明年企业就绪」序列，每项派 owner+预算包+90天里程碑接 QBR。最佳实践：会前一周发 pre-read（市场/财务/竞争/战略问题）；换环境（别订自己楼会议室）；高 stake 请外部引导师；问题 framing 非演讲；非结构化时间；实时写决策；48h 内发摘要接 OKR/QBR 节奏。",
        "how": "办高管战略 offsite，学 BestMeetingPlanner「决策窗+owner+90天接QBR」：用真实数据（非直觉）辩论、每优先级派 executive owner 与预算包、承诺接现有 QBR/OKR 节奏防遗忘；pre-read 提前一周、换环境、高 stake 请外部引导师。把战略选择变可运营计划。",
        "url": "https://www.bestmeetingplanner.com/templates/executive-strategy-offsite/",
        "note": "适用：③ 高管战略 offsite（模板站二手；Series B 实战+决策窗+90天接QBR，可作战略静修骨架）。",
    },
    {
        "emoji": "\U0001F91D",
        "title": "团队建设议程模板库（含领导力团队建设专场）",
        "cat": "议程模板",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "Confetti 给出分场景团队建设议程模板。Template 14「领导力团队建设专场」（经理群/高管 offsite，60-90分）：0-10 命名探索的领导行为/挑战；10-25 个人反思团队动力；25-45 讨论对齐/沟通/决策规范；45-65 真实领导情境演练；65-80 选领导协议/行为；80-90 收尾。通用半日 retreat 模板（连接热身→团队反思→战略/规划→团建活动→承诺→收尾）配提示词（我们该为团队骄傲什么/要留下什么/成长要护什么/要强化的习惯/下季成功样貌）。混合场另给「远程倡导+数字工具+避免房内私语」要点。",
        "how": "做团队/offsite 议程，学 Confetti「分场景模板+领导力专场」：领导力专场聚焦信任/对齐/决策规范与真实情境演练，而非破冰游戏；通用 retreat 用「反思→规划→团建→承诺」节奏；混合场设远程倡导防静音。把议程从 filler 变杠杆。",
        "url": "https://twilio.withconfetti.com/blog/post/team-building-agenda-templates-for-every-occasion",
        "note": "适用：② 经理群/团队领导（活动平台二手；分场景议程模板+领导力专场+混合场要点，可作团建议程速查）。",
    },
    {
        "emoji": "\U0001F3D5️",
        "title": "团队静修规划·50%排程 50%留白（文化非怨气）",
        "cat": "规划原则",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "NovaTrek 主张「排 50% 时间、留 50% 灵活」的黄金法则，避免静修变怨气。3天样本：周四错峰抵达+欢迎晚餐+自由；周五仅2个强制工作块（共6h）+大量非结构时间（小群/运动/探索）；周六「自选冒险」（户外/文化/躺平三选项）+团队晚餐；周日告别早午餐+15分 retro「你带走的一件事」。活动选品准则：包容（各体能可参与）、低尴尬、自然对话、有明确目的、尽量可选。衡量超越「好不好玩」：即时评分+30天回访（是否影响工作/是否保持连接）+客观指标（敬业度、跨团队 Slack 模式）。",
        "how": "规划团队静修，学 NovaTrek「50/50 留白+可选活动+客观度量」：只排约半时间、留白养有机对话；活动按包容/低尴尬/有目的/可选筛；用30天回访与跨团队连接模式衡量成败，而非「好玩吗」。把静修从消耗变文化投资。",
        "url": "https://www.novatrek.app/en/blog/team-retreat-planning-guide",
        "note": "适用：② 团队负责人/HR（规划指南二手；50/50留白+活动选品准则+客观度量，可作静修排程心法）。",
    },
    {
        "emoji": "\U0001F3EF",
        "title": "团队 Offsite 要「变」不要「演」",
        "cat": "转型心法",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "Basecamp 主张伟大 offsite 始于一个问题：「走出房间时我们想有什么不同？」澄清（12个月方向/新领导信任/优先级对齐/价值观）。给真实对话留白：用提示词逼真话（「为提速我们要停什么」「我们回避没说却该说的」「哪里不对齐、为什么」）。从想法到决策：离场前定「最重要的3项（Vital Few）+owner+追踪节奏+指标」；用30-60-90天检查保势头。锚定情绪：徒步/共创故事/感恩认可让团队「感到」而非「看到」方向。闭环：会后发 debrief 提醒决定与对齐样貌。",
        "how": "做团队 offsite，学 Basecamp「以终为始+真话提示词+Vital Few+30-60-90」：先问「离场要什么不同」再排议程；用停止/回避/不对齐三问逼真实对话；离场锁3优先+owner+检查节奏；会后 debrief 闭环。把「记得的周末」变「每天感受到的 shifts」。",
        "url": "https://basecampconsultingllc.com/blog/team-offsites-that-transform-not-just-entertain",
        "note": "适用：② 团队领导/HR（咨询二手；以终为始+真话提示词+Vital Few，可作团队 offsite 转型心法）。",
    },
    {
        "emoji": "\U0001F5D3️",
        "title": "企业静修议程设计（目的+混合工作+收尾合成）",
        "cat": "议程设计",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "Campfire 给企业静修议程全指南：①定目的与期望成果并提前广而告之；②欢迎定调（到达缓冲/后勤/开场提醒目标与「可放松」许可）；③混合风格工作块（深度工作坊/小组合/创意/客座）；④连接活动（破冰勿尬、户外自然/可选、非结构社交）；⑤健康正念可选；⑥战略 downtime 非懈怠；⑦收尾合成（总结洞察/决策/下一步，勿以后勤收尾）+庆祝归属。按精力流排：晨聚焦、下午创造、早可选 wellness。强调「事件在邀约发出时已开始」，Priya Parker 式刻意设计。",
        "how": "设计企业静修议程，学 Campfire「目的先行+混合工作块+收尾合成非后勤」：开场给「可放松」许可降防御；工作块混深度/小组/创意；连接活动低尴尬可选；收尾做合成（决策+下一步）而非念退房须知。按精力流排晨聚焦下午创造。",
        "url": "https://www.campfire-company.com/blog/creating-an-agenda-for-a-business-retreat",
        "note": "适用：② 团队领导/行政（议程指南二手；目的先行+混合工作块+收尾合成，可作企业静修议程骨架）。",
    },
]

def card_html(c, indent=4):
    sp = " " * indent
    sp2 = " " * (indent + 2)
    rel_badge = '<span class="badge {0}">{1}</span>'.format(c["rel"], c["rel_text"])
    src_badge = '<span class="badge {0}">{1}</span>'.format(c["src"], c["src_text"])
    return (
        sp + '<div class="hl">\n'
        + sp2 + '<div class="top"><span class="emoji">' + esc(c["emoji"]) + '</span>'
        + '<h3>' + esc(c["title"]) + '</h3><span class="cat">' + esc(c["cat"]) + '</span>'
        + rel_badge + src_badge + '</div>\n'
        + sp2 + '<p class="val">' + esc(c["val"]) + '</p>\n'
        + sp2 + '<details class="exec"><summary>怎么做</summary><div class="inner">' + esc(c["how"]) + '</div></details>\n'
        + sp2 + '<div class="src">\U0001F517 <a href="' + esc(c["url"]) + '" target="_blank">' + esc(c["url"]) + '</a></div>\n'
        + sp2 + '<div class="note">' + esc(c["note"]) + '</div>\n'
        + sp + '</div>\n'
    )

def find_grid_close(h, sec_start):
    gi = h.find('<div class="grid">', sec_start)
    assert gi != -1, "grid not found"
    depth = 0
    i = gi + len('<div class="grid">')
    while i < len(h):
        if h.startswith('<div', i):
            depth += 1
            i = h.find('>', i) + 1
        elif h.startswith('</div>', i):
            if depth == 0:
                return i
            depth -= 1
            i += 5
        else:
            i += 1
    raise RuntimeError("unbalanced")

# ---- 1) 写临时新卡块 ----
open(TMP, "w", encoding="utf-8").write("".join(card_html(c) for c in CARDS))
print("临时新卡块已写:", TMP)

# ---- 2) 墙注入 ----
html = open(CUM, encoding="utf-8").read()
before = html.count('<div class="hl">')
cards_sec3 = [c for c in CARDS if c["rel"] == "r3"]
cards_sec2 = [c for c in CARDS if c["rel"] == "r2"]
assert cards_sec3 and cards_sec2
i3 = html.find('class="sec sec3"')
close3 = find_grid_close(html, i3)
html = html[:close3] + "".join(card_html(c) for c in cards_sec3) + html[close3:]
i2 = html.find('class="sec sec2"')
close2 = find_grid_close(html, i2)
html = html[:close2] + "".join(card_html(c) for c in cards_sec2) + html[close2:]
# hero
hero_old = "2026-08-22 二十二轮补采 +6"
hero_new = "2026-08-22 二十二轮补采 +6 ｜ 2026-08-23 二十三轮补采 +10"
assert hero_old in html, "hero marker not found"
html = html.replace(hero_old, hero_new, 1)
# recount
def recount(tagcls):
    s = html.find('class="' + tagcls + '"')
    e = html.find('class="sec', s + 10)
    return html[s:e].count('<div class="hl">') if e != -1 else html[s:].count('<div class="hl">')
r2n = recount('sec sec2'); r3n = recount('sec sec3')
html = re.sub(r'(<div class="sec sec3">.*?<span class="tag">)\d+', lambda m: m.group(1) + str(r3n), html, count=1, flags=re.S)
html = re.sub(r'(<div class="sec sec2">.*?<span class="tag">)\d+', lambda m: m.group(1) + str(r2n), html, count=1, flags=re.S)
open(CUM, "w", encoding="utf-8").write(html)
after = html.count('<div class="hl">')
r2b = html.count('badge r2'); r3b = html.count('badge r3')
b1b = html.count('badge b1'); b2b = html.count('badge b2')
footer_ok = "\U0001F4CC \u672c\u9875\u7531 yitong" in html
print("累计墙卡片数:", after, "(+", after - before, ") | r2:", r2b, "r3:", r3b, "| b1:", b1b, "b2:", b2b, "| footer:", footer_ok)
print("sec2 tag:", r2n, "sec3 tag:", r3n)

# ---- 3) 独立页（gen_run_page.py，显式 --out 防嵌套路径 bug）----
gen = os.path.join(BASE, "gen_run_page.py")
r = subprocess.run(["python", gen, "--topic", "offsite", "--topic-name",
                    "Offsite \u56e2\u5efa\u52a1\u865a", "--date", DATE, "--round", str(ROUND),
                    "--cards-file", TMP, "--out", RUN_PATH], capture_output=True, text=True)
print("gen_run_page:", r.returncode, r.stdout.strip(), (r.stderr.strip()[:200] if r.stderr else ""))

# ---- 4) index.json ----
def normkey(t):
    out = []
    for ch in t.lower():
        if ch.isalnum() or "一" <= ch <= "鿿":
            out.append(ch)
    return "".join(out)

data = json.load(open(IDX, encoding="utf-8"))
existing_urls = {e.get("url", "").lower().rstrip("/") for e in data}
added = 0
for c in CARDS:
    u = c["url"].lower().rstrip("/")
    if u in existing_urls:
        print("SKIP dup url:", u); continue
    entry = {
        "title": c["title"],
        "normKey": normkey(c["title"]),
        "url": c["url"],
        "sourceType": "secondary" if c["src"] == "b2" else "primary",
        "relation": "exec" if c["rel"] == "r3" else "supervisor",
        "summary": c["cat"] + "：" + c["val"][:60],
        "topic": "offsite",
    }
    data.append(entry); added += 1; existing_urls.add(u)
print("index.json 新增:", added, "-> 现", len(data), "条")
json.dump(data, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

# ---- 5) Obsidian 主题汇总笔记（newest-first：插到首个 ## 轮次 之前）----
VAULT = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库"
NOTE = os.path.join(VAULT, "素材", "offsite", "Offsite-团建务虚-知识卡汇总.md")
t = open(NOTE, encoding="utf-8").read()
round_section = (
    "\n## 轮次 20260823（+10）\n\n"
    "| 卡 | 适用关系 | 一手/二手 |\n"
    "|---|---|---|\n"
)
for c in CARDS:
    rel = "高管间" if c["rel"] == "r3" else "上下级"
    src = "一手" if c["src"] == "b1" else "二手"
    round_section += "| {0}（offsite.html） | {1} | {2} |\n".format(esc(c["title"]), rel, src)
first_round = t.find("## 轮次")
assert first_round != -1
t = t[:first_round] + round_section + t[first_round:]
open(NOTE, "w", encoding="utf-8").write(t)
print("Obsidian 主题汇总笔记已插入本轮 round 段（newest-first）")

# ---- 6) 00-索引（更新计数行 + 关系分层 + 追加卡行）----
IDX0 = os.path.join(VAULT, "00-知识采集索引.md")
i0 = open(IDX0, encoding="utf-8").read()
apos = i0.find("## 主题：Offsite")
assert apos != -1
# 计数行：142 -> 152
assert "**142 卡**" in i0, "142 卡 marker not found"
i0 = i0.replace("**142 卡**", "**152 卡**", 1)
# 轮次标记追加
marker_old = "2026-08-22 二十二轮补采 +6），"
marker_new = "2026-08-22 二十二轮补采 +6｜ 2026-08-23 二十三轮补采 +10），"
assert marker_old in i0, "round marker not found"
i0 = i0.replace(marker_old, marker_new, 1)
# 关系分层 83/59 -> 89/63
assert "③高管间 83 卡 / ②上下级 59 卡" in i0, "rel split not found"
i0 = i0.replace("③高管间 83 卡 / ②上下级 59 卡", "③高管间 89 卡 / ②上下级 63 卡", 1)
# append rows before next "## 主题：" (icebreaker)
npos = i0.find("## 主题：", apos + 10)
assert npos != -1
rows = "".join(
    "| {0}（offsite.html） | 4 | {1} | {2} | {3} |\n".format(
        esc(c["title"]),
        "一手" if c["src"] == "b1" else "二手",
        "③高管间" if c["rel"] == "r3" else "②上下级",
        esc(c["cat"] + "：" + c["val"][:36]))
    for c in CARDS
)
i0 = i0[:npos] + rows + "\n" + i0[npos:]
open(IDX0, "w", encoding="utf-8").write(i0)
print("00-索引已更新（计数+轮次+关系分层+卡行）")

# ---- 7) 本轮独立笔记（runs/ 新建 md）----
os.makedirs(os.path.join(VAULT, "素材", "offsite", "runs"), exist_ok=True)
RUN_NOTE = os.path.join(VAULT, "素材", "offsite", "runs", "Offsite-2026-08-23-第二十三轮-知识卡.md")
n_r3 = sum(1 for c in CARDS if c["rel"] == "r3")
n_r2 = sum(1 for c in CARDS if c["rel"] == "r2")
rn = (
    "---\n"
    "title: Offsite-2026-08-23-第二十三轮-知识卡\n"
    "type: 自动化采集\n"
    "date: 2026-08-23\n"
    "tags: [知识采集, Offsite, 二十三轮]\n"
    "relation: [supervisor, exec]\n"
    "---\n\n"
    "# Offsite 团建务虚 · 第二十三轮补采（2026-08-23，+10）\n\n"
    "- **GitHub Pages 独立页**：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/offsite/runs/offsite-2026-08-23-r23.html\n"
    "- **本地路径**：`knowledge-collection/offsite/runs/offsite-2026-08-23-r23.html`\n"
    "- **累计卡片墙（总索引）**：`knowledge-collection/offsite/offsite.html`（[线上](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/offsite/offsite.html)）\n"
    "- **覆盖关系档**：③高管间 {0} 卡 / ②上下级 {1} 卡（无①平级）\n".format(n_r3, n_r2)
    + "- **乐享团队文件夹**：Offsite 子文件夹（463f5f5387de4a9bb87b773aef79767b，仅每轮独立页）\n\n"
    "## 本轮新增 10 卡\n\n"
    "| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n"
)
for c in CARDS:
    rel = "高管间" if c["rel"] == "r3" else "上下级"
    src = "一手" if c["src"] == "b1" else "二手"
    rn += "| {0} | {1} | {2} |\n".format(esc(c["title"]), rel, src)
rn += "\n> 本笔记仅索引，不拷 HTML 副本；完整卡片见上方 GitHub Pages 独立页。\n"
open(RUN_NOTE, "w", encoding="utf-8").write(rn)
print("本轮独立笔记已建:", RUN_NOTE)

# ---- 8) GitHub 同步 ----
sync = os.path.join(os.path.dirname(BASE), "sync_knowledge_github.py")
try:
    rs = subprocess.run(["python", sync], capture_output=True, text=True, timeout=300)
    print("sync_knowledge_github:", rs.returncode, (rs.stdout.strip()[-300:] if rs.stdout else ""), (rs.stderr.strip()[:200] if rs.stderr else ""))
except Exception as e:
    print("\u26a0\ufe0f GitHub 同步异常（告警不阻断）：" + str(e)[:200])

# ---- 9) 乐享上传（whoami 探活；Offsite 仅新建每轮独立页，不更新累计墙）----
MCP_JSON = r"C:/Users/v_yitcai/.workbuddy/mcp.json"
LEXIANG_URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"
FOLDER = "463f5f5387de4a9bb87b773aef79767b"  # Offsite 子文件夹（待清洗素材下）

class LexiangMCP:
    def __init__(self, token):
        self.token = token; self.session = None
    def _post(self, payload, retries=3):
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(LEXIANG_URL, data=data, method="POST")
        req.add_header("Content-Type", "application/json")
        req.add_header("Accept", "application/json, text/event-stream")
        req.add_header("Authorization", self.token)
        if self.session: req.add_header("Mcp-Session-Id", self.session)
        last = None
        for _ in range(retries):
            try:
                resp = urllib.request.urlopen(req, timeout=120)
                sid = resp.headers.get("mcp-session-id")
                if sid: self.session = sid
                return self._parse(resp.read().decode("utf-8", "replace"))
            except urllib.error.HTTPError as e:
                last = "HTTP {0}: {1}".format(e.code, e.read().decode("utf-8", "replace")[:400]); continue
            except Exception as e:
                last = str(e); continue
        raise RuntimeError("POST fail: " + last)
    def _parse(self, raw):
        raw = raw.strip()
        if raw.startswith("data:"):
            raw = "\n".join(l[5:].strip() for l in raw.splitlines() if l.startswith("data:"))
        try: return json.loads(raw)
        except Exception: return json.loads(raw[raw.find("{"):])
    def initialize(self):
        return self._post({"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"wb-uploader","version":"1.0"}}})
    def initialized(self):
        try: self._post({"jsonrpc":"2.0","method":"notifications/initialized"})
        except Exception: pass
    def call(self, name, args):
        return self._post({"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":name,"arguments":args}})
    def biz(self, resp):
        res = resp.get("result")
        if not res: raise RuntimeError("no result: " + json.dumps(resp, ensure_ascii=False)[:300])
        text = ""
        for c in (res.get("content") or []):
            if c.get("type") == "text": text = c.get("text", ""); break
        try: return json.loads(text)
        except Exception: return {"_raw_text": text}

def put_bytes(url, data, retries=3):
    last = None
    for _ in range(retries):
        try:
            req = urllib.request.Request(url, data=data, method="PUT")
            req.add_header("Content-Type", "text/html")
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.status
        except Exception as e:
            last = str(e); continue
    raise RuntimeError("PUT fail: " + str(last))

try:
    token = json.load(open(MCP_JSON, encoding="utf-8"))["mcpServers"]["lexiang"]["headers"]["Authorization"]
    mc = LexiangMCP(token); mc.initialize(); mc.initialized()
    try:
        w = mc.call("whoami", {})
        print("whoami:", json.dumps(mc.biz(w), ensure_ascii=False)[:120])
    except Exception as e:
        print("whoami 跳过:", str(e)[:120])

    # Offsite 乐享：仅新建本轮独立页条目（累计墙 offsite.html 不在乐享，跳过 wall 更新）
    run_bytes = open(RUN_PATH, "rb").read()
    r = mc.call("file_apply_upload", {"parent_entry_id": FOLDER, "name": RUN_NAME,
                                      "extension":"html", "mime_type":"text/html",
                                      "upload_type":"PRE_SIGNED_URL", "size": str(len(run_bytes))})
    biz = mc.biz(r)
    if biz.get("code") != 0:
        raise RuntimeError("apply_upload(run) FAIL {0}".format(biz.get("message")))
    sess = biz["data"]["session"]
    sid = sess.get("session_id") or sess.get("id")
    url = sess.get("upload_url") or sess["objects"][0]["upload_url"]
    st = put_bytes(url, run_bytes)
    if st != 200: raise RuntimeError("PUT(run) status " + str(st))
    r2 = mc.call("file_commit_upload", {"session_id": sid})
    biz2 = mc.biz(r2)
    if biz2.get("code") != 0: raise RuntimeError("commit(run) FAIL " + str(biz2.get("message")))
    rid = biz2["data"]["entry"]["id"]
    print("乐享新建独立页 OK entry_id=", rid)
    mapf = json.load(open(os.path.join(BASE, "lexiang-entry-map.json"), encoding="utf-8"))
    sm = mapf.setdefault("offsite", {"folder_id": FOLDER, "wall": None, "rounds": []})
    sm["folder_id"] = FOLDER
    sm["rounds"].append({"date": DATE, "entry_id": rid, "name": RUN_NAME, "note": "轮次页 R23 (+10)"})
    json.dump(mapf, open(os.path.join(BASE, "lexiang-entry-map.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("已回写 lexiang-entry-map.json（仅 rounds，wall=None 维持）")
except Exception as e:
    print("\u26a0\ufe0f 乐享上传跳过（warning，不中断）：" + str(e)[:300])

print("\n=== R23 完成：新增", added, "卡，墙现", after, "卡 ===")
