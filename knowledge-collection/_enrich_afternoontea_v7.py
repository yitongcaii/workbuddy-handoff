#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os, re

KC = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(KC, "afternoontea", "afternoontea.html")
IDX = os.path.join(KC, "index.json")

# ---------- 5 new cards (all ② supervisor, no peer) ----------
cards = [
    dict(
        emoji="🍵", title="班组下午茶沟通会·一线情绪疏导与相互支招", cat="一线谈心",
        rel="r2", reltxt="上下级", src_type="b2", srctxt="二手",
        url="https://m.36dianping.com/dianping/59185",
        val="电销等高压一线团队，班组长定期组织班组下午茶沟通会，让员工倾诉工作难题、相互支招，缓解心理压力；员工成功开单时全场即时喊单表扬，共享成就感。主管化身「情感管家」，用轻松茶歇场景打破层级、掌握团队真实状态。",
        how="班组长固定频次开茶歇沟通会（非工作布置会）；设「倾诉+支招」双环节让员工互解；即时公开表扬微小进步；茶歇氛围降低防御、听到真话。",
        note="适用：② 一线班组长用下午茶场景做情绪疏导与相互支招，低成本的心理减压与团队凝聚。",
    ),
    dict(
        emoji="🌸", title="妈妈员工母亲节茶话会·吐槽大会+育儿分享", cat="女职工关怀",
        rel="r2", reltxt="上下级", src_type="b1", srctxt="一手",
        url="https://hailir.cn/newslist1-15/2790.html",
        val="海利尔药业奥迪斯工厂母亲节办「妈妈有话说」主题茶话会：20余位妈妈员工围坐，以「当妈后崩溃瞬间」开场做吐槽大会+育儿分享+温馨茶歇；从辅导作业到工作家庭平衡，真实槽点引发全场共鸣；结尾互赠拥抱。人力行政处表态持续办有温度的员工关怀活动，把「家文化」落到实处。",
        how="选母亲节等节点办妈妈员工专属茶话会；用「吐槽大会」破冰降低防御；茶歇+育儿分享双线；主管现场表态持续机制，避免一次性活动。",
        note="适用：② 女职工（妈妈员工）关怀茶话会，公司官网一手案例，「被看见被倾听」的治愈型团建。",
    ),
    dict(
        emoji="🎧", title="Z世代非正式倾听三通道·15分钟咖啡谈话", cat="倾听机制",
        rel="r2", reltxt="上下级", src_type="b2", srctxt="二手",
        url="https://www.kvalley.biz?p=24971/",
        val="针对「会上没意见、会后抱怨多」的Z世代信号，HR建三条低门槛非正式倾听通道并行：①15分钟咖啡谈话（每月一次）②异步文字频道（匿名提问箱）③员工随行见习（shadow主管半天）。配套主管3句「钥匙句」——「你最近哪件事最卡住」「再多讲一点」「你会建议我怎么做」（非暴力沟通逻辑）；有效互动=员工提观点+主管回应+30天内通知结果。",
        how="HR/主管开三条互补倾听通道（咖啡谈话/异步/见习）；用「钥匙句」替代「最近还好吗」封闭式提问；倾听必闭环（提观点→回应→30天知会结果），否则消耗信任。",
        note="适用：② HR/主管对Z世代员工的系统化非正式倾听，咖啡谈话是三条通道之一。",
    ),
    dict(
        emoji="🔄", title="虚拟咖啡轮盘·混合/远程团队主管咖啡", cat="远程连接",
        rel="r2", reltxt="上下级", src_type="b2", srctxt="二手",
        url="https://www.coffeepals.co/blog/how-managers-can-use-coffee-chats-to-improve-team-morale",
        val="混合/远程团队用虚拟咖啡轮盘（coffee roulette）工具自动随机匹配主管与成员、或跨团队成员进行15分钟视频咖啡；配套主题化（Goal Getter/What's Working/Just for Fun）、小组咖啡（2-4人）、对话卡（「这周让你笑的一件事」）。打破物理隔阂，让远程下属与主管、跨团队同事建立非正式连接，归属感+38%、新人上手时间-30%（BetterUp数据）。",
        how="用 CoffeePals 等工具设月度/季度自动随机匹配；主管带头参与虚拟咖啡；主题化+小组制+对话卡降低开口门槛；远程团队重点靠轮盘制造「偶遇」。",
        note="适用：② 混合/远程团队主管与下属的非正式咖啡连接，远程版下午茶社交。",
    ),
    dict(
        emoji="🍼", title="妈咪小屋定时下午茶·孕乳期女职工互助茶歇", cat="妈咪小屋",
        rel="r2", reltxt="上下级", src_type="b2", srctxt="二手",
        url="https://www.sohu.com/a/507115678_120099886",
        val="文山供电局升级「爱心妈咪小屋」后，每天下午三点半妈咪小屋下午茶准时开始，备孕/怀孕/哺乳期女职工围坐一边休息一边交流育儿经；配冰箱、消毒柜、微波炉、尿布台等设施。工会牵头，综合服务办承办，把妈咪小屋+定时下午茶做成女职工私密、安全、互助的温馨港湾，并配套育儿讲座、心理疏导座谈。",
        how="建妈咪小屋实体空间（隐私+设施）；设固定时段下午茶促成女职工日常互助；工会/综合服务办联合运营；配套育儿讲座与心理疏导形成关怀闭环。",
        note="适用：② 孕乳期女职工关怀，妈咪小屋+定时下午茶作为常态化互助茶歇机制。",
    ),
]

