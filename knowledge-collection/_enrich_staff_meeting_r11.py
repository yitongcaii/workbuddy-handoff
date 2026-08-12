# -*- coding: utf-8 -*-
import json, re, os, datetime

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "staff-meeting", "staff-meeting.html")
TMP = os.path.join(BASE, "staff-meeting", ".run_newcards.tmp.html")
IDX = os.path.join(BASE, "index.json")
NOTE = r"C:\Users\v_yitcai\Documents\Obsidian\知识采集库\素材\staff-meeting\员工大会-知识卡汇总.md"
IDX00 = r"C:\Users\v_yitcai\Documents\Obsidian\知识采集库\00-知识采集索引.md"
PORTAL = os.path.join(BASE, "index.html")
RUNS_NOTE = r"C:\Users\v_yitcai\Documents\Obsidian\知识采集库\素材\staff-meeting\runs\员工大会-2026-08-12-第十一轮-知识卡.md"
TODAY = "2026-08-12"

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

# ---------- 2. 本轮 11 张新卡（③高管间 5 / ②上下级 6）----------
def card(emoji, title, cat, rel, src, val, how, url, disp, note, score):
    rel_label = "高管间" if rel == "r3" else "上下级"
    src_label = "一手" if src == "b1" else "二手"
    return dict(emoji=emoji, title=title, cat=cat, rel=rel, rel_label=rel_label,
                src=src, src_label=src_label, val=val, how=how,
                url=url, disp=disp, note=note, score=score)

