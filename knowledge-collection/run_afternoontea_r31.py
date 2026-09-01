# -*- coding: utf-8 -*-
"""下午茶研讨 三十一轮补采 (2026-09-01) — 渲染增量 + 追加进累计墙 + 更新 index.json + Obsidian + 乐享上传
仅 ②上下级 / ③高管间，0 peer。
经核对，原计划的诚通书记接待日(=R24中国诚通)、浦东首期企业话发展(=R19)、CGF中国董事CEO闭门会(=R20)
均为已收录同事件，本轮剔除；仅保留 9 张全新卡（7 ② + 2 ③）。"""
import json, os, re, urllib.request, urllib.error

BASE = os.path.dirname(os.path.abspath(__file__))
AT_DIR = os.path.join(BASE, "afternoontea")
CUM = os.path.join(AT_DIR, "afternoontea.html")
IDX = os.path.join(BASE, "index.json")
DATE = "20260901"
RUN_NAME = "afternoontea-20260901.html"
RUN_PATH = os.path.join(AT_DIR, RUN_NAME)

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# 关系档：②上下级 7 张（3 一手 + 4 二手）+ ③高管间 2 张（2 一手），0 peer
CARDS = [
    {
        "emoji": "\U0001F4EC",
        "title": "中汽天检「员工接待日」·班子成员月月下沉一线",
        "cat": "员工接待日",
        "rel": "r2", "rel_text": "上下级",
        "src": "b1", "src_text": "一手",
        "val": "中汽研汽车检验中心（天津）2026年常态化开展「员工接待日」，班子成员每月深入集成性能中心、国际化中心、低碳环保中心等一线部门，与员工面对面交流，倾听市场开拓、科研创新、人才管理、物流运输等建议；能当场解决的立即部署，需跨部门协调的明确责任人与时限，一时难解耐心解释并纳入督办。首站（3月25日）即收集回应50余项建议诉求，5月、6月持续延展，把接待日做成「常态化沟通桥梁」。",
        "how": "办员工接待日，学「中汽天检」班子成员每月下沉+当场部署+督办闭环：一把手/副总直接进一线部门，员工提建议现场分「立改/协调/解释」三类处理，用「声声有回音」把关爱落到科研与后勤小事。关键是接待日不走过场、建机制常态化。",
        "url": "https://www.catarc.ac.cn/mobile/detail/9d5d327e8a204eb59a07df0f62863850",
        "note": "适用：② 央企科研院所班子成员 × 一线科研/技术员工（官网一手；员工接待日常态化+闭环反馈，可作研发型单位民主沟通范本）。",
    },
    {
        "emoji": "\U0001F3ED",
        "title": "中国盐湖工业集团首个「职工接待日」·董事长坐班点对点",
        "cat": "职工接待日",
        "rel": "r2", "rel_text": "上下级",
        "src": "b1", "src_text": "一手",
        "val": "中国盐湖工业集团2026年6月在察尔汗盐湖产区举办首个「职工接待日」，党委书记、董事长薛飞与一线职工点对点、面对面交流，围绕企业发展、人力资源、薪酬福利、设备运行、生产协同、制度流程、基层负担、后勤保障等提建议；能立即解决立即办结，需协调的明确责任部门与时限并跟踪督办，暂不具备条件的耐心解释，做到「声声有回音、事事有答复、件件有落实」；后续制度化、常态化闭环管理。",
        "how": "办职工接待日，学「中国盐湖」董事长坐班+首接建账+限时督办：一把手与一线职工点对点，建议分「即办/协调/解释」三类，建制度常态化。适合把接待日做成联系基层、转化民意的硬渠道。",
        "url": "https://www.minmetals.com/ddjj/ghyd/202606/t20260610_315946.html",
        "note": "适用：② 央企集团党委书记/董事长 × 一线职工（五矿官方一手；职工接待日制度化+闭环，可作高原/生产型央企范本）。",
    },
    {
        "emoji": "\U0001F6E0\uFE0F",
        "title": "中国一冶天津公司「工会主席接待日」·工地流动+扫码双线",
        "cat": "工会主席接待日",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "中国一冶天津公司自2025年6月26日起常态化开展书记、工会主席接待日，结合施工项目分散、职工常驻一线特点，创新「工地流动接待+线上扫码反馈」双线模式：线下下沉各在建项目工地设流动接待点，线上开通诉求二维码全天候无间断；已办两期，收集充电桩加装、健身房、快递架、探亲路费补贴等诉求17条，分类建档、移交责任部门、明确时限、跟踪督办，件件有回音。",
        "how": "办工会主席接待日，学「中国一冶天津」双线模式：工地流动接待点+线上扫码，让驻外一线就近反映；诉求分类建档、限时督办、源头疏导。适合项目分散型施工企业把沟通做到工地现场。",
        "url": "https://www.workercn.cn/c/2026-07-13/8845672.shtml",
        "note": "适用：② 建筑企业工会主席 × 驻外一线职工（工人日报二手；流动接待+扫码反馈双线闭环，可作工程类企业范本）。",
    },
    {
        "emoji": "\U0001F9FD",
        "title": "中原油田天然气产销厂「书记接待日」·把桌子搬进班组",
        "cat": "书记接待日",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "中原油田天然气产销厂2026年6月在北海管道项目部开展「书记接待日」，把接待桌搬到基层班组，党支部书记与巡线工面对面，无预约无填表、无严肃会场；围绕水杯容量、食堂菜品、劳保发放、技能提升等「接地气」问题，当场解决16件、提报厂工会批复7件；变「被动接待」为「主动问诊」，每月固定时间地点常态化，打通诉求「最后一米」。",
        "how": "办书记接待日，学「中原油田天然气产销厂」把桌子搬进班组：书记下一线、无门槛交流、现场答+提报督办双路径；从水杯、劳保等小事切入建信任。适合野外/外闯一线单位把接待窗口前移。",
        "url": "http://www.hngrrb.cn/paper/2026-06/15/content_99123659.html",
        "note": "适用：② 油田基层党支部书记 × 野外一线职工（河南工人日报二手；书记接待日进班组+主动问诊，可作能源外闯单位范本）。",
    },
    {
        "emoji": "\U0001F375",
        "title": "荆门工厂「员工沟通会」·总经理坐镇现场回应",
        "cat": "员工沟通会",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "金龙泉啤酒荆门工厂2026年4月召开「凝心聚力，共迎挑战」主题员工沟通会，副总经理、工厂总经理董传金与各部门负责人、员工代表围绕优质高效低耗保供四大导向部署旺季生产；交流环节员工提设备维保、流程优化、后勤保障等数十条建议，总经理及部门负责人逐一现场回应、明确整改责任人与时限；会前还表彰专项认可团队，把沟通会做成管理层与一线距离拉近的常态载体。",
        "how": "办员工沟通会，学「荆门工厂」总经理坐镇+现场回应+表彰先行：旺季前聚一线代表，建议现场分责限时；用颁奖拉近距离、用坦诚换干劲。适合制造业把沟通会嵌进生产节奏。",
        "url": "http://www.jlq.com.cn/admin.php/newspaper/article/id/2149.html",
        "note": "适用：② 工厂总经理 × 一线员工代表（金龙泉官网二手；员工沟通会+现场回应闭环，可作快消制造范本）。",
    },
    {
        "emoji": "\u2600\uFE0F",
        "title": "通威太阳能金堂基地「总经理座谈会」·闭环管理文化抓手",
        "cat": "总经理座谈会",
        "rel": "r2", "rel_text": "上下级",
        "src": "b1", "src_text": "一手",
        "val": "通威太阳能科技金堂基地2026年一季度总经理座谈会，总经理助理朱剑诚携部门负责人与20位员工代表深入交流，收集阳光币审批、办公技能培训、文创更新、后勤服务等10余项诉求，具备条件当即明确整改路径，需协同的现场认领责任并划反馈时限，形成闭环；朱总强调员工是企业最宝贵财富，逐条梳理推动落地；基地把倾听基层心声作为文化建设核心抓手，探索常态化沟通渠道。",
        "how": "办总经理座谈会，学「通威金堂」员工代表小范围+诉求当场分责限时：总经理助理带部门负责人直面20人，建议即时改/协同改双轨，闭环管理。适合光伏制造把座谈做成常态化文化抓手。",
        "url": "https://www.tongwei.com/news/detail/170495.html",
        "note": "适用：② 基地总经理/总助 × 一线员工代表（通威官网一手；总经理座谈会+闭环管理，可作新能源制造范本）。",
    },
    {
        "emoji": "\U0001F5C3\uFE0F",
        "title": "青岛寰宇「车间板凳会」·15分钟提、72小时办",
        "cat": "车间板凳会",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "寰宇东方国际集装箱（青岛）在青岛西海岸新区总工会指导下创新「车间板凳会」，领导班子每月至少1次身着工装、自带板凳深入车间，与一线职工同坐板凳拉家常；执行「直系领导回避」制度消除顾虑，每次聚焦1-2个班组、15-20名代表、限时15分钟直陈问题；能现场答的即时回应，复杂问题明确责任部门与时限，会后24小时出纪要、72小时启动「双跟踪」（联络员反馈职工+责任部门推进）；截至10月办26次、覆盖64个班组，高频诉求最快2天解决。",
        "how": "办车间板凳会，学「青岛寰宇」去层级+直系领导回避+72小时双跟踪：领导进车间坐板凳、限时直陈、回避上级保坦诚；党建+工会联动55名联络员一对一跟踪。把座谈从「议而不决」升级为「15分钟提、72小时办」。",
        "url": "https://www.sdgh.org.cn/art/2025/12/29/art_101583_10363084.html",
        "note": "适用：② 制造企业领导班子 × 一线班组职工（山东工会网二手；车间板凳会+72小时闭环，可作产改民主管理标杆范本）。",
    },
    {
        "emoji": "\U0001F391",
        "title": "国务院发展研究中心中国发展高层论坛2026闭门圆桌会·政策层×全球CEO",
        "cat": "高层闭门圆桌",
        "rel": "r3", "rel_text": "高管间",
        "src": "b1", "src_text": "一手",
        "val": "国务院发展研究中心在中国发展高层论坛2026年年会期间（3月23日）举办闭门圆桌会，中心主任、党组书记陆昊主持，副主任隆国强、张琦出席；近30位跨国企业、国际智库与机构负责人（博世、罗氏、力拓、瑞士再保险、ABB、贝恩、英中贸易协会、港交所等）参加，围绕中国经济与世界经济重要问题、「十五五」扩大高水平对外开放对跨国企业在华投资合作新机遇深入交流；陆昊认真听取外方意见并作总结。",
        "how": "运营高层闭门圆桌，参考国研中心论坛模式：政府高层+跨国企业董事会主席/CEO小范围闭门，围绕宏观与开放议题深度对话；用「听取外方意见+总结回应」形成政策与市场双向校准。区别于企业私董会，本场是「政策层×全球CEO」的国情咨商场。",
        "url": "https://www.drc.gov.cn//DocView.aspx?chnid=382&docid=2909750&leafid=1346",
        "note": "适用：③ 政府智库/部委高层 × 跨国企业董事会主席/CEO（国研中心官方一手；闭门圆桌+高水平开放咨商，可作政企高层对话范本）。",
    },
    {
        "emoji": "\U0001F9EC",
        "title": "浦东政协2026第二期「企业话发展」下午茶·张江生物医药",
        "cat": "政企下午茶",
        "rel": "r3", "rel_text": "高管间",
        "src": "b1", "src_text": "一手",
        "val": "浦东新区政协2026年第二期「企业话发展」下午茶5月29日在张江举办，主题「万亿赛道新引擎：生物医药的全链条创新策源」，由政协医药卫生界、农工党界别、科学技术界联合主办，人民网上海协办；12位创新药/细胞基因治疗/高端医疗器械企业家与专家，围绕创新策源、产业链堵点、临床资源对接、共性技术平台、政策落地建言；政协主席姬兆亮、副主席王小君出席互动，强调就地转化、就近落地、就地示范，把建议形成建言专报跟踪督办。",
        "how": "办政企下午茶，学「浦东政协企业话发展」品牌第二期：政协搭台+界别联合+人民网协办，聚焦单产业链（生物医药）小范围闭门；企业家直陈痛点、政协当场互动并转专报督办。把下午茶做成「倾听企业真问题、破解发展真堵点」的精准协商平台。",
        "url": "https://sh.people.com.cn/n2/2026/0601/c134768-41598064.html",
        "note": "适用：③ 政协主席/副主席 × 行业头部企业家（人民网上海一手；企业话发展下午茶+单产业链专场+专报督办，可作政企协商品牌范本；首期抱团出海已收 R19，本卡为二期生物医药专场）。",
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
        '<title>\u4e0b\u5348\u8336\u7814\u8ba8 \u00b7 \u4e09\u5341\u4e00\u8f6e\u589e\u91cf\u5361\u7247\uff082026-09-01\uff09</title>\n'
        '<style>\n' + STYLE + '\n</style>\n</head><body>\n<div class="wrap">\n'
        '<p style="margin:0 0 16px"><a href="' + WALL_URL + '" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">\U0001F375 \u8fd4\u56de\u4e0b\u5348\u8336\u7d2f\u8ba1\u5361\u7247\u5899 \u2192</a> &nbsp; '
        '<a href="' + PORTAL_URL + '" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">\U0001F4DA \u8fd4\u56de\u77e5\u8bc6\u5e93\u95e8\u6237 \u2192</a></p>\n'
        '  <div class="hero">\n'
        '    <h1>\U0001F375 \u4e0b\u5348\u8336\u7814\u8ba8 \u00b7 \u4e09\u5341\u4e00\u8f6e\u589e\u91cf\u5361\u7247\uff082026-09-01\uff09</h1>\n'
        '    <p>\u672c\u8f6e\u65b0\u589e 9 \u5f20\uff08\u901a\u8fc7\u516d\u7ef4\u8bc4\u4f30\uff0c\u5254\u9664\u5e73\u7ea7/\u670b\u53cb\u5411\uff0c\u4ec5 ②\u4e0a\u4e0b\u7ea7 / ③\u9ad8\u7ba1\u95f4\uff09\uff1b\u5173\u7cfb\u6863\uff1a③\u9ad8\u7ba1\u95f4 2 \u5f20 + ②\u4e0a\u4e0b\u7ea7 7 \u5f20\u3002\u539f\u8ba1\u5212 12 \u5f20\uff0c\u7ecf\u6838\u5bf9\u8bda\u901a\u4e66\u8bb0\u65e5/R24\u3001\u671d\u9633\u9996\u671f/R19\u3001CGF/R20 \u5747\u4e3a\u5df2\u6536\u5f55\u540c\u4e8b\u4ef6\uff0c\u526a\u81f3 9 \u5f20\u5168\u65b0\u3002</p>\n'
        '    <div class="relbar">\n'
        '      <span>② \u9886\u5bfc\u2194\u5458\u5de5\uff08\u4e0a\u4e0b\u7ea7\uff0csupervisor\uff09</span>\n'
        '      <span>③ \u9886\u5bfc\u2194\u9886\u5bfc\uff08\u9ad8\u7ba1\u95f4\uff0cexec\uff09</span>\n'
        '    </div>\n'
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
hero_old = "\u4e09\u5341\u8f6e enrich 2026-08-28(+9)</p>"
hero_new = "\u4e09\u5341\u8f6e enrich 2026-08-28(+9) \uff5c \u4e09\u5341\u4e00\u8f6e enrich 2026-09-01(+9)</p>"
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
assert "（240 卡 · 上下级/高管间）" in t
t = t.replace("（240 卡 · 上下级/高管间）", "（249 卡 · 上下级/高管间）", 1)
assert "\u7d2f\u8ba1 240 \u5361\uff08③\u9ad8\u7ba1\u95f4 87 / ②\u4e0a\u4e0b\u7ea7 157\uff1b\u4e00\u624b 78 / \u4e8c\u624b 162\uff09" in t
t = t.replace("\u7d2f\u8ba1 240 \u5361\uff08③\u9ad8\u7ba1\u95f4 87 / ②\u4e0a\u4e0b\u7ea7 157\uff1b\u4e00\u624b 78 / \u4e8c\u624b 162\uff09",
              "\u7d2f\u8ba1 249 \u5361\uff08③\u9ad8\u7ba1\u95f4 89 / ②\u4e0a\u4e0b\u7ea7 164\uff1b\u4e00\u624b 83 + \u4e8c\u624b 166\uff09", 1)
# timeline blockquote
tl_old = "\u4e09\u5341\u8f6e enrich 2026-08-28(+9)\uff5c"
tl_new = "\u4e09\u5341\u8f6e enrich 2026-08-28(+9) \uff5c \u4e09\u5341\u4e00\u8f6e enrich 2026-09-01(+9)\uff5c"
assert tl_old in t
t = t.replace(tl_old, tl_new, 1)
# section headers (catch up to cumulative)
assert "## ③ 领导↔领导（高管间 · exec）— 57 卡" in t
t = t.replace("## ③ 领导↔领导（高管间 · exec）— 57 卡", "## ③ 领导↔领导（高管间 · exec）— 89 卡", 1)
assert "## ② 领导↔员工（上下级 · supervisor）— 99 卡" in t
t = t.replace("## ② 领导↔员工（上下级 · supervisor）— 99 卡", "## ② 领导↔员工（上下级 · supervisor）— 164 卡", 1)
# append round narrative at end
round_section = (
    "\n## 轮次 2026-09-01（+9）\n"
    "> 三十一轮 enrich：新增 9 卡（③ 高管间 +2：国务院发展研究中心中国发展高层论坛2026闭门圆桌会·政策层×全球CEO咨商 / 浦东政协2026第二期「企业话发展」下午茶·张江生物医药；② 上下级 +7：中汽天检「员工接待日」/ 中国盐湖工业集团首个「职工接待日」/ 中国一冶天津公司「工会主席接待日」/ 中原油田天然气产销厂「书记接待日」/ 荆门工厂「员工沟通会」/ 通威太阳能金堂基地「总经理座谈会」/ 青岛寰宇「车间板凳会」）。无 peer，relation 仅取 supervisor/exec。注：原计划的诚通书记接待日(=R24中国诚通)、浦东首期企业话发展(=R19)、CGF中国董事CEO闭门会(=R20) 经核对均为已收录同事件，本轮剔除，仅保留 9 张全新卡。\n"
    "> 线上预览：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/afternoontea/afternoontea.html ｜ 本轮增量页：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/afternoontea/afternoontea-20260901.html\n"
)
t = t.rstrip("\n") + "\n" + round_section
open(NOTE, "w", encoding="utf-8").write(t)
print("Obsidian 笔记更新完成")

# ---- 5) 00-索引 ----
IDX0 = os.path.join(VAULT, "00-知识采集索引.md")
i0 = open(IDX0, encoding="utf-8").read()
# header timeline backfill 29/30 + add 31
assert "\u4e8c\u5341\u516b\u8f6e enrich 2026-08-26(+10)\uff09" in i0
i0 = i0.replace("\u4e8c\u5341\u516b\u8f6e enrich 2026-08-26(+10)\uff09",
                "\u4e8c\u5341\u516b\u8f6e enrich 2026-08-26(+10)\uff09 \uff5c \u4e8c\u5341\u4e5d\u8f6e enrich 2026-08-27(+10) \uff5c \u4e09\u5341\u8f6e enrich 2026-08-28(+9) \uff5c \u4e09\u5341\u4e00\u8f6e enrich 2026-09-01(+9)\uff09", 1)
# total
if "**240 卡**" in i0:
    i0 = i0.replace("**240 卡**", "**249 卡**", 1)
    print("00-索引 total 240->249")
# breakdown best-effort
old_break = "59 \u5361 / 103 \u5361\uff08\u542b 4 \u5f20\u8de8\u6863\u53cc\u6807\uff0c\u53bb\u91cd\u540e 148\uff09"
if old_break in i0:
    i0 = i0.replace(old_break, "89 \u5361 / 164 \u5361\uff08\u542b 4 \u5f20\u8de8\u6863\u53cc\u6807\uff0c\u53bb\u91cd\u540e 249\uff09", 1)
    print("00-索引 breakdown 已同步")
# append rows + round narrative before nav line
NAV = "\U0001F4C4 \u4e3b\u9898\u6c47\u603b\u7b14\u8bb0\uff1a[[\u77e5\u8bc6\u91c7\u96c6\u5e93/\u7d20\u6750/afternoontea/\u4e0b\u5348\u8336\u7814\u8ba8-\u77e5\u8bc6\u5361\u6c47\u603b|\u4e0b\u5348\u8336\u7814\u8ba8-\u77e5\u8bc6\u5361\u6c47\u603b]]"
assert NAV in i0
rows = "".join(
    "| {0}\uff08afternoontea.html\uff09 | 4 | {1} | {2} | {3} |\n".format(esc(c["title"]), "一手" if c["src"] == "b1" else "二手", "③高管间" if c["rel"] == "r3" else "②上下级", esc(c["note"]))
    for c in CARDS
)
rn = (
    "\n> 三十一轮 enrich 2026-09-01(+9)：③ 国务院发展研究中心中国发展高层论坛2026闭门圆桌会·政策层×全球CEO咨商 / 浦东政协2026第二期「企业话发展」下午茶·张江生物医药；② 中汽天检「员工接待日」/ 中国盐湖工业集团首个「职工接待日」/ 中国一冶天津公司「工会主席接待日」/ 中原油田天然气产销厂「书记接待日」/ 荆门工厂「员工沟通会」/ 通威太阳能金堂基地「总经理座谈会」/ 青岛寰宇「车间板凳会」。\n"
)
i0 = i0.replace(NAV, rows + rn + NAV, 1)
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
    # 回写占位（entry_id=None，待 token 恢复后补传）
    try:
        mapf = json.load(open(os.path.join(BASE, "lexiang-entry-map.json"), encoding="utf-8"))
        sm = mapf.setdefault("afternoontea", {"folder_id": FOLDER, "rounds": []})
        sm["folder_id"] = FOLDER
        sm["rounds"].append({"date": DATE, "entry_id": None, "name": RUN_NAME, "note": "轮次页 R31 (+9：2③高管间+7②上下级，5一手+4二手，待上传)"})
        json.dump(mapf, open(os.path.join(BASE, "lexiang-entry-map.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print("已回写 lexiang-entry-map.json（entry_id=None 占位）")
    except Exception as e2:
        print("map 回写失败:", str(e2)[:200])

print("\n=== R31 完成：新增", added, "卡，墙现", after, "卡 ===")
