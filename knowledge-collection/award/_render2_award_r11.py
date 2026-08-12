# -*- coding: utf-8 -*-
import re, os, json
from html.parser import HTMLParser

BASE = "c:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection/award"
MIRROR = "c:/Users/v_yitcai/WorkBuddy/20260728154244/handoff-repo/knowledge-collection/award/award.html"
HTML = os.path.join(BASE, "award.html")
INDEX = "c:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection/index.json"
RUN_DATE = "20260813"
WALL_URL = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/award.html"
RUNS_URL = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/runs/index.html"

# start from clean mirror
import shutil
shutil.copyfile(MIRROR, HTML)

raw = open(HTML, encoding="utf-8").read()

# ---- robust extraction: cards are flat siblings, split by opener/closer ----
def extract_cards(s):
    opens = [m.start() for m in re.finditer(r'<div class="hl">', s)]
    closes = [m.start() for m in re.finditer(r'</div>', s)]
    blocks = []
    for idx, o in enumerate(opens):
        nxt = opens[idx + 1] if idx + 1 < len(opens) else len(s)
        mc = max(c for c in closes if c < nxt)   # card's own closing </div>
        blocks.append(s[o:mc + 6])
    return blocks

existing = extract_cards(raw)

def title_of(b):
    m = re.search(r"<h3>(.*?)</h3>", b, re.S)
    return m.group(1).strip() if m else "?"

# dedupe by title (keep first)
seen = {}
dedup = []
for b in existing:
    t = title_of(b)
    if t in seen:
        continue
    seen[t] = True
    dedup.append(b)
existing = dedup
print("existing unique cards:", len(existing))
assert len(existing) == 64, "expected 64 existing cards, got %d" % len(existing)

# classify
exec_cards = [b for b in existing if 'class="badge r3"' in b]
sup_cards  = [b for b in existing if 'class="badge r3"' not in b]
print("exec", len(exec_cards), "sup", len(sup_cards))

# ---- style + preamble (hero) ----
style = re.search(r"<style>.*?</style>", raw, re.S).group(0)
body_start = raw.index("<body>")
# find the hero-end: after relbar's closing div and hero's closing div but before first card
# locate first occurrence of the original cards section by searching for first '<div class="hl">' in raw
first_hl = raw.index('<div class="hl">')
# preamble = from <body> to just before first '<div class="hl">' (this includes nav + hero, clean)
preamble = raw[body_start:first_hl]
# update hero <p>
m = re.search(r"(<p>首次采集.*?</p>)", preamble, re.S)
old_p = m.group(1)
new_p = old_p[:-4] + " ｜ 十一轮 enrich 2026-08-13(+5)</p>"
preamble = preamble.replace(old_p, new_p, 1)

# ---- new cards ----
def card(emoji, title, cat, rel, src, val, how, url, note):
    rel_badge = ""
    if "exec" in rel:
        rel_badge += '<span class="badge r3">高管间</span>'
    if "supervisor" in rel:
        rel_badge += '<span class="badge r2">上下级</span>'
    src_cls = "b1" if src == "一手" else "b2"
    disp = url.split("//", 1)[-1]
    return ('<div class="hl">\n'
            '  <div class="top"><span class="emoji">%s</span><h3>%s</h3>'
            '<span class="cat">%s</span>%s<span class="badge %s">%s</span></div>\n'
            '  <p class="val">%s</p>\n'
            '  <details class="exec"><summary>怎么做</summary><div class="inner">%s</div></details>\n'
            '  <div class="src">🔗 <a href="%s" target="_blank">%s</a></div>\n'
            '  <div class="note">%s</div>\n'
            '</div>' % (emoji, title, cat, rel_badge, src_cls, src, val, how, url, disp, note))

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

new_exec = [c for c in new_cards if 'class="badge r3"' in c]
new_sup  = [c for c in new_cards if 'class="badge r3"' not in c]

def sec(sec_cls, tag_cls, tag_txt, desc, cards):
    out = ['  <div class="sec %s">' % sec_cls,
           '    <h2>%s 颁奖典礼 · %s</h2>' % ("③" if sec_cls=="sec3" else "②", tag_txt),
           '    <span class="tag">%s</span>' % tag_cls,
           '    <span class="desc">%s</span>' % desc,
           '  </div>',
           '  <div class="grid">']
    out += ["    " + c for c in cards]
    out.append('  </div>')
    return "\n".join(out)

