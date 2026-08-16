# -*- coding: utf-8 -*-
"""颁奖 十六轮 enrich (2026-08-17) — 更新 Obsidian 笔记 + 00-索引"""
import json, os

VAULT = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库"
NOTE = os.path.join(VAULT, "素材", "award", "颁奖-知识卡汇总.md")
IDX = os.path.join(VAULT, "00-知识采集索引.md")

meta = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "_award_r16_meta.json"), encoding="utf-8"))
cards = meta["cards"]
NEW_COUNT = 97

rel_map = {"r2": "②上下级", "r3": "③高管间"}
def row(c):
    return f"| {c['title']}（award/award.html） | 4 | 二手 | {rel_map[c['rel']]} |  |\n"

rows_block = "".join(row(c) for c in cards)

# ---- award note ----
t = open(NOTE, encoding="utf-8").read()
assert "共 93 张" in t, "summary count not found"
t = t.replace("共 93 张", f"共 {NEW_COUNT} 张", 1)

# 1) 插入轮次小节（在 ## 卡片总表 之前）
round_section = (
    "\n## 轮次 2026-08-17（+4）\n"
    "本轮新增（均通过六维评估、仅 ②上下级 / ③高管间）：\n"
    + "".join(f"- {c['title']}（{rel_map[c['rel']]}·二手）\n" for c in cards)
)
marker_total = "## 卡片总表"
assert marker_total in t, "卡片总表 marker not found"
t = t.replace(marker_total, round_section + "\n" + marker_total, 1)

# 2) 卡片总表追加 4 行（在 ## 卡片墙 之前）
marker_wall = "## 卡片墙（HTML 交互版）"
assert marker_wall in t, "卡片墙 marker not found"
t = t.replace(marker_wall, rows_block + "\n" + marker_wall, 1)

# 3) 适用&备注：更新计数 + 追加轮次说明 + 末尾追加 4 行
assert "**74 卡**" in t, "适用备注 count not found"
t = t.replace("**74 卡**", f"**{NEW_COUNT} 卡**", 1)
t = t.replace(
    "十二轮 enrich（2026-08-14 +5）：主管日常认可战术手册、管理者领 recognition、绿色盛典 ESG、数字荣誉墙×2（含大陆汽车电子一手案例）。",
    "十二轮 enrich（2026-08-14 +5）：主管日常认可战术手册、管理者领 recognition、绿色盛典 ESG、数字荣誉墙×2（含大陆汽车电子一手案例）；十六轮 enrich（2026-08-17 +4）：表彰防偏袒确定性机制、表彰8大反模式避坑、一线即时认可经理工具箱、元宇宙沉浸式颁奖。",
    1,
)
t = t.rstrip("\n") + "\n" + rows_block
open(NOTE, "w", encoding="utf-8").write(t)
print("award note 更新完成, 末行校验:", t.strip().splitlines()[-1][:40])

# ---- 00-index ----
i = open(IDX, encoding="utf-8").read()
# 1) 主题头部追加轮次
hdr_old = "｜ 十五轮 enrich 2026-08-16(+6)"
assert hdr_old in i, "00 header marker not found"
i = i.replace(hdr_old, hdr_old + " ｜ 十六轮 enrich 2026-08-17(+4)", 1)
# 2) 叙述计数 87 -> 97
assert "**87 卡**" in i, "00 narrative count not found"
i = i.replace("**87 卡**", f"**{NEW_COUNT} 卡**", 1)
i = i.replace(
    "十二轮 enrich（2026-08-14 +5）：主管日常认可战术手册、管理者领 recognition、绿色盛典 ESG、数字荣誉墙×2（含大陆汽车电子一手案例）。",
    "十二轮 enrich（2026-08-14 +5）：主管日常认可战术手册、管理者领 recognition、绿色盛典 ESG、数字荣誉墙×2（含大陆汽车电子一手案例）；十六轮 enrich（2026-08-17 +4）：表彰防偏袒确定性机制、表彰8大反模式避坑、一线即时认可经理工具箱、元宇宙沉浸式颁奖。",
    1,
)
# 3) 追加 4 行到颁奖表（在下一个 ## 主题： 之前）
next_theme = i.find("## 主题：", i.find("颁奖典礼（2026-08-06"))
assert next_theme != -1, "next theme not found"
insert_at = next_theme
i = i[:insert_at] + rows_block + "\n" + i[insert_at:]
open(IDX, "w", encoding="utf-8").write(i)
print("00-index 更新完成")
print("新增行样例:", rows_block.strip().splitlines()[0])
