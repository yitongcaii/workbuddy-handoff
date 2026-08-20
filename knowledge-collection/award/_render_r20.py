# -*- coding: utf-8 -*-
import json, os

KC = r"C:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection"
AWARD = os.path.join(KC, "award")
VAULT = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库"

def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

# ---- Cards (R20, 2026-08-21) — 仅 ②上下级 / ③高管间，0 peer ----
cards = [
 {
  "emoji":"🌐","cat":"混合团队","rel":"supervisor","st":"二手",
  "title":"分布式/混合团队经理认可框架·把认可织进日常流（异步feed/嵌Slack Teams/本地化奖励/跨模式度量）",
  "val":"混合与分布式团队里，认可不能靠「刚好在同一个会议室」。Awardco 四点实践：①把认可织进日常——建公开认可 feed，让好工作异步被看见；里程碑（司龄/入职完成/项目节点）自动化，不靠人记；②嵌进工作流——接 Slack/Teams/Outlook/移动端，认可变「两下点击」而非五步表单，融入每日站会/周报/复盘；③奖励要有意义且本地化——全球团队提供本地偏好的奖励选项、币种转换/多语言/履约无缝，海外员工也能真正用上；④跨工作模式度量——看「谁被认可、何时、是否因工作模式不同而有差异」，识别哪些经理停了认可。核心：技术放大人的连接，不让认可取决于物理距离。",
  "how":"经理/一线主管落地：①建公开异步认可 feed + 里程碑自动触发（司龄/项目节点）；②把认可接进 Slack/Teams/站会，做成「两下点击」的肌肉记忆；③给本地化奖励选项（币种/语言/履约），别只发一种全球 catalog；④定期看跨模式认可分布，别让远程员工「眼不见心不想」。",
  "url":"https://www.awardco.com/blog/remote-employee-recognition-making-sure-great-work-gets-seen-in-a-hybrid-world",
  "note":"② 经理/一线主管把混合团队的认可做成「异步可见+嵌工作流+本地化」，不让远程员工被忽略（③ 全球奖励目录与多语言履约需 HR/高管定标准）。"
 },
 {
  "emoji":"💬","cat":"经理话术","rel":"supervisor","st":"二手",
  "title":"管理者认可话术与公开/私下边界·「做了什么/为何重要/帮了谁」3 问法",
  "val":"远程/混合团队里认可最易「模板化翻车」。firacard 给出可落地的经理话术框架：①说什么——弱认可（「项目做得好」「谢谢付出」）几乎无重量；强认可描述行为而非结果：「你把混乱的交接理顺了、早早厘清责任、全程同步客户没过度承诺，帮团队避免混乱、保住信任」。好认可回答三问：做了什么、为何重要、帮了谁；②公开 vs 私下——用公开当「教团队什么是好」、用私下当「关乎个人成长/敏感/怕在群里尴尬」；简单判定：教团队规范→公开，关乎个人→私下；③价值观不说教——别复读口号，举证据（「你提前拦住了一个会变成客户问题的风险」「你写清了流程让跨时区同事更快」）；④经理问责——认可成败在一致性，把认可接进已有的每周 1:1/站会，而非另起任务；⑤别强迫公开——有人偏好私信，硬拉上台适得其反。",
  "how":"经理落地：①每次认可写清「行为+影响+受益方」三要素，忌「谢谢努力」套话；②公开=立规范、私下=护成长，按敏感度选通道；③价值观用具体证据代替口号；④把认可嵌进每周 1:1/站会节奏，靠小习惯而非大活动；⑤尊重员工偏好，不强迫上台。",
  "url":"https://firacard.com/blog/remote-employee-recognition",
  "note":"② 经理把认可从「套话」升级为「具体行为+影响」的话术与公开/私下边界（③ 高管公开认可同理，但须更克制、以专业/共同目标切入）。"
 },
 {
  "emoji":"🤝","cat":"并购整合","rel":"exec","st":"二手",
  "title":"M&A 并购期认可连续性·认可桥接计划（cross-org 互认）+ 流失预警信号",
  "val":"并购期认可不能替代诚实沟通（角色决定/经理关系/整合决策），但能在组织注意力转移时维持「贡献被看见」。rewardian 给出三套整合路径：①即时平台合并（收购方平台直接延展，风险=被吸收感）；②双轨并行 6-12 月（两组织各留程序，风险=可见不平等）；③认可桥接计划（临时轻量、限期的跨组织互认空间，最被低估也常最有效）。整合期五个目标机制：经理认可频率周提示、legacy 间 cross-org 互认（「融合贡献」类别+60 天挑战）、临时「融合行为」类别（容 ambiguity/知识共享）、认可数据当月分析做流失领先指标、把认可计划写进整合叙事。关键：cross-org 互认是结构化文化整合替代不了的人情连接。",
  "how":"HR/整合负责人（高管间）落地：①优先建「认可桥接」临时计划，不急着废任一方系统；②设经理周提示，防整合忙乱期认可断档；③开 cross-org 互认 feed + 「融合贡献」类别 + 60 天挑战；④认可分析改月度，标记「经理停认可/团队掉认可」做流失预警；⑤把认可计划明写进整合沟通，作为文化信号。",
  "url":"https://blog.rewardian.com/employee-engagement-during-ma-how-to-maintain-recognition-through-a-merger",
  "note":"③ HR 高管/整合负责人把并购期认可做成「桥接+互认+流失预警」（② 一线经理靠周提示维持对本团队认可频率）。"
 },
 {
  "emoji":"📈","cat":"变革转型","rel":"exec","st":"二手",
  "title":"组织变革期认可=转型基础设施·量化收益（参与率 2.3x 投入、1.7x 留任）",
  "val":"Awardco 研究：AI 采用/人力重构/持续变革挤掉了认可的优先级，但认可本就是转型的机制而非竞争者。数据：变革期靠认可的组织，员工投入意愿高 2.3 倍、想留下高 1.7 倍。案例——Alera Group（24 次并购/280 office）把认可绑价值观、给经理月度预算、接 onboarding/里程碑：认可采纳 +170%、高参与员工流失风险 -43%、至少两次认可者留任 +9%、经理认可动作 +188%；Paramount（Viacom+CBS 合并，2 万+全球）统一碎片化认可、跨区域公平灵活奖励：统一 141 国、回收约 52 天行政工时。结论：每次认可都在发「什么重要」的信号，比备忘录更能驱动新行为采纳；认可不是 nice-to-have，是转型基础设施。",
  "how":"高管/HR 负责人落地：①把认可写进变革叙事，作为「行为信号」而非额外活动；②给经理月度认可预算，接 onboarding/里程碑，降低门槛；③跨区域用统一平台 + 公平灵活奖励，防文化漂移；④用采纳率/流失风险做量化看板，向董事会证明认可 ROI。",
  "url":"https://www.awardco.com/blog/recognition-during-organizational-change",
  "note":"③ 高管/HR 负责人把组织变革期认可定位为「转型基础设施」并用量化收益（2.3x/1.7x）向董事会证明（② 经理靠月度预算把认可织进日常）。"
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
'<title>颁奖典礼 . 二十轮增量卡片（2026-08-21）</title>\n'+CSS+'</head><body>\n'
'<div class="wrap">\n'
'<p style="margin:0 0 16px"><a href="https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/award.html" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">🏆 返回颁奖累计卡片墙 .</a> &nbsp; <a href="https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/index.html" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">📚 返回知识库门户 .</a></p>\n'
'  <div class="hero">\n'
'    <h1>🏆 颁奖典礼 . 二十轮增量卡片（2026-08-21）</h1>\n'
'    <p>本轮新增 '+str(len(cards))+' 张（通过六维评估，剔除平级/朋友向①，仅 ②上下级 / ③高管间）；关系档：③高管间 '+str(n_exec)+' 张 + ②上下级 '+str(n_sup)+' 张。</p>\n'
'    <div class="relbar">\n      <span>② 领导↔员工（上下级，supervisor）</span>\n      <span>③ 领导↔领导（高管间，exec）</span>\n    </div>\n  </div>\n'
'  <div class="grid">\n'+inc_body+'  </div>\n'
'<footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>\n'
'</div>\n</body>\n</html>\n'
)
inc_path = os.path.join(AWARD, "award-20260821.html")
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

hero_old = '十九轮 enrich 2026-08-19(+6)'
assert summary.count(hero_old)>=1
summary = summary.replace(hero_old, '十九轮 enrich 2026-08-19(+6) ｜ 二十轮 enrich 2026-08-21(+4)', 1)

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
note = note.replace("共 115 张","共 119 张",1)
r20_section = (
"## 轮次 2026-08-21（+4）\n"
"本轮新增（均通过六维评估、仅 ②上下级 / ③高管间）：\n"
)
for c in cards:
    rel_txt = "③高管间" if c["rel"]=="exec" else ("②上下级" if c["rel"]=="supervisor" else "②上下级+③高管间")
    r20_section += "- "+c["title"]+"（"+rel_txt+"·二手）\n"
note = note.replace("## 卡片总表", r20_section+"## 卡片总表", 1)
rows=""
for c in cards:
    rel_cell = "③高管间" if c["rel"]=="exec" else ("②上下级" if c["rel"]=="supervisor" else "②上下级+③高管间")
    rows += "| "+c["title"]+"（award/award.html） | 4 | 二手 | "+rel_cell+" |  |\n"
note = note.replace("## 线上卡片墙（GitHub Pages）", rows+"## 线上卡片墙（GitHub Pages）", 1)
note = note.replace(
 "本轮增量页（十九轮·2026-08-19）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/award-20260819.html",
 "本轮增量页（十九轮·2026-08-19）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/award-20260819.html\n- 本轮增量页（二十轮·2026-08-21）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/award-20260821.html",
 1)
open(note_path,"w",encoding="utf-8").write(note)
print("UPDATED obsidian note")

# ---- 5. 00-index ----
idx00 = open(os.path.join(VAULT,"00-知识采集索引.md"), encoding="utf-8").read()
hdr_old = " ｜ 十九轮 enrich 2026-08-19(+6)"
assert idx00.count(hdr_old)>=1
idx00 = idx00.replace(hdr_old, hdr_old+" ｜ 二十轮 enrich 2026-08-21(+4)", 1)
openday_nav = "📄 主题汇总笔记：[[知识采集库/素材/openday/OpenDay-开放日-知识卡汇总|OpenDay-开放日-知识卡汇总]]"
assert idx00.count(openday_nav)>=1
zrows=""
for c in cards:
    rel_cell = "③高管间" if c["rel"]=="exec" else ("②上下级" if c["rel"]=="supervisor" else "②上下级+③高管间")
    zrows += "| "+c["title"]+"（award/award.html） | 4 | 二手 | "+rel_cell+" |  |\n"
idx00 = idx00.replace(openday_nav, zrows+openday_nav, 1)
open(os.path.join(VAULT,"00-知识采集索引.md"),"w",encoding="utf-8").write(idx00)
print("UPDATED 00-index")
print("DONE R20")
