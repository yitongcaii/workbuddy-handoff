# -*- coding: utf-8 -*-
# 知识采集自动化 · 颁奖 第 29 轮（2026-09-02）
# 仅 ②上下级 / ③高管间，剔除 ①平级/朋友向。
import json, os, re, subprocess, sys, socket, urllib.request, ssl

KC   = r"C:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection"
AWARD = os.path.join(KC, "award")
VAULT = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库"
RUN_DATE = "2026-09-02"
ROUND_LABEL = "二十九轮 enrich 2026-09-02(+7)"
PREV_LABEL  = "二十八轮 enrich 2026-09-01(+6)"
BASE = 181  # 当前墙卡数（hl count）

def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

# ---------- 7 张新卡（均经六维评估、仅 ②/③；URL 全部已校验未在 index） ----------
cards = [
 {
  "emoji":"💰","cat":"税务合规","rel":"supervisor","st":"一手",
  "title":"颁奖奖金/实物个税代扣合规·税务局官方口径（现金/实物并入工资薪金、证书奖杯鲜花不代扣、偶然所得区分）",
  "val":"国家税务总局西藏/广东税务局公开答复——企业以现金、实物、有价证券及其他形式经济利益奖励员工，均按『工资薪金所得』并入当期收入计征个税：①现金/购物卡等奖金——并入工资薪金，企业作为扣缴义务人全员全额扣缴；②实物奖品——按凭证注明价格（无凭证或偏低则参照市场价）核定应纳税所得额并入工资薪金；③荣誉证书/奖杯/奖牌/鲜花——纯精神性表彰物、无经济利益的，不征个税（广东惠州税务明确『荣誉证书、奖杯、奖牌、鲜花不需要扣缴个税』）；④年会/庆典向『本单位以外个人』随机赠送礼品——按『偶然所得』20% 由企业代扣代缴（与员工区分）。实操红线：发钱发物必计税、纯荣誉物可免责、给外部人士走偶然所得。把合规前置，别事后被税务约谈。",
  "how":"② HR/薪酬/财务落地：①奖金/购物卡/实物奖品——一律并入工资薪金、走全员全额扣缴，实物按凭证价或市场价核定；②奖杯/证书/鲜花等纯荣誉物——留存『无经济利益』定性，不代扣（留官方答复依据备查）；③年会向客户/外部人士抽奖赠礼——单独按偶然所得 20% 代扣；④建《表彰发放税务判定表》区分三类，避免一刀切多缴或少缴。",
  "url":"https://xizang.chinatax.gov.cn/art/2018/6/19/art_5347_228937.html",
  "note":"② HR/薪酬/财务：颁奖奖金/实物个税代扣合规（现金/实物并入工资薪金、奖杯证书鲜花纯荣誉物不代扣、外部人士走偶然所得），税务局官方口径前置避风险（一手·国家税务总局西藏/广东税务局）。"
 },
 {
  "emoji":"💬","cat":"经理认可话术","rel":"supervisor","st":"二手",
  "title":"经理即时认可话术库·SBI(情境-行为-影响)框架 + 1小时法则（具体/及时/公开私下分寸）",
  "val":"经理是认可送达率最高的『最后一公里』：①SBI 模型（Center for Creative Leadership）——Specific 具体情境 + Behavior 做了什么 + Impact 带来什么影响，例『昨天站会上你提前拦下计费 bug（情境），保住 200 客户退款（影响）』，比『干得好』可复现 10 倍；②1小时法则——praise 半衰期极短，赢了立刻在 Slack 发一条具体的，胜过一周后 1-on-1 里写满的段落；③公开 vs 私下——怕聚光灯的骨干用私信，团队里程碑用公开频道，原则『团队赢公开庆祝、个人努力私下肯定』；④10 句即用模板（啃下硬骨头/隐藏影响被高管采用/救了同事/问了关键问题/极致交付/完美处理客户/聪明试错/文化稳定器/极其可靠/虚心接反馈）。把『夸人』从心情依赖变成 manager 的系统动作。",
  "how":"② 经理/一线主管落地：①用 SBI 模板替换『nice job』——写清情境+行为+影响三要素；②设『即时』纪律：赢了当天发，别攒到 review；③按性格分公开/私下，怕露脸的私信；④建团队专属话术库（10 句起），让夸奖不再靠灵感。认可送达率=经理执行力。",
  "url":"https://interobservers.com/employee-positive-feedback-examples/",
  "note":"② 经理/一线主管：即时认可话术库（SBI 情境-行为-影响框架 + 1小时法则 + 公开/私下分寸 + 10句即用模板），把认可从心情依赖变系统动作（二手·InterObservers / HarmonyHR / Indeed）。"
 },
 {
  "emoji":"🎯","cat":"积分认可体系","rel":"supervisor","st":"二手",
  "title":"积分制认可体系设计·点数-货币兑换 + 兑换目录 + 简单/会计口径（Bill on redemption vs issuance）",
  "val":"积分制把认可变『职场货币』，可累积、可兑换、跨地点统一：①点数-货币比——10点=$1 之类简单比值，从年度预算反推（别抄别家），让员工一眼懂『我离下个奖励多远』；②规则透明——谁可发、发多少、何时过期、如何兑换，写清楚降低 manager 犹豫；③兑换目录——礼卡/周边/餐饮/旅行/体验/数码/家居多类多价位，按前线/职能/全球分区域；④简单优先——员工体验=『我被认可→得点→换到想要的东西』，别让算公式；⑤会计口径——Bill on Redemption（仅兑付时付费，未兑换成负债）vs Bill on Issuance（发放即计税但 unredeemed 也付费），点数可设不过期以保留激励；⑥平台支撑——HiFives/Vantage/WorkTango 等做发放-通知-余额-排行榜-集成 HRMS/Teams。积分制适合『小奖高频+全球统一货币』两类诉求。",
  "how":"② HR/薪酬落地：①先定年度预算再反推点数价值（如 10点=$1），别拍脑袋；②规则写透明（发放人/额度/有效期/兑换）；③兑换目录按人群分层（前线偏实用、总部偏体验）；④选数字平台做发放-余额-排行榜-集成；⑤会计上优先 Bill on Redemption 控制负债，点数可不过期保激励。",
  "url":"https://faq.recognizeapp.com/hc/en-us/articles/215216268--Points-Strategy-Best-Practices-for-Employee-Recognition-Programs",
  "note":"② HR/薪酬：积分制认可体系设计（点数-货币兑换比值+透明规则+多类兑换目录+简单优先+Bill on redemption会计口径+平台支撑），适合小奖高频/全球统一货币（二手·Recognize / HiFives / Inspirus）。"
 },
 {
  "emoji":"📡","cat":"直播推流实操","rel":"supervisor","st":"二手",
  "title":"虚拟/混合颁奖直播推流实操·嘉宾链接入会 + 候播间 + 失败预案 + 多平台分发（品牌叠加实时）",
  "val":"远程/混合颁奖的成败在『推流执行』而非设备清单：①嘉宾零门槛入会——发浏览器链接（如 StreamYard『发送链接、点击加入』），避免下载与复杂路由，远端获奖者提前 15-20 分钟进候播间(green-room)查音频/构图/发音；②主持人私有提示卡——获奖者姓名、发音指南、赞助口播仅 host 可见；③失败预案——每位远端获奖者提前备好书面获奖感言，掉线也能现场读稿救场；④品牌与高光实时叠加——logo/lower-thirds/提名包/赞助口播在直播中叠加，录制即近成品；⑤多平台分发——YouTube(主播出+回放)/LinkedIn(企业行业)/X(社媒热议) 一次推流多 destinations，内部门户走 RTMP；⑥本地多轨录制——分离音轨便于后期与播客版。别为一场典礼搭数周 OBS 场景树，内置布局+叠加通常够用。",
  "how":"② 活动/IT 落地：①远端嘉宾用『浏览器链接入会』降低当天故障率，提前 15-20 分钟候播间彩排；②host 私有提示卡放获奖者姓名/发音/口播；③每位远端获奖者备书面感言作掉线预案；④直播中实时叠加 logo/lower-thirds/提名包，录制即成品；⑤一次推流多平台（YouTube/LinkedIn/X+内部 RTMP），本地多轨录制留后期。",
  "url":"https://streamyard.com/fr-fr/blog/how-to-stream-award-ceremonies",
  "note":"② 活动/IT：虚拟混合颁奖直播推流实操（嘉宾浏览器链接入会+候播间彩排+host私有提示卡+掉线书面感言预案+实时品牌叠加+多平台一次推流），降低典礼当天故障率（二手·StreamYard）。"
 },
 {
  "emoji":"🏆","cat":"高管荣誉项目","rel":"exec","st":"二手",
  "title":"行业 CEO/高管荣誉项目设计·独立评审 + 战略资产定位（投资者/治理/人才信任杠杆）",
  "val":"面向 CEO/创始人的外部荣誉不是『花钱买奖』，而是战略资产：① merit-based 独立评审——如 World CEO Awards 由独立 jury 按领导力卓越/战略远见/创新/业务增长/全球影响评估，无公众投票、『 recognition is earned, never bought』；②分层类别——CEO of the Year / Visionary / Innovative / Transformational / Lifetime Achievement 等，按『整体领导』『单一特质』『行业』三维设类（Globe and Mail CEO of the Year 分 Corporate Citizen/Global Visionary/Innovator/New CEO/Strategist 五类）；③战略价值——独立第三方验证强化治理可信度、投资者与董事会信任、人才吸引、市场权威，对外传播信号强；④高管内部荣誉同理——设独立评选委员会+多封同行推荐+保密终审（见 NACD Directorship 100），最忌内部人自嗨。给一把手工高管设荣誉时，用独立委员会+透明准则，把『领导力』制度化表彰。",
  "how":"③ 治理/薪酬委员会/品牌落地（表彰董事/CEO/行业高管）：①选 merit-based 独立评审的外部荣誉，拒绝『付费即获奖』；②按『整体/特质/行业』三维设类，匹配表彰意图；③把获奖当战略资产——强化投资者/治理/人才信任，对外传播；④内部高管荣誉用独立委员会+多封同行推荐+保密终审，避免自嗨。",
  "url":"http://worldceoawards.com/",
  "note":"③ 治理/薪酬委员会/品牌：行业 CEO/高管荣誉项目设计（merit-based 独立评审+三维分层类别+战略资产定位+高管内部荣誉独立委员会），把领导力制度化表彰、拒付费自嗨（二手·World CEO Awards / Globe and Mail / Global Banking & Finance）。"
 },
 {
  "emoji":"📝","cat":"事迹材料萃取","rel":"supervisor","st":"二手",
  "title":"先进事迹/表彰材料故事化萃取方法论（最小单位英雄 + 数据细节 + 反差排比结尾）",
  "val":"表彰材料质量决定典型『立得住、传得开』：①立意对标大局——把个人置于单位发展/行业变革/国家战略背景下，避免流水账；②选材『以一当十』——用最具代表性细节说话，不写『经常加班』而写『攻关三天办公室灯彻夜未熄』；③最小单位英雄——每个重要工作回答『谁+什么情况+怎么干+遇何困难』，让画面代替汇报；④结构四步——开头放一个镜头(谁+何时+做了什么+结果)、每段『观点+数据+细节』三件套、让画面代替汇报、结尾用『偏见+不+三个画面』反差排比（先树大众偏见再用三个具体画面打脸）；⑤每 500 字至少出现一个有名有姓的人，名字让人物活、事迹真；⑥不美化——在事实基础上选切入点，避免为荣誉拔高。把『工作流水账』变『打动评委的好材料』。",
  "how":"② HR/党建/表彰经办落地：①写材料前先对标当前倡导（高质量/乡村振兴等），把个人摆进大局；②用『谁在什么情况怎么干』挖最小单位英雄，画面代替汇报；③每段『观点+数据+细节』三件套，每 500 字至少一个真名；④结尾用『偏见+不+三个画面』反差排比制造记忆点；⑤不美化事迹，事实基础上选切入点。好材料=可学可做。",
  "url":"https://www.zhijidoc.com/i-75963.html",
  "note":"② HR/党建/表彰经办：先进事迹材料故事化萃取（对标大局+最小单位英雄+数据细节+反差排比结尾+真名活化），把流水账变打动评委的好材料（二手·知集Doc / 今日头条 / 笔杆儿网）。"
 },
 {
  "emoji":"🥂","cat":"高管荣誉晚宴","rel":"exec","st":"二手",
  "title":"高管荣誉晚宴/顶层成就认可形式·与战略叙事挂钩（仅限顶层成就、executive recognition dinners）",
  "val":"顶层成就的认可需要『匹配量级』的场合：①形式分级——日常/中层走会议表彰段，顶层成就（终身成就/战略级贡献/退休领袖）走 executive recognition dinners / leadership honours 等专属晚宴，场合本身传递『这件事分量够重』；②与战略叙事挂钩——晚宴不是社交，而是把获奖者的贡献接成组织战略故事（如将 retiring 领袖的遗产讲成『文化传承』、将战略级贡献讲成『未来方向』），让在场高管共鸣；③个性化颁奖时刻——获奖者专属短片/同事寄语/客户反馈/照片，灯光音乐随环节明暗，营造情感起伏；④特殊认可——retiring personnel 在晚宴设专属致敬环节，把『告别』变成『传承仪式』。顶层认可最忌与日常表彰同质化，场合与叙事都要『升一档』。",
  "how":"③ 高管/治理落地（顶层成就与退休领袖认可）：①按成就量级分级场合——顶层成就/退休领袖走专属晚宴而非会议表彰段；②晚宴把贡献接成战略叙事（传承/未来方向），引发高管共鸣；③获奖者专属短片+寄语+照片+灯光音乐明暗造情感起伏；④退休领袖设专属致敬环节，把告别变传承仪式。顶层认可场合与叙事都要升一档。",
  "url":"https://digital-trophy-case.com/blog/award-ceremony-planning-memorable-recognition-event",
  "note":"③ 高管/治理：高管荣誉晚宴与顶层成就认可形式（executive recognition dinners/leadership honours，与战略叙事挂钩、个性化颁奖时刻、退休领袖专属致敬），场合与叙事都要升一档（二手·digital-trophy-case）。"
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

exec_cards = [c for c in cards if "exec" in c["rel"]]
sup_cards  = [c for c in cards if "supervisor" in c["rel"]]
n_exec=len(exec_cards); n_sup=len(sup_cards)
assert n_exec + n_sup == len(cards), "card count mismatch"

# Step 1. tmp newcards
tmp = os.path.join(AWARD, ".run_newcards.tmp.html")
with open(tmp, "w", encoding="utf-8") as f:
    for c in cards:
        f.write(card_html(c))
print("WROTE tmp newcards:", len(cards), "cards")

# Step 2. gen incremental page -> award/award-20260902.html
run_page = os.path.join(AWARD, "award-20260902.html")
r = subprocess.run(
    [sys.executable, os.path.join(KC, "gen_run_page.py"),
     "--topic", "award", "--topic-name", "颁奖典礼·荣誉表彰",
     "--date", RUN_DATE, "--round", "29", "--cards-file", tmp,
     "--out", run_page],
    cwd=KC, capture_output=True, text=True, timeout=120)
print("GEN RUN PAGE rc=", r.returncode, r.stdout.strip(), r.stderr.strip()[:200])
assert os.path.isfile(run_page), "run page not generated"

# Step 3. update wall award.html
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

# Step 4. index.json
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

# Step 5. Obsidian note
note_path = os.path.join(VAULT,"素材","award","颁奖-知识卡汇总.md")
note = open(note_path, encoding="utf-8").read()
note = note.replace("共 %d 张" % BASE, "共 %d 张" % (BASE+N), 1)
round_sec = (
"## 轮次 2026-09-02（+%d）\n" % N +
"本轮新增（均通过六维评估、仅 ②上下级 / ③高管间）：\n"
)
for c in cards:
    rel_txt = "③高管间" if c["rel"]=="exec" else "②上下级"
    round_sec += "- "+c["title"]+"（award/award.html） | "+rel_txt+" | "+c["st"]+"\n"
# insert narrative before first 轮次
note = note.replace("## 轮次", round_sec+"## 轮次", 1)
rows=""
for c in cards:
    rel_cell = "③高管间" if c["rel"]=="exec" else "②上下级"
    rows += "| "+c["title"]+"（award/award.html） | 4 | "+c["st"]+" | "+rel_cell+" |  |\n"
inc_link = "- 本轮增量页（二十九轮·2026-09-02）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/award-20260902.html"
note = note.replace("## 线上卡片墙（GitHub Pages）", rows+inc_link+"\n## 线上卡片墙（GitHub Pages）", 1)
open(note_path,"w",encoding="utf-8").write(note)
print("UPDATED obsidian note (共 %d 张)" % (BASE+N))

# Step 6. 00-index
idx00 = open(os.path.join(VAULT,"00-知识采集索引.md"), encoding="utf-8").read()
idx00 = idx00.replace("**%d 卡**" % BASE, "**%d 卡**" % (BASE+N), 1)
# append missing rounds to header line
HEADER_ANCHOR = "二十六轮 enrich 2026-08-27(+9)"
assert HEADER_ANCHOR in idx00, "header anchor not found"
idx00 = idx00.replace(HEADER_ANCHOR, HEADER_ANCHOR+' ｜ 二十七轮 enrich 2026-08-28(+7) ｜ 二十八轮 enrich 2026-09-01(+6) ｜ 二十九轮 enrich 2026-09-02(+%d)' % N, 1)
# insert 7 rows after the LAST award row
lines = idx00.split("\n")
last_award = -1
for i,l in enumerate(lines):
    if "award/award.html" in l and l.strip().startswith("|"):
        last_award = i
assert last_award >= 0, "no award row found"
zrows=""
for c in cards:
    rel_cell = "③高管间" if c["rel"]=="exec" else "②上下级"
    zrows += "| "+c["title"]+"（award/award.html） | 4 | "+c["st"]+" | "+rel_cell+" |  |\n"
lines.insert(last_award+1, zrows.rstrip("\n"))
idx00 = "\n".join(lines)
open(os.path.join(VAULT,"00-知识采集索引.md"),"w",encoding="utf-8").write(idx00)
print("UPDATED 00-index (共 %d 卡)" % (BASE+N))

# Step 8. lexiang-entry-map.json
map_path = os.path.join(KC, "lexiang-entry-map.json")
mp = json.load(open(map_path, encoding="utf-8"))
award_map = mp["award"]
award_map["rounds"].append({
  "date": RUN_DATE,
  "entry_id": None,
  "name": "award-20260902.html",
  "note": "轮次页 R29 (+%d：颁奖个税代扣合规/经理SBI话术/积分制体系/直播推流实操/CEO高管荣誉/事迹萃取/高管荣誉晚宴)｜乐享待补传(token 过期/断开，待重连后补传并回填 entry_id)" % N
})
json.dump(mp, open(map_path,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
print("UPDATED lexiang-entry-map.json (round R29 appended, entry_id=null)")

# Step 9. lexiang probe (best-effort, non-blocking)
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

print("DONE R29 | 新增 N=%d 删除 M=%d | 墙=%d卡 | 增量页=%s" % (N, M, after, run_page))
