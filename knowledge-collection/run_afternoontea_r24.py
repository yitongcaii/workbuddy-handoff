# -*- coding: utf-8 -*-
"""下午茶研讨 二十四轮补采 (2026-08-22 同日二次 R24) — 渲染增量 + 追加进累计墙 + 更新 index.json + Obsidian + 乐享上传
仅 ②上下级 / ③高管间，0 peer。本论增量页 afternoontea-20260822b.html（避开与 R23 afternoontea-20260822.html 同名）。"""
import json, os, re, urllib.request, urllib.error

BASE = os.path.dirname(os.path.abspath(__file__))
AT_DIR = os.path.join(BASE, "afternoontea")
CUM = os.path.join(AT_DIR, "afternoontea.html")
IDX = os.path.join(BASE, "index.json")
DATE = "20260822"
RUN_NAME = "afternoontea-20260822b.html"
RUN_PATH = os.path.join(AT_DIR, RUN_NAME)

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---- 本轮新增卡（仅 ②上下级 / ③高管间，0 peer；7张全 NEW，URL 均未命中 index/wall）----
# 关系档：②上下级 6 张（4 一手 + 2 二手）+ ③高管间 1 张（二手）
CARDS = [
    {
        "emoji": "\U0001F91D",
        "title": "盐城港集团「总经理接待日」·心声有回声",
        "cat": "总经理接待日",
        "rel": "r2", "rel_text": "上下级",
        "src": "b1", "src_text": "一手",
        "val": "盐城港集团航运集团常态化开展「总经理接待日」，在领导与职工间搭建发现问题、沟通问题、解决问题的桥梁。主要负责人深入了解员工思想动态与工作生活现状，耐心倾听职工反映的问题、详细记录需求，对员工在集团高质量发展、五新示范港建设等方面的意见建议逐一解答。接待后即时专题研究、协调相关部门解决，并要求限时反馈，形成「及时了解·及时解决·及时反馈」闭环。自设立以来帮助解决实际困难11次、采纳合理化建议8项；下一步建立常态化长效化机制。",
        "how": "办总经理接待日，学盐城港「面对面+闭环反馈」：主要负责人亲自听、现场记、接后立刻开专题会协调、限时回职工；用「件件有着落、事事有回音」把关爱落到实处。关键是接待不是终点、解决才是，避免「谈完没了」。",
        "url": "https://www.jsycport.com/m/926/2024-11-18/content-20944.html",
        "note": "适用：② 集团主要负责人 × 一线/机关职工（企业官方一手案例；总经理接待日 + 闭环反馈机制，可作常态化沟通范本）。",
    },
    {
        "emoji": "\U0001F5D3\uFE0F",
        "title": "中国诚通「书记接待日」·建账督办十五五建言",
        "cat": "书记接待日",
        "rel": "r2", "rel_text": "上下 级",
        "src": "b1", "src_text": "一手",
        "val": "中国诚通党委书记、董事长奚正平主持首次「书记接待日」，与基层干部职工面对面、心贴心交流，听取关于集团改革发展、党的建设的宝贵意见。强调推动接待活动常态化长效化，健全制度、细化清单，对意见建议逐一建台账、研究分析、逐项督办，确保「件件有回音、事事有着落」；以基层调研、书记信箱、书记接待日为抓手，增进双向理解互信，为「十五五」高质量发展汇聚合力。",
        "how": "办书记接待日，学中国诚通「首接即建账+逐项督办+闭环回音」：党委书记/董事长亲自坐班听基层，现场记、会后建台账、明确责任人与时限；用书记信箱等日常渠道延长触点。核心是「接待制度化、问题清单化、反馈透明化」。",
        "url": "http://www.cctm.cn/cctm/2025-12/31/article_2025123109203792130.html",
        "note": "适用：② 央企党委书记/董事长 × 基层干部职工（官方一手；书记接待日制度化 + 十五五建言闭环，可作国企民主管理范本）。",
    },
    {
        "emoji": "\U0001F375",
        "title": "悦达汽车「党委书记、工会主席接待日」座谈会",
        "cat": "党委工会接待日",
        "rel": "r2", "rel_text": "上下级",
        "src": "b1", "src_text": "一手",
        "val": "悦达汽车集团召开首次「党委书记、工会主席接待日」座谈会，党委书记成荣春、工会主席王丽萍出席。职工代表围绕劳动保护、工资待遇、生活福利等急难愁盼与公司发展提意见建议，领导认真倾听、逐一回应，可立行立改的现场部署。强调完善常态化机制、建问题台账、明责任分工与整改时限，确保「件件有着落、事事有回音」；后续内部平台定期公示整改进展、接受监督、并对职工回访，形成「收集—办理—反馈—提升」闭环。",
        "how": "办党委+工会联合接待日，学悦达「双带头人坐班+台账+公示回访」：一把手与工会主席同场听，现场拍板立改项；用内部平台公示整改进展+回访形成闭环。适合把「接待日」从一次性活动升级为信任资产。",
        "url": "https://www.ydautogroup.com/info/1297",
        "note": "适用：② 党委书记/工会主席 × 职工代表（企业官网一手；党委工会双接待 + 公示回访闭环，可作民主管理范本）。",
    },
    {
        "emoji": "\U0001F309",
        "title": "大唐甘肃「书记接待日」·开门教育连心桥",
        "cat": "书记接待日",
        "rel": "r2", "rel_text": "上下级",
        "src": "b1", "src_text": "一手",
        "val": "大唐甘肃公司各级党组织开展「书记接待日」，与「我为群众办实事」互融互促，打通联系基层、服务职工的「最后一公里」。党组织书记通过现场面谈、视频连线、电话交流等形式接待职工来访，倾听对生产经营、日常生活的意见建议，回应关心关切。碧口水电厂累计接待职工40余人次、收集诉求49条，系统梳理分类、明确责任人与解决时限；景泰党支部「面对面听心声、实打实解难题」，当场能答的即时回复，需协调的建台账说明原因与计划，实现「职工有诉求、组织有回应」。",
        "how": "办书记接待日，学大唐甘肃「多渠道接待+诉求分类建账+即时回复/限时台账」：现场/视频/电话多通道降低参与门槛；对诉求按「即答/建账」分流，明确责任人与时限。把接待做成「连心桥」而非作秀，关键在回应速度与透明度。",
        "url": "https://gs.china-cdt.com/cdtgs/xwzx/jcdt/2025/10/I1427989623405019136.html",
        "note": "适用：② 国企党组织书记 × 基层职工（官网一手；书记接待日 + 开门教育，可作党群沟通范本）。",
    },
    {
        "emoji": "\U0001F4CB",
        "title": "索普集团职工恳谈会·30年闭环制度",
        "cat": "职工恳谈会",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "索普集团自1994年探索召开与职工代表面对面的恳谈会，至今30余年。近5年经职工提出、集团落实项目达120个，职工满意度持续95%以上。恳谈会一般安排在每年职代会期间半天，由董事长、总经理现场接受职工代表提问，领导班子、职能部门负责人、基层分工会主席列席；职工代表按不少于职工6%选举产生，覆盖经营、技术、安全、生产一线。形成「议题征集—双向交流—跟踪落实—成果反馈」四环节闭环；如遇重大事项临时召开。会前工会广泛收集意见，会上职工代表现场提问、主要领导现场答复，会后工会整理汇总提请职能部门进一步答复。",
        "how": "办职工恳谈会，学索普「30年制度化+四环节闭环+回避式直面」：董事长/总经理现场接问、能答现场答、不能答交工会建账督办；代表选举覆盖一线、回避部门负责人保坦诚。把恳谈会从「座谈会」升级为「民主管理闭环制度」。",
        "url": "https://news.workercn.cn/c/2025-10-18/8633607.shtml",
        "note": "适用：② 董事长/总经理 × 职工代表（工人日报深度报道；30年恳谈会制度化 + 闭环，可作职代会配套范本）。",
    },
    {
        "emoji": "\U0001F3ED",
        "title": "亚太森博「厂长沟通会」·季度直面一线",
        "cat": "厂长沟通会",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "亚太森博日照纸板事业部举办首场「纸板厂长沟通会」，工厂总经理徐永祥与来自多个部门的18名员工在轻松开放氛围中面对面交流。员工代表就工作环境、考勤加班、福利补贴、车证班车等提意见建议，徐永祥认真聆听、现场解答记录；能立即解决的当场给方案与时限，需调研协调的纳入跟进清单，由人力资源部一周内回应，确保「事事有回音、件件有着落」。活动旨在搭建纸板员工与管理层直接对话的长效机制，后续每季度定期举行。",
        "how": "办厂长/总经理沟通会，学亚太森博「季度固定+轻松氛围+一周内回应」：一把手与一线代表小范围直面，现场拍板立改项、其余建跟进清单并限时回；以「轻松开放」降层级感。适合制造业把管理层沟通做成常态化固定动作。",
        "url": "https://new.qq.com/rain/a/20251020A042OQ00?refer=cp_1009",
        "note": "适用：② 工厂总经理 × 一线员工（腾讯新闻转载企业稿；厂长沟通会季度化 + 一周回应闭环，可作制造业范本）。",
    },
    {
        "emoji": "\U0001F465",
        "title": "CEO 同侪顾问小组深度指南·孤独决策破局",
        "cat": "高管同侪",
        "rel": "r3", "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "CEO 同侪顾问小组（peer advisory group）是6-12位非竞争 CEO 在绝对保密下定期聚会，压力测试「公司内部无人可核」的决策。2024 HBR 研究107位高管：25%频繁孤独、55%中度孤独，源于决策无人可坦诚权衡。主流形态：Vistage（195 创建，付费主席主持，12-16人/月/全天）、EO Forum（1987，成员主持，Gestalt 协议禁建议只分享亲身经历）、Helix（2024，无主席、百席上限）。价值依次：决策速度→问责→模式获取；选人重「同阶段」而非名气；失败信号＝只更新无进展、舒适却不改变。区别于董事会（治理权）与顾问（付费有立场）。",
        "how": "运营高管同侪圈，参考 shaanrais 指南：小范围（6-12人）+ 绝对保密 + 定时聚 +「带真实决策、先问后荐、呈现者最后说」；用「亲身经历」替代空泛建议（EO 禁建议协议反直觉但有效）。把同侪对话当「没人能给你的董事会」，慎选人、守纪律，避免变推销场。区别于 R22 已收的 Vistage/EO/Helix 官方页，本卡补「为何孤独+HBR数据+选人陷阱」。",
        "url": "https://shaanrais.com/feeds/blog/ceo-peer-advisory-groups",
        "note": "适用：③ 创始人/CEO × 同侪高管（二手深度指南；决策孤独+HBR数据+选人陷阱，与 R22 Vistage/EO/Helix 官方页互补，非重复）。",
    },
]

