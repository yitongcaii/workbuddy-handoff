# -*- coding: utf-8 -*-
import json, os, tempfile, re

KC = os.path.dirname(os.path.abspath(__file__))
IDX = os.path.join(KC, "index.json")
OFF = os.path.join(KC, "offsite", "offsite.html")
PORTAL = os.path.join(KC, "index.html")
NOTE = r"C:\Users\v_yitcai\Documents\Obsidian\知识采集库\素材\offsite\Offsite-团建务虚-知识卡汇总.md"
ZERO = r"C:\Users\v_yitcai\Documents\Obsidian\知识采集库\00-知识采集索引.md"

def atomic_write(path, text):
    d = os.path.dirname(path)
    fd, tmp = tempfile.mkstemp(dir=d, suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp, path)

# ---------- 1) NEW CARDS ----------
cards = [
 dict(title="董事会/治理型 retreat（治理干预·五段强议程）", cat="治理 retreat", emoji="🏛️",
      url="https://giddingsconsulting.com/blog/nonprofit-board-retreat-facilitator",
      display="giddingsconsulting.com/blog/nonprofit-board-retreat-facilitator",
      rel="exec", src="二手",
      summary="董事会/治理型 retreat 不是激励会而是「治理干预」：把“对齐/参与/战略/文化/治理”等宽泛主题转成具体交付物（top-3 战略优先级清单+owner+时间线、董事会参与协议、委员会章程更新、董事会运营协议、继任 90 天计划）；强议程五段（开场定战略时刻→诚实评估董事会表现→战略决策块聚焦 2-3 个关键问题深挖→承诺设计每条绑定 owner/时间/资源→会前就设计好 30 天/90 天跟进）；选引导师看 fit 而非 charisma。",
      how="把主题先转成可交付物而非口号；强议程五段+聚焦 2-3 个决策深挖；每条承诺绑定 owner+时间线；30/90 天跟进前置设计；引导师评估重 fit 与跟进流程。",
      note="适用：③ 董事会/治理层 retreat，把务虚转成治理交付物是可迁移亮点，区别于纯战略务虚。"),
 dict(title="文化转型·价值观重置 offsite（Day1 消 silo + Day2 战略）", cat="文化转型", emoji="🔄",
      url="https://www.theculturefix.works/strategic-offsite",
      display="theculturefix.works/strategic-offsite",
      rel="exec", src="二手",
      summary="Culture-First 战略 offsite：Day1 消除 silo、修复团队动态、对齐“作为领导团队如何运作”，Day2 定公司明年计划与各 leader 认领季度目标；含会前文化测评 + 会后 30 天进度复盘；产出 = 领导层“我们是最重要的团队”心智 + 人际信任 + 全员可执行的年度路线图。文化+战略双轨确保周一上班不褪色。",
      how="Day1 消 silo+修复动态+对齐运作方式；Day2 定明年计划+leader 认领季度目标；会前文化测评+会后 30 天复盘；文化战略双轨防褪色。",
      note="适用：③ 领导团队文化转型/价值观重置 offsite，双日文化+战略结构是可迁移亮点。"),
 dict(title="新整合领导团队 offsite·建立 operating norms（并购/新组）", cat="整合 offsite", emoji="🤝",
      url="https://www.jrgpartners.com/leadership-offsite-agenda-template-new-executive-team-integration",
      display="jrgpartners.com/.../new-executive-team-integration",
      rel="exec", src="二手",
      summary="并购/新组建高管团队的整合 offsite 议程模板：围绕信任/方向对齐/角色接口/显式 operating norms/已疏通张力设计，而非“愉快休息”；最易被跳过也最重要的一步 = 显式建立团队如何运作（决策/沟通/冲突/问责规范），自引导常回避真实张力须外部引导师；offsite 只是起点，会后跟进才固化整合。🔍 区别于「并购后90天文化Charter」「Bain四工作坊」卡——本卡聚焦新整合领导团队的 operating norms 建立议程模板。",
      how="围绕整合结果(信任/对齐/角色接口/operating norms/张力)设计；最优先显式建立决策/沟通/冲突/问责规范；用外部引导师直面真实张力；会后跟进固化。",
      note="适用：③ 并购后/新组建高管团队整合 offsite，operating norms 议程模板是可迁移亮点。"),
 dict(title="远程/混合团队文化塑造 offsite（节奏框架）", cat="文化塑造", emoji="🌐",
      url="https://www.offsite.com/blog/remote-work-culture",
      display="offsite.com/blog/remote-work-culture",
      rel="supervisor", src="二手",
      summary="远程团队文化塑造 offsite：会前做内部审计（敬业度调研/1:1 听痛点）让议程对症；结构把“文化工作”嵌入而非附带——开场命名文化目的、价值观工作坊/引导式复盘/讲故事(为何加入)/跨职能展示造共同参照、用物理环境(山间/可步行社区)降正式感、引入仪式(表彰价值观楷模/共餐/结尾每人写一条带回远程工作的承诺)让文化 sticky；节奏框架：早期团队(<30人)季度或至少半年一次、中型(30-150)年度全员+小队补、企业级年度全员+LE/ERG/区域聚会；2-3 天为甜点区。",
      how="会前内部审计(调研/1:1)让议程对症；文化工作嵌入结构(价值观工作坊/复盘/讲故事/跨职能展示)；用环境降正式感+仪式造黏性；按团队阶段定节奏(早期季度/中型年度/企业年度+LE)。",
      note="适用：② 管理者带远程/混合团队做文化塑造 offsite，节奏框架+仪式化是可迁移亮点。"),
 dict(title="团建/务虚 ROI 三层测量（HR 视角·防 vanity）", cat="ROI测量", emoji="📊",
      url="https://bondeo-offsites.com/blog/offsite-roi-measurement",
      display="bondeo-offsites.com/blog/offsite-roi-measurement",
      rel="supervisor", src="二手",
      summary="团队 offsite ROI 三层框架：L1 情绪(第1周)会前 2 周与会后 5 天同卷测信任/清晰度/能量 delta；L2 行为(第30天)数承诺兑现数/跨团队会议数/此前从不互 DM 的人是否开始联络；L3 结果(第90天)留存/内推/战略里程碑——客户数据中位数 offsite 仅靠留存节省 4 个月内回本(留住 1 名资深 IC 即覆盖 30 人 €2500/人)。须忽略：会后 NPS(只测后勤)/Slack 照片/社媒数/CEO 感觉好——都是 vanity。🔍 区别于「高管 Retreat ROI(SAS/RQI/OFS)」卡——本卡是 HR/团队务实 ROI + 防 vanity 指标。",
      how="三层(情绪/行为/结果)在 W1/D30/D90 分别测；会前 2 周基线卷对照；D30 数承诺兑现与跨团队联络；D90 看留存/内推；坚决忽略 NPS/照片/社媒等 vanity。",
      note="适用：② 管理层/HR 论证团队务虚 ROI，三层框架+防 vanity 是可迁移亮点。"),
 dict(title="远程团队线下 reconnect·最高 ROI morale 投资", cat="团队 reconnect", emoji="🤝",
      url="https://www.offsite.com/blog/employee-morale-suggestions-remote-team",
      display="offsite.com/blog/employee-morale-suggestions-remote-team",
      rel="supervisor", src="二手",
      summary="远程优先团队 morale：虚拟互动(随机咖啡/非工作 Slack 频道/认可系统)只能“维持”不能“转化”——研究一致表明一年一次线下聚首对归属感的作用 >12 个月虚拟 happy hour；高影响 retreat 四特征：非结构化时间 ≈ 议程重要(晚餐/徒步/会前 20 分钟)、共享物理体验造情感记忆(烹饪课/徒步/共创)、节目反映团队文化而非默认公司格式、跟进(half-life：连接须靠后续沟通与认可强化)。HBR：面对面建信任/连接显著优于数字。",
      how="用一年一次线下聚首替代 12 个月虚拟维持；保留非结构化时间(晚餐/徒步)≈议程；造共享物理体验情感记忆；节目反映团队文化；跟进 half-life 靠后续沟通与认可。",
      note="适用：② 管理者带远程团队做线下 reconnect，morale 投资 ROI 论证 + half-life 跟进是可迁移亮点。"),
]

