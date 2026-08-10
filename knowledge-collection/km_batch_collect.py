# -*- coding: utf-8 -*-
# KM 内部一手 全量补采 → 知识采集库（5 主题，icebreaker=peer 向按治理跳过）
import os, re, json, subprocess, datetime

BASE = os.path.dirname(os.path.abspath(__file__))
NODEBIN = r"C:/Users/v_yitcai/.workbuddy/binaries/node/versions/22.22.2"
CMD = os.path.join(NODEBIN, "mcporter.cmd")
TODAY = "2026-08-10"

THEME_CN = {
    "staff-meeting": "员工大会", "offsite": "Offsite/团建", "award": "颁奖",
    "afternoontea": "下午茶研讨", "openday": "Open Day",
}
THEMES = {
    "staff-meeting": {"wall": "staff-meeting/staff-meeting.html", "emoji": "🎤", "cat": "战略沟通",
        "queries": ["员工大会", "全员大会", "年度大会", "司庆"]},
    "offsite": {"wall": "offsite/offsite.html", "emoji": "🏔️", "cat": "团建 Offsite",
        "queries": ["Offsite", "团建", "团队建设", "骨干团建"]},
    "award": {"wall": "award/award.html", "emoji": "🏆", "cat": "荣誉表彰",
        "queries": ["员工颁奖", "表彰大会", "荣誉表彰", "年会颁奖"]},
    "afternoontea": {"wall": "afternoontea/afternoontea.html", "emoji": "☕", "cat": "分享沙龙",
        "queries": ["下午茶", "技术沙龙", "分享会", "内部沙龙"]},
    "openday": {"wall": "openday/openday.html", "emoji": "🚪", "cat": "品牌/媒体开放日",
        "queries": ["开放日", "客户开放日", "媒体开放日", "品牌开放日"]},
}

HRBP_KW = ["薪酬保密","绩效保密","薪资保密","离职","裁员","hc ","招聘内推","员工隐私","薪资结构","工资保密","脉脉"]
FAMILY_KW = ["家属","家庭日","亲子","家属开放日"]
IR_KW = ["投资者","股东","券商","证监局","资本市场","财报路演","投资人","ir ","ir/"]
PEER_KW = ["破冰游戏","平级向","朋友向"]
TRAVEL_KW = ["自驾游","旅游攻略","毕业旅行","亲子游"]

def km_call(expr, timeout=40):
    try:
        r = subprocess.run(f'"{CMD}" call "{expr}"', shell=True, capture_output=True,
                           text=True, timeout=timeout, encoding="utf-8")
        return r.stdout or ""
    except Exception as e:
        return f"__ERR__{e}"

LABELS = ["标题","作者","创建时间","更新时间","标签","阅读","点赞","收藏","评论","K吧","热度","链接"]
def extract(block):
    d = {}; pos = 0
    for i, l in enumerate(LABELS):
        m = re.search(re.escape(l) + r"\s*[:：]\s*", block[pos:])
        if not m: continue
        vs = pos + m.end()
        nxt = LABELS[i+1] if i+1 < len(LABELS) else None
        if nxt:
            nm = re.search(r",\s*" + re.escape(nxt) + r"\s*[:：]", block[vs:])
            ve = vs + nm.start() if nm else len(block)
        else:
            ve = len(block)
        d[l] = block[vs:ve].strip()
        pos = ve
    return d

def parse_list(text):
    arts = []; cur = None
    for ln in text.split("\n"):
        if ln.lstrip().startswith("- 标题:"):
            if cur: arts.append(cur)
            cur = ln
        elif cur is not None:
            cur += " " + ln
    if cur: arts.append(cur)
    out = []
    for a in arts:
        d = extract(a)
        if d.get("标题") and d.get("链接"):
            out.append(d)
    return out

def get_abstract(link):
    m = re.search(r"/articles/show/(\d+)", link)
    if not m: return ""
    aid = m.group(1)
    raw = km_call(f"km.show-article(article: '{aid}')", timeout=30)
    if raw.startswith("__ERR__"): return ""
    # extract AI摘要
    m2 = re.search(r"AI摘要\s*[:：]\s*(.*)", raw, re.S)
    if not m2: return ""
    ab = m2.group(1).strip()
    if "无法" in ab or "缺乏" in ab or "不是一篇" in ab or len(ab) < 15:
        return ""
    return ab[:240]

