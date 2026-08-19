# -*- coding: utf-8 -*-
"""Offsite 十九轮 enrich（2026-08-19）。生成本轮 6 张 ②③ 卡：增量页 + 汇总页注入 + index.json + Obsidian + 00-索引 + 门户。"""
import os, re, json

KC = r"C:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection"
VAULT = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库"
RUN_DATE = "20260819"
NEXT = "破冰"
TOPIC = "offsite"
ROUND = "十九轮"

# ---------- 6 张卡 ----------
cards = [
 dict(emoji="🗳️",
   title="高管务虚会「红蓝军对抗 + 德尔菲匿名投票 + 六维行动矩阵 + 军令状」SOP",
   cat="务虚框架", rel="高管间", relcls="r3", srctype="二手",
   src="https://wenku.baidu.com/view/f8e77f86b007e87101f69e3143323968001cf4db",
   val="闭门务虚会（董事会/战略委员会，15人内，封闭山庄U型座，全员签NDA保密三年，禁电子设备）。核心议程：①破冰「三分钟画像法」用比喻描述企业现状；②战略推演放定制沙盘视频模拟三种经济情境，强制换位（生产从市场角度、财务模拟客户）；③冲突激荡「红蓝军对抗辩论」——反对者须提三个数据支撑反对理由，支持方用场景推演回应；④共识锻造用德尔菲法三轮匿名投票对战略假设优先级排序，得票<30%淘汰；⑤行动锚定把共识转六维行动矩阵（可行性阈值/资源缺口/风险敞口），现场组跨部门攻坚小组签军令状录承诺视频。成果48h内固化三形态：图文纪要+决策要点清单（标注转折性共识）+待验证假设库；双周跟踪由CEO办督办，下次务虚首项查承诺兑现率。",
   exec="闭门签NDA禁电子设备；红蓝军对抗须三个数据支撑反对理由；德尔菲三轮匿名投票淘汰<30%议题；共识转六维行动矩阵现场签军令状；48h出纪要+决策清单+假设库，双周督办查兑现率。",
   note="适用：③ 董事会/战略委员会级闭门务虚会，「红蓝军对抗+德尔菲匿名+六维行动矩阵+军令状」是可迁移硬SOP。🔍 区别于卡片（华为务虚会四步法——本卡补「红蓝军须三个数据反对理由+德尔菲淘汰<30%+军令状录视频」的强约束议事机制，更偏闭门决策纪律）。"),
 dict(emoji="🔭",
   title="华为式「务虚会四步法」：会前60天洞察→会中2天1晚红蓝军→会后几上几下发酵→闭环落地（制造企业翻盘案例）",
   cat="务虚框架", rel="高管间", relcls="r3", srctype="二手",
   src="https://m.toutiao.com/article/7630245697970848292",
   val="基于华为实践提炼「真务虚」四步法。①会前60天精心筹备：议题要\"虚\"（未来三年客户价值怎么变/哪些趋势颠覆我们，而非下季度业绩怎么冲）；每议题成立研究小组答三句话（趋势是什么/对我们意味着什么/我们该怎么办）；配置三类角色——引导员控场激发碰撞、核心参与者贡献真观点、决策者以平等身份参与不提前定调；换环境开会（离开办公室去安静放松处）。②会中2天1晚深度碰撞先发散后收敛：第一天百花齐放允许吵架，不用长PPT只用一页纸，领导不总结不拍板只提问，红蓝军对抗专唱反调挑漏洞；第二天聚焦收敛锁3-5条核心思路，不追求当场拍板允许悬而未决。③会后共识发酵几上几下：下发纪要征求各部门意见、争议点开小会深化、反复几轮形成《战略指引》，任正非态度\"好事多磨方向比速度重要\"。④闭环落地：输出战略方向指引（做什么/不做什么/谁负责），接入年度SP/BP规划，专人跟踪定期复盘结果问责。真实案例：20亿级传统零部件企业增长停滞，用此框架定\"从零部件制造→研发试制服务平台\"，一年后新业务营收2亿毛利45%、估值翻倍。",
   exec="会前60天定\"虚\"议题+研究小组+三类角色+换环境；会中2天1晚红蓝军对抗领导只提问不拍板；会后几上几下发酵成《战略指引》不急决策；接入SP/BP闭环+专人跟踪问责。",
   note="适用：③ 高管战略务虚会，「四步法（会前洞察→发散收敛→发酵→闭环）+红蓝军对抗+制造企业翻盘案例」是可迁移真务虚范式。🔍 区别于卡片（wenku闭门SOP——本卡从华为\"几上几下慢发酵+不追求当场拍板\"切入，补「共识需要时间发酵」的心法与实战案例）。"),
 dict(emoji="🏛️",
   title="董事会务虚会（Board Retreat）玩法：限2-3目标 + 20%事实/80%讨论 + 决策落owner/dates",
   cat="董事会务虚", rel="高管间", relcls="r3", srctype="二手",
   src="https://www.saasceo.com/board-retreat",
   val="SaaS CEO 跑董事会务虚会的玩法。设计原则全源共识：retreat 限2-3个目标，提前至少一周发给董事；最大失败是贪多——把十个议题塞进一天，没有哪个得到配得上离场的深度。按自然精力曲线排：上午新鲜时做硬战略思考，午后做更轻更沉淀的活。一日议程模板：到店咖啡非正式落地→CEO框定\"为什么聚+2-3个问题+赢的样子\"→State of Business 20分钟事实40分钟讨论（不是汇报）→深潜#1核心战略问题→工作午餐小组合议→深潜#2增长引擎单位经济→双退出对话（24个月你的/5年买家的）→风险评审→决策/owner/日期→每人一个takeaway收尾。关键纪律：议程上\"没有会议纪要、没有期权审批、没有委员会更新\"，全推到正式董事会；State of Business 只放20%事实（ARR/NRR/CAC回收/现金跑道），其余留给董事解读；能一句话\"我们Rule of 40\"就别展开。",
   exec="retreat 限2-3目标提前一周发；按精力曲线排（上午硬战略/午后轻）；State of Business 20%事实80%讨论只放核心指标；决策当场落owner+dates；纪要/审批/更新推正式会。",
   note="适用：③ 董事会/CEO 级务虚 retreat，「限2-3目标+20%事实80%讨论+决策落owner/dates+把事务推正式会」是可迁移董事会玩法。🔍 区别于卡片（reworkcontent决策优先offsite——本卡聚焦董事会场景\"限目标数+State of Business仅20%事实\"的董事视角纪律）。"),
 dict(emoji="🎯",
   title="高管务虚会「何时请外部引导师」：CEO需在屋中贡献决策→必请，解锁30-40%更多坦诚",
   cat="引导师决策", rel="高管间", relcls="r3", srctype="二手",
   src="https://bondeo-offsites.com/blog/offsite-facilitator-when-to-hire",
   val="决策密集的高管 offsite，引导师是 ROI 最高的一笔支出。何时请：①战略重置/并购后整合/领导层冲突/融资后转向——CEO 是屋里最高职级又需亲自参与决策；②首次办领导团队 offsite，定好格式能复用。铁律：若 CEO 是场内最高职级、又需要为正在做的决策\"贡献\"，就必须请引导师——同一人同一天既当主席又当参与者，两个角色都做不好。好引导师比自助 facilitation 多解锁 30-40% 坦诚，因为他们能中立打断模糊措辞、逼团队做决定。何时不请：纯团建欢乐 retreat（好主持胜过好引导）、单团队 pod retreat（信任已高有结构议程即可）、新人训练营（内部 leader 跑是文化传递）。成本（欧洲2026）：初级€1200-2000/天、资深€2500-4500、顶级€5000-8000+。",
   exec="CEO 既最高职级又需贡献决策→请外部引导师；他们中立打断模糊、逼出决定、解锁30-40%更多坦诚；纯团建/单pod/新人营不必请；按档选日费（资深€2500-4500）。",
   note="适用：③ 高管/CEO 级决策密集 offsite，「CEO需贡献就必请引导师+解锁30-40%坦诚+按场景分级」是可迁移采购决策。🔍 区别于卡片（consultclarity外部vs内部——本卡更短平快给\"请/不请\"硬判据与日费区间，补采购实操）。"),
 dict(emoji="🤝",
   title="裁员/重组后 manager 带队重建信任：倾听会（领导回避）+ 1:1投入 + 团队宪章共创 + 用户手册交换",
   cat="信任重建", rel="上下级", relcls="r2", srctype="二手",
   src="https://www.fulltiltteams.com/blog/team-building-after-layoffs-the-complete-guide-to-rebuilding-trust-culture-and-performance-in-2026",
   val="裁员/重组后团队信任崩了，先承认现实再建。manager 用 offsite/工作坊重建的四步：①倾听会（第1-2周）：6-10人小组合议，只问\"你现在真实经历什么\"\"未来30天什么对你最重要\"，领导不参加；结果匿名汇总回传领导并公开承诺一周内回应主题——成本极低却产出比敬业度调研更真的组织情报。②1:1投入（第2-4周）：manager 与每位直属下属做30分钟\"你怎么样、需要什么\"对话（非绩效、非 workload 重分配），经理角色几乎全在听+承认，不解释不辩护。③团队宪章会（第4-6周）：90分钟引导共创新 Operating Norms——沟通协议（邮件/Slack/面谈各管什么）、决策权（经理定/团队定/需共识）、会议规范、反馈规范、workload 透明——共同写的比领导下发的高遵从低摩擦。④用户手册交换：每人答5问（沟通偏好/好工作日长啥样/什么让我压力及表现/挣扎时我需要经理什么/希望你懂我怎么工作），尤其适合人员大变动的团队。避坑：在现实被承认前搞团建=表演，员工一眼看穿。",
   exec="裁员后先承认现实；第1-2周办领导回避的倾听会（2问，匿名回传+一周承诺）；第2-4周每人30min 1:1纯倾听；第4-6周引导共创团队宪章（沟通/决策/会议/反馈/负荷透明）；人员变动大时做用户手册交换。",
   note="适用：② 一线/中层 manager 在裁员或重组后带团队 offsite 重建信任，「倾听会(领导回避)+1:1倾听+团队宪章共创+用户手册」是可迁移救场框架。🔍 区别于卡片（团队再契约——本卡聚焦\"危机后信任重建\"的时机节奏与领导回避机制，补救场而非日常维护）。"),
 dict(emoji="🔧",
   title="团队成员进出时 manager 带队「再契约（re-contracting）」：刷新团队宪章 + 重建心理安全",
   cat="团队维护", rel="上下级", relcls="r2", srctype="二手",
   src="https://theconversationcompany.co.uk/team-maintenance-a-cornerstone-of-good-leadership",
   val="团队不是建好就不变——人进进出出、优先级移、外部条件变。每次成员变动，manager 别只当招聘/离职流程管，而要当成重置+加固团队文化的机会，办一次\"再契约\"会话：把团队聚起来公开讨论新一章怎么一起工作，专门更新团队宪章/基本规则，鼓励每个人说出\"要感到舒服、发挥最好需要什么\"（哪些规范继续、要不要新建）。让成员发声定什么是重要的，是把文化塑造权交给团队。同步重建心理安全：经理以身作则想要的行为、对新老成员一致公平、邀请提问、耐心等大家适应；可办轻松社交或破冰重建人际连接，让人感到\"我们仍在一起\"。关键是把\"团队维护\"做成领导例行——每次演变都变成强化基础（重对焦目的、刷新规则、加固安全信任）的机会，而非拖累绩效的扰动。",
   exec="成员进出时办\"再契约\"会话更新团队宪章（继续/新建哪些规范）；让成员发声定重要的事；经理以身作则+一致公平+邀请提问重建心理安全；把团队维护做成领导例行而非一次性。",
   note="适用：② 一线/中层 manager 在团队成员变动（入职/离职/转岗）时带团队 offsite/会话「再契约」，刷新宪章+重建心理安全。🔍 区别于卡片（裁员后重建——本卡聚焦\"日常成员变动的例行再契约维护\"而非危机补救，更轻量可复用）。"),
]