def norm(s):
    s = s.lower()
    out = []
    for ch in s:
        if ch.isalnum() or "\u4e00" <= ch <= "\u9fff":
            out.append(ch)
    return "".join(out)

# ---------- 2) INDEX.JSON DEDUP + APPEND ----------
with open(IDX, encoding="utf-8") as f:
    data = json.load(f)
existing_urls = {e.get("url","") for e in data}
existing_nk = {e.get("normKey","") for e in data}
N, M = 0, 0
for c in cards:
    nk = norm(c["title"])
    if c["url"] in existing_urls or nk in existing_nk:
        M += 1
        continue
    data.append({
        "title": c["title"], "normKey": nk, "url": c["url"],
        "sourceType": c["src"], "relation": c["rel"], "summary": c["summary"],
        "topic": "offsite"
    })
    existing_urls.add(c["url"]); existing_nk.add(nk)
    N += 1
atomic_write(IDX, json.dumps(data, ensure_ascii=False, indent=2) + "\n")
print("index.json: +%d 去重删 %d  → total %d" % (N, M, len(data)))

# count 一手/二手
primary = sum(1 for e in data if e.get("sourceType")=="一手")
secondary = sum(1 for e in data if e.get("sourceType")=="二手")
print("一手 %d / 二手 %d" % (primary, secondary))

