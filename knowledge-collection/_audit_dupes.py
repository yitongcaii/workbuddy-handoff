# -*- coding: utf-8 -*-
import re, json, os
from difflib import SequenceMatcher
from collections import defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
THEMES = {
    'staff-meeting': '员工大会',
    'offsite': '管理层Offsite',
    'icebreaker': '破冰',
    'award': '颁奖',
    'openday': 'OpenDay',
    'afternoontea': '下午茶研讨',
}

def norm(s):
    s = (s or '').lower()
    # keep CJK + alphanumerics, drop punctuation/spaces/symbols
    s = re.sub(r'[^\w\u4e00-\u9fff]', '', s)
    return s

def cjk_bigrams(s):
    # s already normalized; produce character bigrams
    return set(s[i:i+2] for i in range(len(s)-1))

def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)

def parse_cards(html, theme):
    cards = []
    # split by card marker
    parts = re.split(r'(?=<div class="hl">)', html)
    for blk in parts:
        if not blk.strip().startswith('<div class="hl">'):
            continue
        m = re.search(r'<h3>(.*?)</h3>', blk, re.S)
        title = re.sub(r'<.*?>', '', m.group(1)).strip() if m else ''
        mu = re.search(r'href="([^"]+)"', blk)
        url = mu.group(1).strip() if mu else ''
        mv = re.search(r'<p class="val">(.*?)</p>', blk, re.S)
        val = re.sub(r'<.*?>', '', mv.group(1)).strip() if mv else ''
        # relation badges
        rel = []
        if 'badge r3' in blk:
            rel.append('③')
        if 'badge r2' in blk:
            rel.append('②')
        cards.append({
            'theme': theme,
            'title': title,
            'norm_title': norm(title),
            'url': url,
            'val': val,
            'val_norm': norm(val),
            'val_bigrams': cjk_bigrams(norm(val)),
            'rel': '/'.join(rel),
        })
    return cards

# ---- 1. parse all ----
all_cards = []
for slug, name in THEMES.items():
    p = os.path.join(BASE, slug, slug + '.html')
    html = open(p, encoding='utf-8').read()
    cs = parse_cards(html, slug)
    all_cards.extend(cs)
    print(f'{name}({slug}): parsed {len(cs)} cards')

print(f'\nTOTAL CARDS PARSED: {len(all_cards)}')

# ---- 2. URL exact dup ----
url_map = defaultdict(list)
for c in all_cards:
    url_map[c['url']].append(c)
print('\n===== URL EXACT DUPLICATES (same url, >1 card) =====')
url_dup = 0
for u, lst in url_map.items():
    if len(lst) > 1:
        url_dup += 1
        themes = set(x['theme'] for x in lst)
        print(f'  URL dup x{len(lst)} themes={themes}: {u}')
        for x in lst:
            print(f'      [{THEMES[x["theme"]]}] {x["title"]}')
if url_dup == 0:
    print('  (none)')

# ---- 3. title normalization exact equal + high similarity ----
print('\n===== TITLE SIMILARITY (norm ratio >= 0.80) =====')
title_pairs = 0
# within + across
n = len(all_cards)
flagged = []
for i in range(n):
    for j in range(i+1, n):
        a, b = all_cards[i], all_cards[j]
        if not a['norm_title'] or not b['norm_title']:
            continue
        if a['norm_title'] == b['norm_title']:
            ratio = 1.0
        else:
            ratio = SequenceMatcher(None, a['norm_title'], b['norm_title']).ratio()
        if ratio >= 0.80:
            title_pairs += 1
            flagged.append((ratio, a, b))
flagged.sort(reverse=True)
for ratio, a, b in flagged:
    same = 'SAME-NORM' if ratio >= 0.999 else f'{ratio:.2f}'
    print(f'  [{same}] {THEMES[a["theme"]]}<->{THEMES[b["theme"]]}')
    print(f'      A: {a["title"]}')
    print(f'      B: {b["title"]}')
    if a['url'] == b['url']:
        print(f'      (URLS IDENTICAL: {a["url"]})')
    else:
        print(f'      UA: {a["url"]}')
        print(f'      UB: {b["url"]}')
if title_pairs == 0:
    print('  (none >= 0.80)')

# ---- 4. value text overlap (bigram Jaccard) ----
print('\n===== VALUE TEXT OVERLAP (bigram Jaccard >= 0.40) =====')
val_pairs = 0
vflag = []
for i in range(n):
    for j in range(i+1, n):
        a, b = all_cards[i], all_cards[j]
        if len(a['val_norm']) < 20 or len(b['val_norm']) < 20:
            continue
        jc = jaccard(a['val_bigrams'], b['val_bigrams'])
        if jc >= 0.40:
            val_pairs += 1
            vflag.append((jc, a, b))
vflag.sort(reverse=True)
for jc, a, b in vflag:
    print(f'  [J={jc:.2f}] {THEMES[a["theme"]]}<->{THEMES[b["theme"]]}')
    print(f'      A: {a["title"]}')
    print(f'      B: {b["title"]}')
if val_pairs == 0:
    print('  (none >= 0.40)')

# ---- 5. index.json consistency ----
print('\n===== INDEX.JSON CONSISTENCY =====')
idx = json.load(open(os.path.join(BASE, 'index.json'), encoding='utf-8'))
idx_urls = set(x['url'] for x in idx)
html_urls = set(c['url'] for c in all_cards)
print(f'  index entries: {len(idx)} | html cards: {len(all_cards)}')
print(f'  index urls not in any html: {len(idx_urls - html_urls)}')
for u in sorted(idx_urls - html_urls):
    t = [x.get('title') for x in idx if x['url'] == u]
    print(f'      MISSING-IN-HTML: {u}  | {t[:1]}')
print(f'  html urls not in index: {len(html_urls - idx_urls)}')
for u in sorted(html_urls - idx_urls):
    c = [x for x in all_cards if x['url'] == u]
    if c:
        print(f'      MISSING-IN-INDEX: [{THEMES[c[0]["theme"]]}] {c[0]["title"]} | {u}')
