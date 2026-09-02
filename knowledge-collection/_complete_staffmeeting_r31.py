# -*- coding: utf-8 -*-
import re, json, shutil, os

BASE = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(BASE, 'staff-meeting', 'staff-meeting.html')
INC  = os.path.join(BASE, 'staff-meeting', 'staff-meeting-20260902.html')
IDX  = os.path.join(BASE, 'index.json')
NOTE = r'C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\staff-meeting\员工大会-知识卡汇总.md'
ZIDX = r'C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md'
MAP  = os.path.join(BASE, 'lexiang-entry-map.json')
LAST = os.path.join(BASE, '..', 'last-topic.txt')

# ---------- 1. extract 13 card blocks from increment page ----------
inc = open(INC, encoding='utf-8').read()
assert inc.count('class="hl"') == 13, "increment page card count != 13"
starts = [m.start() for m in re.finditer(r'<div class="hl">', inc)]
def extract(s):
    i, depth = s, 0
    while i < len(inc):
        if inc.startswith('<div', i):
            depth += 1
        elif inc.startswith('</div>', i):
            depth -= 1
            if depth == 0:
                return inc[s:i+6]
        i += 1
    return None
blocks = [extract(s) for s in starts]
assert all(b for b in blocks) and len(blocks) == 13, "block extraction failed"

def field(b, pat):
    m = re.search(pat, b, re.S)
    return m.group(1).strip() if m else ''

cards = []
for b in blocks:
    title = field(b, r'<h3>(.*?)</h3>')
    url   = field(b, r'href="(.*?)"')
    rel   = 'exec' if 'badge r3' in b else 'supervisor'
    src   = 'primary' if 'badge b1' in b else 'secondary'
    cat   = field(b, r'<span class="cat">(.*?)</span>')
    val   = field(b, r'<p class="val">(.*?)</p>')
    note  = field(b, r'<div class="note">(.*?)</div>')
    cards.append(dict(title=title, url=url, rel=rel, src=src, cat=cat, val=val, note=note, block=b))

exec_blocks = [c['block'] for c in cards if c['rel'] == 'exec']
sup_blocks  = [c['block'] for c in cards if c['rel'] == 'supervisor']
print(f"cards total={len(cards)} exec={len(exec_blocks)} sup={len(sup_blocks)}")

# ---------- 2. wall injection ----------
wall = open(WALL, encoding='utf-8').read()
wall_bak = WALL + '.bak-r31'
shutil.copy2(WALL, wall_bak)

EXEC_ANCHOR = '</div>\n    </div></div>\n  <div class="sec sec2">'
SUP_ANCHOR  = '</div>\n    </div></div>\n<footer>'
assert wall.count(EXEC_ANCHOR) == 1, f"EXEC_ANCHOR count={wall.count(EXEC_ANCHOR)}"
assert wall.count(SUP_ANCHOR) == 1, f"SUP_ANCHOR count={wall.count(SUP_ANCHOR)}"

exec_frag = ''.join(exec_blocks)
sup_frag  = ''.join(sup_blocks)

wall = wall.replace(EXEC_ANCHOR, EXEC_ANCHOR.replace('</div>\n  <div class="sec sec2">', exec_frag + '</div>\n  <div class="sec sec2">'), 1)
wall = wall.replace(SUP_ANCHOR, SUP_ANCHOR.replace('</div>\n<footer>', sup_frag + '</div>\n<footer>'), 1)

# hero + counts + increment link
assert wall.count('采集于 2026-08-27（第三十轮 +7）') == 1
wall = wall.replace('采集于 2026-08-27（第三十轮 +7）', '采集于 2026-09-02（第三十一轮 +13）', 1)
assert wall.count('<span class="tag">109 卡</span>') == 1
wall = wall.replace('<span class="tag">109 卡</span>', '<span class="tag">113 卡</span>', 1)
assert wall.count('<span class="tag">214 卡</span>') == 1
wall = wall.replace('<span class="tag">214 卡</span>', '<span class="tag">223 卡</span>', 1)
assert wall.count('href="runs/staff-meeting-2026-08-27-r28.html"') == 1
wall = wall.replace('href="runs/staff-meeting-2026-08-27-r28.html"', 'href="staff-meeting-20260902.html"', 1)

# verify
assert wall.count('class="hl"') == 336, f"wall card count={wall.count('class=\"hl\"')}"
assert wall.count('badge r3') == 113, f"r3={wall.count('badge r3')}"
assert wall.count('badge r2') == 223, f"r2={wall.count('badge r2')}"
assert '📌 本页由 yitong 沉淀整理' in wall
open(WALL, 'w', encoding='utf-8').write(wall)
print(f"WALL updated -> {wall.count('class=\"hl\"')} cards (r3={wall.count('badge r3')}, r2={wall.count('badge r2')})")

