# -*- coding: utf-8 -*-
import json, os, re

KC = r"C:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection"
OBS = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库"
TODAY = "2026-08-14"
DATE8 = "20260814"
TOPIC = "afternoontea"

CARDS = [
 dict(emoji="\U0001F393", title="交大安泰中国CEO俱乐部·迎春茶话会圈层", cat="校友CEO圈层", rel="exec", src="二手",
   url="https://c.m.163.com/news/a/JM6TAPTH0516EA1E.html", disp="c.m.163.com/news/a/JM6TAPTH0516EA1E",
   val="交大安泰中国CEO俱乐部2025迎春茶话会：新老校友CEO/董事长/总裁齐聚，回顾年度、展望蓝图；理事长王均豪、会长黄影明等致辞，倡导「利益与发展共同体」「开放连接拓展资源」；以茶为媒凝聚校友企业家网络，常态化走访+读书会+游学+论坛联动，打造产学研落地与校友互助平台。",
   how="借鉴点：以「校友/同侪CEO俱乐部」为载体做高管圈层茶话会——固定年度迎春茶叙+常态化走访+读书会/游学/论坛联动，用「共同体」叙事替代招商路演；可迁移为公司高管校友/同窗圈的轻社交关系经营（属③高管间，定位商务化校友网络，区别于平级朋友向）。",
   note="③ 高管间场景（校友CEO/董事长↔董事长，俱乐部式圈层茶话会，商务化校友网络）"),
 dict(emoji="\U0001F4A1", title="独角兽资本下午茶·强筛选闭门沙龙", cat="资本圈层", rel="exec", src="二手",
   url="https://sh.huodongxing.com/event/8834728408100", disp="sh.huodongxing.com/event/8834728408100",
   val="上海「独角兽资本下午茶」：法式沙龙形式，仅限「好项目遇见好资本」——邀请真正具洞见力的资本人（投资人/资本大佬），含创始人分享价值观、资本大佬自我介绍、项目能级解析、点评问答匹配共识；强调「唯一性+使命」，实名审核、一人一票、不泛社交。",
   how="借鉴点：把高管/资本圈层下午茶做成「强筛选+强议题」的闭门沙龙——明确受众门槛（只限资本人/好项目）、固定议程（价值观→自我介绍→项目解析→匹配共识）、去水社交；可作③高管↔资本关系经营的轻量化范式（偏活动行招募，仅取「筛选+议题」方法论，不照搬收费/营销外壳）。",
   note="③ 高管间场景（创始人/项目方↔资本人，闭门资本下午茶式对接）"),
 dict(emoji="\U0001F91D", title="成都遂宁商会《遂商下午茶》·小而精私享", cat="商会私享", rel="exec", src="二手",
   url="https://www.toutiao.com/article/7544197694949802539/", disp="www.toutiao.com/article/7544197694949802539",
   val="成都遂宁商会第六期《遂商下午茶》暨《遂商家宴》：以茶为媒聚乡情、探传统行业创新；延续「一桌人以内」小规模，围绕「企业发展心得/行业趋势/合作需求」三大方向各抒己见；前5期已促成多项合作共识，成传统行业创新发展新思路；商会持续优化平台推动跨领域多层次合作。",
   how="借鉴点：以「小而精+一桌人」商会下午茶构建企业家私域圈层——控制规模保对话深度、固定三大议题（发展/趋势/合作）、以乡情/行业为情感锚点促成跨界合作；可作③企业家圈层茶叙的运营参考（属高管间，去地域/乡缘外壳取「小圈层+深对话」内核）。",
   note="③ 高管间场景（企业家/商会成员↔企业家，小而精商会下午茶私享）"),
 dict(emoji="☕", title="工会主席下午茶·一对一茶叙民主管理", cat="金融工会", rel="sup", src="二手",
   url="https://www.zjgrrb.cn/html/2025-12/24/content_146741_19157025.htm", disp="zjgrrb.cn/.../content_146741_19157025",
   val="浙江东方金融控股集团工会「工会有约」项目之「工会主席下午茶」：每月第二周周五，工会主席与职工代表一对一面对面茶叙，无严肃会议桌、无层层汇报；半年常态化，成连接管理层与职工心声纽带；一线骨干敞开心扉提职业瓶颈，转化为人才盘点/晋升优化依据；王经理带来「组建量化投资团队」金点子获跟进。",
   how="借鉴点：工会主席以「一对一、面对面、每月固定」的下午茶替代集体会议，营造宽松环境让「沉默大多数」说真话；把一线建议转化为人才盘点/机制优化动作；重点在「心贴心、一对一」，让工会从「发福利」变「发展助推器」。",
   note="② 公司内部上下级场景（工会主席↔职工代表，一对一茶叙民主沟通）"),
 dict(emoji="\U0001F3E2", title="海博物流党总支下午茶·改革攻坚连心桥", cat="国企党建", rel="sup", src="一手",
   url="https://www.brightfood.com/default/detail?id=41380", disp="brightfood.com/default/detail?id=41380",
   val="光明食品旗下海博物流党总支「下午茶」纪实：自群众路线教育起开展一对一下午茶，党总支书记/副书记每月下基层与一线码头/仓库/车间员工、基层中层「一对一」谈心；菜管家领导邀新员工咖啡蛋糕轻松谈，申配老国企「问情于民问计于民问需于民」架连心桥；改革攻坚期资源整合最难是人心融合，下午茶成凝聚人心抓手，新收购公司总经理借茶叙与老员工/新干部彼此熟悉加深了解。",
   how="借鉴点（国企/并购整合场景）：把下午茶做成改革攻坚期的「人心融合」工具——领导定期下一线上与一线/新收购团队一对一茶叙，去层级讲真话；重点在并购整合中加速新老团队彼此熟悉、凝聚共识；可与工会主席茶叙互补。",
   note="② 公司内部上下级场景（党总支书记/副书记↔一线职工与中层，改革攻坚期一对一茶叙连心）"),
 dict(emoji="\U0001F527", title="职工茶话会·开放吐槽+督办闭环", cat="工程一线", rel="sup", src="二手",
   url="https://finance.sina.com.cn/jjxw/2025-09-17/doc-infqtqhz5397737.shtml", disp="finance.sina.com.cn/.../doc-infqtqhz5397737",
   val="中铁上海局淮北地表水厂管网项目部每季度办「职工茶话会」：打破传统汇报式会议，管理人员与一线职工围坐，鼓励畅谈工作难点/生活点滴/职业成长；领导现场拍板能解决的、列入督办清单跟踪；推行以来采纳职工建议20余条，提升施工效率；设「技能微课堂」以老带新，并响应食堂/宿舍等生活需求。",
   how="借鉴点：把茶话会做成「开放吐槽+现场拍板+督办闭环+技能微课堂」的组合——领导人坐一圈去层级、鼓励提建议、能办即办、难办建账、以老带新；适合工程/一线项目部的常态化民主沟通与技能传承。",
   note="② 公司内部上下级场景（项目部领导班子↔一线职工，季度茶话会开放沟通+督办闭环）"),
 dict(emoji="\U0001F454", title="王校长的下午茶·董事长直连基层", cat="民企董事长", rel="sup", src="一手",
   url="http://www.tongdinggroup.com/aboutshow.asp?id=113", disp="tongdinggroup.com/aboutshow.asp?id=113",
   val="通鼎集团「王校长的下午茶」：每月单休周六，董事长王家新（兼通鼎大学校长）与基层员工面对面，围绕成长/企业/见闻真诚分享；已办12期、203名员工代表参与；按人群招募（一线操作工/新大学生/退役军人），鼓励讲实话讲心里话，邀请高管当面听意见；员工反映餐补/食堂加价等问题，职能部门立即约见供应商当场解决；党委思想动态报告当月解决70%、100天内完成剩余。",
   how="借鉴点：民企董事长以「每月固定+按人群招募+高管在场」的下午茶直连基层——领导先自我介绍破冰、鼓励讲真话、现场/限期解决真问题；配合党委思想动态月报形成「收集→整改→闭环」机制；可作②高管↔基层员工直连的标杆范式。",
   note="② 公司内部上下级场景（董事长↔基层员工/新大学生/退役军人，每月固定下午茶直连基层）"),
]

