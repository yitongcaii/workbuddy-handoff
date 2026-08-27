# -*- coding: utf-8 -*-
"""员工大会墙·干净重建：按首枚关系徽章分类，删除重复关系徽章，纠正 grid 错放。"""
import re

WALL = 'knowledge-collection/staff-meeting/staff-meeting.html'
s = open(WALL, encoding='utf-8').read()

def split_cards(html):
    cards = []
    for m in re.finditer(r'<div class="hl">', html):
        i = m.end(); d = 1; j = i
        while j < len(html):
            if html[j:j+4] == '<div':
                d += 1; j += 4
            elif html[j:j+5] == '</div':
                d -= 1; j += 6
            else:
                j += 1
            if d == 0:
                break
        cards.append(html[m.start():j])
    return cards

REL_RE = re.compile(r'<span class="badge (r[123])">([^<]*)</span>')

def clean_card(c):
    """删除多余关系徽章（仅保留首枚），返回 (clean_html, rel_code)。"""
    spans = list(REL_RE.finditer(c))
    if len(spans) <= 1:
        rel = spans[0].group(1) if spans else 'r2'
        return c, rel
    # 保留首枚，删除其余关系徽章
    keep = spans[0]
    rel = keep.group(1)
    out = c
    for sp in spans[1:]:
        out = out[:sp.start()] + out[sp.end():]
    return out, rel

all_cards = split_cards(s)
assert len(all_cards) == 310, f'expected 310 got {len(all_cards)}'

r3, r2 = [], []
duplicates = 0
for c in all_cards:
    cc, rel = clean_card(c)
    if REL_RE.findall(c).__len__() > 1:
        duplicates += 1
    (r3 if rel == 'r3' else r2).append(cc)

print('cleaned: r3=%d r2=%d total=%d | removed %d duplicate-relation cards' % (len(r3), len(r2), len(r3)+len(r2), duplicates))
assert len(r3) + len(r2) == 310

# 重建
sec3_start = s.find('<div class="sec sec3">')
preamble = s[:sec3_start]
footer = s[s.rfind('<footer>'):]
# hero/link 已在上一轮更新，直接沿用

def sec_block(cls, label, count, cards):
    cards_html = '\n'.join(cards)
    return f'''  <div class="sec {cls}">
    <h2>{label}</h2>
    <span class="tag">{count} 卡</span>
  </div>
  <div class="grid">
{cards_html}
  </div>
'''

body = (sec_block('sec3', '③ 领导↔领导（高管间 · exec）', len(r3), r3)
        + sec_block('sec2', '② 领导↔员工（上下级 · supervisor）', len(r2), r2))
new_wall = preamble + body + footer
open(WALL, 'w', encoding='utf-8').write(new_wall)
print('WALL rewritten bytes=%d' % len(new_wall))

# 校验
v = open(WALL, encoding='utf-8').read()
grids = [m.start() for m in re.finditer(r'<div class="grid">', v)]
def cards_in(region):
    i = region.find('<div class="grid">') + len('<div class="grid">'); d=1; j=i
    while j < len(region):
        if region[j:j+4]=='<div': d+=1; j+=4
        elif region[j:j+5]=='</div': d-=1; j+=6
        else: j+=1
        if d==0: break
    return re.split(r'<div class="hl">', region[i:j])[1:]
g1 = cards_in(v[grids[0]:grids[1]]); g2 = cards_in(v[grids[1]:])
def rt(c):
    m = REL_RE.search(c); return m.group(2) if m else '??'
from collections import Counter
print('GRID1 sec3:', Counter(rt(c) for c in g1))
print('GRID2 sec2:', Counter(rt(c) for c in g2))
print('tags:', re.findall(r'<span class="tag">(\d+) 卡</span>', v))
print('footer ok:', '📌 本页由 yitong' in v, '| grids:', v.count('class="grid"'))
