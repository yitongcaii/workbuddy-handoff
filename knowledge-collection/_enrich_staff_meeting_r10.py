# -*- coding: utf-8 -*-
import json, re, os, datetime

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "staff-meeting", "staff-meeting.html")
TMP = os.path.join(BASE, "staff-meeting", ".run_newcards.tmp.html")
IDX = os.path.join(BASE, "index.json")
NOTE = r"C:\Users\v_yitcai\Documents\Obsidian\知识采集库\素材\staff-meeting\员工大会-知识卡汇总.md"
IDX00 = r"C:\Users\v_yitcai\Documents\Obsidian\知识采集库\00-知识采集索引.md"
PORTAL = os.path.join(BASE, "index.html")
RUNS_NOTE = r"C:\Users\v_yitcai\Documents\Obsidian\知识采集库\素材\staff-meeting\runs\员工大会-2026-08-11-第十轮-知识卡.md"
TODAY = "2026-08-11"

# ---------- 1. 提取现有卡片（按区域）----------
html = open(HTML, encoding="utf-8").read()

def extract_cards(block):
    cards = []
    tokens = list(re.finditer(r'<div\b|</div>', block))
    i = 0
    while i < len(tokens):
        if tokens[i].group() == '<div' and block[tokens[i].end():tokens[i].end()+30].startswith(' class="hl"'):
            depth = 0; end = i
            for t in range(i, len(tokens)):
                if tokens[t].group() == '<div': depth += 1
                else: depth -= 1
                if depth == 0:
                    end = t; break
            start = tokens[i].start(); stop = tokens[end].end()
            cards.append(block[start:stop]); i = end + 1
        else:
            i += 1
    return cards

i3 = html.index('<div class="sec sec3">')
sec2 = html.index('<div class="sec sec2">')
g3_start = html.index('<div class="grid">', i3)
g2_start = html.index('<div class="grid">', sec2)
footer_pos = html.index('<footer>')

three_region = html[g3_start:sec2]
two_region = html[g2_start:footer_pos]

existing_three = extract_cards(three_region)
existing_two = extract_cards(two_region)
print("existing ③:", len(existing_three), "existing ②:", len(existing_two))

# ---------- 2. 本轮 12 张新卡（④高管间 4 / ②上下级 8）----------
def card(emoji, title, cat, rel, src, val, how, url, disp, note, score):
    rel_label = "高管间" if rel == "r3" else "上下级"
    src_label = "一手" if src == "b1" else "二手"
    return dict(emoji=emoji, title=title, cat=cat, rel=rel, rel_label=rel_label,
                src=src, src_label=src_label, val=val, how=how,
                url=url, disp=disp, note=note, score=score)