NEW = [
 # ③ 高管间 (5)
 card("🧯","Carta CEO 全员会 humane 裁员·亲讲担责（Inc·案例）","裁员全员会","r3","b2",
   "Carta CEO Henry Ward 在全员会(Zoom)直播宣布裁 161 人(16%)，全程担责(『若今天是你最后一天，唯一要怪的就是我』)、给足信息(人数/比例/部门/后续通知时点)、最大遣散包+COBRA+校友 Slack、把公告发 Medium 获全网赞誉。信任修复剧本：CEO 亲讲+透明+担责+资源。",
   "裁员前写脚本不即兴；全员会同步宣布+明确『何时/如何被告知』降低不确定；CEO 独担决策不甩锅给经理；遣散包尽量优厚+建校友网络；公告同步对外透明(Medium)反成信任资产；远程用视频并录像供后续处理。",
   "https://www.inc.com/betsy-mikel/how-you-can-conduct-layoffs-humanely.html",
   "inc.com/how-you-can-conduct-layoffs-humanely",
   "③ 高管在全员会宣布艰难决定时以『亲讲+透明+独担责+优厚遣散+对外透明』把信任危机变信任资产(Carta 案例)。",5),
 card("📜","15 个 C-Suite Town Hall 逐字脚本库（leadership-and-development）","高管脚本库","r3","b2",
   "15 套可直接套用的 C-suite town hall 逐字脚本，覆盖无名下英雄表彰/价值观落地/90天目标收尾等；每套含『把后台 quiet win 连到护盘与降本』『用真实一线行为命名核心价值观』『离场前给清 90 天三优先非模糊动员』三板斧。",
   "表彰别只念销售增长，把数据库/合规/薪酬等后台 quiet win 连到护收入(具体$);用真实一线行为(而非抽象价值观)命名文化;收尾给 90 天三非协商优先+各部门周五前领指标，建问责。",
   "https://leadership-and-development.com/15-c-suite-town-hall-scripts-for-leaders-word-for-word",
   "leadership-and-development.com/15-c-suite-town-hall-scripts",
   "③ 高管用『后台 quiet win 连护盘/真实行为命名价值观/离场前 90 天三优先』三板斧把全员会做成问责与对齐现场。",4),
 card("🏛️","公司 Town Hall 活动策划·建信任增参与（Great Place 视角）","活动策划","r3","b2",
   "专业活动策划视角：Town Hall 是领导↔员工真实对话平台，价值在透明/信任/连接；议程须平衡业务更新+员工聚焦(客户故事/员工认可/创新亮点)+互动；领导沟通定调——真实故事/坦诚讲挑战胜过长篇 PPT；技术(直播/投票/互动平台)让现场与远程平等。",
   "会前定清晰单目标(别塞太多主题);议程混业务更新+员工认可+客户成功故事+互动讨论;coaching 演讲者用真实故事非念稿;投技术让远程平等参与;把 Town Hall 当体验非例行播报。",
   "https://coalesceeventz.com/blog/corporate-town-hall-event-planning",
   "coalesceeventz.com/blog/corporate-town-hall-event-planning",
   "③ 用『单目标议程+真实故事领导定调+技术让远程平等+互动优先』把公司 Town Hall 做成信任与参与体验。",4),
 card("📖","内部沟通叙事 7 招·领导先讲人（Blink）","叙事沟通","r3","b2",
   "内部沟通叙事 7 招：领导先讲个人故事(哪怕无关主题)更易共鸣；真实胜过光鲜(连高管失败也讲)；按受众分群避免信息过载；重要故事反复讲(舒尔茨米兰轶事成星巴克 legend)；用多媒体(视频/直播)让一线也能消费；鼓励员工自己产内容。",
   "全员会开场用个人故事破冰显 human;坦诚讲挑战与失败增可信;按员工分群定制信息防 overload;把价值观/使命故事反复讲成文化锚;移动端/短视频让一线可触;开评论让员工产内容。",
   "https://www.joinblink.com/intelligence/internal-communication-storytelling",
   "joinblink.com/intelligence/internal-communication-storytelling",
   "③ 高管用『开场个人故事+坦诚讲失败+分群定制+重要故事反复讲+多媒体触达一线』把叙事变信任与文化锚。",4),
 card("🔄","微软全员会×Pulse 调研·持续双向对话（Resolution）","沟通节奏","r3","b2",
   "微软(22万+全球)内部沟通范式：季度全员会(Nadella 亲讲)为支柱+高频 Pulse 短调研形成持续倾听节奏；Pulse 洞察直接塑下场全员会议程与领导话术；渠道分层(Teams 项目级/Yammer 社区/高管博客)；数据驱动决策——员工见反馈真塑领导动作才持续参与。",
   "建可预测节奏(季全员会+月/周 Pulse);全员会前用 Pulse/匿名征题形塑议程;渠道分层分发(项目/社区/高管视角);把调研洞察可见地落进下场议程与领导话术;用 Yammer 等做无过滤 Q&A。",
   "https://www.resolution.de/post/internal-communication-plan-examples",
   "resolution.de/post/internal-communication-plan-examples",
   "③ 高管用『季全员会为柱+高频 Pulse 塑议程+渠道分层+调研洞察可见落地』建 22 万人持续双向对话。",4),
 # ② 上下级 (6)
 card("🤝","温情裁员·留任者 guilt 修复+持续沟通（GPTW）","裁员沟通","r2","b2",
   "Great Place To Work 研究：艰难期靠信任快恢复；6 实践——①倾听文化(真懂员工才能温柔谈难事)②支持经理(grief/resilience 培训+论坛)③透明常沟通(CEO 全员会+GM 小场+经理团队会，周更视频)④支持受影响者(遣散/COBRA/简历/内推/推荐信)⑤engage 留任者(谈如何帮离场者、创空间谈感受、EAP)⑥跟进离场者(再雇优先)。",
   "裁员前建倾听文化让难对话有温度;给经理 grief/resilience 工具与论坛;CEO 全员会+GM/经理分级场+周更手机视频(不完美但真);对被裁者超基准支持;对留任者直面 survivor's guilt+创表达空间+EAP;离职后保持联系(再雇优先)。",
   "https://www.greatplacetowork.me/how-to-lay-off-employees-with-care-and-compassion/",
   "greatplacetowork.me/how-to-lay-off-employees-with-care-and-compassion",
   "② HR/经理用『倾听文化+支持经理+透明分级沟通+超基准遣散+直面留任者 guilt+EAP+离职后联系』把裁员做成有尊严过程。",5),
 card("⚖️","混合全员会·远程现场平权议程（Daily Pick）","混合场议程","r2","b2",
   "混合全员会 playbook：会前 engineering equity(匿名征题用 Decision Wheel 定议程、双 MC 现场+远程、预读/Loom);45-50min 核心(欢迎/业务+字幕/客户故事轮换/职能 spotlight/互动休息/书面 Q&A);降低发言门槛(reaction bingo/side-channel 拉拉队/白板协同);Q&A 远程现场双队列轮替+匿名提交+24h 书面答;会后 highlight reel+thread steward 续能量。",
   "议程前用匿名征题+双 MC 让远程与现场同权;核心控 45-50min 含客户故事轮换与互动休息;reaction bingo+chat hype squad 降门槛;Q&A 分远程/现场双队列轮替+匿名+24h 答;会后剪 120s 高光+指定 thread steward 续聊。",
   "https://dailypick.dev/blog/hybrid-all-hands-playbook-fair-fun-agendas-that-keep-teams-engaged/",
   "dailypick.dev/blog/hybrid-all-hands-playbook",
   "② 内部沟通用『会前匿名征题+双MC+核心控时+远程现场双队列 Q&A+24h 书面答+高光续能量』让混合全员会真平权。",5),
 card("🎛️","混合全员会三要点·主持/技术/互动（Catchbox）","混合执行","r2","b2",
   "混合全员会三要件：①指定主持(moderator)串场控时防冷场②专职技术支援(80人卡 5min=近 7h 工时损失，专人快修)③互动切段(live Q&A+可抛麦克风/Slido 投票/5min 拉伸)。远程易走神，互动参与才记得住。",
   "指定 moderator 控时串场;配专职 tech support 防 5min 故障=近 7h 工时损失;用可抛麦克风/live Q&A/Slido 投票/5min 拉伸切段提参与;把混合当标配而非权宜。",
   "https://catchbox.com/blog/how-to-run-a-hybrid-all-hands-meeting",
   "catchbox.com/blog/how-to-run-a-hybrid-all-hands-meeting",
   "② 行政/IT 用『指定主持+专职技术支援+互动切段(可抛麦/Slido/拉伸)』把混合全员会做成标配不翻车。",4),
 card("🌐","远程全员会·让人期待的设计（RIEMOTE）","远程设计","r2","b2",
   "远程全员会设计：清晰目的+提前发议程(Notion 征题);短聚焦更新(高管 5-7min/部门 2-3min/公告≤5min+视觉);庆祝人与赢(轮值 peer kudos/客户 win/里程碑);互动 Q&A(Slido/Mentimeter 匿名+Zoom 投票+breakout);时区包容(轮换时段+录播+纪要);指定 MC 控场添轻松;技术测试+备份+必录;surprise guest/虚拟 swag/feedback。",
   "议程前用协作工具征题;更新短聚焦(高管≤7min+视觉);轮值 peer kudos 庆祝;匿名 Q&A+breakout;轮换时段照顾时区+录播+纪要;指定 MC 控场;会前测技术+备份+必录;surprise guest/虚拟 swag 添记忆点+会后 feedback。",
   "http://riemote.com/blog/running-remote-all-hands-meetings-people-love",
   "riemote.com/blog/running-remote-all-hands-meetings-people-love",
   "② 远程团队用『提前征题+短聚焦更新+轮值 peer kudos+匿名 Q&A+时区轮换录播+指定 MC+会前测技术』把全员会做成期待。",4),
 card("📋","裁员沟通最佳实践·步骤序列（Success Knocks）","裁员沟通","r2","b2",
   "裁员沟通步骤序列：①准备信息与传递者(写脚本讲 why+不 blame、经理 role-play 含情绪应对、备 severance/福利/推荐信 FAQ)②选时机渠道(先私下 1:1 通知、24-48h 内广而告之止谣言、避开周五/节前)③共情清晰直说(直给人数与原因+承认影响+立即给下一步+支持资源)④速对留任者(24-48h 内全员会+Q&A+书面复盘+重述价值与愿景)⑤ relentless 跟进(书面总结+1:1+监测情绪+90 天节奏更新)。",
   "先写脚本训经理(role-play 情绪应对、备 FAQ);先 1:1 私下通知再 24-48h 内全员会止谣言、避周五;直给人数原因+承认影响+立即下一步+资源;全员会+Q&A+书面复盘;90 天设沟通节奏 relentless 跟进+监测情绪。",
   "https://successknocks.com/handling-layoff-communication-best-practices",
   "successknocks.com/handling-layoff-communication-best-practices",
   "② HR/经理用『先写脚本训传递者+1:1 先通知再 24-48h 全员会+直给人数原因+90 天节奏跟进』把裁员沟通做成可信赖。",4),
 card("🔗","把 Town Hall 开成真连接·故事/可达/跟进（Zoho）","连接设计","r2","b2",
   "把 Town Hall 开成真连接：①清晰单目的(别塞太多主题)②互动非单向(live Q&A+实时投票+小场 breakout)③讲故事故事非数字(客户成功/团队克难/个人反思，数字给意义)④庆祝里程碑与人(达标/发新/周年，peer 前被认可持续)⑤人人可达(直播+录制+会后分享，混合/时区不落人)⑥会后跟进(纪要/要点/决策/持续问答渠道)⑦短聚焦(45min 胜 2h)⑧形式多变(轮换发言人/视频/客座)。",
   "每场定 1-2 优先别贪多;live Q&A+投票+breakout 变双向;用客户/团队/个人故事替数字堆;庆祝达标与 peer 认可;直播+录制+会后分享保可达;发纪要+留持续问答渠道;控 45min;轮换发言人/客座增新鲜。",
   "https://www.zoho.com/connect/the-collective/how-to-run-town-hall-meetings-that-truly-connect.html",
   "zoho.com/connect/the-collective/how-to-run-town-hall-meetings-that-truly-connect.html",
   "② 内部沟通用『单目的+互动非单向+故事替数字+庆祝 peer+人人可达+会后跟进+短聚焦+形式多变』把 Town Hall 开成真连接。",4),
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
new_html += '    <p>采集于 2026-08-12（十一轮补采 +11）｜ 六维评估（含关系适配度）｜ 一手/二手标注 ｜ 历史去重 ｜ 受众关系分层（仅②上下级 / ③高管间）</p>\n'
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

# ---------- 4. 更新 index.json (+11, 去重) ----------
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
# 5a. 汇总笔记
note = open(NOTE, encoding="utf-8").read()
note = note.replace('本批 **96 卡**', '本批 **%d 卡**' % (n3 + n2))
note = note.replace('(2026-08-10 六轮补采 +11；2026-08-11 九轮补采 +11；2026-08-11 十轮补采 +12)',
                    '(2026-08-10 六轮补采 +11；2026-08-11 九轮补采 +11；2026-08-11 十轮补采 +12；2026-08-12 十一轮补采 +11)')
note = note.replace('### ③ 领导↔领导（高管间 · exec）— 20 卡',
                    '### ③ 领导↔领导（高管间 · exec）— %d 卡' % n3)
note = note.replace('### ② 领导↔员工（上下级 · supervisor）— 76 卡（本表增量更新，全量 76 张见卡片墙 HTML）',
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
    "\n## 轮次 20260812-r11（+11）\n\n"
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
idx00 = idx00.replace('## 主题：员工大会（2026-08-07 首采 · 四轮补采 2026-08-09 · 五轮补采 2026-08-09）',
                       '## 主题：员工大会（2026-08-07 首采 · 四轮补采 2026-08-09 · 五轮补采 2026-08-09 · 六轮补采 2026-08-10 · 十轮补采 2026-08-11 · 十一轮补采 2026-08-12）')
idx00 = idx00.replace('**96 卡**（2026-08-09 五轮补采 +10；2026-08-11 九轮补采 +11；2026-08-11 十轮补采 +12）',
                       '**%d 卡**（2026-08-09 五轮补采 +10；2026-08-11 九轮补采 +11；2026-08-11 十轮补采 +12；2026-08-12 十一轮补采 +11）' % (n3 + n2))
idx00 = idx00.replace('含一手 10（地图产品部内部复盘 + 5 个企业官方真实案例 + 2 个山东能源官方宣贯案例 + 中核集团官方年度工作会 + 鞍钢集团官方表彰大会，均非安全HRBP 空间）+ 二手 35。',
                       '含一手 31（地图产品部内部复盘 + 5 个企业官方真实案例 + 2 个山东能源官方宣贯案例 + 中核集团官方年度工作会 + 鞍钢集团官方表彰大会 + 中牧/中煤/国网/华能 2026工作会 + 中交一航局官方 + 4 央企官方 2026 工作会，均非安全HRBP 空间）+ 二手 %d。' % n2)
idx00 = idx00.replace('Korn Ferry 社媒时代沟通困境) 9 卡 / ②上下级',
                       'Korn Ferry 社媒时代沟通困境) %d 卡 / ②上下级' % n3)
idx00 = idx00.replace('中核鞍钢官方案例) 36 卡。',
                       '中核鞍钢官方案例) %d 卡。' % n2)
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
    "title: 员工大会-2026-08-12-第十一轮-知识卡\n"
    "type: 自动化采集\n"
    "date: 2026-08-12\n"
    "tags: [知识采集, 员工大会, 全员大会, townhall, all-hands, 十一轮]\n"
    "relation: [supervisor, exec]\n"
    "---\n\n"
    "# 员工大会 · 第十一轮补采知识卡（2026-08-12，+11）\n\n"
    "> 本轮独立页（GitHub Pages）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/runs/staff-meeting-2026-08-12-r11.html\n"
    "> 本地路径：`knowledge-collection/staff-meeting/runs/staff-meeting-2026-08-12-r11.html`\n"
    "> 累计总索引（卡片墙）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/staff-meeting.html\n\n"
    "## 本轮 11 张卡（③高管间 5 / ②上下级 6，按受众关系分层，剔除①平级/朋友向）\n\n"
    "| 卡 | 适用关系 | 一手/二手 | 一句话定位 |\n|---|---|---|---|\n"
)
for c in NEW:
    rl = "③高管间" if c["rel"] == "r3" else "②上下级"
    sl = "一手" if c["src"] == "b1" else "二手"
    runs_note += "| %s | %s | %s | %s |\n" % (c["title"], rl, sl, c["note"].replace("③ ", "").replace("② ", ""))
runs_note += "\n## 覆盖关系档与来源\n- ③高管间：Carta CEO 全员会 humane 裁员担责案例 / 15 套 C-Suite 逐字脚本库 / 公司 Town Hall 活动策划建信任 / 内部沟通叙事 7 招 / 微软全员会×Pulse 持续双向对话。\n- ②上下级：温情裁员留任者 guilt 修复(GPTW) / 混合全员会远程现场平权议程(Daily Pick) / 混合全员会三要点主持技术互动(Catchbox) / 远程全员会让人期待设计(RIEMOTE) / 裁员沟通步骤序列(Success Knocks) / 把 Town Hall 开成真连接(Zoho)。\n- 一手率：0/11（本轮聚焦『裁员/艰难消息全员会』与『混合/远程全员会平权设计』两大增量域，源均为权威机构/媒体/工具官方二手）；累计墙一手 31/二手 %d。\n" % n2
open(RUNS_NOTE, "w", encoding="utf-8").write(runs_note)
print("wrote runs note")

# ---------- 6. 更新门户 index.html (96 -> 107) ----------
portal = open(PORTAL, encoding="utf-8").read()
portal = portal.replace('<div class="cnt">96 卡</div>', '<div class="cnt">%d 卡</div>' % (n3 + n2))
open(PORTAL, "w", encoding="utf-8").write(portal)
print("updated portal")

print("DONE")