body = [preamble.rstrip(), "",
        sec("sec3", "高管间", "领导↔领导（exec）", "商务化 · 战略/治理荣誉信号", exec_cards + new_exec), "",
        sec("sec2", "上下级", "领导↔员工（supervisor）", "尊重 · 建信任不越界", sup_cards + new_sup), "",
        '</div>',
        '  <footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>',
        '</body>', '</html>']
new_html = ("<!DOCTYPE html>\n<html lang=\"zh-CN\">\n<head>\n<meta charset=\"UTF-8\">\n"
           "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
           "<title>颁奖典礼 · 知识采集卡片墙</title>\n" + style + "\n</head>\n" + "\n".join(body) + "\n")

tmp = HTML + ".tmp"
open(tmp, "w", encoding="utf-8").write(new_html)
os.replace(tmp, HTML)

total = len(existing) + len(new_cards)
assert total == new_html.count('<div class="hl">'), (total, new_html.count('<div class="hl">'))
print("SUMMARY WALL:", total, "cards (exec", len(exec_cards)+len(new_exec), "/ sup", len(sup_cards)+len(new_sup), ")")

# increment page
def inc_sec(title, cards):
    if not cards: return ""
    return ('  <div class="sec %s">\n    <h2>%s</h2>\n    <span class="tag">%s</span>\n  </div>\n'
            '  <div class="grid">\n%s\n  </div>' % (
            "sec3" if "exec" in title else "sec2", title,
            "高管间" if "exec" in title else "上下级",
            "\n".join("    "+c for c in cards)))

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
print("INCREMENT bytes:", os.path.getsize(inc_path))

# index.json (idempotent)
def norm(t): return re.sub(r"[\s·，。、,.\u3000]+", "", t)
entries = [
    {"title":"复星国际·外部治理奖项与ESG绩效纳入高管考核","normKey":norm("复星国际·外部治理奖项与ESG绩效纳入高管考核"),"url":"https://en.fosun.com/content/details46_5420.html","sourceType":"primary","relation":"exec","summary":"复星国际获亚洲卓越奖（双CEO获Asia's Best CEO），关键机制将ESG绩效纳入执行董事考核；外部治理奖项成高管荣誉信号。"},
    {"title":"日-周-月-季四级认可机制（日常点赞→奥斯卡式年会颁奖）","normKey":norm("日-周-月-季四级认可机制（日常点赞→奥斯卡式年会颁奖）"),"url":"https://m.renrendoc.com/paper/449804869.html","sourceType":"secondary","relation":"supervisor","summary":"把认可拆成日点赞/周闪电奖/月擂台/季奥斯卡式颁奖的日常节奏，配合总裁午餐等荣誉性奖励，避免一年一次认可断层。"},
    {"title":"荣誉与职业发展强挂钩（晋升通道+荣誉档案持续闭环）","normKey":norm("荣誉与职业发展强挂钩（晋升通道+荣誉档案持续闭环）"),"url":"https://m.renrendoc.com/paper/529537903.html","sourceType":"secondary","relation":"supervisor","summary":"核心荣誉自动获晋升资格/答辩优先；荣誉积分兑商城；实体+线上荣誉墙；荣誉档案形成持续激励闭环而非一次性事件。"},
    {"title":"评先评优公平机制（申报→公示→异议处理+申诉通道+第三方存证）","normKey":norm("评先评优公平机制（申报→公示→异议处理+申诉通道+第三方存证）"),"url":"https://blog.ihr360.com/p/63131","sourceType":"secondary","relation":"supervisor","summary":"流程全程公示+工会/员工代表监督+申诉复议+数字化平台留痕防暗箱；跨部门联合提名权重计入防归属不清。"},
    {"title":"把颁奖融入日常：高管午餐会轻量表彰（Leadership Excellence Award）","normKey":norm("把颁奖融入日常：高管午餐会轻量表彰（Leadership Excellence Award）"),"url":"https://www.drivenbrands.com/news/take-5-oil-change-launches-leadership-excellence-award","sourceType":"secondary","relation":"supervisor","summary":"Take 5 由EVP创年度奖，CEO在午餐会亲手表彰企业级员工；认可从盛典下沉到日常轻量场景维持热度。"},
]
data = json.load(open(INDEX, encoding="utf-8"))
eurls = {e.get("url") for e in data}; enorms = {e.get("normKey") for e in data}
added = 0
for e in entries:
    if e["url"] in eurls or e["normKey"] in enorms:
        continue
    data.append(e); added += 1; eurls.add(e["url"]); enorms.add(e["normKey"])
tmpj = INDEX + ".tmp"
json.dump(data, open(tmpj, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
os.replace(tmpj, INDEX)
print("INDEX added:", added, "total:", len(data))
print("OK")
