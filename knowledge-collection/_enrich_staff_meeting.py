# -*- coding: utf-8 -*-
import json, re, os, datetime

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "staff-meeting", "staff-meeting.html")
INC = os.path.join(BASE, "staff-meeting", "staff-meeting-20260811.html")
RUNS = os.path.join(BASE, "staff-meeting", "runs", "index.html")
IDX = os.path.join(BASE, "index.json")
NOTE = r"C:\Users\v_yitcai\Documents\Obsidian\知识采集库\素材\staff-meeting\员工大会-知识卡汇总.md"
IDX00 = r"C:\Users\v_yitcai\Documents\Obsidian\知识采集库\00-知识采集索引.md"
PORTAL = os.path.join(BASE, "index.html")
TODAY = "2026-08-11"

# ---------- 1. 提取现有卡片（按区域，保证原位置）----------
html = open(HTML, encoding="utf-8").read()

def extract_cards(block):
    cards = []
    tokens = list(re.finditer(r'<div\b|</div>', block))
    i = 0
    while i < len(tokens):
        if tokens[i].group() == '<div' and block[tokens[i].end():tokens[i].end()+30].startswith(' class="hl"'):
            depth = 0
            j = i
            end = i
            for t in range(i, len(tokens)):
                if tokens[t].group() == '<div':
                    depth += 1
                else:
                    depth -= 1
                if depth == 0:
                    end = t
                    break
            start = tokens[i].start()
            stop = tokens[end].end()
            cards.append(block[start:stop])
            i = end + 1
        else:
            i += 1
    return cards

comment3 = html.index('<!-- ============ ③')
i3 = html.index('<div class="sec sec3">')
sec2 = html.index('<div class="sec sec2">')
g3_start = html.index('<div class="grid">', i3)
g2_start = html.index('<div class="grid">', sec2)
footer_pos = html.index('<footer>')

loose_region = html[comment3:i3]
three_region = html[g3_start:sec2]
two_region = html[g2_start:footer_pos]

existing_three = extract_cards(three_region)
existing_two = extract_cards(two_region) + extract_cards(loose_region)  # 游离卡并入②
print("existing ③:", len(existing_three), "existing ②:", len(existing_two))

# ---------- 2. 本轮 11 张新卡 ----------
def card(emoji, title, cat, rel, src, val, how, url, disp, note):
    rel_label = "高管间" if rel == "r3" else "上下级"
    src_label = "一手" if src == "b1" else "二手"
    return dict(emoji=emoji, title=title, cat=cat, rel=rel, rel_label=rel_label,
                src=src, src_label=src_label, val=val, how=how,
                url=url, disp=disp, note=note)

