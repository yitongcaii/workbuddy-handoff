# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""Award 二十二轮 enrich (2026-08-22) · 增量页+汇总页+index.json+Obsidian+乐享上传。
仅 ②上下级 / ③高管间，剔除①平级/朋友向。"""
import json, os, re, urllib.request, urllib.error, datetime

BASE = os.path.dirname(os.path.abspath(__file__))
AWARD_DIR = os.path.join(BASE, "award")
RUN_NAME = "award-20260822.html"
RUN_PATH = os.path.join(AWARD_DIR, RUN_NAME)
DATE = "2026-08-22"
ROUND_LABEL = "二十二轮增量卡片（2026-08-22）"
# 乐享 award 子文件夹
FOLDER = "f585d1b78510459db0ce807cc9688448"

# ---------- 候选卡（六维评估通过，仅 supervisor/exec） ----------
CARDS = [
    {
        "emoji":"🏆","cat":"创新表彰","relation":"supervisor","relchip":"上下级","relbadge":"r2",
        "source":"一手",
        "title":"职工技术创新成果奖·政府官方评审 SOP（分等次+专家评审委+公示异议）",
        "url":"https://www.hefei.gov.cn/public/1741/40408761.html",
        "val":"合肥市政府《职工技术创新成果奖励办法》：奖项分特/一/二/三/参评五等次（按行业领先水平+经济增加值门槛，如特等奖 EVA≥500万）；评审由市劳动竞赛委员会组织实施，下设办公室（市总工会）+专家评审委；申报经企事业单位工会→县区/产业工会→市总，四阶段（材料申报→审核→专家评估→评审委评审）；拟授奖项目市级媒体公示10天，异议书面反映、办公室核查→委员会决定；由市政府颁发证书+奖金。机制要点：标准量化分级、第三方专家评审、公示+异议复核防偏袒、政府背书增公信力。",
        "howto":"①按创新经济/社会/环境效益分等次设门槛（特等奖 EVA≥500万、一等奖≥200万）；②建「总工会+专家评审委」第三方评审，主管不直定；③拟授奖名单媒体公示10天+书面异议复核通道；④由单位/政府背书颁奖，增强公信力；⑤把创新奖与专利/技改/推广价值绑定而非仅论文。",
        "note":"② 政府/国企/工会把职工创新成果奖做成「分等次+专家评审+公示异议」的公平治理 SOP（企业内嵌版见「员工创新激励考核管理办法」）。"
    },
    {
        "emoji":"⭐","cat":"一线表彰","relation":"supervisor","relchip":"上下级","relbadge":"r2",
        "source":"一手",
        "title":"服务之星评选·一线基层员工月度/季度/年度表彰（分管领导任组长+明查暗访复核）",
        "url":"http://www.gzjtkgjt.com/wqzl/199.jhtml",
        "val":"赣州高速「橙乡服务之星」管理办法（企业官方一手）：评选原则公平公开、每年底评10名；标准含服务水平/工作态度/个人能力/民主评价（零投诉、全勤、民主投票≥60%支持）；评选机构由公司分管运营领导任组长，HR牵头，办公室/党群/监察审计多部门参与；步骤=基层所（部）推荐→运营公司审核→公司评选小组明查暗访+问卷复核定名单；奖励2000元+通报表彰。机制要点：一线为主、管理层+监察多方把关、暗访复核防形式、零投诉一票否决。",
        "howto":"①评选项目向一线基层倾斜，管理层为辅；②成立「分管领导+HR+监察」多方评选组，避免部门自定；③基层推荐+明查暗访/神秘客户复核，防材料粉饰；④零有效投诉/违纪一票否决；⑤奖励与通报+宣传栏上墙结合，强化榜样。",
        "note":"② 一线主管/HR 把「服务之星」做成月度/季度/年度基层表彰，多方把关+暗访复核（通用企业版评选方案见另卡）。"
    },
    {
        "emoji":"🌟","cat":"青年表彰","relation":"supervisor","relchip":"上下级","relbadge":"r2",
        "source":"一手",
        "title":"全国青年岗位能手·团中央官方评选表彰办法（向基层延伸+监督公示+纪律）",
        "url":"https://news.youth.cn/gn/202104/t20210407_12835491.htm",
        "val":"共青团中央《全国青年岗位能手评选表彰管理办法》：推荐人选16-35岁、精通本职/技能高超/创新贡献突出；评选由共青团中央+人社部联合实施，一般每两年一次；突出向基层团支部、企业班组延伸；程序含推荐考察、审核、监督公示、纪律要求；明确「一般不作为推荐对象」情形（副厅级以上、企业董监高、团专职干部等）防关系；与推优入党、「青马工程」、推优荐才衔接。机制要点：政治标准+技能实绩、向一线倾斜、公示监督+严禁说情打招呼/优亲厚友。",
        "howto":"①推荐向基层一线青年倾斜，设年龄/技能硬门槛；②程序透明：基层推荐→考察审核→公示→审定，开异议通道；③纪律「五严禁」（说情打招呼/优亲厚友/个人说了算/以权谋私/弄虚作假）；④与推优入党、人才培养衔接，让表彰成发展通道而非终点；⑤宁缺毋滥，突出先进性。",
        "note":"② 团委/HR 把青年岗位能手做成「官方标准+基层延伸+公示监督+纪律」的规范表彰（地方实践「三从严/四必须/五严禁」见另卡）。"
    },
    {
        "emoji":"🏅","cat":"组织级荣誉","relation":"exec","relchip":"高管间","relbadge":"r3",
        "source":"一手",
        "title":"省长/董事长质量奖·政府最高质量荣誉+一把手亲颁（组织级战略认可）",
        "url":"https://www.tsingtao.com.cn/news/077B2CF5-7BEF-4AE2-94B9-0F00736B1BA0.html",
        "val":"省长质量奖是省级政府设立的最高质量奖项（如山东每两年一届），由省委副书记/省长出席并向企业董事长/负责人亲自颁奖，表彰其在创建先进质量管理模式、推广科学质量理念、对质量强省建设的突出贡献；流程含舆情调查→资格审查→材料评审→现场评审→陈述答辩→公示→省政府批准→表彰资助（如内蒙古主席质量奖资助100万）。企业视角（得利斯/青啤）：董事长获省长质量奖是对企业质量管理体系与「质量为先」战略的顶级背书，直接转化为品牌公信力与投资者信心。机制要点：政府一把手↔企业一把手的高层互认、公开评审+公示、战略绑定（质量强省）。",
        "howto":"①企业把「创省长/市长质量奖」写入质量战略，由一把手牵头；②对标卓越绩效模式（领导/战略/顾客/资源/过程/测量/结果 1000分框架）；③材料评审+现场评审+陈述答辩三关+政府公示，确保公信力；④获奖后由董事长对外发声，把荣誉转品牌/雇主品牌资产；⑤政府侧：省长亲颁传递「质量优先」战略信号。",
        "note":"③ 政府领导↔企业董事长把质量奖做成「一把手亲颁+公开评审+战略绑定」的顶级组织级认可（组织内部 President's Award 见另卡）。"
    },
    {
        "emoji":"📊","cat":"ROI度量","relation":"exec","relchip":"高管间","relbadge":"r3",
        "source":"二手",
        "title":"认可项目 ROI 测算框架·给 CHRO/CFO 的投入产出度量（5步法+dashboard）",
        "url":"https://walloffame.cloud/recognition-program-roi-calculator",
        "val":"walloffame「Recognition Program ROI Calculator」：认可项目不应只算奖品成本，要建立可复现 ROI 模型——①定义度量周期（月/季/年，匹配颁奖频率）；②算总成本（奖品+证书+物流+活动+平台订阅+管理员与经理耗时）；③选2-3个结果指标（参与率/提名完成率/自愿离职/缺勤/内部流动/敬业度/客户好评/目标完成）；④仅在有可信方法处赋值（如替换成本、生产率提升），不确定用区间而非硬点估计；⑤与基线（上期/对照团队）比较。配套 dashboard KPI：合格员工数、独立提名人数、提名数、发卡数、部门参与率、提名→公布时长、重复获奖者、绑定价值观的奖项占比。",
        "howto":"①先定周期与成本全口径（含经理提名耗时）；②选少量结果指标，参与率用「独立参与员工÷合格员工」且跨期定义一致；③可信处才赋值 ROI，否则成本与结果指标分开报；④用 low/mid/high 区间而非单点；⑤dashboard 先盯「获奖者留任+经理提名参与率」两个健康度信号向董事会汇报。",
        "note":"③ CHRO/CFO 用可复现 ROI 模型向董事会证明认可预算合理、避免「软支出」被砍（与「荣誉体系数据汇报与ROI指标框架」互补）。"
    },
    {
        "emoji":"🤝","cat":"包容认可","relation":"exec","relchip":"高管间","relbadge":"r3",
        "source":"二手",
        "title":"多元包容 DEI 表彰·高管站台式认可（移除给/得限制+一线不掉队）",
        "url":"https://www.hrmagazine.co.uk/content/comment/looking-at-recognition-through-a-dei-lens/",
        "val":"HR Magazine「Looking at recognition through a DEI lens」+ UD Trucks Thailand 案例：把 DEI 织入认可设计——①移除「谁能给认可」的限制（不只 manager-only，改 peer/crowdsourcing，避免 them-and-us 分裂）；②移除「谁能得认可」的限制（不设固定获奖名额，按成就灵活，equal opportunity recognition）；③移除参与障碍（无手机/非英语一线员工也通过 TV 直播墙/HR 美化提名获得平等机会）；④高管赞助+公开表彰（UD Trucks 高管主持倾听论坛+认可活动、CEO 致谢，新员工离职率 16.07%→9.30%，2016 起零劳动/公平投诉）。机制要点：认可公平性是设计问题，高管定调+去层级+一线可达。",
        "howto":"①审计现有认可计划是否排他（仅 manager 给/固定名额/一线无渠道）；②打开给认可权限（peer/crowdsourcing），扩大认可时刻；③设灵活名额+多元奖项覆盖各类贡献；④为无数字设备/非母语一线建平等参与通道（直播墙/翻译美化）；⑤高管公开赞助 DEI 表彰，把包容认可写入战略。",
        "note":"③ 高管把多元包容认可作战略议题、去层级+一线可达（D&I 奖项设计框架/女性领导力表彰见另卡）。"
    },
]

def esc(s):
    return s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

def card_inner(c, rel_in_top=True):
    rel = '<span class="badge {0}">{1}</span>'.format(c["relbadge"], c["relchip"])
    srcbadge = '<span class="badge b2">{0}</span>'.format(c["source"])
    top = '<div class="top"><span class="emoji">{emoji}</span><h3>{title}</h3><span class="cat">{cat}</span>{rel}{src}</div>'.format(
        emoji=c["emoji"], title=esc(c["title"]), cat=c["cat"], rel=rel, src=srcbadge)
    val = '<p class="val">{0}</p>'.format(esc(c["val"]))
    ex = '<details class="exec"><summary>怎么做</summary><div class="inner">{0}</div></details>'.format(esc(c["howto"]))
    sr = '<div class="src">🔗 <a href="{0}" target="_blank">{0}</a></div>'.format(c["url"])
    nt = '<div class="note">适用：{0}</div>'.format(esc(c["note"]))
    return top+val+ex+sr+nt

def card_block(c, indent=4):
    sp = " "*indent; sp2=" "*(indent+2)
    return '{sp}<div class="hl">\n{sp2}{inner}\n{sp}</div>'.format(sp=sp, sp2=sp2, inner=card_inner(c))

# ---------- 1) 增量页 ----------
n_exec = sum(1 for c in CARDS if c["relation"]=="exec")
n_sup = sum(1 for c in CARDS if c["relation"]=="supervisor")
inc_cards = "\n".join(card_block(c, 4) for c in CARDS)
inc_html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>颁奖典礼 . {round} 增量卡片</title>
<style>
:root{{--bg:#f4f6fb;--card:#ffffff;--ink:#1f2430;  --sub:#5b6478;--accent:#6c5ce7;--accent2:#00b8d9;--chip:#eef0ff;}}
*{{box-sizing:border-box;margin:0;padding:0;}}
body{{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:linear-gradient(135deg,#eef1ff 0%,#e6f7ff 100%);color:var(--ink);padding:28px 18px;line-height:1.6;}}
.wrap{{max-width:1080px;margin:0 auto;}}
.hero{{background:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);border-radius:22px;padding:26px 30px;color:#fff;box-shadow:0 14px 40px rgba(108,92,231,.25);margin-bottom:22px;}}
.hero h1{{font-size:24px;font-weight:800;letter-spacing:1px;margin-bottom:6px;}}
.hero p{{font-size:13px;opacity:.95;}}
.relbar{{display:flex;gap:10px;flex-wrap:wrap;margin-top:12px;}}
.relbar span{{background:rgba(255,255,255,.2);border-radius:20px;padding:5px 14px;font-size:13px;font-weight:600;}}
.grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;}}
.hl{{background:var(--card);border-radius:18px;padding:18px 18px 16px;border-top:4px solid var(--accent);box-shadow:0 10px 32px rgba(108,92,231,.10);display:flex;flex-direction:column;gap:9px;}}
.top{{display:flex;align-items:center;gap:8px;flex-wrap:wrap;}}
.emoji{{font-size:22px;}}
.hl h3{{font-size:16px;font-weight:700;flex:1;min-width:120px;}}
.cat{{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:600;background:var(--chip);color:var(--accent);}}
.badge{{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:700;}}
.b2{{background:#fff1e6;color:#c0651a;}}
.r2{{background:#fff3e0;color:#c0651a;}}
.r3{{background:#f3e8ff;color:#7b2cbf;}}
.val{{font-size:13.5px;color:var(--sub);}}
.exec{{margin-top:2px;border-top:1px dashed #e2e8f0;padding-top:8px;}}
.exec summary{{cursor:pointer;font-size:13px;font-weight:600;color:var(--accent);}}
.exec .inner{{font-size:13px;color:var(--sub);margin-top:6px;padding-left:4px;}}
.src{{font-size:12px;word-break:break-all;}}
.src a{{color:var(--accent2);text-decoration:none;}}
.note{{font-size:12px;color:#94a3b8;border-left:3px solid #e2e8f0;padding-left:8px;}}
footer{{text-align:center;padding:24px;color:#94a3b8;font-size:13px;border-top:1px solid #e2e8f0;margin-top:40px;}}
</style></head><body>
<div class="wrap">
<p style="margin:0 0 16px"><a href="https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/award.html" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">🏆 返回颁奖累计卡片墙 .</a> &nbsp; <a href="https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/index.html" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">📚 返回知识库门户 .</a></p>
  <div class="hero">
    <h1>🏆 颁奖典礼 . {round}</h1>
    <p>本轮新增 {n} 张（通过六维评估，剔除平级/朋友向①，仅 ②上下级 / ③高管间）；关系档：③高管间 {ne} 张 + ②上下级 {ns} 张。</p>
    <div class="relbar">
      <span>② 领导↔员工（上下级，supervisor）</span>
      <span>③ 领导↔领导（高管间，exec）</span>
    </div>
  </div>
  <div class="grid">
{cards}
  </div>
<footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>
</div>
</body>
</html>
""".format(round=ROUND_LABEL, n=len(CARDS), ne=n_exec, ns=n_sup, cards=inc_cards)
with open(RUN_PATH, "w", encoding="utf-8") as f:
    f.write(inc_html)
