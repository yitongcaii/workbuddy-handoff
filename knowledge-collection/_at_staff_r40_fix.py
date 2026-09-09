# -*- coding: utf-8 -*-
"""R40 fix：airmeet 卡与既有 staff-meeting 卡 URL 撞重（index.json 已正确 skip），
从墙与 tmp 中移除该卡，计数 271→270、hero +8→+7。index.json 已是 +7，无需动。"""
import re, os

KC = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(KC, 'staff-meeting', 'staff-meeting.html')
TMP = os.path.join(KC, 'staff-meeting', '.run_newcards.tmp.html')

def split_cards(html):
    cards = []
    for m in re.finditer(r'<div class="hl">', html):
        s = m.start(); i = m.end(); d = 1; j = i
        while j < len(html):
            if html[j:j+4] == '<div':
                d += 1; j += 4
            elif html[j:j+5] == '</div':
                d -= 1; j += 6
            else:
                j += 1
            if d == 0:
                break
        cards.append(html[s:j])
    return cards

def remove_card_containing(html, token):
    cards = split_cards(html)
    hit = None
    for c in cards:
        if token in c:
            hit = c; break
    if hit is None:
        print('FIX: card containing', token, 'NOT found'); return html, False
    html = html.replace(hit, '', 1)
    print('FIX: removed card containing', token)
    return html, True

# ---- 墙 ----
w = open(WALL, encoding='utf-8').read()
before_cnt = w.count('class="hl">', 0)  # rough
w, ok = remove_card_containing(w, 'airmeet.com/hub/blog/measuring-employee-engagement')
if ok:
    w = w.replace('    <span class="tag">271 卡</span>', '    <span class="tag">270 卡</span>', 1)
    w = w.replace('四十轮 enrich 2026-09-09(+8)</p>', '四十轮 enrich 2026-09-09(+7)</p>', 1)
    open(WALL, 'w', encoding='utf-8').write(w)
    print('WALL fixed. len=', len(w))

# ---- tmp ----
t = open(TMP, encoding='utf-8').read()
t, ok2 = remove_card_containing(t, 'airmeet.com/hub/blog/measuring-employee-engagement')
if ok2:
    open(TMP, 'w', encoding='utf-8').write(t)
    print('TMP fixed. cards=', len(split_cards(t)))
