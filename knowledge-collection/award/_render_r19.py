# -*- coding: utf-8 -*-
import json, re, os

KC = r"C:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection"
AWARD = os.path.join(KC, "award")
VAULT = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库"

def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

# ---- Cards (R19, 2026-08-19) ----
# rel: 'exec' | 'supervisor' | 'exec,supervisor'
cards = [
 {
  "emoji":"🏆","cat":"销售激励","rel":"exec","st":"二手",
  "title":"销售激励之旅(President's Club)·SiriusDecisions 五元素框架",
  "val":"销售激励之旅（Winner's Circle / President's Club）是总薪酬的重要组成，设计得法可「成本中性」且显著降低销售流失。SiriusDecisions 五元素：①Alignment——认可 quota 与非 quota 员工（含销售 overlay / SE / 市场 / 支持），或分档 President's Club + Circle of Excellence；②Transparency——全年节奏：年初定 winners 截止→Q1 宣布次年目的地→Q1 设资格→Q2 复盘反馈→Q3 规划（早订锁价）；③Accountability——指导委员会含高管 + 销售 + 财务/法务/HR 薪酬，charter 明愿景/风险/职责；④Fairness——设可达且有量化阈值的资格线（如 150% 配额），忌活动量/主观判断，rep 对 KPI 有掌控权；⑤Connectivity——海报/门户/月度+季度 leaderboard 持续造势，结果透明可算。",
  "how":"高管/销售运营落地：①建含 ELT + HR + 财务 + 销售的指导委员会与 charter；②全年节奏 Q1 宣布目的地、Q2 复盘、Q3 规划、年末算 winner；③资格线量化可达（150% quota 类），非 quota 角色也纳入或设第二档；④月度 leaderboard 透明公示；⑤把激励之旅当留才杠杆而非纯销售增长工具。",
  "url":"https://www.forrester.com/blogs/elements-of-sales-incentive-trip-program",
  "note":"③ 高管/销售运营把销售激励之旅做成战略留才与跨职能对齐工具（② 一线销售经理用 leaderboard 透明驱动团队）。"
 },
 {
  "emoji":"🗺️","cat":"俱乐部设计","rel":"supervisor","st":"二手",
  "title":"销售精英俱乐部首办指南·节奏设计与预算基准",
  "val":"首次办 President's Club 的实操：①规模门槛——少于 30 名销售 reps 先别搞旅行（仅 20% 能去会成「高管陪 2 个 rep」），先用代金券/现金/手表；②分阶宣布——销售 kickoff 宣布「今年奖品是 President's Club 旅行、目的地 Q2 揭晓」留悬念→Q2 寄到每家信箱纸质宣布地点→Q3 发场地视频 + 开始定期公布 eligible 排名→Q4 每月倒计时→年后速宣布 winner；③预算——手表/租车/旅游券约 $8-10k/人，旅行约 $15k/对（夫妻），由 Sales Ops 管结构、报结果；④可请活动公司管机酒活动与闭幕晚宴，或内部 Ops + 市场 + 行政搞定。",
  "how":"销售运营/一线销售经理落地：①团队<30人先用现金/手表/代金券，达标再升级旅行；②kickoff 造悬念、Q2 纸质宣布地点、Q3 视频+排名、Q4 月度倒计时；③预算按人数弹性（$15k/对基准）；④Sales Ops 拥有结构与结果汇报。",
  "url":"https://www.insightpartners.com/ideas/designing-your-first-presidents-club",
  "note":"② 销售运营/一线销售经理首办精英俱乐部（③ 旅行目的地与预算需 CRO/高管拍板）。"
 },
 {
  "emoji":"☎️","cat":"一线客服","rel":"supervisor","st":"二手",
  "title":"呼叫中心/一线客服认可·VoC 认证与四类项目",
  "val":"呼叫中心认可的基准：投入约 Agent 年薪的 1%（约 $400/人/年）。四类经证项目：①Call Kudos（全员互认，下属/同事/主管均可，强调认可本身而非积分）；②Santa in a Box（全员同款神秘圣诞礼，VP/SVP 亲手递并顺带 CX 绩效认可，传统感强）；③Service Hero（Regence 运行最久最成功，leader 听录音挖掘超越预期的互动提名）；④Voice of Customer Certification（按客户真实评价认证世界级客服——85% 调查达「非常满意+已解决」即认证，主管每月发 $10-35 现金/礼品卡 + 内在认可，daily 桌面进度提醒）。核心：让客户而非经理当评委，公平且有意义。",
  "how":"客服/一线主管落地：①设 VoC 认证（客户真实评价≥85% 世界级标准，≥25 份可归因调查 + 连续 3 月）；②主管每月亲手发 $10-35 现金/卡 + 口头认可（外在+内在双激励）；③Call Kudos 全员互认 + Service Hero leader 提名；④桌面 daily 进度提醒逼近认证，经理日常鼓励。",
  "url":"https://www.sqmgroup.com/resources/library/blog/recognition-changes-behavior",
  "note":"② 客服/呼叫中心一线主管把「客户评价」做成公平认可主标尺（区别于白领 OKR 式认可）。"
 },
 {
  "emoji":"🤖","cat":"AI认可","rel":"exec","st":"二手",
  "title":"AI 驱动认可·2026 真实能力鉴别（7 项声明 real/hype）",
  "val":"2026 年每个认可平台都喊 AI，需框架辨真伪：①ML 奖励目录个性化 = REAL（协同过滤按兑换史推荐，看赎回率提升）；②AI 写认可文案 = REAL 但有坑（需基于员工近期活动生成具体建议供经理编辑，非复制粘贴）；③从认可数据预测离职 = REAL（规模 1000+ 员工有效，看样本量/准确率）；④认可文案情感分析 = PARTIAL（几乎全正面，价值低；specificity 分析更有用）；⑤NLP 质量监控 = EMERGING（标记泛化文案供经理辅导，有用但未普及）；⑥AI 自动发认可 = HYPE（无人类意图的认可 = 通知而非认可，伤体验）；⑦AI「参与度分数」预测结果 = HYPE（用自身活动算自身，循环论证）。给 vendor 的灵魂三问：信号是什么/如何更新/能否展示个性化 vs 非个性化的赎回率差。",
  "how":"高管/HR 选 AI 认可平台：①只信有真实 ML 的个性化（看赎回率提升证据）；②AI 写文案须供经理编辑、具体不泛化；③用认可网络孤立/频率下降做留才预警（1000+ 才稳）；④坚决拒「自动发认可」「单源参与度分」；⑤问 vendor 三问验证真伪。",
  "url":"https://blog.rewardian.com/ai-and-machine-learning-in-employee-recognition-whats-real-in-2026",
  "note":"③ 高管/HR/CFO 在 2026 评估认可平台 AI 能力，防被销售话术带偏。"
 },
 {
  "emoji":"🌸","cat":"女性领导","rel":"exec,supervisor","st":"二手",
  "title":"女性领导力表彰·去表演化、透明标准、故事驱动",
  "val":"女性表彰要从「事件打卡」升级为「结果驱动」并嵌进 DEI 主线：①定义 meaningful——先定目标（提留任信号/抬隐形贡献能见度/强化包容/扩 peer 提名参与），避免「Best Woman Employee」这种主观头衔，改用贡献类（创新/协作/运营卓越/包容倡导）；②透明标准——发布提名指南 + 可量化评分 rubric + 多元评审团，宣布时讲清「做了什么/变了什么/为何重要」；③从个人聚光到生态认可——纳入跨部门协作/运营可靠/文化构建/包容倡导；④连 wellness——设 Culture Builder/Inclusion Champion 等福祉向类别 + 弹性自选奖励；⑤非象征化——peer 提名跨部门、远程/混合可达、多语言提名、leader 鼓励但不替决策；⑥故事+数据双驱——分享挑战-行动-可量化影响，追踪提名量/部门分布/参与多样性。",
  "how":"HR/管理者落地女性领导表彰：①用贡献类类别替代主观头衔；②发布透明 rubric + 多元评审，宣布讲清影响；③纳入生态贡献（协作/运营/包容）而非只高光；④连 wellness 设弹性奖励；⑤leader 鼓励参与但不替选；⑥用「挑战-行动-影响」故事 + 提名分布数据证明非象征。",
  "url":"https://www.advantageclub.ai/blog/womens-day-awards-workplace",
  "note":"③+② HR/管理者把女性表彰做成去表演化、透明、与 DEI/发展挂钩的真实认可（非一日打卡）。"
 },
 {
  "emoji":"🤝","cat":"公益志愿","rel":"supervisor","st":"二手",
  "title":"员工志愿者/公益表彰·VTO 与高管连接",
  "val":"志愿者表彰要把「回馈」织进公司结构：①带薪志愿假 VTO（如每季度 8 小时，不占正常工作时间）；②等额捐赠（员工捐多少公司配多少，加倍影响）；③基于技能的志愿（工程师帮非营利写代码）；④志愿者挑战/竞赛（部门赛时长，胜队获认可 + 向自选慈善捐款）；⑤认可与奖励——全公司公告/通讯/奖项定期表彰，月度「志愿者聚焦」；⑥非现金激励——预留车位/更多假期/接触关键领导；⑦积分体系（每小时/每活动得积分兑公司周边）；⑧专业发展机会（社会影响议题）；⑨高管连接——资深领导亲签感谢信、top 志愿者与高管虚拟午餐；⑩数字徽章（里程碑可加进邮件签名）。志愿者表彰提升留任与投入，形成善意循环。",
  "how":"HR/管理者落地公益志愿者表彰：①给 VTO 带薪志愿假 + 等额捐赠放大影响；②技能型志愿（工程师写代码）认可能专业贡献；③月度聚焦 + 年度盛典（最具影响项目/新人奖）；④非现金激励（车位/假期/见领导）+ 数字徽章；⑤高管亲签感谢信/虚拟午餐做高层连接。",
  "url":"https://www.pointsoflight.org/blog/ask-a-csr-friend-when-it-comes-to-volunteering-what-counts/",
  "note":"② HR/管理者把员工志愿服务做成有 VTO、高管连接、数字徽章的真实表彰（③ 公益与雇主品牌/ESG 叙事互补）。"
 },
]

