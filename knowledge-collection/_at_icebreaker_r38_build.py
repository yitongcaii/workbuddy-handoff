# -*- coding: utf-8 -*-
# 破冰 R38 构建脚本（2026-09-10）· 5 ③高管间 + 5 ②上下级，全 NEW（M=0，已去重）
import os, re, json

BASE = r'C:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection'
IB = os.path.join(BASE, 'icebreaker')
WALL = os.path.join(IB, 'icebreaker.html')
RUNS = os.path.join(IB, 'runs')
INDEX = os.path.join(BASE, 'index.json')
MAPF = os.path.join(BASE, 'lexiang-entry-map.json')
VAULT = r'C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库'
SUM = os.path.join(VAULT, '素材', 'icebreaker', '破冰-知识卡汇总.md')
IDX = os.path.join(VAULT, '00-知识采集索引.md')
RUNNOTE = os.path.join(VAULT, '素材', 'icebreaker', 'runs', '破冰-2026-09-10-第三十八轮-知识卡.md')

DATE = '2026-09-10'
ROUND = 'r38'

# ---------- 10 卡 ----------
# rel: 'r3'(③高管间/exec) | 'r2'(②上下级/supervisor); src: 'b2'(二手) | 'b1'(一手)
cards = [
 # ===== ③ 高管间（exec）=====
 {"emoji":"🚪","cat":"一把手离任交接","rel":"r3","src":"b2",
  "title":"一把手离任交接·最后100天仪式感闭环（情感收尾+分层交接+校友关系+董事会激励）",
  "val":"把离任当『第二重要的一百天』：早期做情感收尾（重读任期笔记萃取教训/提前打包留心理跑道/手写给保安保洁的告别信），避免未处理的情绪泄漏成破坏性行为；分层交接（driver→passenger→不在车里，把难决策在离任前处理掉，末段少说多做）；用符号与动作传递文化（接力棒隐喻『赢在交接』/亲录告别视频保原声不被公关改写）；董事会用经济滑道（顾问/大使角色+留任激励）让离任CEO对继任成功有利益；主动建 alumni 关系（麦肯锡式校友计划，把前CEO当长期资产而非阴影）；用统一叙事收尾（避免各说各话）。",
  "how":"一把手离任交接·最后100天：①早期情感收尾（重读笔记/提前打包/手写告别信，先处理情绪再离开）；②分层交接（driver→passenger→不在车里，难决策离任前处理，末段少说多做）；③符号传文化（接力棒隐喻/亲录告别视频保原声）；④董事会经济滑道（顾问+留任激励让前任对继任成功有利益）；⑤主动建 alumni（麦肯锡式校友计划当长期资产）；⑥统一离任叙事。把离任当第二重要的一百天。",
  "url":"http://thesavoirgroup.com/insights/the-last-100-days-mastering-the-art-of-the-executive-exit",
  "note":"适用：③ 一把手/CEO 离任交接（The Savoir Group·二手），最后100天仪式感闭环——情感收尾+分层交接(driver→passenger→不在车里)+接力棒符号+董事会经济滑道+alumni 关系，把离任当第二重要的一百天（高管间/一把手离任交接）。"},
 {"emoji":"🔧","cat":"高管团队冲突修复","rel":"r3","src":"b2",
  "title":"高管团队冲突修复·Alignment/Repair/Norms 三框架 + 高管修复协议",
  "val":"按冲突原型选框架：战略冲突→Alignment（命名分歧→重锚企业目标→压力测试选项→决定后公开对齐）；关系冲突→Repair（私下一对一或带教练三方重置→只讲影响不诉动机→约定具体新行为→适当公开重申）；文化/价值观冲突→Norms（浮现各自假设→共定『我们怎么领导』→落成可观察行为→同伴互查）。附高管修复协议：破裂后点名发生了什么→承认影响→重置期望→在受影响同侪前重申新行为（修复不是软弱，是信任建设纪律）。团队冲突规范：在房间里命名分歧/对事不对人/不靠小道消息重开决策/决定后公开对齐。CEO 不是唯一执行者，高管要互相问责。",
  "how":"高管团队冲突修复按原型分三框架：战略冲突用 Alignment（命名分歧→重锚企业目标→压力测选项→决定后公开对齐）；关系冲突用 Repair（私下一对一/带教练三方→只讲影响不诉动机→约定具体新行为→适当公开重申）；文化冲突用 Norms（浮现假设→共定怎么领导→落成可观察行为→同伴互查）。加高管修复协议（点名→承认影响→重置→同侪前重申）。冲突规范：房间里命名分歧/对事不对人/不靠小道重开决策/决定后公开对齐。",
  "url":"https://info.brightarrowcoaching.com/conflict-as-a-catalyst",
  "note":"适用：③ 高管团队冲突/失能修复（Bright Arrow Coaching·二手），Conflict-to-Connection 三框架（Alignment/Repair/Norms）+高管修复协议+冲突规范，把冲突从隐藏操作系统变成连接（高管间/高管团队冲突修复）。"},
 {"emoji":"📜","cat":"领导力团队契约","rel":"r3","src":"b2",
  "title":"领导力团队契约·把 disagreement 规则写进 operating norms（禁邮件开火/实时解决/公开对齐）",
  "val":"把『怎么吵架』变成显式约定（Leadership Team Charter / Operating Norms），共创原则如：对事不对人、实时 disagreement 不靠邮件、决定后在房间里解决不在房间外、决定后全员拥有、假设善意保持好奇。落地动作：①No Conflict by Email 约定（升级就进房间，不说『先暂停这个线程带进会议室』）；②固定 LT 议程加 15–30min『张力/挑战』常设段，或用 Lencioni/EOS IDS（识别-讨论-解决）或『真问题/各自需要/承诺』三问；③60 分钟共创 norms 工作坊；④指派一位『联结者』领导在讨论失控时调解；⑤需要时用外部教练/引导师打破模式。把张力变信任靠 normalize constructive tension（挑战≠不忠诚，目标是清晰对齐非共识）。",
  "how":"领导力团队契约把 disagreement 规则写进 operating norms：共创原则（对事不对人/实时不靠邮件/决定后房间内解决/全员拥有/假设善意）；落地四招——①No Conflict by Email（升级就进房间）；②LT 议程加常设『张力』段或用 Lencioni/EOS IDS 三问；③60min 共创 norms 工作坊；④指派联结者调解；⑤必要时外部教练。张力变信任靠 normalize constructive tension（挑战≠不忠诚）。",
  "url":"https://businessconsultingresources.com/managing-leadership-tension-strategies-to-build-trust-and-alignment",
  "note":"适用：③ 高管团队把冲突规则显式化（BCR·二手），Leadership Team Charter/Operating Norms——禁邮件开火+实时解决+公开对齐+常设张力段+外部教练，把张力变连接（高管间/领导力团队契约）。"},
 {"emoji":"🧩","cat":"高管冲突解决蓝图","rel":"r3","src":"b2",
  "title":"高管团队冲突解决 Blueprint·RACI 厘清权责 + listen-first rounds + 外部顾问提速 30%",
  "val":"高管冲突多源于权责不清/重叠（60% 高管争端来自角色模糊）：①协作定义角色、用 RACI 矩阵厘清决策权边界，文档化；②投资领导力培训四块（沟通倾听/情商/结构技能如 RACI+升级路径/干预技术），可降人际冲突 38%、提心理安全 35%；③建规律反馈系统（短窗口提 concern、safety 对话、脉调调研、事后复盘『成因/学到/下次改』），未决议题降 50%；④listen-first rounds（每人 uninterrupted 讲视角，防主导者独大）；⑤内部卡住时用外部顾问（中立、结构化，争端解决快 30%）。核心心态：角色不是消灭分歧，是让冲突健康。",
  "how":"高管团队冲突解决 Blueprint：①RACI 厘清权责边界（60% 高管争端源于角色模糊）；②领导力培训四块（倾听沟通/情商/结构 RACI+升级路径/干预）降人际冲突 38%、提心理安全 35%；③规律反馈系统（短窗提 concern+safety 对话+脉调+事后复盘）未决降 50%；④listen-first rounds 防主导独大；⑤内部卡住用外部顾问（中立结构化，快 30%）。角色不是消灭分歧，是让冲突健康。",
  "url":"http://growthshuttle.com/conflict-resolution-executive-teams-smes/",
  "note":"适用：③ 高管团队冲突根因干预（Growth Shuttle·二手），Conflict Resolution Blueprint——RACI 厘清权责+领导力培训四块+规律反馈+safety 对话+外部顾问提速 30%，60% 争端源于角色模糊（高管间/高管冲突解决蓝图）。"},
 {"emoji":"🩺","cat":"高管团队失能诊断","rel":"r3","src":"b2",
  "title":"高管团队五大 dysfunction 诊断与干预（信任缺失→冲突恐惧→承诺缺→问责回避→结果漠视）",
  "val":"用 Lencioni 五级失能模型诊断：①信任缺失（不愿脆弱/不求助/防御）→ 个人历史练习+CEO 脆弱建模+一对一关系建设；②冲突恐惧（表面和谐/回避/假共识）→ 允许并邀请挑战、mining for conflict、冲突画像；③承诺缺（模糊/反复/缺买办）→ 决策澄清+级联沟通+期限纪律；④问责回避（不叫同伴/标准下滑/CEO 成唯一执行者）→ 目标清晰+进度复盘+同伴反馈+不交付后果；⑤结果漠视（个人目标压倒团队/状态 ego 优先）→ 团队记分牌+企业目标优先+集体奖励+公开承诺。干预从根基（通常是信任）起逐层修，结构强化健康行为，速效药无效。",
  "how":"高管团队五大 dysfunction（Lencioni）逐层诊断干预：①信任缺失→个人历史练习+CEO 脆弱建模+一对一；②冲突恐惧→允许挑战/mining for conflict/冲突画像；③承诺缺→决策澄清+级联+期限；④问责回避→目标清晰+复盘+同伴反馈+后果；⑤结果漠视→团队记分牌+企业优先+集体奖励。从根基（信任）起修，速效药无效。",
  "url":"https://quarterdeck.co.uk/articles/leadership-team",
  "note":"适用：③ 高管团队系统性失能诊断（Quarterdeck·二手），Lencioni 五级 dysfunction——信任缺失→冲突恐惧→承诺缺→问责回避→结果漠视，逐层干预、结构强化（高管间/高管团队失能诊断）。"},

 # ===== ② 上下级（supervisor）=====
 {"emoji":"💬","cat":"新经理反馈框架","rel":"r2","src":"b2",
  "title":"新经理反馈·Radical Candor 直言+关怀 2×2 + SBI（情境/行为/影响）24–48h 内给",
  "val":"新经理最易踩『ruinous empathy』（只关怀不挑战，软掉反馈护短期关系养大患）。用 Kim Scott 框架：Care Personally × Challenge Directly 两轴，理想是高×高；失败模式=ruinous empathy/obnoxious aggression/manipulative insincerity。给反馈用 SBI（Center for Creative Leadership）：Situation 具体时空→Behavior 可观察动作不带评判→Impact 后果；24–48h 内给、针对事不针对人。关键纪律：①先 solicite 反馈再给（『我哪点能做得更好』并真诚致谢，种下上行反馈文化）；②批评私密、表扬公开；③具体 praise 而非『great job』；④新人首周就立直接具体的反馈期望（正负面都给），错过越早越难收。文化跟着领导走——领导怎么接反馈比说什么更能在全团队定调。",
  "how":"新经理反馈·Radical Candor：Care Personally×Challenge Directly 2×2，落在高×高；避 ruinous empathy（只关怀不挑战）。给反馈用 SBI（情境/可观察行为/影响），24-48h 内、对事不对人；纪律——先 solicite 上行反馈再给、批评私密表扬公开、具体 praise、新人首周就立直接反馈期望。领导怎么接反馈定团队文化。",
  "url":"http://www.radicalcandor.com/blog/4-ways-help-new-managers-succeed/",
  "note":"适用：② 新经理给团队反馈（Radical Candor·二手），直言+关怀 2×2 + SBI（情境/行为/影响）24–48h 内给 + 先 solicite 上行反馈，避 ruinous empathy（上下级/新经理反馈框架）。"},
 {"emoji":"🧭","cat":"新经理生存指南","rel":"r2","src":"b2",
  "title":"新经理生存指南·一致性小承诺建信任 + 1:1 五段模板 + 管理前同事",
  "val":"新经理最快建信任靠『一致的小行动非大姿态』：每承诺必兑现（说周五发邮件就发、说查就查并回哪怕不是好消息），每次兑现都是信任账户小额存款；透明（分享决策理由、不知道就直说、犯错就认不甩锅）。1:1 模板（首月用）：个人 check-in（这周什么在脑子里）→对方议程（卡点/要决策/要反馈）→障碍（我能帮什么）→教练（一个发展问而非给建议）→承诺（各自下次会议前做什么，绝不错过/改期）。绝不错过 1:1（Gallup：有规律 1:1 的员工敬业度近 3 倍）；给反馈用 Radical Candor（具体行为非人格评判、近事件、批评私密）。管前同事：被提拔后最复杂的社会挑战，需显式处理关系转变。",
  "how":"新经理生存指南：信任靠一致小承诺（每承诺必兑现=信任存款）+透明（讲理由/不知直说/犯错认）；1:1 五段模板（个人 check-in→对方议程→障碍→教练一问→承诺，绝不错过，Gallup 敬业近 3 倍）；反馈用 Radical Candor（具体行为/近事件/批评私密）；管前同事需显式处理关系转变。",
  "url":"https://winwithmotivation.com/first-time-manager-survival-guide",
  "note":"适用：② 新任经理落地生存（Win With Motivation·二手），一致小承诺建信任+1:1 五段模板（绝不错过）+Radical Candor 反馈+管前同事，靠信任非职权（上下级/新经理生存指南）。"},
 {"emoji":"🔗","cat":"跨职能团队破冰","rel":"r2","src":"b2",
  "title":"跨职能团队破冰 10 法·非正式联结 + 公司问答 + 多元对话 + 两真一假 + 密室",
  "val":"管跨职能团队难点在冲突与意见分歧，用 10 个练习建强关系：①Engage&Connect 非正式小聚（主题如旅行故事/爱书/成长 tips，破部门墙）；②Company Trivia 竞答（强化公司与行业知识+协作）；③Diversity Dialogue 多元对话（对陈述举手/交叉臂表态再讲理由，尊重差异找行动点）；④Two Truths and a Lie 两真一假（轻快认识）；⑤Escape Room 密室（限时解谜练去中心化决策与压力下协作）；另含 Marshmallow Challenge/Problem-Solving Escape/ Talking Circles 修复圈/Micro-Appreciation Circles 微赞赏/非语言协调游戏。关键：每次活动必带 debrief（把体验连回工作实际），否则只是『好玩一天』无留存。",
  "how":"跨职能团队破冰 10 法：①Engage&Connect 非正式小聚破部门墙；②Company Trivia 竞答强协作；③Diversity Dialogue 多元对话（表态+讲理由+找行动）；④Two Truths and a Lie 两真一假；⑤Escape Room 密室练压力协作；另 Marshmallow/修复圈/微赞赏/非语言协调。关键：每次必带 debrief 把体验连回工作，否则无留存。",
  "url":"https://teambuildingworld.com/cross-functional-team-building/",
  "note":"适用：② 经理带跨职能/矩阵团队破冰（Team Building World·二手），10 法（非正式联结/公司问答/多元对话/两真一假/密室+必做 debrief），破部门墙建关系（上下级/跨职能团队破冰）。"},
 {"emoji":"🎚️","cat":"新经理委派拨盘","rel":"r2","src":"b2",
  "title":"新经理委派·情境领导 4 档拨盘（Direct/Coach/Support/Delegate）+『我在挡你什么路』",
  "val":"新经理常把委派当二元（自己干/甩手），用 Hersey-Blanchard 情境领导当『拨盘』按人按事调：①Direct（高技能需求低当前技能高热情——『我带你走一遍』）；②Coach（有技能但信心/动力掉——『你做了难的，下一步我调』）；③Support（高技能但自我怀疑——『你比我都懂，直觉是？』给许可）；④Delegate（高技能高信心——给结果+期限+约束，然后空间）。调前问本人『这活你熟吗/要多细的指引』避免猜。另：问『我在你路上挡了什么』（最高信号问题之一）挖你看不见的摩擦；新经理最易晚给/模糊给/不给反馈，用 SBI 近事件给。委派是拨盘不是开关。",
  "how":"新经理委派·情境领导 4 档拨盘：Direct（带一遍）/Coach（调下一步）/Support（给许可）/Delegate（给结果+空间）；调前问本人『熟吗/要多细指引』；另问『我在挡你什么路』挖看不见的摩擦；反馈用 SBI 近事件给。委派是拨盘非开关。",
  "url":"https://www.scienceofpeople.com/communication-skills-for-new-managers",
  "note":"适用：② 新经理任务委派（Science of People·二手），情境领导 4 档拨盘（Direct/Coach/Support/Delegate）+『我在挡你什么路』+SBI 反馈，委派是拨盘非开关（上下级/新经理委派拨盘）。"},
 {"emoji":"🎯","cat":"破冰活动选型","rel":"r2","src":"b2",
  "title":"破冰选型框架·按情境匹配（新团队/跨职能/冲突重置）+ 必做 debrief + 可选 pass",
  "val":"破冰不是随机游戏，按情境选：Quick standup（2–5min）→一词能量 check-in；Weekly meeting（5–10min）→This or That 轮答；New team kickoff（15–30min）→Two Truths and a Lie 认识游戏；Cross-functional workshop（10–15min）→Common Ground 配对；Virtual all-hands（5–10min）→Emoji check-in 投票；Offsite/retreat（30–60min）→Marshmallow Challenge。通用原则：①匹配团队熟悉度（新团队低风险、老团队可深）；②匹配会议目的（创意会 vs 严肃讨论）；③文化包容（多方式回应、避文化排他、给神经多元者提前发题）；④必做 debrief（『我们怎么协作学到什么』收尾）；⑤参与可选（给 pass 不强迫）；⑥领导先/早示范分享定调。多想『为什么做这个』再选。",
  "how":"破冰选型框架按情境匹配：standup→一词能量；周会→This or That；新团队→两真一假；跨职能→Common Ground；虚拟→Emoji check-in；offsite→Marshmallow。原则——匹配熟悉度/会议目的、文化包容多方式回应、必做 debrief、参与可选(pass)、领导先示范。先问『为何做』再选。",
  "url":"https://www.pryor.com/blog/goal-setting-activities-from-process-to-product-to-outcome",
  "note":"适用：② 经理/HR 选破冰活动（Pryor·二手），按情境匹配框架（新团队/跨职能/虚拟/offsite）+文化包容+必做 debrief+可选 pass+领导先示范，破冰是目的驱动非随机游戏（上下级/破冰选型框架）。"},
]

