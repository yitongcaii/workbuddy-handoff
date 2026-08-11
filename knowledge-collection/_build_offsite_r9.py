# -*- coding: utf-8 -*-
import json, os, re, datetime

KC = os.path.dirname(os.path.abspath(__file__))
DATE = "20260812"
TOPIC = "offsite"
SLUG = "offsite"
HTML_FILE = os.path.join(KC, TOPIC, TOPIC + ".html")
INC_FILE = os.path.join(KC, TOPIC, f"{TOPIC}-{DATE}.html")
INDEX_FILE = os.path.join(KC, "index.json")

# ---------- card data (only ②上下级 / ③高管间, no peer) ----------
# badge: r2=上下级, r3=高管间 ; src: b1=一手, b2=二手
cards = [
    {
        "emoji":"💰","title":"Offsite 立项商业论证·一页 business case 拿 CFO 签字",
        "cat":"立项论证","badge":"r2","src":"b2",
        "val":"向 CFO/董事会 要 offsite 预算，别用 deck 用一页 business case（5 要素）：① 一句话首要业务目标（如「降低资深 IC 主动离职」而非「团队凝聚力」）② 全成本（差旅+场地+餐饮+策划费+保守估算的产出工时损失）③ 成功指标+怎么测 ④ 不做的成本（SHRM 基准：留 1 人=年薪 50-200%，100 人 offsite 留 2 个 10 万者即避免 10-40 万替换成本）⑤ 先例（2019 后 59% 公司加了 offsite 预算）。把目标翻成财务语言——「战略对齐」=「把 Top3 倡议决策延迟砍半」，再贴美元值对比活动成本；董事会/CFO 看风险调整回报。指标会前定，别会后补。",
        "how":"一页五要素带进预算会；目标翻财务语言+贴美元值；指标会前定；对标「不做的成本」而非只算活动价。",
        "url":"https://www.affinitytravel.co/blog/how-to-build-the-business-case-for-a-company-offsite",
        "note":"适用：② 管理者/HR 向 CFO 立项团建务虚预算，一页 business case 框架 + 留人成本数学是可迁移亮点（exec 同样适用董事会论证）。",
        "section":"sec2","relation":"supervisor,exec","sourceType":"secondary"
    },
    {
        "emoji":"📍","title":"领导力 Retreat 选址完全指南（隐私·目的地·踩点·合同陷阱）",
        "cat":"选址","badge":"r2","src":"b2",
        "val":"领导力 retreat 选址与议程/引导同等重要——私密住宅式物业（6-14 人，多套卫浴卧室+主厨厨房+大起居+泳池/温泉）给高管团队完全隐私与客厅式非正式讨论，代价是 Wi-Fi 不稳须提前测、餐饮自理；目的地匹配目标（山=专注战略/海=反思焕新/城=创新工坊），优先机场 90 分钟内直达、2-3 天门到门<6-7h；肩季（4-5/9-10 月）常省 10-25%；踩点必做（听真实噪声/走房间动线/测多点 Wi-Fi/看真实客房）；合同盯缩水房/取消条款/AV 加价/F&B 最低消费/30-40% 高管有特殊饮食；红绿灯：销售不回/报价模糊/Wi-Fi 差/不愿给参考=拒；隐私与舒适不达标=高管预期落空。",
        "how":"私密住宅式优先(6-14人)给诚实对话空间；目的地匹配目标+机场90分钟内；肩季省10-25%；必踩点(噪声/动线/Wi-Fi/真实客房)；合同盯AV加价/F&B最低消费/饮食复杂性。",
        "url":"https://www.offsite.com/blog/leadership-retreat-venue",
        "note":"适用：② 团建/务虚 选址策划（管理者/行政），私密物业+踩点清单+合同陷阱是可迁移硬货（exec 高管 retreat 同样适用）。",
        "section":"sec2","relation":"supervisor,exec","sourceType":"secondary"
    },
    {
        "emoji":"⚔️","title":"Offsite 战略推演·商业战争游戏（war-gaming）与去政治化",
        "cat":"战略推演","badge":"r3","src":"b2",
        "val":"高管 offsite 做战略，用「商业战争游戏」推演竞争者反击：分组扮演对手（「若你跳去竞对会怎么打我们」），给 3 轮反应-反制循环，把最极端场景逼出来反而能高质量讨论中间态；Monster 案例用 142 页 fact book 上墙+红绿黄 Post-it 标记共识/分歧/待数据，快速聚焦高分歧高重要议题。倡议过多时用「射箭练习」去政治化：把 42 个倡议写成贴纸贴到 5 个战略目标的靶上（靶心/外环/脱靶），自然 cull 掉对目标无直接影响的十几个，逼团队补留人等缺口倡议——比让 CEO 亲手砍「心头好」倡议更少政治阻力。⚠️ 时间框架须先对齐（「长期」对 A 是 10 年、对 B 是 10 季度）。",
        "how":"分组扮演竞对推 3 轮反应-反制；fact book 上墙+三色贴聚焦高分歧；射箭练习把倡议贴到目标靶上去政治化 cull；先对齐时间框架再讨论。",
        "url":"https://blog.strategicoffsites.com/insights-blog/offsites-that-work",
        "note":"适用：③ 高管战略务虚会，战争游戏推演+射箭练习去政治化是独特可迁移手法，区别于纯议程清单卡。",
        "section":"sec3","relation":"exec","sourceType":"secondary"
    },
    {
        "emoji":"🗣️","title":"Offsite 难题对话引导·CEO 不该主持自己 offsite",
        "cat":"冲突引导","badge":"r3","src":"b2",
        "val":"offsite 真正考验是房间变紧张时——沉默在领导层通常=不同意而非同意，当成默许是引导失败。三步框架化解张力：① 显式点名张力（「这里对 X 有明显分歧，摊开而非跳过」）② 把人与立场分开（让各方讲驱动立场的底层顾虑）③ 共创解题路径（定「什么信息/标准能让 group 做决定」+设 deadline）。关键红线：CEO 不该自己主持自己的 offsite——CEO 主持时其他高管会自我审查（研究证实），外部引导师才能创造无职业风险的开诚异议；高 stake offsite 里 CEO 应作为团队成员参与、不当 session 主持。四类常见张力处理：继任模糊（移离线+另设流程）/资源分配冲突（用数据标准+引导师把框）/战略分歧（先发散后收敛+pre-mortem 去人格化）/团队内低绩效者（移离线，绝不在 group 解）。",
        "how":"张力显式点名→人立场分离→共创路径+deadline；CEO 不主持自己 offsite（外部引导师换 candor）；个人绩效/薪酬/继任红线移离线。",
        "url":"https://georgedupontleadership.com/leadership-team-offsite-planning-guide-and-agenda-ideas/",
        "note":"适用：③ 高管 offsite 冲突引导，CEO 不主持自己会+三步张力框架+四类红线是可迁移亮点。",
        "section":"sec3","relation":"exec","sourceType":"secondary"
    },
    {
        "emoji":"🔄","title":"AAR 任务后复盘·把 offsite 变团队学习节奏",
        "cat":"复盘文化","badge":"r2","src":"b2",
        "val":"美军 AAR（任务后复盘）可迁移到高管 offsite 收尾：四问——目标是什么/实际发生什么/哪里好/下次哪不同；核心是无责难（blame-free）、只谈绩效不评人。高管团队 embedding AAR 能建心理安全+无责问责+暴露真障碍（非 KPI 表面）。落地：顶部脆弱感示范（「不为谁做错，为团队更锐」）；小但恒（15 分钟 huddle 也够，节奏 Plan→Execute→Debrief→Adjust→Repeat）；捕获并级联（洞察若被捕获可跨团队/区域放大，问「刚学到什么别人该知道」）。大多数企业只交付不学习——AAR 把经验转洞察、洞察转行动，是敏捷执行的关键机制。",
        "how":"四问无责难（目标/实际/好/不同）；顶部脆弱示范+小但恒（15min huddle）；捕获级联放大跨团队。",
        "url":"https://beperpetual.com/insights/articles/military-precision-to-boardroom-performancepart-3",
        "note":"适用：② 管理者带团队做 offsite 复盘文化（也适用 ③ 高管团队学习节奏），AAR 四问+无责难+级联是可迁移亮点。",
        "section":"sec2","relation":"supervisor,exec","sourceType":"secondary"
    },
]

