# -*- coding: utf-8 -*-
# Offsite 团建务虚 · 第三十二轮补采（2026-09-02, +7）
# 关系档：②上下级 4 / ③高管间 3（无①平级）
import os, re, json, subprocess

KC = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(KC, "offsite", "offsite.html")
TMP = os.path.join(KC, "offsite", ".run_newcards.tmp.html")
IDX = os.path.join(KC, "index.json")
OBS_SUM = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\offsite\Offsite-团建务虚-知识卡汇总.md"
OBS_00 = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
RUNS_NOTE = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\offsite\runs\Offsite-2026-09-02-第三十二轮-知识卡.md"

TOPIC = "offsite"
DATE = "2026-09-02"
ROUND = 32

CARDS = [
    {
        "emoji": "🧠", "cat": "包容设计", "rel": "r2", "rel_label": "上下级",
        "title": "神经多元友好型 Offsite（包容性设计：提前2-3周发详尽信息/感官友好/多参与模式免伪装/安静室常态不污名）",
        "url": "https://www.offsite.com/blog/inclusive-event-planning",
        "val": "团队约15-20%为神经多元（ADHD/自闭症/感统差异/学习差异），多数不披露。标准 high-stimulation 设计（荧光灯/强气味/连续8小时社交/突发惊喜）会让他们全程耗在焦虑与「伪装」上，等于浪费 offsite 投资。包容性设计原则：①可预测性——提前2-3周（而非几天前）发详尽日程、场地、餐饮、住宿、着装、社交强度预期，让其有心理准备；②真灵活——「可选」必须真可选，不惩罚跳过者；多参与模式（书面/1:1/边走边谈），不强制上台；③感官友好——可调光场地、降噪、无香氛、安静室常态化且用起来不显「不合群」；④把便利变默认而非「申请」——不要求自曝需求才给 accommodation。对领导的 pitch：这不是降低标准，是扩大「参与」的定义让所有人贡献最佳；成本近乎为零（多为设计选择），留人是真金白银。设专属保密联系人、主动问「节奏合适吗」、离场/跳活动不扣分。",
        "exec_inner": "神经多元友好 offsite：提前2-3周发详尽信息(日程/场地/餐饮/社交强度)降焦虑;「可选」真可选不惩罚跳过;多参与模式(书面/1:1/边走边谈)免强制上台;感官友好(可调光/降噪/无香氛/安静室常态不污名);accommodation 变默认不要求自曝;设保密联系人+主动问节奏;成本近零留人真金白银。",
        "note": "适用：② 公司内部上下级场景（HR/行政 owner 办含多元认知风格的团队 offsite），「可预测性+真灵活+感官友好+安静室常态+默认便利」是可迁移包容设计，补西方心理安全/无障碍之外「神经多元」这一被忽视的硬缺口（约15-20%人口）。🔍 区别于卡片（一般无障碍/DEI 征集需求）；本卡是「神经多元专属设计纪律（免伪装、提前发信息、多模式参与）」，非泛泛无障碍清单。",
        "summary": "神经多元友好型 offsite：提前2-3周发详尽信息降焦虑/「可选」真可选不惩罚/多参与模式免强制上台/感官友好+安静室常态不污名/accommodation 变默认不要求自曝；成本近零、留人真金白银（约15-20%人口为神经多元）。",
        "quality": 4,
    },
    {
        "emoji": "💰", "cat": "预算论证", "rel": "r2", "rel_label": "上下级",
        "title": "向 CFO/财务争取 Offsite 预算批准的商业论证框架（支出重构为资本投资/目标翻译为财务语言/留人成本$50-200k/真实ROI非感受）",
        "url": "https://www.affinitytravel.co/blog/how-to-build-the-business-case-for-a-company-offsite",
        "val": "offsite 常被毙因「当文化支出 pitching、CFO 按 EBITDA 思考」，两句话不交汇。解法：把 offsite 从「费用」重构为「带可测 thesis 的资本投资」。CFO 真听的三个数：①SHRM 替换一名员工成本=年薪50-200%，一个本想走的员工因一场好的 offsite 留下即回本；②Gallup 2024 顶部象限业务单元比底部盈利高23%，驱动是敬业度，offsite（围绕共享成就而非强制欢乐设计）是规模化拉敬业的最可靠方式之一；③Emburse 2024 调研59%企业自2019增 offsite 预算，因「有效」非「感觉好」。标准 pitch（「提士气/团队需要/对齐」）不是商业论证是愿望——CFO 要的是风险调整后回报：成本多少、成功长啥样、怎么知道成了。真实 ROI 度量：事前定成功指标（留人→追踪参会者90天自愿离职 vs 基线；战略对齐→追踪 offsite 决策落地数与速度）；问业务问题（「更清楚销售策略吗」「更 equipped 干活吗」）而非「更有连接感吗」。还要算 CEO 时间（某40人 offsite CEO 自估省65小时规划时间）。",
        "exec_inner": "向 CFO 争取 offsite 预算：把支出重构为「带可测 thesis 的资本投资」非文化费用;CFO 三数(留人成本=年薪50-200%一留即回本/Gallup顶部象限盈利高23%敬业驱动/Emburse 59%企业增预算因有效);反标准愿望式 pitch(提士气/对齐=被砍);真实ROI度量(事前定指标/留人追90天自愿离职/对齐追决策落地速度与数/问业务问题非感受);算 CEO 省下的规划时间。",
        "note": "适用：② 公司内部上下级场景（HR/CoS/行政 owner 向 CFO/财务争取 offsite 预算批准），「重构为资本投资+翻译目标为财务语言+留人成本弹药+真实ROI度量」是可迁移内推框架，补既有「CFO 就绪预算模板/ROI 测算」之外的「怎么把预算卖下来」这一叙事缺口。🔍 区别于卡片（47行项CFO就绪预算模板/面向CFO可审计预算ROI框架）；本卡是「争取批准的叙事与成本-of-inaction」，非预算表本身。",
        "summary": "向 CFO 争取 offsite 预算：重构为资本投资非文化费用；CFO 三数（留人成本=年薪50-200%一留即回本/Gallup顶部象限盈利高23%/Emburse 59%企业增预算因有效）；真实ROI度量（事前定指标/留人追90天离职/对齐追决策落地）/算CEO省下规划时间。",
        "quality": 4,
    },
    {
        "emoji": "🎯", "cat": "团队对齐", "rel": "r2", "rel_label": "上下级",
        "title": "团队对齐工作坊（决策非讨论/3-5个rocks单一owner/角色清晰矩阵/周节奏/停车不解决）",
        "url": "https://www.thekpsgroup.com/resources/team-alignment-workshop-agenda",
        "val": "多数 offsite 留下一白板想法+周三就凉的暖意。半日团队对齐工作坊的硬规则：板上每一条都变「决策——owner+日期+数字」否则进停车场。输出不是好意文档，是短清单优先级+每职能单一owner+保真诚的周节奏。半天议程（约9:00-12:30，一次短休）：①定调（owner 说唯一产出：离场有优先级/owner/节奏；立「决策非仅讨论」规则）；②描现状（列每核心职能，标是否清晰owner、是否在运转，缺口与双归属=真问题）；③定3-5个季度优先级 rocks（多于5个全落不了；每个写「done when」具体完工条件）；④每职能+每 rock 填单一 owner（备份+其拥有的一个数；绝不留「我们盯着点」）；⑤锁周节奏+承诺（固定周会日时/首份记分卡/每人下周一条承诺/离场前排好首次复盘）。 facilitation：一人出声计时、每 block 最后5分钟喊停、漂移的 block 是只带2决策离场的根因；强制每件事一个名字；停车场不解决（周会才是解决地）；优先级封顶5个。",
        "exec_inner": "团队对齐工作坊硬规则：板上每条变决策(owner+日期+数字)否则进停车场;输出=优先级+每职能单一owner+周节奏非好意文档;半天议程(定调→描现状标缺口/双归属→定3-5 rocks写done when→每职能单一owner+备份+其数字→锁周会+承诺);一人出声计时/强制每事一个名字/停车场不解决/优先级封顶5。",
        "note": "适用：② 公司内部上下级场景（中层 manager/职能 leader 带团队做半日对齐工作坊），「决策非讨论+3-5 rocks+单一owner+周节奏+停车场」是可迁移对齐格式，补「务虚会/战略 offsite 议程」之外「小团队季度对齐」这一轻量可执行缺口（不上 offsite 也能用）。🔍 区别于卡片（合并后团队整合5步/团队章程）；本卡是「半日对齐工作坊的精确议程与决策纪律」，非整合或章程文档。",
        "summary": "团队对齐工作坊：决策非讨论（每杠变owner+日期+数字否则停车场）；3-5个季度rocks写done when；每职能单一owner+备份+其数字；锁周节奏+承诺；一人计时/强制每事一名字/优先级封顶5。",
        "quality": 4,
    },
    {
        "emoji": "🌿", "cat": "绿色落地", "rel": "r2", "rel_label": "上下级",
        "title": "绿色/可持续 Offsite 落地（eco认证场地LEED/Green Key/低废弃/本地采购/碳抵消/无纸化）",
        "url": "https://learn.offsiteio.com/venue-guides-by-city/how-to-plan-a-sustainable-corporate-retreat-in-6-steps",
        "val": "73%员工更愿为强可持续承诺的公司工作，offsite 是展示价值观的高杠杆场景。6步：①定可持续目标（减塑50%/本地采购80%/补碳，要可测）；②选 eco 认证场地（LEED/Green Key/生态旅游认证，看节水/节能/废弃管理）；③绿色活动（自然徒步/社区园艺/在地烹饪课用本地食材降碳）；④详细时间线（8-12周定目标订场→6周定议程餐饮→2周发可持续提醒→1周最终核对）；⑤预算分解（场地40%/F&B25%/活动15%/交通15%/备用5%，样本20人$10k）；⑥风险缓释（天气备用/供应商备选/废弃处置回收）。补充：group transport+直飞降交通碳（最大排放源）；无纸化（数字票务/QR）；本地采购降运输排+文化真实；透明沟通目标建信任；会后将碳排/减废 KPI 出报告。成本增量小，品牌善意+员工满意 ROI 大。",
        "exec_inner": "绿色 offsite 6步：定可测可持续目标(减塑/本地采/补碳)→选eco认证场地(LEED/Green Key)→绿色活动(徒步/在地烹饪)→8-12周时间线→预算(场地40/F&B25/活动15/交通15/备用5)→风险缓释(天气/供应商/废弃);group transport+直飞降碳/无纸化/本地采购/会后出可持续报告。",
        "note": "适用：② 公司内部上下级场景（行政/ESG owner 办可持续 offsite），「eco认证场地+低废弃+本地采购+碳抵消+无纸化+会后报告」是可迁移绿色落地，补「目的地主题式可持续 sprint」之外「把 offsite 本身办绿」这一运营缺口（现有卡是把可持续当议题，本卡是把绿色当执行标准）。🔍 区别于卡片（目的地可持续sprint/碳审计议题）；本卡是「绿色会务运营清单」。",
        "summary": "绿色 offsite 落地：定可测目标→选eco认证场地(LEED/Green Key)→绿色活动→8-12周时间线→预算(场地40/F&B25/活动15/交通15/备用5)→风险缓释；group transport+直飞/无纸化/本地采购/会后可持续报告。",
        "quality": 4,
    },
    {
        "emoji": "📡", "cat": "ELT信号", "rel": "r3", "rel_label": "高管间",
        "title": "2026 ELT 务虚室现场信号 5 模式（AI/peak employment·团队动力学集体·2年+10年视野·客户数据·使命）",
        "url": "http://interchange.com.au/blog/what-were-hearing-in-elt-rooms-right-now",
        "val": "高管引导师在 ELT 务虚室观察到的5个当下信号（跨医疗/零售/建筑/金融/能源/政府）：①AI 已改写游戏规则——有的还在琢磨怎么用，有的已把「任务」与「思考」工作分开，少数在重塑组织运作；「peak employment（雇佣峰值）」说法浮现=未来增长靠人机混合模型；②团队动力学——ELT 从痴迷个体领导（风格/心智/成长边）转向「真实绩效活在集体里」，最好团队急于理解共享模式并在拖慢进度前重校；③战略视野——去年还在做3/5年计划，今年转「2年务实视野+10年展望」双轨（10年保野心、2年让董事会与员工可感）；④客户——客户重心更早更强进入议程，多数团队已带数据来测假设（从直觉到洞察）；⑤使命——高绩效组织比以往更紧绕「why」为指南针，使命清则能量升。对办 offsite 的启示：议程要容得下「集体团队动力学」「AI 对组织设计的影响」「双轨战略视野」这些新议题，而非只重排旧三年计划。",
        "exec_inner": "2026 ELT 务虚室5信号：AI改写游戏规则(任务vs思考分离/peak employment人机混合)→团队动力学转向集体共享模式重校(非个体领导)→战略视野转2年务实+10年展望双轨→客户重心更早带数据测假设(直觉到洞察)→使命更紧绕why为指南针;offsite议程要容这些新议题非只排旧三年计划。",
        "note": "适用：③ 高管团队（ELT/C-suite）务虚议程设计，「AI/集体团队动力学/双轨战略视野/客户数据/使命」是2026现场信号，补「务虚议程模板/2026趋势」之外「引导师在一线 ELT 室实测到的具体转向」（田野信号级，非规划 tip）。🔍 区别于卡片（2026高管Retreat规划趋势/10套议程模板）；本卡是「ELT 室里正在发生什么」的实证观察，给议程定调弹药。",
        "summary": "2026 ELT 务虚室5现场信号：AI改写规则(任务vs思考分离/peak employment) / 团队动力学转集体共享模式重校 / 战略视野转2年+10年双轨 / 客户更早带数据测假设 / 使命更紧绕why；offsite 议程须容这些新议题。",
        "quality": 4,
    },
    {
        "emoji": "🛠️", "cat": "执行纪律", "rel": "r3", "rel_label": "高管间",
        "title": "专业务虚执行 vs 内部 DIY（战略意图先于行程/引导师逼出决策非对话/会后问责挂钩KPI/风险与品牌完整）",
        "url": "https://www.planretreat.com/blog-old/retreat-execution-in-2026-what-smart-planners-know-that-diy-doesnt-deliver",
        "val": "2026 高杠杆务虚与平均务虚的差别不在预算，在「执行」。专业执行相对内部 DIY（HR/EA 好意但缺系统）的5个差：①战略意图先于行程——专业方从业务需求/待决决策/待解错位/需达成果倒推每场设计，DIY 只排可见项（差旅/餐饮/议程排版）；②引导逼出决策非对话——外部引导不受内部政治/角色动力学约束，用工具加速说真话、解锁群体动力学、建共享 ownership，敢碰难对话；③运营精度不分散参与者——内部人既要当参与者又要管后勤必分心，专业方有专属 on-site 支持与实时适配；④体验设计造记忆流与洞察——用行为科学/体验地图/环境心理排能量与注意力、结构化思考+互动、意外与意义的钩子（情感粘性→行为改变）；⑤数据闭环与会后问责——pre-event 诊断测错位/士气gap、实时反馈调引导、会后行动映射挂团队 KPI（让务虚成执行引擎非孤立事件）；外加风险与品牌完整（危机预案/法律责任/保险/声誉与行为守护）。结论：不确定性年代，清晰是竞争优势，执行是纪律。",
        "exec_inner": "专业务虚执行 vs DIY 5差：战略意图先于行程(从业务需求/待决决策倒推)→引导逼出决策非对话(外部不受政治约束/加速说真话)→运营精度不分散参与者(专属on-site支持)→体验设计造记忆流(行为科学排能量/情感粘性)→数据闭环+会后问责挂KPI(务虚成执行引擎);加风险与品牌完整;执行是纪律非预算。",
        "note": "适用：③ 高管团队务虚的筹备决策（CHRO/CoS 判断「自建还是外聘专业执行」），「战略意图倒推+外部引导逼决策+会后问责挂KPI+风险品牌完整」是可迁移执行标准，补「引导师遴选/务虚议程」之外「为什么专业执行值得（DIY 的坑）」这一采购论证缺口。🔍 区别于卡片（高管offsite引导师遴选标准）；本卡是「专业执行整体 vs 内部DIY 的差距论证」，补「是否值得外聘」的决策层。",
        "summary": "专业务虚执行 vs 内部DIY：战略意图先于行程(业务需求倒推)/外部引导逼出决策非对话/运营精度不分散参与者/体验设计造记忆流/数据闭环+会后问责挂KPI+风险品牌完整；2026 执行是纪律非预算。",
        "quality": 4,
    },
]


