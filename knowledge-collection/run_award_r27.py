# -*- coding: utf-8 -*-
# 知识采集自动化 · 颁奖 第 27 轮（2026-08-28）
# 仅 ②上下级 / ③高管间，剔除 ①平级/朋友向。
import json, os, re, subprocess, sys, socket, urllib.request, ssl

KC   = r"C:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection"
AWARD = os.path.join(KC, "award")
VAULT = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库"
RUN_DATE = "2026-08-28"
ROUND_LABEL = "二十七轮 enrich 2026-08-28(+7)"
PREV_LABEL  = "二十六轮 enrich 2026-08-27(+9)"

def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

# ---------- 7 张新卡（均经六维评估、仅 ②/③） ----------
cards = [
 {
  "emoji":"🗳️","cat":"提名系统","rel":"supervisor","st":"二手",
  "title":"员工提名系统平台·端到端自动化（多轮审批/委员会投票/资格控制）",
  "val":"Awardco Nominations 把提名全生命周期从『表格+邮件+电子表格』碎片化流程，收进一个平台：配置提名项目（个人/团队/自荐/提名上限/按部门·成本中心设资格）、自定义问题（文本/附件/价值观标签）、多轮审查（审批轮=直通直属经理的 pass/fail gate；投票轮=指定评审按配额投票；委员会打分轮=rubric 引导）。领导力参与：把 leader 放进 voter review hub 做有效决策；提名即认可——提交时即通知候选人『被看见了』，不止最后赢家；庆祝所有提名人扩大文化势能。全球/跨职能：用 HRIS 元数据自动跑复杂资格规则，全球市场本地化履约。降偏见：清晰标准+结构化流程+资格控制+集中评审数据，减少『嗓门大/离领导近/好记』的偏见。",
  "how":"② HR/IT 落地：①别再用手动表格，用平台统一收提名→路由审查→多轮（审批/投票/委员会）→认可赢家与所有提名人；②用 HRIS 元数据设资格规则（部门/成本中心），自动路由到直属经理；③提名即发通知『被看见』，不止最后赢家，扩大参与；④委员会打分轮配 rubric 降主观；⑤全球团队用本地化履约。把评优从『行政苦差』变『文化引擎』。",
  "url":"https://www.awardco.com/ca/platform-features/nominations",
  "note":"② HR/IT：提名平台端到端自动化（多轮审批/委员会投票/资格控制/提名即认可/HRIS 履约），把评优从表格邮件搬进统一系统降偏见（二手·Awardco 平台文档）。"
 },
 {
  "emoji":"🔀","cat":"提名治理","rel":"supervisor","st":"二手",
  "title":"提名工作流治理·经理审批路由 + HR 治理 + 公平性分析（一线 SMS 可达）",
  "val":"Recognize 的提名工作流给 HR 完整治理、给员工极简提交：HR 控 badge/谁能提名/是否需经理或 HR 审批/是否带积分/正式或非正式；员工选 badge→写提名→提交，审批人（经理/HR/领导）在 Teams/邮件/Web 收到，无需手动追踪。为分布式与一线团队设计：覆盖 Teams/Outlook/移动端/SMS 登录，工地/诊所/门店/总部同样易用。管理后台可扩：审批流/badge 权限/可见性/积分预算/报表与审计轨迹。与 M365+HRIS 深度集成（Teams+Outlook、Azure AD SSO、Workday 用户同步、sFTP 自动更新），提名路由始终对齐真实汇报线。分析看『谁被提名/哪些行为值最多/各部门参与/经理参与与跟进』——帮 HR 确保公平且与战略对齐。",
  "how":"② HR/经理落地：①员工提交极简（选 badge+写提名），审批在 Teams/邮件自动流转，不追邮件；②一线员工用 SMS/移动端也能提名，覆盖门店工地；③用 M365+HRIS 集成让路由对齐真实汇报线，免手动维护；④管理后台控审批流/积分预算/审计轨迹；⑤用分析看『谁被提名/经理覆盖』，查公平漏洞。治理与易用并行。",
  "url":"https://recognizeapp.com/cms/articles/how-the-nomination-process-works-in-recognize",
  "note":"② HR/经理：提名工作流治理（经理审批路由+HR 治理+公平性分析+一线 SMS 可达+M365/HRIS 集成），降偏见扩参与（二手·Recognize 文档）。"
 },
 {
  "emoji":"📊","cat":"工具实操","rel":"supervisor","st":"二手",
  "title":"飞书落地优秀员工表彰·五阶段数字化（提名/投票/公示/专栏/开屏）",
  "val":"飞书实践模板把『优秀员工表彰』做成全员可达的数字化闭环：①提名征集——用多维表格表单/飞书问卷向各部门 Leader 收提名，一键触达；②投票评选——飞书问卷展示候选、设匿名填写、订阅号推全员；③结果公示——设飞书开屏界面跳链接，员工打开飞书即见；④表彰——订阅号发结果+材料；⑤设『优秀员工』专栏铺价值观宣传，传经验方法。解决传统邮件/群聊单向、信息分散、只有少数人知的问题，把表彰接成『企业文化塑造+经验分享』双价值。",
  "how":"② HR/行政落地（国内团队）：①用多维表格表单或飞书问卷向各部门 Leader 收提名，一键触达全员；②飞书问卷做投票、设匿名防刷；③飞书开屏+订阅号公示结果，打开即见增强仪式；④设『优秀员工』专栏持续铺价值观与经验；⑤把表彰从『一次活动』变『常态化文化运营』。轻量、零开发、可抄。",
  "url":"https://www.feishu.cn/practice_template/67492",
  "note":"② HR/行政：飞书五阶段数字化表彰（提名/投票/公示/专栏/开屏），国内团队零开发可抄，把表彰接成文化+经验双价值（二手·飞书实践模板）。"
 },
 {
  "emoji":"📋","cat":"工具实操","rel":"supervisor","st":"二手",
  "title":"简道云零代码表扬公示系统（提名→复核→公示→数据沉淀）",
  "val":"简道云零代码 OA 把『员工表扬公示』做成自动化流：任一员工发起表扬提名（填事迹+被表扬人），自动流转至直接上级或 HR 复核审批，通过后系统自动发布到内网公示栏/企业微信公告栏，后台自动统计月度/季度表扬次数与贡献类型，为年度评优供数据。优势：普通管理者 HR 零代码搭建、流程自定义（提名-审核-发布-公示）、模板一键套用快速迭代、数据实时统计辅助决策、多级权限与隐私控制、PC/手机多端+企微/钉钉集成。落地要点：明确表扬标准防主观、提名-审核-公示流程保公正透明、自动推送扩时效与广度、定期汇总成典型案例库、多元提名（自荐/互荐/领导提名）+专项表扬、结合物质精神激励+追踪成长。",
  "how":"② HR/管理者落地（国内）：①零代码搭表扬公示系统，员工发起→上级/HR 复核→自动公示→数据沉淀；②多级权限+隐私控制保合规；③后台自动统计表扬数据，接年度评优；④定期汇总成典型案例库；⑤多元提名（自荐/互荐/领导提名）+专项表扬。把表扬从『零散口头』变『可查可溯的数据资产』。",
  "url":"https://www.jiandaoyun.com/nblog/215975",
  "note":"② HR/管理者：简道云零代码表扬公示系统（提名→复核→公示→数据沉淀+权限隐私+多端），国内团队轻量落地、接年度评优（二手·简道云）。"
 },
 {
  "emoji":"💰","cat":"预算与ROI","rel":"supervisor","st":"二手",
  "title":"颁奖典礼预算配比·per-head 基准·ROI 倍数·12 周 timeline",
  "val":"颁奖之夜（awards night）预算配比（eventnest）：场地 18-25% / 餐饮 28-35% / AV灯光舞台 15-20% / AVP 制作 5-10% / 舞美设计 10-15% / 主持演艺 8-12% / 摄影摄像 5-8% / 奖杯证书 5-10% / 应急 10%。per-head 基准（bwproductions，含场地餐饮AV舞美制作）：颁奖典礼约 R900-1800/人，ROI 倍数 3.0-3.5x（低于 gala 的 3.5-4x，战略信号弱于品牌激活）。timeline：12 周前定日期/预算/委员会→10 周锁场地定主题→8 周开提名→6 周订摄影/主持/AV→5 周定餐饮→4 周关提名开始评审→3 周锁名单开始 AVP→2 周发正式邀请（含获奖者座位备注）→1 周技术彩排→前 2 天最终人数/证书质检/AV 备份。评选流程前置：明确提名标准+窗口+跨职能评审 panel+决策留痕+保密协议防泄漏+缺席替补，名单至少提前 3 周锁定给 AVP/刻字/家属协调留时间。",
  "how":"② 活动/行政落地：①按配比排预算（餐饮+场地+AV 占大头，奖杯线最易被低估，别省）；②用 per-head 基准（≈R900-1800/人或本地等价）做 cost ceiling，ROI 用 3-3.5x 做内部论证；③给 8-12 周 lead time，评选流程（提名/评审/保密/替补）必须在订场地前就位；④名单提前 3 周锁，给 AVP/刻字/家属留缓冲；⑤应急留 10%。把『花钱』讲成『可测算的留任/敬业投资』。",
  "url":"https://eventnest.ph/blog/planning-an-employee-recognition-or-awards-night/",
  "note":"② 活动/行政：颁奖之夜预算配比+per-head基准+ROI倍数(3-3.5x)+12周timeline+评选流程前置，把花钱讲成可测算投资（二手·Event Nest / B&W Productions）。"
 },
 {
  "emoji":"🏛️","cat":"荣誉体系·官方","rel":"exec","st":"一手",
  "title":"市属国企负责人荣誉体系·政府官方评选办法（精神为主/物质为辅）",
  "val":"嘉峪关市政府办印发《市属国有企业荣誉体系奖励评选办法》（一手·政府公开文件），把对国企负责人的荣誉表彰制度化：奖项设『优秀国有企业家/优秀国有企业/最具成长型国有企业/突出贡献国有企业』四类，对上交国有资本收益排名前 3 与同比增幅前 3 企业另设奖励。原则：公开公平公正、精神奖励为主物质为辅、争先创优树典范、激励创新促发展。奖励=精神（荣誉称号+奖金+奖牌证书），优秀企业家/最具成长型/优秀国企各奖 10 万、突出贡献国企奖 30 万；收益排名前 3 奖 7/5/3 万。优秀企业家表彰『对党忠诚/勇于创新/治企有方/兴企有为/清正廉洁』的经营管理者，每三年评一次、每次一般不超 2 名。把荣誉体系作为增强企业负责人职业荣誉感与责任感的治理工具。",
  "how":"③ 国资/组织/HR 落地（国企/大型组织）：①把对一把手的荣誉表彰写成正式办法，奖项分层（个人优秀企业家/组织优秀国企/成长型/突出贡献）；②定原则——精神为主物质为辅、公开公平、树典范；③设评选周期与名额上限（如每三年≤2 名）防通胀；④奖金与荣誉绑定，增强负责人职业荣誉感与责任感；⑤可用『上交收益排名』等硬指标挂钩，导向清晰。把『评优』当治理杠杆而非年终仪式。",
  "url":"https://jyg.gov.cn/zfxxgk/fdzdgknr/zfgb/wqzfgb/2020n5yzfgb/art/2022/art_25819aac7f4449768a3a7db607ce7944.html",
  "note":"③ 国资/组织/HR：市属国企负责人荣誉体系官方办法（四类奖+精神为主物质为辅+每三年≤2名），把对一把手表彰当治理杠杆（一手·嘉峪关市政府公开文件）。"
 },
 {
  "emoji":"🎖️","cat":"荣休仪式","rel":"supervisor","st":"二手",
  "title":"荣休仪式「五个一」暖心流程（家属绶带+工龄纪念章+手写感谢信+全家福+上门荣休）",
  "val":"赛诺美『五个一』荣休方案把退休欢送做成有温度的荣誉时刻：①家属戴绶带+家人拥抱——配偶/子女上台佩『光荣退休』绶带，无家属由密友同事代；②徒弟/同事献花+祝福卡——花束内插部门手写祝福；③领导颁发纪念章——章与工龄挂钩，15年银底『感谢十五载』/20年金底『感谢二十载』/30年金底『感谢三十载风雨同行』差异化尊重，领导同时送睡眠枕+手写贺卡『夜夜好眠，身心安顿』；④致辞不说套话——主要领导讲一个故事或读手写感谢信，赠每位退休职工；⑤合影全家福——领导/家属/同事合影制相框赠留念。后续：活动照片视频发每人；未到场者上门荣休（绶带/花/章/枕/卡），『退休不脱钩、关爱不断线』；建常态化荣休机制（当年退休·当年仪式·当年上门）。",
  "how":"② 工会/HR/领导落地：①荣休是『荣誉表彰』的延伸，别只发纪念品合影了事；②用『五个一』结构化温暖——家属绶带+徒弟献花+领导颁工龄纪念章（15/20/30 年差异化）+手写感谢信+全家福；③领导致辞讲真实故事/读手写信，忌套话；④未到场者上门荣休，覆盖全；⑤建常态化机制（当年退休当年仪式）。把『退场』变成『被郑重看见』。",
  "url":"https://www.xianceremony.com/fangan/1422",
  "note":"② 工会/HR/领导：荣休『五个一』暖心流程（家属绶带+徒弟献花+工龄纪念章差异化+手写感谢信+全家福+上门荣休），把退场变被郑重看见（二手·赛诺美活动策划）。"
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

# ---------- Step 2. gen_run_page.py → runs/award-2026-08-28-r27.html ----------
run_page = os.path.join(AWARD, "runs", "award-2026-08-28-r27.html")
r = subprocess.run(
    [sys.executable, os.path.join(KC, "gen_run_page.py"),
     "--topic", "award", "--topic-name", "颁奖典礼·荣誉表彰",
     "--date", RUN_DATE, "--round", "27", "--cards-file", tmp,
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
note = note.replace("共 168 张","共 %d 张" % (168+N), 1)

round_sec = (
"## 轮次 2026-08-28（+%d）\n" % N +
"本轮新增（均通过六维评估、仅 ②上下级 / ③高管间）：\n"
)
for c in cards:
    rel_txt = "③高管间" if c["rel"]=="exec" else "②上下级"
    round_sec += "- "+c["title"]+"（award/award.html） | "+rel_txt+" | "+c["st"]+"\n"
note = note.replace("## 轮次 2026-08-27（+9）", round_sec+"## 轮次 2026-08-27（+9）", 1)

rows=""
for c in cards:
    rel_cell = "③高管间" if c["rel"]=="exec" else "②上下级"
    rows += "| "+c["title"]+"（award/award.html） | 4 | "+c["st"]+" | "+rel_cell+" |  |\n"
note = note.replace("## 线上卡片墙（GitHub Pages）", rows+"## 线上卡片墙（GitHub Pages）", 1)

inc_link = "- 本轮增量页（二十七轮·2026-08-28）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/runs/award-2026-08-28-r27.html"
note = note.replace("## 线上卡片墙（GitHub Pages）", inc_link+"\n## 线上卡片墙（GitHub Pages）", 1)
open(note_path,"w",encoding="utf-8").write(note)
print("UPDATED obsidian note (共 %d 张)" % (168+N))

# ---------- Step 6. 00-知识采集索引.md ----------
idx00 = open(os.path.join(VAULT,"00-知识采集索引.md"), encoding="utf-8").read()
# 修正过期头部计数（实际墙 168 + 本轮 N）→ 175
idx00 = idx00.replace("**178 卡**", "**%d 卡**" % (168+N), 1)
openday_nav = "📄 主题汇总笔记：[[知识采集库/素材/openday/OpenDay-开放日-知识卡汇总|OpenDay-开放日-知识卡汇总]]"
assert idx00.count(openday_nav)>=1
zrows=""
for c in cards:
    rel_cell = "③高管间" if c["rel"]=="exec" else "②上下级"
    zrows += "| "+c["title"]+"（award/award.html） | 4 | "+c["st"]+" | "+rel_cell+" |  |\n"
idx00 = idx00.replace(openday_nav, zrows+openday_nav, 1)
open(os.path.join(VAULT,"00-知识采集索引.md"),"w",encoding="utf-8").write(idx00)
print("UPDATED 00-index")

# ---------- Step 7. lexiang-entry-map.json ----------
map_path = os.path.join(KC, "lexiang-entry-map.json")
mp = json.load(open(map_path, encoding="utf-8"))
award_map = mp["award"]
award_map["rounds"].append({
  "date": RUN_DATE,
  "entry_id": None,
  "name": "award-2026-08-28-r27.html",
  "note": "轮次页 R27 (+%d：提名平台端到端自动化/提名工作流治理/飞书五阶段表彰/简道云表扬公示/颁奖预算ROI+12周timeline/市属国企负责人荣誉体系官方办法/荣休五个一)｜乐享待补传(token 过期/断开，待重连后补传并回填 entry_id)" % N
})
json.dump(mp, open(map_path,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
print("UPDATED lexiang-entry-map.json (round R27 appended, entry_id=null)")

# ---------- Step 8. 乐享 best-effort whoami 探活（不阻断） ----------
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
        # initialize
        body=json.dumps({"jsonrpc":"2.0","id":1,"method":"initialize","params":{
            "protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"kb-auto","version":"1.0"}}}).encode()
        req=urllib.request.Request(url, data=body, headers={
            "Content-Type":"application/json","Accept":"application/json, text/event-stream",
            "Authorization":tok})
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            resp.read()
        # notifications/initialized
        body2=json.dumps({"jsonrpc":"2.0","method":"notifications/initialized"}).encode()
        req2=urllib.request.Request(url, data=body2, headers={
            "Content-Type":"application/json","Accept":"application/json, text/event-stream",
            "Authorization":tok})
        try:
            urllib.request.urlopen(req2, timeout=15, context=ctx).read()
        except Exception:
            pass
        # whoami
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

print("DONE R27 | 新增 N=%d 删除 M=%d | 墙=%d卡 | 独立页=%s" % (N, M, after, run_page))
