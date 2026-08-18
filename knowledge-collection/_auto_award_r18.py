# -*- coding: utf-8 -*-
"""知识采集自动化 . 颁奖 十八轮 enrich（2026-08-18，同主题二次轮次）。
生成增量页 + 追加汇总页 + 更新 index.json + Obsidian 笔记 + 00索引。"""
import os, json

WS = r"C:\Users\v_yitcai\WorkBuddy\20260728154244"
KC = os.path.join(WS, "knowledge-collection")
AWARD = os.path.join(KC, "award")
AWARD_HTML = os.path.join(AWARD, "award.html")
IDX = os.path.join(KC, "index.json")
RUN_NAME = "award-20260818b.html"   # 同日二次轮次，b 后缀避与 R17 增量页同名
RUN_PATH = os.path.join(AWARD, RUN_NAME)
NOTE = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\award\颁奖-知识卡汇总.md"
IDX00 = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
GP = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection"

# ---- 6 张新卡（剔除 peer，仅 ②supervisor / ③exec）----
CARDS = [
  dict(emoji="\U0001F91D", title="即时认可（Spot Recognition）最佳实践·经理主导分发与公平框架", cat="经理认可", rel="r2",
       url="https://www.blueboard.com/blog/best-practices-spot-recognition-program",
       val="即时奖励（Spot Recognition）是经理级认可的核心杠杆——管理者是主要分发者，需先拿「领导 buy-in」（CEO/People 负责人官宣激发参与）+「经理培训」（让其理解如何用认可建信任、尤其在混合办公）；公平框架避免只奖 top 1% 而冷落多数，把奖励对齐岗位 JD 与价值观（GoPro 实践：经理给体现价值观的行为发奖）；设分级奖励（3-4 级，按影响与持续度）、审批护栏（HRBP/上级审批防滥用）、易用的提名通道。核心：把「年度念名字」升级为「日常高频、经理亲手、对行为而非结果」的认可。",
       inner="落地即时认可：①先获领导官宣 + 培训经理（含混合办公场景）；②把奖励对齐岗位 JD 与价值观，避免只奖明星；③设 3-4 级奖励对应不同影响度；④加审批护栏（HRBP/上级）防滥用；⑤用平台降低经理操作摩擦。经理用这套把认可从「HR 事务」变成「带团队的手感」。",
       note="适用：② 经理/一线主管主导的即时认可体系，把「被看见」做成日常机制而非年度仪式。"),
  dict(emoji="\U0001F9ED", title="价值观驱动认可·把「墙上价值观」翻译成可观察行为与公平基建", cat="价值观认可", rel="r2",
       url="https://www.xoxoday.com/blogs/empuls/values-based-recognition-program",
       val="价值观驱动认可（Values-Based Recognition）是把公司价值观变成「可见、可重复、可真实落地」的行为系统——三件套：①行为地图（每个价值观翻译成 3-5 个可观察行为，如「ownership」→「主动承接职责外客户升级」）；②认可渠道（平台/feed，经理与同事均可给，且同事权重等同）；③公平基础设施（按价值观/团队/地点/司龄交叉报表，暴露谁被看见、谁被忽略）。关键洞察：通用认可只追踪「可见产出」，价值观认可追踪「做事的方式」，二者结构性不同；经理-only 认可继承经理盲区（远程/安静贡献者被过滤），需叠加同事互认破除 line-of-sight 盲区（Gallup：仅 22% 员工觉得获得「适量」认可）。",
       inner="落地价值观认可：①把每条价值观拆成 3-5 个可观察行为（让任何人能指认）；②开放经理+同事双星认可，避免经理盲区；③建公平报表（按价值观/团队/地点/司龄交叉看分布）；④避免「贴价值观标签的通用表扬」——必须命名行为+价值。HR/经理用这套让文化从口号变日常。",
       note="适用：② HR/经理把「价值观」从海报做成可被认可、可被重复的真实行为。"),
  dict(emoji="\U0001F6E1", title="裁员/重组期认可·幸存者综合征下的「最需要却最先消失」", cat="变革期认可", rel="r2",
       url="https://www.advantageclub.ai/blog/employee-engagement-during-layoffs",
       val="裁员/重组后，认可往往是最先消失的，但此时「被看见」比平时更重要——留下的人常陷恐惧、愧疚、精力透支（survivor syndrome）。研究：认可频繁且真实嵌入文化的组织，员工相信「变化被管好」的可能性高 9 倍；若在变革期仍公开认可适应快/跨团队协作的人，能重建信心与归属感。做法：经理定期公开认可（会议点名+具体贡献）、庆祝小里程碑、真实具体（机械式表扬适得其反）、配以经理一对一稳定情绪；HR 提供「难对话」沟通支持与倾听通道。",
       inner="变革/裁员期维持认可：①经理在会议公开、具体地认可（避免「一切照旧」的虚假乐观）；②庆祝小里程碑重建 momentum；③把认可与「新 normal 的成功模样」挂钩；④真实优先——机械表扬伤信任；⑤配经理赋能（共情沟通+倾听）。HR/经理用这套在动荡期稳团队。",
       note="适用：② 经理/HR 在裁员重组等高压期用认可稳团队、防流失（③ 高管公开传递「无进一步裁员」等确定性信号与此互补）。"),
  dict(emoji="\U0001F527", title="一线班组长月度表彰·「考核—即时奖惩—标杆引领」驱动模式", cat="一线表彰", rel="r2",
       url="http://6j.powerchina.cn/col/col4470/art/2025/art_9d50efd24f274cfea92ab1a1455addcb.html",
       val="一线班组的「兵头将尾」激励范式（电力/煤矿等制造业实践）——「月度考核—即时奖惩—标杆引领」三驱：①月度考核（安全/生产/团队/培训四维量化，安全一票否决，当月津贴挂钩）；②即时奖惩（当月考核当月兑现，红黑榜公示正向激励+反向警示，形成「比学赶超」）；③标杆引领（月度评优秀班组长奖一线200/二线100元、年度累积评优集中表彰+末位淘汰）。班组长「责权利」绑定：赋紧急避险权/生产组织权/考核分配权 + 「经济+政治」双激励（津贴+外出培训/晋升资格）。经理/班组长用「即时认可法」（班前/班后会 2 分钟点名表扬 1-2 件具体好事）满足「被看见」需求。",
       inner="一线/蓝领团队表彰落地：①建「月度考核—当月兑现」即时奖惩闭环，红黑榜公示；②班组长赋权（考核分配权+津贴）+优秀班组长专项奖；③班前/班后会 2 分钟「具体好事即时认可」（当天说、说清楚做了啥为啥好、全班面前说）；④技能矩阵看板让成长可视化、「金点子时间」让一线从「被管」到「参与」。主管/班组长用这套激活最小作战单元。",
       note="适用：② 一线主管/班组长对蓝领、产线、施工团队的表彰与即时认可（制造业/工程场景，区别于白领 OKR 式认可）。"),
  dict(emoji="\U0001F4CB", title="生产车间奖惩制度·即时奖励提名→HR合规审核→公示→发放闭环", cat="合规闭环", rel="r2",
       url="https://www.renrendoc.com/paper/486885594.html",
       val="生产车间奖惩制度的标准化闭环（renrend 制度范本）——程序四步：①提名申请（即时奖励由班组长/车间主管现场观察直接提名填《即时奖励记录表》，附事由+贡献+金额，车间主任签字；定期奖励每月 25 日前由班组长据月度表现提交《月度奖励推荐表》附数据）；②审核公示（HR 合规审核真实性，定期候选名单车间公告栏公示 3 工作日接受监督，异议由 HR 牵头调查复核）；③审批发放（即时奖 HR 3 工作日内发，定期奖总经理审批、次月 5 日前发、注明类型事由）；④形式（现金/物品/福利，月度生产之星 800元、年度优秀 3000元 等）。要点：奖要「有标准、可追溯、受监督」，避免主管随意发、暗箱。",
       inner="主管/HR 落地车间奖惩：①即时奖励由主管现场提名+主任签字，附具体事由；②HR 做合规与真实性审核，定期奖公示 3 工作日接受异议；③奖金经审批后注明类型事由发放，避免「暗箱」；④物质+精神组合（现金/家电/年货），金额随效益动态调整。主管用这套把表彰做成「看得见的公平」。",
       note="适用：② 车间主管/HR 主导的生产一线奖惩合规闭环，把「表彰不发错、不偏袒」制度化。"),
  dict(emoji="\U0001F3C5", title="高管/CEO 外部获奖·雇主品牌与投资者信心的战略杠杆", cat="高管品牌", rel="r3",
       url="https://www.aspectusgroup.com/insights/the-top-ceo-awards-for-2026/",
       val="高管外部获奖（CEO Excellence Awards、European CEO of the Year、Global CEO Excellence、Cybersecurity Excellence「CEO of the Year」等）是战略品牌杠杆而非单纯荣誉——对营销/IR 团队：提升 CEO 个人 profile、强化投资者信心、支撑雇主品牌；关键是「奖项叙事与商业目标对齐」（创新/转型/可持续各有侧重），对外释放「领导被内外部双重认可」信号。选奖纪律：看准入围/颁奖日期、受众触达、是否第三方权威背书（shortlist/win 都是有用外部 stamp）；中小市值可用 LDC Top 50「无报名费」等低成本高杠杆奖项。对 HR/雇主品牌：高管获奖是「最好的雇主广告」——候选人更愿加入被认可的领导团队。",
       inner="高管对外获奖运营：①按「商业目标（创新/转型/可持续）×受众触达」选奖，不看名气看契合；②用 shortlist/win 做第三方背书，写进 IR/雇主品牌材料；③与其说是 CEO 个人荣誉，不如做成「组织领导力被认可」的战略叙事；④中小公司优先低门槛高杠杆奖（如 LDC Top 50 免报名费）。HR/IR/品牌用这套把「高管获奖」变成招聘与投资者沟通的弹药。",
       note="适用：③ 高管/HR/IR/品牌负责人把「高管获奖」做成雇主品牌与投资者信心的战略杠杆。"),
]