NEW = [
 # ③ 高管间 (4)
 card("🎬","CEO Town Hall 45分钟执行脚本（Everywow·2026）","CEO议程SOP","r3","b2",
   "2026 CEO Town Hall 实操脚本：0-5min 主持 framing(为什么开+提问规则)/5-15min CEO 用大白话讲 context(变了什么·为什么)/15-25min 业务或领导更新(至多1个辅助声音)/25-40min 主持 moderated Q&A/40-45min CEO 收尾(现在什么重要·下一步·未答问题去哪)。强调：简报 CEO(每人1个必落地信息+1个最难问题)；Q&A 用匿名书面提问防 cosmetic；规划 live/hybrid/replay/无障碍(审校字幕)与指标(到场/观看时长/回放/提问量/跟进动作/经理反馈)。",
   "给 CEO 每人定『1必落地信息+1最可能难题』再砍多余；大场用主持读匿名书面提问(非开放麦防噪音)；决定录制/字幕/经理级联简报/未答书面回复四件事再办会；按观看时长与提问量而非仅到场率衡量。",
   "https://www.everywow.ch/en/2026/05/how-to-run-a-ceo-town-hall/",
   "everywow.ch/en/2026/05/how-to-run-a-ceo-town-hall",
   "③ CEO/高管 Town Hall 的 45 分钟分镜与「主持读匿名书面提问+录制/字幕/经理级联」四件事先决(防形式主义、跨时区可达)。",5),
 card("🎤","标杆公司 All-Hands 实操·嘉宾+分段AMA+多场（Tim's Playbook）","标杆实践","r3","b2",
   "从做得好的公司提炼：①请外部/跨界嘉宾就业务焦点演讲并开放提问(Clearco 评价最高环节)②把 AMA 从主 presentation 拆出来单独成段(Humi 甚至会后一周再开两场 AMA：一场业务产品、一场人&文化)，避免赶场、让人有时间想问题③跨国远程开第二场同内容 All-Hands(国际员工本就缺 context，不给等同发信号『你不重要』)④文化『特殊酱汁』(Top Hat 每周员工策展歌单/Motley Fool 月度 Fool's Errand 抽奖)让大会有记忆点。",
   "把 AMA 与主演讲物理分离(甚至延后一周双场)；远程跨时区必开第二场同内容；每届找一个轻量『文化专属动作』(歌单/抽奖/故事)强化认同；嘉宾话题对齐业务焦点并留足提问。",
   "https://www.timsplaybook.com/p/how-to-run-a-great-all-hands-meeting",
   "timsplaybook.com/p/how-to-run-a-great-all-hands-meeting",
   "③ 高管/内部沟通从标杆公司学『AMA 分段+跨国双场+文化专属动作』，把全员会做成有记忆点的双向流。",4),
 card("📣","反向 Town Hall·员工定议程+影子董事会（Review.jobs）","员工心声","r3","b2",
   "把 engagement 做成持续练习而非运动：季度级仪式用 reverse town hall(员工定议程、问想问的)、shadow board(员工顾问组直接影响战略与运营)、创新大赛(真落地)、peer recognition、async Q&A。核心闭环：听到→分析→行动→回贴(分享『听到什么/学到什么/要改什么』)，让员工见『发声真有结果』才强化反馈文化。节奏：周微活动+月一有意义事件+季一高影响仪式，聚焦 1-2 优先项 30-60 天。",
   "每季度开 reverse town hall(议程员工定)；设 shadow board 让年轻员工进战略对话；所有 engagement 活动后必做『听到→改了什么』闭环公告；用 5C(清晰/连接/贡献/选择/庆祝)锚定，按情绪与行为而非仅到场率衡量。",
   "https://review.jobs/blog/employee-engagement-ideas",
   "review.jobs/blog/employee-engagement-ideas",
   "③ 高管用 reverse town hall + shadow board 把『员工心声』制度化并闭环(发声真有结果才强化信任)。",4),
 card("👂","倾听四级模型·反向导师制（Francesco Pecoraro）","倾听文化","r3","b2",
   "领导倾听四阶段：①表演性(点头记笔记但心不变)②选择性(只听合己见/尊敬的)③开放性(真好奇、愿被影响)④变革性(把倾听建成流程/指标/文化)。反 mentor(年轻员工定期给高管分享视角)是让被淹没声音被听见的结构化机制；微软 Nadella 从 know-it-all→learn-it-all：脉冲调研+高管可见回应、任意员工向领导 pitch 的 hackathon、stay interview、把倾听效力纳入领导考核，七年间市值涨 500%+。小公司『倾听之旅』(领导无议程小范围听)半年离职降 68%。",
   "自测倾听阶段并请人反馈；重要讨论设 devil's advocate 与 steelman(最强形式复述异见)；把『倾听效力』纳入领导考核；推反向导师制(年轻员工教高管数字/GenZ视角)；领导做无议程『倾听之旅』小范围听。",
   "https://francescopecoraro.com/the-silent-crisis-when-voices-go-unheard",
   "francescopecoraro.com/the-silent-crisis-when-voices-go-unheard",
   "③ 高管用『倾听四级+反向导师+无议程倾听之旅』穿透层级听真实声音(微软 learn-it-all 案例)。",4),
 # ② 上下级 (8)
 card("🧰","办一场杀手级 All-Hands·三阶段AMA+无名英雄（Slido）","AMA机制","r2","b2",
   "Slido 自家 All-Hands 方法论：①新兵两真一假破冰猜谎②庆祝入职周年(凸显长期服务)③公开认可『无名英雄』(每人提名上月最帮自己的人，词云投屏)④透明开放 Q&A——CEO 主持 AMA 成信任工具。Q&A 三阶段：会前收集并投票(让领导备好难答、更民主)/会中 live AMA(最流行是 Ask Me Anything)/会后书面答剩余(M&S 写成文档发布或并入相关会)。收尾三件事：亮成绩对实数/公开认可能力者/留足问答。",
   "会前 4 天开 AMA 收集投票、主持做准备；会中允许匿名提问、主持按热度分组读；会后书面答剩余并群发；设『无名英雄』提名让后台贡献被看见；庆祝入职周年强化归属。",
   "https://blog.sli.do/how-to-organize-all-hands-meetings/",
   "blog.sli.do/how-to-organize-all-hands-meetings",
   "② 主持人/内部沟通用『三阶段 AMA(前收集/中 live/后书面)+无名英雄提名』把全员会做成透明信任场。",5),
 card("💬","Ask Me Anything 会话怎么做·主持与跟进（Slido）","AMA机制","r2","b2",
   "AMA 的本质是『承诺透明+赋权员工讲重要的事+给安全感』。准备是关键：会前 4 天开提问、监测并 dry run、写答案；难问题也有价值——不回避、走进提问者鞋里当学习机会。没全答案时就承诺会后查清(收购期数百问题大多无答案，但『人在场』本身保连接)。主持视角：提前开匿名提问最大化参与(全球分散不能 live 也不该被排除)；按 upvote 找热点、按主题分组(block of 3)问领导；尖锐问题『软化语气但保核心』。闭环：未答承诺跟进(邮件/Slack/内网)。",
   "AMA 提前 4 天开匿名收集+投票；主持按 upvote 与主题分组、尖锐问题软化语气保核心；leader 不知就承诺会后查并真的回；全球团队靠异步提问+录制不排斥任何人。",
   "https://blog.slido.com/ask-me-anything",
   "blog.slido.com/ask-me-anything",
   "② 主持人/领导用『提前匿名收集+按主题分组+软化尖锐+会后必跟进』把 AMA 做成安全感与透明度来源。",4),
 card("🗂️","高效 All-Hands 筹备·议程/混合公平/新人（ClickUp）","议程框架","r2","b2",
   "可消费信息规划：icebreaker/趣味问答定调→town hall 式公司更新→高管 AMA 开放提问→实时投票/Q&A。混合公平：远程与现场同体验(现场有 swag 则提前寄给远程，别让人掉队)。定时间照顾多时区(中国同事不愿半夜接电话→找多数可行窗口或轮换+录播)。沟通计划：先 survey 收集员工想要的(可能他们想要和 CEO 掏心而非 anniversary)而非邮件线程。议程结构：新面孔介绍→CEO 谈项目更新→各部门如何连使命→健康文化表彰→C-suite 开放 Q&A；每段标时长。技术：测视频/麦/投票工具。",
   "先发 survey 问员工想讨论什么再定议程；混合场远程与现场同权(提前寄 swag/轮换时段/给录播)；议程标每段时长(新人介绍/CEO更新/部门连使命/表彰/AMA)；会前测 AV 与互动工具。",
   "https://clickup.com/blog/all-hands-meeting",
   "clickup.com/blog/all-hands-meeting",
   "② HR/行政用『先 survey 定议程+混合同权+每段标时长+会前测 AV』把全员会筹备标准化。",4),
 card("🏅","表彰做成体验而非仪式·公平提名+多渠道放大（S:US CHRO）","表彰体验","r2","b2",
   "S:US 首席人力官：好表彰共享一个特质——被设计成『体验』而非『仪式』。三实践：①有目的设计(先定强化什么行为/受众/想被怎么谈论/怎么衡量；前线排班需多场次或混合)②公平包容提名(清晰标准+翻译/字幕/灵活时段；小培训委员会轮值；提前公布标准/时间/评审；2024 扩到 peer/自荐+首轮匿名，前台与夜班提名显著涨，荣誉更均衡)③日常文化延伸(次月多渠道发荣誉画像、经理工具包含 1:1 提示)。核心：过程不公则落地稀碎，公平才全员共参与。",
   "表彰前先定『强化行为+受众+衡量』；建正式提名(清晰标准/多语言/字幕/轮值委员会/提前公示)；扩 peer+自荐并首轮匿名减偏见；次月多渠道放大荣誉画像+给经理 1:1 谈资包。",
   "https://sus.org/instead-of-hosting-recognition-events-start-designing-experiences",
   "sus.org/instead-of-hosting-recognition-events-start-designing-experiences",
   "② HR/领导把表彰从『仪式』重做成『体验』：公平包容提名(peer+自荐+匿名)+次月多渠道放大。",5),
 card("📜","表彰日流程模板·环节时长+谁颁奖（VantageCircle）","表彰体验","r2","b2",
   "表彰日节目模板：领导开场→宣读个人颁奖词→peer recognition 时刻→文化反思(视频/现场故事)→公司致谢→团队活动/聚餐收尾。时长：团队级 45-90min；公司级 2-3h；虚拟最佳<75min(在线 60min 后注意力骤降)。环节间留 10min buffer(掌声/拍照/过渡)。避免像 HR Exercise：用具体故事而非类别(『Priya 救了 Harrington 客户』>『客户服务奖给 Priya』)；获奖者讲 60-90s；含 peer shout-out。颁奖人：可用的最资深领导(CEO/业务负责人)，按奖项类别映射(CEO 颁顶尖、VP 颁部门)。",
   "公司级表彰控 2-3h、虚拟控 75min 内、环节间留 buffer；领导致开场+宣读颁奖词、获奖者讲 60-90s、插 peer shout-out；颁奖人按类别映射(顶尖 CEO、部门 VP)，避免像行政流程。",
   "https://www.vantagecircle.com/recognition-templates/recognition-day-program-template/",
   "vantagecircle.com/recognition-templates/recognition-day-program-template",
   "② 行政/HR 用『表彰日时长红线(公司2-3h/虚拟<75min)+具体故事+资深领导颁顶尖奖』防形式化。",4),
 card("🏗️","中交一航局年终职工大会·全员提名奖项自创（一手官方）","表彰大会","r2","b1",
   "中交一航局一公司渤化码头项目部 2025 年终职工大会暨先进表彰会(一手官方复盘)：一改传统评优，首推『全员提名、奖项自创』民主评优——提前发多维度奖项参考库但鼓励职工突破框架、按身边真实贡献『量身定制』奖项并匿名提名(收 46 份，涌现『多面手/客户价值/最佳导师』等原创名)；为每位获奖者(尤其 7 位『品牌员工』)写个性化颁奖词(结合事迹勾勒立体画像)；设『优秀风尚→专项贡献→专业标兵→品牌员工』梯次荣誉进阶，覆盖基础奉献到顶尖标杆，激发『见贤思齐』内生动力；同时嘉奖先进集体强化『荣辱与共』。",
   "表彰前发奖项参考库但开放职工自创奖项+匿名提名(视角从管理转同事)；为获奖者写个性化颁奖词(结合事迹非罗列)；设梯次荣誉进阶(基础→专项→标杆→最高)兼顾覆盖与引领；个人+集体双表彰强化集体意识。",
   "https://www.cinn.cn/wh/2025/12-29/gDanmBpk.html",
   "cinn.cn/wh/2025/12-29/gDanmBpk.html",
   "② 企业官方一手：年终职工大会用『全员匿名提名+自创奖项+个性化颁奖词+梯次荣誉』把表彰做成团队文化洗礼。",5),
 card("📡","公司 Town Hall 直播三档配置·专业制作（Epiphan）","直播制作","r2","b2",
   "按公司规模与野心三档配直播：①简单连(webcam+会议软件，小团队/非正式)②看起来专业(硬件编码器+capture card+会议软件，中型企业多机位 polished)③承载大虚拟观众(硬件编码器+企业直播平台，支持数千观众，大型多办公室)。每档都须交互( Poll Everywhere/聊天/主持 Q&A，指派专人监 chat 喂问题)。关键警示：简陋制作会让远程员工感觉『被遗忘的 afterthought』，反伤参与——别用烂画质发错信号。硬件编码器可安全录制高清存内网回看，复用广(营销/销售赋能/培训)。",
   "按规模选档(小=会议软件/中=硬件编码器多机位/大=企业直播平台数千观众)；每档必配交互(投票/聊天/主持 Q&A+专人监 chat)；避免简陋制作伤远程归属感；用编码器安全录高清存内网复用。",
   "https://www.epiphan.com/blog/town-hall-meeting-live-stream/",
   "epiphan.com/blog/town-hall-meeting-live-stream",
   "② 行政/IT 用『三档直播配置(简单/专业/大观众)+必配交互+专人监 chat』让大型全员会远程可达不脱节。",4),
 card("🎥","2026 公司 Townhall 直播 7 步·电视级制作（2Stream）","直播制作","r2","b2",
   "2026 直播 7 步，把交互当『必做非可选』：预提交提问(会前 48-72h，不敢 live 讲的人会提前交，主持备答防冷场)/live 投票(每场≤2-3 个，多了稀释)/chat moderation(指定专人，CEO townhall 无 moderation 是风险)/按部门/地区 breakout(主会后续，协作+32%)/双语可及。制作像 live TV：show caller 同时管机位/字幕/讲者提示/流健康；远程讲者配 green room 防延迟混乱；townhall 超时伤信誉、show caller 管时长非 CEO；技术故障要有文档预案(65% 比利时企业用交互 webinar，内置 live 干预降掉线 40%)。掉线率是注意力真实指标。",
   "交互每场配具名负责人(预提问/投票≤3/chat moderation/breakout)；制作电视级(show caller 管机位字幕流健康+远程 green room+超时由 show caller 卡非 CEO)；主会后续按地区 breakout；技术故障走文档预案；以掉线率而非仅到场衡量。",
   "https://www.2stream.live/en/post/how-to-livestream-a-company-townhall-7-steps-for-2026",
   "2stream.live/en/post/how-to-livestream-a-company-townhall-7-steps-for-2026",
   "② 行政/直播团队用『交互具名负责人+电视级 show caller+地区 breakout+掉线率指标』把大型直播全员会做成真对话。",4),
]

