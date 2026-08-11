# -*- coding: utf-8 -*-
import os, re
BASE = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(BASE, 'icebreaker', 'icebreaker.html')
TMP = os.path.join(BASE, 'icebreaker', '.run_newcards.tmp.html')

raw = open(TMP, encoding='utf-8').read()
# split tmp into hl blocks
blocks = []
for m in re.finditer(r'<div class="hl">', raw):
    s = m.start(); i = m.end(); d = 1; j = i
    while j < len(raw):
        if raw[j:j+4] == '<div': d += 1; j += 4
        elif raw[j:j+5] == '</div': d -= 1; j += 5
        else: j += 1
        if d == 0: break
    blocks.append(raw[s:j])
sec2 = ''.join(b for b in blocks if 'badge r2' in b)
print('sec2 blocks from tmp:', sec2.count('<div class="hl">'))

html = open(WALL, encoding='utf-8').read()
anchor = '    </div>\n    </div>\n\n  <footer>'
print('anchor count:', html.count(anchor))
html = html.replace(anchor, '    </div>\n' + sec2 + '    </div>\n\n  <footer>', 1)
open(WALL, 'w', encoding='utf-8').write(html)
print('done. total hl:', html.count('<div class="hl"'))
print('tags:', re.findall(r'<span class="tag">(\d+) 卡</span>', html))
