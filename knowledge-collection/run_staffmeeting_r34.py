# -*- coding: utf-8 -*-
import re, json, shutil, os

BASE = os.path.dirname(os.path.abspath(__file__))
THEME = 'staff-meeting'
WALL = os.path.join(BASE, THEME, THEME + '.html')
INC  = os.path.join(BASE, THEME, 'staff-meeting-20260903.html')
IDX  = os.path.join(BASE, 'index.json')
NOTE = r'C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\staff-meeting\员工大会-知识卡汇总.md'
ZIDX = r'C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md'
MAP  = os.path.join(BASE, 'lexiang-entry-map.json')
LAST = os.path.join(BASE, '..', 'last-topic.txt')

DATE = '2026-09-03'
ROUND = 34
ROUND_CN = '三十二轮'

# -------- 12 张新卡（仅 ②上下级 / ③高管间，0 peer）--------
cards = [
 {
  "emoji":"🆕","rel":"exec","src":"secondary","cat":"新任领导首秀",
  "title":"新任领导首次全员会·10 步准备法（二手）",
  "url":"https://www.graphic.com.gh/business/business-news/how-to-prepare-for-your-first-town-hall-meeting.html",
  "val":"新领导首次 town hall 不是秀修辞而是「定模式」：员工在听信号（懂不懂这家公司/值不值得信/难时不躲/讲人话还是喊口号）而非听口才。10 步：①定一个离场要带走的故事主线 ②庆祝团队既往成绩建立信任 ③描绘共同未来（别个人化）④讲清上任后已做的动作及为何 ⑤说明人人如何参与 ⑥明确邀请「我需要你」⑦说明对达标/不达标者的不同回应 ⑧按价值观划红线 ⑨开放提问（无即时答案就承诺回复）⑩以祝愿与能量收尾。核心：首秀建立的是「以后怎么相处」的信任基线。",
  "howto":"新领导上任首场全员会，先做「听信号」而非「表演」——开场具体感谢既有团队成绩、坦诚点名当前真实挑战、给出前 90 天倾听期承诺（小范围座谈+不擅自大改）；把「我不会拆掉你们建的，我是因它而来」这句放慢说，能瞬间让全场肩膀放下；留足匿名提问+当场承诺跟进。",
  "note":"适用：高管间 — 新任 CEO/领导首次全员会 10 步准备（定主线/庆祝既往/描绘未来/划红线/开放提问），首秀建信任基线而非秀口才。"
 },
 {
  "emoji":"🎯","rel":"exec","src":"secondary","cat":"新任领导首秀",
  "title":"新 CEO 首次全员会·该做与不该做（二手）",
  "url":"https://www.ivolver.be/post/the-art-of-the-first-all-hands-meeting-what-to-do-and-what-not-to-do-in-your-first-address",
  "val":"首场全员会的价值在「可信」不在「惊艳」。有效做法：谦逊（承认还不全懂）、讲清起步聚焦（前几周聊什么/听什么）、坦诚点名张力（市场变/不确定性）、露出领导风格（靠说而非自夸）。三坑：①过度承诺（几个月后被迫修正伤信任）②太抽象（满篇使命愿景无可抓手）③表演权威（装「总统一贯」僵硬不自然）。首秀是 100 天沟通的起点，要用小范围座谈/Q&A/跟进信延续，一场演讲造不出连接。",
  "howto":"新 CEO 首秀写稿/演讲时，删掉宏大战略全图与确定感表演；用「我还不知道答案，但前 90 天会问」替代过度承诺；把真实紧张说破（「这对我也是大时刻」）比完美魅力更破防；会后立刻排小范围座谈延续关系，别靠一场演讲封神。",
  "note":"适用：高管间 — 新 CEO 首场全员会「可信>惊艳」：谦逊/坦诚命名挑战/露风格，避过度承诺与表演权威。"
 },
 {
  "emoji":"🗣️","rel":"exec","src":"secondary","cat":"新任领导首秀",
  "title":"新 CEO 首秀致辞·感恩→坦诚→好奇→向前四段弧（二手）",
  "url":"https://pulserevops.com/knowledge/sp0078",
  "val":"最强首秀遵循清晰情绪弧：①感恩与认可过去（具体点名公司既有成就，表明「我来是因为它而非拆它」，直接压住「新官会推倒重来」的隐性恐惧）②坦诚当下（点名一个真挑战：市场位移/产品缺口/艰难年，跳过这步整篇像新闻稿）③好奇与倾听（承诺前 90 天倾听期：小范围座谈+不擅作重大决定）④向前（开放邀请「一起想下一章」，避开「我全有答案」陷阱）。3-5 分钟/400-600 字为宜，避行话与硬承诺。",
  "howto":"新领导首秀致辞按「感恩→坦诚→好奇→向前」四段写：开场用具体既有成就表达尊重（降防御）；中段命名房间里的大象（变化可怕/有人兴奋有人慌）再转到真挑战；收尾用一句安静笃定的邀请而非口号。全程避「我们是一家人」等空话与体育比喻，稳住眼神/镜头、该停顿处停顿。",
  "note":"适用：高管间 — 新 CEO 首秀致辞四段情绪弧（感恩既有/坦诚挑战/90天倾听/向前邀请），简短克制显尊重。"
 },
 {
  "emoji":"🎬","rel":"exec","src":"secondary","cat":"全员会制作",
  "title":"CEO 全员会·制作清单+成功指标+风险阈值（二手）",
  "url":"https://www.everywow.ch/en/2026/05/how-to-run-a-ceo-town-hall",
  "val":"CEO town hall 成败可预测：常见坑=烂技术/话太多/满篇术语/假互动/无跟进/用错场景。清单：①定单一沟通目标 ②确认 town hall 是正确形式 ③锁受众/目标/形式/语言/Q&A 模型 ④写带时限的 run of show ⑤用大白话 brief CEO（非 slide 顺序）⑥备好三个最难问题的答案 ⑦测音/屏/光/网与备份 ⑧分派主持/制作/Q&A 控场/讲者支持角色 ⑨告知员工为何重要+提问机制 ⑩定录制后共享内容 ⑪会前审字幕/逐字稿/管理者跟进 ⑫会前定成功指标。指标看现场观看时长、回放使用、提问量、未答主题、管理者是否还要重讲。时长通常 30-45 分钟。",
  "howto":"办 CEO 全员会，先做「制作清单」而非只写稿：分派明确的制作人/主持人/Q&A 控场三角色；会前彩排音频灯光、备好三个最难问题的答案；决定录制后发什么（审过字幕+逐字稿+管理者级联包）；用「现场观看时长+提问量+未答主题」三指标会前定基线，别只看出席人数。",
  "note":"适用：高管间 — CEO 全员会制作清单（角色分派/彩排/最难问题备答/会后共享/成功指标），技术翻车比内容更伤信任。"
 },
 {
  "emoji":"🔄","rel":"exec","src":"secondary","cat":"反向倾听",
  "title":"反向全员会·员工讲、领导听（二手）",
  "url":"https://www.squareoneky.com/post/leadership-are-you-listening-the-case-for-a-reverse-town-hall-this-summer",
  "val":"反向 town hall：翻转常态——不是领导站前台讲战略、末尾收问，而是员工讲、领导听。做法：每季度 4 次、每次 90-120 分钟，各部门员工每人提 2-3 个想法（非正式提案），筛若干上台每人 10 分钟讲「看到什么/觉得什么可行/为何」，领导只问、只记、不反驳不纠正——分析留到会后。价值：打破「一线洞察经层层过滤被磨平」的结构性失真，让 Cabinet 听到漏斗底的真问题（某项目退率真相、被绕开的流程 workaround、家长真实疑问）。最难的不是流程是领导忍住不现场辩解。",
  "howto":"想听一线真声音，把全员会翻转成「反向」：每季度半天，员工提想法、选人上台讲、高管只听只记不反驳；会前给员工准备时间、会后做分析再回应；关键是领导忍住不现场「为什么不行/试过」。适合战略卡壳、想听前线洞察时，比常规 town hall 挖得深。",
  "note":"适用：高管间 — 反向全员会（员工讲/领导听/不现场反驳），打破层层过滤失真、听漏斗底真问题。"
 },
 {
  "emoji":"💬","rel":"exec","src":"secondary","cat":"AMA开放论坛",
  "title":"高管 AMA·内部沟通开放论坛操作法（二手）",
  "url":"https://tchop.io/resources/glossary/internal-communication/ask-me-anything-(ama)",
  "val":"AMA=员工实时/异步向领导提问的开放论坛，是 town hall 的进化形态。类型：领导 AMA（直连高管答战略/政策/变革）、团队 AMA、项目 AMA、匿名 AMA。运行法：①定目的 ②选平台（Zoom/Teams/Slido/匿名工具）③多渠道邀参与（提前+现场收问）④立规则（建设性尊重）⑤给领导看已收问题备答 ⑥会后发摘要+行动项+未答跟进。最佳实践：定期化显承诺、鼓励参与、透明与审慎平衡（难问题诚实答但不泄密）、跨层级/地区/时区包容、会后问卷追踪。避坑：参与低（推匿名）、躲难问题（毁信任）、时间不够（承诺跟进）、过度使用致疲劳。",
  "howto":"把高管 AMA 当「定期而非一次性」的信任机制：会前多渠道收匿名问+给领导看问题备答；现场由中立主持控场、对难问题诚实答（「还没定，但我们这么想」）；会后 24h 内发摘要+行动项+未答跟进；用会后问卷看有效性，避「只答软球」与频次过高疲劳。",
  "note":"适用：高管间 — 高管 AMA 内部开放论坛（类型/运行法/最佳实践），定期+匿名+诚实答难问才是真透明。"
 },
 {
  "emoji":"📌","rel":"exec","src":"secondary","cat":"AMA案例",
  "title":"Pinterest 高管 AMA·Slido 投票+难问题公开上升（二手）",
  "url":"https://www.ragan.com?p=341152/",
  "val":"Pinterest（5265 人）用 Slido 做高管 AMA：上一场结束即开提交窗、会前一周关窗，员工投票、最高赞问题进现场；因平台公开，连难/争议问题都过滤不掉——CEO Bill Ready 坚持正面答（「不答只会积累挑战」）。每场约答 10 问（提交 20-50）；VP 级内部主持加语境；通讯团队现场记要、需跟进的会后闭环。频次从「每季度随全员会 1 次」升到「每季度 2 次」（独立 1+全员会内 1），因响应好、提问频。全球 24 个办公室尽量就地办、直播录播覆盖远程。",
  "howto":"学 Pinterest 把高管 AMA 做成「公开投票+难问题不躲」的机制：用 Slido 开长提交窗、员工 upvote、最高赞必答（含争议题）；VP 级内部主持加语境、通讯团队现场记要并闭环未答；频次随提问量上调；远程优先用直播+录播+就地办覆盖多地。",
  "note":"适用：高管间 — Pinterest 高管 AMA 实操（Slido 投票上升/难问题公开答/VP 主持/会后闭环），响应好即提频。"
 },
 {
  "emoji":"🤖","rel":"supervisor","src":"secondary","cat":"AI会后沉淀",
  "title":"AI 转写全员会·10 行摘要+Q&A 问答集工作流（二手）",
  "url":"https://vocap.io/en/blog/transcribe-all-hands-town-halls-ai",
  "val":"全员会最被低估的是 Q&A（信息密度最高却最没文档化）。AI 工作流：①录制（远程开原生录制；现场用台麦/手机近讲台，Q&A 也录清、PA 复读问题）②AI 转写（Whisper 类，别依赖平台自动字幕——数字/专名/快问快答会翻车）③生成 10 行高管摘要+公告决策（谁受影响/从何时）+指标+里程碑 ④从 Q&A 抽 FAQ（每问配逐字答、按主题分组、标未答待跟进）⑤当天发摘要+FAQ 到内部渠道、全逐字稿挂底作底稿。落地格式=短可扫：10 行摘要+带「影响谁」的公告+Q&A FAQ，全稿作 source of truth。",
  "howto":"全员会别只靠人记——录完用 AI 转写（避开平台自动字幕对数字/专名的翻车），让 AI 出「10 行摘要+公告(谁受影响/从何时)+Q&A FAQ」；Q&A 抽每问逐字答、把「我们回头」的未答单列给领导书面跟进；当天发内部群、全逐字稿挂 wiki 累积成可搜历史。",
  "note":"适用：上下级 — AI 转写全员会工作流（录制→转写→10行摘要+Q&A FAQ→当天发），Q&A 变资产而非遗失。"
 },
 {
  "emoji":"🌐","rel":"supervisor","src":"secondary","cat":"AI会后沉淀",
  "title":"多语全员会·同日多语纪要（AI 一稿多译）（二手）",
  "url":"https://www.oakmeeting.ai/learn-bilingual-town-halls.html",
  "val":"跨国全员会（如粤语+英语+普通话三语）常态痛点：多语纪要手写一下午，干脆跳过，未到场同事零信息。解法：一份转写覆盖所有语种→生成结构化摘要→翻译成各受众语→路由到对应渠道；人只需短审。单稿可译 99+ 语，让粤语高管、英语工程、普通话区域各得能读能用的纪要。纪要内容宜高 level：3-5 主题+关键公告+领导 Q&A+分团队行动项+下次会议议程，避逐字细节。",
  "howto":"办多语/跨国全员会，别手写多份纪要——一份转写→AI 摘要→按受众语翻译分发，通讯只需短审；纪要锁定「3-5 主题+公告+Q&A+分团队行动项+下次会议议程」模板，避免逐字；让不同语种同事同日拿到能用的版本，消除「没参会的啥也没有」。",
  "note":"适用：上下级 — 多语全员会同日多语纪要（一稿多译+短审），消除跨国/跨语同事信息差。"
 },
 {
  "emoji":"🎥","rel":"supervisor","src":"secondary","cat":"混合参会",
  "title":"混合全员会·双主持+远程平权玩法手册（二手）",
  "url":"https://dailypick.dev/blog/hybrid-all-hands-playbook-fair-fun-agendas-that-keep-teams-engaged",
  "val":"混合全员会最易变成「总部鼓掌、远程静音回邮件」。玩法：①会前工程平权——发「本月 exec 该回应什么」预调研、用决策轮抽匿名建议定议程、设「远程+现场」双 MC 分 script 交接、测房间摄像头跟人/远程可见观众/双方可见 chat、发 pre-read；②议程呼吸感——欢迎(远程 MC 用轮盘抽「第一句」感谢)→业务状态(10min+实时字幕+共享 Q&A 文档)→客户故事(轮流转讲述者)→职能快闪(10min)→互动 break(7min：远程vs现场答题赛/两真一假)→直播 Q&A(8min：Slido 收问+轮盘在远程/现场队列间公平切)→收尾仪式(5min)；③参与零门槛——反应 bingo 卡/聊天 hype 小队/白板快照上云；④Q&A 远程音量大——双列「远程/现场」问题都上大屏、轮盘公平选、匿名提交、24h 书面答；⑤会后延续——2 天内 retro 选 1 改进、剪 120 秒高光发 Slack、开帖续问。",
  "howto":"混合全员会按「远程与现场平等」设计：设远程+现场双 MC 各管一摊、用匿名预调研/决策轮定议程；Q&A 双列问题都上屏、轮盘在两边公平切、匿名可投；互动 break 用远程vs现场小竞赛破静音；会后剪高光+开续问题帖。核心信号：远程提问优先被读、被记名。",
  "note":"适用：上下级 — 混合全员会双主持+远程平权玩法（双MC/双列Q&A/互动break/会后retro），远程不静音。"
 },
 {
  "emoji":"📋","rel":"supervisor","src":"secondary","cat":"议程设计",
  "title":"全员会 60 分钟议程模板·节奏稳内容新（二手）",
  "url":"https://super-intern.com/en/blog/2026-all-hands-meeting-guide",
  "val":"全员会节奏「形稳意新」：人知其节奏、被其内容惊喜。60 分钟模板：欢迎与战果(5min：点名新人+2-3 具体胜仗)→数据(10min：固定 3-5 指标同序同图、只讲趋势)→主故事(15min：本期一个主题，由最贴近的人讲非必 CEO)→演示/深潜(10min：团队秀真活)→Q&A(15min：先匿名预提交再现场、未答有主+书面跟)→收尾(5min：一句记住的+纪要录屏在哪)。原则：小公司高频短（周/双周 30min）、大公司纪律化（月/季 60-90）；保护 Q&A 占 ≥1/4 否则退回广播；指标段固定同图、故事在趋势；一个主故事非四个；轮转舞台（只高管讲强化等级）；匿名预收集问一举转 Q&A。",
  "howto":"全员会议程用「固定骨架+每期一主故事」：开场点名具体胜仗（非「感谢平台组」空话）、数据段永远同指标同图只讲趋势、主故事给最贴近的人讲、Q&A 占 ≥1/4 且先匿名预提交；保护节奏——某段超时就砍或转书面；轮转舞台让不同团队上讲台破「同一批高管」。",
  "note":"适用：上下级 — 全员会 60 分钟议程模板（欢迎战果/固定数据/一主故事/匿名Q&A/收尾），形稳意新+保护Q&A。"
 },
 {
  "emoji":"📊","rel":"supervisor","src":"secondary","cat":"效果度量",
  "title":"全员会后调研·3-5 题脉冲+专属题库（二手）",
  "url":"https://surveymars.com/blog/post-meeting-survey-questions",
  "val":"全员会/ town hall 属「必调研」场景（每场都该收）。脉冲格式 3-5 题、<90 秒、响应率 70%+：P1「这会是好时间投资吗」(1-5) 周环比成会议健康 KPI，连跌两周低于 3.5/5 即开复盘；P2「是否有清晰行动项与负责人」(Y/N)；P3「下次改什么」(开放)。全员会专属题库：战略清晰度/领导更新是否激励/高管是否答了最关心的问/材料是否好读/是否敢参与现场 Q&A/下场该多讲什么。公司规律反馈可降 25-40% 不必要会议时长。关键：持续追、据改、让员工见其声被听。",
  "howto":"把全员会调研做成「脉冲」而非长卷：每场结束发 3-5 题(<90秒)，核心一题「这是好时间投资吗」周环比追趋势；专属题覆盖战略清晰度/领导可信/高管是否答了最关心问；响应率掉或分数连跌两周就开复盘；调研后据改并回贴，让员工见「声音被听」才闭环。",
  "note":"适用：上下级 — 全员会后脉冲调研（3-5题/周环比健康KPI/专属题库），持续追+据改才闭环。"
 },
]

