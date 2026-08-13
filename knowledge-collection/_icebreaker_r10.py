# -*- coding: utf-8 -*-
import json, re, os, datetime

KC = os.path.dirname(os.path.abspath(__file__))
IB_DIR = os.path.join(KC, "icebreaker")
WALL = os.path.join(IB_DIR, "icebreaker.html")
TMP = os.path.join(IB_DIR, ".run_newcards.tmp.html")
BAD_R10 = os.path.join(IB_DIR, "runs", "icebreaker-2026-08-14-r10.html")
INC = os.path.join(IB_DIR, "icebreaker-20260814.html")
INDEX = os.path.join(KC, "index.json")
PORTAL = os.path.join(KC, "index.html")

TODAY = "2026-08-14"
RUN_DATE = "20260814"

# ---------- 7 张真实新增卡（仅②③，0 peer；全二手） ----------
NEW = [
 dict(rel="exec", src="secondary", emoji="🌐", cat="高管入职",
   title="跨文化/远程高管入职·前100天信任与权限地图",
   url="https://pactandpartners.com/zh-hans/qian-100-tian-mei-guo-gao-guan-ru-zhi",
   disp="pactandpartners.com/zh-hans/qian-100-tian-mei-guo-gao-guan-ru-zhi",
   val="外国企业聘用外籍（如美国）高管，文化模型冲突是头号失败源：共识决策 vs 个人决断、层级尊重 vs 直接沟通。有效做法=在招聘时就明确「聘你来改文化还是融入现有文化」，CEO 必须发信号支持。反主流洞见：有意的远程入职可优于同址——它强迫把汇报线、权限、文化规范讲明白，反而更少意外。好/坏入职对比：权限清晰度(D30 成文)、前90天交付2-3个可见战略项目在董事会建信誉、18个月留任率85%+ vs 行业50-60%、CEO-高管周/双周结构化1:1。",
   howto="聘前用「改文化 or 融文化」二选一校准期望；远程入职当作高端服务：更充分准备+更清晰议程+会话留痕；D30 前把决策权限书面化（可独决/需征询）；CEO 与高管固定节奏 1:1；时区节律 D30 前确立防燃尽。",
   note="适用：③ 跨国/远程高管入职——用「权限地图+结构化1:1」替代寒暄式融入，化解文化模型冲突。"),
 dict(rel="exec", src="secondary", emoji="🏛️", cat="高管入职",
   title="家族企业 C-suite 入职·文化翻译官+关系资本",
   url="https://carterbaldwin.com/wp-content/uploads/2025/06/The-First-90-Days.pdf",
   disp="carterbaldwin.com/.../The-First-90-Days.pdf",
   val="家族企业（常多代、关系导向、潜规则深）空降 C 级高管，成败在文化/信任/所有权动态。五步：① 战略+文化双清晰（明确90天/1年成功样貌、正式/非正式决策如何做、地雷在哪）；② 配「文化翻译官」——指派资深领导/董事（非HR）当导师，帮新高管读懂房间（谁真有影响力、什么算尊重、何时推进何时停）；③ 不跳基础（30-60-90 计划+与家族领导定期对齐）；④ 投资关系资本（下现场、先听后说、与 owner 一对一）；⑤ 驱动变革前先与 CEO/所有权对齐。金句：家族企业 onboarding 不是提速，是慢下来以快。",
   howto="入职即配文化翻译官；把 landmines/sacred cows 显式列给 CEO 与家族；前90天重关系轻变革；重大变革先 co-create 再推。",
   note="适用：③ 家族/私企 C-suite 空降——用文化翻译官与关系资本化解代际/所有权敏感。"),
 dict(rel="exec", src="secondary", emoji="🤝", cat="高管信任",
   title="COO-CEO 二号位对齐·从签约前到任期持续信任",
   url="https://www.cooforum.net/blogs/post/you-re-not-the-coo-i-hired-how-coos-can-find-and-sustain-alignment",
   disp="cooforum.net/.../you-re-not-the-coo-i-hired",
   val="COO 是 C-suite 最危险座位——命运系于 CEO 风格。对齐不是加分项是生死线。签约前就把对齐当过滤器：澄清角色「为何现在聘 COO」（执行者/变革者/继承人/稳定者）、要书面 charter（决策权/分歧升级路径）、测 CEO 对挑战的舒适度、辨授权 vs 许可。入职早期：过度沟通（前90-180天透明分享进展+关系型「对齐检查」而非只谈指标）；确立 Leadership Avatar（边界/节奏/非 Negotiable 公开给 CEO）；自信沟通（Here's my concern/proposal/need 替代软化）；监测怨恨（「为何没 loop 我 in」是煤矿金丝雀）。",
   howto="面试阶段用 archetype+书面 charter 验对齐；上任即设关系型对齐检查（非指标复盘）；公开 Leadership Avatar 设边界；用「关切-提议-所需」三句替代被动软化。",
   note="适用：③ CEO↔COO 二号位——把对齐前置到签约、用 Leadership Avatar 防关系漂移。"),
 dict(rel="exec", src="secondary", emoji="📜", cat="高管信任",
   title="CEO-COO 工作协议·代理授权宪章（边界决策权）",
   url="https://www.antoinebuteau.com/great-coo-series-5-the-ceo-coo-partnership-trust-tension-and-proxy-authority/",
   disp="antoinebuteau.com/.../ceo-coo-partnership",
   val="最佳 CEO-COO 搭档保有共享运营地图，并显式定义边界决策权。坑：过于简单的分工造「意外双政府」（CEO 拥有战略/文化/外部，COO 拥有运营/人/财务/执行，但多数决策跨界）。解法=在边界定义决策权：CEO 拥战略、COO 拥运营计划翻译；CEO 拥生存级战略最终拍板、COO 拥既定优先级内的资源分配。必须写「代理授权宪章」（平静期而非危机时）：COO 可独决/可作 CEO 代理/可建议不可终裁/需 CEO 介入的事项；含升级规则、通信规则（联合/CEO only/COO only）、冲突规则、反模式（私下推翻/三角化/惊喜承诺）。信任来自运营一致性。",
   howto="在平静期写工作协议+代理授权宪章；把「谁真能决」显式化减少猜测；定义升级与冲突规则；定期 revisits。",
   note="适用：③ CEO↔COO——用书面工作协议与代理授权宪章把「信任」落成可执行的边界。"),
 dict(rel="exec", src="secondary", emoji="🧭", cat="高管入职",
   title="新任领导者战略入职·信任与连续性路线图",
   url="https://www.roberthalf.cn/cn/zh/insights/management-tips/leveraging-strategic-onboarding-to-build-trust-and-ensure-continuity-for-new-leaders",
   disp="roberthalf.cn/.../leveraging-strategic-onboarding",
   val="最有效的领导过渡，从入职第一天起就与团队/同事/组织建信任。三种从零加速信任法：① 结构化入职路线图（90天计划含阶段学习目标、关键关系网络、可量化早期成果；留足倾听空间，未深懂前不贸然大改）；② 让介绍见面成为信任契机而非信息传递——精心安排与直属下属/跨部门同事/高层/必要外部伙伴的 1:1 与小组会谈，双向对话理解文化与隐形规则；③ 情境认知+关系网络+目标清晰三者结合。信任是核心要素，缺之再完善策略也失效。",
   howto="给新领导者 90 天结构化路线图（学习>行动）；安排多元利益相关者 1:1；把「介绍会」设计成双向对话而非宣讲；入职即建关系网络。",
   note="适用：③ 新任领导者（含高管）入职——用结构化路线图+多元1:1把信任从 Day1 注入过渡。"),
 dict(rel="supervisor", src="secondary", emoji="🗂️", cat="新经理破冰",
   title="新经理首次团队会议·议程模板与准备清单",
   url="https://sirjohnnymai.com/zh/blog/zh-%E6%96%B0%E7%BB%8F%E7%90%86%E7%AC%AC%E4%B8%80%E6%AC%A1%E5%9B%A2%E9%98%9F%E4%BC%9A%E8%AE%AE%E8%AE%AE%E7%A8%8B%E6%A8%A1%E6%9D%BF%EF%BC%88%E5%8F%AF%E4%B8%8B%E8%BD%BD%EF%BC%89",
   disp="sirjohnnymai.com/zh/blog/新经理第一次团队会议议程模板",
   val="新经理首会不是「民主讨论」而是「建立共识的起点」。准备清单：① 上级/跨职能负责人 30min 1:1 调研期望与底线；② 回顾 6-12 月团队 OKR/路线图/反馈/bug 找痛点；③ 起草五环节核心议程（现状洞察/核心原则/未来方向/预期设定/结构化反馈）+ 宣讲稿；④ 明确≥3条「不可谈判」红线并会议宣示；⑤ 准备匿名反馈工具（问卷/投票箱）低风险提示；⑥ 会后即排每位成员 30-45min 1:1；⑦ 准备≤3min 领导理念简述。避坑：以「开放式讨论」开场显无主见；应明确阐述方向+收结构化反馈。",
   howto="会前做上级期望调研+数据回顾+五环节议程稿+红线清单；会上先阐述方向再收结构化反馈（非自由讨论）；会后用匿名工具+1:1 深化信任。",
   note="适用：② 新经理首场团队会——用准备清单+红线宣示+结构化反馈替代「亲和力式」开场。"),
 dict(rel="supervisor", src="secondary", emoji="🔄", cat="接手低绩效",
   title="低绩效团队 90 天转身·GROW 模型路线图",
   url="https://leadershipshop.wordpress.com/tag/coaching/",
   disp="leadershipshop.wordpress.com/tag/coaching",
   val="接手低绩效团队，90 天结构化计划用 GROW（Goal/Reality/Options/Way Forward）建信任拿结果。前30天=定位起点：1:1 识个人优弱与风格、听而不判、审计工作流找卡点、快速赢（一周内能修的摩擦如沟通渠道/下单流程）；31-60天=绘路径：带领团队共创 SMART(ER) 目标、授权所需、明确责任；61-90天=固动量：用 GROW 教练每个人、建庆祝文化、看继任与可持续。原则：不是强加改变，是培育团队达最佳；附反思日志+GROW 提示卡可下载。",
   howto="前30天只做 1:1 倾听+挑 1-2 个可见快赢兑现；31-60天带团队共创 SMART 目标并授权；61-90天用 GROW 教练个人+庆祝小胜固化节奏。",
   note="适用：② 接手低绩效/涣散团队——用 GROW 90天（倾听→共创→固化）重建信任不靠铁腕。"),
]

