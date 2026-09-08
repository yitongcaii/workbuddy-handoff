# -*- coding: utf-8 -*-
# 破冰 R36 构建脚本（2026-09-08）· 5 ③高管间 + 5 ②上下级，全 NEW（M=0）
import os, re, json

BASE = r'C:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection'
IB = os.path.join(BASE, 'icebreaker')
WALL = os.path.join(IB, 'icebreaker.html')
RUNS = os.path.join(IB, 'runs')
INDEX = os.path.join(BASE, 'index.json')
VAULT = r'C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库'
SUM = os.path.join(VAULT, '素材', 'icebreaker', '破冰-知识卡汇总.md')
IDX = os.path.join(VAULT, '00-知识采集索引.md')
RUNNOTE = os.path.join(VAULT, '素材', 'icebreaker', 'runs', '破冰-2026-09-08-第三十六轮-知识卡.md')

DATE = '2026-09-08'
ROUND = 'r36'

# ---------- 10 卡 ----------
# rel: 'r3'(③高管间/exec) | 'r2'(②上下级/supervisor); src: 'b2'(二手) | 'b1'(一手)
cards = [
 # ===== ③ 高管间（exec）=====
 {"emoji":"🪪","cat":"高管入职","rel":"r3","src":"b2",
  "title":"高管入职 90 天计划·pre-boarding 利益方引荐 + 30/60/90 学-对齐-执行",
  "val":"Enboarder 框架：pre-boarding（入职前）即启动——自动发战略文档/董事会材料/年报让高管吸收语境，指派 buddy/transition mentor 并由 CEO/董事发非正式欢迎；D1–30 纯学习（结构化利益方会议：同侪/直属/跨职能，问问题而非改革）；D31–60 对齐诊断出路线图（拿 quick wins 建早期可信度+深化团队信任）；D61–90 执行建沟通节奏（例行 1:1/跨职能 check-in/董事会汇报）。按角色定制（CRO 偏客户+CRM，CHRO 偏文化+员工情绪）。",
  "how":"高管入职 90 天分三段：pre-boarding 先发语境+指派 buddy/导师、CEO 非正式欢迎；D1-30 只学不听改（结构化利益方 1:1）；D31-60 拿 low-hanging quick wins 建可信度+对齐路线图；D61-90 建例行沟通节奏。按职能定制（CRO 重客户/CRM，CHRO 重文化/员工情绪）。",
  "url":"https://enboarder.com/blog/executive-onboarding",
  "note":"适用：③ 新任高管/C-suite 入职落地——90 天三段（pre-boarding 语境+利益方引荐 / 30 天只学 / 60 天 quick win / 90 天节奏）（Enboarder·二手），按角色定制，先建关系再出成绩（高管间/高管入职）。"},
 {"emoji":"🧩","cat":"高管入职","rel":"r3","src":"b2",
  "title":"高管入职前 90 天·建关系与信任的结构化框架 + 度量（过渡期领导力）",
  "val":"Leadership-development.net：前 90 天是建关系与信任的关键窗，须结构化连接关键利益方（直属/跨职能/同侪/高层），不止 direct reports；用 30/60/90 里程碑例会与反馈闭环加速信任；透明度+积极倾听+双向反馈建可信度；用 KPI（短期整合+长期发展）与直接下属/利益方反馈度量 onboarding 成败；入职后持续辅导（mentor/教练+跨职能项目）嵌入日常。",
  "how":"高管入职用 30/60/90 里程碑例会+反馈闭环；早期系统连接关键利益方（同侪/跨职能/高层，不止直属）；透明度+积极倾听+双向反馈建可信度；用 KPI+利益方反馈度量成败；入职后配 mentor/教练+跨职能项目持续嵌入。",
  "url":"https://www.leadership-development.net/blog/mastering-executive-onboarding-for-successful-leadership-transitions",
  "note":"适用：③ 高管入职过渡期——前 90 天结构化建关系信任（leadership-development.net·二手），30/60/90 里程碑+反馈闭环+KPI 度量，连接同侪/跨职能/高层（高管间/领导力过渡）。"},
 {"emoji":"🧱","cat":"新领导同化","rel":"r3","src":"b2",
  "title":"团队同化新领导·打破行话盲区 + 共享历史 + 欢迎节奏（领导胜任力）",
  "val":"Transformation Management：长期共事团队会沉淀专属行话/黑话、假设与共享记忆，让新领导（尤其外部空降）天然「局外人」。给新领导的做法：第一周多次自我介绍记名字、盘点并解释内部 acronym/行话、引用过往事件时补背景、指文档存哪、安排与同侪一对一 orientation；团队也要主动邀请新领导评论观察（「为啥我们这么做」别超过一两次）。新领导别反复比对自己旧公司。",
  "how":"团队同化新领导：第一周多次自我介绍记名字、盘点并解释内部行话/acronym、引旧事件补背景、指文档位置、安排与同侪 1:1；新领导多问少比旧公司、团队主动邀其观察反馈。把「局外人」盲区显性化来消排异。",
  "url":"https://transformationmanagement.com/leadership-competency-integrating-a-new-leader/",
  "note":"适用：③ 团队迎接空降/新任高管——打破行话盲区+共享历史（transformationmanagement.com·二手），多次自我介绍/解释黑话/补旧事件背景/同侪 1:1，消「局外人」排异（高管间/新领导同化）。"},
 {"emoji":"🔄","cat":"新领导同化","rel":"r3","src":"b2",
  "title":"新领导同化流程（NLA）·团队先问 4 问→领导离场→回应→持续对话（5 步）",
  "val":"BizTimes（Vernal Mgmt）：New Leader Assimilation 由 HR/OD 引导，直下属与新领导在安全空间互识、建信任。5 步：① 欢迎+说明流程；② 领导离圈，团队答 6 问（已知 Tom 什么/想知什么/对 Tom 的顾虑/想要 Tom 给什么/要 Tom 知什么/组织要 Tom 什么）；③ 休息时把回答交给 Tom 反思；④ Tom 回圈回应、转成对话而非 Q&A；⑤ 领导承诺跟进+定期续谈。结果：双方互懂期待、团队彼此更懂、开门持续沟通。",
  "how":"新领导同化流程 5 步：领导先欢迎→离场，团队答 6 问（已知/想知/顾虑/要他给/要他知/组织要他什么）→休息交 Tom 反思→回圈回应转对话→承诺跟进+定期续谈。HR/OD 引导，安全空间建信任。",
  "url":"https://biztimes.com/bringing-the-new-boss-on-board/",
  "note":"适用：③ 新任 CEO/高管与直下属破冰同化——5 步同化流程（BizTimes·二手），团队先问 6 问、领导离场反思再回应，把陌生变互懂期待（高管间/新领导同化）。"},
 {"emoji":"🤝","cat":"新任高管融入","rel":"r3","src":"b2",
  "title":"新任高管融入既有团队 5 策·破冰介绍/学文化/一对一/讲管理风格/庆成就",
  "val":"Rees Marx：新高管空降既有团队易因假设/未知引发震荡。5 策：① 计划破冰与自我介绍（开会让团队认识你、分享一点自己，别躲会议室）；② 花时间学现有团队文化（每团队有长期默契习惯，先懂再改）；③ 给每个成员聚焦一对一（诊断团队强弱、建 rapport）；④ 讲清你的管理风格与期望（透明说明怎么管、要什么，缓焦虑）；⑤ 庆祝团队成就（肯定过往亮点+共设目标，渐变非突变）。",
  "how":"新任高管融入既有团队 5 策：计划破冰自我介绍（别躲会议室）、学现有团队文化（先懂再改）、给每人聚焦 1:1 诊断强弱、透明讲管理风格与期望、庆祝过往成就+渐变改革。缓焦虑、建信任。",
  "url":"https://reesmarx.com/blog-post/5-team-building-strategies-for-newly-hired-executive-leaders/",
  "note":"适用：③ 空降高管接手既有团队——5 策融入（reesmarx.com·二手），破冰介绍/学文化/一对一/讲风格/庆成就，先建信任再渐进改革（高管间/新任高管融入）。"},

 # ===== ② 上下级（supervisor）=====
 {"emoji":"🩹","cat":"重组信任修复","rel":"r2","src":"b2",
  "title":"裁员/重组后重建信任三步走·LISTEN 听情绪 / REBUILD 复清晰 / SUSTAIN 稳行为",
  "val":"Inpulse：裁员后幸存者出现幸存者内疚、过度警觉、情绪耗竭、安静离职——信任不会自动恢复，须有意重建。三步走：LISTEN（30 天内做倾听循环：小组会话/越级/引导对话+脉冲调研+给经理 check-in 模板）；REBUILD（月度「业务现状」更新保透明、训经理变革沟通与心理安全、重确认优先级、再平衡工作量、刷新发展与晋升对话）；SUSTAIN（保持透明节奏、用脉冲数据查心理安全、庆祝小胜、把福祉/工作量检查变日常管理）。文化/信任靠「有意且可见的领导力」恢复。",
  "how":"裁员/重组后重建信任三步：LISTEN（30 天内小组/越级倾听+脉冲调研+给经理 check-in 模板）；REBUILD（月度业务现状更新+训经理变革沟通/心理安全+重确认优先级+再平衡工作量）；SUSTAIN（持续透明节奏+脉冲查心理安全+庆祝小胜+福祉变日常管理）。先恢复心理安全再追绩效。",
  "url":"https://www.inpulse.com/redundancies-what-leaders-get-wrong",
  "note":"适用：② 经理/中层在裁员重组后重建团队信任（Inpulse·二手），LISTEN/REBUILD/SUSTAIN 三步，先复心理安全再追绩效（上下级/重组信任修复）。"},
 {"emoji":"📈","cat":"新晋管理者","rel":"r2","src":"b2",
  "title":"新晋管理者 90 天破局·CCL 40% 低于预期 + 3 大坑 + 30/45/90 行动",
  "val":"腾讯网（CCL 创意领导力中心数据）：超 40% 新任管理者头 18 个月「低于预期或明显失败」，其中 80%+ 能力没问题、是没意识到「角色已变」。华为统计新干部快速胜任仅 30%、空降成活率<10%。三坑：事必躬亲的超级英雄/急于烧三把火的爆破专家/只做兄弟的和平使者。行动：D1–30 思维破壁（60% 精力识人用人育人、与每人深度 1:1、首月不宣布重大决策）；D1–45 沟通破冰（向上对齐期望+团队启动会坦诚分享理念）；D30–90 绩效破局（锁速赢小胜+把功劳归下属）。",
  "how":"新晋管理者 90 天：D1-30 思维破壁（60% 精力识人用人、与每人深度 1:1、首月不宣布重大决策）；D1-45 沟通破冰（向上对齐期望+团队启动会坦诚分享）；D30-90 绩效破局（锁周期短见效快的速赢+把功劳归具体下属）。避三坑：别事事亲为/别急着烧三把火/别只做兄弟。",
  "url":"https://new.qq.com/rain/a/20260807A0EF9H00",
  "note":"适用：② 新晋/新任基层管理者 90 天破局（腾讯网·CCL 数据·二手），40% 低于预期、三坑三阶段，先关系破冰再绩效破局（上下级/新晋管理）。"},
 {"emoji":"🧭","cat":"新经理入职","rel":"r2","src":"b2",
  "title":"新经理 onboarding 团队·双向信任 + 30-60-90 + Talent Grid 识团队强弱",
  "val":"Talent Plus：团队迎新经理如学生迎新老师——既期待又怕被改。信任是双向的：新经理别急着说「我旧公司怎么做的」（易被视为否定现有文化），要中心 curiosity 与学习心态；用关系建设活动让团队看到管理者也是「完整的人」。早期做 talent 测评看管理者的 top-5 天赋主题、用 Talent Grid 识团队强弱与缺口（缺口当共同成长机会）；走 30-60-90 计划，90 天做绩效回顾，围绕 TeamView 倡议定一年目标，开发对话才有根基。",
  "how":"新经理 onboarding 团队：双向信任（管理者中心好奇心、少比旧公司、用关系活动露真实自己）；早期 talent 测评看自身 top-5 天赋+用 Talent Grid 识团队强弱缺口；走 30-60-90，90 天绩效回顾+定一年目标+开发对话。信任先建再探缺口。",
  "url":"https://talentplus.com/blog/get-ready-onboarding-a-team-manager/",
  "note":"适用：② 新经理接手既有团队 onboarding（Talent Plus·二手），双向信任+30-60-90+Talent Grid 识强弱，先关系再探缺口（上下级/新经理入职）。"},
 {"emoji":"🌐","cat":"远程团队连接","rel":"r2","src":"b2",
  "title":"远程/混合高绩效团队·优势地图/异步破冰/微 retreat/认可仪式（可度量）",
  "val":"Inside the Team：分布式团队须有意设计连接。核心原则：心理安全、目标对齐、包容公平、持续优于一次性。高影响力活动：优势地图（每人共享 top 优势+被支持方式，30–45min 讨论重叠与缺口）；项目制 sprint（真实问题的迷你黑客松）；学习圈（轮值同伴教学）；虚拟共工块（可选专注+首尾打卡减孤立）；异步破冰（共享文档/chat 帖「本周小赢」跨时区参与）；微 retreat/步行会（短 offsite 反思+轻规划）；认可仪式（周 shoutout/kudos 轮/轮值 team hero）。用脉冲调研+参与率+留存+交付可度量。",
  "how":"远程/混合团队连接：优势地图（共享 top 优势+被支持方式）、异步破冰（共享文档/chat「本周小赢」跨时区）、微 retreat/步行会、认可仪式（周 shoutout/kudos）；配虚拟共工块减孤立；用脉冲调研+参与率+留存度量。持续小投入>一次性大活动。",
  "url":"https://insidetheteam.com?p=593/",
  "note":"适用：② 经理带远程/混合分布式团队建连接（insidetheteam.com·二手），优势地图/异步破冰/微 retreat/认可仪式，持续小投入+可度量（上下级/远程团队连接）。"},
 {"emoji":"🔧","cat":"新经理带老团队","rel":"r2","src":"b2",
  "title":"新经理带既有团队·沟通支持 + Stop-Start-Continue + 轮桌对话",
  "val":"Ragan（企业传播视角）：新/空降经理最贴近员工的领导触点，应给对支持——早澄清汇报结构与角色定位、提供工具（Slack/Asana/内网/品牌话术/组织架构图/领导 talking points），AI 与模板缩短适应期；让经理从一开始就沟通「管理风格+相关成功+热情」建同侪情谊；分散团队多上路见面。持续一致的团队建设才有效：志愿/健康挑战/心理假；请每人带 1 次 5 分钟破冰或轮值主持；中小 roundtable 摸组织各层脉搏；Stop-Start-Continue 建诚实对话框架。",
  "how":"新经理带既有团队：早给汇报结构+工具（协作/项目/内网/话术/架构图/talking points）+AI 模板缩短适应；从首日开始讲管理风格与热情建情谊；分散团队多上路见面；用 Stop-Start-Continue+中小 roundtable 建诚实对话、请每人轮值 5 分钟破冰/主持。",
  "url":"https://www.ragan.com/?p=322978",
  "note":"适用：② 新/空降经理带既有（尤其分散）团队（Ragan·二手），给工具+讲风格+Stop-Start-Continue roundtable，一致团队建设>一次性（上下级/新经理带老团队）。"},
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

# ---------- 1) 独立增量页 runs/icebreaker-2026-09-08-r36.html ----------
run_html = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>破冰 · 第36轮补采（独立页）</title>
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
.back{display:inline-block;margin:0 0 14px;font-size:13px;color:var(--accent2);text-decoration:none;font-weight:600;}
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
    <h1>🤝 破冰 · 第36轮补采（独立页）</h1>
    <p>采集于 2026-09-08 ｜ 本轮新增 10 卡（③高管间 5 / ②上下级 5）｜ 六维评估 ｜ 一手/二手标注 ｜ 受众关系分层（仅②③，剔除①）｜ 累计总索引见 <a href="../icebreaker.html" style="color:#fff;text-decoration:underline;">icebreaker.html</a></p>
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
with open(os.path.join(RUNS, 'icebreaker-2026-09-08-r36.html'), 'w', encoding='utf-8') as f:
    f.write(run_html)
print("written run page")

# ---------- 2) 累计墙 icebreaker.html ----------
html = open(WALL, encoding='utf-8').read()
html = html.replace('<span class="tag">120 卡</span>', '<span class="tag">125 卡</span>')
html = html.replace('<span class="tag">189 卡</span>', '<span class="tag">194 卡</span>')

# hero log: insert R36 line before relbar
r36_log = ('<p style="margin-top:8px">本轮（三十六轮 2026-09-08）主线：高管入职 90 天三段落地与「新领导同化」流程（pre-boarding 利益方引荐 / 30-60-90 学-对齐-执行 / NLA 5 步同化 / 空降高管 5 策融入）（③）；'
           '裁员重组后重建信任 LISTEN-REBUILD-SUSTAIN 三步、新晋管理者 90 天破局（CCL 40% 低于预期）、新经理双向信任 onboarding+Talent Grid、远程/混合团队连接活动、新经理带既有团队 Stop-Start-Continue（②）。</p>')
html = html.replace('<div class="relbar">', r36_log + '\n<div class="relbar">', 1)

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
# update 本轮增量页 link (lines 19-21 region): replace the R35 本轮 block with R36 + push R35 to 上轮
s = s.replace(
'''**本轮增量页（2026-09-08 · 三十五轮 R35）**：[icebreaker-2026-09-08-r35.html · GitHub Pages](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/runs/icebreaker-2026-09-08-r35.html)  
**本机源**：`knowledge-collection/icebreaker/runs/icebreaker-2026-09-08-r35.html`
**上轮增量页（2026-09-04 · 三十轮 R30）**：[icebreaker-20260904.html · GitHub Pages](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/icebreaker-20260904.html)''',
'''**本轮增量页（2026-09-08 · 三十六轮 R36）**：[icebreaker-2026-09-08-r36.html · GitHub Pages](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/runs/icebreaker-2026-09-08-r36.html)  
**本机源**：`knowledge-collection/icebreaker/runs/icebreaker-2026-09-08-r36.html`
**上轮增量页（2026-09-08 · 三十五轮 R35）**：[icebreaker-2026-09-08-r35.html · GitHub Pages](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/runs/icebreaker-2026-09-08-r35.html)''')

# append round blockquote after R35 blockquote
r36_bq = ('\n> 三十六轮补采 +10（2026-09-08，②×5/③×5）：高管入职 90 天三段（pre-boarding 语境+利益方引荐/30 天只学/60 天 quick win/90 天节奏）、前 90 天结构化建关系信任（30/60/90+KPI 度量）、团队同化新领导打破行话盲区、新领导同化 5 步流程 NLA、新任高管融入既有团队 5 策（③）；'
           '裁员重组后重建信任三步 LISTEN/REBUILD/SUSTAIN、新晋管理者 90 天破局（CCL 40% 低于预期+三坑）、新经理双向信任 onboarding+Talent Grid、远程/混合团队连接活动、新经理带既有团队 Stop-Start-Continue（②）。本次全二手，定向补「高管入职/新领导同化」「重组信任修复/新晋管理/远程团队连接」五个稀缺子域。')
s = s.replace(
'> 三十五轮补采 +8（2026-09-08，②×5/③×3）：高管务虚精致破冰·Future Headlines/Artifact Introduction/User Manual to Me+opt-in 文化（③）；CEO 冒险式熔炼·登山/漂流/深潜共享挑战卸 urban mask（③）；领导力静修六类活动菜单+WHY.os 框架（③）；会议 5 分钟暖场 Rose/Thorn/Bud 检查法（②）；65 个会议破冰问题库按会议类型分层（②）；基层管理者赋能工作坊·管理者角色卡破冰+团队画像共创·一手案例（②）；25 个破冰问题按深度分层+四类目标活动（②）；新经理首场员工会·Weather Check+带零食破冰议程（②）。本次 1 手 / 7 二手，定向补「高管精致破冰/CEO 冒险熔炼/静修活动菜单」「日常会议暖场/问题库/新经理首会/基层管理者工作坊」八个稀缺子域。',
'> 三十五轮补采 +8（2026-09-08，②×5/③×3）：高管务虚精致破冰·Future Headlines/Artifact Introduction/User Manual to Me+opt-in 文化（③）；CEO 冒险式熔炼·登山/漂流/深潜共享挑战卸 urban mask（③）；领导力静修六类活动菜单+WHY.os 框架（③）；会议 5 分钟暖场 Rose/Thorn/Bud 检查法（②）；65 个会议破冰问题库按会议类型分层（②）；基层管理者赋能工作坊·管理者角色卡破冰+团队画像共创·一手案例（②）；25 个破冰问题按深度分层+四类目标活动（②）；新经理首场员工会·Weather Check+带零食破冰议程（②）。本次 1 手 / 7 二手，定向补「高管精致破冰/CEO 冒险熔炼/静修活动菜单」「日常会议暖场/问题库/新经理首会/基层管理者工作坊」八个稀缺子域。' + r36_bq)

# append ## 轮次 table at end
table_rows = []
for i, c in enumerate(cards, start=310):
    rel_txt = '③高管间' if c['rel']=='r3' else '②上下级'
    src_txt = '一手' if c['src']=='b1' else '二手'
    table_rows.append("| {} | {} | {} | {} | {} |".format(i, c['title'], rel_txt, src_txt, c['note']))
sec = ("\n## 轮次 20260908-r36（+10）\n"
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
title: 破冰-2026-09-08-第三十六轮-知识卡
type: 自动化采集
date: 2026-09-08
tags: [知识采集, 破冰, 第三十六轮]
relation: [supervisor, exec]
---

# 破冰 · 第三十六轮补采（2026-09-08，+10）

> 本轮独立页（GitHub Pages）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/runs/icebreaker-2026-09-08-r36.html
> 本地路径：C:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection/icebreaker/runs/icebreaker-2026-09-08-r36.html
> 累计总索引墙：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/icebreaker.html

## 本轮新增 10 卡（关系分层）

### ③ 领导↔领导（高管间 · exec）— 5 卡
- 高管入职 90 天计划·pre-boarding 利益方引荐 + 30/60/90 学-对齐-执行〔二手〕
- 高管入职前 90 天·建关系与信任的结构化框架 + 度量（过渡期领导力）〔二手〕
- 团队同化新领导·打破行话盲区 + 共享历史 + 欢迎节奏（领导胜任力）〔二手〕
- 新领导同化流程（NLA）·团队先问 4 问→领导离场→回应→持续对话（5 步）〔二手〕
- 新任高管融入既有团队 5 策·破冰介绍/学文化/一对一/讲管理风格/庆成就〔二手〕

### ② 领导↔员工（上下级 · supervisor）— 5 卡
- 裁员/重组后重建信任三步走·LISTEN 听情绪 / REBUILD 复清晰 / SUSTAIN 稳行为〔二手〕
- 新晋管理者 90 天破局·CCL 40% 低于预期 + 3 大坑 + 30/45/90 行动〔二手〕
- 新经理 onboarding 团队·双向信任 + 30-60-90 + Talent Grid 识团队强弱〔二手〕
- 远程/混合高绩效团队·优势地图/异步破冰/微 retreat/认可仪式（可度量）〔二手〕
- 新经理带既有团队·沟通支持 + Stop-Start-Continue + 轮桌对话〔二手〕
'''
os.makedirs(os.path.dirname(RUNNOTE), exist_ok=True)
open(RUNNOTE, 'w', encoding='utf-8').write(note)
print("run note written")
print("DONE")
