# -*- coding: utf-8 -*-
import re
KC = "c:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection"
ICE = KC + "/icebreaker"
INC = ICE + "/icebreaker-20260901.html"
SUM = ICE + "/icebreaker.html"
VAULT_NOTE = "C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库/素材/icebreaker/破冰-知识卡汇总.md"
DUP = "galvinrowley"

def remove_card_containing(path, substr):
    h = open(path, encoding="utf-8").read()
    i = h.find(substr)
    # find enclosing <div class="hl"> ... </div>
    s = h.rfind('<div class="hl">', 0, i)
    assert s != -1
    depth = 0; j = s
    while j < len(h):
        if h.startswith('<div', j):
            depth += 1; j = h.find('>', j)+1; continue
        elif h.startswith('</div>', j):
            depth -= 1; j += 6
            if depth == 0: break
            continue
        else: j += 1
    new = h[:s] + h[j:]
    # trim possible blank line left
    open(path, "w", encoding="utf-8").write(new)
    return new

# 1) increment page: remove dup card, fix counts +10->+9, sec3 4->3
remove_card_containing(INC, DUP)
inc = open(INC, encoding="utf-8").read()
inc = inc.replace("本轮 +10（仅②上下级", "本轮 +9（仅②上下级")
inc = inc.replace('<span class="tag">4 卡</span>', '<span class="tag">3 卡</span>', 1)
open(INC, "w", encoding="utf-8").write(inc)
print("increment page: removed dup, +10->+9, sec3 4->3")

# 2) summary page: remove dup card, sec3 93->92
remove_card_containing(SUM, DUP)
s = open(SUM, encoding="utf-8").read()
s = s.replace('<span class="tag">93 卡</span>', '<span class="tag">92 卡</span>', 1)
open(SUM, "w", encoding="utf-8").write(s)
print("summary page: removed dup, sec3 93->92")

# 3) obsidian table: remove row 225, 231->230
lines = open(VAULT_NOTE, encoding="utf-8").read().split("\n")
lines = [l for l in lines if not l.startswith("| 225 |")]
n = "\n".join(lines)
n = n.replace("## 卡片总表（231 卡 · 仅②/③）", "## 卡片总表（230 卡 · 仅②/③）", 1)
open(VAULT_NOTE, "w", encoding="utf-8").write(n)
print("obsidian: removed row 225, 231->230")
print("DONE")
