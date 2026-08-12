# -*- coding: utf-8 -*-
import re, os, json, tempfile

BASE = "c:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection/award"
HTML = os.path.join(BASE, "award.html")
INDEX = "c:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection/index.json"
RUN_DATE = "20260813"
WALL_URL = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/award.html"
RUNS_URL = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/runs/index.html"

html = open(HTML, encoding="utf-8").read()

# ---- 1. extract style + preamble(hero) ----
style = re.search(r"<style>.*?</style>", html, re.S).group(0)
body_start = html.index("<body>")
pre_end = html.index("<!-- ============ ③")
preamble = html[body_start:pre_end]

# update hero <p> (append this round)
m = re.search(r"(<p>首次采集.*?</p>)", preamble, re.S)
old_p = m.group(1)
assert "十一轮" not in old_p, "already enriched?"
new_p = old_p[:-4] + " ｜ 十一轮 enrich 2026-08-13(+5)</p>"
preamble = preamble.replace(old_p, new_p, 1)

# ---- 2. parse existing cards (raw blocks) + classify ----
def card_blocks(s):
    blocks = []
    for mt in re.finditer(r'<div class="hl">', s):
        i = s.index(">", mt.start()) + 1
        depth = 1
        while i < len(s):
            if s.startswith("<div", i):
                depth += 1
                i = s.index(">", i) + 1
            elif s.startswith("</div>", i):
                depth -= 1
                i = s.index(">", i) + 1
                if depth == 0:
                    break
            else:
                i += 1
        blocks.append(s[mt.start():i])
    return blocks

existing = card_blocks(html)
exec_cards = [b for b in existing if 'class="badge r3"' in b]
sup_cards  = [b for b in existing if 'class="badge r3"' not in b]
assert len(existing) == len(exec_cards) + len(sup_cards), (len(existing), len(exec_cards), len(sup_cards))

# ---- 3. new cards ----
def card(emoji, title, cat, rel, src, val, how, url, note):
    rel_badge = ""
    if "exec" in rel:
        rel_badge += '<span class="badge r3">高管间</span>'
    if "supervisor" in rel:
        rel_badge += '<span class="badge r2">上下级</span>'
    src_cls = "b1" if src == "一手" else "b2"
    disp = url.split("//", 1)[-1]
    return (f'<div class="hl">\n'
            f'  <div class="top"><span class="emoji">{emoji}</span><h3>{title}</h3>'
            f'<span class="cat">{cat}</span>{rel_badge}<span class="badge {src_cls}">{src}</span></div>\n'
            f'  <p class="val">{val}</p>\n'
            f'  <details class="exec"><summary>怎么做</summary><div class="inner">{how}</div></details>\n'
            f'  <div class="src">🔗 <a href="{url}" target="_blank">{disp}</a></div>\n'
            f'  <div class="note">{note}</div>\n'
            f'</div>')