def card_html(c):
    badges = '<span class="badge %s">%s</span><span class="badge b2">二手</span>' % (
        c["rel"], "高管间" if c["rel"]=="r3" else "上下级")
    return ('''    <div class="hl">
      <div class="top"><span class="emoji">%s</span><h3>%s</h3><span class="cat">%s</span>%s</div>
      <p class="val">%s</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">%s</div></details>
      <div class="src">\U0001F517 <a href="%s" target="_blank">%s</a></div>
      <div class="note">适用：%s</div>
    </div>''' % (c["emoji"], c["title"], c["cat"], badges, c["val"], c["inner"], c["url"], c["url"], c["note"]))

sec3_cards = [c for c in CARDS if c["rel"]=="r3"]
sec2_cards = [c for c in CARDS if c["rel"]=="r2"]

# ---------- 1) 增量页 ----------
inc_grid = "\n".join(card_html(c) for c in CARDS)
inc_html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>颁奖典礼 . 十八轮增量卡片（2026-08-18）</title>
<style>
:root{--bg:#f4f6fb;--card:#ffffff;--ink:#1f2430;  --sub:#5b6478;--accent:#6c5ce7;--accent2:#00b8d9;--chip:#eef0ff;}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:linear-gradient(135deg,#eef1ff 0%,#e6f7ff 100%);color:var(--ink);padding:28px 18px;line-height:1.6;}
.wrap{max-width:1080px;margin:0 auto;}
.hero{background:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);border-radius:22px;padding:26px 30px;color:#fff;box-shadow:0 14px 40px rgba(108,92,231,.25);margin-bottom:22px;}
.hero h1{font-size:24px;font-weight:800;letter-spacing:1px;margin-bottom:6px;}
.hero p{font-size:13px;opacity:.95;}
.relbar{display:flex;gap:10px;flex-wrap:wrap;margin-top:12px;}
.relbar span{background:rgba(255,255,255,.2);border-radius:20px;padding:5px 14px;font-size:13px;font-weight:600;}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;}
.hl{background:var(--card);border-radius:18px;padding:18px 18px 16px;border-top:4px solid var(--accent);box-shadow:0 10px 32px rgba(108,92,231,.10);display:flex;flex-direction:column;gap:9px;}
.top{display:flex;align-items:center;gap:8px;flex-wrap:wrap;}
.emoji{font-size:22px;}
.hl h3{font-size:16px;font-weight:700;flex:1;min-width:120px;}
.cat{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:600;background:var(--chip);color:var(--accent);}
.badge{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:700;}
.b2{background:#fff1e6;color:#c0651a;}
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
</head><body>
<div class="wrap">
<p style="margin:0 0 16px"><a href="@@GP@@/award/award.html" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">\U0001F3C6 返回颁奖累计卡片墙 .</a> &nbsp; <a href="@@GP@@/index.html" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">\U0001F4DA 返回知识库门户 .</a></p>
  <div class="hero">
    <h1>\U0001F3C6 颁奖典礼 . 十八轮增量卡片（2026-08-18）</h1>
    <p>本轮新增 6 张（通过六维评估，剔除平级/朋友向①，仅 ②上下级 / ③高管间）；关系档：③高管间 1 张 + ②上下级 5 张。</p>
    <div class="relbar">
      <span>② 领导↔员工（上下级，supervisor）</span>
      <span>③ 领导↔领导（高管间，exec）</span>
    </div>
  </div>
  <div class="grid">
@@GRID@@
  </div>
<footer>\U0001F4CC 本页由 yitong 沉淀整理 . 文化活动知识库</footer>
</div>
</body></html>
'''.replace("@@GP@@", GP).replace("@@GRID@@", inc_grid)

with open(RUN_PATH, "w", encoding="utf-8") as f:
    f.write(inc_html)
print("增量页已写:", RUN_PATH, os.path.getsize(RUN_PATH), "字节")

# ---------- 2) 追加汇总页 award.html（稳健：注入到各 section grid 闭合 </div> 之前，保持 div 平衡）----------
html = open(AWARD_HTML, encoding="utf-8").read()

# hero 追加轮次标记
hero_old = "十七轮 enrich 2026-08-18(+6)"
hero_new = "十七轮 enrich 2026-08-18(+6) . 十八轮 enrich 2026-08-18(+6)"
if hero_old in html:
    html = html.replace(hero_old, hero_new, 1)
else:
    print("WARNING: hero 锚点未命中，跳过 hero 替换")

# sec3（高管间）卡片注入到 sec3 grid 闭合 </div> 之前
sec2_open = html.index('<div class="sec sec2">')
sec3_close = html.rfind("</div>", 0, sec2_open)
sec3_block = "\n".join(card_html(c) for c in sec3_cards)
html = html[:sec3_close] + "\n" + sec3_block + "\n" + html[sec3_close:]

# sec2（上下级）卡片注入到 sec2 grid 闭合 </div>（即 <footer> 之前最后一个 </div>）之前
footer_open = html.index("<footer>")
sec2_close = html.rfind("</div>", 0, footer_open)
sec2_block = "\n".join(card_html(c) for c in sec2_cards)
html = html[:sec2_close] + "\n" + sec2_block + "\n" + html[sec2_close:]

with open(AWARD_HTML, "w", encoding="utf-8") as f:
    f.write(html)
print("汇总页已更新:", AWARD_HTML, os.path.getsize(AWARD_HTML), "字节")

# ---------- 3) index.json ----------
data = json.load(open(IDX, encoding="utf-8"))
before = len(data)
for c in CARDS:
    data.append(dict(
        title=c["title"],
        normKey=c["title"],
        url=c["url"],
        sourceType="secondary",
        relation="exec" if c["rel"]=="r3" else "supervisor",
        summary=c["val"][:120],
    ))
json.dump(data, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("index.json:", before, "->", len(data), "(+%d)" % (len(data)-before))

# ---------- 4) Obsidian 笔记 ----------
note = open(NOTE, encoding="utf-8").read()
note = note.replace("共 103 张", "共 109 张", 1)
note = note.replace("**97 卡**", "**109 卡**", 1)   # 修正 适用&备注 段落陈旧计数
round_sec = "\n## 轮次 2026-08-18（十八轮 +6）\n本轮新增（均通过六维评估、仅 ②上下级 / ③高管间）：\n"
for c in CARDS:
    tag = "③高管间" if c["rel"]=="r3" else "②上下级"
    round_sec += "- %s（%s·二手）\n" % (c["title"], tag)
note = note.replace("## 卡片总表", round_sec + "\n## 卡片总表", 1)
# 追加表格行到文件末尾
new_rows = ""
for c in CARDS:
    rel_txt = "③高管间" if c["rel"]=="r3" else "②上下级"
    new_rows += "| %s（award/award.html） | 4 | 二手 | %s |  |\n" % (c["title"], rel_txt)
note = note.rstrip("\n") + "\n" + new_rows
open(NOTE, "w", encoding="utf-8").write(note)
print("Obsidian 笔记已更新:", NOTE)

# ---------- 5) 00 索引 ----------
idx00 = open(IDX00, encoding="utf-8").read()
idx00 = idx00.replace("**103 卡**", "**109 卡**", 1)
desc_tail = "元宇宙沉浸式颁奖。"
if desc_tail in idx00:
    idx00 = idx00.replace(desc_tail,
        desc_tail + "十八轮 enrich（2026-08-18 +6）：即时认可经理主导分发与公平框架、价值观驱动认可、裁员/重组期认可敏感性、一线班组长月度表彰闭环、车间生产奖惩合规闭环、高管外部获奖战略品牌杠杆（③1/②5）。", 1)
# 在颁奖典礼 section 末尾（下一 ## 主题： 之前）插入 6 行
marker = "## 主题：颁奖典礼"
if marker in idx00:
    si = idx00.index(marker)
    ni = idx00.index("## 主题：", si+10)
    rows = ""
    for c in CARDS:
        rel_txt = "③高管间" if c["rel"]=="r3" else "②上下级"
        rows += "| %s（award/award.html） | 4 | 二手 | %s |  |\n" % (c["title"], rel_txt)
    idx00 = idx00[:ni] + rows + idx00[ni:]
open(IDX00, "w", encoding="utf-8").write(idx00)
print("00 索引已更新:", IDX00)
print("DONE")