def norm_key(s):
    s = re.sub(r'[\s\u3000]+','', s)
    for c in '，。、；:：,.;·•·“”"\'’‘（）()【】[]《》<>/\\|-_—~！!？?…·':
        s = s.replace(c,'')
    return s.lower()

# ---------- card html ----------
def card_html(c):
    badge_rel = "r3" if c["rel"]=="exec" else "r2"
    rel_txt = "高管间" if c["rel"]=="exec" else "上下级"
    badge_src = "b2"  # all secondary
    src_txt = "二手"
    return (
      '  <div class="hl">\n'
      '      <div class="top"><span class="emoji">%s</span><h3>%s</h3><span class="cat">%s</span>'
      '<span class="badge %s">%s</span><span class="badge %s">%s</span></div>\n'
      '      <p class="val">%s</p>\n'
      '      <details class="exec"><summary>怎么做</summary><div class="inner">%s</div></details>\n'
      '      <div class="src">🔗 <a href="%s" target="_blank">%s</a></div>\n'
      '      <div class="note">%s</div>\n'
      '    </div>' % (
        c["emoji"], c["title"], c["cat"], badge_rel, rel_txt, badge_src, src_txt,
        c["val"], c["howto"], c["url"], c["disp"], c["note"]
      )
    )

EXEC_NEW = [c for c in NEW if c["rel"]=="exec"]
SUP_NEW  = [c for c in NEW if c["rel"]=="supervisor"]
print("exec new:",len(EXEC_NEW),"sup new:",len(SUP_NEW),"total:",len(NEW))

