# -*- coding: utf-8 -*-
# 破冰 R37 构建脚本（2026-09-09）· 5 ③高管间 + 5 ②上下级，全 NEW（M=0，已去重）
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
RUNNOTE = os.path.join(VAULT, '素材', 'icebreaker', 'runs', '破冰-2026-09-09-第三十七轮-知识卡.md')

DATE = '2026-09-09'
ROUND = 'r37'

# ---------- 10 卡 ----------
# rel: 'r3'(③高管间/exec) | 'r2'(②上下级/supervisor); src: 'b2'(二手) | 'b1'(一手)
cards = [
 # ===== ③ 高管间（exec）=====
 {"emoji":"🗺️","cat":"新CEO百天","rel":"r3","src":"b2",
  "title":"新任 CEO 百天五阶段框架·pre-boarding 利益方地图 + 前 30 天只学不决策",
  "val":"把头百天当「授权期」而非冲刺：Phase1 上任前——结构化倾听+利益方地图（按影响力×信任两轴标出前30天须投入的人，给每人写一页：对我期待/对领导团队看法/求变欲），读旧董事会纪要/分析师报告/员工敬业度数据；Phase2 D1–30 学习战役——像倾听之旅而非重组，问三类同题（什么永不能变/什么须快变/旧领导哪些有效无效）跨业务单元比对；明确前30天不做（不宣布大重组/不动核心团队/不承诺新战略方向）。Phase3 31–60 战略构图；Phase4 几不可逆决策；Phase5 从新CEO变被信任的在位领导。每段有 day plan+文化/利益方/业务组合。",
  "how":"新任CEO百天五阶段：上任前做利益方地图（影响力×信任两轴，给每人写一页期待/看法/求变欲）+读旧纪要/报告；D1-30只做倾听之旅（跨单元问「什么不变/什么快变/旧领导哪些有效」，不宣布大重组/不动核心团队/不承诺新方向）；D31-60构图、再几不可逆决策、最后落为被信任的在位领导。保护学习期=保护产出。",
  "url":"https://www.c-suite-strategy.com/first-100-days-as-ceo-a-five-phase-framework-to-land-your-mandate",
  "note":"适用：③ 新任CEO/一号位落地头百天（c-suite-strategy.com·二手），五阶段=授权期而非冲刺，pre-boarding利益方地图+前30天只学不决策+每阶段day plan，先读现实再动（高管间/新CEO百天）。"},
 {"emoji":"🧭","cat":"高管入职","rel":"r3","src":"b2",
  "title":"高管入职四阶段框架·stakeholder mapping 两问 + 倾听之旅 3 问 + 90 天沟通计划",
  "val":"四阶段：①Pre-boarding（入职前3–5月）澄清角色期望与战略语境、点明关键利益方并画关系图、文化简报（讲清非正式决策模式与不成文规则）、让组织准备好迎接；②D1–30 沉浸与关系建设——stakeholder mapping 两问（对你职责成功至关重要的利益方是谁 / 你对其成功至关重要的人是谁，不能各立刻说出5个就是红旗）、Carucci 倾听3问（我怎么做能当你更好的同事/你今天最重要的工作是什么/我能怎么帮你）、文化对齐深潜；③D31–90 战略清晰+早期速赢（跨部门的网络拓展、2–3个早期影响点、建立反馈闭环）；④4–6月完全融入（领导风格微调、团队优化、战略主动权移交）。附 Stakeholder Analysis 框架（内/外部×关系强度×影响力×互动频率）与90天沟通计划（W1-2全覆盖1:1、W3-4团队+跨部门、M2客户、M3战略复盘）。",
  "how":"高管入职四阶段：pre-boarding（入职前3-5月画利益方关系图+文化简报，讲清不成文规则）；D1-30 stakeholder mapping两问（对你关键的利益方/你对其关键的人，各5个）+Carucci倾听3问（怎么当更好同事/你今天最重要的事/我怎么帮你）+文化深潜；D31-90战略清晰+2-3早期速赢+反馈闭环；4-6月完全融入。配 stakeholder 分析框架与90天沟通计划。",
  "url":"https://deliberatedirections.com/executive-onboarding-guide/",
  "note":"适用：③ 高管/C-suite 入职过渡（Deliberate Directions·二手），四阶段从pre-boarding到完全融入，stakeholder mapping两问+倾听3问+90天沟通计划，先建关系网再出成绩（高管间/高管入职）。"},
 {"emoji":"🤝","cat":"新领导同化","rel":"r3","src":"b2",
  "title":"新领导同化（NLA）完整指南·外部引导 + 入职后 2–3 周 + 30/90 天跟进",
  "val":"NLA 把假设在固化前摊开、共建共事约定，适用于新部门负责人到新CEO。形式：1整日或2个半日（领导在场+团队无领导讨论+联合对话建约定）。时机：入职后2–3周、行政onboarding之后、重大决策之前。引导师须有心理/OD背景的外部教练或顾问（内部HR只适合低层级，高管过渡需客观第三方）。度量：新领导首个战略举措上线时间、30/60/90天团队敬业度、半年自愿离职率、6个月360、需HR介入的冲突次数。跟进：30天与90天 check-in（90分钟–2小时，可虚拟）。与onboarding区别：onboarding管行政，NLA管关系与期望共建。",
  "how":"新领导同化NLA：1整日或2半日，领导开场→离场让团队无顾虑讨论→联合对话共建共事约定；时机在入职2-3周、行政onboarding后、重大决策前；引导师用有OD背景的外部教练（高管过渡需客观第三方）；度量首个战略举措时间/30-60-90敬业度/半年离职率/360/冲突次数；30与90天跟进。把一年试错压成一天坦诚对话。",
  "url":"https://leadingwithheart.com/?p=57/",
  "note":"适用：③ 新任高管/CEO 与团队同化（Leading with Heart·二手），NLA完整指南——外部引导+2-3周时机+30/90天跟进+5项度量，与onboarding互补只管关系与期望共建（高管间/新领导同化）。"},
 {"emoji":"🌱","cat":"高管同化","rel":"r3","src":"b2",
  "title":"高管同化最佳实践·入职期拉长至 6–12 月 + 团队测评画像 + 领导人开场共识目标",
  "val":"把onboarding视为前6–12月而非90天，强度递减但关系建设持续。Assimilation session：由中立引导师（非新领导或其老板，外部教练/顾问或可信内部HR）主持；先用团队测评（如Predictive Index）揭示行为偏好与动力需求、集体团队画像（mavericks还是analyzers、优势与缺口）；领导人开场（讲清为何来、管理风格、沟通偏好、露一点个人脆弱）；团队无领导讨论（leader离场，引导师问团队想知/顾虑/建议/对新老板期望+历史价值观/潜规则）；私下一对一反馈（引导师把匿名汇总交领导反思）；领导回应+共识期望与目标（3-6-9-12月）；持续团队+个人session维系。",
  "how":"高管同化最佳实践：onboarding期拉长到6-12月；同化session由中立引导师主持，先用团队测评（Predictive Index）出集体画像；领导人开场讲风格/偏好/露脆弱→离场让团队无顾虑讨论→引导师匿名汇总私下一对一反馈→领导回应+共识3-6-9-12月目标；持续团队+个人session。关系优先于流程。",
  "url":"https://strategic-imperatives.com/blog-post-holder/",
  "note":"适用：③ 新任高管融入既有团队（Strategic Imperatives·二手），同化最佳实践——期拉长至6-12月+团队测评画像+领导人开场+共识目标，把onboarding当过程非事件（高管间/高管同化）。"},
 {"emoji":"📋","cat":"高管入职清单","rel":"r3","src":"b2",
  "title":"高管入职 90 天清单·按 HR/IT/CEO董事会/新高管 四角色分流 + 4 大坑",
  "val":"按关键利益方分角色的可照搬清单：HR/People Ops——pre-boarding用AI生成岗位专属30-60-90 ramp计划、自动指派buddy/内部导师、D30感知调研、D60与CEO正式复盘、D90测eNPS与文化影响；IT/安全——D1前配齐高管硬件+安全访问+网络与数据隐私简报；hiring manager(CEO/董事会)——录欢迎视频、D1明确90天期望与愿景、D1-30保护倾听学习时间、D30/60/90持续教练对齐；新高管——D1-30完成所有关键利益方介绍会+文化深潜（学不成文规则）、D31-60找2-3个quick win+向CEO/董事会呈诊断与路线图、D61-90建例行沟通节奏（town hall/1:1/周报）。4坑：onboarding当一次性事件（应90天+行为滴灌）、信息过载（应智能平台喂小口）、忽视文化（应嵌入导师制）、跨职能各自为战（应自动协同）。",
  "how":"高管入职90天清单按四类角色分流：HR（AI生成30-60-90 ramp+buddy+D30/60/90 check-in+D90 eNPS）、IT（D1前硬件+安全访问+隐私简报）、CEO/董事会（欢迎视频+明确90天期望+保护倾听期+D30/60/90教练）、新高管（D1-30利益方介绍+文化深潜、D31-60 quick win+呈诊断、D61-90建沟通节奏）。避4坑：非一次性/防信息过载/嵌文化/跨职能协同。",
  "url":"https://enboarder.com?p=19944/",
  "note":"适用：③ 组织层面高管入职落地（Enboarder·二手），90天清单按HR/IT/CEO董事会/新高管四角色分流+4大坑，把onboarding当连续旅程非首周导向（高管间/高管入职清单）。"},

 # ===== ② 上下级（supervisor）=====
 {"emoji":"❓","cat":"接管新团队","rel":"r2","src":"b2",
  "title":"接管新团队 21 问·拆成 3–4 场 1:1（信任/偏好/积怨/动机 四类）",
  "val":"新领导接手陌生团队，用对的问题厘清方向。21问分4场1:1而非一次倾倒：第1场信任建设——工作外什么让你 energized/放松、为何选在这家公司、最好/最差老板、最好/最差团队体验、你最感激什么（领导也分享同答 reciprocity）；第2场工作偏好与团队动态——偏好何种反馈（口头/书面/当面）、何时觉被微管/最需支持、最佳老板/团队经验、喜被认可方式、固定1:1节奏；第3场积怨与改进——想改什么/不想改什么、过去什么 taboo/不敢提、近期最大挫折、最大改进机会；第4场动机与志向——全年最 motivating 项目（与谁/为何）、对公司什么兴奋、最感激什么、最大进步障碍。理想在1:1私密场景问，给安全感也便深挖。",
  "how":"接管新团队21问拆4场1:1：①信任（工作外 energized/为何选这公司/最好最差老板团队/最感激）领导也自答；②偏好与动态（反馈方式/微管点/认可方式/1:1节奏）；③积怨与改进（想改不想改/ taboo/挫折/改进机会）；④动机志向（最 motivating 项目/对公司兴奋点/进步障碍）。私密1:1分场问，给安全感也便深挖。",
  "url":"https://knowyourteam.com/blog/2022/06/12/21-questions-to-ask-when-taking-over-a-new-team/",
  "note":"适用：② 新经理/新主管接手既有团队（Know Your Team·二手），21问拆3-4场1:1（信任/偏好/积怨/动机四类），私密场景给安全感也便深挖，用问题照亮盲区（上下级/接管新团队）。"},
 {"emoji":"🗂️","cat":"新主管首次1:1","rel":"r2","src":"b2",
  "title":"新主管首次 1:1 结构化七问·历史/优先级/状态/顾虑/优势/志向/生活",
  "val":"首周与团队成员1:1用结构化问题，既捞信息也释放信号（关心人+盯优先级+早露顾虑）。建议顺序：①History 在职多久/为何加入/最骄傲的成就；②Priorities 大图目标/未来90-120天top优先级；③Status 各优先级交付物与日期/红黄绿状态；④Concerns 项目/资源/路障/部门/文化顾虑+我怎么帮；⑤个人优势与发展区+我怎么助你成长；⑥职业志向+我怎么帮你达成；⑦愿意分享的工作外生活。前尾都关于人，中段显式盯优先级与review机制，第4问早露顾虑降盲区，第7问显关心。回应要听/反射/澄清/暂缓判断，首周 powder dry 不下结论。",
  "how":"新主管首次1:1七问（按序）：历史（在职/为何来/最骄傲）→优先级（大图/90-120天top）→状态（交付物/日期/红黄绿）→顾虑（项目/资源/路障/部门/文化+我怎么帮）→优势发展区→职业志向→工作外生活。前尾都关于人、中段盯优先级；早问顾虑降盲区，首周powder dry缓判断，听>说。",
  "url":"http://www.adsuminsights.com/first-100-days-initial-meetings-with-your-staff",
  "note":"适用：② 新主管/经理首周与成员1:1（Adsum Insights·二手），结构化七问（历史/优先级/状态/顾虑/优势/志向/生活），信号=关心人+盯优先级+早露顾虑，首周缓判断（上下级/新主管首次1:1）。"},
 {"emoji":"🛡️","cat":"心理安全感","rel":"r2","src":"b2",
  "title":"心理安全感三练习·价值观工作坊 / Fear Conversation / 无责备复盘",
  "val":"经理可直接带的三练习：①Values & Behaviours 工作坊——团队共创价值观再推导出行为（如「无责怪」→「对失误集体负责」），须团队拥有而非自上而下；产出共同行为期待=安全感基底。②Fear Conversation——白板三栏 Fear/Mitigations/Target Norm，leader先说自己恐惧示范脆弱，团队共拟缓解动作与「理想准则」（如人人可犯错无惧报复）；把开放变常态。③Retrospectives——定期复盘找失败根因不归咎不羞辱，成功也复盘；在非公开处、不录制，让人敢坦诚。附心理安全感 IN/OUT、团队绩效矩阵等。",
  "how":"经理带心理安全感三练习：①价值观工作坊（团队共创价值观→推导行为，须团队拥有）；②Fear Conversation（白板 Fear/缓解/理想准则三栏，leader先说恐惧示范脆弱）；③无责备复盘（定期找根因不归咎、成功也复盘、非公开不录制）。把开放与容错变团队常态。",
  "url":"https://psychsafety.co.uk/three-simple-exercises-to-build-psychological-safety-in-your-team/",
  "note":"适用：② 经理在团队内建心理安全感（PsychSafety.co.uk·二手），三练习（价值观工作坊/Fear Conversation/无责备复盘），leader先示范脆弱、团队共创行为期待（上下级/心理安全感）。"},
 {"emoji":"📅","cat":"首次团队会议","rel":"r2","src":"b2",
  "title":"首次团队会议 6 要素议程·破冰 + 我怎么支持你 + 沟通规范 + 节奏 + 期望 + Q&A",
  "val":"新经理/接手新团队首会6项：①Icebreaker（如「这周工作外最 jazzed 的一件事」，每周轮换fun question提气场）；②我作为经理怎么最好支持团队（先自举例再round-table）；③团队最佳沟通方式（按工具切分：Slack即时/Asana项目/Jira工程/1:1）；④会议节奏（何时/何地/频率，远程用哪虚拟间，如2周sprint双周1h）；⑤期望（团队日常价值观/心理安全空间/「完成」定义/是否鼓励跨角色）；⑥Q&A 留白。会前发邮件附议程降低焦虑；30-45分钟；round-table让每人发声。把首会变成工作契约而非演讲。",
  "how":"首次团队会议6要素：破冰（如「本周最 jazzed 一事」）→我怎么最好支持你（自举例+round-table）→最佳沟通方式（按工具切分）→会议节奏（何时/地/频/远程间）→期望（价值观/心理安全/完成定义）→Q&A。会前发邮件附议程降焦虑，30-45min，round-table人人发声。",
  "url":"https://hypercontext.com/blog/meetings/first-team-meeting-agenda",
  "note":"适用：② 新经理首场团队会议（Hypercontext·二手），6要素议程（破冰/支持/沟通/节奏/期望/Q&A），会前发邮件+round-table，把首会变工作契约非演讲（上下级/首次团队会议）。"},
 {"emoji":"🔔","cat":"心理安全感仪式","rel":"r2","src":"b2",
  "title":"心理安全感日常仪式·一词打卡 / 赞赏圈 / 失误故事轮 / 潜规则拆解",
  "val":"经理可嵌入日常的小仪式：①One-word check-in 会前每人一词形容当下情绪，低门槛情绪诚实+快速 pulse；②Team appreciation circle 轮流给同事具体表扬（重努力/助人/成长非仅结果），变月度节奏提士气；③Mistake story round 人人（含领导）讲一次失误与所学，领导先讲示范安全、把不完美正常化；④Unwritten rules unpacked 团队脑暴职场/团队潜规则（大家默认但不说），共省「帮或碍安全感」；⑤Blind spots brainstorm 问「我们漏了什么/谁没被听见」，促关键思考与主人翁。HR经理尤可借onboarding/反馈文化定调。",
  "how":"心理安全感日常仪式：一词打卡（会前每人一词形容情绪，低门槛 pulse）、赞赏圈（轮流具体表扬，月度节奏）、失误故事轮（含领导先讲，把不完美正常化）、潜规则拆解（脑暴默认但不说的规则，共省帮/碍安全）、盲区脑暴（「漏了什么/谁没被听见」）。小仪式持续嵌入非一次性。",
  "url":"https://mci.edu.au/articles/building-psychological-safety-in-teams-hr-leaders",
  "note":"适用：② 经理/HR 在日常建心理安全感（MCI·二手），五仪式（一词打卡/赞赏圈/失误故事轮/潜规则拆解/盲区脑暴），小投入持续嵌入、领导先示范（上下级/心理安全感仪式）。"},
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

n3 = [c for c in cards if c['rel']=='r3']
n2 = [c for c in cards if c['rel']=='r2']
print("N=", len(cards), "③=", len(n3), "②=", len(n2))

# ---------- 1) 独立增量页 runs/icebreaker-2026-09-09-r37.html ----------
run_html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>破冰 · 第37轮补采（独立页）</title>
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
    <h1>🤝 破冰 · 第37轮补采（独立页）</h1>
    <p>采集于 2026-09-09 ｜ 本轮新增 10 卡（③高管间 5 / ②上下级 5）｜ 六维评估 ｜ 一手/二手标注 ｜ 受众关系分层（仅②③，剔除①）｜ 累计总索引见 <a href="../icebreaker.html" style="color:#fff;text-decoration:underline;">icebreaker.html</a></p>
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
with open(os.path.join(RUNS, 'icebreaker-2026-09-09-r37.html'), 'w', encoding='utf-8') as f:
    f.write(run_html)
print("written run page")

# ---------- 2) 累计墙 icebreaker.html ----------
html = open(WALL, encoding='utf-8').read()
html = html.replace('<span class="tag">125 卡</span>', '<span class="tag">130 卡</span>')
html = html.replace('<span class="tag">194 卡</span>', '<span class="tag">199 卡</span>')

# hero log: insert R37 line before relbar
r37_log = ('<p style="margin-top:8px">本轮（三十七轮 2026-09-09）主线：新任CEO百天五阶段落地框架（pre-boarding 利益方地图+影响力/信任两轴+前30天只学不决策）、高管入职四阶段框架（stakeholder mapping 两问+倾听之旅3问+90天沟通计划）、新领导同化NLA完整指南（外部引导+2-3周后+30/90天跟进）、高管同化最佳实践（入职期拉长至6-12月+团队测评画像+领导人开场共识目标）、高管入职90天清单（按HR/IT/CEO董事会/新高管四角色分流）（③）；'
           '接管新团队21问分拆4场1:1、新主管首次1:1结构化七问（历史/优先级/状态/顾虑/优势/志向/生活）、心理安全感三练习（价值观工作坊/Fear Conversation/无责备复盘）、首次团队会议6要素议程（破冰+如何支持+沟通规范+节奏+期望+Q&A）、心理安全感日常仪式（一词打卡/赞赏圈/失误故事轮/潜规则拆解）（②）。</p>')
html = html.replace('<div class="relbar">', r37_log + '\n<div class="relbar">', 1)

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

# ---------- 3) index.json ----------
data = json.load(open(INDEX, encoding='utf-8'))
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
'''**本轮增量页（2026-09-08 · 三十六轮 R36）**：[icebreaker-2026-09-08-r36.html · GitHub Pages](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/runs/icebreaker-2026-09-08-r36.html)  
**本机源**：`knowledge-collection/icebreaker/runs/icebreaker-2026-09-08-r36.html`
**上轮增量页（2026-09-08 · 三十五轮 R35）**：[icebreaker-2026-09-08-r35.html · GitHub Pages](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/runs/icebreaker-2026-09-08-r35.html)''',
'''**本轮增量页（2026-09-09 · 三十七轮 R37）**：[icebreaker-2026-09-09-r37.html · GitHub Pages](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/runs/icebreaker-2026-09-09-r37.html)  
**本机源**：`knowledge-collection/icebreaker/runs/icebreaker-2026-09-09-r37.html`
**上轮增量页（2026-09-08 · 三十六轮 R36）**：[icebreaker-2026-09-08-r36.html · GitHub Pages](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/runs/icebreaker-2026-09-08-r36.html)''')