print("增量页已写:", RUN_PATH, len(inc_html), "字符")

# ---------- 2) 汇总页 award.html 注入 ----------
summary_path = os.path.join(AWARD_DIR, "award.html")
html = open(summary_path, encoding="utf-8").read()
before = html.count('<div class="hl">')
exec_block = "\n".join(card_block(c, 4) for c in CARDS if c["relation"]=="exec")
sup_block = "\n".join(card_block(c, 4) for c in CARDS if c["relation"]=="supervisor")
# exec 注入 sec2 前；sup 注入 footer 前
html = html.replace('  <div class="sec sec2">', exec_block + '\n  <div class="sec sec2">', 1)
html = html.replace('<footer>', sup_block + '\n<footer>', 1)
# hero 描述追加
html = html.replace('二十一轮 enrich 2026-08-21(+6)"', '二十一轮 enrich 2026-08-21(+6) ｜ 二十二轮 enrich 2026-08-22(+{0})"'.format(len(CARDS)), 1)
open(summary_path, "w", encoding="utf-8").write(html)
after = html.count('<div class="hl">')
print("汇总页注入: 前 {0} 卡 -> 后 {1} 卡 (+{2})".format(before, after, after-before))

# ---------- 3) index.json ----------
idx = json.load(open(os.path.join(BASE, "index.json"), encoding="utf-8"))
existing_urls = set(e.get("url") for e in idx)
added = 0
for c in CARDS:
    if c["url"] in existing_urls:
        print("  跳过重复 URL:", c["url"]); continue
    idx.append({
        "title": c["title"], "normKey": c["title"], "url": c["url"],
        "sourceType": c["source"], "relation": c["relation"],
        "summary": c["val"][:120]
    })
    existing_urls.add(c["url"]); added += 1
