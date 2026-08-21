# -*- coding: utf-8 -*-
import json, os, re

KC = r"C:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection"
AWARD = os.path.join(KC, "award")
VAULT = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库"

def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

# ---- Cards (R21 / 二十一轮 enrich, 2026-08-21b) — 仅 ②上下级 / ③高管间，0 peer ----
cards = [
 {
  "emoji":"🎖","cat":"司龄荣誉","rel":"supervisor","st":"二手",
  "title":"长期服务/里程碑奖·分层认可（早期经理主导→重大里程碑高管亲签）",
  "val":"服务奖应随司龄递增强度：早期里程碑（1/2/3年）由经理主导轻量及时认可（数字徽章+内部墙 profile+团队提及）；中期（5/10/15年）更强可见度+个性化信息+适度礼品；重大里程碑（20/25年）高管亲签 note+公开表彰+更长 profile+纪念性礼品/体验。避免「早期花太多、重大太少」。关键：服务奖与绩效奖分离防混淆；纳入经理故事/项目亮点而非仅 Loyalty；公开 vs 内部规则提前定；eligibility 规则（兼职/离职返聘/并购进来员工）写清防例外。可建「常开式」认可平台让里程碑与日常赞赏并存。",
  "how":"经理/HR 落地：①按司龄设递增档（1/5/10/20年），早期经理轻量、重大高管亲签；②服务奖与绩效奖分离；③把经理具体故事写进里程碑信息（非泛泛忠诚）；④eligibility 与公示规则提前定；⑤建常开平台让司龄里程碑+日常赞赏并存。",
  "url":"https://walloffame.cloud/years-of-service-awards-guide-milestones-ideas-and-recognition-timing",
  "note":"② 经理/HR 把长期服务奖做成「递增强度+高管亲签重大里程碑」，与绩效奖分离、规则透明（③ 高管站台式认可见另卡）。"
 },
 {
  "emoji":"🛡","cat":"安全表彰","rel":"supervisor","st":"一手",
  "title":"安全奖/零事故班组表彰·「表彰卡+星级+隐患上报」闭环（一线工地）",
  "val":"潜江市建筑工地「安全啄木鸟+行为安全之星」：每月发表彰卡≥一线人数50%，小程序上报隐患数持续提升；月底大红榜公示「行为安全之星」（约1%分一二三等奖金+宣传栏亮身份）；季度「平安班组」对隐患上报多、整改好的班组授称号+集体奖；「安全啄木鸟」隐患上报核实后按等级给现金/实物/积分，全程小程序闭环（上报-核实-整改-奖励）。多重激励让一线从「要我安全」变「我要安全」。机制保障：专项经费专款专用+台账留痕+监督箱防弄虚作假。",
  "how":"一线主管/项目经理落地：①月度发表彰卡覆盖≥50%一线、月底红榜公示星级安全之星；②季度评「平安班组」授称号+集体奖；③隐患上报小程序闭环（上报-核实-整改-奖励）+专项台账留痕；④设监督箱防乱发。",
  "url":"https://www.hbqj.gov.cn/szfhcxjsj/xwzx/gzdt/202604/t20260402_5906030.html",
  "note":"② 一线主管/项目经理把安全表彰做成「表彰卡+星级+班组+隐患上报闭环」，让一线从被动合规变主动守安全（政府官方一手案例）。"
 },
 {
  "emoji":"💡","cat":"改善提案","rel":"supervisor","st":"一手",
  "title":"创意提案/Kaizen 改善奖·主管现地现物审奖+小额高频（丰田 70 年体系）",
  "val":"丰田「创意提案奖励制度」70余年：员工在日常发现麻烦→想改善→与主管商量→主管给支持→实施并量化结果→填提案表→主管现地现物(genchi-genbutsu)审奖→发奖。2019修订按「结果分（改善效果5维）+过程分（立意/独创/努力）」定奖金（500日元~20万日元）；5000日元以上由室长/课长评、5万以上由创意提案委员会审。2023年提案约81万条（人均14.4条）。核心：领导重视每一条小提案（挪垃圾桶也是改善），不轻易否定，让提案系统成人才培养工具。",
  "how":"一线主管/班组长落地 Kaizen 提案奖：①建「发现问题→与主管商量→实施→填表→主管现地审奖」闭环；②奖金按结果分+过程分双轨，小提案也认真评；③主管不轻易否定、鼓励尝试；④新人设 Rookie Award 养成提案习惯；⑤把提案系统当人才培养而非仅省成本。",
  "url":"https://toyotatimes.jp/en/series/Imaginative_and_creative/001_1.html",
  "note":"② 一线主管把创意提案做成「主管现地现物审奖+小额高频+不否定小改善」的人才培养机制（丰田官方一手）。"
 },
 {
  "emoji":"⚖️","cat":"公平治理","rel":"supervisor","st":"一手",
  "title":"评优评先公平治理·评审委+全员监督+公示+申诉（打破「轮流坐庄/论资排辈」）",
  "val":"榆社化工新选举办法破传统弊端：评选标准多维（业绩+团队协作+创新+品行，避免片面）；流程四阶段（初选含班组联名+员工自荐→五进二随机抽取员工代表评议→3天公示接受匿名检举→终评委员会投票）；公示期员工可匿名异议、评委会调查回应，全员监督增公信力。配套「近2年考评良好」基础条件、打破轮流坐庄/论资排辈。通用公平机制：明确标准、公开透明、设评审委员会（多部门/多层代表）、绩效挂钩、申诉复核、定期审查。",
  "how":"管理者/HR 落地评优公平：①多维标准（业绩+协作+创新+品行）替代单一；②流程透明（初选→抽查评议→公示→终评），公示期开匿名异议+评委会回应；③建跨部门评审委员会防主管偏袒；④绩效挂钩+申诉复核通道；⑤定期审查优化。",
  "url":"http://sxyh.com.cn/wap_news_detail/typeid/14/id/4119.html",
  "note":"② 管理者/HR 把评优评先做成「评审委+公示+匿名申诉」的公平治理，破关系/论资排辈（③ 组织级荣誉体系由高管/党委审批的顶层架构见另卡）。"
 },
 {
  "emoji":"🏅","cat":"组织级认可","rel":"exec","st":"一手",
  "title":"总裁奖/President's Award·组织级认可（CEO 颁 top 1%、董事会选、50 年传统）",
  "val":"麦当劳 President's Award 代表全球公司员工 top 1%（2022 为 37 市场 121 人），由 EVP Global Chief People Officer 在全球员工 appreciation day 署名表彰，是公司最高荣誉之一（1973 年由 Ray Kroc/Fred Turner 创立，2023 满 50 年）；Circle of Excellence 表彰 15 个跨职能团队、Shining Light 表彰 60 市场 220 人（收 2000+ 提名）。住友电工 President's Award 由社长在全球 Kaizen 大会亲自颁发给 Small Group/Kaizen Suggestions/200 Kaizen 工厂三类总统奖。特征：最高层（CEO/社长）亲自颁奖+署名、董事会/评委会遴选、面向全球 top performer、作为组织能力与雇主品牌信号。",
  "how":"高管（CEO/HR 一把手）落地组织级认可：①设公司最高荣誉（President's Award 级），由 CEO 亲自颁奖+署名信；②评委会/董事会遴选，标准绑定价值观与战略贡献；③面向全球 top performer（如 top 1%），作为雇主品牌信号；④与年度盛典/全球公告结合放大。",
  "url":"https://corporate.mcdonalds.com/corpmcd/our-stories/article/2022-global-award-winners.html",
  "note":"③ 高管/CEO 把组织级认可做成「一把手亲自颁奖+董事会遴选+全球 top 1%」的战略信号（② 一线经理用日常认可承接）。"
 },
 {
  "emoji":"🎤","cat":"高管站台","rel":"exec","st":"二手",
  "title":"高管站台式认可·把表彰写进组织战略文化议程（最高层亲自颁奖+叙事）",
  "val":"认可 tone 由顶层定——当 senior leadership visibly champion 服务奖/认可计划，向全员发强信号。做法：高管亲自参与颁奖（分享 recipient 个人轶事）、持续沟通员工忠诚与贡献价值、把认可织进 broader 文化倡议（连价值观/使命）、训练经理给个性化信息。反模式：last-minute 匆忙 presentation 贬低意义、只用通用礼品、忽略反馈、仅靠 HR（认可应是全层级 shared responsibility 非 HR 职能）。核心：高管站台让认可从「HR 项目」升为「组织能力」。",
  "how":"高管落地：①一把手亲自颁奖并讲 recipient 真实故事（非念稿）；②把认可写进文化/战略议程，连价值观与使命；③训练一线经理给个性化认可信息（高管定调+赋能）；④持续沟通「为何认可」，不靠 HR 单打。",
  "url":"https://recruit-talent.com/the-strategic-imperative-transforming-employee-service-awards-for-modern-workforce-engagement-and-retention",
  "note":"③ 高管把认可体系作为组织能力顶层议题、亲自站台颁奖+叙事（② 经理承接日常个性化认可）。"
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
      '      <div class="src">🔗 <a href="'+c["url"]+'" target="_blank">'+esc(c["url"])+'</a></div>\n'
      '      <div class="note">适用：'+esc(c["note"])+'</div>\n'
      '    </div>\n'
    )

CSS = """<style>
:root{--bg:#f4f6fb;--card:#ffffff;--ink:#1f2430;  --sub:#5b6478;--accent:#6c5ce7;--accent2:#00b8d9;--chip:#eef0ff;}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:linear-gradient(135deg,#eef1ff 0%,#e6f7ff 100%);color:var(--ink);padding:28px 18px;line-height:1.6;}
.wrap{max-width:1080px;margin:0 auto;}
.hero{background:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);border-radius:22px;padding:26px 30px;color:#fff;box-shadow:0 14px 40px rgba(108,92,231,.25);margin-bottom:22px;}
.hero h1{font-size:24px;font-weight:800;letter-spacing:1px;margin-bottom:6px;}
.hero p{font-size:13px;opacity:.95;}
.relbar{display:flex;gap:10px;flex-wrap:wrap;margin-top:12px;}
.relbar span{background:rgba(255,255,255,.2);border-radius:20px;padding:5px 14px;font-size:13px;font-weight:600;}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;}
.hl{background:var(--card);border-radius:18px;padding:18px 18px 16px;border-top:4px solid var(--accent);box-shadow:0 10px 32px rgba(108,92,231,.10);display:flex;flex-direction:column;gap:9px;}
.top{display:flex;align-items:center;gap:8px;flex-wrap:wrap;}
.emoji{font-size:22px;}
.hl h3{font-size:16px;font-weight:700;flex:1;min-width:120px;}
.cat{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:600;background:var(--chip);color:var(--accent);}
.badge{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:700;}
.b2{background:#fff1e6;color:#c0651a;}
.r2{background:#fff3e0;color:#c0651a;}
.r3{background:#f3e8ff;color:#7b2cbf;}
.val{font-size:13.5px;color:var(--sub);}
.exec{margin-top:2px;border-top:1px dashed #e2e8f0;padding-top:8px;}
.exec summary{cursor:pointer;font-size:13px;font-weight:600;color:var(--accent);}
.exec .inner{font-size:13px;color:var(--sub);margin-top:6px;padding-left:4px;}
.src{font-size:12px;word-break:break-all;}
.src a{color:var(--accent2);text-decoration:none;}
.note{font-size:12px;color:#94a3b8;border-left:3px solid #e2e8f0;padding-left:8px;}
footer{text-align:center;padding:24px;color:#94a3b8;font-size:13px;border-top:1px solid #e2e8f0;margin-top:40px;}
</style>"""

exec_cards = [c for c in cards if "exec" in c["rel"]]
sup_cards  = [c for c in cards if c["rel"]=="supervisor"]
n_exec=len(exec_cards); n_sup=len(sup_cards)

inc_body = "".join(card_html(c) for c in cards)
inc_html = (
'<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n<meta charset="UTF-8">\n'
'<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
'<title>颁奖典礼 . 二十一轮增量卡片（2026-08-21b）</title>\n'+CSS+'</head><body>\n'
'<div class="wrap">\n'
'<p style="margin:0 0 16px"><a href="https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/award.html" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">🏆 返回颁奖累计卡片墙 .</a> &nbsp; <a href="https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/index.html" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">📚 返回知识库门户 .</a></p>\n'
'  <div class="hero">\n'
'    <h1>🏆 颁奖典礼 . 二十一轮增量卡片（2026-08-21b）</h1>\n'
'    <p>本轮新增 '+str(len(cards))+' 张（通过六维评估，剔除平级/朋友向①，仅 ②上下级 / ③高管间）；关系档：③高管间 '+str(n_exec)+' 张 + ②上下级 '+str(n_sup)+' 张。</p>\n'
'    <div class="relbar">\n      <span>② 领导↔员工（上下级，supervisor）</span>\n      <span>③ 领导↔领导（高管间，exec）</span>\n    </div>\n  </div>\n'
'  <div class="grid">\n'+inc_body+'  </div>\n'
'<footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>\n'
'</div>\n</body>\n</html>\n'
)
inc_path = os.path.join(AWARD, "award-20260821b.html")
with open(inc_path, "w", encoding="utf-8") as f:
    f.write(inc_html)
print("WROTE incremental:", inc_path, len(inc_html), "bytes")

# ---- 2. update summary award.html ----
summary = open(os.path.join(AWARD,"award.html"), encoding="utf-8").read()
exec_frag = "".join(card_html(c) for c in exec_cards)
sup_frag  = "".join(card_html(c) for c in sup_cards)

assert summary.count('  <div class="sec sec2">')==1, "sec2 marker not unique"
summary = summary.replace('  <div class="sec sec2">', '  '+exec_frag+'  <div class="sec sec2">', 1)

marker = '</div>\n<footer>'
assert summary.count(marker)==1, "footer grid-close marker not unique: "+str(summary.count(marker))
summary = summary.replace(marker, '  '+sup_frag+marker, 1)

hero_old = '二十轮 enrich 2026-08-21(+4)'
assert summary.count(hero_old)>=1
summary = summary.replace(hero_old, '二十轮 enrich 2026-08-21(+4) ｜ 二十一轮 enrich 2026-08-21(+6)', 1)

open(os.path.join(AWARD,"award.html"),"w",encoding="utf-8").write(summary)
print("UPDATED summary award.html")

# ---- 3. index.json ----
idx = json.load(open(os.path.join(KC,"index.json"), encoding="utf-8"))
new_entries=[]
for c in cards:
    e={
      "title": c["title"],
      "normKey": c["title"],
      "url": c["url"],
      "sourceType": "secondary" if c["st"]=="二手" else "primary",
      "relation": c["rel"],
      "summary": c["val"][:120],
      "topic": "award",
      "dateCollected": "2026-08-21"
    }
    idx.append(e)
    new_entries.append(e)
json.dump(idx, open(os.path.join(KC,"index.json"),"w",encoding="utf-8"), ensure_ascii=False, indent=2)
print("UPDATED index.json (+%d) total=%d" % (len(new_entries), len(idx)))

# ---- 4. Obsidian note ----
note_path = os.path.join(VAULT,"素材","award","颁奖-知识卡汇总.md")
note = open(note_path, encoding="utf-8").read()
note = note.replace("共 119 张","共 125 张",1)
r_section = (
"## 轮次 2026-08-21b（+6）\n"
"本轮新增（均通过六维评估、仅 ②上下级 / ③高管间）：\n"
)
for c in cards:
    rel_txt = "③高管间" if c["rel"]=="exec" else ("②上下级" if c["rel"]=="supervisor" else "②上下级+③高管间")
    r_section += "- "+c["title"]+"（"+rel_txt+"·"+c["st"]+"）\n"
note = note.replace("## 卡片总表", r_section+"## 卡片总表", 1)
rows=""
for c in cards:
    rel_cell = "③高管间" if c["rel"]=="exec" else ("②上下级" if c["rel"]=="supervisor" else "②上下级+③高管间")
    rows += "| "+c["title"]+"（award/award.html） | 4 | "+c["st"]+" | "+rel_cell+" |  |\n"
note = note.replace("## 线上卡片墙（GitHub Pages）", rows+"## 线上卡片墙（GitHub Pages）", 1)
old_link = "本轮增量页（二十轮·2026-08-21）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/award-20260821.html"
assert note.count(old_link)>=1
note = note.replace(old_link, old_link+"\n- 本轮增量页（二十一轮·2026-08-21b）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/award-20260821b.html", 1)
open(note_path,"w",encoding="utf-8").write(note)
print("UPDATED obsidian note")

# ---- 5. 00-index ----
idx00 = open(os.path.join(VAULT,"00-知识采集索引.md"), encoding="utf-8").read()
hdr_old = " ｜ 二十轮 enrich 2026-08-21(+4)"
assert idx00.count(hdr_old)>=1
idx00 = idx00.replace(hdr_old, hdr_old+" ｜ 二十一轮 enrich 2026-08-21(+6)", 1)
idx00 = idx00.replace("**115 卡**", "**125 卡**", 1)
openday_nav = "📄 主题汇总笔记：[[知识采集库/素材/openday/OpenDay-开放日-知识卡汇总|OpenDay-开放日-知识卡汇总]]"
assert idx00.count(openday_nav)>=1
zrows=""
for c in cards:
    rel_cell = "③高管间" if c["rel"]=="exec" else ("②上下级" if c["rel"]=="supervisor" else "②上下级+③高管间")
    zrows += "| "+c["title"]+"（award/award.html） | 4 | "+c["st"]+" | "+rel_cell+" |  |\n"
idx00 = idx00.replace(openday_nav, zrows+openday_nav, 1)
open(os.path.join(VAULT,"00-知识采集索引.md"),"w",encoding="utf-8").write(idx00)
print("UPDATED 00-index")
print("DONE R21 (award) N=+%d" % len(cards))