def card_html(c, indent=4):
    sp = " " * indent
    sp2 = " " * (indent + 2)
    rel_badge = '<span class="badge {0}">{1}</span>'.format(c["rel"], c["rel_text"])
    src_badge = '<span class="badge {0}">{1}</span>'.format(c["src"], c["src_text"])
    return (
        sp + '<div class="hl">\n'
        + sp2 + '<div class="top"><span class="emoji">' + esc(c["emoji"]) + '</span>'
        + '<h3>' + esc(c["title"]) + '</h3><span class="cat">' + esc(c["cat"]) + '</span>'
        + rel_badge + src_badge + '</div>\n'
        + sp2 + '<p class="val">' + esc(c["val"]) + '</p>\n'
        + sp2 + '<details class="exec"><summary>怎么做</summary><div class="inner">' + esc(c["how"]) + '</div></details>\n'
        + sp2 + '<div class="src">\U0001F517 <a href="' + esc(c["url"]) + '" target="_blank">' + esc(c["url"]) + '</a></div>\n'
        + sp2 + '<div class="note">' + esc(c["note"]) + '</div>\n'
        + sp + '</div>\n'
    )

def find_grid_close(h, sec_start):
    gi = h.find('<div class="grid">', sec_start)
    assert gi != -1, "grid not found"
    depth = 0
    i = gi + len('<div class="grid">')
    while i < len(h):
        if h.startswith('<div', i):
            depth += 1
            i = h.find('>', i) + 1
        elif h.startswith('</div>', i):
            if depth == 0:
                return i
            depth -= 1
            i += 5
        else:
            i += 1
    raise RuntimeError("unbalanced")

