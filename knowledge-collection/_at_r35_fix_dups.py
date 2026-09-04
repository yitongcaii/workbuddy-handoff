# -*- coding: utf-8 -*-
# R35 修正：剔除 3 张与前轮同标题/同内容重复卡（短URL版），保留 7 张真新卡
import json, os, re

BASE = os.path.dirname(os.path.abspath(__file__))
TOPIC = "offsite"; SLUG = "offsite"; DATE = "20260905"
VAULT = "C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库"
VAULT_NOTE = "Offsite-团建务虚-知识卡汇总"

# 3 张重复卡的短 URL（本轮新增，前轮已有完整 URL 同标题卡）
DUP_URLS = [
    "https://www.sprintlaw.com/articles/retreat-terms",
    "https://www.ascentlawfirm.com/force-majeure",
    "https://pamelajgreen.com/scaling-communication",
]
# 对应标题片段（用于删笔记/00index 行）
DUP_FRAGS = ["供应商合同审查清单", "Force Majeure 不可抗力条款谈判要点", "C-suite 沟通级联"]

def remove_card(h, url):
    ui = h.find(url)
    assert ui != -1, "url not found: " + url
    cs = h.rfind('<div class="hl">', 0, ui)
    ce = h.find('\n    </div>\n', ui)
    assert ce != -1, "card close not found: " + url
    return h[:cs] + h[ce + len('\n    </div>\n'):]

# ---------- 1. wall ----------
html_path = os.path.join(BASE, TOPIC, TOPIC + ".html")
html = open(html_path, encoding="utf-8").read()
for u in DUP_URLS:
    html = remove_card(html, u)
sec2_header = html.find('<div class="sec sec2">')
footer = html.rfind('<footer>')
s3 = html.count('class="hl"', 0, sec2_header)
s2 = html.count('class="hl"', sec2_header, footer)
print("wall after dedup: sec3=%d sec2=%d total=%d" % (s3, s2, s3 + s2))
html = html.replace('<span class="tag">148 卡</span>', '<span class="tag">%d 卡</span>' % s3, 1)
html = html.replace('<span class="tag">104 卡</span>', '<span class="tag">%d 卡</span>' % s2, 1)
old_r35 = (" ｜ 2026-09-05 三十五轮补采 +10（裸心会深度研讨/务虚会成果闭环销号/务虚会务实三原则/"
           "务虚会精神一线穿透/C-suite结论级联 + 供应商合同审查/force majeure谈判/国际签证合规/"
           "保险按活动类型矩阵/组织者责任险双轨）")
new_r35 = (" ｜ 2026-09-05 三十五轮补采 +7（裸心会深度研讨/务虚会成果闭环销号/务虚会务实三原则/"
           "务虚会精神一线穿透 + 国际签证合规/保险按活动类型矩阵/组织者责任险双轨）")
assert old_r35 in html, "wall prose chunk not found"
html = html.replace(old_r35, new_r35, 1)
open(html_path, "w", encoding="utf-8").write(html)
print("wall fixed")

# ---------- 2. index.json ----------
idx_path = os.path.join(BASE, "index.json")
idx = json.load(open(idx_path, encoding="utf-8"))
before = len(idx)
idx = [e for e in idx if e["url"] not in DUP_URLS]
print("index removed:", before - len(idx), "-> total", len(idx))
json.dump(idx, open(idx_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ---------- 3. increment page ----------
inc_path = os.path.join(BASE, TOPIC, "%s-%s.html" % (TOPIC, DATE))
inc = open(inc_path, encoding="utf-8").read()
for u in DUP_URLS:
    inc = remove_card(inc, u)
inc = inc.replace("本轮 +10（5 高管间 + 5 上下级）", "本轮 +7（4 高管间 + 3 上下级）", 1)
inc = inc.replace('<span class="tag">5 卡</span>', '<span class="tag">4 卡</span>', 1)
inc = inc.replace('<span class="tag">5 卡</span>', '<span class="tag">3 卡</span>', 1)
open(inc_path, "w", encoding="utf-8").write(inc)
print("increment fixed")

# ---------- 4. obsidian note ----------
note_path = os.path.join(VAULT, "素材", SLUG, VAULT_NOTE + ".md")
note = open(note_path, encoding="utf-8").read()
note = note.replace("知识卡汇总（252 卡", "知识卡汇总（249 卡", 1)
note = note.replace(old_r35, new_r35, 1)
note = note.replace("## 轮次 20260905·三十五轮（+10）", "## 轮次 20260905·三十五轮（+7）", 1)
for f in DUP_FRAGS:
    note = re.sub(r'\n\| [^|]*' + re.escape(f) + r'[^|]*\|[^|]*\|[^|]*\|\n', '\n', note)
open(note_path, "w", encoding="utf-8").write(note)
print("note fixed")

# ---------- 5. 00-index ----------
idx00_path = os.path.join(VAULT, "00-知识采集索引.md")
t = open(idx00_path, encoding="utf-8").read()
for f in DUP_FRAGS:
    t = re.sub(r'\n\| [^|]*' + re.escape(f) + r'[^|]*\|[^|]*\|\n', '\n', t)
open(idx00_path, "w", encoding="utf-8").write(t)
print("00-index fixed")

# ---------- 6. map R35 ----------
map_path = os.path.join(BASE, "lexiang-entry-map.json")
mp = json.load(open(map_path, encoding="utf-8"))
r = mp[SLUG]["rounds"][-1]
r["note"] = r["note"].replace("(+10：5③高管间+5②上下级)", "(+7：4③高管间+3②上下级)")
mp[SLUG]["rounds"][-1] = r
json.dump(mp, open(map_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("map fixed")
print("DONE")
