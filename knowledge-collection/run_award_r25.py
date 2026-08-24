# -*- coding: utf-8 -*-
"""颁奖典礼 二十五轮补采 (2026-08-25) — 渲染增量 + 追加进累计墙 + 更新 index.json + Obsidian + 乐享上传
仅 ②上下级 / ③高管间，0 peer。本论增量页 award-20260825.html。
乐享：award 主题在乐享以「每轮独立页」落库（folder_id=f585d1b78510459db0ce807cc9688448）。"""
import json, os, re, subprocess, urllib.request, urllib.error

BASE = os.path.dirname(os.path.abspath(__file__))
AT_DIR = os.path.join(BASE, "award")
CUM = os.path.join(AT_DIR, "award.html")
IDX = os.path.join(BASE, "index.json")
DATE = "2026-08-25"
RUN_NAME = "award-20260825.html"
RUN_PATH = os.path.join(AT_DIR, RUN_NAME)
TMP = os.path.join(AT_DIR, ".run_newcards.tmp.html")
ROUND = 25

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---- 本轮新增卡（仅 ②上下级 / ③高管间，0 peer；9张全 NEW，URL 均经 dedup 校验未命中 index/award.html）----
CARDS = [
    {
        "emoji": "\U0001F4CA",
        "title": "认可项目 ROI 建模·给老板看的投资回报论证法",
        "cat": "预算ROI",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "认可/颁奖投入要能向老板证明回报，而非每轮预算都 defending。建模步骤：①先定义目标（降首年流失/奖励里程碑/提销售），目标决定成本假设与回报口径；②算人均年成本——奖项+平台费+行政工时+活动费，固定与变动分离，按人头出数（例 150 人×$100=1.5 万/年）；③量化最大财务杠杆=留任——用当前自愿流失率×替换成本作基线，保守降 1-3pct 转成节省；④生产率/缺勤也折算成钱（服务团队年 5 万单×提升 2%=1000 单，无需加人）；⑤净 ROI=（估算收益-总成本）/总成本，做保守/中性/乐观三情景表。给老板只看「成本/留任节省/生产率/缺勤」一张表，比喊文化有力。",
        "how": "写认可预算 ROI，别只喊「文化值」。先锚定目标（留人/里程碑/销售），再按人头算总投入（奖项+平台+工时+活动），把最大杠杆=留任率降 1-3pct 折算成替换成本节省，生产率/缺勤也折钱，最后净 ROI 三情景表给老板。finance 最爱干净的人均数学，预测可信度来自保守假设。",
        "url": "https://kmuat.kalkinemedia.com/education/guides/how-to-model-the-roi-of-employee-recognition",
        "note": "适用：② HRD/财务/行政负责人（教育媒体二手；ROI 建模五步+人均成本+留任杠杆+三情景，可作颁奖预算论证给老板）。",
    },
    {
        "emoji": "\U0001F4DC",
        "title": "认可 ROI 计算器搭建·成本/参与/结果三问框架",
        "cat": "预算ROI",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "做一张可复用的认可 ROI 计算器，把「感觉有效」换成可重复的管理视图。三问：①成本多少——直接奖励+平台工具+行政工时+传播活动+人员费，用同一周期算；②产生什么活动——提名数/通过奖数/独立获奖人/独立提名者/查阅/分享；③连到什么业务指标——留任/参与度/入职/出勤。关键原则：ROI 不是单一数字，结果当管理估算而非「认可导致」的因果证明；比强行货币化更可信的是 participation/coverage/重复认可/留任 看板。输入字段要带数据字典，别人能复现每个数怎么来的。",
        "how": "搭认可 ROI 计算器，拆三块：总成本（奖励+平台+工时+活动）、活动量（提名/获奖人/提名者/分享）、业务结果（留任/出勤/参与）。把结果当管理估算不是因果证明；与其硬折钱，不如做 participation/coverage/重复认可 看板更稳。字段带数据字典，换人也能复现每个数。",
        "url": "https://walloffame.cloud/recognition-roi-calculator-guide",
        "note": "适用：② HR analytics/薪酬激励负责人（虚拟颁奖平台二手；三问框架+成本项+结果指标+数据字典，可作认可 ROI 计算器模板）。",
    },
    {
        "emoji": "\U0001F9FE",
        "title": "紧预算下的认可配比·80/15/5 省钱不省心意",
        "cat": "预算管控",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "预算紧≠心意薄。80/15/5 配比：80% 日常零成本认可（Slack/Teams 公开点赞、手写卡、例会 spotlight、peer 提名）；15%  tangible 低价实物（胸针/证书/品牌杯/平价奖牌）；5% 「英雄时刻」高 impact（年度水晶奖/销售奖/服务里程碑，当品牌资产）。年度预算公式=人均日常×人数 + 实物单价×数量 + 物流(集装+10-15%缓冲)。省钱杠杆：catalog 优先、CEO/President Club 才定制；批量雕刻标准化文本；亚克力激光刻字可平替水晶；合并寄送降运费。三种规模锚：50 人 $1.8-3.2k / 250 人 $8.5-14k / 2000 人 $55-95k。",
        "how": "预算紧用 80/15/5：八成日常零成本公开认可（点赞/手写卡/例会 spotlight），一成半低价实物（胸针/证书/品牌杯），半成留给年度「英雄奖」当品牌资产。省钱靠 catalog 优先、批量雕刻、亚克力平替水晶、合并寄送；公式=人均日常×人数+实物×量+物流+缓冲。紧预算也能把大时刻办得大。",
        "url": "https://awardmaven.com/managing-employee-recognition-on-a-tight-budget",
        "note": "适用：② 行政/HR/活动执行（颁奖机构二手；80/15/5 配比+预算公式+省钱杠杆+三规模锚，可作紧预算颁奖规划）。",
    },
    {
        "emoji": "\u2696\uFE0F",
        "title": "表彰公开边界·员工个人信息合规（个保法最小必要）",
        "cat": "隐私合规",
        "rel": "r2", "rel_text": "上下级",
        "src": "b1", "src_text": "一手",
        "val": "表彰涉及员工个人信息，必须在「最小必要」内处理。官方口径（《个保法》+中工网）：内部表彰披露姓名+部分工作履历属合法正当，但须事前通知并取得同意；披露身份证号则超出表彰目的之必要性，违法。边界清单：✅ 姓名、部门、获奖事迹摘要（必要且正当）；⚠️ 身份证号/住址/联系方式/家庭情况（超必要，禁止）；🔑 凡公开须取得本人同意，本人提出不公开应尊重其意愿（陕西社会信用条例草案明确）。操作：表彰公告前做个人信息影响评估，只列「姓名+奖项+事迹」，敏感字段一律脱敏；对外公示走「征求同意+可撤回」流程。",
        "how": "做表彰公开，守个保法最小必要：只列姓名+奖项+事迹摘要，身份证号/住址/联系方式/家庭情况一律不公开；任何公开前取得本人同意，本人说「别公开」就尊重。公告前做个人信息影响评估，敏感字段脱敏；对外公示走「征求同意+可撤回」。表彰是好事，但不能任性公开信息。",
        "url": "https://www.workercn.cn/c/2022-02-19/6866782.shtml",
        "note": "适用：② HR合规/法务/行政（中工网+个保法一手；最小必要+同意+脱敏边界，可作表彰个人信息合规 SOP）。",
    },
    {
        "emoji": "\U0001F6E1\uFE0F",
        "title": "荣誉榜/英雄榜公开·隐私与激励的平衡（可反对即停）",
        "cat": "隐私合规",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "企业内部荣誉榜/业绩英雄榜公开姓名，基于「人事管理」特定目的、在必要范围内属合法（法务部函释+104 职涯）；但边界在「非必要不公开、凡公开须征得同意」。实操要点：①荣誉榜只列姓名+业绩亮点，不列身份证/住址/薪资；②发布前告知员工意图并给反对机会——即使 top performer 通常无异议，仍建议留「可反对退出」通道；③内部 leaderboard（如 Employee of the Month）仅列最优、不列末位，数据保护疑虑显著低于全员排名；④末位/低绩效排行对外发布违法风险高（影响当事人内外部声誉），绝不做。结论：表彰公开默认 OK，但「告知+可反对」是底线。",
        "how": "荣誉榜/英雄榜公开姓名默认合法（人事管理目的内），但三条底线：只列姓名+亮点不列敏感信息；发布前告知并给员工反对退出通道；只列最优不列末位，全员低绩效排行绝不对外。表彰要激励也要护隐私——「告知+可反对」是底线。",
        "url": "https://www.workercn.cn/c/2021-11-25/6744512.shtml",
        "note": "适用：② HR/合规/业务负责人（中工网评论+法務部函释二手；荣誉榜合法边界+告知可反对+末位禁公开，可作内部表彰隐私指南）。",
    },
    {
        "emoji": "\U0001F3AD",
        "title": "颁奖典礼供应商甄选·五维评估与避坑（自有团队/案例/报价/应急）",
        "cat": "供应商甄选",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "选颁奖典礼策划/礼仪服务商，五维评估：①按规模定范围——千人级优先自有团队大、硬件足、有同类案例；中小活动重性价比与响应；②查自有团队——策划/设计/搭建/摄像全岗自有，避开依赖转包的中间商（实地考察办公/仓库/成片核实）；③索同类案例包——方案+现场照+成片+客户评价，重点看流程设计/舞台/影像；④报价明细——含服务项/设备规格/人工/时间，合同写明交付标准+应急+售后，防临时加价；⑤异地保障——选有跨省落地、自有设备可整车运、配驻场团队的。费用常含：全案策划+舞美搭建+主持演艺+摄制+礼仪接待+物料+统筹。避坑：低价陷阱后期增项、设备老旧无应急、团队临时拼凑。",
        "how": "选颁奖供应商，五维打分：按规模选范围、查自有全岗团队（别转包）、要同类案例包、逼出明细报价+应急条款、异地看跨省落地能力。合同锁死交付标准与售后，防临时加价；实地考察仓库与成片比看 PPT 真。低价引流+无应急=高危。",
        "url": "https://m.cnpinpai.cn/news_hot/2539766.html",
        "note": "适用：② 行政/采购/活动负责人（品牌排行网二手；五维评估+费用构成+避坑，可作颁奖供应商甄选 SOP）。",
    },
    {
        "emoji": "\u2705",
        "title": "颁奖策划机构选型·一站式闭环与「按图索骥」考察法",
        "cat": "供应商甄选",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "选颁奖晚宴策划机构，核心看「一站式闭环交付」能力（创意→视觉→物料→搭建→执行→传播），减少多供应商协调成本与风格不一风险，高端颁奖尤甚。选型四法：①「按图索骥」——别只看方案 PPT，必须让其提供 1-2 个同规模/预算/性质完整案例包（提案+时间表+现场照/视频+费用清单+客户反馈）；②聚焦项目经理——洽谈阶段要求与未来实际负责的项目经理及核心创意/执行见面，其人经验与响应比公司品牌更重要；③拆分报价明晰权责——区分策划/设计/搭建/物料/第三方人员费，标清每项内容与采购方，避免模糊地带；④验证专属稳定团队+本地资源。Q：中型颁奖盛典提前 3-6 个月启动；预算有限可简化机械灯光、用电子邀请函、保核心颁奖体验。",
        "how": "选颁奖策划机构，认一站式闭环（少协调、风格统一）；用「按图索骥」逼出同规模完整案例包（别只看 PPT），洽谈就锁定实际项目经理见面，拆分报价明晰权责，验证专属团队与本地资源。中型盛典提前 3-6 月启动，预算紧就砍辅助环节、保核心颁奖体验。",
        "url": "https://www.zgswcn.com/shangxun/news.html?aid=808563",
        "note": "适用：② 行政/品牌/活动负责人（中国商报网二手；一站式闭环+按图索骥+项目经理锁定+报价拆分，可作颁奖机构选型指南）。",
    },
    {
        "emoji": "\U0001F3A6",
        "title": "CEO/高管颁奖·影像纪实与品牌战略价值（外部获奖杠杆）",
        "cat": "高管品牌",
        "rel": "r3", "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "高管颁奖的影像与品牌价值，是面向董事会/品牌负责人的战略议题。要点：①高管颁奖本身就是「雇主品牌信号」——把认可与组织战略叙事绑定，对外传递「我们重视什么人」；②外部获奖（行业/媒体/政府奖项）是高管级品牌杠杆——把企业获奖写进战略沟通，提升外部可信度与人才吸引；③影像纪实必须专业——高管致辞/颁奖瞬间/获奖者反应是高价值素材，用于年报、IR 材料、招聘页、社媒；④高管全球颁奖当「文化信号+留人杠杆」，让海外团队感到与总部同频。给品牌/IR 负责人的 ROI：一次高管颁奖的影像资产可复用 12+ 月传播，单位成本远低于单独拍品牌片。",
        "how": "高管颁奖别只当内部仪式——它是雇主品牌信号。把认可与战略叙事绑定，外部获奖写进 IR/战略沟通抬可信度；致辞/颁奖瞬间/获奖反应拍专业影像，复用进年报/招聘/社媒 12+ 月，单位成本远低于单拍品牌片；全球颁奖当留人杠杆让海外同频。给品牌/IR 负责人算这笔复用账。",
        "url": "https://digital-trophy-case.com/blog/employee-recognition-awards-creative-ideas-celebrate-team-achievements",
        "note": "适用：③ CEO/CMO/品牌负责人/IR（企业奖项机构二手；雇主品牌信号+外部获奖杠杆+影像复用 ROI，可作高管颁奖品牌战略论证）。",
    },
    {
        "emoji": "\U0001F4CA",
        "title": "认可项目 ROI 三层次度量·运营/参与/业务影响记分卡",
        "cat": "预算ROI",
        "rel": "r3", "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "向高管汇报认可项目，用三层记分卡替代单一模糊数字：①运营效率层——程序耗时/提名数/评审时长/模板降噪；②参与 engagement 层——提名率/投票完成率/虚拟荣誉墙访问/社媒分享/经理参与/重复提名/跨团队参与（最先可靠的指标）；③业务影响层——留任（被认可者留任、提名者留任、强参与团队流失降）、内部流动、生产率、客户反馈、招聘兴趣。财务只估合理处（留任最典型，用自身替换成本保守算区间），其余留行为记分卡。给高管的最佳交付=「财务估算+行为记分卡+叙述」混合报告，而非硬塞单一 ROI 数。",
        "how": "向高管汇报认可，交三层记分卡：运营（耗时/提名/评审）、参与（提名率/荣誉墙访问/经理参与/跨团队）、业务（留任/流动/生产率/招聘）。财务只估留任等合理处、用区间不吹单点；其余留行为记分卡。最佳交付=「财务估算+行为记分卡+叙述」混合，别硬塞单一 ROI。",
        "url": "https://greatest.live/recognition-program-roi-metrics-benchmarks-and-reporting-ideas",
        "note": "适用：③ CHRO/CFO/高管（HR 媒体二手；三层度量+混合报告+留任区间估，可作认可项目高管汇报框架）。",
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
hero_old = "二十一轮 enrich 2026-08-21(+6) ｜ 二十二轮 enrich 2026-08-22(+6) ｜ 二十三轮 enrich 2026-08-23(+10) ｜ 二十四轮 enrich 2026-08-24(+8)"
hero_new = hero_old + " ｜ 二十五轮 enrich 2026-08-25(+9)"
assert hero_old in html, "hero marker not found"
html = html.replace(hero_old, hero_new, 1)
open(CUM, "w", encoding="utf-8").write(html)
after = html.count('<div class="hl">')
r2b = html.count('badge r2'); r3b = html.count('badge r3')
b1b = html.count('badge b1'); b2b = html.count('badge b2')
footer_ok = "\U0001F4CC \u672c\u9875\u7531 yitong" in html
print("累计墙卡片数:", after, "(+", after - before, ") | r2:", r2b, "r3:", r3b, "| b1:", b1b, "b2:", b2b, "| footer:", footer_ok)

# ---- 3) 独立页（gen_run_page.py）----
gen = os.path.join(BASE, "gen_run_page.py")
r = subprocess.run(["python", gen, "--topic", "award", "--topic-name",
                    "\u9881\u5956\u5178\u793c", "--date", DATE, "--round", str(ROUND),
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
        "topic": "award",
    }
    data.append(entry); added += 1; existing_urls.add(u)
print("index.json 新增:", added, "-> 现", len(data), "条")
json.dump(data, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

# ---- 5) Obsidian 主题汇总笔记（newest-first：插到首个 ## 轮次 之前）----
VAULT = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库"
NOTE = os.path.join(VAULT, "素材", "award", "颁奖-知识卡汇总.md")
t = open(NOTE, encoding="utf-8").read()
assert "共 149 张" in t, "摘要 149 marker not found"
t = t.replace("共 149 张", "共 158 张", 1)
round_section = (
    "\n## 轮次 2026-08-25（+9）\n\n"
    "本轮新增（均通过六维评估、仅 ②上下级 / ③高管间）：\n"
)
for c in CARDS:
    rel = "高管间" if c["rel"] == "r3" else "上下级"
    src = "一手" if c["src"] == "b1" else "二手"
    round_section += "- {0}（award.html） | {1} | {2}\n".format(esc(c["title"]), rel, src)
first_round = t.find("## 轮次")
assert first_round != -1
t = t[:first_round] + round_section + t[first_round:]
open(NOTE, "w", encoding="utf-8").write(t)
print("Obsidian 主题汇总笔记已插入本轮 round 段（newest-first）+ 摘要计数 149->158")

# ---- 6) 00-索引（更新计数行 + 轮次标记 + 追加卡行）----
IDX0 = os.path.join(VAULT, "00-知识采集索引.md")
i0 = open(IDX0, encoding="utf-8").read()
apos = i0.find("## 主题：颁奖")
assert apos != -1
npos = i0.find("## 主题：", apos + 10)
assert npos != -1
blk = i0[apos:npos]
assert "**149 卡**" in blk, "149 卡 marker not found in award block"
i0 = i0[:apos] + blk.replace("**149 卡**", "**158 卡**", 1) + i0[npos:]
marker_old = "二十一轮 enrich 2026-08-21(+6) ｜ 二十二轮 enrich 2026-08-22(+6) ｜ 二十三轮 enrich 2026-08-23(+10) ｜ 二十四轮 enrich 2026-08-24(+8)"
marker_new = marker_old + " ｜ 二十五轮 enrich 2026-08-25(+9)"
assert marker_old in i0, "round marker not found"
i0 = i0.replace(marker_old, marker_new, 1)
rows = "".join(
    "| {0}（award/award.html） | 4 | {1} | {2} | {3} |\n".format(
        esc(c["title"]),
        "一手" if c["src"] == "b1" else "二手",
        "③高管间" if c["rel"] == "r3" else "②上下级",
        esc(c["cat"] + "：" + c["val"][:30]))
    for c in CARDS
)
i0 = i0[:npos] + rows + "\n" + i0[npos:]
open(IDX0, "w", encoding="utf-8").write(i0)
print("00-索引已更新（计数149->158+轮次+卡行）")

# ---- 7) 本轮独立笔记（runs/ 新建 md）----
os.makedirs(os.path.join(VAULT, "素材", "award", "runs"), exist_ok=True)
RUN_NOTE = os.path.join(VAULT, "素材", "award", "runs", "颁奖-2026-08-25-第二十五轮-知识卡.md")
n_r3 = sum(1 for c in CARDS if c["rel"] == "r3")
n_r2 = sum(1 for c in CARDS if c["rel"] == "r2")
rn = (
    "---\n"
    "title: 颁奖-2026-08-25-第二十五轮-知识卡\n"
    "type: 自动化采集\n"
    "date: 2026-08-25\n"
    "tags: [知识采集, 颁奖, 二十五轮]\n"
    "relation: [supervisor, exec]\n"
    "---\n\n"
    "# 颁奖典礼 · 第二十五轮补采（2026-08-25，+9）\n\n"
    "- **GitHub Pages 独立页**：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/award-20260825.html\n"
    "- **本地路径**：`knowledge-collection/award/award-20260825.html`\n"
    "- **累计卡片墙（总索引）**：`knowledge-collection/award/award.html`（[线上](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/award.html)）\n"
    "- **覆盖关系档**：③高管间 {0} 卡 / ②上下级 {1} 卡（无①平级）\n".format(n_r3, n_r2)
    + "- **乐享团队文件夹**：颁奖 子文件夹（f585d1b78510459db0ce807cc9688448，每轮独立页）\n\n"
    "## 本轮新增 9 卡\n\n"
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

# ---- 9) 乐享上传（whoami 探活；award 新建每轮独立页）----
MCP_JSON = r"C:/Users/v_yitcai/.workbuddy/mcp.json"
LEXIANG_URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"
FOLDER = "f585d1b78510459db0ce807cc9688448"  # award 子文件夹（待清洗素材下）

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

    # 新建本轮独立页
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
    sm = mapf.setdefault("award", {"folder_id": FOLDER, "rounds": []})
    sm["folder_id"] = FOLDER
    sm["rounds"].append({"date": DATE, "entry_id": rid, "name": RUN_NAME, "note": "轮次页 R25 (+9：预算ROI/认可计算器/紧预算配比/隐私合规×2/供应商甄选×2/高管品牌/高管ROI记分卡)"})
    json.dump(mapf, open(os.path.join(BASE, "lexiang-entry-map.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("已回写 lexiang-entry-map.json")
except Exception as e:
    print("\u26a0\ufe0f 乐享上传跳过（warning，不中断）：" + str(e)[:300])

print("\n=== R25 完成：新增", added, "卡，墙现", after, "卡 ===")
