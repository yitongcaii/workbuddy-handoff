# -*- coding: utf-8 -*-
"""员工大会 二十四轮补采 (2026-08-23) — 渲染增量 + 追加进累计墙 + 更新 index.json + Obsidian + 乐享上传
仅 ②上下级 / ③高管间，0 peer。本论增量页 staff-meeting-2026-08-23-r24.html。"""
import json, os, re, subprocess, urllib.request, urllib.error

BASE = os.path.dirname(os.path.abspath(__file__))
AT_DIR = os.path.join(BASE, "staff-meeting")
CUM = os.path.join(AT_DIR, "staff-meeting.html")
IDX = os.path.join(BASE, "index.json")
DATE = "2026-08-23"
RUN_NAME = "staff-meeting-2026-08-23-r24.html"
RUN_PATH = os.path.join(AT_DIR, "runs", RUN_NAME)
TMP = os.path.join(AT_DIR, ".run_newcards.tmp.html")
ROUND = 24

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---- 本轮新增卡（仅 ②上下级 / ③高管间，0 peer；10张全 NEW，URL 均未命中 index/wall）----
# 关系档：②上下级 8 张（4 一手 + 4 二手）+ ③高管间 2 张（2 二手）
CARDS = [
    {
        "emoji": "\U0001F3AD",
        "title": "天津城投集团职工述能大会·沉浸式思政课堂",
        "cat": "职工述能",
        "rel": "r2", "rel_text": "上下级",
        "src": "b1", "src_text": "一手",
        "val": "天津城投集团举办职工述能大会决赛暨「津彩思政」优秀职工作品展演，创新打造沉浸式职工思政课堂，融合「职工述能风采展示+原创思政情景剧展演」双主线。9名一线职工登台讲奋斗故事（园林/城市智管/低空经济/数字化转型等赛道）；职工自编自导自演5部原创情景剧以小切口讲大担当；现场专业评委打分+职工大众投票，颁发语言类/情景类奖项表彰岗位先锋。150余人参与。集团工会以活动为样板常态化开展情景化、沉浸式职工思政教育。",
        "how": "办职工述能/故事大会，学天津城投「沉浸式思政+双主线」：一线职工登台讲真实奋斗故事 + 职工自编情景剧演身边事，用「小切口讲大担当」替代单向宣讲；现场评委+大众双投票即时表彰，把思政做成情感共鸣而非说教。适合国企把价值观落地成员工自己的舞台。",
        "url": "https://www.ftutj.cn/2026/06/30/90435.html",
        "note": "适用：② 集团工会/党建 × 一线职工（企业官网一手；沉浸式职工思政 + 奋斗故事+情景剧，可作国企价值观落地范本）。",
    },
    {
        "emoji": "\U0001F4F1",
        "title": "大庆钻探无纸化职代会·降本60%",
        "cat": "无纸化会议",
        "rel": "r2", "rel_text": "上下级",
        "src": "b1", "src_text": "一手",
        "val": "大庆钻探地质录井分公司第一届二次职代会推行「无纸化」会议，为101名代表配发专用平板电脑，所有议程、审议文件、表决事项经加密系统推送阅读。本次会议节省打印用纸超2万张及印刷耗材运输费，直接节约会议成本60%以上；材料实时零成本替换提升办会效率，更契合绿色低碳。代表感慨「清晰又环保」。工会将持续探索智慧工会建设，把省下的钱用于服务职工办实事、帮扶困难职工。",
        "how": "办职代会/职工大会，学大庆钻探「平板无纸化」：为代表配专用加密平板推送全部材料，省印刷费+提效率+绿色低碳；修改意见实时替换。把「过紧日子」落进办会细节，省下的经费反哺服务职工。适合国企降本+数字化双目标。",
        "url": "https://www.cinn.cn/2026/02-13/VDWYxdN1.html",
        "note": "适用：② 工会/行政 × 职工代表（中国工业新闻网报道一手；无纸化职代会降本60%+民主参与，可作绿色办会范本）。",
    },
    {
        "emoji": "\U0001F91D",
        "title": "中铁六局丰桥「永不闭幕的职代会」·联席会闭环",
        "cat": "职工代表联席会",
        "rel": "r2", "rel_text": "上下级",
        "src": "b1", "src_text": "一手",
        "val": "中铁六局丰桥公司工会召开职工代表联席会议，专题审议拟调整文件。技术/市场/行政/党群/后勤代表围坐逐条过筛，提修改建议12条、5条当场敲定纳入修订。这是「永不闭幕的职代会」机制常规动作：闭会期间涉及发展规划、重大经营调整、薪酬考核等必须提交联席会审议；一线设流动意见箱+线上「云履职」端口，想法当天直达决策层。搭建「征集—分类—交办—反馈—评议」全流程闭环，结果按月公示、接受无记名评议，优秀「金点子」年底表彰挂钩绩效。去年至今收建议52条、落地15条。",
        "how": "建「永不闭幕的职代会」，学丰桥「联席会+闭环」：职代会闭会期凡涉职工利益制度必交职工代表联席会逐条审议；线上线下收建议→当天分类建账→移交职能部门明时限→「首接盯办」→按月公示+无记名评议；金点子表彰挂钩绩效。把「坐着听文件」变「上手改文件」。",
        "url": "https://www.cnwomen.com.cn/2026/07/27/991333868.html",
        "note": "适用：② 工会主席/行政 × 职工代表（中国妇女网报道一手；联席会审议+五步闭环+云履职，可作民主管理长效范本）。",
    },
    {
        "emoji": "\U0001F4AC",
        "title": "浙江国贸资产青年建功大讨论·走心交流",
        "cat": "青年大讨论",
        "rel": "r2", "rel_text": "上下级",
        "src": "b1", "src_text": "一手",
        "val": "浙江国贸资产举办「青春建功十五五 我与企业共成长」青年员工创业建功大讨论。党委书记、董事长金彤，党委副书记、纪委书记、工会主席朱亚清等出席，18名青年代表围绕「战略解码、文化落地、角色转变」走心交流、畅所欲言。青年从「青春视角」提务实建议；集团团委书记以「墨水、汗水、活水」赠成长箴言；金彤作指导讲话提四点期望（讲政治/讲情怀/讲专业/讲担当）。打破传统会议模式，搭建青年与企业的深度沟通桥梁。",
        "how": "办青年员工大讨论，学浙江国贸资产「走心交流+领导在场」：一把手与青年代表围坐畅所欲言（非汇报式），围绕战略/文化/角色转变真问题；领导现场赠箴言+作期望讲话但不抢话。把青年沟通做成「企业↔青年」双向桥梁而非单向宣贯。",
        "url": "https://cnsoe.com.cn/df/zj/djhgs/content_144858.html",
        "note": "适用：② 党委书记/董事长 × 青年员工（国企网一手；青年建功大讨论+领导走心交流，可作青年沟通范本）。",
    },
    {
        "emoji": "\U0001F4BB",
        "title": "保利威企业大会直播·白名单+万人并发",
        "cat": "直播技术方案",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "保利威企业大会直播方案：千万级并发+超10000全球加速节点支撑集团万人同步在线；企业级白名单准入仅内部授权人员可进，从源头杜绝战略/经营内容外泄；评论敏感词屏蔽+违规禁言+优质评论上墙规范互动；一体化智能导播多机位/PPT/视频无缝切换；开放API对接OA/人事系统，自动签到打卡+导出观看时长/互动数据形成复盘闭环；福袋抽奖/有奖问答/红包雨提升参与。适配超大企业内部活动。",
        "how": "办大型员工大会直播，学保利威「私密+安全+数据闭环」：白名单限内部人员准入防泄密；弹幕敏感词屏蔽+优质评论上墙兼顾秩序与活跃；API对接OA自动签到+导出观看/互动数据做复盘；福袋抽奖提专注度。适合集团万人级大会的线上分发与效果度量。",
        "url": "https://www.polyv.net/news/%e4%b8%ad%e5%a4%a7%e5%9e%8b%e4%bc%81%e4%b8%9a%e5%a6%82%e4%bd%95%e9%ab%98%e6%95%88%e5%bc%80%e5%b1%95%e5%86%85%e9%83%a8%e7%9b%b4%e6%92%ad%ef%bc%9f%e5%85%a8%e5%91%98%e5%9f%b9%e8%ae%ad%e4%b8%8e%e4%bc%81",
        "note": "适用：② 行政/IT × 全体职工（服务商方案二手；白名单安全+万人并发+数据闭环，可作大型内部直播技术选型参考）。",
    },
    {
        "emoji": "\U0001F39E",
        "title": "摄行科技混合会议直播·多机位双向互动",
        "cat": "混合会议直播",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "摄行科技混合会议方案：2-4机位覆盖全景/讲台特写/观众反打/游机，导播实时切换具电视级体验；双向互动系统——线上提问审核后投影现场大屏、主持人选择性回答，支持在线投票/弹幕；专业调音台统一现场与线上音频，线上语音提问经返送接入现场音响实现双向语音互通；专线+5G聚合+卫星三重网络冗余保障不中断。适用企业全员大会、经销商大会等需同时覆盖线下线上场景。",
        "how": "办混合全员大会，学摄行「多机位+双向互动+网络冗余」：线下线上同体验——线上提问投屏+语音返送现场；多机位导播让远程有电视感；三重网络冗余防掉线。核心是让线上观众「在场」而非看录播。适合总部年会覆盖海外分公司。",
        "url": "https://www.720sjz.com/cases/meeting-live/qi-ye-hun-he-hui-yi-zhi-bo.html",
        "note": "适用：② 行政/直播执行 × 全体职工（服务商案例二手；混合会议多机位双向互动，可作线下+线上同体验技术范本）。",
    },
    {
        "emoji": "\U0001F5E3\uFE0F",
        "title": "为什么大家讨厌你的 Town Hall·匿名Q&A+脉冲",
        "cat": "匿名Q&A",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "RiLiFi 指出全员会最贵却常成60分钟领导独白。修复法：①「真正的Q&A」——会前数天匿名提交+投票，领导答硬问题（含匿名）信任飙升；②「脉冲检查」——实时投票「Q2路线图清晰度1-5分」，若2分当场停讲去解困惑，别等离职面谈；③「庆祝胜利」——用词云问「本月谁值得 shoutout」读出来是最佳士气 booster。结论：Town Hall 是给「镇上的人」不是只给「镇长」，把麦克风给群众。",
        "how": "救活全员会，学 RiLiFi「匿名Q&A+脉冲+庆祝」三板斧：会前开匿名提问通道并投票排序，领导当众答最难的（含匿名）；用1-5脉冲投票实时测清晰度，低分当场停讲去解；结尾词云 shoutout 读名字庆祝。把独白变双向对话，信任自然来。",
        "url": "https://rilifi.com/blogs/why-everyone-hates-your-town-hall-and-how-to-fix-it",
        "note": "适用：② 内部沟通/HR × 全体职工（服务商博客二手；匿名Q&A+脉冲检查+庆祝胜利，可作全员会互动急救范本）。",
    },
    {
        "emoji": "\U0001F4A1",
        "title": "创意员工沟通·直播体验+虚拟焦点小组",
        "cat": "创意沟通",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "Connected Company 提出季度数字全员会要「互动非幻灯片」：建直播Q&A（聊天提交问题）+实时投票测情绪（「对2026路线图多有信心」）+匿名提交保护心理安全；变换形式——跨职能小组讨论面板、Ask the CEO Anything 无脚本、项目负责人的聚光灯访谈；虚拟焦点小组8-10人深挖调研结果，会前发脉冲调研定主题、会后10工作日内回主题摘要并明说什么变/不变。闭环失败是多数组织通病，用「You asked, we answered」显式回应。",
        "how": "设计员工沟通，学 Connected Company「直播体验+焦点小组+闭环」：季度数字全员会配匿名Q&A+实时情绪投票；变形式为跨职能面板/CEO无脚本AMA/负责人访谈；虚拟焦点小组8-10人深挖；会后10天内回摘要并明确「什么变/什么不变」。关键是闭环显式回应（「你问了我答了」）。",
        "url": "https://connectedcompany.app/blog/creative-ways-to-communicate-with-employees/",
        "note": "适用：② 内部沟通 × 全体职工（咨询博客二手；季度数字全员会+虚拟焦点小组+闭环回应，可作沟通组合拳范本）。",
    },
    {
        "emoji": "\U0001F9E9",
        "title": "24Frames 分层全员会·中枢+功能breakout",
        "cat": "分层全员会",
        "rel": "r3", "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "24 Frames Digital 提出2026全员会新形态「分层 townhall」：中央 all-hands 设定整体方向，更小功能 breakout 给团队空间谈「信息对自己日常意味着什么」，尊重时间、让沟通更可行动，也打开更坦诚讨论（文化对齐真发生处）。配套：领导用大白话讲context（为什么决策、对人意味什么）而非数字堆砌；故事驱动townhall（员工/团队活现价值观）；混合多地点让区域/远程同等可见被听；会前收问题反馈让领导答真关切。技术退后、信息不抢戏。",
        "how": "设计高管主导全员会，学 24Frames「分层townhall」：中央场定方向 + 小功能breakout谈落地，尊重时间又打开坦诚；领导讲context大白话、故事驱动、混合平权、会前征题。把全员会从「日历义务」变「文化投资」。适合多地点/混合组织。",
        "url": "http://24framesdigital.com/Strategic-Townhall-Formats-to-Improve-Employee-Culture-in-2026.html",
        "note": "适用：③ 高管/内部沟通负责人（服务商博客二手；分层townhall+功能breakout，可作多地点全员会架构范本）。",
    },
    {
        "emoji": "\U0001F3AC",
        "title": "PRmoment Oprah·像电视制片人设计全员会",
        "cat": "受众中心设计",
        "rel": "r3", "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "PRmoment 借 Oprah 经验重思全员会：伟大沟通始于懂受众。五招：①从员工真想听的开始——用 listening/pulse 定议程而非领导想说的；②别做成CEO秀——引入不同领导/专家/客户声/员工故事，反映整个组织非仅顶层；③像电视制片人——每几分钟换节奏/形式/声音维持注意力（尤其远程）；④让远程员工成为体验一部分——平等提问/投票/讨论并全程致谢非仅最后5分钟；⑤衡量成功——看员工记住/学到/后续聊了什么、是否更知情连接自信，而非仅出勤。",
        "how": "重塑全员会，学 PRmoment「像电视制片人」：用员工聆听定议程（非领导议程）；多声音上台（专家/客户/员工故事）破CEO秀；每几分钟换节奏保注意力；远程全程平等参与并致谢；以「记住/连接/自信」衡量非仅出勤。把日历邀约变真想参加。",
        "url": "https://www.prmoment.com/internal-comms/what-would-oprah-do-lessons-for-internal-communicators-on-re-thinking-the-town-hall",
        "note": "适用：③ 内部沟通负责人/高管（行业媒体二手；受众中心+电视化分段+远程平权，可作全员会体验设计范本）。",
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

# ---- 1) 写 .run_newcards.tmp.html（Step 6 临时块）----
open(TMP, "w", encoding="utf-8").write("".join(card_html(c) for c in CARDS))
print("临时新卡块已写:", TMP)

# ---- 2) 墙注入（Step 6 累计墙）----
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
hero_old = "2026-08-22（第二十三轮补采 +10）"
hero_new = "2026-08-23（第二十四轮补采 +10）"
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

# ---- 3) 独立页（Step 6.5：gen_run_page.py）----
gen = os.path.join(BASE, "gen_run_page.py")
r = subprocess.run(["python", gen, "--topic", "staff-meeting", "--topic-name",
                    "\u5458\u5de5\u5927\u4f1a", "--date", DATE, "--round", str(ROUND),
                    "--cards-file", TMP], capture_output=True, text=True)
print("gen_run_page:", r.returncode, r.stdout.strip(), (r.stderr.strip()[:200] if r.stderr else ""))

# ---- 4) index.json（Step 5/7）----
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
        "topic": "staff-meeting",
    }
    data.append(entry); added += 1; existing_urls.add(u)
print("index.json 新增:", added, "-> 现", len(data), "条")
json.dump(data, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

# ---- 5) Obsidian 主题汇总笔记（Step 7① 追加本轮 round 段）----
VAULT = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库"
NOTE = os.path.join(VAULT, "素材", "staff-meeting", "员工大会-知识卡汇总.md")
t = open(NOTE, encoding="utf-8").read()
round_section = (
    "\n## 轮次 20260823（二十四轮补采 +10）\n\n"
    "| 卡 | 适用关系 | 一手/二手 |\n"
    "|---|---|---|\n"
)
for c in CARDS:
    rel = "高管间" if c["rel"] == "r3" else "上下级"
    src = "一手" if c["src"] == "b1" else "二手"
    round_section += "| {0}（staff-meeting.html） | {1} | {2} |\n".format(esc(c["title"]), rel, src)
assert "## 轮次 20260822（二十三轮补采 +10）" in t
t = t.rstrip("\n") + "\n" + round_section
open(NOTE, "w", encoding="utf-8").write(t)
print("Obsidian 主题汇总笔记已追加本轮 round 段")

# ---- 6) 00-索引（Step 7② 更新轮次头 + 计数 + 追加卡行）----
IDX0 = os.path.join(VAULT, "00-知识采集索引.md")
i0 = open(IDX0, encoding="utf-8").read()
hdr_old = "\u4e8c\u5341\u4e09\u8f6e\u8865\u91c7 2026-08-22\uff08+10\uff09\uff09"
hdr_new = "\u4e8c\u5341\u4e09\u8f6e\u8865\u91c7 2026-08-22\uff08+10\uff09\uff5c \u4e8c\u5341\u56db\u8f6e\u8865\u91c7 2026-08-23\uff08+10\uff09\uff09"
assert hdr_old in i0, "00-index header marker not found"
i0 = i0.replace(hdr_old, hdr_new, 1)
if "**258 卡**" in i0:
    i0 = i0.replace("**258 卡**", "**268 卡**", 1)
# append rows before next "## 主题：" (Offsite)
apos = i0.find("## 主题：员工大会")
npos = i0.find("## 主题：", apos + 10)
assert npos != -1
rows = "".join(
    "| {0}（staff-meeting.html） | 4/5 | {1} | {2} | {3} |\n".format(
        esc(c["title"]),
        "一手" if c["src"] == "b1" else "二手",
        "③高管间" if c["rel"] == "r3" else "②上下级",
        esc(c["cat"] + "：" + c["val"][:40]))
    for c in CARDS
)
i0 = i0[:npos] + rows + "\n" + i0[npos:]
open(IDX0, "w", encoding="utf-8").write(i0)
print("00-索引已更新（轮次头+计数+卡行）")

# ---- 7) 本轮独立笔记（Step 7③ runs/ 新建 md）----
os.makedirs(os.path.join(VAULT, "素材", "staff-meeting", "runs"), exist_ok=True)
RUN_NOTE = os.path.join(VAULT, "素材", "staff-meeting", "runs", "员工大会-2026-08-23-第二十四轮-知识卡.md")
n_r3 = sum(1 for c in CARDS if c["rel"] == "r3")
n_r2 = sum(1 for c in CARDS if c["rel"] == "r2")
rn = (
    "---\n"
    "title: 员工大会-2026-08-23-第二十四轮-知识卡\n"
    "type: 自动化采集\n"
    "date: 2026-08-23\n"
    "tags: [知识采集, 员工大会, 二十四轮]\n"
    "relation: [supervisor, exec]\n"
    "---\n\n"
    "# 员工大会 · 第二十四轮补采（2026-08-23，+10）\n\n"
    "- **GitHub Pages 独立页**：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/runs/staff-meeting-2026-08-23-r24.html\n"
    "- **本地路径**：`knowledge-collection/staff-meeting/runs/staff-meeting-2026-08-23-r24.html`\n"
    "- **累计卡片墙（总索引）**：`knowledge-collection/staff-meeting/staff-meeting.html`（[线上](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/staff-meeting.html)）\n"
    "- **覆盖关系档**：③高管间 {0} 卡 / ②上下级 {1} 卡（无①平级）\n".format(n_r3, n_r2)
    + "- **乐享团队文件夹**：员工大会子文件夹（a753a4ebc526495c9e9b2e2fb3cac314）\n\n"
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

# ---- 8) GitHub 同步（Step 7 末尾）----
sync = os.path.join(os.path.dirname(BASE), "sync_knowledge_github.py")
try:
    rs = subprocess.run(["python", sync], capture_output=True, text=True, timeout=300)
    print("sync_knowledge_github:", rs.returncode, (rs.stdout.strip()[-300:] if rs.stdout else ""), (rs.stderr.strip()[:200] if rs.stderr else ""))
except Exception as e:
    print("\u26a0\ufe0f GitHub 同步异常（告警不阻断）：" + str(e)[:200])

# ---- 9) 乐享上传（whoami 探活，不依赖连接器状态面板）----
MCP_JSON = os.path.expanduser("~/.workbuddy/mcp.json")
LEXIANG_URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"
FOLDER = "a753a4ebc526495c9e9b2e2fb3cac314"  # 员工大会子文件夹（待清洗素材下）
WALL_FILE_ID = "a1415122f8034d8d988fb06e41be44ac"
WALL_ENTRY_ID = "f3b5ea59395e49ca859f8726142742c2"

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

    # (a) 更新累计墙文件本体
    wall_bytes = open(CUM, "rb").read()
    r = mc.call("file_apply_upload", {"file_id": WALL_FILE_ID, "parent_entry_id": WALL_ENTRY_ID,
                                      "name": "staff-meeting.html", "extension":"html",
                                      "mime_type":"text/html", "upload_type":"PRE_SIGNED_URL",
                                      "size": str(len(wall_bytes))})
    biz = mc.biz(r)
    if biz.get("code") != 0:
        raise RuntimeError("apply_upload(wall) FAIL {0}".format(biz.get("message")))
    sess = biz["data"]["session"]
    sid = sess.get("session_id") or sess.get("id")
    url = sess.get("upload_url") or sess["objects"][0]["upload_url"]
    st = put_bytes(url, wall_bytes)
    if st != 200: raise RuntimeError("PUT(wall) status " + str(st))
    r2 = mc.call("file_commit_upload", {"session_id": sid})
    biz2 = mc.biz(r2)
    if biz2.get("code") != 0: raise RuntimeError("commit(wall) FAIL " + str(biz2.get("message")))
    print("乐享累计墙已更新 OK")

    # (b) 新建本轮独立页条目
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
    sm = mapf.setdefault("staff-meeting", {"folder_id": FOLDER, "wall": {}, "rounds": []})
    sm["folder_id"] = FOLDER
    sm["rounds"].append({"date": DATE, "entry_id": rid, "name": RUN_NAME})
    json.dump(mapf, open(os.path.join(BASE, "lexiang-entry-map.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("已回写 lexiang-entry-map.json")
except Exception as e:
    print("\u26a0\ufe0f 乐享上传跳过（warning，不中断）：" + str(e)[:300])

print("\n=== R24 完成：新增", added, "卡，墙现", after, "卡 ===")