NEW = [
 # ③ 高管间 (7)
 card("🕊️","裁员后全员会信任修复剧本（Unicorn Labs）","危机沟通","r3","b2",
   "Unicorn Labs 裁员后全员会剧本：把『信任测试』当核心——承认(Acknowledge)先于解释；讲真实版本(why)不含糊；直接回答『我是不是下一个』(讲稳定项)；90 天 3 优先；不过滤 Q&A；收尾一句真话。三失败模式：有毒正能量/空洞乐观/过度解释。信任双引擎=胜任力(真实计划)+善意(承认人的代价)，两者裁员后都受损，需同时修复。",
   "开场先让人的时刻落地再讲业务；坦诚说『我们基于错误假设扩张、部分可避免』；直接答 Am I next；Q&A 不过滤、I don't know 也有效；收尾一句真信念非打鸡血。",
   "https://unicornlabs.ca/blog/town-hall-script-after-layoffs",
   "unicornlabs.ca/blog/town-hall-script-after-layoffs",
   "③ 高管在裁员/重组后开全员会修复信任的真实剧本（信任=胜任+善意双引擎）。"),
 card("📉","CEO 向员工传达坏消息最佳实践（Glenn Gow）","危机沟通","r3","b2",
   "Glenn Gow：CEO 传坏消息(裁员/冻薪/项目失败)保信任的框架——充分准备(数据+预判问题+简练信息)、透明诚实不粉饰、担责不甩锅、给上下文与原因、列应对步骤、亲自当面讲、留问答时间、会后书面摘要。真实案例：关亏损产品线『探索所有方案后艰难决定，理解影响，提供过渡支持』。",
   "会前备齐财务/行业数据+预判 Q；用清晰直白语言+共情；担责『我负责此决定』；给后续计划与支援(离职包/EAP/再就业)；能当面不当邮件；会后发书面要点。",
   "https://www.glenngow.com/communication-tips-for-ceos-delivering-bad-news-to-your-company-and-employees",
   "glenngow.com/.../communication-tips-for-ceos-delivering-bad-news",
   "③ CEO/高管在全员会宣布坏消息的沟通纪律(透明+担责+共情+跟进)。"),
 card("📊","全员会五大进阶衡量指标（Success-Communications）","效果衡量","r3","b2",
   "把全员会从『出席率』虚荣指标升级为『认同度』——5 进阶指标：①信息共鸣分(会后让员工用自己话重述战略要点)②情绪位移(会前/后 48h Slack/Teams 关键词情绪)③经理级联指数(一周后中层对向下解释战略的信心 1-10+是否开跟进会)④问题主题分析(从战术提问→战略提问=对齐成熟)⑤战略举措关联(会后 PM 工具新增任务明确引用该战略)。证明沟通 ROI 给 C-suite。",
   "每次全员会挑 1-2 个指标试点；会后测清晰度/情绪位移/经理级联/问题迁移/PM 任务引用；用看板向 C-suite 证明价值并持续迭代。",
   "https://www.success-communications.com/orchestrating-all-hands-meetings-that-transform-strategy-into-collective-action",
   "success-communications.com/.../orchestrating-all-hands-meetings",
   "③ 高管/内部沟通用 5 进阶指标把全员会做成可衡量战略工具(对 C-suite 证明 ROI)。"),
 card("🌐","全球跨时区全员会·黄金窗口+异步（EarthTimezones）","全球同步","r3","b2",
   "全球全员会的时区解法——①找『黄金窗口』(美/欧/亚通常仅 2-3h 重叠，留给 all-hands)②异步优先(学 GitLab/Basecamp，录 Loom/写简报让东京时区睡醒再回应)③『共担痛苦』轮换(APAC 本周深夜→下周 US 清晨，别让一区恒牺牲)④deadline 统一用 UTC。核心：避免让某人凌晨 3 点开会。",
   "把全员会固定放进黄金窗口；常规更新改异步(录屏/简报)；必须同步时按区域轮换时段；所有截止时间标 UTC；用世界时钟仪表盘透明化。",
   "https://earthtimezones.com/blog-post-global-meetings",
   "earthtimezones.com/blog-post-global-meetings",
   "③ 跨国/分布式组织的高管用『黄金窗口+异步+轮换+UTC』解决全员会时区排斥。"),
 card("📖","叙事弧框架·全员会讲公司故事（OpsLab）","叙事框架","r3","b2",
   "全员会的本质是『共创共享清晰度』——回答三问『我们从哪来/现在在哪/去哪』。框架：①Where we've been(赢面+价值观故事)②Where we are(诚实业务快照+适度财务+坦承挑战)③Where we are going(愿景+季度 Rocks+大赌注)④Reinforce values(表彰践行者)⑤Open Q&A。文化靠这种『把人连回大故事』的时刻防侵蚀。",
   "每次全员会按『过去赢面→当下诚实快照(含挑战)→未来方向→价值观表彰→开放问答』五段走；让全员从座位 zoom out 看全局；价值观用真实案例活着讲而非贴墙。",
   "https://www.opslab.ca/blog/why-do-town-halls-matter",
   "opslab.ca/blog/why-do-town-halls-matter",
   "③ 高管用『三问叙事弧+价值观活讲』把全员会做成共创清晰度与文化防侵蚀。"),
 card("🎬","领导力故事五步模板（TAC Results）","叙事模板","r3","b2",
   "故事比数据更能驱动认同——五步框架 Hook(10-15s 好奇/张力)→Challenge(30-45s 障碍)→Turning Point(30-45s 决策/心态转折)→Resolution(20-30s 正果)→Takeaway(10-15s 拉回团队现状)。用法：讲起源故事/员工影响故事/变革故事；真实含挣扎、可互动、连价值观。",
   "全员会/镇会开场用『三秒钩子→障碍→转折→结果→落点』五步讲一段真实领导故事；把故事绑回公司使命；邀请员工也讲自己的；真实(含教训)胜过完美。",
   "https://www.tacresults.com/blog/power-of-storytelling/",
   "tacresults.com/blog/power-of-storytelling",
   "③ 高管在全员会用『五步故事框架』把战略变可感可记(数据给证据、故事给意义)。"),
 card("💡","Open Book Meeting·CFO 财务透明全员会（Girdley）","财务透明","r3","b2",
   "Girdley 『Open Book Meeting』(又名 All-Hands/Town Hall)：CEO 四季末向全员极透明更新——赢面→长/短/即期目标(诚实是否达标)→CFO 讲财务(多数人首次看到关乎生计的数字)→小团建(Kahoot)→新动向聚光→颁高绩效奖→CEO Q&A(主持+邀难题+『我不知，回头答』)→准时收尾。消除『叙事真空』(Narrative Void)提对齐/敬业/文化。",
   "季末开全员 Open Book：先赢面再诚实讲目标进度；CFO 亲讲财务建信任；中段小互动防困；颁高绩效奖建热情；Q&A 主持+邀尖锐问题+敢说『不知』；准时结束尊重时间。",
   "https://newsletter.girdley.com/p/killing-the-narrative-void-free-template",
   "newsletter.girdley.com/p/killing-the-narrative-void-free-template",
   "③ 高管/CFO 用『Open Book』季度全员会极透明讲财务、消叙事真空、提对齐。"),
 # ② 上下级 (4)
 card("🎙️","员工大会主持词结构与串场范本（renrendoc）","主持词","r2","b2",
   "员工大会主持词标准结构：开场白(欢迎+定调)→介绍主要领导→宣布大会开始→领导致辞/工作报告(主持串『高屋建瓴+指明方向』)→宣读表彰决定/通知→先进代表发言→互动答疑(可选)→其他仪式(签责任书/启动)→总结讲话→结束语。串场要简洁、突出仪式感、承上启下，避免卡壳。",
   "用『欢迎定调→介绍领导→宣布开始→引领导报告(概括核心)→宣读表彰→代表发言→可选答疑→仪式→总结→结束』固定串词骨架；每段用一句承上启下过渡；重大仪式(颁奖/签约)单独给主持词强调感。",
   "https://www.renrendoc.com/paper/525850400.html",
   "renrendoc.com/paper/525850400.html",
   "② 主持人/行政用标准串词骨架串起员工大会议程，防卡壳、强仪式感。"),
 card("🐦","主管宣布坏消息6大要领·当机立断（中国新闻网）","危机沟通","r2","b2",
   "主管扮好『乌鸦』传坏消息 6 要领——①当机立断尽早宣布(拖延助长谣言；上午开会让员工有空消化；邮件最糟媒介，全体会议上宣布)②老实说(不知全貌就直说)③清楚直接(简洁、不复述绕圈、不模棱两可、不故作幽默)④表现体谅(不显得不痛不痒)⑤复述讯息助记忆⑥安排问答。把冲击减到最小且赢得敬重。",
   "坏消息第一时间全体会议上讲清；用直接简洁语言+共情不回避；先简短正面再讲负面+应对改变；允许提问并准备答；上午开、不当邮件；复述关键讯息。",
   "https://www.chinanews.com/hb/2011/10-12/3384295.shtml",
   "chinanews.com/hb/2011/10-12/3384295.shtml",
   "② 中基层主管向团队宣布坏消息(裁员/冻薪/缩编)的 6 要领(早/真/直/共情/复述/答疑)。"),
 card("📈","员工大会效果评估体系·定量+定性闭环（renrendoc）","效果评估","r2","b2",
   "员工大会工作方案评估体系：定量(出勤率/现场互动频/直播观看+完播/问卷回收/舆情热度)+定性(战略理解度/情感认同/归属感/行动意愿量表+行为观察+关键岗深访)；闭环改进(实时弹幕/投票箱/即时通讯捕反馈→会后立即析问卷高频词→建『改进委员会』定措施→建大会档案库)；长期把仪式感转生产力。",
   "建『定量+定性』双维评估模型；会中实时捕反馈现场调、会后析问卷建改进委员会；每届归档成企业大会知识库；跟踪『战略理解/情感认同/行动意愿』长期位移。",
   "https://m.renrendoc.com/paper/525832825.html",
   "renrendoc.com/paper/525832825.html",
   "② HR/行政建多维评估+闭环改进机制，让大会质量螺旋上升(非只看出勤)。"),
 card("📝","会后即时调研四维度（myculture.ai）","效果评估","r2","b2",
   "全员会效果用会后即时调研四维度(1-5 量表)——清晰度(『会后更懂公司优先项』)/参与度(『时间花得值』)/信任(『听更新后对领导更信』)/可行动性(『知道我/团队接下来要做什么』)；定量+开放题混用；持续跟踪趋势(清晰度跳升=简化 PPT 有效、信任涨=某次坦诚 Q&A 有效)证明价值并迭代。",
   "每次全员会发四维度量表(清晰/参与/信任/可行动)+1-2 开放题；跨会议跟踪趋势定位问题；用看板向领导证明会议改善对齐与信心；依数据调下一届形式。",
   "https://www.myculture.ai/blog/all-employee-meeting",
   "myculture.ai/blog/all-employee-meeting",
   "② HR/内部沟通用『清晰/参与/信任/可行动』四维度即时调研持续度量全员会效果。"),
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
        if c not in seen:
            seen.append(c)
    return " / ".join(seen)

three_cats = cats("\n".join(all_three))
two_cats = cats("\n".join(all_two))

new_html = head + "\n<body>\n<div class=\"wrap\">\n"
new_html += '<p style="margin:0 0 16px"><a href="runs/index.html" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">📑 查看本主题分页独立页 →</a></p>\n'
new_html += '  <div class="hero">\n'
new_html += '    <h1>🎤 员工大会 · 知识采集卡片墙</h1>\n'
new_html += '    <p>采集于 2026-08-11（九轮补采 +11）｜ 六维评估（含关系适配度）｜ 一手/二手标注 ｜ 历史去重 ｜ 受众关系分层（仅②上下级 / ③高管间）</p>\n'
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

# ---------- 4. 渲染增量页 staff-meeting-20260811.html ----------
inc_html = head + "\n<body>\n<div class=\"wrap\">\n"
inc_html += '<p style="margin:0 0 16px"><a href="staff-meeting.html" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">🗂 返回累计总索引 →</a></p>\n'
inc_html += '  <div class="hero">\n'
inc_html += '    <h1>🎤 员工大会 · 本轮增量卡片墙</h1>\n'
inc_html += '    <p>轮次 2026-08-11（九轮补采 +11）｜ 仅含本轮通过六维评估的 ②上下级 / ③高管间 卡 ｜ 受众关系分层（剔除①平级/朋友向）</p>\n'
inc_html += '    <div class="relbar">\n'
inc_html += '      <span>② 领导↔员工（上下级，supervisor）</span>\n'
inc_html += '      <span>③ 领导↔领导（高管间，exec）</span>\n'
inc_html += '    </div>\n'
inc_html += '  </div>\n\n'
inc_html += '  <div class="sec sec3">\n'
inc_html += '    <h2>③ 领导↔领导（高管间 · exec）</h2>\n'
inc_html += '    <span class="tag">%d 卡</span>\n' % len(new_three)
inc_html += '    <span class="desc">本轮新增 ③高管间 卡</span>\n'
inc_html += '  </div>\n  <div class="grid">\n\n'
inc_html += "\n".join(card_html(c) for c in new_three) + "\n"
inc_html += '  </div>\n\n'
inc_html += '  <div class="sec sec2">\n'
inc_html += '    <h2>② 领导↔员工（上下级 · supervisor）</h2>\n'
inc_html += '    <span class="tag">%d 卡</span>\n' % len(new_two)
inc_html += '    <span class="desc">本轮新增 ②上下级 卡</span>\n'
inc_html += '  </div>\n  <div class="grid">\n\n'
inc_html += "\n".join(card_html(c) for c in new_two) + "\n"
inc_html += '  </div>\n\n'
inc_html += '  <footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>\n'
inc_html += '</div>\n</body>\n</html>\n'
open(INC, "w", encoding="utf-8").write(inc_html)
print("wrote incremental bytes:", len(inc_html))

# ---------- 5. 更新 runs/index.html（追加第 8 批）----------
runs = open(RUNS, encoding="utf-8").read()
new_batch = (
    '    <div class="idxcard">\n'
    '      <div class="seq">8</div>\n'
    '      <h3>第 8 / 共 8 批</h3>\n'
    '      <div class="meta">11 卡 ｜ ③高管间 %d / ②上下级 %d</div>\n' % (len(new_three), len(new_two)) +
    '      <a href="staff-meeting-20260811.html">查看本批 →</a>\n'
    '    </div>\n'
)
runs = runs.replace('  </div>\n</div>\n<footer', '    ' + new_batch + '  </div>\n</div>\n<footer', 1)
runs = runs.replace('共拆为 7 个批次', '共拆为 8 个批次', 1)
open(RUNS, "w", encoding="utf-8").write(runs)
print("updated runs/index.html")

# ---------- 6. 更新 index.json (+11) ----------
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

# ---------- 7. 更新 Obsidian 笔记 ----------
note = open(NOTE, encoding="utf-8").read()
# 更新头部计数
note = re.sub(r'本批 \*\*73 卡\*\*', '本批 **84 卡**', note)
note = re.sub(r'（2026-08-10 六轮补采 \+11；[^）]*）', '(2026-08-10 六轮补采 +11；2026-08-11 九轮补采 +11)', note, count=1)
# 在 "# 员工大会 · 知识卡汇总" 标题后插入轮次小节
round_block = (
    "\n## 轮次 20260811（+11）\n\n"
    "| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n"
)
for c in NEW:
    rl = "③高管间" if c["rel"] == "r3" else "②上下级"
    sl = "一手" if c["src"] == "b1" else "二手"
    round_block += "| %s | %s | %s |\n" % (c["title"], rl, sl)
round_block += "\n"
note = re.sub(r'(# 员工大会 · 知识卡汇总（2026-08-07 自动化采集）\n)',
              r'\1' + round_block, note, count=1)
# 更新 ③ 小节计数与追加行
note = re.sub(r'### ③ 领导↔领导（高管间 · exec）— 9 卡',
              '### ③ 领导↔领导（高管间 · exec）— %d 卡' % n3, note)
note = re.sub(r'### ② 领导↔员工（上下级 · supervisor）— 64 卡[^\n]*',
              '### ② 领导↔员工（上下级 · supervisor）— %d 卡（本表增量更新，全量 %d 张见卡片墙 HTML）' % (n2, n2), note)
# 在 ③ 表末尾（首个 ② 小节前）追加 7 行
three_rows = ""
for c in new_three:
    three_rows += "| %s | 5 | 二手 | ③高管间 | %s |\n" % (c["title"], c["note"].replace("③ ", ""))
note = note.replace("| CEO 全员会沟通困境·社媒时代（Korn Ferry） | 5 | 二手 | ③高管间 | 赋权时代 CEO 每句「在记录上」、坦诚雷达极高；提前征集并主动挑难题答、CCO/CMO 可代表 C-suite、沉默也是信息 |",
                   "| CEO 全员会沟通困境·社媒时代（Korn Ferry） | 5 | 二手 | ③高管间 | 赋权时代 CEO 每句「在记录上」、坦诚雷达极高；提前征集并主动挑难题答、CCO/CMO 可代表 C-suite、沉默也是信息 |\n" + three_rows)
# 在 ② 表末尾（笔记 ② 小节最后一行后、下一个 ## 前）追加 4 行
two_rows = ""
for c in new_two:
    two_rows += "| %s | 4 | 二手 | ②上下级 | %s |\n" % (c["title"], c["note"].replace("② ", ""))
# 找 ② 小节最后一行（年会新范式...）后插入
anchor = "| 年会新范式·沉浸式创新体验（头条构思）（staff-meeting.html） | 4 | 二手 | ②上下级 | 年会当组织干预：星际船隐喻+AR 沉浸入场+小程序任务解锁+管理层发蓝图各队认领+微光故事长尾 |"
note = note.replace(anchor, anchor + "\n" + two_rows)
open(NOTE, "w", encoding="utf-8").write(note)
print("updated note")

# ---------- 8. 更新 00-索引员工大会段 ----------
idx00 = open(IDX00, encoding="utf-8").read()
# 更新计数头
idx00 = re.sub(r'\*\*10 卡\*\*（2026-08-09 五轮补采 \+10）', '**84 卡**（2026-08-09 五轮补采 +10；2026-08-11 九轮补采 +11）', idx00, count=1)
# 在该段表格末尾（Offsite 段之前）追加 11 行
new_rows = ""
for c in NEW:
    rl = "③高管间" if c["rel"] == "r3" else "②上下级"
    sl = "一手" if c["src"] == "b1" else "二手"
    new_rows += "| %s（staff-meeting.html） | 4/5 | %s | %s | %s |\n" % (c["title"], sl, rl, c["note"].replace("③ ", "").replace("② ", ""))
# 锚点：员工大会段最后一行 -> 其后插入（在 "## 主题：Offsite" 之前）
anchor2 = "| 年会新范式·沉浸式创新体验（头条构思）（staff-meeting.html） | 4 | 二手 | ②上下级 | 年会当组织干预：星际船隐喻+AR 沉浸入场+小程序任务解锁+管理层发蓝图各队认领+微光故事长尾 |"
idx00 = idx00.replace(anchor2, anchor2 + "\n" + new_rows)
open(IDX00, "w", encoding="utf-8").write(idx00)
print("updated 00-index")

# ---------- 9. 更新门户 index.html (73 -> 84) ----------
portal = open(PORTAL, encoding="utf-8").read()
portal = portal.replace('<div class="cnt">73 卡</div>', '<div class="cnt">84 卡</div>')
open(PORTAL, "w", encoding="utf-8").write(portal)
print("updated portal")

print("DONE")