STYLE = """.wrap{max-width:1080px;margin:0 auto;}
.hero{background:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);border-radius:22px;padding:26px 30px;color:#fff;box-shadow:0 14px 40px rgba(108,92,231,.25);margin-bottom:22px;}
.hero h1{font-size:24px;font-weight:800;letter-spacing:1px;margin-bottom:6px;}
.hero p{font-size:13px;opacity:.95;}
.relbar{display:flex;gap:10px;flex-wrap:wrap;margin-top:12px;}
.relbar span{background:rgba(255,255,255,.2);border-radius:20px;padding:5px 14px;font-size:13px;font-weight:600;}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;}
.hl{background:#fff;border-radius:18px;padding:18px 18px 16px;border-top:4px solid #6c5ce7;box-shadow:0 10px 32px rgba(108,92,231,.10);display:flex;flex-direction:column;gap:9px;}
.top{display:flex;align-items:center;gap:8px;flex-wrap:wrap;}
.emoji{font-size:22px;}
.hl h3{font-size:16px;font-weight:700;flex:1;min-width:120px;}
.cat{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:600;background:#eef0ff;color:#6c5ce7;}
.badge{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:700;}
.b2{background:#fff1e6;color:#c0651a;}
.b1{background:#e6f9ed;color:#1a9e5a;}
.r2{background:#fff3e0;color:#c0651a;}
.r3{background:#f3e8ff;color:#7b2cbf;}
.val{font-size:13.5px;color:#5b6478;}
.exec{margin-top:2px;border-top:1px dashed #e2e8f0;padding-top:8px;}
.exec summary{cursor:pointer;font-size:13px;font-weight:600;color:#6c5ce7;}
.exec .inner{font-size:13px;color:#5b6478;margin-top:6px;padding-left:4px;}
.src{font-size:12px;word-break:break-all;}
.src a{color:#00b8d9;text-decoration:none;}
.note{font-size:12px;color:#94a3b8;border-left:3px solid #e2e8f0;padding-left:8px;}
footer{text-align:center;padding:24px;color:#94a3b8;font-size:13px;border-top:1px solid #e2e8f0;margin-top:40px;}
:root{--accent:#6c5ce7;--accent2:#00b8d9;}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:linear-gradient(135deg,#eef1ff 0%,#e6f7ff 100%);color:#1f2430;padding:28px 18px;line-height:1.6;}"""