def rel_badge(rel): return "r3" if rel=="exec" else "r2"
def rel_text(rel):  return "高管间" if rel=="exec" else "上下级"
def src_badge(src): return "b1" if src=="一手" else "b2"

def card_html(c):
    return (
      '    <div class="hl">\n'
      '      <div class="top"><span class="emoji">%s</span><h3>%s</h3><span class="cat">%s</span>'
      '<span class="badge %s">%s</span><span class="badge %s">%s</span></div>\n'
      '      <p class="val">%s</p>\n'
      '      <details class="exec"><summary>怎么做</summary><div class="inner">%s</div></details>\n'
      '      <div class="src">\U0001F517 <a href="%s" target="_blank">%s</a></div>\n'
      '      <div class="note">适用：%s</div>\n'
      '    </div>\n'
    ) % (c["emoji"], c["title"], c["cat"], rel_badge(c["rel"]), rel_text(c["rel"]),
         src_badge(c["src"]), c["src"], c["val"], c["how"], c["url"], c["disp"], c["note"])

# ---------- 1. 汇总页 ----------
html_path = os.path.join(KC, TOPIC, TOPIC+".html")
html = open(html_path, encoding="utf-8").read()
applied = "十二轮 enrich 2026-08-14(+7)" in html
if not applied:
    opens = [m.start() for m in re.finditer(r'<div class="grid">', html)]
    def match_close(html, start):
        depth = 0; i = html.index(">", start) + 1
        while i < len(html):
            if html.startswith("<div", i):
                depth += 1; i = html.index(">", i) + 1
            elif html.startswith("</div>", i):
                if depth == 0: return i + len("</div>")
                depth -= 1; i += len("</div>")
            else:
                i = html.find("<", i)
                if i == -1: break
                i = html.index(">", i) + 1
        return -1
    grids = []
    for o in opens:
        cstart = html.index(">", o) + 1
        cend = match_close(html, o)
        inner = html[cstart:cend]
        is_exec = inner.count('badge r3') >= inner.count('badge r2')
        grids.append((o, cend, is_exec))
    exec_grid = [g for g in grids if g[2]]
    sup_grid  = [g for g in grids if not g[2]]
    assert exec_grid and sup_grid, "grid 分类失败"
    exec_block = "".join(card_html(c) for c in CARDS if c["rel"]=="exec")
    sup_block  = "".join(card_html(c) for c in CARDS if c["rel"]=="sup")
    ins = [(g[1], exec_block) for g in exec_grid] + [(g[1], sup_block) for g in sup_grid]
    ins.sort(reverse=True)
    for cp, blk in ins:
        html = html[:cp] + blk + html[cp:]
    html = html.replace('<span class="tag">25 卡</span>', '<span class="tag">28 卡</span>')
    html = html.replace('<span class="tag">49 卡</span>', '<span class="tag">53 卡</span>')
    html = html.replace('十一轮 enrich 2026-08-13(+3）</p>', '十一轮 enrich 2026-08-13(+3）｜ 十二轮 enrich 2026-08-14(+7）</p>')
    assert html.count("本页由 yitong") == 1, "footer 异常"
    open(html_path, "w", encoding="utf-8").write(html)
    print("summary 写入 OK, exec=%d sup=%d" % (exec_block.count('<div class="hl">'), sup_block.count('<div class="hl">')))