def card_html(c):
    return f'''    <div class="hl">
      <div class="top"><span class="emoji">{c['emoji']}</span><h3>{c['title']}</h3><span class="cat">{c['cat']}</span><span class="badge {c['rel']}">{c['reltxt']}</span><span class="badge {c['src_type']}">{c['srctxt']}</span></div>
      <p class="val">{c['val']}</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">{c['how']}</div></details>
      <div class="src">🔗 <a href="{c['url']}" target="_blank">{c['url']}</a></div>
      <div class="note">{c['note']}</div>
    </div>'''

NEW = "\n".join(card_html(c) for c in cards)

# ---------- HTML update (atomic) ----------
html = open(HTML, encoding="utf-8").read()

# dedup vs existing URLs
existing_urls = set(re.findall(r'href="([^"]+)"', html))
new_urls = [c['url'] for c in cards]
dup = [u for u in new_urls if u in existing_urls]
if dup:
    raise SystemExit("DUP URL in HTML: " + str(dup))

marker = "</div>\n\n  <footer>📌"
assert html.count(marker) == 1, f"marker count={html.count(marker)}"
html = html.replace(marker, NEW + "\n\n  </div>\n\n  <footer>📌", 1)

# sec2 count 26 -> 31
html = html.replace('<span class="tag">26 卡</span>', '<span class="tag">31 卡</span>')
# hero enrich note
html = html.replace(
    "｜ 五轮 enrich 2026-08-09（+6）｜",
    "｜ 五轮 enrich 2026-08-09（+6）｜ 七轮 enrich 2026-08-10（+5）｜",
)

tmp = HTML + ".tmp"
with open(tmp, "w", encoding="utf-8") as f:
    f.write(html)
os.replace(tmp, HTML)
print("HTML updated. new cards:", len(cards))

# ---------- index.json update ----------
idx = json.load(open(IDX, encoding="utf-8"))
idx_urls = set(e.get("url") for e in idx)
idx_norm = set(e.get("normKey") for e in idx)
added = 0
for c in cards:
    if c['url'] in idx_urls:
        print("SKIP dup url:", c['url']); continue
    norm = re.sub(r'[^a-z0-9一-鿿]', '', c['title'].lower())
    if norm in idx_norm:
        print("SKIP dup norm:", c['title']); continue
    idx.append(dict(
        title=c['title'], normKey=norm, url=c['url'],
        sourceType=("一手" if c['src_type'] == 'b1' else "二手"),
        relation="supervisor", summary=c['val'],
    ))
    idx_urls.add(c['url']); idx_norm.add(norm); added += 1

tmp2 = IDX + ".tmp"
with open(tmp2, "w", encoding="utf-8") as f:
    json.dump(idx, f, ensure_ascii=False, indent=2)
os.replace(tmp2, IDX)
print("index.json +", added, "-> total", len(idx))
