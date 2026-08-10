# -*- coding: utf-8 -*-
# Finish script for Offsite 八轮 enrich (2026-08-10).
# index.json (+6, 294 total, 58 offsite) and offsite.html (+6, 58 cards) are
# ALREADY correctly updated by the failed prior run. This script ONLY finishes
# the 3 remaining steps (Obsidian note, 00-index, portal) with correct CURRENT
# numbers + idempotency guards. Does NOT touch index.json / offsite.html.
import os, tempfile

NOTE = r"C:\Users\v_yitcai\Documents\Obsidian\知识采集库\素材\offsite\Offsite-团建务虚-知识卡汇总.md"
ZERO = r"C:\Users\v_yitcai\Documents\Obsidian\知识采集库\00-知识采集索引.md"
PORTAL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")

def atomic_write(path, text):
    d = os.path.dirname(path)
    fd, tmp = tempfile.mkstemp(dir=d, suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(text)
    os.replace(tmp, path)

def safe_replace(s, old, new, label):
    assert old in s, "GUARD FAIL: %s not found" % label
    return s.replace(old, new, 1)

# ============ 1) OBSIDIAN NOTE ============
with open(NOTE, encoding="utf-8") as f:
    note = f.read()

if "③ 领导↔领导（高管间 · exec）— 35 卡" in note:
    print("[note] already at ③35 — skip")
else:
    # header + counts (52 -> 58, ③32 -> 35, ②20 -> 23)
    note = safe_replace(note,
        "# Offsite 团建务虚 · 知识卡汇总（52 卡 · 上下级/高管间）",
        "# Offsite 团建务虚 · 知识卡汇总（58 卡 · 上下级/高管间）", "note header")
    note = safe_replace(note,
        "## ③ 领导↔领导（高管间 · exec）— 32 卡",
        "## ③ 领导↔领导（高管间 · exec）— 35 卡", "note ③ count")
    note = safe_replace(note,
        "## ② 领导↔员工（上下级 · supervisor）— 20 卡",
        "## ② 领导↔员工（上下级 · supervisor）— 23 卡", "note ② count")
    note = safe_replace(note,
        "一手 3（KM 内部腾讯团建）+ 二手 49。",
        "一手 3（KM 内部腾讯团建）+ 二手 55。", "note 一手/二手")
    # blockquote: add 八轮 +6
    note = safe_replace(note,
        "2026-08-10 七轮补采 +10。卡片墙 HTML：",
        "2026-08-10 七轮补采 +10｜ 2026-08-10 八轮补采 +6。卡片墙 HTML：", "note blockquote")

    # append ③ rows 33/34/35 after row 32 (last ③ row)
    note_anchor3 = "| 32 | 高管 Retreat ROI 测量框架（SAS/RQI/OFS） | 二手 | 适用：③ 高管 retreat 立项/验收与 ROI 论证，三支柱框架数据化说服力强。 |\n"
    note_exec_new = (
        "| 33 | 董事会/治理型 retreat（治理干预·五段强议程） | 二手 | 适用：③ 董事会/治理层 retreat，把务虚转成治理交付物是可迁移亮点，区别于纯战略务虚。 |\n"
        "| 34 | 文化转型·价值观重置 offsite（Day1 消 silo + Day2 战略） | 二手 | 适用：③ 领导团队文化转型/价值观重置 offsite，双日文化+战略结构是可迁移亮点。 |\n"
        "| 35 | 新整合领导团队 offsite·建立 operating norms（并购/新组） | 二手 | 适用：③ 并购后/新组建高管团队整合 offsite，operating norms 议程模板是可迁移亮点。 |\n"
    )
    note = safe_replace(note, note_anchor3, note_anchor3 + note_exec_new, "note ③ append anchor")

    # append ② rows 21/22/23 after row 20 (last ② row)
    note_anchor2 = "| 20 | 高影响力团队 Offsite 四策略 | 二手 | 适用：② 管理者带团队务虚/团建，四策略覆盖目标-安全-引导-跟进全闭环。🔍 差异化：区别于卡片20「领导力 Offsite 选型与心理安全」、卡片5「高管团队 Offsite 21条实操」——本卡聚焦「四策略」闭环且明确反对用 MBTI/大五性格测评填充，强调组织因素（资源/目标/角色清晰度）更影响业务。 |\n"
    note_sup_new = (
        "| 21 | 远程/混合团队文化塑造 offsite（节奏框架） | 二手 | 适用：② 管理者带远程/混合团队做文化塑造 offsite，节奏框架+仪式化是可迁移亮点。 |\n"
        "| 22 | 团建/务虚 ROI 三层测量（HR 视角·防 vanity） | 二手 | 适用：② 管理层/HR 论证团队务虚 ROI，三层框架+防 vanity 是可迁移亮点。 |\n"
        "| 23 | 远程团队线下 reconnect·最高 ROI morale 投资 | 二手 | 适用：② 管理者带远程团队做线下 reconnect，morale 投资 ROI 论证 + half-life 跟进是可迁移亮点。 |\n"
    )
    note = safe_replace(note, note_anchor2, note_anchor2 + note_sup_new, "note ② append anchor")
    atomic_write(NOTE, note)
    print("[note] updated: ③35 / ②23 / total 58 (+6 rows)")

# ============ 2) 00-INDEX OFFSITE SECTION ============
with open(ZERO, encoding="utf-8") as f:
    zero = f.read()

if "③高管间 35 卡 / ②上下级 23 卡。" in zero:
    print("[00-index] already at ③35/②23 — skip")
else:
    # blockquote count 52 -> 58
    zero = safe_replace(zero, "**52 卡**（", "**58 卡**（", "00 blockquote count")
    zero = safe_replace(zero,
        "2026-08-10 七轮 +10，含语义去重 -1）",
        "2026-08-10 七轮 +10 ｜ 2026-08-10 八轮 +6，含语义去重 -1）", "00 blockquote rounds")
    zero = safe_replace(zero,
        "一手 3（KM 内部腾讯团建）+ 二手 49。",
        "一手 3（KM 内部腾讯团建）+ 二手 55。", "00 一手/二手")
    zero = safe_replace(zero,
        "③高管间 32 卡 / ②上下级 20 卡。",
        "③高管间 35 卡 / ②上下级 23 卡。", "00 ③/② split")

    # append 6 rows after last ② row (高影响力团队 Offsite 四策略)
    zero_anchor = "| 高影响力团队 Offsite 四策略（offsite.html） | 4 | 二手 | ②上下级 | 四策略覆盖目标-安全-引导-跟进全闭环 |\n"
    zero_new_rows = (
        "| 董事会/治理型 retreat（治理干预·五段强议程）（offsite.html） | 4 | 二手 | ③高管间 | 把主题转治理交付物；强议程五段+聚焦决策；30/90天跟进前置 |\n"
        "| 文化转型·价值观重置 offsite（Day1 消 silo + Day2 战略）（offsite.html） | 4 | 二手 | ③高管间 | 双日文化+战略结构；会前测评+会后30天复盘防褪色 |\n"
        "| 新整合领导团队 offsite·建立 operating norms（并购/新组）（offsite.html） | 4 | 二手 | ③高管间 | operating norms 议程模板；外部引导师直面真实张力 |\n"
        "| 远程/混合团队文化塑造 offsite（节奏框架）（offsite.html） | 4 | 二手 | ②上下级 | 文化工作嵌入结构；按团队阶段定节奏 |\n"
        "| 团建/务虚 ROI 三层测量（HR 视角·防 vanity）（offsite.html） | 4 | 二手 | ②上下级 | 三层框架+防 vanity 指标 |\n"
        "| 远程团队线下 reconnect·最高 ROI morale 投资（offsite.html） | 4 | 二手 | ②上下级 | 线下聚首 ROI 论证+half-life 跟进 |\n"
    )
    zero = safe_replace(zero, zero_anchor, zero_anchor + zero_new_rows, "00 append anchor")
    atomic_write(ZERO, zero)
    print("[00-index] Offsite section updated: 52 -> 58 (+6 rows)")

# ============ 3) PORTAL INDEX.HTML ============
with open(PORTAL, encoding="utf-8") as f:
    portal = f.read()

if '<div class="n">294</div><div class="l">294 张知识卡</div>' in portal:
    print("[portal] already at total 294 — skip")
else:
    # total stat (268 -> 294); matches index.json authoritative total
    portal = safe_replace(portal,
        '<div class="n">268</div><div class="l">268 张知识卡</div>',
        '<div class="n">294</div><div class="l">294 张知识卡</div>', "portal total")
    # per-theme cnt → disk HTML truth
    portal = safe_replace(portal, '<div class="cnt">62 卡</div>', '<div class="cnt">73 卡</div>', "portal staff")   # 员工大会 73
    portal = safe_replace(portal, '<div class="cnt">42 卡</div>', '<div class="cnt">58 卡</div>', "portal offsite")  # Offsite 58
    portal = safe_replace(portal, '<div class="cnt">51 卡</div>', '<div class="cnt">44 卡</div>', "portal icebreaker") # 破冰 44
    portal = safe_replace(portal, '<div class="cnt">15 卡</div>', '<div class="cnt">51 卡</div>', "portal award")    # 颁奖 51
    portal = safe_replace(portal, '<div class="cnt">54 卡</div>', '<div class="cnt">15 卡</div>', "portal openday")  # OpenDay 15
    portal = safe_replace(portal, '<div class="cnt">44 卡</div>', '<div class="cnt">54 卡</div>', "portal afternoontea") # 下午茶 54
    # 一手/二手 normalized (primary+一手=66, secondary+二手=228)
    portal = safe_replace(portal,
        "当前一手 37 张、二手 195 张",
        "当前一手 66 张、二手 228 张", "portal 一手/二手")
    atomic_write(PORTAL, portal)
    print("[portal] updated: total 294; per-theme 73/58/44/51/15/54; 一手/二手 66/228")

print("FINISH DONE")