r37_bq = ('\n> 三十七轮补采 +10（2026-09-09，②×5/③×5）：新任CEO百天五阶段落地框架（pre-boarding 利益方地图+影响力/信任两轴+前30天只学不决策）、高管入职四阶段框架（stakeholder mapping 两问+倾听之旅3问+90天沟通计划）、新领导同化NLA完整指南（外部引导+2-3周后+30/90天跟进）、高管同化最佳实践（入职期拉长至6-12月+团队测评画像+领导人开场共识目标）、高管入职90天清单（按HR/IT/CEO董事会/新高管四角色分流）（③）；'
           '接管新团队21问分拆4场1:1、新主管首次1:1结构化七问（历史/优先级/状态/顾虑/优势/志向/生活）、心理安全感三练习（价值观工作坊/Fear Conversation/无责备复盘）、首次团队会议6要素议程（破冰+如何支持+沟通规范+节奏+期望+Q&A）、心理安全感日常仪式（一词打卡/赞赏圈/失误故事轮/潜规则拆解）（②）。本次全二手，定向补「新CEO百天五阶段/高管入职四阶段框架」「接管新团队21问/首次1:1七问/心理安全感练习与仪式」五个稀缺子域。')
s = s.replace(
'> 三十六轮补采 +10（2026-09-08，②×5/③×5）：高管入职 90 天三段（pre-boarding 语境+利益方引荐/30 天只学/60 天 quick win/90 天节奏）、前 90 天结构化建关系信任（30/60/90+KPI 度量）、团队同化新领导打破行话盲区、新领导同化 5 步流程 NLA、新任高管融入既有团队 5 策（③）；裁员重组后重建信任三步 LISTEN/REBUILD/SUSTAIN、新晋管理者 90 天破局（CCL 40% 低于预期+三坑）、新经理双向信任 onboarding+Talent Grid、远程/混合团队连接活动、新经理带既有团队 Stop-Start-Continue（②）。本次全二手，定向补「高管入职/新领导同化」「重组信任修复/新晋管理/远程团队连接」五个稀缺子域。',
'> 三十六轮补采 +10（2026-09-08，②×5/③×5）：高管入职 90 天三段（pre-boarding 语境+利益方引荐/30 天只学/60 天 quick win/90 天节奏）、前 90 天结构化建关系信任（30/60/90+KPI 度量）、团队同化新领导打破行话盲区、新领导同化 5 步流程 NLA、新任高管融入既有团队 5 策（③）；裁员重组后重建信任三步 LISTEN/REBUILD/SUSTAIN、新晋管理者 90 天破局（CCL 40% 低于预期+三坑）、新经理双向信任 onboarding+Talent Grid、远程/混合团队连接活动、新经理带既有团队 Stop-Start-Continue（②）。本次全二手，定向补「高管入职/新领导同化」「重组信任修复/新晋管理/远程团队连接」五个稀缺子域。' + r37_bq)

