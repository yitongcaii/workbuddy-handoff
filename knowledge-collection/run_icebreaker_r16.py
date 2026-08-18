# -*- coding: utf-8 -*-
"""知识采集自动化 · 破冰 第16轮（2026-08-18 晚）注入脚本。
把 8 张新卡（4×③高管间 + 4×②上下级）注入 icebreaker.html 累计墙，
写 .run_newcards.tmp.html，并追加到 index.json。动态重算 tag 计数。"""
import json, re, os

BASE = r"C:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection"
WALL = os.path.join(BASE, "icebreaker", "icebreaker.html")
TMP = os.path.join(BASE, "icebreaker", ".run_newcards.tmp.html")
IDX = os.path.join(BASE, "index.json")

REL_LABEL = {"r2": "上下级", "r3": "高管间"}
SRC_LABEL = {"b1": "一手", "b2": "二手"}

CARDS = [
    # ---- ② 上下级 ----
    dict(emoji="💬", title="留任访谈(Stay Interview)·11 问建信任留人（经理↔员工）", cat="留任访谈",
         rel="r2", src="b2",
         val="Stay Interview=经理与直属员工的定期一对一，主动问『什么让你想留下 / 什么可能让你走』，在人才 emotionally check out 前干预（区别于事后 exit interview）。11 问按序：①你最期待工作的哪部分 ②最不喜欢哪部分 ③工作生活平衡如何改善 ④为何留下来 ⑤对公司认可策略怎么看 ⑥近月有无焦虑/是否缓解 ⑦学习成长机会如何 ⑧在此学到了什么/还想学什么 ⑨我能做什么改善你的体验 ⑩理想工作长什么样 ⑪是否曾考虑离职、因何。成功关键：高管背书+经理↔下属配对最稳+新人满 60 天再做+持续而非一次。落点：把『我们关心你、想让你留下』变成行动，员工在被听见前主动谈隐患。",
         exec="留任访谈用 11 问按『喜欢→不喜欢→平衡→留任意愿→成长→我能做什么→理想职位→离职念头』顺序挖；设私密无评判环境、listen without defensiveness、不做兑现不了的承诺、会后闭环快赢+长期计划并回查；新人 60 天后、关键岗位定期做。",
         url="https://skillhubs.io/employee-retention-stay-interviews",
         label="skillhubs.io/employee-retention-stay-interviews",
         note="适用：② 经理↔员工定期留任访谈——在离职前挖动机、建信任，替代只做 exit interview 的事后诸葛。"),
    dict(emoji="📋", title="留任访谈模板·量表+选择题+关系诊断（轻量可落地）", cat="留任访谈",
         rel="r2", src="b2",
         val="Stribe 留任访谈模板=把敏感对话变轻量结构化工具：9 道混合题型（多选/1-10 量表/开放），覆盖『最舍不得放弃的工作部分(多选+追问)』『想改善的一块(多选+改动)』『近半年是否想过跳槽(多选+诱因)』『能否不带后果地说真话(1-10)』『哪种认可最有意义(多选)』『优势是否充分发挥(1-10)』『归属感(1-10)』『与经理关系如何(多选)』『若别的公司明天 offer 接受度(1-10)』。避坑：勿当绩效面谈、问了不行动最伤信任、别太正式、别做一次就停。落点：用量表把『感受』变可追踪信号，经理用咖啡式闲聊而非审讯。",
         exec="留任访谈用轻量量表+多选模板（归属感/真话安全感/优势发挥/离职倾向各 1-10），把主观感受量化；氛围走咖啡闲聊非审讯、明确『说真话无后果』、问后必有行动闭环、纳入长期 engagement 策略而非一次性。",
         url="http://www.stribehq.com/resources/stay-interviews/",
         label="stribehq.com/resources/stay-interviews",
         note="适用：② 经理用轻量量表化留任访谈——把信任/归属感/离职风险变可测信号，低门槛高频做。"),
    dict(emoji="🩹", title="冲突后团队信任修复工作坊·90 分钟剧本（SBI+Lencioni）", cat="信任修复",
         rel="r2", src="b2",
         val="90 分钟冲突后修复剧本：先用 Lencioni 五 dysfunction 举手/点投定位最痛 2-3 项（不贪全），映射到心理安全感/赋能/沟通三层；50-70min『清场对话』用 SBI(情境-行为-影响)结构——引导师先低风险示范，每人讲一个具体有日期的瞬间，接收者只说『谢谢，让我想想』不辩解，资深者先接（CEO 接不住则工作坊失效），20min 内 3-5 个足够；70-85min 写承诺卡（『我将开始/停止的具体行为』+『我需要团队什么』），轮流读 2min/人；85-90min 收尾一句话。铁律：散会前就把 3 周后的 30min 复盘+再承诺排上日历，否则行为改变一个月内蒸发。",
         exec="冲突后修复用 90min 剧本：Lencioni 定位最痛 2-3 dysfunction→SBI 清场对话(具体有日期瞬间、接收者不辩解、资深先接)→每人写『开始/停止的具体行为+所需支持』卡并轮流读→散会前锁定 3 周后 30min 复盘。specificity 是药，vagueness 是敌。",
         url="https://www.unicornlabs.ca/blog/team-trust-workshop",
         label="unicornlabs.ca/blog/team-trust-workshop",
         note="适用：② 冲突后团队信任修复——SBI 具体对话+承诺卡+3周复盘闭环，而非道歉了事。"),
    dict(emoji="🔗", title="重建团队凝聚力·经理实操 7 步（目标/倾听/规则/认可）", cat="团队凝聚力",
         rel="r2", src="b2",
         val="冲突后/低动能团队重建凝聚力的实操 7 步：①定共享目标——把个人责任转向集体项目，每人看到贡献如何服务总目标；②鼓励沟通与积极倾听——建立『说该说的哪怕不舒服』的透明文化，设自由表达空间；③团建活动——密室/烹饪/徒步/角色扮演/头脑风暴，在非工作语境里认识彼此；④定清晰行为准则——角色分工/冲突处理流程/内部沟通政策/职业操守；⑤推公司文化——庆祝里程碑、认可个人贡献、包容多元；⑥快速有效解决冲突——冷静中立、听全各方、寻妥协、跟踪调整；⑦认可个人贡献——正式+非正式认可 booster 士气。落点：凝聚力不是一次活动，是日常透明沟通+持续认可的小行动累积。",
         exec="重建凝聚力走 7 步：共享目标对齐→透明沟通+积极倾听→非工作语境团建→清晰行为准则→文化庆祝与认可→快速中立解冲突→持续个人贡献认可；把『说该说的』当核心价值观，用日常小行动而非一次性活动累积信任。",
         url="https://www.archetype-eu.com/en/how-to-rebuild-team-cohesion",
         label="archetype-eu.com/en/how-to-rebuild-team-cohesion",
         note="适用：② 经理重建低动能/冲突后团队凝聚力——目标对齐+透明沟通+持续认可七步。"),
    # ---- ③ 高管间 ----
    dict(emoji="🗳️", title="高管 Offsite 2 日议程·产出对齐与决策（决策块+RACI/DACI）", cat="高管Offsite",
         rel="r3", src="b2",
         val="高管 offsite 的核心不是 vibes 是决策。2 日模板：D0 预读 2 页决策简报+脉搏调研(最大错位/风险/该停的事)；D1 08:30 定规则+check-in『我需要团队给我什么才能最好工作』→决策块1/2(静读→澄清→结构化辩论→首投→收敛→决定→记录)→工作午餐『我一直在回避的取舍』→操作系统工作坊(决策权 RACI/DACI、升级路径、规划节奏、KPI 体检)→连接爆发(红队策略/静默头脑风暴后响亮辩论/前测 pre-mortem/工作风格互换)→决策块3；D2 决策块4→风险前测→资源排序(都优先=都不优先)→操作系统仪式锁定→关系澄清(期望/反馈偏好/与我共事手册)→沟通计划(谁何时从谁那听到什么)→决策日志终核。金句：能把讨论变承诺的 offsite 才 stick；高管不要信任摔，要短促有用的摩擦。",
         exec="高管 offsite 用 2 日决策型议程：预读简报+脉搏调研→多轮『静读-辩论-首投-决定-记录』决策块→RACI/DACI 操作系统工作坊→连接爆发(red-team/pre-mortem/工作风格互换)→关系澄清+沟通计划+决策日志终核；请外部引导师解锁 30-40% 更多坦率，杜绝 vibes 不落地。",
         url="https://www.scavify.com/blog/executive-team-building-retreats-that-align-leaders",
         label="scavify.com/blog/executive-team-building-retreats",
         note="适用：③ 高管 offsite 决策型 2 日议程——决策块+操作系统(RACI/DACI)+连接爆发，重承诺落地。"),
    dict(emoji="🧭", title="高管 Offsite 五块议程·30 天强化才 stick（buildingteams）", cat="高管Offsite",
         rel="r3", src="b2",
         val="高管/领导 offsite 同一套五块结构（顺序不能乱）：①定『30 天后什么必须不同』这一个结果→倒推建议程；②Reset the Flag(对齐未来一季服务的 2-3 优先级，定不出就是 offsite 本身)；③The honest conversation(团队一直绕着走、从不直面的那个话题，CEO 当参与者非裁判)；④把谈话变决策(每个开放问题收口：一个 owner+一个 deadline+必须 defend)；⑤Set the Standard(定彼此要守住的 bar，错过怎么办)+30 天强化(最易被砍却决定成败的一块：谁在哪一会检查什么)。时长 2-3 天(抵达放松→全天工作→半天承诺)；1 天压缩保留结构，半天只做 honest conversation+决策+强化。金句：没有强化块的 offsite 是大多数领导 offsite 不 stick 的原因。",
         exec="高管 offsite 五块法：先定『30 天后哪点必须不同』→Reset the Flag(2-3 优先级)→honest conversation(CEO 参与非裁判)→变决策(owner+deadline+defend)→Set the Standard+30 天强化(谁在哪会检查)；无论几天，最后一块(强化)必保，否则一周内蒸发。",
         url="https://www.buildingteams.com/resources/executive-offsite-agenda",
         label="buildingteams.com/resources/executive-offsite-agenda",
         note="适用：③ 高管 offsite 五块议程——honest conversation+决策+30 天强化闭环，杜绝热闹不落地。"),
    dict(emoji="🏛️", title="领导力 Offsite 2.5 天议程·外部引导师 ROI（bondeo）", cat="高管Offsite",
         rel="r3", src="b2",
         val="领导力 offsite 是企业日历上杠杆最高的会——房间里人天成本极高，必须产出决策非氛围。实战格式：8-16 人、2.5 天(更大变广播、更短丢第二天突破)；场地要修道院感非节日感(山林小屋/静谧精品酒店，避开度假村)。样例 3 日议程：D1 个人 check-in→年度诚实复盘→战略优先级工作坊；D2 战略红队→top3 赌注前测→1:1 散步配对→组织设计+人才复盘→close+合影；D3 承诺→离场。必带：对去年承诺的诚实成绩单、一页战略草稿(供攻击非从零写)、top10 人才评估(姓名/层级/留任风险)、top3 战略赌注(成功标准已写好)、提前 7 天预读、手机入篮。铁律：always 请外部引导师——再强的 CEO 也难引导自己所在的房间，好引导师多解锁 30-40% 坦率，欧洲预算 €2500-6000/天当最高 ROI 项。",
         exec="领导力 offsite 用 8-16 人 2.5 天格式(修道院感场地避开度假村)；必带诚实成绩单+一页战略草稿+top10 人才评估+top3 赌注+7 天预读+手机入篮；always 请外部引导师(多解锁 30-40% 坦率，预算当最高 ROI)；议程 honest 复盘→红队→人才→承诺，CEO 不当裁判。",
         url="https://bondeo-offsites.com/blog/leadership-offsite-ideas",
         label="bondeo-offsites.com/blog/leadership-offsite-ideas",
         note="适用：③ 领导力 offsite 2.5 天实操——外部引导师 ROI+必带物料清单+红队/人才复盘议程。"),
    dict(emoji="🧩", title="领导团队凝聚力工作坊·2-3h 结构+避坑（culturevitale）", cat="领导力工作坊",
         rel="r3", src="b2",
         val="领导力团队凝聚力工作坊设计：价值与领导身份工作坊(每人讲个人领导价值观及在角色中如何/未体现，成对先分享再全组)→团队效能评估(评『我们作为团队』如何运作，引导师优先诚实非舒适)→同侪教练圈(每人抛一个战略/领导挑战，他人只问教练问题不给建议不安慰，建模倾听)→建设性分歧工作坊(教结构化实质性分歧：挑战观点不挑战身份、压力下守立场、改立场不失面子)。2-3h 样例结构：0-10 定规则→10-30 个人反思(我珍视/我希望不同)→30-55 成对分享→55-1:20 全组综合(引导师映射主题不归因个人)→1:20 休息→1:30-2:00 凝聚活动→2:00-2:30 工作规范(承诺 3 具体行为)→2:30-2:45 问责结构→2:45-3:00 收尾一词。避坑：先诊断再活动(别在信任裂痕上盖表演性正能量)、裂痕团队用外部引导师(内部 HRBP 也难中立)、安全建好再要脆弱、承诺要在随后 2-3 次会回看、高管须以真 peer 参与非观察员、警惕 groupthink(高凝聚+低挑战=错)。",
         exec="领导团队凝聚力工作坊用 2-3h 结构：个人反思→成对分享→全组综合(不归因个人)→凝聚活动→承诺 3 具体行为→问责结构→收尾；先诊断真实问题再上活动、裂痕团队必请外部引导师、安全建好才要脆弱、承诺在随后会议回看防蒸发、高管以 peer 参与、警惕高凝聚低挑战的 groupthink。",
         url="https://culturevitale.com/journal/team-cohesion-activities-workshops-exercises",
         label="culturevitale.com/journal/team-cohesion-activities",
         note="适用：③ 领导团队凝聚力工作坊——2-3h 结构+五大避坑(外部引导师/先诊断/防 groupthink)。"),
]