# ---------- 3) OFFSITE.HTML INJECT ----------
with open(OFF, encoding="utf-8") as f:
    html = f.read()

def html_block(c):
    rlabel = "高管间" if c["rel"]=="exec" else "上下级"
    rcls = "r3" if c["rel"]=="exec" else "r2"
    return (
        '    <div class="hl">\n'
        '      <div class="top"><span class="emoji">%s</span><h3>%s</h3><span class="cat">%s</span>'
        '<span class="badge %s">%s</span><span class="badge b2">二手</span></div>\n'
        '      <p class="val">%s</p>\n'
        '      <details class="exec"><summary>怎么做</summary><div class="inner">%s</div></details>\n'
        '      <div class="src">🔗 <a href="%s" target="_blank">%s</a></div>\n'
        '      <div class="note">适用：%s</div>\n'
        '    </div>\n' % (c["emoji"], c["title"], c["cat"], rcls, rlabel,
                          c["summary"], c["how"], c["url"], c["display"], c["note"])
    )

# split exec (③) and sup (②)
exec_cards = [c for c in cards if c["rel"]=="exec"]
sup_cards  = [c for c in cards if c["rel"]=="supervisor"]
sec3_block = "".join(html_block(c) for c in exec_cards)
sec2_block = "".join(html_block(c) for c in sup_cards)

# inject ③ before sec3 grid close (marker unique between sec3 grid and sec2)
marker3 = '</div>\n\n  <div class="sec sec2">'
assert marker3 in html, "sec3 marker not found"
html = html.replace(marker3, sec3_block + marker3, 1)
# inject ② before sec2 grid close (marker unique before footer)
marker2 = '</div>\n\n  <footer>'
assert marker2 in html, "sec2 marker not found"
html = html.replace(marker2, sec2_block + marker2, 1)

# update section count tags
html = html.replace('<span class="tag">32 卡</span>', '<span class="tag">35 卡</span>', 1)
html = html.replace('<span class="tag">20 卡</span>', '<span class="tag">23 卡</span>', 1)
# hero line
html = html.replace('｜ 2026-08-10 七轮补采 +10',
                    '｜ 2026-08-10 七轮补采 +10｜ 2026-08-10 八轮补采 +6', 1)