table_rows = []
for i, c in enumerate(cards, start=320):
    rel_txt = '③高管间' if c['rel']=='r3' else '②上下级'
    src_txt = '一手' if c['src']=='b1' else '二手'
    table_rows.append("| {} | {} | {} | {} | {} |".format(i, c['title'], rel_txt, src_txt, c['note']))
sec = ("\n## 轮次 20260909-r37（+10）\n"
       "| # | 卡片 | 关系档 | 一手/二手 | 核心要点 |\n"
       "|---|---|---|---|---|\n" + "\n".join(table_rows) + "\n")
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
title: 破冰-2026-09-09-第三十七轮-知识卡
type: 自动化采集
date: 2026-09-09
tags: [知识采集, 破冰, 第三十七轮]
relation: [supervisor, exec]
---

# 破冰 · 第三十七轮补采（2026-09-09，+10）

> 本轮独立页（GitHub Pages）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/runs/icebreaker-2026-09-09-r37.html
> 本地路径：C:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection/icebreaker/runs/icebreaker-2026-09-09-r37.html
> 累计总索引墙：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/icebreaker.html

## 本轮新增 10 卡（关系分层）

### ③ 领导↔领导（高管间 · exec）— 5 卡
- 新任 CEO 百天五阶段框架·pre-boarding 利益方地图 + 前 30 天只学不决策〔二手〕
- 高管入职四阶段框架·stakeholder mapping 两问 + 倾听之旅 3 问 + 90 天沟通计划〔二手〕
- 新领导同化（NLA）完整指南·外部引导 + 入职后 2–3 周 + 30/90 天跟进〔二手〕
- 高管同化最佳实践·入职期拉长至 6–12 月 + 团队测评画像 + 领导人开场共识目标〔二手〕
- 高管入职 90 天清单·按 HR/IT/CEO董事会/新高管 四角色分流 + 4 大坑〔二手〕