def kbar_name(kbar):
    if not kbar: return "KM"
    m = re.search(r"#\d+\s+(.*?)\s*https", kbar)
    return m.group(1).strip() if m else kbar[:30]

def detect_relation(title, tags, kbar):
    t = (title + tags + kbar)
    if re.search(r"高管|CEO|战略|VP|总经理|总裁|董事|管理层|CXO|副总|总监", t):
        return "exec"
    return "supervisor"

def should_skip(theme, d):
    t = (d.get("标题","") + d.get("标签","") + d.get("K吧",""))
    if any(k in t for k in HRBP_KW): return "hrbp"
    if any(k in t for k in FAMILY_KW): return "family"
    if theme == "openday" and any(k in t for k in IR_KW): return "ir"
    if any(k in t for k in PEER_KW): return "peer"
    if theme == "offsite" and any(k in t for k in TRAVEL_KW) and "团建" not in t and "team" not in t.lower():
        return "travel"
    return None

def norm_title(s):
    return re.sub(r"[\s\u3000\W_]+", "", s).lower()

def norm_url(u):
    return u.split("?")[0].rstrip("/")

# ---------- load index.json dedup set ----------
idx_path = os.path.join(BASE, "index.json")
idx_text = open(idx_path, encoding="utf-8").read()
idx = json.loads(idx_text)  # JSON array of cards
assert isinstance(idx, list), "index.json must be a list"
seen_urls = set(); seen_titles = set()
for c in idx:
    if c.get("url"): seen_urls.add(norm_url(c["url"]))
    if c.get("title"): seen_titles.add(norm_title(c["title"]))

# ---------- collect ----------
added_total = 0
added_by_theme = {}
obs_rows = []   # (theme, title, src, rel, oneliner)
new_cards_for_index = []  # (key, card)

