import re, os

HTML = r"c:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection\offsite\offsite.html"
NOTE = r"C:\Users\v_yitcai\Documents\Obsidian\知识采集库\素材\offsite\Offsite-团建务虚-知识卡汇总.md"
INDEX = r"C:\Users\v_yitcai\Documents\Obsidian\知识采集库\00-知识采集索引.md"

html = open(HTML, encoding="utf-8").read()
sentinel3 = html.index('<div class="sec sec3">')
sentinel2 = html.index('<div class="sec sec2">')

cards = []  # (sec, title, source, relation_label, note)
for m in re.finditer(r'<div class="hl">', html):
    start = m.start()
    i = m.end(); depth = 1; j = i
    while j < len(html):
        if html[j:j+4] == '<div':
            depth += 1; j += 4
        elif html[j:j+5] == '</div':
            depth -= 1; j += 5
            if depth == 0: break
        else: j += 1
    card = html[start:j]
    sec = 'sec3' if (start > sentinel3 and start < sentinel2) else ('sec2' if start > sentinel2 else 'sec3')
    title = re.search(r'<h3>(.*?)</h3>', card, re.S).group(1)
    src = '一手' if 'badge b1' in card else '二手'
    rel = '③高管间' if 'badge r3' in card else '②上下级'
    note = re.search(r'<div class="note">(.*?)</div>', card, re.S)
    note = note.group(1).strip() if note else ''
    cards.append((sec, title, src, rel, note))

sec3 = [c for c in cards if c[0] == 'sec3']
sec2 = [c for c in cards if c[0] == 'sec2']
print('parsed sec3', len(sec3), 'sec2', len(sec2), 'total', len(cards))

# ---- summary note ----
def sum_rows(lst):
    out = []
    for n, (sec, title, src, rel, note) in enumerate(lst, 1):
        out.append(f"| {n} | {title} | {src} | {note} |")
    return "\n".join(out)

note_md = f"""---
title: Offsite 团建务虚 知识卡汇总
tags: [知识采集, Offsite, 活动/ai]
date: 2026-08-07
type: 自动化采集
quality: 综合 4-5 分
relation: ②上下级 / ③高管间
---

# Offsite 团建务虚 · 知识卡汇总（{len(cards)} 卡 · 上下级/高管间）

> 自动化采集于 2026-08-07 ｜ 多轮 enrich ｜ 2026-08-10 语义去重 -1 ｜ 2026-08-10 七轮补采 +10。卡片墙 HTML：`knowledge-collection/offsite/offsite.html`
> 线上预览：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/offsite/offsite.html
> 已按受众关系分层剔除平级/朋友向（①）；仅 ②上下级 / ③高管间。一手 3（KM 内部腾讯团建）+ 二手 {len(cards)-3}。

## ③ 领导↔领导（高管间 · exec）— {len(sec3)} 卡

| # | 卡 | 一手/二手 | 价值定位 |
|---|---|---|---|
{sum_rows(sec3)}

## ② 领导↔员工（上下级 · supervisor）— {len(sec2)} 卡

| # | 卡 | 一手/二手 | 价值定位 |
|---|---|---|---|
{sum_rows(sec2)}

## 适用&备注
- Offsite 在企业文化中承担「抽离日常、面向未来的深度对齐」职能：③ 用于高管团队战略务虚 / 闭门决策，强调结构、保密与问责；② 用于管理层与骨干以真实业务难题共创、建信任不越界。
- 共性方法论：③ 的黄金结构 = 会前访谈/范围锁定 → 发散收敛分节 → 决策落 owner+期限 → 会后 cascade+复盘节奏；② 则以「行动学习 / 群策群力 / 复盘」三大训战方法为骨架，把讨论变决策、决策变行动。
- 全部剔除平级/朋友向，凡 relation 含 peer 不进库（用户硬约束）。
"""
open(NOTE, "w", encoding="utf-8").write(note_md)
print("wrote summary note")

# ---- 00-index offsite section ----
def oneliner(note):
    # cut at 🔍 or first 。, strip leading '适用：X '
    s = re.split(r'🔍', note)[0]
    s = s.split('。')[0]
    s = re.sub(r'^适用：[③②][^，,]*[，,]?', '', s).strip()
    return s

def idx_rows(lst):
    out = []
    for (sec, title, src, rel, note) in lst:
        q = 5 if src == '一手' else 4
        relshort = '③高管间' if sec == 'sec3' else '②上下级'
        out.append(f"| {title}（offsite.html） | {q} | {src} | {relshort} | {oneliner(note)} |")
    return "\n".join(out)

section = f"""## 主题：Offsite 团建务虚（2026-08-07）

📄 主题汇总笔记：[[素材/offsite/Offsite-团建务虚-知识卡汇总|Offsite-团建务虚-知识卡汇总]]

> 卡片墙 HTML 承载（未逐卡建 md）：`knowledge-collection/offsite/offsite.html（[线上卡片墙·GitHub Pages](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/offsite/offsite.html)）`。**{len(cards)} 卡**（2026-08-07 首采 15 ｜ 2026-08-08 三轮 +10 ｜ 2026-08-09 五轮 +8 ｜ 2026-08-09夜 六轮 +5 ｜ 2026-08-10 KM补采 +3 ｜ 2026-08-10 七轮 +10，含语义去重 -1），已按「受众关系分层」剔除平级/朋友向（①），仅 ②上下级 / ③高管间；一手 3（KM 内部腾讯团建）+ 二手 {len(cards)-3}。按关系分层：③高管间 {len(sec3)} 卡 / ②上下级 {len(sec2)} 卡。

| 卡 | 质量分 | 一手/二手 | 适用关系 | 一句话定位 |
|---|---|---|---|---|
{idx_rows(sec3)}
{idx_rows(sec2)}
"""

idx = open(INDEX, encoding="utf-8").read()
start = idx.index('## 主题：Offsite')
# find next '## 主题：' after start
nxt = idx.index('## 主题：', start + 5)
new_idx = idx[:start] + section + "\n" + idx[nxt:]
open(INDEX, "w", encoding="utf-8").write(new_idx)
print("wrote 00-index offsite section; total len", len(new_idx))
