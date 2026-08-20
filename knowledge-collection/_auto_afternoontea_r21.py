# -*- coding: utf-8 -*-
"""下午茶研讨 二十一轮补采 (2026-08-20) — 渲染增量 + 追加进累计墙 + 更新 index.json
同时补完上一轮(二十轮 2026-08-20 +6)缺失的 run page 由后续 gen_run_page 处理。
"""
import json, os, re

BASE = os.path.dirname(os.path.abspath(__file__))
AT_DIR = os.path.join(BASE, "afternoontea")
CUM = os.path.join(AT_DIR, "afternoontea.html")
IDX = os.path.join(BASE, "index.json")
DATE = "20260820"
ROUND = "二十一轮 enrich 2026-08-20(+9)"

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---- 本轮新增卡（仅 ②上下级 / ③高管间，0 peer；9张全 NEW，URL 均未命中 index/wall）----
CARDS = [
    {
        "emoji": "🥂",
        "title": "非执行董事闭门午餐会·CEO 同侪坦诚对话（RRA）",
        "cat": "治理层闭门",
        "rel": "r3", "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "全球高管寻聘巨头 Russell Reynolds Associates（RRA）在新西兰举办「非执行董事午餐会」系列闭门活动，把该国顶尖企业 CEO 聚到一起，就经济增速与地缘政治不确定性下的领导挑战展开「同行主导（peer-led）」的坦诚对话；同期配套「公司秘书圆桌」，围绕如何借人才与文化撬动企业战略分享洞见。以私密午宴替代正式论坛，让同量级决策者卸下姿态、讲真问题。",
        "how": "做治理层/高管圈层运营时，参考 RRA 的「闭门午餐会 + 同行主导」模式——定向邀约同层级（CEO/非执行董事/董秘）小范围闭门，由专业机构背书增信；议题紧扣当下宏观与治理痛点；午宴氛围降低姿态、提升坦诚，让同侪敢讲真问题。适合作为高管同侪圈层的固定载体，与「独立董事会客厅」互补。",
        "url": "https://www.russellreynolds.co/zh-cn/insights/events/non-executive-director-luncheon-2025",
        "note": "适用：③ 治理层/CEO 同侪闭门（非对外，纯高管私密交流；RRA 为国际高管寻聘权威机构，视为行业权威二手）。",
    },
    {
        "emoji": "☕",
        "title": "硅谷咖啡文化·非正式碰撞是信任测试与协作基础设施",
        "cat": "高管 networking",
        "rel": "r3", "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "硅谷最关键的对话常在早餐铺、咖啡馆、甜甜圈店发生——创始人撞上投资人、工程师撞上研究员。咖啡馆比公司会议室更「exploratory 而非 transactional」：人在此更敢讲未完成的点子、测理论。咖啡局也是硅谷高效的「信任测试系统」：投资人投的是 founder 而非产品，cofounder 选彼此看能否共渡不确定，而咖啡局暴露好奇心、ego、倾听力、韧性、脾性——pitch deck 测不出。Buck's 餐厅的早餐局曾助推 Netscape 诞生。",
        "how": "管高管生态/创始人关系时，把「咖啡」当战略触点而非休息：非正式氛围降低防御，让同侪/投资人/潜在 cofounder 暴露真实信号；用「What are you working on?」开场测好奇心与韧性；重大决策（融资/并购/合伙）前，先咖啡局验「我愿不愿意和这人共渡不确定性」。别用正式会议扼杀未成形想法的碰撞空间。",
        "url": "https://www.sparknify.com/post/20260524-coffee-and-boba-en",
        "note": "适用：③ 创始人×投资人/同侪高管，非正式咖啡作为信任测试与 networking 基础设施（洞察向，非内部员工活动；可作高管关系经营的方法论参考）。",
    },
    {
        "emoji": "📋",
        "title": "Skip-level 越级 1:1 议程模板（Range·工具官方）",
        "cat": "越级沟通",
        "rel": "r2", "rel_text": "上下级",
        "src": "b1", "src_text": "一手",
        "val": "团队协作工具 Range 官方提供 skip-level 1:1 议程模板：作为高管/VP/CEO，与「非直接下属」做 1:1，获得团队日常真实视角、检验中层管理表现，也给一线员工了解公司战略的机会。标准议程：破冰(2min)→团队怎么样(5min)→你在做什么(5min)→个人目标(5min)→公司该改什么(5min)→开放问答(20min)→收尾(3min)。强调「可预测的节奏 + 提前沟通目的」，倾听多于表达，平衡公司/团队/个人三维度。",
        "how": "做越级沟通时，直接用 Range 这套可复制议程：固定节奏（别突然袭击）、开场讲清目的（非评估）、多听少说；破冰用轻松问题，中段问团队/工作/个人目标，留出大段开放问答让员工问战略。关键是「中层经理知情 + 不绕过经理」——收集到的反馈聚合后回传给直属经理，避免制造三角冲突。",
        "url": "https://www.range.co/templates/skip-level-one-on-one-meeting-agenda",
        "note": "适用：② 高管/中层 leader 做 skip-level 越级 1:1（工具官方一手方法论；落地前务必让中间经理知情，避免信任三角）。",
    },
    {
        "emoji": "🔍",
        "title": "Skip-level 深度指南 2026·「跟进是信任引擎」+ 文档悖论",
        "cat": "越级沟通",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "2026 skip-level 实操指南提炼核心法则：少问多跟进——把一条线索问透（「你说发布流程每迭代吃掉一天，展开讲讲」）胜过十个问卷式问题。给出 30-45 分钟议程（框架2min/他们的世界15min/信息流10min/他们的问题10min/收尾3min）。点破「文档悖论」：skip-level 的价值在跨多次对话的模式，笔记很重要，但当场打字会让紧张员工退回安全答案——用无入会机器人的设备级录音（透明告知+取得同意）替代。最重要一条：收尾的「跟进+责任人+日期」与「哪些会回传中层经理」决定下一轮更容易而非更难。",
        "how": "办 skip-level 别只收集意见——把最后一块「跟进承诺+回传范围」当整个格式的信任引擎：员工讲的事若需行动就跟进，即便结论是暂不 action 也要告知；把反馈聚合回中层经理让其知道自己在循环中。记录用设备级工具、透明声明并获同意，绝不在信任建设会上偷偷录音。避免把人当经理的「法庭」。",
        "url": "https://super-intern.com/en/blog/2026-skip-level-meeting-guide",
        "note": "适用：② 高管/HR 做 skip-level 越级沟通（2026 实操指南；强调跟进闭环与记录透明度，与 Range 议程模板互补）。",
    },
    {
        "emoji": "🪑",
        "title": "创始人每季度与每位员工炉边谈话（SpareFoot CEO 自述）",
        "cat": "创始人对话",
        "rel": "r2", "rel_text": "上下级",
        "src": "b1", "src_text": "一手",
        "val": "SpareFoot 联合创始人兼 CEO Chuck Gordon 自述：借鉴罗斯福「炉边谈话」的非正式对话基调，每半年与全公司 90+ 员工一对一炉边谈话，每次约 30 分钟——给反馈、聊进展、听顾虑、答问题。会前用 Google 表单让员工先想清楚「什么顺利 / 什么让你睡不着 / 给自己定个半年目标」，提升对话质量。初衷是团队长大到 12→90 人后，想保持对公司的「一对一能见度」。他说研究显示员工需要的不只是「门永远敞开」，而是真正安全的发声环境。",
        "how": "创始人/一号位想保持与全员连接时，参考「半年一轮、每人 30 分钟、会前问卷」的炉边谈话机制：把「你半年目标我们下次复盘」变成闭环；会前问卷逼员工先想清楚，省下寒暄、提升质量；坦诚氛围让员工敢讲问题。关键是用「固定节奏 + 会前准备 + 安全发声」替代空泛的「我门常开」。",
        "url": "https://www.allbusiness.com/why-i-hold-fireside-chats-with-every-employee-at-my-company-9695-1.html",
        "note": "适用：② 创始人/一号位 × 全员（当事人一手自述；90人规模可复制的「炉边谈话」机制，与高管 fireside chat 方法论互补）。",
    },
    {
        "emoji": "🫖",
        "title": "总经理见面会·零距离倾听一线员工（龙珠达·官方）",
        "cat": "总经理见面",
        "rel": "r2", "rel_text": "上下级",
        "src": "b1", "src_text": "一手",
        "val": "龙珠达集团总经理与来自一线的 8 名员工代表，在轻松茶歇氛围中齐聚交流。总经理以暖心开场感谢一线辛勤付出、鼓励放下拘谨敞开心扉；员工围绕日常工作、个人成长、团队协作分享心得并提出实际困难，总经理认真倾听、现场答疑，并结合自身经历为年轻员工职业发展指方向。氛围温馨，拉近彼此距离，体现「龙珠达一家人」理念，集团表示将持续搭建此类沟通桥梁。",
        "how": "做「总经理 × 一线」沟通时，学龙珠达：用茶歇替代正式会议室降姿态；领导开场先感谢+鼓励畅言定调；现场答疑+结合自身经历给年轻人指路，比空讲战略更暖；小范围（8 人左右）保证人人发声。把单次见面会变成「持续沟通桥梁」而非一次性作秀。",
        "url": "https://www.longzhudagroup.com/News_1/58.html",
        "note": "适用：② 总经理/高管 × 一线员工代表（企业官方一手案例；茶歇降姿态 + 现场答疑 + 职业指路，小范围沟通范本）。",
    },
    {
        "emoji": "🍵",
        "title": "红府超市 茶话会式员工座谈·破除层级壁垒（官方一手）",
        "cat": "员工座谈",
        "rel": "r2", "rel_text": "上下级",
        "src": "b1", "src_text": "一手",
        "val": "红府超市（国生电器）打破传统圆桌座谈，以轻松茶话会形式开员工座谈会：商之都副总经理、红府超市董事长主持，各业务部门负责人与基层员工代表参会。宽松自由氛围破除层级沟通壁垒，员工放下顾虑畅所欲言，聚焦岗位痛点、发展难点、工作堵点提合理化建议。董事长认真聆听、细致记录，现场逐一回应、集中研判、统筹部署，把基层心声转化为优化管理、提质增效的务实行动，构建双向沟通、双向赋能机制。",
        "how": "办员工座谈别用「领导坐主席台、员工排排坐」的正式圆桌——改茶话会降壁垒；一把手主持+现场记录+当场回应，把建议变成可落地的整改动作；会后形成「收集—梳理—落实—回音」闭环。关键是让管理层真正下沉、员工真正敢讲，而非走流程。",
        "url": "http://www.ahszd.com.cn/hongfuchaoshi/info_itemid_30406.html",
        "note": "适用：② 一把手/管理层 × 基层员工（企业官方一手案例；茶话会破层级 + 现场回应 + 闭环落实，座谈范式）。",
    },
    {
        "emoji": "📮",
        "title": "中国邮政工会「品茗+座谈」茶话会·旺季献计（官方一手）",
        "cat": "工会茶话",
        "rel": "r2", "rel_text": "上下级",
        "src": "b1", "src_text": "一手",
        "val": "宜宾市邮政公司工会为旺季营销减压鼓劲，举办「关怀赋能，决胜旺季」茶话会，创新采用「品茗+座谈」形式：全市十区县支局长、揽投部经理与公司党委书记、总经理、工会主席及部门负责人齐聚，围绕「我为旺季献计献策」深入交流、畅所欲言，分享网点经验、提营销策略与困境。总经理以「茶道讲经营」类比（凝聚力如细胞核、专业力如六艺），现场回应诉求、对接资源。茶艺表演舒缓压力、激发建言。",
        "how": "做「领导 × 一线骨干」沟通（尤其业务攻坚期）时，学邮政工会：用「品茗+座谈」替代硬核会议降压力；一把手用生活化类比（茶道→经营）拉近距离、讲清要求；现场回应+对接资源，把建言变战斗力。适合旺季/冲刺期给一线减压鼓劲、群策群力。",
        "url": "https://www.cptu.org.cn/gh/report/2511/7612-1.htm",
        "note": "适用：② 工会/一把手 × 一线骨干（官方工会一手案例；品茗座谈 + 业务攻坚期减压鼓劲 + 茶道类比，攻坚期沟通范本）。",
    },
    {
        "emoji": "🤝",
        "title": "卓尔科技 总经理接待日·有温度的对话（官方一手）",
        "cat": "总经理接待",
        "rel": "r2", "rel_text": "上下级",
        "src": "b1", "src_text": "一手",
        "val": "卓尔科技长期开展「总经理接待日」：公司领导分别与各部门员工代表诚挚对话，重点从「疫情期间员工状态 / 个人与公司发展方向 / 如何快速恢复状态 / 后续如何改进」四方向听建议。员工列举环境与状态不足，也对「不裁员不降薪」、优秀员工涨薪点赞，提宝贵建议；晚宴几小时全员吐露心声、真情互动。活动拓宽诉求渠道，下一步形成「意见集中梳理→提交总经办→制定改善措施→件件有回音」闭环机制。",
        "how": "做常态化「领导接待日」时，学卓尔：固定栏目（接待日）+ 明确四方向议题（状态/方向/恢复/改进）；把晚宴/茶叙当真情互动场；最关键建「收集—梳理—总经办—改善—回音」闭环，让提的意见件件有下落。避免「开了会没下文」消耗信任。",
        "url": "https://www.zhuoer-tech.com/section/44/51",
        "note": "适用：② 总经理/领导 × 员工代表（企业官方一手案例；常态化接待日 + 四方向议题 + 闭环回音机制）。",
    },
]

