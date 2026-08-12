# -*- coding: utf-8 -*-
import json, os, re, shutil

BASE = "knowledge-collection"
TOP = "afternoontea"
HTML = os.path.join(BASE, TOP, f"{TOP}.html")
INC = os.path.join(BASE, TOP, f"{TOP}-20260812.html")
IDX = os.path.join(BASE, "index.json")
NOTE = "C:/Users/v_yitcai/Documents/Obsidian/知识采集库/素材/afternoontea/下午茶研讨-知识卡汇总.md"
IDX00 = "C:/Users/v_yitcai/Documents/Obsidian/知识采集库/00-知识采集索引.md"
RUN_DATE = "20260812"

# ---------- 1. 读取现有墙，提取 URL / 归一化标题 用于去重 ----------
html = open(HTML, encoding="utf-8").read()
existing_urls = set(re.findall(r'href="(https?://[^"]+)"', html))
def norm(t):
    return re.sub(r'[\s【】()（）\[\]【】“”"\'，,。.、:：!！?？]', '', t).lower()
existing_titles = set(norm(re.sub(r'<[^>]+>', '', t)) for t in re.findall(r'<h3>(.*?)</h3>', html, re.S))

# ---------- 2. 定义本轮新卡 ----------
# sec3 = ③高管间(r3) ; sec2 = ②上下级(r2) ; supervisor,exec 归入 sec2
CARDS = [
 {
  "emoji":"🤝","title":"Skip-level 跨级信任茶话会·高管与一线直接对话",
  "cat":"跨级沟通","relation":"supervisor,exec","sec":"sec2",
  "sourceType":"secondary","source":"hrsimple",
  "url":"https://hrsimple.com/skip-level-meeting",
  "display":"hrsimple.com/skip-level-meeting",
  "val":"跨级会议（senior leader 跳过直属经理，直接对话一线 individual contributors）是建信任、收集未过滤反馈、提升敬业度的关键场域。核心要点：会前先 brief 直属经理消除焦虑、明确「非评审·安全空间」；开场讲目的与保密承诺，员工说话占 70%；用 what/how/tell me about 开放式提问，绝不诱导或绕开经理；收尾给 1-2 个清晰下一步 + 跟进时间线；以咖啡/茶叙式轻松氛围替代正式会谈，季度/半年常态化才真诚（出问题才做会被视为作秀）。",
  "how":"落地建议：把跨级茶话会作为「高管↔一线」轻社交固定动作——选 8-12 名跨团队/跨层级代表，提前发议程与开放式问题集；领导者先分享脆弱再听；承诺「只共享主题不点名」，会后输出主题级复盘并闭环可见行动；绝不在危机时才开，避免被贴上「审查」标签。首轮可做成 coffee chat 式自由对话破冰。",
  "note":"适用：② 公司内部跨级场景（高管与一线员工，跳过直属经理的信任型茶叙；relation 含跨级，归入上下级档）",
 },
 {
  "emoji":"🍵","title":"深圳湾「湾里下午茶」·CEO 早茶会圈层私享",
  "cat":"圈层私享","relation":"exec","sec":"sec3",
  "sourceType":"secondary","source":"shenzhenware",
  "url":"https://shenzhenware.com/member_plan",
  "display":"shenzhenware.com/member_plan",
  "val":"深圳湾「湾享会」为科技/互联网/硬件产业链高管与创业精英的高端会员制私享会；其中「湾里下午茶·CEO 早茶会」每月 1 期，形式 = 闭门会 + 圆桌对话 + 私享小饭桌，围绕时下热点话题深度交流；核心圈层覆盖广深一线 C-level/VP/创始人，以「友直友谅友多闻」为价值主张，借茶叙场景完成认知共创与人脉链接。",
  "how":"借鉴点：把「高管早茶会」做成轻量闭门圆桌——定向邀约同频 C-level，以早茶/下午茶替代正式论坛，议题聚焦真实业务热点；闭门 + 小饭桌降低姿态、提升坦诚度，适合作为高管圈层关系经营的固定载体（非对外活动，纯内部/盟友圈层）。",
  "note":"适用：③ 高管间场景（科技/产业链 C-level 圈层私享茶会，构建同侪信任与人脉）",
 },
 {
  "emoji":"🎂","title":"退休欢送茶话会·中银公司 20 年「暖心茶」传统",
  "cat":"荣誉关怀","relation":"supervisor","sec":"sec2",
  "sourceType":"secondary","source":"epaper",
  "url":"https://epaper.zjgrrb.com/images/2015-09/29/z2015092900001.pdf",
  "display":"epaper.zjgrrb.com（张家港日报）",
  "val":"中银公司近 20 年坚持为每位退休职工办「欢送茶话会」：工会领导 + 所在部门经理与退休职工欢聚，喝暖心茶、吃甜心糖、嗑瓜子话家常；单位送「光荣退休」蛋糕 + 刻有本人姓名/入职时间的退休纪念金币；退休职工回部门给同事分喜糖。单 2004 年起已欢送 260+ 人、129+ 场，多为车间一线工人；后续还以「敲锣打鼓送职工」仪式送到家，家属共享荣誉感。",
  "how":"借鉴点：把退休关怀做成「茶话会 + 荣誉实物 + 家属在场」的温情闭环——领导/经理与退休员工围坐喝茶话别，颁发刻名纪念品与退休蛋糕，临别以仪式感送达并邀请参与后续公司活动；核心是「被看见、被感谢」，可作为高信氛围与雇主温度的固定载体。",
  "note":"适用：② 公司内部上下级场景（领导/工会↔退休员工，温情茶话会式欢送关怀）",
 },
 {
  "emoji":"🥂","title":"投资者关系闭门午餐会·非正式 IR 社交",
  "cat":"投资者关系","relation":"exec","sec":"sec3",
  "sourceType":"secondary","source":"roadshowchina",
  "url":"https://applet.10100.com/article/92164606",
  "display":"applet.10100.com（卓越IR/路演中）",
  "val":"卓越 IR（Roadshow China 路演中）分享的买方视角 IR 实践：除路演电话会外，每年不定期举办「闭门晚宴或午餐会」，通常由卖方分析师联席主持并邀请投资者参加；在更轻松环境中提供独特洞察，并让投资者一窥管理团队合作方式。核心 = 制度化高管曝光（不只让 CFO/CEO 路演，展示多元管理视角）+ 可扩展的非正式交流机制。",
  "how":"借鉴点：把投资者关系做成「闭门午宴/茶叙」轻社交——由 IR 牵头、分析师联席、定向邀约核心机构投资者，以午餐/下午茶替代大型路演；让多元高管与投资者在小场域坦诚对话，既传递战略深度、又建立长期信任。属 ③ 高管↔投资者关系经营。",
  "note":"适用：③ 高管间场景（公司高管↔机构投资者，闭门午餐/茶叙式 IR 关系经营）",
 },
 {
  "emoji":"🍃","title":"狮峰会·高端圈层茶会（西湖龙井核心产区）",
  "cat":"圈层茶会","relation":"exec","sec":"sec3",
  "sourceType":"secondary","source":"baidu",
  "url":"https://baike.baidu.com/item/%E7%8B%AE%E5%B3%B0%E4%BC%9A/66793935",
  "display":"baike.baidu.com/item/狮峰会",
  "val":"狮峰会是由杭州西湖龙井茶叶有限公司发起管理的高端会员制组织，以稀缺狮峰龙井茶为核心纽带：定期举办「高端茶会、闭门会议、文化论坛及主题沙龙」，为重视传统文化与生活美学的企业经营管理/文化艺术/学术研究/公共服务等领域精英，搭建以茶会友、思想交流、价值共创的圈层平台；强调专业、细节、开放、审美。",
  "how":"借鉴点：以「稀缺茶资源 + 高端茶会 + 闭门会议」组合运营高管圈层——用原产地茶文化做情感锚点，定期闭门茶叙促成同频精英的理念共鸣与资源互联；可作为 ③ 高管圈层关系经营的设计参考（注意：偏商业会员俱乐部，仅取「茶会+闭门」运营方法论，不照搬品牌/收费模式）。",
  "note":"适用：③ 高管间场景（高净值/精英圈层茶会式社交，仅取运营方法论参考）",
 },
]

