# -*- coding: utf-8 -*-
# 知识采集自动化 · 颁奖 第 28 轮（2026-09-01）
# 仅 ②上下级 / ③高管间，剔除 ①平级/朋友向。
import json, os, re, subprocess, sys, socket, urllib.request, ssl

KC   = r"C:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection"
AWARD = os.path.join(KC, "award")
VAULT = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库"
RUN_DATE = "2026-09-01"
ROUND_LABEL = "二十八轮 enrich 2026-09-01(+6)"
PREV_LABEL  = "二十七轮 enrich 2026-08-28(+7)"

def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

# ---------- 6 张新卡（均经六维评估、仅 ②/③） ----------
cards = [
 {
  "emoji":"⚖️","cat":"公平性治理","rel":"supervisor","st":"二手",
  "title":"公平提名流程·10 步可落地框架（资格标准/多通道/独立评审团/匿名/评分量规/利益冲突/迭代反馈）",
  "val":"Nominee.app 实操框架——把公平性设计进提名每一步：①定义清晰资格与可观测标准（用『协作过≥2 个跨职能项目』替代『团队 player』）；②多提名通道（网页表单+邮件+Slack/Teams 集成）降摩擦、跨通道收同一结构化数据；③表单结构化但宽容（提名人/角色/类别/影响例证/佐证链接，必填校验但不劝退）；④主动推广扩多样提名（鼓励经理/同侪跨团队跨层级提名、做无意识偏见培训）；⑤组建独立多元评审团（多部门多资历轮换、配 rubric 与匿名提交）；⑥适当匿名降偏见（按结果/叙事评判的类别适用）；⑦公开评分量规（每条标准 0-10 数值，提名前就公开）；⑧公开 timeline 与反馈（提名/评审/公布窗口，事后给聚合反馈说明标准）；⑨利益冲突回避（评委对关联提名声明并回避，留记录）；⑩每轮收匿名反馈迭代（把流程当产品打磨）。核心：公平不是终点而是实践，透明+无障碍+清晰标准=认可『应得』、参与成习惯。",
  "how":"② HR/委员会落地：①先写『谁可被提名+凭什么』（可观测标准，废话指标全删）；②开≥2 通道（表单+IM 集成）让提名零摩擦；③评审团必须多元且轮换，配 rubric；④评前就公开量规，评审用数值打分；⑤利益冲突书面回避留痕；⑥每轮结束发匿名问卷迭代。把『公平』从口号变可审计的流程。",
  "url":"https://nominee.app/how-to-run-a-fair-nomination-process",
  "note":"② HR/委员会：公平提名 10 步框架（清晰资格/多通道/独立多元评审/匿名/公开量规/利益冲突回避/迭代反馈），把公平设计进流程每一步（二手·Nominee.app 实操指南）。"
 },
 {
  "emoji":"🧾","cat":"奖项治理","rel":"supervisor","st":"二手",
  "title":"奖项项目治理·全周期审计追踪（治理owner/版本控制/决策链/合规导出）",
  "val":"RQ Awards 治理框架——奖项缺治理信任崩得快：72% 员工认为认可公平度影响对领导的信任 3 倍于其他因素；决策清晰可解释时再参与率 3 倍。全周期透明：①设计期——标准/量规/权重在开放前文档化并留版本历史（含时间戳+审批人）；②提名期——记录谁提交/何时/哪个渠道，每次编辑/撤回/管理员覆盖带原因码；③评审期——每位评审的分数/评论/利益冲突声明留痕，匿名评审的解除屏蔽事件也记录，分数不可无主；④决策期——多级审批生成清晰监管链（谁批准/谁升级/何时签署），挂每条记录而非邮件；⑤公布后——获奖/入围/淘汰各有可检索理由，事后审计轻松。选型要点：自动防篡改时间戳、基于角色的访问日志、可导出审计报表、量规版本控制、利益冲突标记与回避跟踪、跨项目统一治理视图。设『治理负责人』一人对审计就绪负责；退邮件审批、改平台留痕；每轮做 30 分钟事后审计。",
  "how":"② 项目/合规落地：①给每个奖项设唯一『治理负责人』对审计就绪负责；②标准/量规开放前就文档化并锁版本（改要留痕）；③提名/评审/决策全程平台留痕（谁/何时/为何），别走邮件；④多级审批生成监管链挂记录；⑤每轮结束做 30 分钟事后审计。治理不是开销是竞争力——参与更敢提名、领导更信结果。",
  "url":"https://rqawards.com/program-governance-101-building-audit-trails-and-transparency-into-every-stage",
  "note":"② 项目/合规：奖项治理全周期审计追踪（治理owner/版本控制/决策链/可导出报表/利益冲突追踪），72%员工认为公平影响对领导信任3倍，把治理变竞争力（二手·RQ Awards）。"
 },
 {
  "emoji":"🧠","cat":"评审防偏见","rel":"exec","st":"一手",
  "title":"评审隐性偏见防控·政府官方指南（委员会多样性/先列名单/避免标准漂移/利益冲突）",
  "val":"澳大利亚总理科学奖《多样性管理指南》（一手·政府公开文件）为评选委员会提供降隐性偏见的标准做法：背景——研究证实女性获奖率与提名数/学科占比不匹配，隐性偏见是主因，委员会要求每年评审前审读该简报。①委员会构成——更 diverse 的群体决策更好，按政府董事会多样性目标 40/40/20 性别平衡并鼓励其他多样性；②鼓励提名——多通道广泛推广、直接触达代表性不足群体；③年度复审资格准则消除障碍；④公开标准与截止日增透明包容；⑤评审原则——讨论前先对齐属性优先级（防『标准漂移』）、听他人建议前先列个人 Top 名单（防单一成员过度影响）、给每候选人按 merit 而非找理由剔除、会前书面打分排名、确保每人发声、留足时间反思；⑥利益冲突——委员与候选人有关联须声明，被提名须退出委员会。把『公平』写成可执行的评审纪律。",
  "how":"③ 评审/治理落地（高管/政府/大型评审）：①评审委员会按 40/40/20 性别平衡并扩多样性，每年审读防偏见简报；②讨论前先对齐评分属性防『标准漂移』，听人建议前各自先列 Top 名单；③会前书面打分排名，确保每人发声、留足反思时间；④利益冲突书面声明+被提名者退委员会。把『公平评选』当纪律而非善意。",
  "url":"https://www.industry.gov.au/funding-and-incentives/science-and-research/science-and-research/prime-ministers-prizes-for-science/prime-ministers-prizes-for-science-guidelines-for-managing-diversity",
  "note":"③ 评审/治理：评审隐性偏见防控官方指南（委员会40/40/20多样性/先列个人Top名单防从众/避免标准漂移/利益冲突退委员会），把公平写成评审纪律（一手·澳总理科学奖政府指南）。"
 },
 {
  "emoji":"🎬","cat":"影像制作","rel":"supervisor","st":"二手",
  "title":"颁奖影像/AVP 制作策略·类型拆解 + 拍摄规划 + 二次利用（高管远程同框/蒙太奇/获奖者特写）",
  "val":"颁奖视频制作类型（Vivid Snaps / Firebrand Media 实操）：①员工感谢/表彰视频——混剪获奖者工作场景+其他机构素材，可做成 45 分钟预录直播流；②年度蒙太奇——黑金主题用获奖者肖像照做庆典视频（省拍摄、用既有职业照）；③提名视频——讲业务独特卖点，字幕+文字叠层；④获奖者特写——动态排版动画+活动摄影+办公室访谈，金句激励后人；⑤祝贺视频——提词器让领导直视镜头，叠 logo+字幕；⑥高管远程同框——多地远程拍摄+剪辑把全球获奖者拼进无缝视频；⑦绿幕/直播——混合式颁奖直播。企业颁奖活动视频规划（Firebrand）：仪式常 45 分–1.5 小时，须备足电源（假电池直插）+半 TB 数据卡+备用机位防中断；拍舞台全景/获奖者特写/品牌背景板合影/观众反应；成片可剪成 sizzle reel/recap 做内宣与士气素材，延长仪式影响。案例：倍思年度表彰用创意开场视频（谐音梗揭主题）+ CEO 年度主题分享《从平庸到卓越》+ 三篇章串讲人 + 19 团队/116 个人表彰，把颁奖接成战略传播。",
  "how":"② 活动/品牌落地：①按目的选视频类型（感谢混剪/蒙太奇/获奖者特写/高管远程同框/直播）；②长仪式备足电源+大容量卡+多机位，防中断、多视角；③拍舞台+特写+品牌板合影+观众反应四类镜头；④成片剪 sizzle reel 做内宣延长影响；⑤高管异地用远程拍摄拼无缝视频。把『影像』当战略传播资产而非记录。",
  "url":"https://www.vividsnaps.com/awards-video-production-singapore",
  "note":"② 活动/品牌：颁奖影像/AVP 制作策略（7类视频+长仪式拍摄规划+二次利用sizzle reel+高管远程同框），把影像当战略传播资产（二手·Vivid Snaps / Firebrand Media；含倍思年度表彰案例）。"
 },
 {
  "emoji":"🏛️","cat":"高管治理奖项","rel":"exec","st":"二手",
  "title":"董事会/高管治理类奖项设计·NACD Directorship 100（类别/独立评选委员会/推荐信/评分准则）",
  "val":"全美董事协会（NACD）Directorship 100 是表彰董事、CEO 与治理专业人士的权威奖项（二手·权威机构）：①奖项类别——终身成就奖（B.Kenneth West）、上市公司/私企/非营利董事 of the Year、治理专业人士等，聚焦『对董事会的实质影响』；②评选资格——董事须展现诚信/成熟自信/明智判断/高绩效标准，治理专业人士须有近期（24–36 月）实质贡献；③提名包——完整提名表+简历+≥3 封同行推荐信（来自共事过的董事/高管权重最高），阐明如何体现董事职业四大标准；④评选流程——外部独立评选委员会（由往届获奖者组成、强调独立与思想多样性）按定性+定量标准打分，再报 NACD 董事会终审，全程保密；⑤治理意义——把『董事会领导力』制度化表彰，树立治理标杆、激励继任梯队。启示：给一把手工高管设治理类荣誉时，须用独立委员会+多封同行推荐+保密评选+明确评分准则，避免『内部人自嗨』。",
  "how":"③ 治理/薪酬委员会落地（表彰董事/CEO/治理高管）：①设独立外部评选委员会（往届获奖者+思想多样性），不内部人自定；②提名包含≥3 封同行推荐信（共事过的董事/高管权重最高）；③按『诚信/明智判断/高绩效/近期实质贡献』打分，报董事会终审，全程保密；④把『董事会领导力』制度化表彰，树标杆激励继任。高管治理奖项最忌自嗨，须独立+透明+保密。",
  "url":"https://www.nacdonline.org/about/nacd-directorship-100/awards-descriptions/",
  "note":"③ 治理/薪酬委员会：董事会/高管治理类奖项设计（NACD Directorship 100：独立评选委员会+≥3同行推荐信+保密终审+评分准则），高管荣誉最忌自嗨须独立透明（二手·NACD 权威机构）。"
 },
 {
  "emoji":"📋","cat":"外部表彰合规","rel":"supervisor","st":"一手",
  "title":"社会组织评比表彰合规办法·政府规章（自主申报/公示/征求意见/备案/禁收费禁党政机关）",
  "val":"韶关市政府门户《社会组织评比表彰活动管理办法》（一手·政府规章）对『社会组织办评比表彰』设硬约束，对 externally-facing 表彰合规有借鉴：①参评方式——自主申报或推荐，推荐须适当范围公示无异议后上报评审；②征求意见——审慎核查资格/声誉，通过全国信用信息共享平台查违法失信/行政处罚，可要求专项信用报告，涉企业负责人征求人社/生态环境/应急管理/税务/市场监管/金融监管意见，涉党政机关工作人员征求组织人事+纪检监察；③公示——形成拟表彰名单向社会公示，无异议后确定；④决定——发布决定、颁奖牌章证书；⑤备案——结束后 10 个工作日内报业务主管单位备案。禁止性规定：不得面向各级党委政府或党政机关开展；一般不以党政机关领导干部/事业单位领导人员为评选对象；不得与营利性组织合作或委托其开展；不得超章程宗旨业务范围；不得收取或变相收取任何费用；全国性不得要求地方性配套，地方性不得借全国性新增项目。对办对外/行业表彰的 HR：合规红线=公示+信用核查+征求意见+备案+不收费不合作营利方。",
  "how":"② HR/合规落地（办对外/行业表彰时）：①参评自主申报或推荐，推荐须公示；②用全国信用平台查违法失信，涉企业/党政征求对应主管部门意见；③拟表彰名单向社会公示无异议后定；④结束后 10 个工作日内备案；⑤红线：不面向党政机关、不收费、不与营利方合作、不超章程范围。把『合规』前置别事后被整改。",
  "url":"https://www.sg.gov.cn/bmpdlm/mzj/ywgz/content/post_2867250.html",
  "note":"② HR/合规：社会组织评比表彰合规办法（自主申报/公示/信用核查/征求意见/10日备案+禁收费禁党政机关禁营利合作），对外表彰合规红线（一手·韶关市政府规章）。"
 },
]