def normkey(t):
    return ''.join(ch for ch in t.lower() if ch.isalnum() or '\u4e00' <= ch <= '\u9fff')

def card_html(c):
    rel_txt = '③高管间' if c['rel']=='r3' else '②上下级'
    src_txt = '一手' if c['src']=='b1' else '二手'
    disp = c['url'].replace('https://','').replace('http://','')
    return (
'<div class="hl">\n'
'      <div class="top"><span class="emoji">{emoji}</span><h3>{title}</h3><span class="cat">{cat}</span>'
'<span class="badge {rel}">{reltxt}</span><span class="badge {src}">{srctxt}</span></div>\n'
'      <p class="val">{val}</p>\n'
'      <details class="exec"><summary>怎么做</summary><div class="inner">{how}</div></details>\n'
'      <div class="src">🔗 <a href="{url}" target="_blank">{disp}</a></div>\n'
'      <div class="note">{note}</div>\n'
'    </div>'
    ).format(emoji=c['emoji'], title=c['title'], cat=c['cat'], rel=c['rel'], reltxt=rel_txt,
             src=c['src'], srctxt=src_txt, val=c['val'], how=c['how'], url=c['url'], disp=disp, note=c['note'])

# ---------- Step 5: dedup against index.json ----------
data = json.load(open(INDEX, encoding='utf-8'))
existing_urls = {d.get('url') for d in data}
existing_keys = {d.get('normKey') for d in data}
existing_titles = {d.get('title') for d in data}
filtered = []
skipped = []
for c in cards:
    k = normkey(c['title'])
    if c['url'] in existing_urls or k in existing_keys or c['title'] in existing_titles:
        skipped.append(c['title'])
    else:
        filtered.append(c)