# ---------- 3. 去重 ----------
accepted = []
removed = 0
for c in CARDS:
    u = c["url"]
    t = norm(c["title"])
    if u in existing_urls or t in existing_titles:
        removed += 1
        print("DUP skipped:", c["title"])
        continue
    accepted.append(c)
N = len(accepted)
print(f"去重后新增 N={N}，去重删 M={removed}")

# ---------- 4. 生成卡片 HTML ----------
def card_html(c):
    badge = "r3" if c["relation"] in ("exec",) else "r2"
    rel_txt = "高管间" if c["relation"] in ("exec",) else "上下级"
    src_badge = "b1" if c["sourceType"] == "primary" else "b2"
    src_txt = "一手" if c["sourceType"] == "primary" else "二手"
    return f'''    <div class="hl">
      <div class="top"><span class="emoji">{c['emoji']}</span><h3>{c['title']}</h3><span class="cat">{c['cat']}</span><span class="badge {badge}">{rel_txt}</span><span class="badge {src_badge}">{src_txt}</span></div>
      <p class="val">{c['val']}</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">{c['how']}</div></details>
      <div class="src">🔗 <a href="{c['url']}" target="_blank">{c['display']}</a></div>
      <div class="note">适用：{c['note']}</div>
    </div>
'''

sec3_cards = "".join(card_html(c) for c in accepted if c["sec"] == "sec3")
sec2_cards = "".join(card_html(c) for c in accepted if c["sec"] == "sec2")