def rel_badges(rel):
    out=""
    if "exec" in rel:
        out+='<span class="badge r3">高管间</span>'
    if "supervisor" in rel:
        out+='<span class="badge r2">上下级</span>'
    return out

def card_html(c):
    return (
      '    <div class="hl">\n'
      '      <div class="top"><span class="emoji">'+esc(c["emoji"])+'</span><h3>'+esc(c["title"])+'</h3>'
      '<span class="cat">'+esc(c["cat"])+'</span>'+rel_badges(c["rel"])+'<span class="badge b2">'+esc(c["st"])+'</span></div>\n'
      '      <p class="val">'+esc(c["val"])+'</p>\n'
      '      <details class="exec"><summary>怎么做</summary><div class="inner">'+esc(c["how"])+'</div></details>\n'
      '      <div class="src">🔗 <a href="'+esc(c["url"])+'" target="_blank">'+esc(c["url"])+'</a></div>\n'
      '      <div class="note">适用：'+esc(c["note"])+'</div>\n'
      '    </div>\n'
    )

# ---------- 基础计数 ----------
exec_cards = [c for c in cards if "exec" in c["rel"]]
sup_cards  = [c for c in cards if "supervisor" in c["rel"]]
n_exec=len(exec_cards); n_sup=len(sup_cards)
assert n_exec + n_sup == len(cards), "card count mismatch"