assert len(cards) == 12, len(cards)
N_exec = sum(1 for c in cards if c['rel']=='exec')
N_sup  = sum(1 for c in cards if c['rel']=='supervisor')
print(f"cards=12 exec={N_exec} sup={N_sup}")

# -------- HTML 卡片块生成 --------
def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def block(c):
    rel_badge = '<span class="badge r3">高管间</span>' if c['rel']=='exec' else '<span class="badge r2">上下级</span>'
    src_badge = '<span class="badge b1">一手</span>' if c['src']=='primary' else '<span class="badge b2">二手</span>'
    return (f'<div class="hl">\n'
            f'      <div class="top"><span class="emoji">{c["emoji"]}</span><h3>{esc(c["title"])}</h3>'
            f'<span class="cat">{esc(c["cat"])}</span>{rel_badge}{src_badge}</div>\n'
            f'      <p class="val">{esc(c["val"])}</p>\n'
            f'      <details class="exec"><summary>怎么做</summary><div class="inner">{esc(c["howto"])}</div></details>\n'
            f'      <div class="src">🔗 <a href="{esc(c["url"])}" target="_blank">{esc(c["url"])}</a></div>\n'
            f'      <div class="note">{esc(c["note"])}</div>\n'
            f'    </div>')

exec_blocks = ''.join(block(c) for c in cards if c['rel']=='exec')
sup_blocks  = ''.join(block(c) for c in cards if c['rel']=='supervisor')