# ---- relation badge html ----
def rel_badges(rel):
    out=""
    if "exec" in rel:
        out+='<span class="badge r3">高管间</span>'
    if "supervisor" in rel:
        out+='<span class="badge r2">上下级</span>'
    return out

def card_html(c):
    return (
      '    <div class="hl">\n'
      '      <div class="top"><span class="emoji">'+esc(c["emoji"])+'</span><h3>'+esc(c["title"])+'</h3>'
      '<span class="cat">'+esc(c["cat"])+'</span>'+rel_badges(c["rel"])+'<span class="badge b2">'+esc(c["st"])+'</span></div>\n'
      '      <p class="val">'+esc(c["val"])+'</p>\n'
      '      <details class="exec"><summary>怎么做</summary><div class="inner">'+esc(c["how"])+'</div></details>\n'
      '      <div class="src">🔗 <a href="'+c["url"]+'" target="_blank">'+esc(c["url"])+'</a></div>\n'
      '      <div class="note">适用：'+esc(c["note"])+'</div>\n'
      '    </div>\n'
    )

# ---- 1. incremental page ----
CSS = """<style>
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
</style>"""

exec_cards = [c for c in cards if "exec" in c["rel"]]
sup_cards  = [c for c in cards if c["rel"]=="supervisor"]
n_exec=len(exec_cards); n_sup=len(sup_cards)