print("total candidates:", len(cards), "| skipped(dedup):", len(skipped), skipped)
cards = filtered

n3 = [c for c in cards if c['rel']=='r3']
n2 = [c for c in cards if c['rel']=='r2']
print("N=", len(cards), "③=", len(n3), "②=", len(n2))

# ---------- 1) 独立增量页 runs/icebreaker-2026-09-10-r38.html ----------
run_html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>破冰 · 第38轮补采（独立页）</title>
<style>
:root{
  --bg:#f4f6fb; --card:#ffffff; --ink:#1f2430; --sub:#5b6478;
  --accent:#6c5ce7; --accent2:#00b8d9; --chip:#eef0ff;
}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:linear-gradient(135deg,#eef1ff 0%,#e6f7ff 100%);color:var(--ink);padding:28px 18px;line-height:1.6;}
.wrap{max-width:1080px;margin:0 auto;}
.hero{background:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);border-radius:22px;padding:30px 32px;color:#fff;box-shadow:0 14px 40px rgba(108,92,231,.25);margin-bottom:22px;}
.hero h1{font-size:26px;font-weight:800;letter-spacing:1px;margin-bottom:8px;}
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
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;}
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
  <div class="hero">
    <h1>🤝 破冰 · 第38轮补采（独立页）</h1>
    <p>采集于 2026-09-10 ｜ 本轮新增 10 卡（③高管间 5 / ②上下级 5）｜ 六维评估 ｜ 一手/二手标注 ｜ 受众关系分层（仅②③，剔除①）｜ 累计总索引见 <a href="../icebreaker.html" style="color:#fff;text-decoration:underline;">icebreaker.html</a></p>
    <div class="relbar">
      <span>② 领导↔员工（上下级）</span>
      <span>③ 领导↔领导（高管间）</span>
    </div>
  </div>
  <div class="sec sec3">
    <h2>③ 领导↔领导（高管间，exec）</h2>
    <span class="tag">5 卡</span>
  </div>
  <div class="grid">
{C3}
  </div>
  <div class="sec sec2">
    <h2>② 领导↔员工（上下级，supervisor）</h2>
    <span class="tag">5 卡</span>
  </div>
  <div class="grid">
{C2}
  </div>

