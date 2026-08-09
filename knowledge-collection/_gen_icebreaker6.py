# -*- coding: utf-8 -*-
import json, io

HTML = "icebreaker/icebreaker.html"
IDX = "index.json"

# ---------- ③ 高管间 (3 new cards) ----------
cards_exec = [
    {
        "emoji": "🧱", "cat": "高管团队框架",
        "title": "Lencioni 五 dysfunction 模型·高管团队诊断与修复",
        "val": "Patrick Lencioni《团队协作的五大障碍》(2002)金字塔模型，专为高管团队设计——①信任缺失(不愿暴露脆弱)→②惧怕冲突(表面和谐不敢争)→③欠缺投入(没被听见故不承诺)→④逃避担责(不互 hold 同伴)→⑤忽视结果(个人/部门凌驾团队)。正向逆推：建脆弱信任→鼓励建设性冲突→达成清晰承诺→同伴互担责→聚焦集体结果。何时用：聪明但不合拍的高管团队、重组/换帅后速建新 top team、跨职能 interdependent 团队、并购整合期。强调「团队级模型」——靠显式规范与例会/决策日志/OKR 等机制把行为变可追踪承诺，而非性格测试。",
        "inner": "高管团队用 Lencioni 金字塔自下而上诊断(先查信任与冲突，不直奔担责)；配决策日志/OKR/仪表盘把「行为」变成可追踪承诺；重组或并购后优先用来把「职能负责人联邦」变成「企业领导团队」。",
        "url": "https://umbrex.com/resources/frameworks/organization-frameworks/lencioni-five-dysfunctions-of-a-team-model",
        "display": "umbrex.com/.../lencioni-five-dysfunctions-of-a-team-model",
        "note": "适用：③ 高管团队(尤重组/换帅/并购后)用 Lencioni 金字塔做凝聚力诊断——自下而上修信任→冲突→承诺→担责→结果。",
    },
    {
        "emoji": "🎯", "cat": "高管共识",
        "title": "Purpose & Values 工作坊·对齐领导团队使命与决策",
        "val": "Purpose and Values Workshop 是结构化领导工作坊，帮高管团队(而非写官网口号)重新连接共同使命、定义真正重要的价值、把信念嵌进日常决策。流程：①澄清组织目的(我们为何存在/想创造什么影响/独特之处)②识别核心价值观(想鼓励的行为/领导期待/客户承诺/协作/担责标准)③对齐领导行为(沟通/决策/绩效/冲突/战略如何体现价值)④外部引导师确保客观、难话题被尊重讨论、每个声音被听见。收益：统一成功定义→沟通更顺→决策更快(用价值而非意见度量)→跨部门协作→员工敬业→变革韧性。信号：频繁高管分歧/方向困惑/敬业度下滑/重组/高速增长/领导更替/并购时最该做。",
        "inner": "高管团队用 Purpose&Values 工作坊把「使命价值」从墙上的口号变成决策标尺；请外部引导师保客观；让价值可度量(招聘/客户/创新都对照价值)，用价值而非个人意见做难决策。",
        "url": "https://verticaljournal.org/blog/purpose-and-values-workshop-to-align-your-leadership-team",
        "display": "verticaljournal.org/.../purpose-and-values-workshop-to-align-your-leadership-team",
        "note": "适用：③ 高管团队用 Purpose&Values 工作坊对齐使命与决策标尺——价值可度量、冲突用价值而非意见解决，重组/并购/领导更替时尤该做。",
    },
    {
        "emoji": "🤝", "cat": "高管对齐",
        "title": "高管团队对齐工作坊·诊断+2天+团队章程+跟进",
        "val": "高管团队对齐工作坊(教练交付框架)：即便最有经验的高管团队，优先级竞争/竖井/战略漂移也会让小缝隙在组织中放大成昂贵低效。结构：①前期诊断(个体领导力访谈+团队效能问卷+战略文档审阅，直击真实挑战)②两天现场工作坊——诊断集体效能强弱与屏障、围绕连战略的共同愿景、厘清角色与决策权消除重复摩擦、建立运营规范与冲突解决机制、深化信任把难对话变战略对话、承诺团队章程+担责计划③六周后 90 分钟跟进复盘承诺与 emergent 挑战。产出不止关系好，而是更快更聪明决策+可衡量组织影响的高绩效高管团队。适用于 C-suite/高管组。",
        "inner": "高管对齐工作坊用「前期诊断访谈+两天现场(愿景/决策权/规范/章程)+六周跟进」三段；强调先诊断再 workshop、把决策权与冲突机制写进团队章程、跟进 session 保新协议落地。",
        "url": "https://jakubgrzadzielski.com/coaching/high-performance-executive-team-alignment-workshop",
        "display": "jakubgrzadzielski.com/.../high-performance-executive-team-alignment-workshop",
        "note": "适用：③ 高管团队对齐(战略漂移/竖井/换帅后)——诊断访谈+两天 workshop+团队章程+六周跟进，把「职能头联邦」炼成企业领导团队。",
    },
]