json.dump(idx, open(os.path.join(BASE, "index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("index.json 新增 {0} 条，现共 {1} 条".format(added, len(idx)))

# ---------- 4) Obsidian 颁奖-知识卡汇总.md ----------
NOTE = os.path.join(BASE, "..", "..", "..", "Documents", "Obsidian", "活动", "知识采集库", "素材", "award", "颁奖-知识卡汇总.md")
NOTE = os.path.abspath(NOTE)
note = open(NOTE, encoding="utf-8").read()
total = after  # 与汇总页一致
note = note.replace("共 125 张", "共 {0} 张".format(total), 1)
# 轮次小节（插在 ## 卡片总表 前）
round_sec = "\n## 轮次 2026-08-22(+{0})\n本轮新增（均通过六维评估、仅 ②上下级 / ③高管间）：\n".format(len(CARDS))
for c in CARDS:
    reltxt = "③高管间" if c["relation"]=="exec" else "②上下级"
    stxt = "一手" if c["source"]=="一手" else "二手"
    round_sec += "- {0}（{1}·{2}）\n".format(c["title"], reltxt, stxt)
note = note.replace("\n## 卡片总表", round_sec + "\n## 卡片总表", 1)
# 卡片总表追加行（在 ## 线上卡片墙 前）
rows = ""
for c in CARDS:
    reltxt = "③高管间" if c["relation"]=="exec" else "②上下级"
    rows += "| {0}（award/award.html） | 4 | {1} | {2} |  |\n".format(c["title"], c["source"], reltxt)
note = note.replace("\n## 线上卡片墙", rows + "\n## 线上卡片墙", 1)
# 线上卡片墙追加增量页链接
note = note.replace("本轮增量页（二十一轮·2026-08-21b）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/award-20260821b.html",
                    "本轮增量页（二十一轮·2026-08-21b）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/award-20260821b.html\n- 本轮增量页（二十二轮·2026-08-22）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/award-20260822.html", 1)
open(NOTE, "w", encoding="utf-8").write(note)
print("Obsidian 颁奖-知识卡汇总.md 已更新（{0} 卡）".format(total))

# ---------- 5) 00-知识采集索引.md ----------
IDX = os.path.abspath(os.path.join(BASE, "..", "..", "..", "Documents", "Obsidian", "活动", "知识采集库", "00-知识采集索引.md"))
idxmd = open(IDX, encoding="utf-8").read()
# 5a 头部追加轮次
idxmd = idxmd.replace("二十一轮 enrich 2026-08-21(+6)",
                      "二十一轮 enrich 2026-08-21(+6) ｜ 二十二轮 enrich 2026-08-22(+{0})".format(len(CARDS)), 1)
# 5b blockquote 追加
idxmd = idxmd.replace("（③1/②5）。",
                      "（③1/②5）。二十二轮 enrich（2026-08-22 +{0}）：职工技术创新成果奖政府SOP、一线服务之星表彰、青年岗位能手团中央办法、省长/董事长质量奖一把手亲颁、认可项目ROI测算框架、多元包容DEI表彰（③{1}/②{2}）。".format(len(CARDS), n_exec, n_sup), 1)
# 5c 在 Open Day 段前插入 6 行 award 表行
newrows = ""
for c in CARDS:
    reltxt = "③高管间" if c["relation"]=="exec" else "②上下级"
    newrows += "| {0}（award/award.html） | 4 | {1} | {2} |  |\n".format(c["title"], c["source"], reltxt)
idxmd = idxmd.replace("\n## 主题：Open Day", "\n" + newrows + "\n## 主题：Open Day", 1)
open(IDX, "w", encoding="utf-8").write(idxmd)
print("00-知识采集索引.md 已更新（award 表 +{0} 行）".format(len(CARDS)))

print("\n=== 本地渲染与落库完成（{0} 卡：③{1}/②{2}）===".format(len(CARDS), n_exec, n_sup))