</div>
<footer style="text-align:center;padding:24px;color:#94a3b8;font-size:13px;border-top:1px solid #e2e8f0;margin-top:40px;">📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>
</body>
</html>
'''.replace('{C3}', "\n".join(card_html(c) for c in n3)).replace('{C2}', "\n".join(card_html(c) for c in n2))

os.makedirs(RUNS, exist_ok=True)
with open(os.path.join(RUNS, 'icebreaker-2026-09-10-r38.html'), 'w', encoding='utf-8') as f:
    f.write(run_html)
print("written run page")

# ---------- 2) 累计墙 icebreaker.html ----------
html = open(WALL, encoding='utf-8').read()
m3 = re.search(r'<div class="sec sec3">.*?<span class="tag">(\d+) 卡</span>', html, re.S)
m2 = re.search(r'<div class="sec sec2">.*?<span class="tag">(\d+) 卡</span>', html, re.S)
c3 = int(m3.group(1)); c2 = int(m2.group(1))
new_c3 = c3 + len(n3); new_c2 = c2 + len(n2)
html = html.replace('<span class="tag">%d 卡</span>' % c3, '<span class="tag">%d 卡</span>' % new_c3, 1)
html = html.replace('<span class="tag">%d 卡</span>' % c2, '<span class="tag">%d 卡</span>' % new_c2, 1)
print("wall tags:", c3, "->", new_c3, "|", c2, "->", new_c2)

# hero log: insert R38 line before relbar
r38_log = ('<p style="margin-top:8px">本轮（三十八轮 2026-09-10）主线：一把手离任交接·最后100天仪式感闭环（情感收尾+分层交接 driver→passenger→校友关系+董事会经济滑道）、高管团队冲突修复 Conflict-to-Connection（Alignment/Repair/Norms 三框架+高管修复协议）、领导力团队契约（把 disagreement 写进 operating norms·禁邮件开火/实时解决/公开对齐）、高管冲突解决 Blueprint（RACI 厘清权责+listen-first rounds+外部顾问提速30%）、高管团队五大 dysfunction 诊断与干预（Lencioni·信任→冲突→承诺→问责→结果）（③）；'
           '新经理反馈 Radical Candor（直言+关怀2×2+SBI 24-48h）、新经理生存指南（一致小承诺建信任+1:1五段模板+管前同事）、跨职能团队破冰10法（非正式联结/公司问答/多元对话/两真一假/密室+必做debrief）、新经理委派情境领导4档拨盘（Direct/Coach/Support/Delegate+『我在挡你什么路』）、破冰选型框架（按情境匹配+文化包容+必做debrief+可选pass）（②）。</p>')
html = html.replace('<div class="relbar">', r38_log + '\n<div class="relbar">', 1)

# sec3 cards before sec3 grid close (before <div class="sec sec2">)
sec3_block = "\n".join(card_html(c) for c in n3)
i = html.index('<div class="sec sec2">')
close = html.rfind('</div>', 0, i)
html = html[:close] + sec3_block + "\n" + html[close:]

# sec2 cards before sec2 grid close (before <footer>)
sec2_block = "\n".join(card_html(c) for c in n2)
fi = html.index('<footer>')
close2 = html.rfind('</div>', 0, fi)
html = html[:close2] + sec2_block + "\n" + html[close2:]

open(WALL, 'w', encoding='utf-8').write(html)
print("wall updated")

# ---------- 3) index.json (only filtered cards) ----------
before = len(data)
for c in cards:
    rel = 'exec' if c['rel']=='r3' else 'supervisor'
    data.append({
        "title": c['title'],
        "normKey": normkey(c['title']),
        "url": c['url'],
        "sourceType": "primary" if c['src']=='b1' else "secondary",
        "relation": rel,
        "summary": c['note'],
        "topic": "icebreaker"
    })
after = len(data)
json.dump(data, open(INDEX, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print("index.json", before, "->", after)

# ---------- 4) Obsidian 汇总 md ----------
s = open(SUM, encoding='utf-8').read()
s = s.replace(
'''**本轮增量页（2026-09-09 · 三十七轮 R37）**：[icebreaker-2026-09-09-r37.html · GitHub Pages](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/runs/icebreaker-2026-09-09-r37.html)  
**本机源**：`knowledge-collection/icebreaker/runs/icebreaker-2026-09-09-r37.html`
**上轮增量页（2026-09-08 · 三十六轮 R36）**：[icebreaker-2026-09-08-r36.html · GitHub Pages](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/runs/icebreaker-2026-09-08-r36.html)''',
'''**本轮增量页（2026-09-10 · 三十八轮 R38）**：[icebreaker-2026-09-10-r38.html · GitHub Pages](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/runs/icebreaker-2026-09-10-r38.html)  
**本机源**：`knowledge-collection/icebreaker/runs/icebreaker-2026-09-10-r38.html`
**上轮增量页（2026-09-09 · 三十七轮 R37）**：[icebreaker-2026-09-09-r37.html · GitHub Pages](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/runs/icebreaker-2026-09-09-r37.html)''')

r38_bq = ('\n> 三十八轮补采 +10（2026-09-10，②×5/③×5）：一把手离任交接·最后100天仪式感闭环（情感收尾+分层交接+校友关系+董事会激励）、高管团队冲突修复 Conflict-to-Connection（Alignment/Repair/Norms 三框架+高管修复协议）、领导力团队契约（把 disagreement 写进 operating norms·禁邮件开火/实时解决/公开对齐）、高管冲突解决 Blueprint（RACI 厘清权责+listen-first rounds+外部顾问提速30%）、高管团队五大 dysfunction 诊断与干预（Lencioni·信任→冲突→承诺→问责→结果）（③）；'
           '新经理反馈 Radical Candor（直言+关怀2×2+SBI 24-48h）、新经理生存指南（一致小承诺建信任+1:1五段模板+管前同事）、跨职能团队破冰10法（非正式联结/公司问答/多元对话/两真一假/密室+必做debrief）、新经理委派情境领导4档拨盘（Direct/Coach/Support/Delegate+『我在挡你什么路』）、破冰选型框架（按情境匹配+文化包容+必做debrief+可选pass）（②）。本次全二手，定向补「一把手离任100天闭环/高管冲突修复三框架/领导力团队契约/高管冲突Blueprint/五大dysfunction」「新经理Radical Candor反馈/生存指南/跨职能破冰/委派拨盘/破冰选型」十个稀缺子域。')
anchor = '定向补「新CEO百天五阶段/高管入职四阶段框架」「接管新团队21问/首次1:1七问/心理安全感练习与仪式」五个稀缺子域。'
assert anchor in s, "R37 blockquote anchor not found"
s = s.replace(anchor, anchor + r38_bq)

baseline_total = c3 + c2
table_rows = []
for j, c in enumerate(cards, start=baseline_total+1):
    rel_txt = '③高管间' if c['rel']=='r3' else '②上下级'
    src_txt = '一手' if c['src']=='b1' else '二手'
    table_rows.append("| {} | {} | {} | {} | {} |".format(j, c['title'], rel_txt, src_txt, c['note']))
sec = ("\n## 轮次 20260910-r38（+{}）\n".format(len(cards))
       + "| # | 卡片 | 关系档 | 一手/二手 | 核心要点 |\n"
       + "|---|---|---|---|---|\n" + "\n".join(table_rows) + "\n")
s = s.rstrip() + "\n" + sec
open(SUM, 'w', encoding='utf-8').write(s)
print("summary md updated")

# ---------- 5) 00-知识采集索引.md ----------
rows = []
for c in cards:
    rel_txt = '高管间' if c['rel']=='r3' else '上下级'
    src_txt = '一手' if c['src']=='b1' else '二手'
    rows.append("| {}（{}）（icebreaker.html） | 5 | {} | {} | {} |".format(c['title'], src_txt, src_txt, rel_txt, c['note']))
idx_s = open(IDX, encoding='utf-8').read().rstrip()
if not idx_s.endswith('\n'):
    idx_s += '\n'
idx_s = idx_s + "\n".join(rows) + "\n"
open(IDX, 'w', encoding='utf-8').write(idx_s)
print("00-index updated")

# ---------- 6) runs note ----------
note = '''---
title: 破冰-2026-09-10-第三十八轮-知识卡
type: 自动化采集
date: 2026-09-10
tags: [知识采集, 破冰, 第三十八轮]
relation: [supervisor, exec]
---