new_cards = [
    card("🏛️", "复星国际·外部治理奖项与ESG绩效纳入高管考核", "高管荣誉体系", ["exec"], "一手",
         "复星国际获 Corporate Governance Asia 第15届亚洲卓越奖（双CEO同获 Asia's Best CEO，并揽 Sustainable Asia / 最佳环境责任 / 最佳企业传播等5项）。关键机制：将 ESG 管理绩效作为执行董事绩效考核因素，自上而下长效 ESG 改善机制延伸至各业务集团 CEO 与负责人。外部权威治理奖项成为治理层荣誉信号。",
         "借鉴：把荣誉/ESG 纳入高管绩效考核，形成『自上而下长效荣誉机制』——治理层奖项不只是对外品牌，更对内导向高管行为；可迁移至本公司高管表彰设计，让外部权威奖项与内部高管考核挂钩。",
         "https://en.fosun.com/content/details46_5420.html",
         "适用：③ 公司治理/高管间场景（外部权威奖项作为高管荣誉信号 + ESG 纳入高管考核）"),
    card("🔁", "日-周-月-季四级认可机制（日常点赞→奥斯卡式年会颁奖）", "认可节奏机制", ["supervisor"], "二手",
         "把认可从『年度单次事件』拆成日常节奏——日常企业微信即时点赞、周例会『闪电奖』、月度『王者擂台』业绩龙虎榜、季度奥斯卡式颁奖典礼（走红毯+奖杯）。配合总裁共进午餐/创新实验室冠名权等荣誉性奖励，重大获奖信息官网+行业媒体发布增强社会认可。",
         "借鉴：用『日-周-月-季』四级节奏把颁奖典礼的庄重感日常化，避免一年一次认可断层；管理层日常即可通过轻量认可维持热度，季度盛典收口。",
         "https://m.renrendoc.com/paper/449804869.html",
         "适用：② 上下级日常认可场景（管理者用四级节奏把颁奖日常化）"),
    card("🪜", "荣誉与职业发展强挂钩（晋升通道+荣誉档案持续闭环）", "长效机制", ["supervisor"], "二手",
         "荣誉激励最终落脚点是职业发展——获核心荣誉自动获得晋升资格/答辩优先推荐；荣誉积分转化为积分商城权益。实体荣誉墙/电子荣誉墙陈列照片证书事迹；线上荣誉传播矩阵（短视频/推文/直播）。荣誉档案管理形成『持续循环』而非一次性事件。",
         "借鉴：把颁奖从『一次性仪式』升级为『荣誉→晋升→档案→持续激励』的闭环；管理者在颁奖时同步宣导荣誉与晋升/福利的强关联，放大长期激励。",
         "https://m.renrendoc.com/paper/529537903.html",
         "适用：② 上下级长效激励场景（荣誉与晋升/职业发展强挂钩）"),
    card("⚖️", "评先评优公平机制（申报→公示→异议处理+申诉通道+第三方存证）", "评选公平性", ["supervisor"], "二手",
         "流程节点全程公示（申报→初审→复审→全员公示→异议处理→最终确认）；邀请工会/员工代表民主监督；设置申诉机制由专门小组客观复议；引入数字化平台（如 i人事）全流程留痕、自动生成报表防暗箱。跨部门协作人员采用联合提名+权重计入防归属不清。",
         "借鉴：颁奖的公信力来自『公示+申诉+留痕』三件套——在表彰制度设计阶段就内置异议处理窗口与第三方存证，避免评选争议反噬士气。",
         "https://blog.ihr360.com/p/63131",
         "适用：② 上下级评选治理场景（公示+申诉+第三方存证防暗箱）"),
    card("🍽️", "把颁奖融入日常：高管午餐会轻量表彰（Leadership Excellence Award）", "日常化颁奖", ["supervisor"], "二手",
         "Take 5 由 EVP 创设年度 Leadership Excellence Award，CEO 在总部午餐会上亲手表彰表现卓越的企业级员工；配合日常『High 5』认可（2000+人/年）、月度 Super Tech、Presidents Club（最佳经理携家属度假）。认可从盛典延伸到日常轻量场景。",
         "借鉴：高管不必只在年度盛典颁奖——把颁奖下沉到午餐会/日常轻量场景，由高管亲自颁发，拉近与获奖员工距离、维持认可热度。",
         "https://www.drivenbrands.com/news/take-5-oil-change-launches-leadership-excellence-award",
         "适用：② 上下级日常轻量颁奖场景（高管午餐会亲手表彰）"),
]

# classify new
new_exec = [c for c in new_cards if "class=\"badge r3\"" in c]
new_sup  = [c for c in new_cards if "class=\"badge r3\"" not in c]

# ---- 4. render summary wall ----
def sec(sec_cls, tag_cls, tag_txt, desc, cards):
    out = [f'  <div class="sec {sec_cls}">',
           f'    <h2>{"③" if sec_cls=="sec3" else "②"} 颁奖典礼 · {tag_txt}</h2>',
           f'    <span class="tag">{tag_cls}</span>',
           f'    <span class="desc">{desc}</span>',
           f'  </div>',
           f'  <div class="grid">']
    out += ["    " + c for c in cards]
    out.append('  </div>')
    return "\n".join(out)

body_parts = [
    preamble.rstrip(),
    "",
    sec("sec3", "高管间", "领导↔领导（exec）", "商务化 · 战略/治理荣誉信号", exec_cards + new_exec),
    "",
    sec("sec2", "上下级", "领导↔员工（supervisor）", "尊重 · 建信任不越界", sup_cards + new_sup),
    "",
    '</div>',
    '  <footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>',
    '</body>',
    '</html>',
]
new_html = "<!DOCTYPE html>\n<html lang=\"zh-CN\">\n<head>\n<meta charset=\"UTF-8\">\n" \
           "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n" \
           "<title>颁奖典礼 · 知识采集卡片墙</title>\n" + style + "\n</head>\n" + "\n".join(body_parts) + "\n"

# atomic write
tmp = HTML + ".tmp"
open(tmp, "w", encoding="utf-8").write(new_html)
os.replace(tmp, HTML)

total = len(existing) + len(new_cards)
print("SUMMARY WALL:", total, "cards (exec", len(exec_cards)+len(new_exec), "/ sup", len(sup_cards)+len(new_sup), ")")

# ---- 5. render increment page ----
def inc_sec(title, cards):
    if not cards:
        return ""
    return ('  <div class="sec %s">\n    <h2>%s</h2>\n    <span class="tag">%s</span>\n  </div>\n'
            '  <div class="grid">\n%s\n  </div>' % (
            "sec3" if "exec" in title else "sec2",
            title, "高管间" if "exec" in title else "上下级",
            "\n".join("    "+c for c in cards)))