def card_html(c):
    return (
        '    <div class="hl">\n'
        '      <div class="top"><span class="emoji">{emoji}</span><h3>{title}</h3>'
        '<span class="cat">{cat}</span><span class="badge {rel}">{rel_label}</span>'
        '<span class="badge {src}">{src_label}</span></div>\n'
        '      <p class="val">{val}</p>\n'
        '      <details class="exec"><summary>怎么做</summary><div class="inner">{how}</div></details>\n'
        '      <div class="src">🔗 <a href="{url}" target="_blank">{disp}</a></div>\n'
        '      <div class="note">适用：{note}</div>\n'
        '    </div>\n'
    ).format(**c)

new_three = [c for c in NEW if c["rel"] == "r3"]
new_two = [c for c in NEW if c["rel"] == "r2"]
print("new ③:", len(new_three), "new ②:", len(new_two))

# 写 .run_newcards.tmp.html（供 gen_run_page 消费）
open(TMP, "w", encoding="utf-8").write("\n".join(card_html(c) for c in NEW))
print("wrote tmp cards:", len(NEW))

all_three = existing_three + [card_html(c) for c in new_three]
all_two = existing_two + [card_html(c) for c in new_two]
n3, n2 = len(all_three), len(all_two)
print("total ③:", n3, "total ②:", n2, "grand:", n3 + n2)