WALL_URL = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/afternoontea/afternoontea.html"
PORTAL_URL = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/index.html"

def build_incremental():
    n_r3 = sum(1 for c in CARDS if c["rel"] == "r3")
    n_r2 = sum(1 for c in CARDS if c["rel"] == "r2")
    cards_block = "".join(card_html(c) for c in CARDS)
    html = (
        '<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '<title>\u4e0b\u5348\u8336\u7814\u8ba8 \u00b7 \u4e8c\u5341\u56db\u8f6e\u589e\u91cf\u5361\u7247\uff082026-08-22\uff09</title>\n'
        '<style>\n' + STYLE + '\n</style>\n</head><body>\n<div class="wrap">\n'
        '<p style="margin:0 0 16px"><a href="' + WALL_URL + '" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">\U0001F375 \u8fd4\u56de\u4e0b\u5348\u8336\u7d2f\u8ba1\u5361\u7247\u5899 \u2192</a> &nbsp; '
        '<a href="' + PORTAL_URL + '" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">\U0001F4DA \u8fd4\u56de\u77e5\u8bc6\u5e93\u95e8\u6237 \u2192</a></p>\n'
        '  <div class="hero">\n'
        '    <h1>\U0001F375 \u4e0b\u5348\u8336\u7814\u8ba8 \u00b7 \u4e8c\u5341\u56db\u8f6e\u589e\u91cf\u5361\u7247\uff082026-08-22\uff09</h1>\n'
        '    <p>\u672c\u8f6e\u65b0\u589e 7 \u5f20\uff08\u901a\u8fc7\u516d\u7ef4\u8bc4\u4f30\uff0c\u5254\u9664\u5e73\u7ea7/\u670b\u53cb\u5411\uff0c\u4ec5 ②\u4e0a\u4e0b\u7ea7 / ③\u9ad8\u7ba1\u95f4\uff09\uff1b\u5173\u7cfb\u6863\uff1a③\u9ad8\u7ba1\u95f4 1 \u5f20 + ②\u4e0a\u4e0b\u7ea7 6 \u5f20\u3002</p>\n'
        '    <div class="relbar">\n'
        '      <span>② \u9886\u5bfc\u2194\u5458\u5de5\uff08\u4e0a\u4e0b\u7ea7\uff0csupervisor\uff09</span>\n'
        '      <span>③ \u9886\u5bfc\u2194\u9886\u5bfc\uff08\u9ad8\u7ba1\u95f4\uff0cexec\uff09</span>\n'
        '    </  </div>\n'  # placeholder to avoid accidental close error
    )
    # fix the relbar close (mistranscribed above)
    html = html.replace('    </  </div>\n', '    </div>\n')
    html = html + (
        '  </div>\n'
        '  <div class="grid">\n' + cards_block + '  </div>\n'
        '<footer>\U0001F4CC \u672c\u9875\u7531 yitong \u6c89\u6dc0\u6574\u7406 \u00b7 \u6587\u5316\u6d3b\u52a8\u77e5\u8bc6\u5e93</footer>\n'
        '</div>\n</body>\n</html>\n'
    )
    open(RUN_PATH, "w", encoding="utf-8").write(html)
    return len(html.encode("utf-8"))

