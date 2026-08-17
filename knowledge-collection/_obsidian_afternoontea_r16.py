# -*- coding: utf-8 -*-
"""下午茶研讨 十六轮 enrich (2026-08-17) — 更新 Obsidian 笔记 + 00-索引"""
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
VAULT = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库"
NOTE = os.path.join(VAULT, "素材", "afternoontea", "下午茶研讨-知识卡汇总.md")
IDX = os.path.join(VAULT, "00-知识采集索引.md")

meta = json.load(open(os.path.join(BASE, "_afternoontea_r16_meta.json"), encoding="utf-8"))
CARDS = meta["cards"]
NEW_TOTAL = meta["new_total"]      # 100
PREV_TOTAL = meta["prev_total"]    # 96
assert NEW_TOTAL == 100 and PREV_TOTAL == 96

rel_map = {"r2": "②上下级", "r3": "③高管间"}
src_map = {"b1": "一手", "b2": "二手"}
def val(c): return c["val"]
def row_md(c, num):
    return f"| {num} | {c['title']} | {src_map[c['src']]} | {val(c)} |\n"

# ③ 表追加 2 行（r3 卡），② 表追加 2 行（r2 卡）
r3 = [c for c in CARDS if c["rel"] == "r3"]
r2 = [c for c in CARDS if c["rel"] == "r2"]
assert len(r3) == 2 and len(r2) == 2
r3_rows = "".join(row_md(c, 35 + i) for i, c in enumerate(r3))
r2_rows = "".join(row_md(c, 63 + i) for i, c in enumerate(r2))

# ============ 笔记 ============
t = open(NOTE, encoding="utf-8").read()
# 1) H1 计数
assert "（96 卡 · 上下级/高管间）" in t, "H1 count not found"
t = t.replace("（96 卡 · 上下级/高管间）", "（100 卡 · 上下级/高管间）", 1)
# 2) 顶部 round 时间线（blockquote 第二行）
assert "十五轮 enrich 2026-08-16(+7)" in t, "timeline marker not found"
t = t.replace("十五轮 enrich 2026-08-16(+7)",
              "十五轮 enrich 2026-08-16(+7)｜ 十六轮 enrich 2026-08-17(+4)", 1)
# 3) 累计计数行
assert "累计 96 卡（③高管间 34 / ②上下级 62；一手 20 + 二手 76）" in t, "narrative count not found"
t = t.replace("累计 96 卡（③高管间 34 / ②上下级 62；一手 20 + 二手 76）",
              "累计 100 卡（③高管间 36 / ②上下级 64；一手 21 + 二手 79）", 1)
# 4) 插入轮次小节（在 ## ③ 之前）
round_section = (
    "\n## 轮次 2026-08-17（+4）\n"
    "> 十六轮 enrich：新增 4 卡（③ 高管间 +2：全球领导者咖啡文化·跨文化领导拉平层级 / 独立董事南京会客厅·治理层闭门茶叙圈层；② 上下级 +2：跨文化咖啡仪式·把咖啡做成「文化桥梁」溶解层级 / 并购变革期 tea time·跨部门破壁+员工随时找老总）。无 peer，relation 仅取 supervisor/exec。\n"
    "> 线上预览：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/afternoontea/afternoontea.html ｜ 本轮增量页：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/afternoontea/afternoontea-20260817.html\n"
)
marker3 = "## ③ 领导↔领导（高管间 · exec）— 34 卡"
assert marker3 in t, "③ header marker not found"
t = t.replace(marker3, round_section + marker3, 1)
# 5) ③ 表追加 2 行 + 更新 ③ 计数（在 ## ② 之前插入行，并把 ② 表头计数改 64）
marker2 = "## ② 领导↔员工（上下级 · supervisor）— 62 卡"
assert marker2 in t, "② header marker not found"
t = t.replace(marker2, r3_rows + "\n" + marker2.replace("62 卡", "64 卡"), 1)
# 6) ② 表追加 2 行（文件末尾）
t = t.rstrip("\n") + "\n" + r2_rows
open(NOTE, "w", encoding="utf-8").write(t)
print("笔记更新完成; 末行校验:", t.strip().splitlines()[-1][:50])

# ============ 00-索引 ============
i = open(IDX, encoding="utf-8").read()
# 1) 主题头部追加轮次
hdr_old = "十五轮 enrich 2026-08-16(+7)）"
assert hdr_old in i, "00 header marker not found"
i = i.replace(hdr_old, "十五轮 enrich 2026-08-16(+7) ｜ 十六轮 enrich 2026-08-17(+4)）", 1)
# 2) 叙述计数 + 分档
assert "**96 卡**" in i, "00 narrative count not found"
i = i.replace("**96 卡**", "**100 卡**", 1)
assert "一手 20 + 二手 76" in i, "00 一手二手 not found"
i = i.replace("一手 20 + 二手 76", "一手 21 + 二手 79", 1)
assert "③高管间(...) 34 卡 / ②上下级(...) 62 卡" in i, "00 分档 not found"
i = i.replace("③高管间(...) 34 卡 / ②上下级(...) 62 卡",
              "③高管间(...) 36 卡 / ②上下级(...) 64 卡", 1)
# 3) 追加十六轮 enrich 叙述（接在十四轮行尾）
assert "常州周末下午茶书记一对一谈心）。" in i, "十四轮 tail not found"
i = i.replace(
    "常州周末下午茶书记一对一谈心）。",
    "常州周末下午茶书记一对一谈心）。十六轮 enrich 新增（③全球领导者咖啡文化·跨文化领导拉平层级 / ③独立董事南京会客厅·治理层闭门茶叙圈层 + ②跨文化咖啡仪式·把咖啡做成「文化桥梁」溶解层级 / ②并购变革期 tea time·跨部门破壁+员工随时找老总）。",
    1,
)
# 4) 追加 4 行到下午茶表（在下一个 ## 主题： 之前）
next_theme = i.find("## 主题：", i.find("## 主题：下午茶研讨"))
assert next_theme != -1, "next theme not found"
rows = "".join(
    f"| {c['title']}（afternoontea.html） | 4 | {src_map[c['src']]} | {rel_map[c['rel']]} |  |\n"
    for c in CARDS
)
i = i[:next_theme] + rows + "\n" + i[next_theme:]
open(IDX, "w", encoding="utf-8").write(i)
print("00-索引更新完成; 新增行样例:", rows.strip().splitlines()[0])
print("本轮卡片:", [c['title'] for c in CARDS])