# ---------- 5. 就地更新汇总页 afternoontea.html ----------
# ③ grid：插入到「② 上下级」注释之前（即 ③ grid 关闭 </div> 之前）
m2 = re.search(r'<!-- =+ ② 上下级 =+ -->', html)
idx_c2 = m2.start()
head = html[:idx_c2]
rest = html[idx_c2:]
# head 末尾最后一个 </div> 即 ③ grid 关闭
last_div = head.rfind("</div>")
head_new = head[:last_div] + sec3_cards + head[last_div:]
html2 = head_new + rest

# ② grid：插入到 <footer> 之前的 ② grid 关闭 </div> 之前
fidx = html2.index("<footer>")
before_footer = html2[:fidx]
ld = before_footer.rfind("</div>")
html3 = html2[:ld] + sec2_cards + html2[ld:]

# hero 轮次标注
html3 = html3.replace("八轮 enrich 2026-08-11(+6）", "八轮 enrich 2026-08-11(+6)")
html3 = html3.replace("八轮 enrich 2026-08-11(+6)", "八轮 enrich 2026-08-11(+6)｜ 九轮 enrich 2026-08-12(+5)")

# 校验结构
assert "本页由 yitong 沉淀整理" in html3
assert html3.count('class="hl"') == 60 + N, html3.count('class="hl"')
print("汇总页卡数:", html3.count('class="hl"'), "r3:", html3.count('class="badge r3"'), "r2:", html3.count('class="badge r2"'))

tmp = HTML + ".tmp"
open(tmp, "w", encoding="utf-8").write(html3)
os.replace(tmp, HTML)

