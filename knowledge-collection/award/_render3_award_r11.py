# -*- coding: utf-8 -*-
import re, os, json, shutil

BASE = "c:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection/award"
MIRROR = "c:/Users/v_yitcai/WorkBuddy/20260728154244/handoff-repo/knowledge-collection/award/award.html"
HTML = os.path.join(BASE, "award.html")
INDEX = "c:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection/index.json"
RUN_DATE = "20260813"
WALL_URL = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/award.html"
RUNS_URL = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/runs/index.html"

shutil.copyfile(MIRROR, HTML)
raw = open(HTML, encoding="utf-8").read()

# ---- extract 64 existing card blocks (flat siblings) ----
opens = [m.start() for m in re.finditer(r'<div class="hl">', raw)]
closes = [m.start() for m in re.finditer(r'</div>', raw)]
footer_pos = raw.find('📌 本页由 yitong')
blocks = []
for i, o in enumerate(opens):
    nxt = opens[i + 1] if i + 1 < len(opens) else footer_pos
    if nxt < 0:
        nxt = len(raw)
    mc = max(c for c in closes if c < nxt)
    blocks.append(raw[o:mc + 6])
assert len(blocks) == 64, len(blocks)

# ---- parse fields from each block ----
def parse(b):
    def g(pat):
        m = re.search(pat, b, re.S)
        return m.group(1).strip() if m else ""
    emoji = g(r'<span class="emoji">(.*?)</span>')
    title = g(r'<h3>(.*?)</h3>')
    cat = g(r'<span class="cat">(.*?)</span>')
    val = g(r'<p class="val">(.*?)</p>')
    how = g(r'<div class="inner">(.*?)</div>')
    src_m = re.search(r'<div class="src">.*?href="(.*?)".*?>(.*?)</a>', b, re.S)
    url = src_m.group(1).strip() if src_m else ""
    note = g(r'<div class="note">(.*?)</div>')
    is_exec = 'class="badge r3"' in b
    is_sup = 'class="badge r2"' in b
    rel = []
    if is_exec: rel.append("exec")
    if is_sup: rel.append("supervisor")
    src = "一手" if 'class="badge b1"' in b else "二手"
    return dict(emoji=emoji, title=title, cat=cat, val=val, how=how,
                url=url, note=note, rel=rel, src=src)

existing = [parse(b) for b in blocks]
# dedupe by title
seen = set(); ded = []
for c in existing:
    if c["title"] in seen: continue
    seen.add(c["title"]); ded.append(c)
existing = ded
assert len(existing) == 64, len(existing)