# ---- 1) 增量页 ----
inc_bytes = build_incremental()
print("增量页已写出:", RUN_PATH, inc_bytes, "B")

# ---- 2) 墙注入 ----
html = open(CUM, encoding="utf-8").read()
before = html.count('<div class="hl">')
cards_sec3 = [c for c in CARDS if c["rel"] == "r3"]
cards_sec2 = [c for c in CARDS if c["rel"] == "r2"]
i3 = html.find('class="sec sec3"')
close3 = find_grid_close(html, i3)
html = html[:close3] + "".join(card_html(c) for c in cards_sec3) + html[close3:]
i2 = html.find('class="sec sec2"')
close2 = find_grid_close(html, i2)
html = html[:close2] + "".join(card_html(c) for c in cards_sec2) + html[close2:]
# hero
hero_old = "\u4e8c\u5341\u4e09\u8f6e enrich 2026-08-22(+6)</p>"
hero_new = "\u4e8c\u5341\u4e09\u8f6e enrich 2026-08-22(+6) \uff5c \u4e8c\u5341\u56db\u8f6e enrich 2026-08-22(+7)</p>"
assert hero_old in html, "hero marker not found"
html = html.replace(hero_old, hero_new, 1)
# recount
def recount(tagcls):
    s = html.find('class="' + tagcls + '"')
    e = html.find('class="sec', s + 10)
    return html[s:e].count('<div class="hl">')
r2n = recount('sec sec2'); r3n = recount('sec sec3')
html = re.sub(r'(<div class="sec sec2">.*?<span class="tag">)\d+( \u5361</span>)',
              lambda m: m.group(1) + str(r2n) + m.group(2), html, count=1, flags=re.S)
html = re.sub(r'(<div class="sec sec3">.*?<span class="tag">)\d+( \u5361</span>)',
              lambda m: m.group(1) + str(r3n) + m.group(2), html, count=1, flags=re.S)
open(CUM, "w", encoding="utf-8").write(html)
after = html.count('<div class="hl">')
r2b = html.count('badge r2'); r3b = html.count('badge r3')
b1b = html.count('badge b1'); b2b = html.count('badge b2')
footer_ok = "\U0001F4CC \u672c\u9875\u7531 yitong" in html
print("累计墙卡片数:", after, "(+", after - before, ") | r2:", r2b, "r3:", r3b, "| b1:", b1b, "b2:", b2b, "| footer:", footer_ok)
print("sec2 tag:", r2n, "sec3 tag:", r3n)

# ---- 3) index.json ----
def normkey(t):
    out = []
    for ch in t.lower():
        if ch.isalnum() or "一" <= ch <= "鿿":
            out.append(ch)
    return "".join(out)

data = json.load(open(IDX, encoding="utf-8"))
existing_urls = {e.get("url", "").lower().rstrip("/") for e in data}
added = 0
for c in CARDS:
    u = c["url"].lower().rstrip("/")
    if u in existing_urls:
        print("SKIP dup url:", u); continue
    entry = {
        "title": c["title"],
        "normKey": normkey(c["title"]),
        "url": c["url"],
        "sourceType": "secondary" if c["src"] == "b2" else "primary",
        "relation": "exec" if c["rel"] == "r3" else "supervisor",
        "summary": c["cat"] + "：" + c["val"][:60],
        "topic": "afternoontea",
    }
    data.append(entry); added += 1; existing_urls.add(u)