# ---------- 6. 生成增量页 afternoontea-20260812.html ----------
def inc_page(cards_sec3, cards_sec2, n):
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>下午茶研讨 · 九轮 enrich 增量页（2026-08-12）</title>
<style>
:root{{--bg:#f4f6fb;--card:#ffffff;--ink:#1f2430;--sub:#5b6478;--accent:#6c5ce7;--accent2:#00b8d9;--chip:#eef0ff;}}
*{{box-sizing:border-box;margin:0;padding:0;}}
body{{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:linear-gradient(135deg,#eef1ff 0%,#e6f7ff 100%);color:var(--ink);padding:28px 18px;line-height:1.6;}}
.wrap{{max-width:1080px;margin:0 auto;}}
.hero{{background:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);border-radius:22px;padding:30px 32px;color:#fff;box-shadow:0 14px 40px rgba(108,92,231,.25);margin-bottom:22px;}}
.hero h1{{font-size:26px;font-weight:800;letter-spacing:1px;margin-bottom:8px;}}
.hero p{{font-size:14px;opacity:.95;}}
.relbar{{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px;}}
.relbar span{{background:rgba(255,255,255,.2);border-radius:20px;padding:5px 14px;font-size:13px;font-weight:600;}}
.sec{{margin:30px 0 12px;display:flex;align-items:center;gap:10px;}}
.sec h2{{font-size:19px;font-weight:800;}}
.sec .tag{{font-size:12px;padding:4px 12px;border-radius:12px;font-weight:700;}}
.sec3 .tag{{background:#f3e8ff;color:#7b2cbf;}} .sec3 h2{{color:#7b2cbf;}}
.sec2 .tag{{background:#fff3e0;color:#c0651a;}} .sec2 h2{{color:#c0651a;}}
.grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;}}
.hl{{background:var(--card);border-radius:18px;padding:18px 18px 16px;border-top:4px solid var(--accent);box-shadow:0 10px 32px rgba(108,92,231,.10);display:flex;flex-direction:column;gap:9px;}}
.top{{display:flex;align-items:center;gap:8px;flex-wrap:wrap;}}
.emoji{{font-size:22px;}}
.hl h3{{font-size:16px;font-weight:700;flex:1;min-width:120px;}}
.cat{{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:600;background:var(--chip);color:var(--accent);}}
.badge{{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:700;}}
.b2{{background:#fff1e6;color:#c0651a;}}
.b1{{background:#e6f9ed;color:#1a9e5a;}}
.r1{{background:#eaf2ff;color:#2b6cb0;}}
.r2{{background:#fff3e0;color:#c0651a;}}
.r3{{background:#f3e8ff;color:#7b2cbf;}}
.val{{font-size:13.5px;color:var(--sub);}}
.exec{{margin-top:2px;border-top:1px dashed #e2e8f0;padding-top:8px;}}
.exec summary{{cursor:pointer;font-size:13px;font-weight:600;color:var(--accent);}}
.exec .inner{{font-size:13px;color:var(--sub);margin-top:6px;padding-left:4px;}}
.src{{font-size:12px;word-break:break-all;}}
.src a{{color:var(--accent2);text-decoration:none;}}
.note{{font-size:12px;color:#94a3b8;border-left:3px solid #e2e8f0;padding-left:8px;}}
@media(max-width:680px){{.grid{{grid-template-columns:1fr;}}}}
footer{{text-align:center;padding:24px;color:#94a3b8;font-size:13px;border-top:1px solid #e2e8f0;margin-top:40px;}}
</style>
</head>
<body>
<div class="wrap">
<p style="margin:0 0 16px"><a href="afternoontea.html" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">← 返回累计总索引（afternoontea.html）</a></p>
  <div class="hero">
    <h1>🍵 下午茶研讨 · 九轮 enrich 增量页</h1>
    <p>本轮采集于 2026-08-12（+{n} 卡）｜ 仅含本轮回新增且通过六维评估的 ②上下级 / ③高管间 卡片（已剔除平级/朋友向）｜ 累计总墙见 afternoontea.html</p>
    <div class="relbar">
      <span>② 领导↔员工（上下级，supervisor）</span>
      <span>③ 领导↔领导（高管间，exec）</span>
    </div>
  </div>
  <div class="sec sec3"><h2>③ 领导↔领导（高管间 · exec）</h2><span class="tag">本轮回新增</span></div>
  <div class="grid">
{cards_sec3}  </div>
  <div class="sec sec2"><h2>② 领导↔员工（上下级 · supervisor）</h2><span class="tag">本轮回新增</span></div>
  <div class="grid">
{cards_sec2}  </div>
  <footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>
</div>
</body>
</html>
'''
open(INC, "w", encoding="utf-8").write(inc_page(sec3_cards, sec2_cards, N))
print("增量页字节:", os.path.getsize(INC))

# ---------- 7. 更新 index.json ----------
data = json.load(open(IDX, encoding="utf-8"))
for c in accepted:
    data.append({
        "normKey": norm(c["title"]),
        "relation": c["relation"],
        "source": c["source"],
        "sourceType": c["sourceType"],
        "summary": c["val"],
        "title": c["title"],
        "topic": TOP,
        "url": c["url"],
    })
json.dump(data, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("index.json 现总数:", len(data))

# ---------- 8. 更新 Obsidian 笔记 ----------
note = open(NOTE, encoding="utf-8").read()
note = note.replace("（60 卡 · 上下级/高管间）", "（65 卡 · 上下级/高管间）")
note = note.replace("八轮 enrich 2026-08-11(+6）", "八轮 enrich 2026-08-11(+6)")
note = note.replace("八轮 enrich 2026-08-11(+6)", "八轮 enrich 2026-08-11(+6)｜ 九轮 enrich 2026-08-12（+5）")
note = note.replace("## ③ 领导↔领导（高管间 · exec）— 18 卡", "## ③ 领导↔领导（高管间 · exec）— 21 卡")
note = note.replace("## ② 领导↔员工（上下级 · supervisor）— 42 卡", "## ② 领导↔员工（上下级 · supervisor）— 44 卡")

# ③ 表新行（插到 ## ② 之前）
sec3_rows = """| 19 | 深圳湾「湾里下午茶」·CEO 早茶会圈层私享 | 二手 | 科技/产业链 C-level 会员制私享会，每月早茶会=闭门圆桌+私享小饭桌，以茶叙做认知共创与人脉链接 |
| 20 | 投资者关系闭门午餐会·非正式 IR 社交 | 二手 | 卓越IR实践：闭门午宴/午餐会由 IR 牵头、分析师联席、定向邀约机构投资者，小场域坦诚对话建长期信任 |
| 21 | 狮峰会·高端圈层茶会（西湖龙井核心产区） | 二手 | 高端会员制以稀缺茶+高端茶会+闭门会议运营高管圈层，仅取「茶会+闭门」方法论参考 |
"""
note = note.replace("## ② 领导↔员工", sec3_rows + "## ② 领导↔员工", 1)

# ② 表新行（追加到文件末尾，接在 ② 表后）
sec2_rows = """
| 43 | Skip-level 跨级信任茶话会·高管与一线直接对话 | 二手 | 跨级会议：会前 brief 直属经理、咖啡茶叙式轻松氛围、员工说70%、开放式提问、闭环跟进，季度/半年常态化 |
| 44 | 退休欢送茶话会·中银公司 20 年「暖心茶」传统 | 二手 | 工会领导+部门经理与退休职工围坐喝茶话别，颁发刻名纪念品+退休蛋糕，温情闭环关怀 |
"""
note_round = f"""
## 轮次 20260812（+{N}）

> 九轮 enrich：新增 {N} 卡（③ 高管间 +3：深圳湾CEO早茶会 / 投资者关系闭门午餐会 / 狮峰会高端茶会；② 上下级 +2：跨级信任茶话会 / 退休欢送茶话会）。全部二手、无 peer、relation 仅取 supervisor/exec。
> 线上预览：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/afternoontea/afternoontea.html ｜ 本轮增量页：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/afternoontea/afternoontea-20260812.html
"""
note = note.rstrip() + "\n" + sec2_rows + note_round
open(NOTE, "w", encoding="utf-8").write(note)
print("笔记已更新")

# ---------- 9. 更新 00-知识采集索引.md ----------
idx0 = open(IDX00, encoding="utf-8").read()
idx0 = idx0.replace("｜ 2026-08-11 八轮 enrich +6）", "｜ 2026-08-11 八轮 enrich +6）")
idx0 = idx0.replace("｜ 2026-08-11 八轮 enrich +6)", "｜ 2026-08-11 八轮 enrich +6｜ 2026-08-12 九轮 enrich +5)")
idx0 = idx0.replace("**10 卡**", "**65 卡**")
# 在下午茶表末尾（下一个 ## 主题： 之前）插入新行
marker = "## 主题：下午茶研讨（"
si = idx0.index(marker)
# 找该段之后下一个 "## 主题：" （非下午茶）
rest = idx0[si:]
ni = rest.index("\n## 主题：", 1)
insert_at = si + ni
new_rows = (
 "| 深圳湾「湾里下午茶」·CEO 早茶会圈层私享（afternoontea.html） | 4 | 二手 | ③高管间 | 科技/产业链 C-level 会员制私享会，每月早茶会=闭门圆桌+私享小饭桌 |\n"
 "| 投资者关系闭门午餐会·非正式 IR 社交（afternoontea.html） | 4 | 二手 | ③高管间 | IR 牵头+分析师联席+定向邀约机构，闭门午宴建长期信任 |\n"
 "| 狮峰会·高端圈层茶会（西湖龙井核心产区）（afternoontea.html） | 4 | 二手 | ③高管间 | 稀缺茶+高端茶会+闭门会议运营高管圈层，仅取方法论 |\n"
 "| Skip-level 跨级信任茶话会·高管与一线直接对话（afternoontea.html） | 4 | 二手 | ②上下级 | 跨级会议：咖啡茶叙式、员工说70%、开放式提问、闭环跟进 |\n"
 "| 退休欢送茶话会·中银公司 20 年「暖心茶」传统（afternoontea.html） | 4 | 二手 | ②上下级 | 工会+部门经理与退休职工围坐喝茶话别，刻名纪念品+蛋糕 |\n"
)
idx0 = idx0[:insert_at] + new_rows + idx0[insert_at:]
open(IDX00, "w", encoding="utf-8").write(idx0)
print("00-索引已更新")

print("DONE N=", N)