else:
    print("summary 已应用，跳过")

# ---------- 2. 增量页 ----------
inc_path = os.path.join(KC, TOPIC, "%s-%s.html" % (TOPIC, DATE8))
inc_cards = "".join(card_html(c) for c in CARDS)
inc_template = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>下午茶研讨 · 十二轮 enrich 增量页（2026-08-14）</title>
<style>
:root{--bg:#f4f6fb;--card:#ffffff;--ink:#1f2430;--sub:#5b6478;--accent:#6c5ce7;--accent2:#00b8d9;--chip:#eef0ff;}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:linear-gradient(135deg,#eef1ff 0%,#e6f7ff 100%);color:var(--ink);padding:28px 18px;line-height:1.6;}
.wrap{max-width:1080px;margin:0 auto;}
.hero{background:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);border-radius:22px;padding:30px 32px;color:#fff;box-shadow:0 14px 40px rgba(108,92,231,.25);margin-bottom:22px;}
.hero h1{font-size:26px;font-weight:800;letter-spacing:1px;margin-bottom:8px;}
.hero p{font-size:14px;opacity:.95;}
.relbar{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px;}
.relbar span{background:rgba(255,255,255,.2);border-radius:20px;padding:5px 14px;font-size:13px;font-weight:600;}
.back{margin:0 0 16px;}
.back a{display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;}
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
footer{text-align:center;padding:24px;color:#94a3b8;font-size:13px;border-top:1px solid #e2e8f0;margin-top:40px;}
</style>
</head>
<body>
<div class="wrap">
<p class="back"><a href="__TOPIC__.html">← 返回下午茶研讨·累计卡片墙</a></p>
  <div class="hero">
    <h1>🍵 下午茶研讨 · 十二轮 enrich 增量页</h1>
    <p>采集于 2026-08-14（本轮新增 7 卡）｜ 受众关系分层（仅②上下级 / ③高管间）｜ 六维评估含关系适配度 ｜ 一手/二手标注 ｜ 历史去重（老板私享局判 peer 排除）</p>
    <div class="relbar">
      <span>② 领导↔员工（上下级，supervisor）</span>
      <span>③ 领导↔领导（高管间，exec）</span>
    </div>
  </div>
  <div class="grid">
__CARDS__  </div>
<footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>
</div>
</body>
</html>
'''
inc_html = inc_template.replace("__TOPIC__", TOPIC).replace("__CARDS__", inc_cards)
open(inc_path, "w", encoding="utf-8").write(inc_html)
print("increment 写入 OK:", inc_path, len(inc_html.encode("utf-8")), "字节")

# ---------- 3. index.json ----------
idx_path = os.path.join(KC, "index.json")
idx = json.load(open(idx_path, encoding="utf-8"))
before = len(idx)
existing_urls = {x.get("url") for x in idx}
added = 0
for c in CARDS:
    if c["url"] in existing_urls:
        continue
    idx.append({
        "title": c["title"], "topic": TOPIC, "url": c["url"],
        "sourceType": c["src"], "relation": "exec" if c["rel"]=="exec" else "supervisor",
        "summary": c["val"],
        "key": re.sub(r"[\s\u3000]+", "", c["title"]).lower()
    })
    added += 1
json.dump(idx, open(idx_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("index.json %d -> %d (added %d)" % (before, len(idx), added))

# ---------- 4. 门户 ----------
portal = os.path.join(KC, "index.html")
p = open(portal, encoding="utf-8").read()
if "81 卡" not in p:
    p = p.replace('<div class="cnt">74 卡</div>', '<div class="cnt">81 卡</div>')
    p = p.replace('<div class="n">428</div>', '<div class="n">435</div>')
    p = p.replace('<div class="l">428 张知识卡</div>', '<div class="l">435 张知识卡</div>')
    open(portal, "w", encoding="utf-8").write(p)
    print("portal 更新 OK: 74->81, 428->435")
else:
    print("portal 已更新，跳过")

# ---------- 5. Obsidian 笔记 ----------
note_path = os.path.join(OBS, "素材", TOPIC, "下午茶研讨-知识卡汇总.md")
note = open(note_path, encoding="utf-8").read()
if "81 卡" not in note:
    note = note.replace("下午茶研讨 · 知识卡汇总（74 卡", "下午茶研讨 · 知识卡汇总（81 卡")
    note = note.replace("## ③ 领导↔领导（高管间 · exec）— 25 卡", "## ③ 领导↔领导（高管间 · exec）— 28 卡")
    note = note.replace("## ② 领导↔员工（上下级 · supervisor）— 47 卡", "## ② 领导↔员工（上下级 · supervisor）— 51 卡")
if "轮次 2026-08-14（+7）" not in note:
    round_block = '''
## 轮次 2026-08-14（+7）

> 十二轮 enrich：新增 7 卡（③ 高管间 +3：交大安泰中国CEO俱乐部迎春茶话会 / 独角兽资本下午茶 / 成都遂宁商会遂商下午茶；② 上下级 +4：工会主席下午茶 / 海博物流党总支下午茶纪实 / 职工茶话会 / 王校长的下午茶）。一手 2 + 二手 5，无 peer，relation 仅取 supervisor/exec；老板私享局（平级老板互撩式资源局）判 peer 排除。
> 线上预览：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/afternoontea/afternoontea.html ｜ 本轮增量页：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/afternoontea/afternoontea-20260814.html

| 26 | 交大安泰中国CEO俱乐部·迎春茶话会圈层 | 二手 | 校友CEO/董事长俱乐部年度迎春茶叙+常态化走访/读书会/游学/论坛联动，以「共同体」凝聚校友企业家网络 |
| 27 | 独角兽资本下午茶·强筛选闭门沙龙 | 二手 | 仅限资本人/好项目的闭门沙龙：价值观→自我介绍→项目解析→匹配共识，强筛选+强议题去水社交 |
| 28 | 成都遂宁商会《遂商下午茶》·小而精私享 | 二手 | 「一桌人以内」商会下午茶：固定发展/趋势/合作三议题，以乡情/行业为锚促成跨界合作 |
| 50 | 工会主席下午茶·一对一茶叙民主管理 | 二手 | 月频一对一茶叙(无会议桌)，一线谈瓶颈，建议转人才盘点/机制优化，工会从发福利变发展助推器 |
| 51 | 海博物流党总支下午茶·改革攻坚连心桥 | 一手 | 党总支书记每月下基层一对一谈心，改革攻坚期作人心融合工具，新收购公司总经理借茶叙熟团队 |
| 52 | 职工茶话会·开放吐槽+督办闭环 | 二手 | 季度茶话会：开放吐槽+现场拍板+督办清单+技能微课堂，工程/一线项目部常态化民主沟通 |
| 53 | 王校长的下午茶·董事长直连基层 | 一手 | 民企董事长每月固定+按人群招募+高管在场直连基层，配合党委思想动态月报形成收集→整改闭环 |
'''
    note = note.rstrip() + "\n" + round_block
    open(note_path, "w", encoding="utf-8").write(note)
    print("obsidian 笔记更新 OK")
else:
    print("obsidian 笔记已更新，跳过")

# ---------- 6. 00-索引 ----------
zidx_path = os.path.join(OBS, "00-知识采集索引.md")
z = open(zidx_path, encoding="utf-8").read()
if "十二轮 enrich +7" not in z:
    z = z.replace("下午茶研讨（2026-08-06 首轮 ｜ 2026-08-07 二轮补采 ｜ 2026-08-08 三轮 enrich +5 ｜ 2026-08-08 四轮 enrich +11 ｜ 2026-08-09 五轮 enrich +6 ｜ 2026-08-10 七轮 enrich +5 ｜ 2026-08-11 八轮 enrich +6 ｜ 2026-08-13 十轮 enrich +6 ｜ 2026-08-13 十一轮 enrich +3）",
                  "下午茶研讨（2026-08-06 首轮 ｜ 2026-08-07 二轮补采 ｜ 2026-08-08 三轮 enrich +5 ｜ 2026-08-08 四轮 enrich +11 ｜ 2026-08-09 五轮 enrich +6 ｜ 2026-08-10 七轮 enrich +5 ｜ 2026-08-11 八轮 enrich +6 ｜ 2026-08-13 十轮 enrich +6 ｜ 2026-08-13 十一轮 enrich +3 ｜ 2026-08-14 十二轮 enrich +7）")
    z = z.replace("**71 卡**", "**81 卡**")
    anchor = "## 主题：员工大会（2026-08-07 首采"
    rows = (
"| 交大安泰中国CEO俱乐部·迎春茶话会圈层（afternoontea.html） | 4 | 二手 | ③高管间 | 校友CEO/董事长俱乐部年度迎春茶叙+常态化走访/读书会/游学/论坛联动，以「共同体」凝聚校友企业家网络 |\n"
"| 独角兽资本下午茶·强筛选闭门沙龙（afternoontea.html） | 4 | 二手 | ③高管间 | 仅限资本人/好项目的闭门沙龙：价值观→自我介绍→项目解析→匹配共识，强筛选+强议题去水社交 |\n"
"| 成都遂宁商会《遂商下午茶》·小而精私享（afternoontea.html） | 4 | 二手 | ③高管间 | 「一桌人以内」商会下午茶：固定发展/趋势/合作三议题，以乡情/行业为锚促成跨界合作 |\n"
"| 工会主席下午茶·一对一茶叙民主管理（afternoontea.html） | 4 | 二手 | ②上下级 | 月频一对一茶叙(无会议桌)，一线谈瓶颈，建议转人才盘点/机制优化 |\n"
"| 海博物流党总支下午茶·改革攻坚连心桥（afternoontea.html） | 4 | 一手 | ②上下级 | 党总支书记每月下基层一对一谈心，改革攻坚期作人心融合工具，新收购公司总经理借茶叙熟团队 |\n"
"| 职工茶话会·开放吐槽+督办闭环（afternoontea.html） | 4 | 二手 | ②上下级 | 季度茶话会：开放吐槽+现场拍板+督办清单+技能微课堂，工程/一线项目部常态化民主沟通 |\n"
"| 王校长的下午茶·董事长直连基层（afternoontea.html） | 4 | 一手 | ②上下级 | 民企董事长每月固定+按人群招募+高管在场直连基层，配合党委思想动态月报形成收集→整改闭环 |\n"
    )
    z = z.replace(anchor, rows + anchor, 1)
    open(zidx_path, "w", encoding="utf-8").write(z)
    print("00-索引 更新 OK")
else:
    print("00-索引 已更新，跳过")
print("DONE")