# ---------- Step 1. 写入 .run_newcards.tmp.html（供 gen_run_page.py） ----------
tmp = os.path.join(AWARD, ".run_newcards.tmp.html")
with open(tmp, "w", encoding="utf-8") as f:
    for c in cards:
        f.write(card_html(c))
print("WROTE tmp newcards:", tmp, len(cards), "cards")

# ---------- Step 2. gen_run_page.py → runs/award-2026-09-01-r28.html ----------
run_page = os.path.join(AWARD, "runs", "award-2026-09-01-r28.html")
r = subprocess.run(
    [sys.executable, os.path.join(KC, "gen_run_page.py"),
     "--topic", "award", "--topic-name", "颁奖典礼·荣誉表彰",
     "--date", RUN_DATE, "--round", "28", "--cards-file", tmp,
     "--out", run_page],
    cwd=KC, capture_output=True, text=True, timeout=120)
print("GEN RUN PAGE rc=", r.returncode, r.stdout.strip(), r.stderr.strip()[:200])
assert os.path.isfile(run_page), "run page not generated"

# ---------- Step 3. 更新累计墙 award.html ----------
wall = open(os.path.join(AWARD,"award.html"), encoding="utf-8").read()
before = wall.count('class="hl"')
exec_frag = "".join(card_html(c) for c in exec_cards)
sup_frag  = "".join(card_html(c) for c in sup_cards)