inc = ("<!DOCTYPE html>\n<html lang=\"zh-CN\">\n<head>\n<meta charset=\"UTF-8\">\n"
       "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
       "<title>颁奖典礼 · 本轮新增卡片（+5）</title>\n" + style + "\n</head>\n<body>\n"
       '<div class="wrap">\n'
       f'<p style="margin:0 0 16px"><a href="{WALL_URL}" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">🏆 返回累计卡片墙 →</a> '
       f'<a href="{RUNS_URL}" style="display:inline-block;background:#e6f7ff;color:#00b8d9;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;margin-left:8px;">📑 分页独立页 →</a></p>\n'
       '  <div class="hero">\n'
       '    <h1>🏆 颁奖典礼 · 本轮新增卡片（+5）</h1>\n'
       '    <p>轮次：十一轮 enrich ｜ 运行日期 2026-08-13 ｜ 仅 ②上下级 / ③高管间（已剔除平级/朋友向）</p>\n'
       '    <div class="relbar"><span>② 领导↔员工（上下级，supervisor）</span><span>③ 领导↔领导（高管间，exec）</span></div>\n'
       '  </div>\n'
       + inc_sec("③ 高管间（1）", new_exec) + "\n"
       + inc_sec("② 上下级（4）", new_sup) + "\n"
       '</div>\n  <footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>\n</body>\n</html>\n')
inc_path = os.path.join(BASE, f"award-{RUN_DATE}.html")
open(inc_path, "w", encoding="utf-8").write(inc)
print("INCREMENT PAGE bytes:", os.path.getsize(inc_path), "->", inc_path)

# ---- 6. update index.json ----
def norm(t):
    return re.sub(r"[\s·，。、,.\u3000]+", "", t)

entries = [
    {"title": c[1], "normKey": norm(c[1]), "url": c[8],
     "sourceType": "primary" if c[4]=="一手" else "secondary",
     "relation": "+".join(c[3]),
     "summary": c[5][:120]}
    for c in [
        ("", "复星国际·外部治理奖项与ESG绩效纳入高管考核", "", ["exec"], "一手",
         "复星国际获亚洲卓越奖（双CEO获Asia's Best CEO），关键机制将ESG绩效纳入执行董事考核；外部治理奖项成高管荣誉信号。",
         "", "https://en.fosun.com/content/details46_5420.html", ""),
        ("", "日-周-月-季四级认可机制（日常点赞→奥斯卡式年会颁奖）", "", ["supervisor"], "二手",
         "把认可拆成日点赞/周闪电奖/月擂台/季奥斯卡式颁奖的日常节奏，配合总裁午餐等荣誉性奖励，避免一年一次认可断层。",
         "", "https://m.renrendoc.com/paper/449804869.html", ""),
        ("", "荣誉与职业发展强挂钩（晋升通道+荣誉档案持续闭环）", "", ["supervisor"], "二手",
         "核心荣誉自动获晋升资格/答辩优先；荣誉积分兑商城；实体+线上荣誉墙；荣誉档案形成持续激励闭环而非一次性事件。",
         "", "https://m.renrendoc.com/paper/529537903.html", ""),
        ("", "评先评优公平机制（申报→公示→异议处理+申诉通道+第三方存证）", "", ["supervisor"], "二手",
         "流程全程公示+工会/员工代表监督+申诉复议+数字化平台留痕防暗箱；跨部门联合提名权重计入防归属不清。",
         "", "https://blog.ihr360.com/p/63131", ""),
        ("", "把颁奖融入日常：高管午餐会轻量表彰（Leadership Excellence Award）", "", ["supervisor"], "二手",
         "Take 5 由EVP创年度奖，CEO在午餐会亲手表彰企业级员工；认可从盛典下沉到日常轻量场景维持热度。",
         "", "https://www.drivenbrands.com/news/take-5-oil-change-launches-leadership-excellence-award", ""),
    ]
]

data = json.load(open(INDEX, encoding="utf-8"))
existing_urls = {e.get("url") for e in data}
existing_norm = {e.get("normKey") for e in data}
added = 0
for e in entries:
    if e["url"] in existing_urls or e["normKey"] in existing_norm:
        print("DUP skipped:", e["title"])
        continue
    data.append(e)
    added += 1
tmpj = INDEX + ".tmp"
json.dump(data, open(tmpj, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
os.replace(tmpj, INDEX)
print("INDEX added:", added, "total:", len(data))

# dump new card titles+relation for obsidian step
json.dump(
    [{"title": e["title"], "relation": e["relation"], "sourceType": e["sourceType"]} for e in entries],
    open(os.path.join(BASE, "_r11_new.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("OK")