def card_html(c, indent=4):
    sp = " " * indent
    sp2 = " " * (indent + 2)
    rel_badge = f'<span class="badge {c["rel"]}">{c["rel_text"]}</span>'
    src_badge = f'<span class="badge {c["src"]}">{c["src_text"]}</span>'
    return (
        f'{sp}<div class="hl">\n'
        f'{sp2}<div class="top"><span class="emoji">{esc(c["emoji"])}</span>'
        f'<h3>{esc(c["title"])}</h3><span class="cat">{esc(c["cat"])}</span>'
        f'{rel_badge}{src_badge}</div>\n'
        f'{sp2}<p class="val">{esc(c["val"])}</p>\n'
        f'{sp2}<details class="exec"><summary>怎么做</summary><div class="inner">{esc(c["how"])}</div></details>\n'
        f'{sp2}<div class="src">🔗 <a href="{esc(c["url"])}" target="_blank">{esc(c["url"])}</a></div>\n'
        f'{sp2}<div class="note">{esc(c["note"])}</div>\n'
        f'{sp}</div>\n'
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

html = open(CUM, encoding="utf-8").read()
before = html.count('<div class="hl">')

cards_sec3 = [c for c in CARDS if c["rel"] == "r3"]
cards_sec2 = [c for c in CARDS if c["rel"] == "r2"]

# r3 卡插入 sec3 的 grid 闭合前
i3 = html.find('class="sec sec3"')
close3 = find_grid_close(html, i3)
card3_html = "".join(card_html(c) for c in cards_sec3)
html = html[:close3] + card3_html + html[close3:]

# r2 卡插入 sec2 的 grid 闭合前
i2 = html.find('class="sec sec2"')
close2 = find_grid_close(html, i2)
card2_html = "".join(card_html(c) for c in cards_sec2)
html = html[:close2] + card2_html + html[close2:]

# 更新 hero 时间线
hero_old = "二十轮 enrich 2026-08-20(+6)</p>"
hero_new = "二十轮 enrich 2026-08-20(+6) ｜ 二十一轮 enrich 2026-08-20(+9)</p>"
assert hero_old in html, "hero timeline marker not found"
html = html.replace(hero_old, hero_new, 1)

# 更新 sec 区段计数标签
def recount(tagcls):
    # 统计该 sec 内 hl 数量
    s = html.find(f'class="{tagcls}"')
    e = html.find('class="sec', s + 10)
    seg = html[s:e]
    return seg.count('<div class="hl">')
r2n = recount('sec sec2')
r3n = recount('sec sec3')
html = re.sub(r'(<div class="sec sec2">.*?<span class="tag">)\d+( 卡</span>)',
              lambda m: m.group(1) + str(r2n) + m.group(2), html, count=1, flags=re.S)
html = re.sub(r'(<div class="sec sec3">.*?<span class="tag">)\d+( 卡</span>)',
              lambda m: m.group(1) + str(r3n) + m.group(2), html, count=1, flags=re.S)

with open(CUM, "w", encoding="utf-8") as f:
    f.write(html)

# 写出本轮新卡 HTML 块（供 gen_run_page 模式A）
tmp = os.path.join(AT_DIR, ".run_newcards.tmp.html")
with open(tmp, "w", encoding="utf-8") as f:
    f.write("".join(card_html(c) for c in CARDS))

# 校验
after = html.count('<div class="hl">')
r2 = html.count('badge r2'); r3 = html.count('badge r3')
b1 = html.count('badge b1'); b2 = html.count('badge b2')
footer_ok = "📌 本页由 yitong" in html
print("累计墙卡片数:", after, "(+", after - before, ") | r2:", r2, "r3:", r3, "| b1:", b1, "b2:", b2, "| footer:", footer_ok)
print("sec2 tag:", r2n, "sec3 tag:", r3n)

# ---- 更新 index.json ----
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
        print("SKIP dup url:", u)
        continue
    rel_map = {"r2": "supervisor", "r3": "exec"}
    entry = {
        "title": c["title"],
        "normKey": normkey(c["title"]),
        "url": c["url"],
        "sourceType": "secondary" if c["src"] == "b2" else "primary",
        "relation": rel_map[c["rel"]],
        "summary": c["cat"] + "：" + c["val"][:60],
        "topic": "afternoontea",
    }
    data.append(entry)
    added += 1
print("index.json 新增:", added, "-> 现", len(data), "条")
json.dump(data, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

meta = {
    "date": DATE, "round": ROUND, "added": added, "before": before, "after": after,
    "r2only": r2n, "r3only": r3n, "b1": b1, "b2": b2,
}
json.dump(meta, open(os.path.join(BASE, "_afternoontea_r21_meta.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("meta 已写出")