### ② 领导↔员工（上下级 · supervisor）— 5 卡
- 接管新团队 21 问·拆成 3–4 场 1:1（信任/偏好/积怨/动机 四类）〔二手〕
- 新主管首次 1:1 结构化七问·历史/优先级/状态/顾虑/优势/志向/生活〔二手〕
- 心理安全感三练习·价值观工作坊 / Fear Conversation / 无责备复盘〔二手〕
- 首次团队会议 6 要素议程·破冰 + 我怎么支持你 + 沟通规范 + 节奏 + 期望 + Q&A〔二手〕
- 心理安全感日常仪式·一词打卡 / 赞赏圈 / 失误故事轮 / 潜规则拆解〔二手〕
'''
os.makedirs(os.path.dirname(RUNNOTE), exist_ok=True)
open(RUNNOTE, 'w', encoding='utf-8').write(note)
print("run note written")

# ---------- 7) lexiang-entry-map.json (追加 pending round) ----------
m = json.load(open(MAPF, encoding='utf-8'))
ib = m['icebreaker']
ib['rounds'].append({
    "date": "2026-09-09",
    "entry_id": None,
    "name": "icebreaker-2026-09-09-r37.html",
    "note": "轮次页 R37 (+10：5③高管间+5②上下级)｜乐享待补传(token 401 过期，待重配 mcp.json lxmcp_ token 后补传并回填 entry_id)"
})
json.dump(m, open(MAPF, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print("lexiang map updated, rounds:", len(ib['rounds']))
print("DONE")
