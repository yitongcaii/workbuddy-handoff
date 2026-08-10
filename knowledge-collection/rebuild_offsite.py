import re

PATH = r"c:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection\offsite\offsite.html"
html = open(PATH, encoding="utf-8").read()

# 1) extract all cards in document order, tracking section by last sentinel
sentinel3 = html.index('<!-- ============ ③')
sentinel2 = html.index('<!-- ============ ②')

cards = []  # (section, card_html)
positions = []
for m in re.finditer(r'<div class="hl">', html):
    start = m.start()
    i = m.end()
    depth = 1
    j = i
    while j < len(html):
        if html[j:j+4] == '<div':
            depth += 1
            j += 4
        elif html[j:j+5] == '</div':
            depth -= 1
            j += 5
            if depth == 0:
                break
        else:
            j += 1
    card = html[start:j]
    if start > sentinel3 and start < sentinel2:
        sec = 'sec3'
    elif start > sentinel2:
        sec = 'sec2'
    else:
        sec = 'sec3'  # before any sentinel (shouldn't happen)
    cards.append((sec, card))
    positions.append((start, sec))

sec3 = [c for s, c in cards if s == 'sec3']
sec2 = [c for s, c in cards if s == 'sec2']
print('sec3', len(sec3), 'sec2', len(sec2), 'total', len(cards))

# 2) preamble = head+body+wrap+hero (everything before the ③ comment)
preamble = html[:sentinel3]

# update hero subtitle
preamble = preamble.replace(
    "｜ KM补采 2026-08-10(+3)</p>",
    "｜ KM补采 2026-08-10(+3) ｜ 2026-08-10 七轮补采 +10</p>",
    1,
)

# 3) regenerate section headers + grids
sec3_header = f'''  <div class="sec sec3">
    <h2>③ 领导↔领导（高管间 · exec）</h2>
    <span class="tag">{len(sec3)} 卡</span>
    <span class="desc">商务化、以专业/共同目标切入，避免幼稚游戏；含战略务虚会、闭门决策会、领导力团队 offsite 议程模板与权威方法论</span>
  </div>
  <div class="grid">
'''
sec2_header = f'''  <div class="sec sec2">
    <h2>② 领导↔员工（上下级 · supervisor）</h2>
    <span class="tag">{len(sec2)} 卡</span>
    <span class="desc">尊重、不隐私暴露、建信任不越界；含行动学习工作坊、群策群力、复盘工作坊、管理层团建与信任责任建设</span>
  </div>
  <div class="grid">
'''

footer = '\n  <footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>\n</div>\n</body>\n</html>\n'

out = preamble
out += sec3_header
out += "\n".join(sec3)
out += "\n  </div>\n\n"
out += sec2_header
out += "\n".join(sec2)
out += "\n  </div>\n"
out += footer

open(PATH, "w", encoding="utf-8").write(out)
print("written", len(out), "bytes")