assert wall.count('  <div class="sec sec2">')==1, "sec2 marker not unique"
wall = wall.replace('  <div class="sec sec2">', '  '+exec_frag+'  <div class="sec sec2">', 1)

parts = wall.split('<footer>', 1)
assert len(parts)==2, "footer marker not found"
wall = parts[0] + sup_frag + '<footer>' + parts[1]

assert PREV_LABEL in wall, "prev round label not found in hero"
wall = wall.replace(PREV_LABEL, PREV_LABEL+' ｜ '+ROUND_LABEL, 1)

open(os.path.join(AWARD,"award.html"),"w",encoding="utf-8").write(wall)
after = wall.count('class="hl"')
print("UPDATED wall award.html: hl %d -> %d (added %d)" % (before, after, after-before))

# ---------- Step 4. index.json ----------
idx = json.load(open(os.path.join(KC,"index.json"), encoding="utf-8"))
existing_urls = {x.get("url","") for x in idx if isinstance(x,dict)}
new_entries=[]
for c in cards:
    if c["url"] in existing_urls:
        print("SKIP dup url:", c["url"]); continue
    e={
      "title": c["title"],
      "normKey": c["title"],
      "url": c["url"],
      "sourceType": "secondary" if c["st"]=="二手" else "primary",
      "relation": c["rel"],
      "summary": c["val"][:120],
      "topic": "award",
      "dateCollected": RUN_DATE
    }
    idx.append(e); new_entries.append(e)