def card_html(c):
    rel = REL_LABEL[c["rel"]]
    src = SRC_LABEL[c["src"]]
    return (
        '  <div class="hl">\n'
        f'      <div class="top"><span class="emoji">{c["emoji"]}</span><h3>{c["title"]}</h3>'
        f'<span class="cat">{c["cat"]}</span><span class="badge {c["rel"]}">{rel}</span>'
        f'<span class="badge {c["src"]}">{src}</span></div>\n'
        f'      <p class="val">{c["val"]}</p>\n'
        f'      <details class="exec"><summary>怎么做</summary><div class="inner">{c["exec"]}</div></details>\n'
        f'      <div class="src">🔗 <a href="{c["url"]}" target="_blank">{c["label"]}</a></div>\n'
        f'      <div class="note">{c["note"]}</div>\n'
        '    </div>\n'
    )


sec3_cards = [c for c in CARDS if c["rel"] == "r3"]
sec2_cards = [c for c in CARDS if c["rel"] == "r2"]
blocks3 = "".join(card_html(c) for c in sec3_cards)
blocks2 = "".join(card_html(c) for c in sec2_cards)

html = open(WALL, encoding="utf-8").read()

# 动态计数：sec3 = sec2 标记之前的 hl 数；sec2 = sec2 标记之后 footer 之前的 hl 数
sec2_marker = '<div class="sec sec2">'
assert sec2_marker in html, "sec2 marker missing"
assert "<footer>" in html, "footer missing"
idx_sec2 = html.index(sec2_marker)
idx_footer = html.index("<footer>")
n_sec3_before = html[:idx_sec2].count('<div class="hl">')
n_sec2_before = html[idx_sec2:idx_footer].count('<div class="hl">')

