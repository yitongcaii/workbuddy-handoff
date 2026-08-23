# -*- coding: utf-8 -*-
"""颁奖典礼 二十三轮补采 (2026-08-23) — 渲染增量 + 追加进累计墙 + 更新 index.json + Obsidian + 乐享上传
仅 ②上下级 / ③高管间，0 peer。本论增量页 award-2026-08-23-r23.html。
乐享：award 主题在乐享以「每轮独立页」落库（folder_id=f585d1b78510459db0ce807cc9688448），
并 best-effort 更新累计墙（若 folder 内存在 award.html 条目则更新，否则跳过，不阻断）。"""
import json, os, re, subprocess, urllib.request, urllib.error

BASE = os.path.dirname(os.path.abspath(__file__))
AT_DIR = os.path.join(BASE, "award")
CUM = os.path.join(AT_DIR, "award.html")
IDX = os.path.join(BASE, "index.json")
DATE = "2026-08-23"
RUN_NAME = "award-2026-08-23-r23.html"
RUN_PATH = os.path.join(AT_DIR, "runs", RUN_NAME)
TMP = os.path.join(AT_DIR, ".run_newcards.tmp.html")
ROUND = 23

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---- 本轮新增卡（仅 ②上下级 / ③高管间，0 peer；10张全 NEW，URL 均经 dedup 校验未命中 index）----
# 关系档：③高管间 3 张（全二手）+ ②上下级 7 张（全二手）。填补空白：典礼执行SOP / 颁奖词撰写 / 线上典礼 / 内部表彰演出 / 即时奖金 / 价值观奖项 / 奖项品牌化 / 高端盛典制作 / 高管peer认可 / 高管团队内部认可。
CARDS = [
    {
        "emoji": "\U0001F3AC",
        "title": "颁奖典礼全流程 SOP 与避坑（全场景落地指南）",
        "cat": "典礼执行SOP",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "颁奖典礼全流程拆解：前期（定主题/时间避节假日/舞台尺寸/声光设备/嘉宾名单含颁奖者+获奖者+观众，奖杯奖状提前3天定制核名避错别字，LED主屏侧屏提前24h调试，麦克风4-6支专人切音效）；现场（签到分VIP/普通区、胸卡颜色分区、暖场回顾视频、灯光秀+开场视频+主持人3分钟、核心颁奖按「从次要到重要」排序、颁奖词≤40秒+获奖者VCR30秒+礼仪引导+合影站位嘉宾左获奖者右+感言1-2分钟、每3-4奖穿插5分钟表演）；应急（LED黑屏切备用投影+主持人互动拖延、嘉宾迟到调顺序、超时压感言删非核心）；后期24h内发回顾推文+获奖故事专访。",
        "how": "办员工颁奖典礼，学这套「全场景落地SOP」：前期把奖杯姓名/设备/流程彩排（提前1天全流程彩排）做到位，现场按「次要→重要」排奖防开场即高潮，每个颁奖环节控时（词40秒+VCR30秒+感言≤2分），备应急方案；后期24h内出回顾传播延长荣誉感。把「流程不翻车」当第一KPI。",
        "url": "https://www.xunmei365.com/ask/3635783.html",
        "note": "适用：② 行政/HR/活动执行（中文实操指南二手；物料+人员+彩排+应急+后期传播全链路，可作颁奖典礼执行checklist）。",
    },
    {
        "emoji": "\u270D\uFE0F",
        "title": "颁奖词撰写方法论（点题-叙事-升华 + 真诚/画面/温度）",
        "cat": "颁奖词撰写",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "颁奖词撰写核心技巧：①结构「点题-叙事-升华」三层——开头点题（「[姓名/团队]以……荣获[奖项]」快速聚焦）、中间叙事（具象场景+数据化成果还原事迹，避免空话）、结尾升华（提炼精神内核关联企业价值观）；②语言「真诚感+画面感+温度感」三重质感——拒绝「该员工/此团队」冰冷称谓改用「他/她/他们」、善用「加班时的咖啡渍/调研时的泥泞鞋」等细节、朴素词汇传递认可；③内容「岗位特质+独特事迹+精神内核」三维——销售突出业绩突破客户信任、技术突出创新攻坚、服务突出温度解决问题，避开「努力认真」通用词聚焦「别人没做过/克服的特殊困难」。",
        "how": "写颁奖词，套「点题-叙事-升华」结构：开头一句话点荣誉归属，中间用具体场景+数据讲事迹（不写空话），结尾升华成团队精神坐标；语言上弃用「该员工」改「她/他们」、加细节画面、用朴素真诚词；按岗位特质写独特事迹而非套话。让颁奖词成为「成长的勋章，精神的火种」。",
        "url": "https://www.renrendoc.com/paper/507458683.html",
        "note": "适用：② 行政/HR/主持人/直属上级（文档模板二手；三层结构+三质感+三维度，可作颁奖词撰写方法论与范文库）。",
    },
    {
        "emoji": "\U0001F4BB",
        "title": "虚拟/线上颁奖典礼设计与观众体验",
        "cat": "线上典礼",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "虚拟颁奖典礼设计：先定目标（提振士气/品牌/筹款不可混在一个小时）与成功指标（直播观看率/提名量/聊天参与/回放/分享/下轮参与）。格式五选一：直播主持/杂志式（预录+直播intro）/社区秀（获奖故事+投票）/团队庆祝（经理带头 shout-out+里程碑）/混合异步（先发交互荣誉页再短直播）。观众体验设计＞run of show：开场投票、peer recognition 弹幕、观众票选 bonus 奖、30秒提前录感言、 spotlight 幻灯片、会后可下载证书/徽章。内容包：每人姓名职务照+奖项+一句 citation+短简介+引言可分享图+永久荣誉页。技术排练至少一次（纠发音/lower-third/冷场/死链）。",
        "how": "做线上/混合颁奖，先定单一主目标再选格式（远程团队优先「混合异步」最可持续：先发荣誉页再短直播讲故事）；把精力放观众每5分钟在做什么（投票/弹幕/票选bonus）；给每人建永久荣誉页（仪式造 moment、页面存记忆）；至少一次全要素技术排练。避免把士气活动当品牌宣讲。",
        "url": "https://successes.live/virtual-awards-ceremony-ideas",
        "note": "适用：② 行政/HR/雇主品牌（虚拟活动指南二手；格式五选一+观众体验设计+永久荣誉页，可作远程/混合颁奖方案）。",
    },
    {
        "emoji": "\U0001F3AD",
        "title": "社内表彰式演出设计 + 评选透明度（日本内行）",
        "cat": "内部表彰演出",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "日本社内表彰式运营要点：①演出设计——主题与着装统一（「晚宴/奥斯卡风/白金统一」）造非日常一体感，每年换主题提期待；MC 在获奖者演讲前介绍 episode 再「请一言」引共鸣；副赏（奖品）用「开封演出/MC吊胃口/全员聚焦瞬间」放大价值，选「选择制礼物/体验型礼品」胜固定商品券；②评选透明度——定量的（达成率/件数/满意度）与定性的（团队合作/价值观体现/客户贡献）组合多面标准，事前全社周知，防「为什么是他」的不信感；③实时投稿——式典样子上 Slack/Teams 实时发「姓名+理由+本人评论」，stamps 可视化赞赏，式后定期发「获奖者一覧/访谈」使表彰文化浸透。",
        "how": "办社内表彰式，学日本这套：先立「评选标准透明性」（定量+定性组合、事前全社周知）再谈演出华丽；主题/着装统一造一体感；MC 先讲获奖 episode 再请发言引共鸣；副赏用开封演出+选择制体验礼品放大记忆；式后把获奖者一覧/访谈定期发，让表彰文化落地。把「谁因什么被评」的设计质量放第一位。",
        "url": "https://jp.vcube.com/eventdx/blog/internal-awards-ideas-and-benefits",
        "note": "适用：② 行政/HR/总务（日本服务商二手；评选透明+演出设计+实时投稿，可作内部表彰式运营范式）。",
    },
    {
        "emoji": "\u26A1",
        "title": "Spot Bonus 即时奖金项目落地（6周启动+审计+指标）",
        "cat": "即时奖金",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "Spot Bonus（即时奖金）落地指南：定义=对超额/短期目标达成给的即时非经常性现金奖励，胜在「即时」。4-6周启动：W1定资格/预算/审批流/金额上下限；W2对接薪酬财务设支付与税务；W3建短提名表（姓名+事迹+业务影响+建议金额）+HRIS追踪；W4培训经理「什么该奖/怎么写认可话术」；W5全员宣发+2-3范例；W6激活+90天复盘。防偏见：哈佛肯尼迪研究指经理更倾向奖「像自己」的人，须季度按人口统计审计分布+每奖书面理由留痕。效果指标：经理使用率/从成就到支付时长/分布公平性/敬业度相关。注意「即时」——走最近一次薪资而非季末，延迟即失意义。",
        "how": "推即时奖金，学 hyring「6周落地+季度审计」：先定清晰可观察的获奖行为（非「团队协作」空话）与分层金额；流程极简（经理填几句+24-48h审批）保「即时」；季度按团队/层级/人口统计审计分布防偏见+每奖留书面理由；90天复盘使用率与敬业度相关。避免用 off-cycle 支付难而改预付礼品卡桥接（仍走税）。",
        "url": "https://hyring.com/free-hr-toolkit/hr-glossary/spot-bonus",
        "note": "适用：② 薪酬/HR/一线经理（HR glossary 二手；6周启动+偏见审计+效果指标，可作 spot bonus 项目设计手册）。",
    },
    {
        "emoji": "\U0001F3C6",
        "title": "价值观驱动的文化奖项设计（10类命名+落地）",
        "cat": "价值观奖项",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "价值驱动文化奖项：传统「月度员工」易变人气竞赛致挫败，应改为对齐核心价值的 peer 提名奖（如 Zappos 月度 Culture Champion 同事互提）。10个可抄奖项：客户冠军/简化者/无畏反馈/桥梁建设者/创新火花/成长催化剂/共情贡献者/韧性精神/正直图标/社区连接者——每个绑定一个常见价值观（客户痴迷/效率/透明/协作/创新/学习/同理/韧性/诚信/归属）。落地 mini-guide：①清晰定义价值；②每个价值设具体可观察行为；③peer 提名+经理背书；④季度颁+故事化呈现；⑤公开标准防「黑箱」。价值奖让「被认可的行为」=公司想要的文化。",
        "how": "设计文化奖项，学 junoschool「价值绑定+peer提名」：先列公司核心价值，每个价值对应一个具名奖项（如「桥梁建设者」=协作），标准写「具体可观察行为」而非空话；用同事互提+经理背书保公平与信；季度颁+讲故事让价值「被看见」。用价值奖替代「月度员工」避免人气竞赛。",
        "url": "https://junoschool.org/article/company-culture-award-ideas",
        "note": "适用：② 文化/HR/People Ops（教育机构二手；10类价值奖项+Zappos案例+落地guide，可作文化奖项设计弹药库）。",
    },
    {
        "emoji": "\U0001F3A8",
        "title": "员工奖项与品牌价值对齐（语言/标准/体验/美学）",
        "cat": "奖项品牌化",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "员工奖项与品牌对齐四要素：①语言——奖项名即身份工具，用「The Builder/Connector/Trailblazer」替代「月度员工」映射品牌个性；②标准——奖励映射价值观的行为（重团队就不奖孤胆英雄，重客户就突出超越预期的服务故事），清晰标准消歧义；③体验——认可 moment 要 on-brand（领导个性化便条+关联价值的故事+绑定文化仪式的公开时刻），奖是体验非交易；④美学——品牌高端则奖与包装高端、品牌活泼则设计带能量，定制包装与惊喜感造可展示的纪念。常见坑：通用礼品卡显交易感、忽视个体偏好、团队间不一致、奖项与内部信息矛盾（preach 创新却只奖安全可预测）。",
        "how": "把员工奖项做成「品牌延伸」，学 inchcreative 四要素：命名用映射品牌个性的称号（非「月度员工」）；标准写清「哪些行为体现哪条价值」；认可时刻 on-brand（领导手写便条+价值故事+文化仪式）；美学匹配品牌（高端/活泼）。避免通用礼品卡交易感与团队间不一致侵蚀信任。让奖项成为文化信号而非日历任务。",
        "url": "https://inchcreative.com/employee-awards-brand-values",
        "note": "适用：② 雇主品牌/HR/市场（创意机构二手；四要素+品牌原型奖项示例+避坑，可作奖项品牌化设计参考）。",
    },
    {
        "emoji": "\U0001F387",
        "title": "高端企业颁奖盛典制作全指南（制作占预算25-35%）",
        "cat": "高端盛典制作",
        "rel": "r3", "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "高端企业颁奖盛典制作指南：定义 6-12 个有意义奖项类别（反映真实成就非头衔，拉部门头参与设计增 ownership）；场地需支持舞台/AV/坐席用餐/酒会，留 8h 搭建彩排、内置 rigging/黑场/音响；制作是记忆点——专业灯光设计、高质音响、品牌舞台、LED 播提名视频/直播feed/赞助LOGO、走台乐、摄影师/摄像；预算 25-35% 砸制作；running order pacing（酒会30分+开场+3个奖块各3-4奖+块间用餐+headline 娱乐+闭场祝酒，单奖≤3-4分）；专业主持人（懂商务文化、warm/witty/professional、brief 公司文化与敏感话题）；餐饮（优雅但可高效上菜）；娱乐不抢戏、after-party 建关系。",
        "how": "办高管/客户级颁奖盛典，学 hoabinh「制作即记忆点」：奖项类别拉部门头共设增 ownership；预算 25-35% 投灯光/LED/音响/走台乐/摄影；running order 用「酒会+奖块+用餐+娱乐+祝酒」节奏、单奖≤4分；请懂商务文化的专业主持控场与敏感话题；餐饮优雅可高效上菜、after-party 养关系。把制作当战略投资而非成本。",
        "url": "https://hoabinh-group.com/en/award-ceremony-planning",
        "note": "适用：③ 高管/品牌/雇主品牌（高端活动公司二手；制作预算占比+running order+专业主持，可作高管级盛典制作范本）。",
    },
    {
        "emoji": "\U0001F91D",
        "title": "高管间相互认可·Peer Recognition 奖项机制（ORBIE/C-suite）",
        "cat": "高管peer认可",
        "rel": "r3", "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "高管间相互认可范式：ORBIE Awards 自1998由同行评审（peer-adjudicated）评选 CIO/CISO/CMO 等 C-level，提名来自同事与可信商业伙伴、终审由往届获奖者主导的独立同行评审，标准=领导力效能/行业与社区参与/驱动业务价值。近25年近5000决赛、800+获奖。核心不是「向下表彰」而是「peer 之间互相看见」——高管也被认可、被连接、被激励，fostering executive relationships 并 inspire 下一代领导者。对内的启发：可设「高管 peer 提名奖」，让 C-level 互提互评（如年度最佳跨界协作者/最敢挑战现状者），由同行而非 HR 定，增可信与关系。",
        "how": "设计高管相互认可，学 ORBIE「peer-adjudicated」：提名来自同事/商业伙伴、终审由往届得主同行评审（非HR/老板定），标准聚焦领导力效能与业务价值；对内可设「高管 peer 提名奖」让 C-level 互提互评，增可信与关系网。把高管认可从「向下发奖」升级为「peer 之间互相看见」。",
        "url": "http://orbiecircle.org/",
        "note": "适用：③ 高管/CHRO/董事会（奖项机构二手；peer-adjudicated 机制+高管关系网，可作高管相互认可制度参考）。",
    },
    {
        "emoji": "\U0001F4A1",
        "title": "高管团队内部认可·把成功写成「被理解」而非「被看见」（Leadership Spotlight）",
        "cat": "高管团队认可",
        "rel": "r3", "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "高管团队内部认可实践集：①Leadership Spotlight——每季度 highlight 一位领导，不用公开奖杯/泛泛赞，而是个性化叙述：与本人走查「哪些决策/在场/情商改变了项目轨迹」，再短文字版向 broader org 分享供学习，让人「被理解」而非仅「被看见」；②Alps chalet 信任冒险——把领导团队请进私人空间（冰泳/via ferrata/夜滑/炉边 peer recognition），深友谊与共享故事超办公室；③即时庆祝——有人砸大单立刻停下手头全员 loud 庆祝；④sticky note——在桌上留具体行为+为何重要的便利贴，人留着、互留、信任长。核心：认可过程/心态/情商而非仅结果指标，personal/timely/sincere。",
        "how": "认可高管团队，学 CEO Mag「过程＞结果」：季度 Leadership Spotlight 用个性化叙述让人「被理解」（走查决策/情商如何改变轨迹再分享）；把领导团队请进私人空间做信任冒险+炉边 peer recognition；大赢立刻 loud 庆祝；sticky note 留具体行为。聚焦过程/心态/情商，personal+timely+sincere。",
        "url": "https://ceofficialmag.com/recognizing-leadership-celebrating-success-with-your-team",
        "note": "适用：③ CEO/高管团队/CHRO（高管杂志二手；Leadership Spotlight+信任冒险+即时庆祝+sticky note，可作高管团队内部认可心法）。",
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

# ---- 1) 写临时新卡块 ----
open(TMP, "w", encoding="utf-8").write("".join(card_html(c) for c in CARDS))
print("临时新卡块已写:", TMP)

# ---- 2) 墙注入 ----
html = open(CUM, encoding="utf-8").read()
before = html.count('<div class="hl">')
cards_sec3 = [c for c in CARDS if c["rel"] == "r3"]
cards_sec2 = [c for c in CARDS if c["rel"] == "r2"]
assert cards_sec3 and cards_sec2
i3 = html.find('class="sec sec3"')
close3 = find_grid_close(html, i3)
html = html[:close3] + "".join(card_html(c) for c in cards_sec3) + html[close3:]
i2 = html.find('class="sec sec2"')
close2 = find_grid_close(html, i2)
html = html[:close2] + "".join(card_html(c) for c in cards_sec2) + html[close2:]
# hero
hero_old = "二十一轮 enrich 2026-08-21(+6)"
hero_new = "二十一轮 enrich 2026-08-21(+6) ｜ 二十二轮 enrich 2026-08-22(+6) ｜ 二十三轮 enrich 2026-08-23(+10)"
assert hero_old in html, "hero marker not found"
html = html.replace(hero_old, hero_new, 1)
# recount
def recount(tagcls):
    s = html.find('class="' + tagcls + '"')
    e = html.find('class="sec', s + 10)
    return html[s:e].count('<div class="hl">') if e != -1 else html[s:].count('<div class="hl">')
r2n = recount('sec sec2'); r3n = recount('sec sec3')
html = re.sub(r'(<div class="sec sec3">.*?<span class="tag">)\d+', lambda m: m.group(1) + str(r3n), html, count=1, flags=re.S)
html = re.sub(r'(<div class="sec sec2">.*?<span class="tag">)\d+', lambda m: m.group(1) + str(r2n), html, count=1, flags=re.S)
open(CUM, "w", encoding="utf-8").write(html)
after = html.count('<div class="hl">')
r2b = html.count('badge r2'); r3b = html.count('badge r3')
b1b = html.count('badge b1'); b2b = html.count('badge b2')
footer_ok = "\U0001F4CC \u672c\u9875\u7531 yitong" in html
print("累计墙卡片数:", after, "(+", after - before, ") | r2:", r2b, "r3:", r3b, "| b1:", b1b, "b2:", b2b, "| footer:", footer_ok)
print("sec2 tag:", r2n, "sec3 tag:", r3n)

# ---- 3) 独立页（gen_run_page.py，显式 --out 防嵌套路径 bug）----
gen = os.path.join(BASE, "gen_run_page.py")
r = subprocess.run(["python", gen, "--topic", "award", "--topic-name",
                    "\u9881\u5956\u5178\u793c", "--date", DATE, "--round", str(ROUND),
                    "--cards-file", TMP, "--out", RUN_PATH], capture_output=True, text=True)
print("gen_run_page:", r.returncode, r.stdout.strip(), (r.stderr.strip()[:200] if r.stderr else ""))

# ---- 4) index.json ----
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
        "topic": "award",
    }
    data.append(entry); added += 1; existing_urls.add(u)
print("index.json 新增:", added, "-> 现", len(data), "条")
json.dump(data, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

# ---- 5) Obsidian 主题汇总笔记（newest-first：插到首个 ## 轮次 之前）----
VAULT = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库"
NOTE = os.path.join(VAULT, "素材", "award", "颁奖-知识卡汇总.md")
t = open(NOTE, encoding="utf-8").read()
# 摘要计数 共 131 张 -> 共 141 张
assert "共 131 张" in t, "摘要 131 marker not found"
t = t.replace("共 131 张", "共 141 张", 1)
round_section = (
    "\n## 轮次 2026-08-23（+10）\n\n"
    "本轮新增（均通过六维评估、仅 ②上下级 / ③高管间）：\n"
)
for c in CARDS:
    rel = "高管间" if c["rel"] == "r3" else "上下级"
    src = "一手" if c["src"] == "b1" else "二手"
    round_section += "- {0}（award.html） | {1} | {2}\n".format(esc(c["title"]), rel, src)
first_round = t.find("## 轮次")
assert first_round != -1
t = t[:first_round] + round_section + t[first_round:]
open(NOTE, "w", encoding="utf-8").write(t)
print("Obsidian 主题汇总笔记已插入本轮 round 段（newest-first）+ 摘要计数 131->141")

# ---- 6) 00-索引（更新计数行 + 轮次标记 + 追加卡行）----
IDX0 = os.path.join(VAULT, "00-知识采集索引.md")
i0 = open(IDX0, encoding="utf-8").read()
apos = i0.find("## 主题：颁奖")
assert apos != -1
# 计数行：125 卡 -> 141 卡（与累计墙对齐）
assert "**125 卡**" in i0, "125 卡 marker not found"
i0 = i0.replace("**125 卡**", "**141 卡**", 1)
# 轮次标记追加
marker_old = "二十二轮 enrich 2026-08-22(+6)"
marker_new = "二十二轮 enrich 2026-08-22(+6) ｜ 二十三轮 enrich 2026-08-23(+10)"
assert marker_old in i0, "round marker not found"
i0 = i0.replace(marker_old, marker_new, 1)
# append rows before next "## 主题：" (Open Day / 下午茶)
npos = i0.find("## 主题：", apos + 10)
assert npos != -1
rows = "".join(
    "| {0}（award/award.html） | 4 | {1} | {2} | {3} |\n".format(
        esc(c["title"]),
        "一手" if c["src"] == "b1" else "二手",
        "③高管间" if c["rel"] == "r3" else "②上下级",
        esc(c["cat"] + "：" + c["val"][:30]))
    for c in CARDS
)
i0 = i0[:npos] + rows + "\n" + i0[npos:]
open(IDX0, "w", encoding="utf-8").write(i0)
print("00-索引已更新（计数125->141+轮次+卡行）")

# ---- 7) 本轮独立笔记（runs/ 新建 md）----
os.makedirs(os.path.join(VAULT, "素材", "award", "runs"), exist_ok=True)
RUN_NOTE = os.path.join(VAULT, "素材", "award", "runs", "颁奖-2026-08-23-第二十三轮-知识卡.md")
n_r3 = sum(1 for c in CARDS if c["rel"] == "r3")
n_r2 = sum(1 for c in CARDS if c["rel"] == "r2")
rn = (
    "---\n"
    "title: 颁奖-2026-08-23-第二十三轮-知识卡\n"
    "type: 自动化采集\n"
    "date: 2026-08-23\n"
    "tags: [知识采集, 颁奖, 二十三轮]\n"
    "relation: [supervisor, exec]\n"
    "---\n\n"
    "# 颁奖典礼 · 第二十三轮补采（2026-08-23，+10）\n\n"
    "- **GitHub Pages 独立页**：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/runs/award-2026-08-23-r23.html\n"
    "- **本地路径**：`knowledge-collection/award/runs/award-2026-08-23-r23.html`\n"
    "- **累计卡片墙（总索引）**：`knowledge-collection/award/award.html`（[线上](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/award.html)）\n"
    "- **覆盖关系档**：③高管间 {0} 卡 / ②上下级 {1} 卡（无①平级）\n".format(n_r3, n_r2)
    + "- **乐享团队文件夹**：颁奖 子文件夹（f585d1b78510459db0ce807cc9688448，每轮独立页）\n\n"
    "## 本轮新增 10 卡\n\n"
    "| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n"
)
for c in CARDS:
    rel = "高管间" if c["rel"] == "r3" else "上下级"
    src = "一手" if c["src"] == "b1" else "二手"
    rn += "| {0} | {1} | {2} |\n".format(esc(c["title"]), rel, src)
rn += "\n> 本笔记仅索引，不拷 HTML 副本；完整卡片见上方 GitHub Pages 独立页。\n"
open(RUN_NOTE, "w", encoding="utf-8").write(rn)
print("本轮独立笔记已建:", RUN_NOTE)

# ---- 8) GitHub 同步 ----
sync = os.path.join(os.path.dirname(BASE), "sync_knowledge_github.py")
try:
    rs = subprocess.run(["python", sync], capture_output=True, text=True, timeout=300)
    print("sync_knowledge_github:", rs.returncode, (rs.stdout.strip()[-300:] if rs.stdout else ""), (rs.stderr.strip()[:200] if rs.stderr else ""))
except Exception as e:
    print("\u26a0\ufe0f GitHub 同步异常（告警不阻断）：" + str(e)[:200])

# ---- 9) 乐享上传（whoami 探活；award 新建每轮独立页 + best-effort 更新累计墙）----
MCP_JSON = r"C:/Users/v_yitcai/.workbuddy/mcp.json"
LEXIANG_URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"
FOLDER = "f585d1b78510459db0ce807cc9688448"  # award 子文件夹（待清洗素材下）

class LexiangMCP:
    def __init__(self, token):
        self.token = token; self.session = None
    def _post(self, payload, retries=3):
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

def put_bytes(url, data, retries=3):
    last = None
    for _ in range(retries):
        try:
            req = urllib.request.Request(url, data=data, method="PUT")
            req.add_header("Content-Type", "text/html")
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.status
        except Exception as e:
            last = str(e); continue
    raise RuntimeError("PUT fail: " + str(last))

try:
    token = json.load(open(MCP_JSON, encoding="utf-8"))["mcpServers"]["lexiang"]["headers"]["Authorization"]
    mc = LexiangMCP(token); mc.initialize(); mc.initialized()
    try:
        w = mc.call("whoami", {})
        print("whoami:", json.dumps(mc.biz(w), ensure_ascii=False)[:120])
    except Exception as e:
        print("whoami 跳过:", str(e)[:120])

    # best-effort 累计墙更新：列出 folder 子条目，找 award.html 墙条目
    try:
        lc = mc.call("entry_list_children", {"parent_id": FOLDER})
        biz_lc = mc.biz(lc)
        entries = biz_lc.get("data", {}).get("entries", []) if isinstance(biz_lc.get("data"), dict) else biz_lc.get("data", [])
        wall_entry = None
        for e in entries:
            nm = (e.get("name") or "").lower().replace(".html", "")
            if nm == "award" and e.get("type") in (None, "file", "FILE") or (e.get("extension") in ("html", "HTML")):
                if nm == "award":
                    wall_entry = e; break
        if wall_entry:
            wall_id = wall_entry.get("id") or wall_entry.get("entry_id")
            target = wall_entry.get("target") or {}
            file_id = target.get("id") or target.get("file_id") or wall_entry.get("file_id")
            if wall_id and file_id:
                wall_bytes = open(CUM, "rb").read()
                r = mc.call("file_apply_upload", {"file_id": file_id, "parent_entry_id": wall_id,
                                                  "name": "award.html", "extension": "html",
                                                  "mime_type": "text/html", "upload_type": "PRE_SIGNED_URL",
                                                  "size": str(len(wall_bytes))})
                biz = mc.biz(r)
                if biz.get("code") != 0:
                    raise RuntimeError("apply_upload(wall) FAIL " + str(biz.get("message")))
                sess = biz["data"]["session"]
                sid = sess.get("session_id") or sess.get("id")
                url = sess.get("upload_url") or sess["objects"][0]["upload_url"]
                st = put_bytes(url, wall_bytes)
                if st != 200: raise RuntimeError("PUT(wall) status " + str(st))
                r2 = mc.call("file_commit_upload", {"session_id": sid})
                biz2 = mc.biz(r2)
                if biz2.get("code") != 0: raise RuntimeError("commit(wall) FAIL " + str(biz2.get("message")))
                print("乐享累计墙更新 OK entry_id=", wall_id)
            else:
                print("乐享累计墙条目缺 file_id，跳过墙更新（仅建独立页）")
        else:
            print("乐享 folder 内未发现 award.html 墙条目，跳过墙更新（仅建独立页）")
    except Exception as e:
        print("\u26a0\ufe0f 乐享累计墙更新跳过（warning，不中断）：" + str(e)[:200])

    # 新建本轮独立页
    run_bytes = open(RUN_PATH, "rb").read()
    r = mc.call("file_apply_upload", {"parent_entry_id": FOLDER, "name": RUN_NAME,
                                      "extension":"html", "mime_type":"text/html",
                                      "upload_type":"PRE_SIGNED_URL", "size": str(len(run_bytes))})
    biz = mc.biz(r)
    if biz.get("code") != 0:
        raise RuntimeError("apply_upload(run) FAIL {0}".format(biz.get("message")))
    sess = biz["data"]["session"]
    sid = sess.get("session_id") or sess.get("id")
    url = sess.get("upload_url") or sess["objects"][0]["upload_url"]
    st = put_bytes(url, run_bytes)
    if st != 200: raise RuntimeError("PUT(run) status " + str(st))
    r2 = mc.call("file_commit_upload", {"session_id": sid})
    biz2 = mc.biz(r2)
    if biz2.get("code") != 0: raise RuntimeError("commit(run) FAIL " + str(biz2.get("message")))
    rid = biz2["data"]["entry"]["id"]
    print("乐享新建独立页 OK entry_id=", rid)
    mapf = json.load(open(os.path.join(BASE, "lexiang-entry-map.json"), encoding="utf-8"))
    sm = mapf.setdefault("award", {"folder_id": FOLDER, "rounds": []})
    sm["folder_id"] = FOLDER
    sm["rounds"].append({"date": DATE, "entry_id": rid, "name": RUN_NAME, "note": "轮次页 R23 (+10：典礼执行SOP/颁奖词撰写/线上典礼/内部表彰演出/即时奖金/价值观奖项/奖项品牌化/高端盛典制作/高管peer认可/高管团队内部认可)"})
    json.dump(mapf, open(os.path.join(BASE, "lexiang-entry-map.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("已回写 lexiang-entry-map.json")
except Exception as e:
    print("\u26a0\ufe0f 乐享上传跳过（warning，不中断）：" + str(e)[:300])

print("\n=== R23 完成：新增", added, "卡，墙现", after, "卡 ===")
