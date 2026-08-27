# -*- coding: utf-8 -*-
import os, re, json, subprocess

KC = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(KC, "offsite", "offsite.html")
TMP = os.path.join(KC, "offsite", ".run_newcards.tmp.html")
IDX = os.path.join(KC, "index.json")
OBS_SUM = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\offsite\Offsite-团建务虚-知识卡汇总.md"
OBS_00 = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
RUNS_NOTE = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\offsite\runs\Offsite-2026-08-28-第二十九轮-知识卡.md"

TOPIC = "offsite"
DATE = "2026-08-28"
ROUND = 29

CARDS = [
    {
        "emoji": "⚖️", "cat": "合规责任", "rel": "r2", "rel_label": "上下级",
        "title": "中国法下活动组织者安全保障义务（民法典1198条）+ 自甘风险（1176条）",
        "url": "https://www.dpxq.gov.cn/hdjl/ywzsk/flzx/content/post_12470740.html",
        "val": "中文团队办 offsite/团建/务虚会，组织者是「群众性活动组织者」，依《民法典》第1198条负有法定安全保障义务：未尽义务致他人损害须担侵权责任；因第三人行为致损，第三人担责，组织者未尽安保义务担相应补充责任（可向第三人追偿）。第1176条「自甘风险」：自愿参加一定风险文体活动，因其他参加者行为受损，不得请求其他参加者担责（除非故意或重大过失）——但组织者责任不适用此免责。实务落地：签合同前过场地应急与就医距离、RSVP 收医疗/紧急联系人、避免全员同航班、指定唯一应急 owner、购意外险；活动前安全简报+通信树。中国大陆无《好撒玛利亚人法》，现场急救失误可直接追诉主办方，法定照护义务不能靠外包转移。",
        "exec_inner": "中文 offsite 组织者先立「安全保障义务」底线：依民法典1198条尽场所安保（场地应急/就医距离/疏散），依1176条知「自甘风险」只免参加者间责任、不免组织者；指定唯一应急 owner、RSVP 收医疗与紧急联系人、避免全员同航班、购意外险、活动前安全简报+通信树；照护义务不可外包转移。",
        "note": "适用：② 中文语境公司内部上下级场景（HR/行政 owner 团建/务虚会合规），「民法典1198安全保障义务+1176自甘风险+照护义务不可外包」是本土法务硬约束，补西方 ISO 31030 框架之外的中国法底座。🔍 区别于卡片（duty of care/ISO 31030/探险安全协议）——本卡是「中国民法典法定责任」一手法条口径，非西方标准。",
        "summary": "中国法下 offsite 组织者责任：民法典1198条安全保障义务（未尽则担责/第三人致损担补充责任）+1176条自甘风险（免参加者间责任不免组织者）+照护义务不可外包转移；落地唯一应急owner/医疗RSVP/意外险/安全简报。",
        "quality": 4,
    },
    {
        "emoji": "💬", "cat": "场地议价", "rel": "r2", "rel_label": "上下级",
        "title": "场地议价 7 杠杆省 15-30%（工作日/案例置换/打包/尾期价/回头客/3报价比价）",
        "url": "https://camproxx.com?p=4244/",
        "val": "offsite 最大预算线（场地+住宿常占 55-65%）靠议价而非砍品质省钱。7 个反复验证的杠杆：① 订工作日（周一至周四）省 15-25%，团队损一个工日但省下最大头；② 用案例/好评/品牌授权置换折扣 10-15%（给场地专业照/Google 评价/列其为客户）；③ 单供应商打包（住宿+餐饮+会议+活动+篝火一价）几乎总比拆 4-5 家便宜；④ 要「最近可订日期」尾价——2-3 周内空房场地愿打 20-30% 防空置；⑤ 承诺 12 个月内再办一场（意向书）换 5-10% 回头客折扣；⑥ 拿 3 份书面报价互相施压（可隐去对方名）；⑦ 谈 extras 不谈房价（免费升级/餐/会议室/摄影/免搭建费，等效折扣）。硬数据：留 10% 保守 retention 改善即回本；行业基准团队建设 ROI 7.5x。",
        "exec_inner": "场地议价学 camproxx 七杠杆：订工作日(省15-25%)/案例置换(10-15%)/单供应商打包/尾期空房价(20-30%)/承诺回头客(5-10%)/3份书面报价比价/谈extras不谈房价；最大预算线靠议价不靠砍品质。",
        "note": "适用：② 公司内部上下级场景（行政/HR budget owner 锁场地），「7 杠杆议价省 15-30%」是可抄采购纪律，补 Marco 预算基准（只给三档人均）之外的「怎么把报价压下来」。🔍 区别于卡片（Marco 预算基准/Beefed 会后对账）——本卡是「签约前议价」这一采购动作。",
        "summary": "场地议价7杠杆：工作日订(15-25%)/案例品牌置换(10-15%)/单供应商打包/尾期空房价(20-30%)/回头客意向(5-10%)/3书面报价比价/谈附加不谈房价；最大预算线靠议价不靠砍品质。",
        "quality": 4,
    },
    {
        "emoji": "🏨", "cat": "场地选型", "rel": "r2", "rel_label": "上下级",
        "title": "场地选型评分矩阵（7 要素 / 20 点 MICE / 15 问）：别只比价",
        "url": "https://thetivolihotels.com/blog/choosing-right-mice-venue-checklist",
        "val": "选错场地比选贵场地更贵（天花高度挡投影/带宽撑不住同时设备/厨房 45min 出不来 500 份餐）。用评分矩阵而非只比价：① 容量与布局灵活（同厅 theatre 500 人可能 classroom 只 250）；② AV 与技术基建（HD 投影/无线麦/调音台/广播级 LED，带宽要测模拟负载）；③ 网络带宽（500 人同时 WiFi 需企业级专线+failover）；④ 停车与交通（车位比、近地铁/机场接驳）；⑤ 无障碍合规（轮椅坡道/电梯/听障环路/同传间）；⑥ 餐饮弹性（多样菜单/饮食禁忌/出餐速度/可否外烩）；⑦ 合同条款（取消/ exclusivity/搭建时间/噪音限时/保险要求）。MICE 20 点评分法：四类（Logistics/Hospitality/Budget/Experience）每点 1-5 分，关键项<3 即淘汰或进入议价；总分>80/100 才接专业会。到场看≥2-3 家，最好蹭一场别的会看实景。",
        "exec_inner": "场地选型用评分矩阵不比价：容量布局灵活/AV带宽测负载/无障碍合规/餐饮弹性/合同细项五类；MICE 20点每点1-5分、关键项<3淘汰、总分>80才接；到场看2-3家并蹭实景。",
        "note": "适用：② 公司内部上下级场景（行政/HR 选址 owner），「评分矩阵替代只比价 + MICE 20点打分 + 关键项<3淘汰」是可迁移选址纪律，补「预算基准/议价」之外的「怎么筛掉错场地」。🔍 区别于卡片（Marco 预算/议价杠杆）——本卡是「选型评估」这一前置漏斗。",
        "summary": "场地选型评分矩阵：容量布局/AV带宽测负载/无障碍合规/餐饮弹性/合同细项五维；MICE 20点每点1-5分、关键项<3淘汰、总分>80接专业会；到场看≥2-3家蹭实景。",
        "quality": 4,
    },
    {
        "emoji": "🧰", "cat": "工具栈", "rel": "r2", "rel_label": "上下级",
        "title": "Offsite 工具栈：单一中枢 + 预算/供应商 + 工作坊 + 差旅 + 预调研 + 报销",
        "url": "https://futuremagazine.co.uk/?p=4618",
        "val": "团建/务虚会崩在计划散落多文档+DM+半更新表格。小工具栈把决策/物流/沟通连起来：① 单一中枢——Notion 建 Retreat Dashboard（旅行/日程/预算/决策日志 tab，stakeholders 开权限、参会者限读）；Airtable 管房间/饮食/供应商/发票，附「人均成本」字段算 ROI；② 工作坊——Miro 协作白板建议程流（prompt→timebox→决策捕获），关键讨论先 3 分钟静写降「最大声赢」；③ 差旅——TravelPerk 集中订+自动报销+集团规则（到达窗/可退/酒店半径），单一到达离开视图防接驳猜；④ 预调研——SurveyMonkey 收约束（出行窗/无障碍/饮食）与偏好，问「什么会让这 retreat 浪费」红 flag 题；⑤ 日期——Doodle 两阶段收敛（先定周再定天）+ firm poll deadline；⑥ 报销——Expensify 扫票分类、Splitwise 分摊自发费用；⑦ 注册——Cvent/Whova 管容量与签到。迷你清单：一个总时间表+一个参会表+一个决策日志+一个最终议程链接。",
        "exec_inner": "offsite 工具栈：Notion 中枢(Attendee/预算/决策日志)+Airtable(房间饮食供应商发票/人均成本算ROI)+Miro(议程流/静写降最大声赢)+TravelPerk(差旅报销/到达视图)+SurveyMonkey(约束与红flag预调研)+Doodle(两阶段定日)+Expensify/Splitwise(报销)；迷你清单=总时间表+参会表+决策日志+最终议程。",
        "note": "适用：② 公司内部上下级场景（行政/HR 项目 owner 统筹多部门 offsite），「单一中枢+决策日志+预调研红flag题+静写降最大声赢」是可迁移工具纪律，补「议程/风险」之外的「计划执行不散架」底座。🔍 区别于卡片（议程模板/风险管理）——本卡是「协作工具链」这一执行操作系统。",
        "summary": "Offsite 工具栈：Notion 中枢+Airtable 预算供应商+Miro 工作坊(静写降最大声赢)+TravelPerk 差旅报销+SurveyMonkey 预调研红flag+Doodle 定日+Expensify 报销；迷你清单=时间表/参会表/决策日志/最终议程。",
        "quality": 4,
    },
    {
        "emoji": "👑", "cat": "新CEO务虚", "rel": "r3", "rel_label": "高管间",
        "title": "新 CEO 务虚·愿景共建 Retreat（百日计划 Phase2：与高管共创未来愿景 + 战略叙事）",
        "url": "https://www.vciinstitute.com/blog/charting-your-course-the-definitive-100-day-blueprint-for-new-ceos",
        "val": "新 CEO 前 100 天决定任期轨迹，offsite 是 Phase2（31-60 天）的关键动作：在听完一轮（1:1 直达下属、skip-level 挖关键人才、客户与董事对话）后，办一场「愿景共建 Retreat」与高管团队 co-create 未来愿景，而非单向宣布。要点：① 先诊断再共创——把 Days1-30 的倾听笔记合成 3-5 个撬动最大杠杆的优先项，先和领导团队 draft 100 天计划征求意见（早建 ownership）；② 愿景铸造 Retreat——facilitated offsite 让高管共同塑造「可信且共享」的未来画面，避免新 CEO 从旧公司照搬剧本；③ 战略叙事——用讲故事方式把愿景传遍组织（town hall/备忘录/视频/1:1 多通道），不抄前任；④ 早期人才审计——谁在状态/谁错位/能力缺口，retreat 后即做 tough call。符号学：早期动作（如给全员发手机、结束远程办公）的「象征意义」常与实质同等重要。新 CEO 务虚的坑：要么讨好所有人冻住、要么冲进来「我上家怎么做」——最关键是 aggressive listening + 早定 3-5 优先项 + 与团队共创而非宣布。",
        "exec_inner": "新 CEO 百日务虚：先 Days1-30 aggressive listening(1:1/skip-level/客户/董事)→Phase2(31-60)办愿景共建 Retreat 与高管 co-create 未来愿景(非宣布)→战略叙事多通道传播(不抄前任)→retreat 后即做人才审计 tough call；坑=讨好冻住或照搬旧剧本。",
        "note": "适用：③ 新任 CEO / 最高决策层务虚（接班/空降首 100 天），「百日 Phase2 愿景共建 Retreat + aggressive listening 先行 + 战略叙事多通道 + 人才审计」是可迁移新 CEO 落地框架，补既有「务虚会/转型 Retreat」之外「新 leader 上任首 100 天如何用 offsite 定调」这一场景。🔍 区别于卡片（转型/交接期 Retreat/新 leader 融入）——本卡是「新 CEO 视角（含象征意义/不抄前任/百日节奏）」，补「一把手上任」最高层场景。",
        "summary": "新 CEO 务虚：百日 Phase2 愿景共建 Retreat 与高管 co-create（非宣布）+ Days1-30 aggressive listening 先行 + 战略叙事多通道(不抄前任) + retreat 后即人才审计 tough call；坑=讨好冻住或照搬旧剧本。",
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
    hero_old = "2026-08-27 续·补采 +5（议程五块法/董事会retreat治理/家族董事会案例 + 新leader融入/90天onboarding）"
    hero_new = hero_old + " ｜ 2026-08-28 二十九轮补采 +5（中国法组织者责任/场地议价/场地选型矩阵/工具栈/新CEO愿景共建）"
    html = html.replace(hero_old, hero_new, 1)
    # tag 计数
    html = html.replace(">126 卡<", ">127 卡<", 1)
    html = html.replace(">81 卡<", ">85 卡<", 1)

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
    s = s.replace("（252 卡", "（257 卡", 1)
    s = s.replace("二手 248", "二手 253", 1)
    s = s.replace("卡片墙 HTML：", "｜ 2026-08-28 二十九轮补采 +5（中国法组织者责任/场地议价/场地选型矩阵/工具栈/新CEO愿景共建）卡片墙 HTML：", 1)
    r29_section = (
        "## 轮次 20260828·二十九轮（+5）\n\n"
        "| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n"
        "| 中国法下活动组织者安全保障义务（民法典1198条）+ 自甘风险（1176条）（offsite.html） | 上下级 | 二手 |\n"
        "| 场地议价 7 杠杆省 15-30%（offsite.html） | 上下级 | 二手 |\n"
        "| 场地选型评分矩阵（7 要素 / 20 点 MICE / 15 问）（offsite.html） | 上下级 | 二手 |\n"
        "| Offsite 工具栈：单一中枢 + 预算/供应商 + 工作坊 + 差旅 + 预调研 + 报销（offsite.html） | 上下级 | 二手 |\n"
        "| 新 CEO 务虚·愿景共建 Retreat（百日计划 Phase2）（offsite.html） | 高管间 | 二手 |\n\n"
    )
    s = s.replace("## 轮次 20260827·二十八轮（+14）", r29_section + "## 轮次 20260827·二十八轮（+14）", 1)
    open(OBS_SUM, "w", encoding="utf-8").write(s)
    print("[obs-sum] updated")

    # ---------- 5) 00 索引 ----------
    z = open(OBS_00, encoding="utf-8").read()
    z = z.replace("**252 卡**", "**257 卡**", 1)
    z = z.replace("③高管间 124 卡 / ②上下级 128 卡", "③高管间 125 卡 / ②上下级 132 卡", 1)
    z = z.replace("二手 248", "二手 253", 1)
    rows = (
        "| 中国法下活动组织者安全保障义务（民法典1198条）+自甘风险（1176条）（offsite.html） | 4 | 二手 | ②上下级 | 中文 offsite 组织者法定安保义务+自甘风险免参加者不免组织者+照护义务不可外包 |\n"
        "| 场地议价 7 杠杆省 15-30%（offsite.html） | 4 | 二手 | ②上下级 | 工作日/案例置换/打包/尾期价/回头客/3报价比价/谈extras不谈房价 |\n"
        "| 场地选型评分矩阵（7要素/20点MICE/15问）（offsite.html） | 4 | 二手 | ②上下级 | 评分矩阵替代只比价+MICE20点打分+关键项<3淘汰 |\n"
        "| Offsite 工具栈：单一中枢+预算/供应商+工作坊+差旅+预调研+报销（offsite.html） | 4 | 二手 | ②上下级 | Notion中枢/Airtable/Miro静写/TravelPerk/SurveyMonkey红flag/Doodle/Expensify |\n"
        "| 新 CEO 务虚·愿景共建 Retreat（百日计划Phase2）（offsite.html） | 4 | 二手 | ③高管间 | 新CEO首100天愿景共建offsite+aggressive listening+战略叙事+人才审计 |\n"
    )
    z = z.replace("| TADHUB·2026乐行-实验平台西双版纳团建游记（offsite.html）", rows + "| TADHUB·2026乐行-实验平台西双版纳团建游记（offsite.html）", 1)
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
        "title: Offsite-2026-08-28-第二十九轮-知识卡\n"
        "type: 自动化采集\n"
        "date: 2026-08-28\n"
        "tags: [知识采集, Offsite, 二十九轮]\n"
        "relation: [supervisor, exec]\n"
        "---\n\n"
        "# Offsite 团建务虚 · 第二十九轮补采（2026-08-28，+5）\n\n"
        "- **GitHub Pages 独立页**：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/offsite/runs/offsite-2026-08-28-r29.html\n"
        "- **本地路径**：`knowledge-collection/offsite/runs/offsite-2026-08-28-r29.html`\n"
        "- **累计卡片墙（总索引）**：`knowledge-collection/offsite/offsite.html`（[线上](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/offsite/offsite.html)）\n"
        f"- **覆盖关系档**：③高管间 {rel_counts['r3']} 卡 / ②上下级 {rel_counts['r2']} 卡（无①平级）\n"
        "- **乐享团队文件夹**：Offsite 子文件夹（463f5f5387de4a9bb87b773aef79767b，仅每轮独立页）\n\n"
        "## 本轮新增 5 卡\n\n"
        "| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n"
        "| 中国法下活动组织者安全保障义务（民法典1198条）+ 自甘风险（1176条） | 上下级 | 二手 |\n"
        "| 场地议价 7 杠杆省 15-30% | 上下级 | 二手 |\n"
        "| 场地选型评分矩阵（7 要素 / 20 点 MICE / 15 问） | 上下级 | 二手 |\n"
        "| Offsite 工具栈：单一中枢 + 预算/供应商 + 工作坊 + 差旅 + 预调研 + 报销 | 上下级 | 二手 |\n"
        "| 新 CEO 务虚·愿景共建 Retreat（百日计划 Phase2） | 高管间 | 二手 |\n\n"
        "> 本笔记仅索引，不拷 HTML 副本；完整卡片见上方 GitHub Pages 独立页。\n"
    )
    open(RUNS_NOTE, "w", encoding="utf-8").write(note)
    print("[runs-note] wrote", RUNS_NOTE)


if __name__ == "__main__":
    main()