# -------- 增量页 --------
STYLE = '''<style>
:root{
  --bg:#f4f6fb; --card:#ffffff; --ink:#1f2430; --sub:#5b6478;
  --accent:#6c5ce7; --accent2:#00b8d9; --chip:#eef0ff;
}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:linear-gradient(135deg,#eef1ff 0%,#e6f7ff 100%);color:var(--ink);padding:28px 18px;line-height:1.6;}
.wrap{max-width:1080px;margin:0 auto;}
.hero{background:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);border-radius:22px;padding:30px 32px;color:#fff;box-shadow:0 14px 40px rgba(108,92,231,.25);margin-bottom:22px;}
.hero h1{font-size:28px;font-weight:800;letter-spacing:1px;margin-bottom:8px;}
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
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;}
.hl{background:var(--card);border-radius:18px;padding:18px 18px 16px;border-top:4px solid var(--accent);box-shadow:0 10px 32px rgba(108,92,231,.10);display:flex;flex-direction:column;gap:9px;}
.top{display:flex;align-items:center;gap:8px;flex-wrap:wrap;}
.emoji{font-size:22px;}
.hl h3{font-size:16px;font-weight:700;flex:1;min-width:120px;}
.cat{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:600;background:var(--chip);color:var(--accent);}
.badge{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:700;}
.b2{background:#fff1e6;color:#c0651a;}
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
</style>'''