# ---------- 3. 渲染 staff-meeting.html（整体重渲染）----------
head = html[:html.index('</head>') + 7]
def cats(cards_html):
    cs = re.findall(r'<span class="cat">([^<]+)</span>', cards_html)
    seen = []
    for c in cs:
        if c not in seen: seen.append(c)
    return " / ".join(seen)

three_cats = cats("\n".join(all_three))
two_cats = cats("\n".join(all_two))

new_html = head + "\n<body>\n<div class=\"wrap\">\n"
new_html += '<p style="margin:0 0 16px"><a href="runs/index.html" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">📑 查看本主题分页独立页 →</a></p>\n'
new_html += '  <div class="hero">\n'
new_html += '    <h1>🎤 员工大会 · 知识采集卡片墙</h1>\n'
new_html += '    <p>采集于 2026-08-11（十轮补采 +12）｜ 六维评估（含关系适配度）｜ 一手/二手标注 ｜ 历史去重 ｜ 受众关系分层（仅②上下级 / ③高管间）</p>\n'
new_html += '    <div class="relbar">\n'
new_html += '      <span>② 领导↔员工（上下级，supervisor）</span>\n'
new_html += '      <span>③ 领导↔领导（高管间，exec）</span>\n'
new_html += '    </div>\n'
new_html += '  </div>\n\n'
new_html += '  <div class="sec sec3">\n'
new_html += '    <h2>③ 领导↔领导（高管间 · exec）</h2>\n'
new_html += '    <span class="tag">%d 卡</span>\n' % n3
new_html += '    <span class="desc">%s</span>\n' % three_cats
new_html += '  </div>\n  <div class="grid">\n\n'
new_html += "\n".join(all_three) + "\n"
new_html += '  </div>\n\n'
new_html += '  <div class="sec sec2">\n'
new_html += '    <h2>② 领导↔员工（上下级 · supervisor）</h2>\n'
new_html += '    <span class="tag">%d 卡</span>\n' % n2
new_html += '    <span class="desc">%s</span>\n' % two_cats
new_html += '  </div>\n  <div class="grid">\n\n'
new_html += "\n".join(all_two) + "\n"
new_html += '  </div>\n\n'
new_html += '  <footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>\n'
new_html += '</div>\n</body>\n</html>\n'