inc_body = "".join(card_html(c) for c in cards)
inc_html = (
'<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n<meta charset="UTF-8">\n'
'<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
'<title>颁奖典礼 . 十九轮增量卡片（2026-08-19）</title>\n'+CSS+'</head><body>\n'
'<div class="wrap">\n'
'<p style="margin:0 0 16px"><a href="https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/award.html" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">🏆 返回颁奖累计卡片墙 .</a> &nbsp; <a href="https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/index.html" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">📚 返回知识库门户 .</a></p>\n'
'  <div class="hero">\n'
'    <h1>🏆 颁奖典礼 . 十九轮增量卡片（2026-08-19）</h1>\n'
'    <p>本轮新增 '+str(len(cards))+' 张（通过六维评估，剔除平级/朋友向①，仅 ②上下级 / ③高管间）；关系档：③高管间 '+str(n_exec)+' 张 + ②上下级 '+str(n_sup)+' 张。</p>\n'
'    <div class="relbar">\n      <span>② 领导↔员工（上下级，supervisor）</span>\n      <span>③ 领导↔领导（高管间，exec）</span>\n    </div>\n  </div>\n'
'  <div class="grid">\n'+inc_body+'  </div>\n'
'<footer>📌 本页由 yitong 沉淀整理 . 文化活动知识库</footer>\n'
'</div>\n</body>\n</html>\n'
)
inc_path = os.path.join(AWARD, "award-20260819.html")
with open(inc_path, "w", encoding="utf-8") as f:
    f.write(inc_html)
print("WROTE incremental:", inc_path, len(inc_html), "bytes")

# ---- 2. update summary award.html ----
summary = open(os.path.join(AWARD,"award.html"), encoding="utf-8").read()
exec_frag = "".join(card_html(c) for c in exec_cards)
sup_frag  = "".join(card_html(c) for c in sup_cards)