# ---------- 1) 增量页（仅本轮新增） ----------
CSS = """<style>
:root{--bg:#f4f6fb;--card:#ffffff;--ink:#1f2430;--sub:#5b6478;--accent:#6c5ce7;--accent2:#00b8d9;--chip:#eef0ff;}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:linear-gradient(135deg,#eef1ff 0%,#e6f7ff 100%);color:var(--ink);padding:28px 18px;line-height:1.6;}
.wrap{max-width:1080px;margin:0 auto;}
.hero{background:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);border-radius:22px;padding:30px 32px;color:#fff;box-shadow:0 14px 40px rgba(108,92,231,.25);margin-bottom:22px;}
.hero h1{font-size:28px;font-weight:800;letter-spacing:1px;margin-bottom:8px;}
.hero p{font-size:14px;opacity:.95;}
.relbar{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px;}
.relbar span{background:rgba(255,255,255,.2);border-radius:20px;padding:5px 14px;font-size:13px;font-weight:600;}
.sec{margin:30px 0 12px;display:flex;align-items:center;gap:10px;}
.sec h2{font-size:19px;font-weight:800;}
.sec .tag{font-size:12px;padding:4px 12px;border-radius:12px;font-weight:700;}
.sec3 .tag{background:#f3e8ff;color:#7b2cbf;} .sec3 h2{color:#7b2cbf;}
.sec2 .tag{background:#fff3e0;color:#c0651a;} .sec2 h2{color:#c0651a;}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;}
.hl{background:var(--card);border-radius:18px;padding:18px 18px 16px;border-top:4px solid var(--accent);box-shadow:0 10px 32px rgba(108,92,231,.10);display:flex;flex-direction:column;gap:9px;}
.top{display:flex;align-items:center;gap:8px;flex-wrap:wrap;}
.emoji{font-size:22px;}
.hl h3{font-size:16px;font-weight:700;flex:1;min-width:120px;}
.cat{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:600;background:var(--chip);color:var(--accent);}
.badge{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:700;}
.b2{background:#fff1e6;color:#c0651a;}
.b1{background:#eaf7ee;color:#1b8a4b;}
.r1{background:#eaf2ff;color:#2b6cb0;}
.r2{background:#fff3e0;color:#c0651a;}
.r3{background:#f3e8ff;color:#7b2cbf;}
.val{font-size:13.5px;color:var(--sub);}
.exec{margin-top:2px;border-top:1px dashed #e2e8f0;padding-top:8px;}
.exec summary{cursor:pointer;font-size:13px;font-weight:600;color:var(--accent);}
.exec .inner{font-size:13px;color:var(--sub);margin-top:6px;padding-left:4px;}
.src{font-size:12px;word-break:break-all;}
.src a{color:var(--accent2);text-decoration:none;}
.note{font-size:12px;color:#94a3b8;border-left:3px solid #e2e8f0;padding-left:8px;}
.back{display:block;text-align:center;margin:26px 0 6px;color:var(--accent2);text-decoration:none;font-weight:700;}
footer{text-align:center;padding:24px;color:#94a3b8;font-size:13px;border-top:1px solid #e2e8f0;margin-top:40px;}
</style>"""