tmp = HTML + ".tmp"
open(tmp, "w", encoding="utf-8").write(new_html)
os.replace(tmp, HTML)
print("wrote staff-meeting.html bytes:", len(new_html))

# ---------- 4. 更新 index.json (+12, 去重) ----------
data = json.load(open(IDX, encoding="utf-8"))
existing_urls = {x.get("url", "") for x in data}
added = 0
for c in NEW:
    if c["url"] in existing_urls:
        continue
    entry = {
        "title": c["title"],
        "normKey": c["title"],
        "url": c["url"],
        "sourceType": "primary" if c["src"] == "b1" else "secondary",
        "relation": "exec" if c["rel"] == "r3" else "supervisor",
        "summary": c["val"],
        "topic": "staff-meeting",
        "source": "web",
    }
    data.append(entry)
    existing_urls.add(c["url"])
    added += 1
json.dump(data, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("index.json added:", added, "total:", len(data))

# ---------- 5. 更新 Obsidian 笔记 ----------
GR = " | 4/5 | "  # 质量分列占位（00-索引用）
# 5a. 汇总笔记
note = open(NOTE, encoding="utf-8").read()
note = note.replace('本批 **84 卡**', '本批 **96 卡**')
note = note.replace('(2026-08-10 六轮补采 +11；2026-08-11 九轮补采 +11)',
                    '(2026-08-10 六轮补采 +11；2026-08-11 九轮补采 +11；2026-08-11 十轮补采 +12)')
note = note.replace('### ③ 领导↔领导（高管间 · exec）— 16 卡',
                    '### ③ 领导↔领导（高管间 · exec）— %d 卡' % n3)
note = note.replace('### ② 领导↔员工（上下级 · supervisor）— 68 卡（本表增量更新，全量 68 张见卡片墙 HTML）',
                    '### ② 领导↔员工（上下级 · supervisor）— %d 卡（本表增量更新，全量 %d 张见卡片墙 HTML）' % (n2, n2))

three_rows = ""
for c in new_three:
    three_rows += "| %s | %d | %s | ③高管间 | %s |\n" % (c["title"], c["score"], c["src_label"], c["note"].replace("③ ", ""))
two_rows = ""
for c in new_two:
    two_rows += "| %s | %d | %s | ②上下级 | %s |\n" % (c["title"], c["score"], c["src_label"], c["note"].replace("② ", ""))

note = note.replace('### ② 领导↔员工', three_rows + '\n### ② 领导↔员工', 1)
note = note.replace('## 适用与备注', two_rows + '\n## 适用与备注', 1)

# 新增本轮轮次小节（插在卡片墙 blockquote 之前）
round_block = (
    "\n## 轮次 20260811-r10（+12）\n\n"
    "| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n"
)
for c in NEW:
    rl = "③高管间" if c["rel"] == "r3" else "②上下级"
    sl = "一手" if c["src"] == "b1" else "二手"
    round_block += "| %s | %s | %s |\n" % (c["title"], rl, sl)
round_block += "\n"
note = note.replace('> 卡片墙 HTML：', round_block + '> 卡片墙 HTML：', 1)
open(NOTE, "w", encoding="utf-8").write(note)
print("updated note")

# 5b. 00-索引
idx00 = open(IDX00, encoding="utf-8").read()
idx00 = idx00.replace('**84 卡**（2026-08-09 五轮补采 +10；2026-08-11 九轮补采 +11）',
                       '**96 卡**（2026-08-09 五轮补采 +10；2026-08-11 九轮补采 +11；2026-08-11 十轮补采 +12）')
new_rows = ""
for c in NEW:
    rl = "③高管间" if c["rel"] == "r3" else "②上下级"
    sl = "一手" if c["src"] == "b1" else "二手"
    new_rows += "| %s（staff-meeting.html） | 4/5 | %s | %s | %s |\n" % (c["title"], sl, rl, c["note"].replace("③ ", "").replace("② ", ""))
idx00 = idx00.replace('## 主题：Offsite 团建务虚', new_rows + '\n## 主题：Offsite 团建务虚', 1)
open(IDX00, "w", encoding="utf-8").write(idx00)
print("updated 00-index")

# 5c. 当轮独立笔记（runs/）
runs_note = (
    "---\n"
    "title: 员工大会-2026-08-11-第十轮-知识卡\n"
    "type: 自动化采集\n"
    "date: 2026-08-11\n"
    "tags: [知识采集, 员工大会, 全员大会, townhall, all-hands, 十轮]\n"
    "relation: [supervisor, exec]\n"
    "---\n\n"
    "# 员工大会 · 第十轮补采知识卡（2026-08-11，+12）\n\n"
    "> 本轮独立页（GitHub Pages）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/runs/staff-meeting-2026-08-11-r10.html\n"
    "> 本地路径：`knowledge-collection/staff-meeting/runs/staff-meeting-2026-08-11-r10.html`\n"
    "> 累计总索引（卡片墙）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/staff-meeting.html\n\n"
    "## 本轮 12 张卡（③高管间 4 / ②上下级 8，按受众关系分层，剔除①平级/朋友向）\n\n"
    "| 卡 | 适用关系 | 一手/二手 | 一句话定位 |\n|---|---|---|---|\n"
)
for c in NEW:
    rl = "③高管间" if c["rel"] == "r3" else "②上下级"
    sl = "一手" if c["src"] == "b1" else "二手"
    runs_note += "| %s | %s | %s | %s |\n" % (c["title"], rl, sl, c["note"].replace("③ ", "").replace("② ", ""))
runs_note += "\n## 覆盖关系档与来源\n- ③高管间：CEO Town Hall 45分钟分镜 / 标杆公司 AMA 分段+跨国双场 / reverse town hall+shadow board / 倾听四级+反向导师。\n- ②上下级：三阶段 AMA+无名英雄 / AMA 主持跟进 / 高效筹备 survey+混合公平 / 表彰体验化 / 表彰日模板 / 中交一航局官方表彰案例(一手) / 直播三档配置 / 电视级直播制作。\n- 一手率：1/12（中交一航局官方年终职工大会表彰案例）；余 11 二手（Slido/ClickUp/VantageCircle/Epiphan/2Stream 工具官方 + S:US CHRO + Everywow/Tim's/Review.jobs/Francesco 权威方法论）。\n"
open(RUNS_NOTE, "w", encoding="utf-8").write(runs_note)
print("wrote runs note")

# ---------- 6. 更新门户 index.html (84 -> 96) ----------
portal = open(PORTAL, encoding="utf-8").read()
portal = portal.replace('<div class="cnt">84 卡</div>', '<div class="cnt">96 卡</div>')
open(PORTAL, "w", encoding="utf-8").write(portal)
print("updated portal")

print("DONE")