def card_html(c):
    return (
        '    <div class="hl">\n'
        f'      <div class="top"><span class="emoji">{c["emoji"]}</span><h3>{c["title"]}</h3>'
        f'<span class="cat">{c["cat"]}</span><span class="badge {c["rel"]}">{c["rel_label"]}</span>'
        '<span class="badge b2">二手</span></div>\n'
        f'      <p class="val">{c["val"]}</p>\n'
        '      <details class="exec"><summary>怎么做</summary>'
        f'<div class="inner">{c["exec_inner"]}</div></details>\n'
        f'      <div class="src">🔗 <a href="{c["url"]}" target="_blank">{c["url"]}</a></div>\n'
        f'      <div class="note">{c["note"]}</div>\n'
        '    </div>\n'
    )


def main():
    # ---------- 1) 注入累计墙 ----------
    html = open(WALL, encoding="utf-8").read()
    before = html.count('<div class="hl">')

    cards_r3 = "".join(card_html(c) for c in CARDS if c["rel"] == "r3")
    cards_r2 = "".join(card_html(c) for c in CARDS if c["rel"] == "r2")

    sec2_marker = '<div class="sec sec2">'
    i = html.index(sec2_marker)
    j = html[:i].rfind('</div>')  # sec3 grid 闭合
    html = html[:j] + cards_r3 + html[j:]

    fidx = html.index('<footer')
    k = html[:fidx].rfind('</div>')  # sec2 grid 闭合
    html = html[:k] + cards_r2 + html[k:]

    # hero round 注记
    hero_old = "2026-09-02三十一轮补采 +8（高管冲突治理(CEO不当治疗师/分级干预)/决策机制operating model(RACI-RAPID)/多新成员团队90天/心理安全前置+经理难对话/30-60-90落地/团队章程/混合远程平权）"
    hero_new = hero_old + " ｜ 2026-09-02 三十二轮补采 +7（神经多元友好型offsite/向CFO争取预算批准商业论证框架/团队对齐工作坊决策非讨论/绿色可持续offsite落地/2026 ELT务虚室5现场信号/专业务虚执行vs内部DIY）"
    html = html.replace(hero_old, hero_new, 1)
    # tag 计数
    html = html.replace(">134 卡<", ">137 卡<", 1)
    html = html.replace(">91 卡<", ">95 卡<", 1)

    open(WALL, "w", encoding="utf-8").write(html)
    after = html.count('<div class="hl">')
    print(f"[wall] hl before={before} after={after} (+{after-before})")

    # ---------- 2) .run_newcards.tmp.html ----------
    open(TMP, "w", encoding="utf-8").write("".join(card_html(c) for c in CARDS))
    print("[tmp] wrote", len(CARDS), "cards")

    # ---------- 3) index.json 追加 ----------
    data = json.load(open(IDX, encoding="utf-8"))
    existing_urls = set()
    for e in data:
        u = e.get("url", "")
        u = u.strip().lower().replace("&amp;", "&")
        u = re.sub(r"^https?://", "", u); u = re.sub(r"^www\.", "", u); u = u.rstrip("/")
        existing_urls.add(u)
    added = 0
    for c in CARDS:
        u = c["url"]
        nu = u.strip().lower().replace("&amp;", "&")
        nu = re.sub(r"^https?://", "", nu); nu = re.sub(r"^www\.", "", nu); nu = nu.rstrip("/")
        if nu in existing_urls:
            continue
        data.append({
            "title": c["title"],
            "normKey": c["title"],
            "url": u,
            "sourceType": "secondary",
            "relation": "exec" if c["rel"] == "r3" else "supervisor",
            "summary": c["summary"],
            "topic": "offsite",
        })
        existing_urls.add(nu)
        added += 1
    json.dump(data, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"[index.json] total={len(data)} added={added}")

    # ---------- 4) Obsidian 汇总笔记 ----------
    s = open(OBS_SUM, encoding="utf-8").read()
    s = s.replace("· 知识卡汇总（225 卡", "· 知识卡汇总（232 卡", 1)
    s = s.replace("二手 253。", "二手 260。", 1)
    s = s.replace("三十一轮补采 +8（高管冲突治理/决策机制operating model/多新成员团队/心理安全前置+经理难对话/30-60-90落地/团队章程/混合远程平权）卡片墙 HTML：",
                  "三十一轮补采 +8（高管冲突治理/决策机制operating model/多新成员团队/心理安全前置+经理难对话/30-60-90落地/团队章程/混合远程平权） ｜ 2026-09-02 三十二轮补采 +7（神经多元友好型offsite/向CFO争取预算批准商业论证框架/团队对齐工作坊决策非讨论/绿色可持续offsite落地/2026 ELT务虚室5现场信号/专业务虚执行vs内部DIY）卡片墙 HTML：", 1)
    r32_section = (
        "## 轮次 20260902·三十二轮（+7）\n\n"
        "| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n"
        "| 神经多元友好型 Offsite（包容性设计）（offsite.html） | 上下级 | 二手 |\n"
        "| 向 CFO/财务争取 Offsite 预算批准的商业论证框架（offsite.html） | 上下级 | 二手 |\n"
        "| 团队对齐工作坊（决策非讨论/3-5 rocks/单一owner）（offsite.html） | 上下级 | 二手 |\n"
        "| 绿色/可持续 Offsite 落地（eco认证/低废弃/本地采购/碳抵消）（offsite.html） | 上下级 | 二手 |\n"
        "| 2026 ELT 务虚室现场信号 5 模式（AI/集体团队动力学/双轨视野）（offsite.html） | 高管间 | 二手 |\n"
        "| 专业务虚执行 vs 内部 DIY（战略意图倒推/会后问责KPI）（offsite.html） | 高管间 | 二手 |\n\n"
    )
    s = s.replace("## 轮次 20260902·三十一轮（+8）", r32_section + "## 轮次 20260902·三十一轮（+8）", 1)
    open(OBS_SUM, "w", encoding="utf-8").write(s)
    print("[obs-sum] updated")

    # ---------- 5) 00 索引 ----------
    z = open(OBS_00, encoding="utf-8").read()
    z = z.replace("**225 卡**（2026-08-07 首采", "**232 卡**（2026-08-07 首采", 1)
    z = z.replace(
        "2026-09-02 三十一轮补采 +8（高管冲突治理/决策机制operating model/多新成员团队/心理安全前置+经理难对话/30-60-90落地/团队章程/混合远程平权），已按「受众关系分层」",
        "2026-09-02 三十一轮补采 +8（高管冲突治理/决策机制operating model/多新成员团队/心理安全前置+经理难对话/30-60-90落地/团队章程/混合远程平权） ｜ 2026-09-02 三十二轮补采 +7（神经多元友好型offsite/向CFO争取预算批准商业论证框架/团队对齐工作坊决策非讨论/绿色可持续offsite落地/2026 ELT务虚室5现场信号/专业务虚执行vs内部DIY），已按「受众关系分层」", 1)
    z = z.replace("二手 221。按关系分层：③高管间 134 卡 / ②上下级 91 卡。",
                  "二手 228。按关系分层：③高管间 137 卡 / ②上下级 95 卡。", 1)
    rows = (
        "| 神经多元友好型 Offsite（包容性设计：提前发信息/感官友好/多参与模式免伪装）（offsite.html） | 4 | 二手 | ②上下级 | 15-20%为神经多元;可预测性+真灵活+感官友好+安静室常态+默认便利;成本近零留人真金白银 |\n"
        "| 向 CFO/财务争取 Offsite 预算批准商业论证（支出重构为资本投资/留人成本$50-200k/真实ROI非感受）（offsite.html） | 4 | 二手 | ②上下级 | 重构为资本投资非文化费用;CFO三数(留人/敬业23%/59%增预算);事前定指标+问业务问题非感受 |\n"
        "| 团队对齐工作坊（决策非讨论/3-5 rocks/单一owner/周节奏）（offsite.html） | 4 | 二手 | ②上下级 | 板上每条变决策否则停车场;3-5季度rocks写done when;每职能单一owner;停车场不解决;封顶5 |\n"
        "| 绿色/可持续 Offsite 落地（eco认证/低废弃/本地采购/碳抵消/无纸化）（offsite.html） | 4 | 二手 | ②上下级 | 定可测目标→选LEED/Green Key场地→绿色活动→8-12周时间线→预算(场地40/F&B25);group transport+直飞/会后报告 |\n"
        "| 2026 ELT 务虚室现场信号 5 模式（AI/集体团队动力学/双轨视野/客户数据/使命）（offsite.html） | 4 | 二手 | ③高管间 | AI改写规则/团队动力学转集体/2年+10年双轨/客户更早带数据/使命更紧绕why;田野信号级 |\n"
        "| 专业务虚执行 vs 内部 DIY（战略意图倒推/引导逼决策/会后问责KPI/风险品牌）（offsite.html） | 4 | 二手 | ③高管间 | 专业执行5差(意图先于行程/逼决策非对话/不分散参与者/记忆流/数据闭环挂KPI)+风险品牌;执行是纪律非预算 |\n"
    )
    z = z.replace("| 务虚会后不回落：深挖+向下传导+主题目标记分牌（Lencioni）（offsite.html）",
                  rows + "| 务虚会后不回落：深挖+向下传导+主题目标记分牌（Lencioni）（offsite.html）", 1)
    open(OBS_00, "w", encoding="utf-8").write(z)
    print("[obs-00] updated")

    # ---------- 6) 生成当轮独立页 ----------
    out = os.path.join(KC, "offsite", "runs", f"offsite-{DATE}-r{ROUND}.html")
    r = subprocess.run(
        ["python", os.path.join(KC, "gen_run_page.py"),
         "--topic", TOPIC, "--topic-name", "Offsite 团建务虚",
         "--date", DATE, "--round", str(ROUND),
         "--cards-file", TMP, "--out", out],
        capture_output=True, text=True, shell=True,
    )
    print("[run-page]", r.returncode, r.stdout.strip(), r.stderr.strip()[:300])

    # ---------- 7) 当轮独立笔记（Obsidian runs）----------
    rel_counts = {"r3": 0, "r2": 0}
    for c in CARDS:
        rel_counts[c["rel"]] += 1
    note = (
        "---\n"
        "title: Offsite-2026-09-02-第三十二轮-知识卡\n"
        "type: 自动化采集\n"
        "date: 2026-09-02\n"
        "tags: [知识采集, Offsite, 三十二轮]\n"
        "relation: [supervisor, exec]\n"
        "---\n\n"
        "# Offsite 团建务虚 · 第三十二轮补采（2026-09-02，+7）\n\n"
        "- **GitHub Pages 独立页**：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/offsite/runs/offsite-2026-09-02-r32.html\n"
        "- **本地路径**：`knowledge-collection/offsite/runs/offsite-2026-09-02-r32.html`\n"
        "- **累计卡片墙（总索引）**：`knowledge-collection/offsite/offsite.html`（[线上](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/offsite/offsite.html)）\n"
        f"- **覆盖关系档**：③高管间 {rel_counts['r3']} 卡 / ②上下级 {rel_counts['r2']} 卡（无①平级）\n"
        "- **乐享团队文件夹**：待清洗素材·Offsite 子目录（仅每轮独立页，token 失效待补传）\n\n"
        "## 本轮新增 7 卡\n\n"
        "| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n"
        "| 神经多元友好型 Offsite（包容性设计） | 上下级 | 二手 |\n"
        "| 向 CFO/财务争取 Offsite 预算批准商业论证框架 | 上下级 | 二手 |\n"
        "| 团队对齐工作坊（决策非讨论/3-5 rocks/单一owner） | 上下级 | 二手 |\n"
        "| 绿色/可持续 Offsite 落地（eco认证/低废弃/本地采购/碳抵消） | 上下级 | 二手 |\n"
        "| 2026 ELT 务虚室现场信号 5 模式（AI/集体团队动力学/双轨视野） | 高管间 | 二手 |\n"
        "| 专业务虚执行 vs 内部 DIY（战略意图倒推/会后问责KPI） | 高管间 | 二手 |\n\n"
        "> 本笔记仅索引，不拷 HTML 副本；完整卡片见上方 GitHub Pages 独立页。\n"
    )
    open(RUNS_NOTE, "w", encoding="utf-8").write(note)
    print("[runs-note] wrote", RUNS_NOTE)


if __name__ == "__main__":
    main()