assert summary.count('  <div class="sec sec2">')==1, "sec2 marker not unique"
summary = summary.replace('  <div class="sec sec2">', '  '+exec_frag+'  <div class="sec sec2">', 1)

# footer grid-close insertion (grid close div is at column 0, then <footer>)
marker = '</div>\n<footer>'
assert summary.count(marker)==1, "footer grid-close marker not unique: "+str(summary.count(marker))
summary = summary.replace(marker, '  '+sup_frag+marker, 1)

# hero update
hero_old = '十八轮 enrich 2026-08-18(+6)</p>'
assert summary.count(hero_old)>=1
summary = summary.replace(hero_old, '十八轮 enrich 2026-08-18(+6) ｜ 十九轮 enrich 2026-08-19(+6)</p>', 1)

open(os.path.join(AWARD,"award.html"),"w",encoding="utf-8").write(summary)
print("UPDATED summary award.html")

# ---- 3. index.json ----
idx = json.load(open(os.path.join(KC,"index.json"), encoding="utf-8"))
base = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/award.html"
new_entries=[]
for c in cards:
    e={
      "title": c["title"],
      "normKey": c["title"],
      "url": c["url"],
      "sourceType": "secondary" if c["st"]=="二手" else "primary",
      "relation": c["rel"],
      "summary": c["val"][:120],
      "topic": "award",
      "dateCollected": "2026-08-19"
    }
    idx.append(e)
    new_entries.append(e)
json.dump(idx, open(os.path.join(KC,"index.json"),"w",encoding="utf-8"), ensure_ascii=False, indent=2)
print("UPDATED index.json (+%d) total=%d" % (len(new_entries), len(idx)))

# ---- 4. Obsidian note ----
note_path = os.path.join(VAULT,"素材","award","颁奖-知识卡汇总.md")
note = open(note_path, encoding="utf-8").read()
# update count 109 -> 115
note = note.replace("共 109 张","共 115 张",1)
# insert R19 round section before '## 卡片总表'
r19_section = (
"## 轮次 2026-08-19（+6）\n"
"本轮新增（均通过六维评估、仅 ②上下级 / ③高管间）：\n"
)
for c in cards:
    rel_txt = "③高管间" if c["rel"]=="exec" else ("②上下级" if c["rel"]=="supervisor" else "②上下级+③高管间")
    r19_section += "- "+c["title"]+"（"+rel_txt+"·二手）\n"
note = note.replace("## 卡片总表", r19_section+"## 卡片总表", 1)
# add 6 rows at end of card table (before '## 线上卡片墙')
rows=""
for c in cards:
    rel_cell = "③高管间" if c["rel"]=="exec" else ("②上下级" if c["rel"]=="supervisor" else "②上下级+③高管间")
    rows += "| "+c["title"]+"（award/award.html） | 4 | 二手 | "+rel_cell+" |  |\n"
note = note.replace("## 线上卡片墙（GitHub Pages）", rows+"## 线上卡片墙（GitHub Pages）", 1)
# add incremental link bullet
note = note.replace(
 "本轮增量页（十七轮·2026-08-18）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/award-20260818.html",
 "本轮增量页（十七轮·2026-08-18）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/award-20260818.html\n- 本轮增量页（十九轮·2026-08-19）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/award-20260819.html",
 1)
open(note_path,"w",encoding="utf-8").write(note)
print("UPDATED obsidian note")

# ---- 5. 00-index ----
idx00 = open(os.path.join(VAULT,"00-知识采集索引.md"), encoding="utf-8").read()
# update award section header
hdr_old = " ｜ 十七轮 enrich 2026-08-18(+6)"
assert idx00.count(hdr_old)>=1
idx00 = idx00.replace(hdr_old, hdr_old+" ｜ 十九轮 enrich 2026-08-19(+6)", 1)
# add 6 rows before openday nav link
openday_nav = "📄 主题汇总笔记：[[知识采集库/素材/openday/OpenDay-开放日-知识卡汇总|OpenDay-开放日-知识卡汇总]]"
assert idx00.count(openday_nav)>=1
zrows=""
for c in cards:
    rel_cell = "③高管间" if c["rel"]=="exec" else ("②上下级" if c["rel"]=="supervisor" else "②上下级+③高管间")
    zrows += "| "+c["title"]+"（award/award.html） | 4 | 二手 | "+rel_cell+" |  |\n"
idx00 = idx00.replace(openday_nav, zrows+openday_nav, 1)
open(os.path.join(VAULT,"00-知识采集索引.md"),"w",encoding="utf-8").write(idx00)
print("UPDATED 00-index")
print("DONE R19")