def host_of(url):
    m = re.sub(r'^https?://', '', url)
    m = re.sub(r'^www\.', '', m)
    return m

def card_html(c):
    rel_text = "上下级" if c["badge"]=="r2" else "高管间"
    src_text = "一手" if c["src"]=="b1" else "二手"
    return f'''    <div class="hl">
      <div class="top"><span class="emoji">{c['emoji']}</span><h3>{c['title']}</h3><span class="cat">{c['cat']}</span><span class="badge {c['badge']}">{rel_text}</span><span class="badge {c['src']}">{src_text}</span></div>
      <p class="val">{c['val']}</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">{c['how']}</div></details>
      <div class="src">🔗 <a href="{c['url']}" target="_blank">{host_of(c['url'])}</a></div>
      <div class="note">{c['note']}</div>
    </div>
'''

STYLE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Offsite 团建务虚 · 知识采集卡片墙</title>
<style>
:root{
  --bg:#f4f6fb; --card:#ffffff; --ink:#1f2430; --sub:#5b6478;
  --accent:#6c5ce7; --accent2:#00b8d9; --chip:#eef0ff;
}
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
.sec1 .tag{background:#eaf2ff;color:#2b6cb0;} .sec1 h2{color:#2b6cb0;}
.sec .desc{font-size:12.5px;color:var(--sub);margin-left:2px;}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;}
.hl{background:var(--card);border-radius:18px;padding:18px 18px 16px;border-top:4px solid var(--accent);box-shadow:0 10px 32px rgba(108,92,231,.10);display:flex;flex-direction:column;gap:9px;}
.top{display:flex;align-items:center;gap:8px;flex-wrap:wrap;}
.emoji{font-size:22px;}
.hl h3{font-size:16px;font-weight:700;flex:1;min-width:120px;}
.cat{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:600;background:var(--chip);color:var(--accent);}
.badge{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:700;}
.b2{background:#fff1e6;color:#c0651a;}
.b1{background:#e6f9ed;color:#1a9e5a;}
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
@media(max-width:680px){.grid{grid-template-columns:1fr;}}
footer{text-align:center;padding:24px;color:#94a3b8;font-size:13px;border-top:1px solid #e2e8f0;margin-top:40px;}
</style>
</head>
<body>
<div class="wrap">'''

FOOTER = '''
  <footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>
</div>
</body>
</html>'''

# ---------- 1) incremental page ----------
sec3_inc = "".join(card_html(c) for c in cards if c["section"]=="sec3")
sec2_inc = "".join(card_html(c) for c in cards if c["section"]=="sec2")
n3 = sum(1 for c in cards if c["section"]=="sec3")
n2 = sum(1 for c in cards if c["section"]=="sec2")
inc_html = STYLE + f'''
<p style="margin:0 0 16px"><a href="./offsite.html" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">← 返回 Offsite 累计卡片墙</a></p>
  <div class="hero">
    <h1>🏔️ Offsite 团建务虚 · 本轮增量（2026-08-12 · +{len(cards)}）</h1>
    <p>本轮仅沉淀通过六维评估的 ②上下级 / ③高管间 卡；已剔除平级/朋友向。累计墙见 <a href="./offsite.html" style="color:#fff;text-decoration:underline">offsite.html</a>。</p>
    <div class="relbar">
      <span>② 领导↔员工（上下级，supervisor）</span>
      <span>③ 领导↔领导（高管间，exec）</span>
    </div>
  </div>
'''
if n3:
    inc_html += f'''
    <div class="sec sec3">
    <h2>③ 领导↔领导（高管间 · exec）</h2>
    <span class="tag">{n3} 卡</span>
    <span class="desc">本轮新增（仅高管间）</span>
  </div>
  <div class="grid">
{sec3_inc}  </div>
'''
if n2:
    inc_html += f'''
    <div class="sec sec2">
    <h2>② 领导↔员工（上下级，supervisor）</h2>
    <span class="tag">{n2} 卡</span>
    <span class="desc">本轮新增（含上下级/高管间混合）</span>
  </div>
  <div class="grid">
{sec2_inc}  </div>
'''
inc_html += FOOTER
tmp = INC_FILE + ".tmp"
open(tmp,"w",encoding="utf-8").write(inc_html)
os.replace(tmp, INC_FILE)
print("增量页:", INC_FILE, len(inc_html), "bytes")

# ---------- 2) update cumulative offsite.html ----------
html = open(HTML_FILE, encoding="utf-8").read()
# insert exec cards before sec3 grid close (before '<div class="sec sec2">')
sec2_idx = html.index('<div class="sec sec2">')
last_div_before_sec2 = html.rfind('</div>', 0, sec2_idx)
html = html[:last_div_before_sec2] + "".join(card_html(c) for c in cards if c["section"]=="sec3") + html[last_div_before_sec2:]
# insert supervisor cards before footer's closing grid div
foot_idx = html.index('<footer>')
last_div_before_foot = html.rfind('</div>', 0, foot_idx)
html = html[:last_div_before_foot] + "".join(card_html(c) for c in cards if c["section"]=="sec2") + html[last_div_before_foot:]
# update hero description
html = html.replace(
    "｜ 2026-08-10 八轮补采 +6</p>",
    "｜ 2026-08-10 八轮补采 +6 ｜ 2026-08-12 九轮补采 +5</p>")
# update section counts: sec3 35->36, sec2 23->27 (also fixes prior -1 drift)
html = html.replace('<span class="tag">35 卡</span>', '<span class="tag">36 卡</span>')
html = html.replace('<span class="tag">23 卡</span>', '<span class="tag">27 卡</span>')
tmp = HTML_FILE + ".tmp"
open(tmp,"w",encoding="utf-8").write(html)
os.replace(tmp, HTML_FILE)
print("汇总页:", HTML_FILE, "r3:",html.count('badge r3'),"r2:",html.count('badge r2'),"total hl:",html.count('class="hl"'))

# ---------- 3) update index.json ----------
data = json.load(open(INDEX_FILE, encoding="utf-8"))
existing_urls = set(x["url"] for x in data)
new_entries = []
added = 0
for c in cards:
    if c["url"] in existing_urls:
        print("跳过重复URL:", c["title"])
        continue
    entry = {
        "title": c["title"],
        "normKey": c["title"],
        "url": c["url"],
        "sourceType": c["sourceType"],
        "relation": c["relation"],
        "summary": c["val"],
        "topic": TOPIC,
        "source": "web"
    }
    new_entries.append(entry)
    added += 1
data.extend(new_entries)
tmp = INDEX_FILE + ".tmp"
json.dump(data, open(tmp,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
os.replace(tmp, INDEX_FILE)
print("index.json +", added, "-> total", len(data))

# save added for downstream (obsidian/lexiang)
json.dump([{"title":c["title"],"url":c["url"],"relation":c["relation"],"sourceType":c["sourceType"],"section":c["section"],"note":c["note"]} for c in cards],
          open(os.path.join(KC,"_offsite_r9_added.json"),"w",encoding="utf-8"), ensure_ascii=False, indent=2)
print("DONE build")