json.dump(idx, open(os.path.join(KC,"index.json"),"w",encoding="utf-8"), ensure_ascii=False, indent=2)
print("UPDATED index.json (+%d) total=%d" % (len(new_entries), len(idx)))
N = len(new_entries); M = len(cards) - N
print("去重: 新增 N=%d, 删/跳过 M=%d" % (N, M))

# ---------- Step 5. Obsidian 汇总笔记 ----------
note_path = os.path.join(VAULT,"素材","award","颁奖-知识卡汇总.md")
note = open(note_path, encoding="utf-8").read()
note = note.replace("共 175 张","共 %d 张" % (175+N), 1)

round_sec = (
"## 轮次 2026-09-01（+%d）\n" % N +
"本轮新增（均通过六维评估、仅 ②上下级 / ③高管间）：\n"
)
for c in cards:
    rel_txt = "③高管间" if c["rel"]=="exec" else "②上下级"
    round_sec += "- "+c["title"]+"（award/award.html） | "+rel_txt+" | "+c["st"]+"\n"
note = note.replace("## 轮次 2026-08-28（+7）", round_sec+"## 轮次 2026-08-28（+7）", 1)

rows=""
for c in cards:
    rel_cell = "③高管间" if c["rel"]=="exec" else "②上下级"
    rows += "| "+c["title"]+"（award/award.html） | 4 | "+c["st"]+" | "+rel_cell+" |  |\n"
note = note.replace("## 线上卡片墙（GitHub Pages）", rows+"## 线上卡片墙（GitHub Pages）", 1)

inc_link = "- 本轮增量页（二十八轮·2026-09-01）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/runs/award-2026-09-01-r28.html"
note = note.replace("## 线上卡片墙（GitHub Pages）", inc_link+"\n## 线上卡片墙（GitHub Pages）", 1)
open(note_path,"w",encoding="utf-8").write(note)
print("UPDATED obsidian note (共 %d 张)" % (175+N))

# ---------- Step 6. 00-知识采集索引.md ----------
idx00 = open(os.path.join(VAULT,"00-知识采集索引.md"), encoding="utf-8").read()
idx00 = idx00.replace("**175 卡**", "**%d 卡**" % (175+N), 1)
openday_nav = "📄 主题汇总笔记：[[知识采集库/素材/openday/OpenDay-开放日-知识卡汇总|OpenDay-开放日-知识卡汇总]]"
assert idx00.count(openday_nav)>=1
zrows=""
for c in cards:
    rel_cell = "③高管间" if c["rel"]=="exec" else "②上下级"
    zrows += "| "+c["title"]+"（award/award.html） | 4 | "+c["st"]+" | "+rel_cell+" |  |\n"
idx00 = idx00.replace(openday_nav, zrows+openday_nav, 1)
open(os.path.join(VAULT,"00-知识采集索引.md"),"w",encoding="utf-8").write(idx00)
print("UPDATED 00-index")

# ---------- Step 7. runs 独立笔记（本轮独立笔记，仅索引不拷 HTML） ----------
runs_note_path = os.path.join(VAULT,"素材","award","runs","颁奖-2026-09-01-第二十八轮-知识卡.md")
os.makedirs(os.path.dirname(runs_note_path), exist_ok=True)
rel_rows=""
for c in cards:
    rel_cell = "高管间" if c["rel"]=="exec" else "上下级"
    rel_rows += "| "+c["title"]+" | "+rel_cell+" | "+c["st"]+" |\n"