INC_HTML = (f'<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n<meta charset="UTF-8">\n'
           f'<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
           f'<title>员工大会 · 知识采集卡片墙</title>\n{STYLE}\n</head><body>\n<div class="wrap">\n'
           f'  <div class="hero">\n    <h1>🎤 员工大会 · {ROUND_CN}增量卡片（{DATE}）</h1>\n'
           f'    <p>本轮新增 12 张（③高管间 {N_exec} ＋ ②上下级 {N_sup}）｜ 六维评估（含关系适配度）｜ 一手/二手标注 ｜ 受众关系分层（仅②上下级 / ③高管间，已剔除平级/朋友向）</p>\n'
           f'    <div class="relbar">\n      <span>② 领导↔员工（上下级，supervisor）</span>\n      <span>③ 领导↔领导（高管间，exec）</span>\n    </div>\n  </div>\n'
           f'  <div class="sec sec3">\n    <h2>③ 领导↔领导（高管间 · exec）</h2>\n    <span class="tag">{N_exec} 卡</span>\n  </div>\n  <div class="grid">\n'
           f'{exec_blocks}  </div>\n'
           f'  <div class="sec sec2">\n    <h2>② 领导↔员工（上下级，supervisor）</h2>\n    <span class="tag">{N_sup} 卡</span>\n  </div>\n  <div class="grid">\n'
           f'{sup_blocks}  </div>\n'
           f'  <footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>\n</div>\n</body>')