# ---------- 3. index.json ----------
idx = json.load(open(IDX, encoding='utf-8'))
def normKey(t): return re.sub(r'[\s（）()「」“”"，。、：；·\-—’‘]', '', t)
before = len([e for e in idx if e.get('topic') == 'staff-meeting'])
for c in cards:
    idx.append({
        "title": c['title'],
        "normKey": normKey(c['title']),
        "url": c['url'],
        "sourceType": c['src'],
        "relation": c['rel'],
        "summary": re.sub(r'\s+', ' ', c['val'])[:160],
        "topic": "staff-meeting"
    })
json.dump(idx, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
after = len([e for e in idx if e.get('topic') == 'staff-meeting'])
print(f"index.json staff-meeting: {before} -> {after} (+{after-before})")

# ---------- 4. vault note ----------
note = open(NOTE, encoding='utf-8').read()
rel_label = {'exec': '③高管间', 'supervisor': '②上下级'}
src_label = {'primary': '一手', 'secondary': '二手'}
rows = '\n'.join(f"| {c['title']} | {rel_label[c['rel']]} | {src_label[c['src']]} |" for c in cards)
section = f"\n## 轮次 2026-09-02（+13）\n\n| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n{rows}\n"
note = note.rstrip() + section
open(NOTE, 'w', encoding='utf-8').write(note)
print("vault note: appended ## 轮次 2026-09-02（+13）")

# ---------- 5. 00-index ----------
z = open(ZIDX, encoding='utf-8').read()
assert z.count('**263 卡**') == 1
z = z.replace('**263 卡**', '**336 卡**', 1)
# append 13 rows to staff-meeting table (before the section's closing or at end of its table)
def oneliner(c):
    n = re.sub(r'^适用[：:]\s*', '', c['note'])
    n = re.sub(r'^[③②]?[一-龥A-Za-z]+?\s*[—–-]\s*', '', n)  # drop leading relation prefix
    n = re.sub(r'\s+', ' ', n).strip()
    return n[:46] + ('…' if len(n) > 46 else '')
score = lambda c: 5 if (c['src'] == 'primary' or c['rel'] == 'exec') else 4
zrows = '\n'.join(
    f"| {c['title']}（staff-meeting.html） | {score(c)} | {src_label[c['src']]} | {rel_label[c['rel']]} | {oneliner(c)} |"
    for c in cards)
# insert rows right after the last existing data row of the staff-meeting table
msec = re.search(r'## 主题：员工大会', z)
mnext = re.search(r'\n## 主题：', z[msec.end():])
sec_end = msec.end() + (mnext.start() if mnext else len(z))
# find last table row index in section
sec = z[msec.start():sec_end]
last_row = None
for mm in re.finditer(r'^\| .*staff-meeting\.html.* \|$', sec, re.M):
    last_row = mm
assert last_row is not None
ins_pos = msec.start() + last_row.end()
z = z[:ins_pos] + '\n' + zrows + z[ins_pos:]
# add round to header history
z = z.replace('二十六轮补采 2026-08-25(+8））',
              '二十六轮补采 2026-08-25(+8）｜ 2026-09-02 三十一轮补采 +13（CEO全员信五段框架/CEO信起草四步/CEO沟通三结构/CEO三阶段激励/英特尔CEO全员信/蚂蚁CEO全员信/72小时法则/管理者级联KPI/留任5步/高EQ坏消息7步/坏消息全员会/匿名Q&A手册/管理者沟通工具包））', 1)
open(ZIDX, 'w', encoding='utf-8').write(z)
print("00-index: +13 rows, header 263->336")

# ---------- 6. lexiang-entry-map pending round ----------
mp = json.load(open(MAP, encoding='utf-8'))
mp['staff-meeting']['rounds'].append({
    "date": "2026-09-02",
    "entry_id": None,
    "name": "staff-meeting-20260902",
    "note": "R31 增量页（乐享 token 401，待重连后补传）"
})
json.dump(mp, open(MAP, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print("lexiang-entry-map: appended pending R31 round (entry_id=null)")

# ---------- 7. last-topic.txt -> Offsite ----------
open(LAST, 'w', encoding='utf-8').write('Offsite\n')
print("last-topic.txt -> Offsite")

print("\nDONE. backup wall at", wall_bak)