# ---- new cards ----
new_cards = [
    dict(emoji="🏛️", title="复星国际·外部治理奖项与ESG绩效纳入高管考核", cat="高管荣誉体系",
         rel=["exec"], src="一手",
         val="复星国际获 Corporate Governance Asia 第15届亚洲卓越奖（双CEO同获 Asia's Best CEO，并揽 Sustainable Asia / 最佳环境责任 / 最佳企业传播等5项）。关键机制：将 ESG 管理绩效作为执行董事绩效考核因素，自上而下长效 ESG 改善机制延伸至各业务集团 CEO 与负责人。外部权威治理奖项成为治理层荣誉信号。",
         how="借鉴：把荣誉/ESG 纳入高管绩效考核，形成『自上而下长效荣誉机制』——治理层奖项不只是对外品牌，更对内导向高管行为；可迁移至本公司高管表彰设计，让外部权威奖项与内部高管考核挂钩。",
         url="https://en.fosun.com/content/details46_5420.html",
         note="适用：③ 公司治理/高管间场景（外部权威奖项作为高管荣誉信号 + ESG 纳入高管考核）"),
    dict(emoji="🔁", title="日-周-月-季四级认可机制（日常点赞→奥斯卡式年会颁奖）", cat="认可节奏机制",
         rel=["supervisor"], src="二手",
         val="把认可从『年度单次事件』拆成日常节奏——日常企业微信即时点赞、周例会『闪电奖』、月度『王者擂台』业绩龙虎榜、季度奥斯卡式颁奖典礼（走红毯+奖杯）。配合总裁共进午餐/创新实验室冠名权等荣誉性奖励，重大获奖信息官网+行业媒体发布增强社会认可。",
         how="借鉴：用『日-周-月-季』四级节奏把颁奖典礼的庄重感日常化，避免一年一次认可断层；管理层日常即可通过轻量认可维持热度，季度盛典收口。",
         url="https://m.renrendoc.com/paper/449804869.html",
         note="适用：② 上下级日常认可场景（管理者用四级节奏把颁奖日常化）"),
    dict(emoji="🪜", title="荣誉与职业发展强挂钩（晋升通道+荣誉档案持续闭环）", cat="长效机制",
         rel=["supervisor"], src="二手",
         val="荣誉激励最终落脚点是职业发展——获核心荣誉自动获得晋升资格/答辩优先推荐；荣誉积分转化为积分商城权益。实体荣誉墙/电子荣誉墙陈列照片证书事迹；线上荣誉传播矩阵（短视频/推文/直播）。荣誉档案管理形成『持续循环』而非一次性事件。",
         how="借鉴：把颁奖从『一次性仪式』升级为『荣誉→晋升→档案→持续激励』的闭环；管理者在颁奖时同步宣导荣誉与晋升/福利的强关联，放大长期激励。",
         url="https://m.renrendoc.com/paper/529537903.html",
         note="适用：② 上下级长效激励场景（荣誉与晋升/职业发展强挂钩）"),
    dict(emoji="⚖️", title="评先评优公平机制（申报→公示→异议处理+申诉通道+第三方存证）", cat="评选公平性",
         rel=["supervisor"], src="二手",
         val="流程节点全程公示（申报→初审→复审→全员公示→异议处理→最终确认）；邀请工会/员工代表民主监督；设置申诉机制由专门小组客观复议；引入数字化平台（如 i人事）全流程留痕、自动生成报表防暗箱。跨部门协作人员采用联合提名+权重计入防归属不清。",
         how="借鉴：颁奖的公信力来自『公示+申诉+留痕』三件套——在表彰制度设计阶段就内置异议处理窗口与第三方存证，避免评选争议反噬士气。",
         url="https://blog.ihr360.com/p/63131",
         note="适用：② 上下级评选治理场景（公示+申诉+第三方存证防暗箱）"),
    dict(emoji="🍽️", title="把颁奖融入日常：高管午餐会轻量表彰（Leadership Excellence Award）", cat="日常化颁奖",
         rel=["supervisor"], src="二手",
         val="Take 5 由 EVP 创设年度 Leadership Excellence Award，CEO 在总部午餐会上亲手表彰表现卓越的企业级员工；配合日常『High 5』认可（2000+人/年）、月度 Super Tech、Presidents Club（最佳经理携家属度假）。认可从盛典延伸到日常轻量场景。",
         how="借鉴：高管不必只在年度盛典颁奖——把颁奖下沉到午餐会/日常轻量场景，由高管亲自颁发，拉近与获奖员工距离、维持认可热度。",
         url="https://www.drivenbrands.com/news/take-5-oil-change-launches-leadership-excellence-award",
         note="适用：② 上下级日常轻量颁奖场景（高管午餐会亲手表彰）"),
]

# ---- balanced render template ----
def render_card(c):
    rel_badge = ""
    if "exec" in c["rel"]:
        rel_badge += '<span class="badge r3">高管间</span>'
    if "supervisor" in c["rel"]:
        rel_badge += '<span class="badge r2">上下级</span>'
    src_cls = "b1" if c["src"] == "一手" else "b2"
    disp = c["url"].split("//", 1)[-1]
    return ('<div class="hl">\n'
            '  <div class="top"><span class="emoji">%s</span><h3>%s</h3>'
            '<span class="cat">%s</span>%s<span class="badge %s">%s</span></div>\n'
            '  <p class="val">%s</p>\n'
            '  <details class="exec"><summary>怎么做</summary><div class="inner">%s</div></details>\n'
            '  <div class="src">🔗 <a href="%s" target="_blank">%s</a></div>\n'
            '  <div class="note">%s</div>\n'
            '</div>' % (c["emoji"], c["title"], c["cat"], rel_badge, src_cls, c["src"],
                        c["val"], c["how"], c["url"], disp, c["note"]))

exec_all = [render_card(c) for c in existing if "exec" in c["rel"]] + [render_card(c) for c in new_cards if "exec" in c["rel"]]
sup_all  = [render_card(c) for c in existing if "supervisor" in c["rel"] and "exec" not in c["rel"]] + [render_card(c) for c in new_cards if "supervisor" in c["rel"] and "exec" not in c["rel"]]
# NOTE: exec_all (line above) already includes mixed cards (those with both exec+supervisor badges),
# placed in sec3 per convention. Do NOT re-append — that double-counted them (88 instead of 69).
print("exec", len(exec_all), "sup", len(sup_all), "total", len(exec_all)+len(sup_all))

style = re.search(r"<style>.*?</style>", raw, re.S).group(0)
body_start = raw.index("<body>")
pre_end = raw.index("<!-- ============ ③")
preamble = raw[body_start:pre_end]
m = re.search(r"(<p>首次采集.*?</p>)", preamble, re.S)
preamble = preamble.replace(m.group(1), m.group(1)[:-4] + " ｜ 十一轮 enrich 2026-08-13(+5)</p>", 1)