atomic_write(OFF, html)
print("offsite.html injected +3(③) +3(②); sec3=35 sec2=23")

# ---------- 4) OBSIDIAN NOTE ----------
with open(NOTE, encoding="utf-8") as f:
    note = f.read()

def md_row(num, c, rel_label):
    return "| %d | %s | %s | %s |\n" % (num, c["title"], c["src"], c["summary"][:150])

# append ③ rows (26,27,28) + ② rows (15,16,17)
exec_new = "".join(md_row(26+i, c, "③") for i,c in enumerate(exec_cards))
sup_new  = "".join(md_row(15+i, c, "②") for i,c in enumerate(sup_cards))
# ③ table ends at line with "| 25 | 500+ 人大型 Offsite 作战框架" -> append after that row
anchor3 = "| 25 | 500+ 人大型 Offsite 作战框架（offsite.html） | 二手 | 500+人=临时城市（指数级复杂）；战略简报五问→类型定配置→90天框架→规模风险三防（容量/F&B/技术） |\n"
assert anchor3 in note, "note ③ anchor not found"
note = note.replace(anchor3, anchor3 + exec_new, 1)
# ② table ends at "| 14 | 高影响力团队 Offsite 四策略 ..."
anchor2 = "| 14 | 高影响力团队 Offsite 四策略 | 二手 | 业务影响聚焦(目标具体避空泛)/共建心理安全/用外部引导师/收尾承诺+1-3-6月 check-in 维持。🔍 区别于卡片20「领导力 Offsite 选型与心理安全」、卡片5「高管团队 Offsite 21条实操」——本卡聚焦「四策略」闭环且明确反对用 MBTI/大五性格测评填充，强调组织因素（资源/目标/角色清晰度）更影响业务 |\n"
assert anchor2 in note, "note ② anchor not found"
note = note.replace(anchor2, anchor2 + sup_new, 1)

# header count 39 -> 58 ; ③ 25 -> 28 ; ② 14 -> 17 ; "一手 0 + 二手 39" -> "一手 0 + 二手 58"
note = note.replace("# Offsite 团建务虚 · 知识卡汇总（39 卡 · 上下级/高管间）",
                    "# Offsite 团建务虚 · 知识卡汇总（58 卡 · 上下级/高管间）", 1)
note = note.replace("## ③ 领导↔领导（高管间 · exec）— 25 卡",
                    "## ③ 领导↔领导（高管间 · exec）— 28 卡", 1)
note = note.replace("## ② 领导↔员工（上下级 · supervisor）— 14 卡",
                    "## ② 领导↔员工（上下级 · supervisor）— 17 卡", 1)
note = note.replace("一手 0 + 二手 39（offsite 一手源稀缺，多为权威机构/引导师方法论）。",
                    "一手 0 + 二手 58（offsite 一手源稀缺，多为权威机构/引导师方法论）。", 1)
# marker in blockquote
note = note.replace("｜ 2026-08-10 语义去重 -1（合并 iceindia→easyhotelrfp）。卡片墙 HTML",
                    "｜ 2026-08-10 语义去重 -1（合并 iceindia→easyhotelrfp）｜ 2026-08-10 八轮补采 +6。卡片墙 HTML", 1)
atomic_write(NOTE, note)
print("Obsidian note updated: ③28 / ②17 / total 58")

# ---------- 5) 00-INDEX OFFSITE SECTION ----------
with open(ZERO, encoding="utf-8") as f:
    zero = f.read()