open(INC,'w',encoding='utf-8').write(INC_HTML)
print(f"INCREMENT page written: {INC} ({len(INC_HTML)} bytes, exec={INC_HTML.count('badge r3')}, sup={INC_HTML.count('badge r2')})")

# -------- 汇总墙注入 --------
wall = open(WALL, encoding='utf-8').read()
wall_bak = WALL + '.bak-r34'
shutil.copy2(WALL, wall_bak)

assert wall.count('class="hl"') == 336, f"wall hl={wall.count('class=\"hl\"')}"
assert wall.count('badge r3') == 113, f"r3={wall.count('badge r3')}"
assert wall.count('badge r2') == 223, f"r2={wall.count('badge r2')}"

EXEC_ANCHOR = '</div>\n    </div></div>\n  <div class="sec sec2">'
SUP_ANCHOR  = '</div>\n    </div></div>\n<footer>'
assert wall.count(EXEC_ANCHOR) == 1, f"EXEC_ANCHOR={wall.count(EXEC_ANCHOR)}"
assert wall.count(SUP_ANCHOR) == 1, f"SUP_ANCHOR={wall.count(SUP_ANCHOR)}"

wall = wall.replace(EXEC_ANCHOR, EXEC_ANCHOR.replace('</div>\n  <div class="sec sec2">', exec_blocks + '</div>\n  <div class="sec sec2">'), 1)
wall = wall.replace(SUP_ANCHOR, SUP_ANCHOR.replace('</div>\n<footer>', sup_blocks + '</div>\n<footer>'), 1)