# 注入：③ 在 sec2 标记前（sec3 grid 末尾）；② 在 footer 前（sec2 grid 末尾）
html = html.replace(sec2_marker, blocks3 + sec2_marker, 1)
html = html.replace("<footer>", blocks2 + "<footer>", 1)

n_sec3 = n_sec3_before + len(sec3_cards)
n_sec2 = n_sec2_before + len(sec2_cards)

# 替换 sec3 / sec2 的 tag 计数
html = re.sub(r'(<div class="sec sec3">.*?<span class="tag">)\d+ 卡(</span>)',
              lambda m: m.group(1) + f"{n_sec3} 卡" + m.group(2), html, count=1, flags=re.S)
html = re.sub(r'(<div class="sec sec2">.*?<span class="tag">)\d+ 卡(</span>)',
              lambda m: m.group(1) + f"{n_sec2} 卡" + m.group(2), html, count=1, flags=re.S)

# hero <p> 追加 r16 说明
m = re.search(r'(<div class="hero">.*?<p>)(.*?)(</p>)', html, re.S)
assert m, "hero p not found"
r16 = (' ｜ 十六轮补采 +8（2026-08-18 晚）：留任访谈 Stay Interview 11 问(skillhubs)/留任访谈轻量量表模板(stribehq)（②）；'
       '冲突后 90 分钟信任修复工作坊 SBI+Lencioni(unicornlabs)/重建团队凝聚力 7 步(archetype)（②）；'
       '高管 Offsite 2 日决策议程 RACI/DACI(scavify)/高管 Offsite 五块+30 天强化(buildingteams)/领导力 Offsite 2.5 天外部引导师 ROI(bondeo)/领导团队凝聚力工作坊 2-3h+culturevitale 避坑（③）')
new_p = m.group(2) + r16
html = html[:m.start()] + m.group(1) + new_p + m.group(3) + html[m.end():]

open(WALL, "w", encoding="utf-8").write(html)

# 写 run tmp（当轮新增全 8 张）
open(TMP, "w", encoding="utf-8").write(blocks3 + blocks2)

# 追加 index.json（去重按 URL）
idx = json.load(open(IDX, encoding="utf-8"))
existing_urls = {e.get("url") for e in idx}
added = 0
for c in CARDS:
    if c["url"] in existing_urls:
        continue
    norm = re.sub(r'[\s\W]+', '', c["title"]).lower()
    rel = "exec" if c["rel"] == "r3" else "supervisor"
    idx.append({
        "title": c["title"],
        "normKey": norm,
        "url": c["url"],
        "sourceType": "primary" if c["src"] == "b1" else "secondary",
        "relation": rel,
        "topic": "icebreaker",
        "summary": c["val"],
    })
    added += 1
json.dump(idx, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

print(f"OK wall injected | sec3 {n_sec3_before}->{n_sec3} | sec2 {n_sec2_before}->{n_sec2} | "
      f"new cards={len(CARDS)} | index added={added} | total index={len(idx)}")