def card_html(c):
    return (f'    <div class="hl">\n'
            f'      <div class="top"><span class="emoji">{c["emoji"]}</span><h3>{c["title"]}</h3>'
            f'<span class="cat">{c["cat"]}</span><span class="badge {c["relcls"]}">{c["rel"]}</span>'
            f'<span class="badge {c["srctype"]=="一手" and "b1" or "b2"}">{c["srctype"]}</span></div>\n'
            f'      <p class="val">{c["val"]}</p>\n'
            f'      <details class="exec"><summary>怎么做</summary><div class="inner">{c["exec"]}</div></details>\n'
            f'      <div class="src">🔗 <a href="{c["src"]}" target="_blank">{c["src"]}</a></div>\n'
            f'      <div class="note">{c["note"]}</div>\n'
            f'    </div>\n')

sec3_html = "".join(card_html(c) for c in cards if c["rel"]=="高管间")
sec2_html = "".join(card_html(c) for c in cards if c["rel"]=="上下级")
n3 = sum(1 for c in cards if c["rel"]=="高管间")
n2 = sum(1 for c in cards if c["rel"]=="上下级")
print(f"cards: ③={n3} ②={n2} total={len(cards)}")

# ---------- 1) 增量页 ----------
inc_path = os.path.join(KC, TOPIC, f"{TOPIC}-{RUN_DATE}.html")
inc = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Offsite 团建务虚 · {ROUND}增量（+{len(cards)}）</title>
<style>
:root{{
  --bg:#f4f6fb; --card:#ffffff; --ink:#1f2430; --sub:#5b6478;
  --accent:#6c5ce7; --accent2:#00b8d9; --chip:#eef0ff;
}}
*{{box-sizing:border-box;margin:0;padding:0;}}
body{{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:linear-gradient(135deg,#eef1ff 0%,#e6f7ff 100%);color:var(--ink);padding:28px 18px;line-height:1.6;}}
.wrap{{max-width:1080px;margin:0 auto;}}
.hero{{background:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);border-radius:22px;padding:30px 32px;color:#fff;box-shadow:0 14px 40px rgba(108,92,231,.25);margin-bottom:22px;}}
.hero h1{{font-size:28px;font-weight:800;letter-spacing:1px;margin-bottom:8px;}}
.hero p{{font-size:14px;opacity:.95;}}
.relbar{{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px;}}
.relbar span{{background:rgba(255,255,255,.2);border-radius:20px;padding:5px 14px;font-size:13px;font-weight:600;}}
.grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;}}
.hl{{background:var(--card);border-radius:18px;padding:18px 18px 16px;border-top:4px solid var(--accent);box-shadow:0 10px 32px rgba(108,92,231,.10);display:flex;flex-direction:column;gap:9px;}}
.top{{display:flex;align-items:center;gap:8px;flex-wrap:wrap;}}
.emoji{{font-size:22px;}}
.hl h3{{font-size:16px;font-weight:700;flex:1;min-width:120px;}}
.cat{{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:600;background:var(--chip);color:var(--accent);}}
.badge{{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:700;}}
.b2{{background:#fff1e6;color:#c0651a;}}
.b1{{background:#e6f9ed;color:#1a9e5a;}}
.r1{{background:#eaf2ff;color:#2b6cb0;}}
.r2{{background:#fff3e0;color:#c0651a;}}
.r3{{background:#f3e8ff;color:#7b2cbf;}}
.val{{font-size:13.5px;color:var(--sub);}}
.exec{{margin-top:2px;border-top:1px dashed #e2e8f0;padding-top:8px;}}
.exec summary{{cursor:pointer;font-size:13px;font-weight:600;color:var(--accent);}}
.exec .inner{{font-size:13px;color:var(--sub);margin-top:6px;padding-left:4px;}}
.src{{font-size:12px;word-break:break-all;}}
.src a{{color:var(--accent2);text-decoration:none;}}
.note{{font-size:12px;color:#94a3b8;border-left:3px solid #e2e8f0;padding-left:8px;}}
footer{{text-align:center;padding:24px;color:#94a3b8;font-size:13px;border-top:1px solid #e2e8f0;margin-top:40px;}}
</style>
</head>
<body>
<div class="wrap">
  <p style="margin:0 0 16px"><a href="offsite.html" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">📑 返回 Offsite 累计卡片墙 →</a> &nbsp; <a href="https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/offsite/offsite.html" style="display:inline-block;background:#e6f7ff;color:#00b8d9;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">🌐 线上累计墙</a></p>
  <div class="hero">
    <h1>🏔️ Offsite 团建务虚 · {ROUND}增量页（+{len(cards)}）</h1>
    <p>采集于 {RUN_DATE[:4]}-{RUN_DATE[4:6]}-{RUN_DATE[6:]} ｜ 本轮新增 {len(cards)} 张（③高管间 {n3} + ②上下级 {n2}）｜ 仅 ②上下级 / ③高管间，已剔除平级/朋友向 ｜ 六维评估通过</p>
    <div class="relbar">
      <span>② 领导↔员工（上下级，supervisor）</span>
      <span>③ 领导↔领导（高管间，exec）</span>
    </div>
  </div>
  <div class="grid">
{sec3_html}{sec2_html}  </div>
<footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>
</div>
</body>
</html>
'''
open(inc_path, "w", encoding="utf-8").write(inc)
print("增量页:", inc_path, len(inc.encode("utf-8")), "B")

# ---------- 2) 汇总页注入 ----------
summary_path = os.path.join(KC, TOPIC, f"{TOPIC}.html")
html = open(summary_path, encoding="utf-8").read()
# sec3 grid (first)
k = html.find('<div class="grid">')
html = html[:k+len('<div class="grid">')] + sec3_html + "\n" + html[k+len('<div class="grid">'):]
# sec2 grid (second, after sec2 marker)
i = html.find('<div class="sec sec2">')
j = html.find('<div class="grid">', i)
html = html[:j+len('<div class="grid">')] + sec2_html + "\n" + html[j+len('<div class="grid">'):]
# counts
html = html.replace("67 卡", "71 卡", 1)
html = html.replace("46 卡", "48 卡", 1)
# hero narrative
html = html.replace("2026-08-18 十八轮补采 +3", "2026-08-18 十八轮补采 +3 ｜ 2026-08-19 十九轮补采 +6", 1)
open(summary_path, "w", encoding="utf-8").write(html)
print("汇总页更新: 113 -> 119 卡 (③71/②48)")

# ---------- 3) index.json ----------
idx = json.load(open(os.path.join(KC, "index.json"), encoding="utf-8"))
base = max((e.get("id",0) for e in idx if isinstance(e.get("id"),int)), default=0)
for c in cards:
    rel_v = "exec" if c["rel"]=="高管间" else "supervisor"
    st_v = "primary" if c["srctype"]=="一手" else "secondary"
    idx.append({
        "title": c["title"],
        "normKey": re.sub(r"\s+"," ", c["title"].lower()).strip(),
        "url": c["src"],
        "sourceType": st_v,
        "relation": rel_v,
        "summary": c["val"][:120],
        "topic": TOPIC,
    })
json.dump(idx, open(os.path.join(KC, "index.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("index.json +%d -> %d 条" % (len(cards), len(idx)))

# ---------- 4) Obsidian 笔记 ----------
note_path = os.path.join(VAULT, "素材", TOPIC, "Offsite-团建务虚-知识卡汇总.md")
note = open(note_path, encoding="utf-8").read()
note = note.replace("（112 卡 · 上下级/高管间）", "（119 卡 · 上下级/高管间）", 1)
note = note.replace("2026-08-18 十八轮补采 +3。", "2026-08-18 十八轮补采 +3 ｜ 2026-08-19 十九轮补采 +6。", 1)
note = note.replace("— 67 卡", "— 71 卡", 1)
note = note.replace("— 46 卡", "— 48 卡", 1)
# round section before 20260818
round_block = (f"## 轮次 {RUN_DATE}（+{len(cards)}）\n\n"
               f"| 关系档 | 新增卡 |\n|---|---|\n"
               + "".join(f"| {c['rel']} | {c['title']} |\n" for c in cards) + "\n")
note = note.replace("## 轮次 20260818（+3）", round_block + "## 轮次 20260818（+3）", 1)
# append ③ rows before '## ② '
rows3 = "".join(f"| {68+i} | {c['title']} | 二手 |  |\n" for i,c in enumerate([x for x in cards if x['rel']=='高管间'])) 
idx2 = note.find("\n## ② ")
note = note[:idx2] + rows3 + note[idx2:]
# append ② rows before '## 适用&备注'
rows2 = "".join(f"| {47+i} | {c['title']} | 二手 |  |\n" for i,c in enumerate([x for x in cards if x['rel']=='上下级']))
idx3 = note.find("\n## 适用&备注")
note = note[:idx3] + rows2 + note[idx3:]
open(note_path, "w", encoding="utf-8").write(note)
print("Obsidian 笔记更新: 轮次 + 表尾 +4/+2 行")

# ---------- 5) 00-索引 ----------
idx0_path = os.path.join(VAULT, "00-知识采集索引.md")
idx0 = open(idx0_path, encoding="utf-8").read()
idx0 = idx0.replace("**110 卡**", "**119 卡**", 1)
idx0 = idx0.replace("③高管间 65 卡 / ②上下级 45 卡", "③高管间 71 卡 / ②上下级 48 卡", 1)
idx0 = idx0.replace("2026-08-17 十六轮补采 +6）", "2026-08-17 十六轮补采 +6 ｜ 2026-08-19 十九轮补采 +6）", 1)
# append 6 rows before '## 主题：破冰'
newrows = "".join(
    f"| {c['title']}（offsite.html） | 4 | {c['srctype']} | {c['rel']} | {c['val'][:40]} |\n"
    for c in cards)
bi = idx0.find("\n## 主题：破冰")
idx0 = idx0[:bi] + newrows + idx0[bi:]
open(idx0_path, "w", encoding="utf-8").write(idx0)
print("00-索引更新: offsite 段 +6 行 + 计数")

# ---------- 6) 门户 ----------
portal = os.path.join(KC, "index.html")
p = open(portal, encoding="utf-8").read()
p = p.replace('<div class="cnt">110 卡</div>', '<div class="cnt">119 卡</div>', 1)
p = p.replace("二手 539 张", "二手 545 张", 1)
open(portal, "w", encoding="utf-8").write(p)
print("门户更新: offsite 110->119, 二手 539->545")

print("\nDONE build. N=%d, ③=%d, ②=%d" % (len(cards), n3, n2))