# 破冰 · 第三十八轮补采（2026-09-10，+10）

> 本轮独立页（GitHub Pages）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/runs/icebreaker-2026-09-10-r38.html
> 本地路径：C:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection/icebreaker/runs/icebreaker-2026-09-10-r38.html
> 累计总索引墙：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/icebreaker.html

## 本轮新增 10 卡（关系分层）

### ③ 领导↔领导（高管间 · exec）— 5 卡
- 一把手离任交接·最后100天仪式感闭环（情感收尾+分层交接+校友关系+董事会激励）〔二手〕
- 高管团队冲突修复·Alignment/Repair/Norms 三框架 + 高管修复协议〔二手〕
- 领导力团队契约·把 disagreement 规则写进 operating norms（禁邮件开火/实时解决/公开对齐）〔二手〕
- 高管团队冲突解决 Blueprint·RACI 厘清权责 + listen-first rounds + 外部顾问提速 30%〔二手〕
- 高管团队五大 dysfunction 诊断与干预（信任缺失→冲突恐惧→承诺缺→问责回避→结果漠视）〔二手〕

### ② 领导↔员工（上下级 · supervisor）— 5 卡
- 新经理反馈·Radical Candor 直言+关怀 2×2 + SBI（情境/行为/影响）24–48h 内给〔二手〕
- 新经理生存指南·一致性小承诺建信任 + 1:1 五段模板 + 管理前同事〔二手〕
- 跨职能团队破冰 10 法·非正式联结 + 公司问答 + 多元对话 + 两真一假 + 密室〔二手〕
- 新经理委派·情境领导 4 档拨盘（Direct/Coach/Support/Delegate）+『我在挡你什么路』〔二手〕
- 破冰选型框架·按情境匹配（新团队/跨职能/冲突重置）+ 必做 debrief + 可选 pass〔二手〕
'''
os.makedirs(os.path.dirname(RUNNOTE), exist_ok=True)
open(RUNNOTE, 'w', encoding='utf-8').write(note)
print("run note written")

# ---------- 7) lexiang-entry-map.json (追加 pending round) ----------
m = json.load(open(MAPF, encoding='utf-8'))
ib = m['icebreaker']
ib['rounds'].append({
    "date": "2026-09-10",
    "entry_id": None,
    "name": "icebreaker-2026-09-10-r38.html",
    "note": "轮次页 R38 (+10：5③高管间+5②上下级)｜乐享待补传(token 401 过期，待重配 mcp.json lxmcp_ token 后补传并回填 entry_id)"
})
json.dump(m, open(MAPF, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print("lexiang map updated, rounds:", len(ib['rounds']))
print("DONE")