print("index.json 新增:", added, "-> 现", len(data), "条")
json.dump(data, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

# ---- 4) Obsidian 笔记 ----
VAULT = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库"
NOTE = os.path.join(VAULT, "素材", "afternoontea", "下午茶研讨-知识卡汇总.md")
t = open(NOTE, encoding="utf-8").read()
assert "（151 卡 · 上下级/高管间）" in t
t = t.replace("（151 卡 · 上下级/高管间）", "（158 卡 · 上下级/高管间）", 1)
assert "\u7d2f\u8ba1 151 \u5361\uff08③\u9ad8\u7ba1\u95f4 58 / ②\u4e0a\u4e0b\u7ea7 97\uff0c\u542b 4 \u5f20\u8de8\u6863\u53cc\u6807\uff1b\u4e00\u624b 47 + \u4e8c\u624b 104\uff09" in t
t = t.replace("\u7d2f\u8ba1 151 \u5361\uff08③\u9ad8\u7ba1\u95f4 58 / ②\u4e0a\u4e0b\u7ea7 97\uff0c\u542b 4 \u5f20\u8de8\u6863\u53cc\u6807\uff1b\u4e00\u624b 47 + \u4e8c\u624b 104\uff09",
              "\u7d2f\u8ba1 158 \u5361\uff08③\u9ad8\u7ba1\u95f4 59 / ②\u4e0a\u4e0b\u7ea7 103\uff0c\u542b 4 \u5f20\u8de8\u6863\u53cc\u6807\uff1b\u4e00\u624b 51 + \u4e8c\u624b 107\uff09", 1)
# timeline blockquote
tl_old = "\u4e8c\u5341\u4e09\u8f6e enrich 2026-08-22(+6)"
tl_new = "\u4e8c\u5341\u4e09\u8f6e enrich 2026-08-22(+6) \uff5c \u4e8c\u5341\u56db\u8f6e enrich 2026-08-22(+7)"
assert tl_old in t
t = t.replace(tl_old, tl_new, 1)
# section headers
assert "## ③ 领导↔领导（高管间 · exec）— 56 卡" in t
t = t.replace("## ③ 领导↔领导（高管间 · exec）— 56 卡", "## ③ 领导↔领导（高管间 · exec）— 57 卡", 1)
assert "## ② 领导↔员工（上下级 · supervisor）— 93 卡" in t
t = t.replace("## ② 领导↔员工（上下级 · supervisor）— 93 卡", "## ② 领导↔员工（上下级 · supervisor）— 99 卡", 1)
# r3 rows: insert before "## ②" header, numbering continues
r3_rows = "".join(
    "| {0} | {1}（afternoontea.html） | {2} | {3} |\n".format(88 + i, esc(c["title"]), "一手" if c["src"] == "b1" else "二手", "③高管间")
    for i, c in enumerate(cards_sec3)
)
marker2 = "## ② 领导↔员工（上下级 · supervisor）— 99 卡"
assert marker2 in t
t = t.replace(marker2, r3_rows + "\n" + marker2, 1)
# r2 rows: append at end of r2 table -> before next "## 主题：" after afternoontea
sec2_head_pos = t.find("## ② 领导↔员工")
# find max r2 row number currently in the r2 table (between sec2_head_pos and next "## 主题")
seg = t[sec2_head_pos:]
next_topic = seg.find("\n## 主题：", 1)
r2_region = seg[:next_topic] if next_topic != -1 else seg
nums = [int(x) for x in re.findall(r'^\| (\d+) \|', r2_region, flags=re.M)]
max_r2 = max(nums) if nums else 0
r2_rows = "".join(
    "| {0} | {1}（afternoontea.html） | {2} | {3} |\n".format(max_r2 + 1 + i, esc(c["title"]), "一手" if c["src"] == "b1" else "二手", "②上下级")
    for i, c in enumerate(cards_sec2)
)
# insert before the next "## 主题：" following afternoontea header
apos = t.find("## 主题：下午茶研讨")
npos = t.find("## 主题：", apos + 10)
assert npos != -1
t = t[:npos] + r2_rows + "\n" + t[npos:]
# round narrative section before "## ③" header
round_section = (
    "\n## 轮次 2026-08-22（+7）\n"
    "> 二十四轮 enrich：新增 7 卡（③ 高管间 +1：CEO 同侪顾问小组深度指南·孤独决策破局（shaanrais/HBR数据）；② 上下级 +6：盐城港「总经理接待日」/ 中国诚通「书记接待日」/ 悦达汽车党委工会接待日 / 大唐甘肃「书记接待日」/ 索普集团职工恳谈会·30年闭环 / 亚太森博「厂长沟通会」）。无 peer，relation 仅取 supervisor/exec。\n"
    "> 线上预览：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/afternoontea/afternoontea.html ｜ 本轮增量页：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/afternoontea/afternoontea-20260822b.html\n"
)
marker3 = "## ③ 领导↔领导（高管间 · exec）— 57 卡"
assert marker3 in t
t = t.replace(marker3, round_section + marker3, 1)
open(NOTE, "w", encoding="utf-8").write(t)
print("Obsidian 笔记更新完成")

# ---- 5) 00-索引 ----
IDX0 = os.path.join(VAULT, "00-知识采集索引.md")
i0 = open(IDX0, encoding="utf-8").read()
# section header timeline
assert "\u4e8c\u5341\u4e09\u8f6e enrich 2026-08-22(+6)\uff09" in i0
i0 = i0.replace("\u4e8c\u5341\u4e09\u8f6e enrich 2026-08-22(+6)\uff09",
                "\u4e8c\u4e09\u8f6e enrich 2026-08-22(+6) \uff5c \u4e8c\u5341\u56db\u8f6e enrich 2026-08-22(+7)\uff09", 1)
# counts blockquote
assert "**151 卡**" in i0
i0 = i0.replace("**151 卡**", "**158 卡**", 1)
assert "\u4e00\u624b 47 + \u4e8c\u624b 104" in i0
i0 = i0.replace("\u4e00\u624b 47 + \u4e8c\u624b 104", "\u4e00\u624b 51 + \u4e8c\u624b 107", 1)
assert "\u2462\u9ad8\u7ba1\u95f4(...) 58 \u5361 / \u2461\u4e0a\u4e0b\u7ea7(...) 97 \u5361\uff08\u542b 4 \u5f20\u8de8\u6863\u53cc\u6807\uff0c\u53bb\u91cd\u540e 141\uff09" in i0
i0 = i0.replace("\u2462\u9ad8\u7ba1\u95f4(...)  * 58 \u5361 / \u2461\u4e0a\u4e0b\u7ea7(...) 97 \u5361\uff08\u542b 4 \u5f20\u8de8\u6863\u53cc\u6807\uff0c\u53bb\u91cd\u540e 141\uff09".replace("* ", ""),
              "\u2462\u9ad8\u7ba1\u95f4(...) 59 \u5361 / \u2461\u4e0a\u4e0b\u7ea7(...) 103 \u5361\uff08\u542b 4 \u5f20\u8de8\u6863\u53cc\u6807\uff0c\u53bb\u91cd\u540e 148\uff09", 1)
# fallback exact (no stray *)
i0 = i0.replace("\u2462\u9ad8\u7ba1\u95f4(...) 58 \u5361 / \u2461\u4e0a\u4e0b\u7ea7(...) 97 \u5361\uff08\u542b 4 \u5f20\u8de8\u6863\u53cc\u6807\uff0c\u53bb\u91cd\u540e 141\uff09",
              "\u2462\u9ad8\u7ba1\u95f4(...) 59 \u5361 / \u2461\u4e0a\u4e0b\u7ea7(...) 103 \u5361\uff08\u542b 4 \u5f20\u8de8\u6863\u53cc\u6807\uff0c\u53bb\u91cd\u540e 148\uff09", 1)
# append rows before next "## 主题：" after afternoontea header
apos2 = i0.find("## 主题：下午茶研讨")
npos2 = i0.find("## 主题：", apos2 + 10)
assert npos2 != -1
rows = "".join(
    "| {0}\uff08afternoontea.html\uff09 | 4 | {1} | {2} | \n".format(c["title"], "一手" if c["src"] == "b1" else "二手", "③高管间" if c["rel"] == "r3" else "②上下级")
    for c in CARDS
)
i0 = i0[:npos2] + rows + "\n" + i0[npos2:]
open(IDX0, "w",  encoding="utf-8").write(i0)
print("00-索引更新完成")

# ---- 6) 乐享上传（新建独立页文件模式）----
MCP_JSON = os.path.expanduser("~/.workbuddy/mcp.json")
LEXIANG_URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"
FOLDER = "96e0ca6a548e4202a12d43dc91b48938"
class LexiangMCP:
    def __init__(self, token):
        self.token = token; self.session = None
    def _post(self, payload, retries=2):
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(LEXIANG_URL, data=data, method="POST")
        req.add_header("Content-Type", "application/json")
        req.add_header("Accept", "application/json, text/event-stream")
        req.add_header("Authorization", self.token)
        if self.session: req.add_header("Mcp-Session-Id", self.session)
        last = None
        for _ in range(retries):
            try:
                resp = urllib.request.urlopen(req, timeout=120)
                sid = resp.headers.get("mcp-session-id")
                if sid: self.session = sid
                return self._parse(resp.read().decode("utf-8", "replace"))
            except urllib.error.HTTPError as e:
                last = "HTTP {0}: {1}".format(e.code, e.read().decode("utf-8", "replace")[:400]); continue
            except Exception as e:
                last = str(e); continue
        raise RuntimeError("POST fail: " + last)
    def _parse(self, raw):
        raw = raw.strip()
        if raw.startswith("data:"):
            raw = "\n".join(l[5:].strip() for l in raw.splitlines() if l.startswith("data:"))
        try: return json.loads(raw)
        except Exception: return json.loads(raw[raw.find("{"):])
    def initialize(self):
        return self._post({"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"wb-uploader","version":"1.0"}}})
    def initialized(self):
        try: self._post({"jsonrpc":"2.0","method":"notifications/initialized"})
        except Exception: pass
    def call(self, name, args):
        return self._post({"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":name,"arguments":args}})
    def biz(self, resp):
        res = resp.get("result")
        if not res: raise RuntimeError("no result: " + json.dumps(resp, ensure_ascii=False)[:300])
        text = ""
        for c in (res.get("content") or []):
            if c.get("type") == "text": text = c.get("text", ""); break
        try: return json.loads(text)
        except Exception: return {"_raw_text": text}
def put_bytes(url, data):
    req = urllib.request.Request(url, data=data, method="PUT")
    req.add_header("Content-Type", "text/html")
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.status
try:
    token = json.load(open(MCP_JSON, encoding="utf-8"))["mcpServers"]["lexiang"]["headers"]["Authorization"]
    mc = LexiangMCP(token); mc.initialize(); mc.initialized()
    try:
        print("whoami:", json.dumps(mc.call("whoami", {})[:0] if False else mc.call("whoami", {}), ensure_ascii=False)[:120])
    except Exception as e:
        print("whoami 跳过:", str(e)[:120])
    data_bytes = open(RUN_PATH, "rb").read()
    r = mc.call("file_apply_upload", {"parent_entry_id": FOLDER, "name": RUN_NAME, "extension":"html", "mime_type":"text/html", "upload_type":"PRE_SIGNED_URL", "size": str(len(data_bytes))})
    biz = mc.biz(r)
    if biz.get("code") != 0:
        raise RuntimeError("apply_upload FAIL {0}".format(biz.get("message")))
    sess = biz["data"]["session"]
    sid = sess.get("session_id") or sess.get("id")
    url = sess.get("upload_url") or sess["objects"][0]["upload_url"]
    st = put_bytes(url, data_bytes)
    if st != 200: raise RuntimeError("PUT status " + str(st))
    r2 = mc.call("file_commit_upload", {"session_id": sid})
    biz2 = mc.biz(r2)
    if biz2.get("code") != 0: raise RuntimeError("commit FAIL " + str(biz2.get("message")))
    rid = biz2["data"]["entry"]["id"]
    print("乐享新建页 OK entry_id=", rid)
    mapf = json.load(open(os.path.join(BASE, "lexiang-entry-map.json"), encoding="utf-8"))
    sm = mapf.setdefault("afternoontea", {"folder_id": FOLDER, "rounds": []})
    sm["folder_id"] = FOLDER
    sm["rounds"].append({"date": DATE, "entry_id": rid, "name": RUN_NAME})
    json.dump(mapf, open(os.path.join(BASE, "lexiang-entry-map.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("已回写 lexiang-entry-map.json")
except Exception as e:
    print("\u26a0\ufe0f 乐享上传跳过（warning，不中断）：" + str(e)[:300])

print("\n=== R24 完成：新增", added, "卡，墙现", after, "卡 ===")