def sec(sec_cls, tag_cls, tag_txt, desc, cards):
    out = ['  <div class="sec %s">' % sec_cls,
           '    <h2>%s 颁奖典礼 · %s</h2>' % ("③" if sec_cls=="sec3" else "②", tag_txt),
           '    <span class="tag">%s</span>' % tag_cls,
           '    <span class="desc">%s</span>' % desc,
           '  </div>', '  <div class="grid">']
    out += ["    " + c for c in cards]
    out.append('  </div>')
    return "\n".join(out)

body = [preamble.rstrip(), "",
        sec("sec3", "高管间", "领导↔领导（exec）", "商务化 · 战略/治理荣誉信号", exec_all), "",
        sec("sec2", "上下级", "领导↔员工（supervisor）", "尊重 · 建信任不越界", sup_all), "",
        '</div>',
        '  <footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>',
        '</body>', '</html>']
new_html = ("<!DOCTYPE html>\n<html lang=\"zh-CN\">\n<head>\n<meta charset=\"UTF-8\">\n"
           "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
           "<title>颁奖典礼 · 知识采集卡片墙</title>\n" + style + "\n</head>\n" + "\n".join(body) + "\n")
assert new_html.count('<div class="hl">') == len(exec_all)+len(sup_all)
tmp = HTML + ".tmp"; open(tmp, "w", encoding="utf-8").write(new_html); os.replace(tmp, HTML)
print("SUMMARY WALL written, hl:", new_html.count('<div class="hl">'),
      "divbal", new_html.count("<div")-new_html.count("</div>"),
      "footer", new_html.count("本页由 yitong"))

# ---- increment page ----
new_exec = [render_card(c) for c in new_cards if "exec" in c["rel"]]
new_sup  = [render_card(c) for c in new_cards if "supervisor" in c["rel"]]
def inc_sec(title, cards):
    if not cards: return ""
    return ('  <div class="sec %s">\n    <h2>%s</h2>\n    <span class="tag">%s</span>\n  </div>\n'
            '  <div class="grid">\n%s\n  </div>' % (
            "sec3" if "exec" in title else "sec2", title,
            "高管间" if "exec" in title else "上下级", "\n".join("    "+c for c in cards)))
inc = ("<!DOCTYPE html>\n<html lang=\"zh-CN\">\n<head>\n<meta charset=\"UTF-8\">\n"
       "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
       "<title>颁奖典礼 · 本轮新增卡片（+5）</title>\n" + style + "\n</head>\n<body>\n<div class=\"wrap\">\n"
       f'<p style="margin:0 0 16px"><a href="{WALL_URL}" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">🏆 返回累计卡片墙 →</a> '
       f'<a href="{RUNS_URL}" style="display:inline-block;background:#e6f7ff;color:#00b8d9;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;margin-left:8px;">📑 分页独立页 →</a></p>\n'
       '  <div class="hero">\n    <h1>🏆 颁奖典礼 · 本轮新增卡片（+5）</h1>\n'
       '    <p>轮次：十一轮 enrich ｜ 运行日期 2026-08-13 ｜ 仅 ②上下级 / ③高管间（已剔除平级/朋友向）</p>\n'
       '    <div class="relbar"><span>② 领导↔员工（上下级，supervisor）</span><span>③ 领导↔领导（高管间，exec）</span></div>\n  </div>\n'
       + inc_sec("③ 高管间（1）", new_exec) + "\n" + inc_sec("② 上下级（4）", new_sup) + "\n"
       '</div>\n  <footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>\n</body>\n</html>\n')
inc_path = os.path.join(BASE, "award-%s.html" % RUN_DATE)
open(inc_path, "w", encoding="utf-8").write(inc)
print("INCREMENT bytes:", os.path.getsize(inc_path), "divbal", inc.count("<div")-inc.count("</div>"))

# ---- index.json (idempotent) ----
def norm(t): return re.sub(r"[\s·，。、,.\u3000]+", "", t)
entries = [
    {"title":c["title"],"normKey":norm(c["title"]),"url":c["url"],"sourceType":"primary" if c["src"]=="一手" else "secondary","relation":"+".join(c["rel"]),"summary":c["val"][:110]}
    for c in new_cards]
data = json.load(open(INDEX, encoding="utf-8"))
eurls = {e.get("url") for e in data}; enorms = {e.get("normKey") for e in data}
added = 0
for e in entries:
    if e["url"] in eurls or e["normKey"] in enorms: continue
    data.append(e); added += 1; eurls.add(e["url"]); enorms.add(e["normKey"])
tmpj = INDEX + ".tmp"; json.dump(data, open(tmpj,"w",encoding="utf-8"), ensure_ascii=False, indent=2); os.replace(tmpj, INDEX)
print("INDEX added:", added, "total:", len(data))
print("OK")
