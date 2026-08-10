#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prune specific KM cards (user-decision): keep 1&2, drop 3&4.
Targets (by km article id in url):
  639680 -> openday  重阳敬老开放日 (3)
  624840 -> afternoontea 明湾育见-家长 (4)
  622349 -> afternoontea 明湾育见-家长 (4)
"""
import os, re, json

BASE = os.path.dirname(os.path.abspath(__file__))
REMOVE_URLS = {
    "https://km.woa.com/articles/show/639680",
    "https://km.woa.com/articles/show/624840",
    "https://km.woa.com/articles/show/622349",
}

# ---------- 1) index.json (array) ----------
idx_path = os.path.join(BASE, "index.json")
cards = json.load(open(idx_path, encoding="utf-8"))
before = len(cards)
cards = [c for c in cards if (c.get("url") or "") not in REMOVE_URLS]
after = len(cards)
json.dump(cards, open(idx_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"index.json: {before} -> {after} (删 {before-after})")

# ---------- 2) walls: remove .hl block containing target url ----------
def remove_hl_block(text, url):
    lines = text.split("\n")
    # locate href line
    start = None
    for i, l in enumerate(lines):
        if url in l and "href" in l:
            for j in range(i, -1, -1):
                if lines[j].strip() == '<div class="hl">':
                    start = j
                    break
            break
    if start is None:
        return text, False
    depth = 0
    end = None
    for k in range(start, len(lines)):
        depth += lines[k].count("<div")
        depth -= lines[k].count("</div>")
        if depth <= 0 and k > start:
            end = k
            break
    if end is None:
        return text, False
    del lines[start:end + 1]
    return "\n".join(lines), True

WALLS = {
    "openday": os.path.join(BASE, "openday", "openday.html"),
    "afternoontea": os.path.join(BASE, "afternoontea", "afternoontea.html"),
}
for theme, path in WALLS.items():
    t = open(path, encoding="utf-8").read()
    n0 = t.count('<div class="hl">')
    for u in REMOVE_URLS:
        t, ok = remove_hl_block(t, u)
        if ok:
            print(f"  wall {theme}: 删除块 {u}")
    n1 = t.count('<div class="hl">')
    # refresh per-wall count spans (sec2/footer tag)
    t = re.sub(r'(<span class="tag">)\d+( 卡</span>)',
               lambda m: m.group(1) + str(n1) + m.group(2), t, count=2)
    open(path, "w", encoding="utf-8").write(t)
    print(f"  wall {theme}: {n0} -> {n1} 卡")

# ---------- 3) portal counts: recount all walls ----------
THEME_WALLS = {
    "staff-meeting": os.path.join(BASE, "staff-meeting", "staff-meeting.html"),
    "offsite": os.path.join(BASE, "offsite", "offsite.html"),
    "award": os.path.join(BASE, "award", "award.html"),
    "openday": os.path.join(BASE, "openday", "openday.html"),
    "afternoontea": os.path.join(BASE, "afternoontea", "afternoontea.html"),
    "icebreaker": os.path.join(BASE, "icebreaker", "icebreaker.html"),
}
counts = {}
for th, p in THEME_WALLS.items():
    counts[th] = open(p, encoding="utf-8").read().count('<div class="hl">')
total = sum(counts.values())
print("各墙计数:", counts, "总计:", total)

portal = os.path.join(BASE, "index.html")
pt = open(portal, encoding="utf-8").read()
# total stat
pt = re.sub(r'(<div class="n">)\d+(</div><div class="l">)\d+( 张知识卡</div>)',
            lambda m: m.group(1) + str(total) + m.group(2) + str(total) + m.group(3), pt, count=1)
# per-theme cnt span mapping by order of theme cards in portal
order = ["staff-meeting", "offsite", "award", "openday", "afternoontea", "icebreaker"]
# replace each <div class="cnt">N 卡</div> sequentially
def repl_cnt(m):
    repl_cnt.i += 1
    th = order[repl_cnt.i - 1]
    return f'<div class="cnt">{counts[th]} 卡</div>'
repl_cnt.i = 0
pt = re.sub(r'<div class="cnt">\d+ 卡</div>', repl_cnt, pt)
open(portal, "w", encoding="utf-8").write(pt)
print("门户计数已刷新: 总计", total)