# ---------- ② 上下级 (6 new cards) ----------
cards_sup = [
    {
        "emoji": "📋", "cat": "团队契约",
        "title": "Atlassian·Working Agreements Play +「与我共事说明书」",
        "val": "Atlassian Team Playbook 官方玩法(一手)：团队工作协议(Working Agreements)是团队共创的「如何一起工作」共享规范——何时/如何沟通、决策与升级路径、会议节奏。Teamwork Lab 实测：跑过此 Play 的员工 74% 更敢提出改进建议；能减少会议、清晰沟通、降误解、提心理安全、加速新人融入。何时跑：组队初期、新人加入、重组后、工作方式变化。关键动作：①每人填「与我共事说明书(User Manual)」——工作地/时区/工时/环境偏好/反馈接收方式/关于我；②leader 预填沟通渠道+升级流程(DACI)；③现场设基调(开放好奇/积极倾听/手机放下)④每人分享「刚学到的关于他人的一件新事」暖场；⑤共拟协议并随团队演进修订。把「人」而非「流程」放中心。",
        "inner": "经理用 Atlassian Working Agreements Play 建团队共享规范；让每人先写「与我共事说明书(User Manual)」暴露工作偏好；leader 预填沟通渠道+升级路径；现场以「刚学到关于他人的一件事」暖场；协议随团队演进定期复盘。",
        "url": "https://www.atlassian.com/team-playbook/plays/working-agreements",
        "display": "atlassian.com/team-playbook/plays/working-agreements",
        "note": "适用：② 经理带新团队/重组后/新人融入，用 Working Agreements + User Manual 把协作偏好显式化、降误解提心理安全(工具官方一手)。",
    },
    {
        "emoji": "🎭", "cat": "情境破冰",
        "title": "情境化破冰框架·跨职能/重组/危机/层级四场景",
        "val": "创始人无 HR 团队 onboarding 实战提炼：破冰不是通用套话，按场景定制才有效。①跨职能项目启动(工程+市场等多团队技术熟但语境陌生)——用「你最希望别的团队懂你团队怎么工作的一点」暴露真实功能误解与隐藏约束，3 分钟/人，答案成项目工作记忆；②重组/团队合并(同一公司却成陌生人，标准破冰显刻意)——直面张力：「你希望过去怎么工作能延续一点、又希望改掉一点」；③困难会议(裁员/坏消息/危机)——先简短承认当下，再用一词或 this-or-that 轻问(「今天你带着怎样的状态来」诚实不沉重)，深度留待后续 1:1；④强层级场合(高管与基层同室，junior 会退缩)——两条调整：senior 最后说(给 junior 先定深度)、用 chat 异步格式让 junior 不公开暴露。附「三会规则」：新格式连试三次再评判。",
        "inner": "经理按场景选破冰——跨职能用「希望别团队懂你什么」、重组用「延续/改变各一点」、危机用一词 check-in、层级场合让 senior 最后说+chat 异步；新格式连试三会再定去留。",
        "url": "https://firsthr.app/blog/performance/ice-breaker-questions-for-work",
        "display": "firsthr.app/.../ice-breaker-questions-for-work",
        "note": "适用：② 经理按四类情境(跨职能启动/重组合并/危机会议/强层级)定制破冰——暴露工作语境而非私生活，层级场合让 senior 最后发言+chat 异步降退缩。",
    },
    {
        "emoji": "⛓️", "cat": "越级沟通",
        "title": "Skip-level 会议·破冰与 100+ 提问库",
        "val": "Skip-level = 员工与其「经理的经理」一对一，目的是给管理者内部视角、给员工越级表达窗口，对齐公司目标。成功在提问。开场破冰建立 rapport 降紧张、捞真话：爱好/最近好书播客/想去哪旅行/想学技能/周末怎么过/最近骄傲的事等。再进深层：①团队动态(氛围/优势/改进点/协作/信息壁垒/冲突处理/是否被重视)②个人挑战与路障(最大挑战/拖慢你的事/缺的资源工具/压力应对/被支持感/希望移除的障碍)。管理者用轻量非工作问题开场更易挖到诚实意见。注意：Skip-level 是②上下级关系的「向上越级」变体，须以保护下属安全感为前提，不泄露来源。",
        "inner": "越级沟通(skip-level)用轻量爱好/周末类破冰开场降紧张，再问团队动态与个人路障；经理须保护来源、把听到的问题变成可行动改进，不泄露谁说。",
        "url": "https://krisp.ai/blog/skip-level-meeting-questions",
        "display": "krisp.ai/blog/skip-level-meeting-questions",
        "note": "适用：② 经理的经理与下属越级一对一(skip-level)——破冰降紧张+团队动态/路障提问库，须保护来源安全感。",
    },
    {
        "emoji": "🛡️", "cat": "心理安全感",
        "title": "管理者心理安全感实操指南·5 步建「敢说」文化",
        "val": "澳洲管理指南(给经理的实操)：员工是否敢说，取决于领导对「上一个开口的人」如何反应——一次轻蔑回应可毁数月信任。5 步：①感恩式回应——有人提问题先说「感谢你提出来，我们一起解决」再跟进，最快扭转文化；②会议以 check-in 开头——每人用一词描述状态或心头一事，2 分钟仪式常态化脆弱、微瞬间建立人联结，研究称数周内「敢说」行为+40%；③示弱建模——公开说「上周我搞错了，学到的是…」，不损权威反而以真实赚信任；④多问少说——用「我漏了什么/还有哪些没谈到的顾虑」替代陈述，对话中每 1 指令配≥2 问；⑤对提出的事闭环——承认→解释动作(或为何不)→公开致谢，忽视反馈最毁心理安全。附自查清单(10 条信号判断是否真安全)。",
        "inner": "经理建心理安全感=①对提问题的人先说「谢谢提出」再跟进②会议用一词 check-in 开头③公开示弱(我错了学到…)④每指令配≥2 问⑤对反馈闭环(承认+动作+致谢)；一次轻蔑回应可毁数月信任。",
        "url": "https://iap.edu.au/psychological-safety-guide-managers-australia",
        "display": "iap.edu.au/.../psychological-safety-guide-managers-australia",
        "note": "适用：② 经理系统化建团队心理安全感——check-in 仪式+示弱建模+多问少说+反馈闭环，把「敢说」变文化。",
    },
    {
        "emoji": "🔄", "cat": "回顾会前建信任",
        "title": "首次回顾会前建信任·团队契约+示弱建模",
        "val": "回顾会(retrospective)需要脆弱(认错/吐槽/批评流程/异议)，没信任人们就表演同意。信任要在「第一次回顾会前几周」就建，而非会上。四周法：W1-2 基础——①互相认识(coffee chat/午餐/About Me/工作风格讨论)②共享工作偏好(沟通异步/同步、专注时段、反馈直/婉、冲突直面/需冷却)③共创团队契约(我们假设善意/直接对话/兑现承诺/准时/可说「不知道」并公示)；W3-4 建模——④领导先示弱(公开认错/承认不知/公开求助/认发展区)⑤善意回应脆弱(有人认错说「谢谢提出，学到什么」而非「怎么发生的」)⑥对承诺闭环。首会读「首要指令」(无论发现什么，我们都信彼此已尽所能)，并明确保密(谈行动与主题不谈谁说)。",
        "inner": "经理在首次回顾会前 2-4 周建信任——coffee chat+工作偏好共享+共创团队契约(假设善意/直接/兑现/可说不知)；领导先示弱并善意回应；首会读「首要指令」+明保密。",
        "url": "https://www.retroflow.org/blog/post/building-trust-retrospective",
        "display": "retroflow.org/.../building-trust-retrospective",
        "note": "适用：② 经理在首次回顾会前建信任——团队契约+工作偏好共享+领导示弱建模，让回顾会真有诚实反馈而非表演同意。",
    },
    {
        "emoji": "💡", "cat": "脆弱信任",
        "title": "脆弱信任+Edmondson 七问测评·团队信任加速器",
        "val": "情绪智力领导建信任更快更持久，因同时照顾认知与情感双维。心理安全感(哈佛 Amy Edmondson 1999)是团队人际风险安全的共享信念——高心理安全团队敢于认错、直接挑战、vigorous 辩论，且都在相互尊重与共同目标框架内。Edmondson 原版七陈述测评(1-7 分个人评再团队讨论：犯错不被记恨/能提问题与难题/不因差异被拒/在此冒险安全/易求助/无人蓄意使绊/独特才干被用)；比较个人分差最大的处。Lencioni 区分「预测信任(靠谱)」与「脆弱信任(不怕弱点被利用)」——后者更难更强大，需敢说「我错了/需要帮/不懂/抱歉」。个人史练习(改编 Lencioni，30-45min)：每人答三问(哪长大童年如何/成长中最难或最重要的挑战/在团队最大优势与待发展区)，无插话只澄清。领导定调——有人先示弱，他人才敢。",
        "inner": "经理用 Edmondson 七陈述测评团队心理安全(个人评再比分歧最大处)；用 Lencioni 个人史练习(三问:童年/最大挑战/优势与待发展)建脆弱信任；领导先说「我错了/需要帮」给团队许可。",
        "url": "https://winwithmotivation.com/build-trust-team-high-performing",
        "display": "winwithmotivation.com/.../build-trust-team-high-performing",
        "note": "适用：② 经理用 Edmondson 七问测评+ Lencioni 个人史练习建脆弱信任——领导先示弱给他人许可，心理安全可度量可追踪。",
    },
]