assert wall.count('采集于 2026-09-02（第三十一轮 +13）') == 1
wall = wall.replace('采集于 2026-09-02（第三十一轮 +13）', f'采集于 {DATE}（{ROUND_CN} +12）', 1)
assert wall.count('<span class="tag">113 卡</span>') == 1
wall = wall.replace('<span class="tag">113 卡</span>', '<span class="tag">120 卡</span>', 1)
assert wall.count('<span class="tag">223 卡</span>') == 1
wall = wall.replace('<span class="tag">223 卡</span>', '<span class="tag">228 卡</span>', 1)
assert wall.count('href="staff-meeting-20260902.html"') == 1
wall = wall.replace('href="staff-meeting-20260902.html"', 'href="staff-meeting-20260903.html"', 1)

assert wall.count('class="hl"') == 348, f"wall hl={wall.count('class=\"hl\"')}"
assert wall.count('badge r3') == 120, f"r3={wall.count('badge r3')}"
assert wall.count('badge r2') == 228, f"r2={wall.count('badge r2')}"
assert '📌 本页由 yitong 沉淀整理' in wall
open(WALL,'w',encoding='utf-8').write(wall)
print(f"WALL updated -> {wall.count('class=\"hl\"')} cards (r3={wall.count('badge r3')}, r2={wall.count('badge r2')})")