runs_note = (
"---\n"
"title: 颁奖-2026-09-01-第二十八轮-知识卡\n"
"type: 自动化采集\n"
"date: 2026-09-01\n"
"tags: [知识采集, 颁奖, 二十八轮]\n"
"relation: [supervisor, exec]\n"
"---\n\n"
"# 颁奖典礼 · 第二十八轮补采（2026-09-01，+%d）\n\n" % N +
"- **GitHub Pages 独立页**：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/runs/award-2026-09-01-r28.html\n"
"- **本地路径**：`knowledge-collection/award/runs/award-2026-09-01-r28.html`\n"
"- **累计卡片墙（总索引）**：`knowledge-collection/award/award.html`（[线上](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/award.html)）\n"
"- **覆盖关系档**：③高管间 %d 卡 / ②上下级 %d 卡（无①平级）\n\n" % (n_exec, n_sup) +
"## 本轮新增 %d 卡\n\n" % N +
"| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n" +
rel_rows +
"\n> 本笔记仅索引，不拷 HTML 副本；完整卡片见上方 GitHub Pages 独立页。\n"
)
open(runs_note_path,"w",encoding="utf-8").write(runs_note)
print("WROTE runs note:", runs_note_path)

# ---------- Step 8. lexiang-entry-map.json ----------
map_path = os.path.join(KC, "lexiang-entry-map.json")
mp = json.load(open(map_path, encoding="utf-8"))
award_map = mp["award"]
award_map["rounds"].append({
  "date": RUN_DATE,
  "entry_id": None,
  "name": "award-2026-09-01-r28.html",
  "note": "轮次页 R28 (+%d：公平提名10步框架/奖项治理全周期审计追踪/评审隐性偏见防控政府指南/颁奖影像AVP制作策略/NACD董事会高管治理奖项/社会组织评比表彰合规办法)｜乐享待补传(token 过期/断开，待重连后补传并回填 entry_id)" % N
})
json.dump(mp, open(map_path,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
print("UPDATED lexiang-entry-map.json (round R28 appended, entry_id=null)")

# ---------- Step 9. 乐享 best-effort whoami 探活（不阻断） ----------
def lexiang_probe():
    try:
        token_path = r"C:\Users\v_yitcai\.workbuddy\mcp.json"
        if not os.path.isfile(token_path):
            return False, "mcp.json 不存在"
        cfg = json.load(open(token_path, encoding="utf-8"))
        tok=None
        for s in cfg.get("mcpServers",{}).values():
            if "lexiang" in (s.get("name","")+s.get("url","")+str(s.get("env",""))).lower():
                env=s.get("env",{})
                tok=env.get("LEXIANG_TOKEN") or env.get("lxmcp_token") or env.get("AUTHORIZATION","")
                if tok and not tok.startswith("Bearer "): tok="Bearer "+tok
                break
        if not tok:
            return False, "未找到 lexiang token"
        url="https://mcp.lexiang-app.com/mcp?company_from=csig"
        ctx=ssl.create_default_context(); ctx.check_hostname=False; ctx.verify_mode=ssl.CERT_NONE
        body=json.dumps({"jsonrpc":"2.0","id":1,"method":"initialize","params":{
            "protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"kb-auto","version":"1.0"}}}).encode()
        req=urllib.request.Request(url, data=body, headers={
            "Content-Type":"application/json","Accept":"application/json, text/event-stream",
            "Authorization":tok})
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            resp.read()
        body2=json.dumps({"jsonrpc":"2.0","method":"notifications/initialized"}).encode()
        req2=urllib.request.Request(url, data=body2, headers={
            "Content-Type":"application/json","Accept":"application/json, text/event-stream",
            "Authorization":tok})
        try:
            urllib.request.urlopen(req2, timeout=15, context=ctx).read()
        except Exception:
            pass
        body3=json.dumps({"jsonrpc":"2.0","id":2,"method":"tools/call","params":{
            "name":"whoami","arguments":{}}}).encode()
        req3=urllib.request.Request(url, data=body3, headers={
            "Content-Type":"application/json","Accept":"application/json, text/event-stream",
            "Authorization":tok})
        with urllib.request.urlopen(req3, timeout=15, context=ctx) as resp:
            data=resp.read().decode("utf-8","replace")
        return True, data[:200]
    except Exception as e:
        return False, "%s: %s" % (type(e).__name__, str(e)[:150])

ok, info = lexiang_probe()
print("LEXIANG PROBE:", "OK" if ok else "FAIL", info)
if ok:
    print("⚠️ 乐享 whoami 通，但本次自动化未内置上传实现，按既有惯例记录待补传。")
else:
    print("⚠️ 乐享未连通（token 过期/断开），按规约告警跳过，不阻断主流程；entry_id 留 null 待重连补传。")

print("DONE R28 | 新增 N=%d 删除 M=%d | 墙=%d卡 | 独立页=%s" % (N, M, after, run_page))