def card_html(c, rel_class, rel_label, src_class, src_label):
    return (
        '    <div class="hl">\n'
        '      <div class="top"><span class="emoji">{e}</span><h3>{t}</h3>'
        '<span class="cat">{cat}</span><span class="badge {rc}">{rl}</span>'
        '<span class="badge {sc}">{sl}</span></div>\n'
        '      <p class="val">{v}</p>\n'
        '      <details class="exec"><summary>怎么做</summary><div class="inner">{i}</div></details>\n'
        '      <div class="src">🔗 <a href="{u}" target="_blank">{d}</a></div>\n'
        '      <div class="note">{n}</div>\n'
        '    </div>\n'
    ).format(e=c["emoji"], t=c["title"], cat=c["cat"], rc=rel_class, rl=rel_label,
             sc=src_class, sl=src_label, v=c["val"], i=c["inner"], u=c["url"],
             d=c["display"], n=c["note"])

# build blocks
exec_block = "".join(card_html(c, "r3", "高管间", "b2", "二手") for c in cards_exec)
sup_block = "".join(card_html(c, "r2", "上下级", "b1" if c["url"].startswith("https://www.atlassian") else "b2",
                               "一手" if c["url"].startswith("https://www.atlassian") else "二手") for c in cards_sup)

# ---------- update HTML ----------
with io.open(HTML, encoding="utf-8") as f:
    html = f.read()