for theme, cfg in THEMES.items():
    print(f"\n===== 主题 {theme} ({THEME_CN[theme]}) =====")
    collected = {}  # url -> dict
    for q in cfg["queries"]:
        raw = km_call(f"km.list-articles(keywords: ['{q}'], limit: 8)", timeout=40)
        if raw.startswith("__ERR__"):
            print(f"  [WARN] list 失败: {q} -> {raw[:60]}")
            continue
        for d in parse_list(raw):
            u = norm_url(d.get("链接",""))
            if u and u not in collected:
                collected[u] = d
    print(f"  list 原始命中（去重后）: {len(collected)}")

    sec2, sec3 = [], []
    theme_added = 0
    for u, d in collected.items():
        title = d.get("标题","")
        if u in seen_urls or norm_title(title) in seen_titles:
            continue
        skip = should_skip(theme, d)
        if skip:
            print(f"  [skip:{skip}] {title[:30]}")
            continue
        # fetch abstract
        ab = get_abstract(d.get("链接",""))
        kb = kbar_name(d.get("K吧",""))
        rel = detect_relation(title, d.get("标签",""), d.get("K吧",""))
        val = ab if ab else f"【KM 内部一手】{title}（{kb} 实践）。"
        how = (f"内部参考：{kb} 的真实落地做法，可迁移至本公司「{THEME_CN[theme]}」场景；"
               f"重点提取其议程结构 / 互动环节 / 叙事温度，避免照搬形式。")
        note = (f"② 公司内部上下级场景（KM 内部一手，{kb} 实践可抄）" if rel == "supervisor"
                else f"③ 高管间场景（KM 内部一手，{kb} 实践可抄）")
        src_short = "km.woa.com/articles/show/" + re.search(r"/show/(\d+)", u).group(1)
        rel_badge = ('<span class="badge r2">上下级</span>' if rel == "supervisor"
                     else '<span class="badge r3">高管间</span>')
        block = (
            '    <div class="hl">\n'
            f'      <div class="top"><span class="emoji">{cfg["emoji"]}</span><h3>{title}</h3>'
            f'<span class="cat">{cfg["cat"]}</span>{rel_badge}<span class="badge b1">一手</span></div>\n'
            f'      <p class="val">{val}</p>\n'
            '      <details class="exec"><summary>怎么做</summary>'
            f'<div class="inner">{how}</div></details>\n'
            f'      <div class="src">🔗 <a href="{u}" target="_blank">{src_short}</a></div>\n'
            f'      <div class="note">适用：{note}</div>\n'
            '    </div>\n'
        )
        card = {"title": title, "normKey": title, "url": u, "sourceType": "primary",
                "relation": "supervisor" if rel == "supervisor" else "exec",
                "summary": val, "topic": theme, "source": "km"}
        if rel == "supervisor":
            sec2.append(block)
        else:
            sec3.append(block)
        new_cards_for_index.append(card)
        obs_rows.append((theme, title, "一手", "②上下级" if rel=="supervisor" else "③高管间",
                         f"{kb}：{title}"))
        seen_urls.add(u); seen_titles.add(norm_title(title))
        theme_added += 1
        print(f"  [+{rel}] {title[:34]}")

    # ---------- insert into wall ----------
    if sec2 or sec3:
        wpath = os.path.join(BASE, cfg["wall"])
        html = open(wpath, encoding="utf-8").read()
        # sec2 before sec3 marker
        m2 = html.find('<div class="sec sec3">')
        if m2 != -1:
            html = html[:m2] + "".join(sec2) + html[m2:]
        else:
            # no sec3 -> insert before footer
            fi = html.rfind('<footer>'); di = html[:fi].rfind('</div>')
            html = html[:di] + "".join(sec2) + html[di:]
        # sec3 before closing </div> of sec3 (just before footer)
        fi = html.rfind('<footer>'); di = html[:fi].rfind('</div>')
        html = html[:di] + "".join(sec3) + html[di:]
        # update counts: first "N 卡" = sec2, second = sec3
        tags = list(re.finditer(r'<span class="tag">(\d+) 卡</span>', html))
        if len(tags) >= 2:
            s2n = int(tags[0].group(1)) + len(sec2)
            s3n = int(tags[1].group(1)) + len(sec3)
            html = html[:tags[0].start()] + f'<span class="tag">{s2n} 卡</span>' + html[tags[0].end():]
            # recompute second after first replace shifted indices
            tags2 = list(re.finditer(r'<span class="tag">(\d+) 卡</span>', html))
            html = html[:tags2[1].start()] + f'<span class="tag">{s3n} 卡</span>' + html[tags2[1].end():]
        # hero subtitle append
        hp = html.find('<div class="hero">')
        if hp != -1:
            ep = html.find('</p>', hp)
            html = html[:ep] + f"｜ KM补采 {TODAY}(+{theme_added})" + html[ep:]
        assert "📌 本页由 yitong 沉淀整理" in html, "footer lost!"
        open(wpath, "w", encoding="utf-8").write(html)
        print(f"  墙更新: sec2+{len(sec2)} sec3+{len(sec3)} -> 文件 OK, footer OK")
    added_by_theme[theme] = theme_added
    added_total += theme_added

# ---------- update index.json (append to list) ----------
if new_cards_for_index:
    idx.extend(new_cards_for_index)
    open(idx_path, "w", encoding="utf-8").write(json.dumps(idx, ensure_ascii=False, indent=1))
    print(f"\nindex.json +{len(new_cards_for_index)} 卡（现 {len(idx)} 卡）")

# ---------- Obsidian 00-索引.md ----------
ob_path = r"C:\Users\v_yitcai\Documents\Obsidian\知识采集库\00-知识采集索引.md"
if os.path.exists(ob_path) and obs_rows:
    t = open(ob_path, encoding="utf-8").read()
    tbl = "\n".join(f"| {ti}（{th}.html） | 4 | {src} | {rel} | {one} |"
                    for (th, ti, src, rel, one) in obs_rows)
    marker = "## 主题："
    mi = t.find(marker)
    if mi != -1:
        t = t[:mi] + tbl + "\n\n" + t[mi:]
    # bump master total **N 卡** (first occurrence)
    m0 = re.search(r"\*\*(\d+) 卡\*\*", t)
    if m0:
        newtot = int(m0.group(1)) + len(obs_rows)
        t = t[:m0.start()] + f"**{newtot} 卡**" + t[m0.end():]
    t = t.replace("）", "）", 1)  # noop
    open(ob_path, "w", encoding="utf-8").write(t)
    print(f"Obsidian 00-索引 +{len(obs_rows)} 行")

print("\n========== 汇总 ==========")
for th, n in added_by_theme.items():
    print(f"  {th} ({THEME_CN[th]}): +{n}")
print(f"  总计新增: {added_total}")
print("  KM 内部一手补采完成。下一步：sync GitHub + 验证。")