# -------- index.json --------
idx = json.load(open(IDX, encoding='utf-8'))
def normKey(t): return re.sub(r'[\s（）()「」“”"，。、：；·\-—’‘]', '', t)
before = len([e for e in idx if e.get('topic')=='staff-meeting'])
for c in cards:
    idx.append({
        "title": c['title'],
        "normKey": normKey(c['title']),
        "url": c['url'],
        "sourceType": c['src'],
        "relation": c['rel'],
        "summary": re.sub(r'\s+',' ', c['val'])[:160],
        "topic": "staff-meeting"
    })
json.dump(idx, open(IDX,'w',encoding='utf-8'), ensure_ascii=False, indent=2)
after = len([e for e in idx if e.get('topic')=='staff-meeting'])
print(f"index.json staff-meeting: {before} -> {after} (+{after-before})")

# -------- vault 笔记 --------
note = open(NOTE, encoding='utf-8').read()
rel_label = {'exec':'③高管间','supervisor':'②上下级'}
src_label = {'primary':'一手','secondary':'二手'}
rows = '\n'.join(f"| {c['title']} | {rel_label[c['rel']]} | {src_label[c['src']]} |" for c in cards)
section = f"\n## 轮次 {DATE}（+12）\n\n| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n{rows}\n"
note = note.rstrip() + section
open(NOTE,'w',encoding='utf-8').write(note)
print("vault note: appended ## 轮次", DATE, "(+12)")

# -------- 00-索引 --------
z = open(ZIDX, encoding='utf-8').read()
assert z.count('**336 卡**') == 1, f"336 卡 count={z.count('**336 卡**')}"
z = z.replace('**336 卡**', '**348 卡**', 1)
def oneliner(c):
    n = re.sub(r'^适用[：:]\s*','', c['note'])
    n = re.sub(r'^[③②]?[一-龥A-Za-z]+?\s*[—–-]\s*','', n)
    n = re.sub(r'\s+',' ', n).strip()
    return n[:46] + ('…' if len(n) > 46 else '')
score = lambda c: 5 if (c['src']=='primary' or c['rel']=='exec') else 4
zrows = '\n'.join(
    f"| {c['title']}（staff-meeting.html） | {score(c)} | {src_label[c['src']]} | {rel_label[c['rel']]} | {oneliner(c)} |"
    for c in cards)
msec = re.search(r'^## 主题：员工大会.*$', z, re.M)
assert msec, "staff-meeting header not found"
sec = z[msec.start():]
last_row = None
for mm in re.finditer(r'^\| .*staff-meeting\.html.* \|$', sec, re.M):
    last_row = mm
assert last_row is not None
ins_pos = msec.start() + last_row.end()
z = z[:ins_pos] + '\n' + zrows + z[ins_pos:]
# header history 追加
seg = ('｜ ' + DATE + ' ' + ROUND_CN + '补采 +12（新任领导首秀10步/新CEO首秀该做不该做/新CEO四段弧/CEO全员会制作清单/反向全员会/高管AMA操作法/Pinterest AMA案例/AI转写Q&A工作流/多语同日纪要/混合双主持玩法/60分钟议程模板/会后脉冲调研）')
z = z[:msec.end()-1] + seg + z[msec.end()-1:]
open(ZIDX,'w',encoding='utf-8').write(z)
print("00-index: +12 rows, 336->348, header history appended")

# -------- lexiang-entry-map pending round --------
mp = json.load(open(MAP, encoding='utf-8'))
mp['staff-meeting']['rounds'].append({
    "date": DATE,
    "entry_id": None,
    "name": "staff-meeting-20260903",
    "note": f"R{ROUND} 增量页（乐享 token 401，待重连后补传）"
})
json.dump(mp, open(MAP,'w',encoding='utf-8'), ensure_ascii=False, indent=2)
print("lexiang-entry-map: appended pending R%d round (entry_id=null)" % ROUND)

# -------- last-topic.txt -> Offsite --------
open(LAST,'w',encoding='utf-8').write('Offsite\n')
print("last-topic.txt -> Offsite")

print("\nDONE. backup wall at", wall_bak)
