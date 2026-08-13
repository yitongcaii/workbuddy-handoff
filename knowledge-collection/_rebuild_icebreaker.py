# -*- coding: utf-8 -*-
import json, re, os

KC = os.path.dirname(os.path.abspath(__file__))
IB_DIR = os.path.join(KC, "icebreaker")
WALL = os.path.join(IB_DIR, "icebreaker.html")
INDEX = os.path.join(KC, "index.json")

data = open(WALL, encoding="utf-8").read()

# ---- extract CSS ----
css = re.search(r'<style>(.*?)</style>', data, re.S).group(1)
# ---- extract hero ----
hero = re.search(r'<div class="hero">.*?</div>\s*</div>', data, re.S).group(0)
# ---- extract sec descriptions ----
def sec_desc(n):
    m = re.search(r'<div class="sec sec%d">.*?<span class="desc">(.*?)</span>' % n, data, re.S)
    return m.group(1) if m else ""
desc3 = sec_desc(3); desc2 = sec_desc(2)

# ---- parse all cards in document order ----
parts = re.split(r'<div class="hl">', data)
def parse(block):
    def g(p):
        m = re.search(p, block, re.S); return m.group(1).strip() if m else None
    return dict(
        title=g(r'<h3>(.*?)</h3>'),
        emoji=g(r'<span class="emoji">(.*?)</span>'),
        cat=g(r'<span class="cat">(.*?)</span>'),
        relc=g(r'badge (r[23])'),
        srcc=g(r'badge (b[12])'),
        url=g(r'<a href="(.*?)"'),
        val=g(r'<p class="val">(.*?)</p>'),
        howto=g(r'<div class="inner">(.*?)</div>'),
        note=g(r'<div class="note">(.*?)</div>'),
        disp=g(r'<a href=".*?">(.*?)</a>'),
    )
cards = []
for p in parts[1:]:
    d = parse(p)
    if not d["title"]:
        continue
    d["rel"] = "exec" if d["relc"] == "r3" else "supervisor"
    d["src"] = "primary" if d["srcc"] == "b1" else "secondary"
    cards.append(d)

exec_cards = [c for c in cards if c["rel"] == "exec"]
sup_cards  = [c for c in cards if c["rel"] == "supervisor"]
print("total parsed:", len(cards), "exec:", len(exec_cards), "sup:", len(sup_cards))

def card_html(c):
    badge_rel = "r3" if c["rel"] == "exec" else "r2"
    rel_txt = "高管间" if c["rel"] == "exec" else "上下级"
    badge_src = "b1" if c["src"] == "primary" else "b2"
    src_txt = "一手" if c["src"] == "primary" else "二手"
    return ('  <div class="hl">\n'
      '      <div class="top"><span class="emoji">%s</span><h3>%s</h3><span class="cat">%s</span>'
      '<span class="badge %s">%s</span><span class="badge %s">%s</span></div>\n'
      '      <p class="val">%s</p>\n'
      '      <details class="exec"><summary>怎么做</summary><div class="inner">%s</div></details>\n'
      '      <div class="src">🔗 <a href="%s" target="_blank">%s</a></div>\n'
      '      <div class="note">%s</div>\n'
      '    </div>' % (
        c["emoji"], c["title"], c["cat"], badge_rel, rel_txt, badge_src, src_txt,
        c["val"], c["howto"], c["url"], c["disp"], c["note"]))

sec3 = ('<div class="sec sec3"><h2>③ 领导↔领导（高管间 · exec）</h2>'
        '<span class="tag">%d 卡</span>\n'
        '    <span class="desc">%s</span>\n  </div>\n  <div class="grid">\n%s\n</div>\n'
        % (len(exec_cards), desc3, "\n".join(card_html(c) for c in exec_cards)))
sec2 = ('<div class="sec sec2"><h2>② 领导↔员工（上下级 · supervisor）</h2>'
        '<span class="tag">%d 卡</span>\n'
        '    <span class="desc">%s</span>\n  </div>\n  <div class="grid">\n%s\n</div>\n'
        % (len(sup_cards), desc2, "\n".join(card_html(c) for c in sup_cards)))

html = ('<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '<title>破冰 · 知识采集卡片墙</title>\n<style>%s</style>\n</head>\n<body>\n'
        '<div class="wrap">\n%s\n%s\n%s'
        '<footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>\n'
        '</div>\n</body>\n</html>') % (css, hero, sec3, sec2)

assert html.count('class="hl"') == len(cards), "count %d vs %d" % (html.count('class="hl"'), len(cards))
assert '📌 本页由 yitong 沉淀整理' in html
tmp = WALL + ".rebuild"
open(tmp, "w", encoding="utf-8").write(html)
os.replace(tmp, WALL)
print("rebuilt wall:", len(cards), "cards; exec", len(exec_cards), "sup", len(sup_cards))

# ---- re-sync index.json: icebreaker segment == wall ----
idx = json.load(open(INDEX, encoding="utf-8"))
others = [x for x in idx if x.get("topic") != "icebreaker"]
print("non-icebreaker entries kept:", len(others))

def norm_key(s):
    s = re.sub(r'[\s\u3000]+', '', s)
    for c in '，。、；:：,.;·•·“”"\'’‘（）()【】[]《》<>/\\|-_—~！!？?…·':
        s = s.replace(c, '')
    return s.lower()

new_seg = []
seen = set()
for c in cards:
    key = (c["title"], c["url"])
    if key in seen:
        continue
    seen.add(key)
    new_seg.append(dict(
        title=c["title"], normKey=norm_key(c["title"]), url=c["url"],
        sourceType=c["src"], relation=c["rel"], topic="icebreaker",
        summary=re.sub(r'\s+', ' ', c["val"])[:400] if c["val"] else ""))
idx2 = others + new_seg
print("icebreaker index entries:", len(new_seg), "total index:", len(idx2))
json.dump(idx2, open(INDEX, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("wrote index.json")
