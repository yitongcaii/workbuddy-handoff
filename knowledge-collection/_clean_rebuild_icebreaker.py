#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Clean icebreaker wall: dedup cards by URL, fix stale sec-tag counts,
and reconcile index.json icebreaker entries from the wall (dedup source)."""
import json, re, os

BASE = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(BASE, "icebreaker", "icebreaker.html")
IDX = os.path.join(BASE, "index.json")
WALL_BAK = os.path.join(BASE, "icebreaker", "icebreaker.html.bak")

text = open(WALL, encoding="utf-8").read()

# ---- locate structural markers ----
sec3_h = text.find('<div class="sec sec3">')
sec2_h = text.find('<div class="sec sec2">')
footer_i = text.find("<footer>")
assert sec3_h != -1 and sec2_h != -1 and footer_i != -1, "markers missing"

def grid_open_after(idx):
    return text.find('<div class="grid">', idx)

g1 = grid_open_after(sec3_h)
g2 = grid_open_after(sec2_h)

def balanced_close(t, start):
    """Return index AFTER the </div> that closes the div opened at t[start:]'s first <div>."""
    depth = 0
    for m in re.finditer(r'<(/?)div\b', t[start:]):
        if m.group(1) == '/':
            depth -= 1
        else:
            depth += 1
        if depth == 0:
            return start + m.end()
    return -1

g1_close = balanced_close(text, g1)
g2_close = balanced_close(text, g2)
assert g1_close != -1 and g2_close != -1, "grid close not found"

hero = text[:sec3_h]
sec3_head = text[sec3_h:g1]            # sec3 header (tag count stale, fix later)
sec3_cards_raw = text[g1 + len('<div class="grid">'):g1_close]
sec2_head = text[sec2_h:g2]
sec2_cards_raw = text[g2 + len('<div class="grid">'):g2_close]
tail = text[g2_close:]                  # includes grid2 close + footer

def extract_cards(block):
    cards = []
    i = 0
    while True:
        s = block.find('<div class="hl">', i)
        if s == -1:
            break
        end = balanced_close(block, s)
        if end == -1:
            break
        cards.append(block[s:end])
        i = end
    return cards

def card_url(card):
    m = re.search(r'class="src"[^>]*>.*?<a href="([^"]+)"', card, re.S)
    if not m:
        m = re.search(r'<a href="([^"]+)"', card)
    return m.group(1).strip() if m else ""

def card_field(card, tag, cls):
    m = re.search(r'<'+tag+r' class="'+cls+r'">(.*?)</'+tag+r'>', card, re.S)
    return m.group(1).strip() if m else ""

def card_badge(card, cls):
    return bool(re.search(r'class="badge '+cls+r'"', card))

def dedup_cards(cards):
    seen = {}
    out = []
    dups = 0
    for c in cards:
        u = card_url(c)
        if u in seen:
            dups += 1
            continue
        seen[u] = True
        out.append(c)
    return out, dups

sec3_cards = extract_cards(sec3_cards_raw)
sec2_cards = extract_cards(sec2_cards_raw)
sec3_clean, d3 = dedup_cards(sec3_cards)
sec2_clean, d2 = dedup_cards(sec2_cards)

before = len(sec3_cards) + len(sec2_cards)
after = len(sec3_clean) + len(sec2_clean)
print(f"before cards={before} (sec3={len(sec3_cards)}, sec2={len(sec2_cards)})")
print(f"after  cards={after} (sec3={len(sec3_clean)}, sec2={len(sec2_clean)})")
print(f"dups removed: sec3={d3}, sec2={d2}, total={d3+d2}")

# ---- fix sec tag counts ----
def set_tag_count(head, n):
    return re.sub(r'<span class="tag">\d+ 卡</span>', f'<span class="tag">{n} 卡</span>', head, count=1)

sec3_head = set_tag_count(sec3_head, len(sec3_clean))
sec2_head = set_tag_count(sec2_head, len(sec2_clean))

new_wall = (hero + sec3_head + '<div class="grid">\n' + "\n".join(sec3_clean)
            + "\n</div>\n" + sec2_head + '<div class="grid">\n' + "\n".join(sec2_clean)
            + "\n</div>\n" + tail)
open(WALL, "w", encoding="utf-8").write(new_wall)
print(f"wall rewritten: {len(new_wall)} bytes, cards={after}")

# ---- build index entries from clean cards ----
def norm(t):
    return t.replace(" ", "").replace("·", "").strip()

entries = []
for section, cards in (("exec", sec3_clean), ("supervisor", sec2_clean)):
    for c in cards:
        url = card_url(c)
        if not url:
            continue
        title = card_field(c, "h3", "")
        val = card_field(c, "p", "val")
        relation = "exec" if card_badge(c, "r3") else ("supervisor" if card_badge(c, "r2") else "peer")
        if card_badge(c, "r1"):
            relation = "peer"
        src = "primary" if card_badge(c, "b1") else "secondary"
        entries.append({
            "title": title,
            "normKey": norm(title),
            "url": url,
            "sourceType": src,
            "relation": relation,
            "topic": "icebreaker",
            "summary": val,
        })
print(f"index icebreaker entries rebuilt: {len(entries)}")

idx = json.load(open(IDX, encoding="utf-8"))
others = [x for x in idx if x.get("topic") != "icebreaker"]
print(f"index total before={len(idx)} (others={len(others)})")
idx_new = others + entries
json.dump(idx_new, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"index total after={len(idx_new)}")

# ---- save unique urls for round dedup ----
urls = [e["url"] for e in entries]
json.dump({"urls": urls, "count": len(entries)}, open(os.path.join(BASE, "icebreaker", "_clean_urls.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("saved _clean_urls.json")