# update blockquote count "**52 卡**" and split + add 八轮
zero = zero.replace("**52 卡**（2026-08-07 首采 15 ｜ 2026-08-08 三轮 +10 ｜ 2026-08-09 五轮 +8 ｜ 2026-08-09夜 六轮 +5 ｜ 2026-08-10 KM补采 +3 ｜ 2026-08-10 七轮 +10，含语义去重 -1），已按「受众关系分层」剔除平级/朋友向（①），仅 ②上下级 / ③高管间；一手 3（KM 内部腾讯团建）+ 二手 49。按关系分层：③高管间 32 卡 / ②上下级 20 卡。",
                    "**58 卡**（2026-08-07 首采 15 ｜ 2026-08-08 三轮 +10 ｜ 2026-08-09 五轮 +8 ｜ 2026-08-09夜 六轮 +5 ｜ 2026-08-10 KM补采 +3 ｜ 2026-08-10 七轮 +10 ｜ 2026-08-10 八轮 +6，含语义去重 -1），已按「受众关系分层」剔除平级/朋友向（①），仅 ②上下级 / ③高管间；一手 3（KM 内部腾讯团建）+ 二手 55。按关系分层：③高管间 35 卡 / ②上下级 23 卡。", 1)
# append 6 rows to the Offsite table (after last ② row: 高影响力团队 Offsite 四策略)
zero_anchor = "| 高影响力团队 Offsite 四策略（offsite.html） | 4 | 二手 | ②上下级 | 四策略覆盖目标-安全-引导-跟进全闭环 |\n"
assert zero_anchor in zero, "00-index offsite table anchor not found"
new_rows = (
"| 董事会/治理型 retreat（治理干预·五段强议程）（offsite.html） | 4 | 二手 | ③高管间 | 把主题转治理交付物；强议程五段+聚焦决策；30/90天跟进前置 |\n"
"| 文化转型·价值观重置 offsite（Day1 消 silo + Day2 战略）（offsite.html） | 4 | 二手 | ③高管间 | 双日文化+战略结构；会前测评+会后30天复盘防褪色 |\n"
"| 新整合领导团队 offsite·建立 operating norms（并购/新组）（offsite.html） | 4 | 二手 | ③高管间 | operating norms 议程模板；外部引导师直面真实张力 |\n"
"| 远程/混合团队文化塑造 offsite（节奏框架）（offsite.html） | 4 | 二手 | ②上下级 | 文化工作嵌入结构；按团队阶段定节奏 |\n"
"| 团建/务虚 ROI 三层测量（HR 视角·防 vanity）（offsite.html） | 4 | 二手 | ②上下级 | 三层框架+防 vanity 指标 |\n"
"| 远程团队线下 reconnect·最高 ROI morale 投资（offsite.html） | 4 | 二手 | ②上下级 | 线下聚首 ROI 论证+half-life 跟进 |\n"
)
zero = zero.replace(zero_anchor, zero_anchor + new_rows, 1)
atomic_write(ZERO, zero)
print("00-index Offsite section updated: 52 -> 58 rows")

# ---------- 6) PORTAL INDEX.HTML ----------
theme_counts = {  # rendered HTML card counts (disk truth) + offsite +6
    "staff-meeting": 73, "offsite": 58, "icebreaker": 44,
    "award": 51, "openday": 15, "afternoontea": 54,
}
total = sum(theme_counts.values())
with open(PORTAL, encoding="utf-8") as f:
    portal = f.read()
portal = portal.replace('<div class="n">268</div>', '<div class="n">%d</div>' % total, 1)
portal = portal.replace("62 卡", "73 卡", 1)   # staff
portal = portal.replace("42 卡", "58 卡", 1)   # offsite
portal = portal.replace("51 卡", "44 卡", 1)   # icebreaker
portal = portal.replace("15 卡", "51 卡", 1)   # award
portal = portal.replace("54 卡", "15 卡", 1)   # openday
portal = portal.replace("44 卡", "54 卡", 1)   # afternoontea
portal = portal.replace("当前一手 37 张、二手 195 张",
                        "当前一手 %d 张、二手 %d 张" % (primary, secondary), 1)
atomic_write(PORTAL, portal)
print("portal updated: total %d; per-theme %s; 一手/二手 %d/%d" % (total, theme_counts, primary, secondary))
print("DONE")