def build_incremental():
    head = ('<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n<meta charset="UTF-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            '<title>破冰 · 知识采集卡片墙 · R10 增量（' + RUN_DATE + '）</title>\n' + CSS + '\n</head>\n<body>\n')
    hero = ('<div class="wrap">\n<div class="hero">\n'
            '  <h1>🧊 破冰 · 知识采集卡片墙（R10 增量）</h1>\n'
            '  <p>本轮新增 ' + str(len(NEW)) + ' 张（②上下级 ' + str(len(SUP_NEW)) +
            ' ｜ ③高管间 ' + str(len(EXEC_NEW)) + '）｜ 采集于 ' + TODAY +
            ' ｜ 仅②③、0 peer ｜ 六维评估（含关系适配度）｜ 一手/二手标注 ｜ 历史去重</p>\n'
            '  <div class="relbar">\n'
            '    <span>② 领导↔员工（上下级，supervisor）</span>\n'
            '    <span>③ 领导↔领导（高管间，exec）</span>\n'
            '  </div>\n</div>\n')
    sec3 = ('<div class="sec sec3"><h2>③ 领导↔领导（高管间 · exec）</h2>'
            '<span class="tag">' + str(len(EXEC_NEW)) + ' 卡</span></div>\n<div class="grid">\n'
            + "".join(card_html(c) for c in EXEC_NEW) + '\n</div>\n')
    sec2 = ('<div class="sec sec2"><h2>② 领导↔员工（上下级 · supervisor）</h2>'
            '<span class="tag">' + str(len(SUP_NEW)) + ' 卡</span></div>\n<div class="grid">\n'
            + "".join(card_html(c) for c in SUP_NEW) + '\n</div>\n')
    tail = ('<a class="back" href="https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/icebreaker.html" target="_blank">← 返回破冰累计卡片墙（汇总页）</a>\n'
            '<footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>\n</div>\n</body>\n</html>')
    return head + hero + sec3 + sec2 + tail

inc_html = build_incremental()
with open(INC, "w", encoding="utf-8") as f:
    f.write(inc_html)
print("wrote incremental:", INC, len(inc_html), "bytes")

# ---------- 2) 合并进汇总墙 ----------
data = open(WALL, encoding="utf-8").read()

# exec 卡插入 sec3 网格闭合前（即 <div class="sec sec2"> 之前）
idx_sec2 = data.find('<div class="sec sec2">')
grid_close_sec3 = data.rfind('</div>', 0, idx_sec2)
exec_block = "\n".join(card_html(c) for c in EXEC_NEW)
data = data[:grid_close_sec3] + exec_block + "\n" + data[grid_close_sec3:]

# supervisor 卡插入 sec2 网格闭合前（即 <footer> 之前）
idx_footer = data.find('<footer>')
grid_close_sec2 = data.rfind('</div>', 0, idx_footer)
sup_block = "\n".join(card_html(c) for c in SUP_NEW)
data = data[:grid_close_sec2] + sup_block + "\n" + data[grid_close_sec2:]

# 更新 sec tag 计数 27->32, 52->54
data = data.replace('<span class="tag">27 卡</span>', '<span class="tag">%d 卡</span>' % (27+len(EXEC_NEW)), 1)
data = data.replace('<span class="tag">52 卡</span>', '<span class="tag">%d 卡</span>' % (52+len(SUP_NEW)), 1)

# 更新 hero
new_hero_p = ('<p>采集于 %s ｜ R10 轮 enrich +%d（仅②③、0 peer；已清退上轮误产 12 张重复卡）'
              '｜ 六维评估（含关系适配度）｜ 一手/二手标注 ｜ 历史去重 ｜ 受众关系分层（仅②上下级 / ③高管间）'
              '｜ 本轮回修 R8 注入的 11 张损坏卡 + 脆弱信任缺失闭合</p>') % (TODAY, len(NEW))
data = re.sub(r'<p>采集于 2026-08-14 ｜ 十轮补采 \+12（R10）.*?</p>', new_hero_p, data, count=1)

# 校验
assert data.count('class="hl"') == 79 + len(NEW), "card count mismatch: %d" % data.count('class="hl"')
assert '📌 本页由 yitong 沉淀整理' in data

tmp = WALL + ".tmp_write"
with open(tmp, "w", encoding="utf-8") as f:
    f.write(data)
os.replace(tmp, WALL)
print("updated wall:", WALL, "cards now", data.count('class="hl"'))

# ---------- 3) index.json：回填 42 缺失 + 追加 7 新 ----------
idx = json.load(open(INDEX, encoding="utf-8"))
urls = set(x.get("url") for x in idx)
titles = set(x.get("title") for x in idx)

def parse_block(block):
    def g(pat):
        m = re.search(pat, block, re.S)
        return m.group(1).strip() if m else None
    return dict(
        title=g(r'<h3>(.*?)</h3>'),
        emoji=g(r'<span class="emoji">(.*?)</span>'),
        cat=g(r'<span class="cat">(.*?)</span>'),
        relc=g(r'badge (r[23])'),
        srcc=g(r'badge (b[12])'),
        url=g(r'<a href="(.*?)"'),
        val=g(r'<p class="val">(.*?)</p>'),
    )

# 先把本轮 7 张新卡种入 titles/urls，避免回填时重复计入
for c in NEW:
    titles.add(c["title"]); urls.add(c["url"])

# 解析全部墙卡
parts = re.split(r'<div class="hl">', open(WALL, encoding="utf-8").read())
backfill = 0
for p in parts[1:]:
    d = parse_block(p)
    if not d["title"]:
        continue
    if d["title"] in titles:
        continue  # 已在 index
    relation = "exec" if d["relc"]=="r3" else "supervisor"
    sourceType = "primary" if d["srcc"]=="b1" else "secondary"
    entry = dict(
        title=d["title"], normKey=norm_key(d["title"]), url=d["url"],
        sourceType=sourceType, relation=relation, topic="icebreaker",
        summary=re.sub(r'\s+',' ', d["val"])[:400] if d["val"] else ""
    )
    idx.append(entry)
    titles.add(d["title"]); urls.add(d["url"])
    backfill += 1
print("backfilled missing:", backfill)

added = 0
for c in NEW:
    if c["url"] in urls or c["title"] in titles:
        print("SKIP dup:", c["title"]); continue
    entry = dict(
        title=c["title"], normKey=norm_key(c["title"]), url=c["url"],
        sourceType=c["src"], relation=c["rel"], topic="icebreaker",
        summary=re.sub(r'\s+',' ', c["val"])[:400]
    )
    idx.append(entry)
    titles.add(c["title"]); urls.add(c["url"])
    added += 1
print("added new:", added)

ib_count = sum(1 for x in idx if x.get("topic")=="icebreaker")
print("icebreaker index entries now:", ib_count)
json.dump(idx, open(INDEX, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("wrote index.json")

# ---------- 4) 清理误产文件 ----------
for bad in (TMP, BAD_R10):
    if os.path.exists(bad):
        os.remove(bad); print("removed:", bad)
print("DONE render+index")