# insert ③ before the ② section comment
marker_exec = '  <!-- ============ ② 上下级 ============ -->'
assert marker_exec in html, "exec marker not found"
html = html.replace(marker_exec, exec_block + "\n" + marker_exec, 1)

# insert ② before footer
marker_sup = '  <footer>'
assert marker_sup in html, "footer marker not found"
html = html.replace(marker_sup, sup_block + "\n" + marker_sup, 1)

# update hero subtitle
import re
html = re.sub(r'采集于 2026-08-09 ｜ 五轮补采 \+8（08:43）｜ 六维评估（含关系适配度）｜ 一手/二手标注 ｜ 历史去重 ｜ 受众关系分层（仅②上下级 / ③高管间）',
              '采集于 2026-08-10 ｜ 六轮补采 +9（03:06）｜ 六维评估（含关系适配度）｜ 一手/二手标注 ｜ 历史去重 ｜ 受众关系分层（仅②上下级 / ③高管间）', html, 1)

# update section counts
html = html.replace('<span class="tag">9 卡</span>', '<span class="tag">12 卡</span>', 1)
html = html.replace('<span class="tag">26 卡</span>', '<span class="tag">32 卡</span>', 1)

with io.open(HTML, "w", encoding="utf-8") as f:
    f.write(html)
print("HTML updated. New ③=12, ②=32, total=44")

# ---------- update index.json ----------
with io.open(IDX, encoding="utf-8") as f:
    data = json.load(f)

def norm(s):
    return "".join(ch for ch in s.lower() if ch.isalnum())

new_entries = []
for c in cards_exec:
    new_entries.append({
        "title": c["title"], "normKey": norm(c["title"]), "url": c["url"],
        "sourceType": "secondary", "relation": "exec", "summary": c["val"][:80]
    })
for c in cards_sup:
    st = "primary" if c["url"].startswith("https://www.atlassian") else "secondary"
    new_entries.append({
        "title": c["title"], "normKey": norm(c["title"]), "url": c["url"],
        "sourceType": st, "relation": "supervisor", "summary": c["val"][:80]
    })

data.extend(new_entries)
with io.open(IDX, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("index.json updated. total entries:", len(data), "+", len(new_entries))
