# -*- coding: utf-8 -*-
"""员工大会 第二十一轮补采（r21, 2026-08-21）：渲染新卡 + 累计墙 + index.json + 临时卡文件。"""
import json, re, os

BASE = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(BASE, 'staff-meeting', 'staff-meeting.html')
TMP = os.path.join(BASE, 'staff-meeting', '.run_newcards.tmp.html')
IDX = os.path.join(BASE, 'index.json')
TOPIC = 'staff-meeting'
ROUND = 21
DATE = '2026-08-21'

CARDS = [
 {"emoji":"📆","title":"CEO Town Hall 半天时间线模板（含避坑）","cat":"CEO议程","rel":"exec","src":"secondary",
  "val":"半日制 CEO Town Hall 时间表：战略演讲+Q&A+分组工作坊+综合汇报，5 小时运营足迹；含 6 大常见错误（塞爆 deck / 把 Q&A 当点缀 / 忽略转场缓冲 / 忽视远程与混合 / 不培训 breakout rapporteur / 会后无茶歇 networking）；硬性：提前 4-6 周规划、提问通道提前 1-2 周开、Q&A ≥45min、会后 5-7 天发执行 FAQ 备忘录。强调预提交+匿名数字投票最大化透明。",
  "howto":"高层全员会严格套时间表：CEO 主旨讲完留 ≥45min Q&A；breakout 配受训 moderator 防单一声音主导；会前开匿名提问通道；会后 1 周内发正式跟进备忘录（含未答问题 FAQ），别让反馈无下文。",
  "url":"https://chronolio.com/templates/ceo-town-hall-meeting",
  "disp":"chronolio.com/templates/ceo-town-hall-meeting",
  "note":"适用：③ 高管主导半天制全员会（含工作坊+跟进闭环）的时间线与避坑清单。"},
 {"emoji":"⚠️","title":"摧毁士气的全员会·5 大信任杀手（反例）","cat":"信任避坑","rel":"exec","src":"secondary",
  "val":"咨询案例：CEO 讲「新方向」12 分钟，200 人当场更新简历，季度内 14 人离职——内容没错，是「讲法」毁了信任。5 大错误：①用企业话术而非人的承认开场 ②回避人人皆知的大象 ③灌水不尊重时间 ④表演而非沟通 ⑤把 Q&A 当威胁。修复结构：先承认现实→给实质非包装→尊重智商→真对话。会前 4 问信任自检。",
  "howto":"上台先点「房间里的大象」（前 60-90 秒）；把「我很兴奋宣布」换成「我知道大家有不确定，今天正面讲」；能砍 30% 就砍；Q&A 别筛问题（员工知道）；用「困难问题先答」建立可信。",
  "url":"https://winningpresentations.com/all-hands-meeting-presentation-mistakes",
  "disp":"winningpresentations.com/all-hands-meeting-presentation-mistakes",
  "note":"适用：③ 高管/CEO 全员会讲话的「反向教材」，重点在信任与开场承认。"},
 {"emoji":"🎙️","title":"Town Hall 演讲不掉线·答问与收尾","cat":"演讲技巧","rel":"exec","src":"secondary",
  "val":"注意力在「未脚本回答」处被检验——员工更信临场答问而非背稿。答问三式：清晰复读问题→直接答再补上下文→没 full answer 就诚实认半截（比含糊自信更建信任）；多问题按主题归并。收尾只答一问「员工带走什么」：一个优先级+一个焦点+一个 checkpoint。避坑：只有数据无意义/领导介绍太长/重复旧更新/无收尾/与员工无关。",
  "howto":"答尖锐问题前先复读让全场听到；不会全答就给「部分诚实答案」；结尾用一句话收口（下一步 60 天聚焦 X）；部门级更新只在影响多团队时才讲，别念孤岛报告。",
  "url":"https://www.airmeet.com/hub?p=124003",
  "disp":"airmeet.com/hub?p=124003",
  "note":"适用：③ 高管 Town Hall 演讲的注意力管理与答问收尾技巧。"},
 {"emoji":"📝","title":"大会致辞高分攻略·三层立意+万能模板","cat":"致辞写作","rel":"exec","src":"secondary",
  "val":"大笔杆子拆解优质致辞：三层立意（回望来路共情→立足当下点使命→奔赴新程提期许）；三段语言梯度（回顾写实带温情/动员对仗排比提气/寄语走心有远）；万能脉络：开篇致意→点题定调→回望成绩→提炼共识→析机遇挑战→分维提要求→号召收尾；升格金句按场景（岁月/征程/薪火 vs 实干/担当/破局 vs 初心/笃行/致远）。适配表彰/工作推进/青年座谈/年会。",
  "howto":"致辞按「三层立意」搭骨架：先共情全体付出（具象场景），再点时代使命，最后提期许号召；金句配具体工作场景别空堆；避「平铺无格局/平淡缺感染/只事务无升华」三短板。",
  "url":"https://m.toutiao.com/article/7652155390003577387",
  "disp":"toutiao.com/article/7652155390003577387",
  "note":"适用：③ 领导在员工大会/工作会的致辞写作框架与金句库。"},
 {"emoji":"🎤","title":"年度员工大会议话稿·金字塔叙事+情绪曲线","cat":"讲话稿","rel":"exec","src":"secondary",
  "val":"2026 专业版 CEO/总经理年会讲话：金字塔叙事（开场共情 2min→回顾成绩 4min→坦诚反思 3min→展望方向 4min→号召 4min，约 2500 字 17min）；情绪曲线设计（温暖→自豪→真诚下沉→激昂→温情收束）；5 类 12 个金句模板（开场定调/业绩回顾/挑战反思/战略展望/结尾号召），如「承认自己的__是__的开始」「下一站不是__而是__」。",
  "howto":"讲话按情绪曲线排布：反思段刻意降温让展望更有力；金句落在高温节点；避免只报喜——留一段坦诚不足建立信任；结尾从激昂回归温暖，让人带感动离场而非亢奋即忘。",
  "url":"https://m.renrendoc.com/paper/523869520.html",
  "disp":"renrendoc.com/paper/523869520.html",
  "note":"适用：③ 高管年度员工大会讲话稿结构、情绪曲线与金句工具箱。"},
 {"emoji":"✨","title":"2026 领导致辞终极指南·三种风格+万能结构","cat":"致辞写作","rel":"exec","src":"secondary",
  "val":"致辞三大范式转变：从「回顾成绩」到「定义意义」、从「展望目标」到「描绘画卷」、从「感谢付出」到「看见个体」（提具体团队/项目/凌晨三点的灯光）。三种人设：理性务实派（科技金融制造）/情怀共鸣派（文创教育消费）/鼓舞前瞻派（互联网创业转型）。万能结构：开场定调破冰(1-2min)→中篇回顾与感谢(3-5min,1主题词+2故事+N感谢)→结尾号召。",
  "howto":"先定「人设」再写稿：科技制造业走逻辑数据、文创走故事、创业公司走热血号召；回顾用「1 主题词+2 故事」承载，感谢点名具体细节；开场用场景化/共情式破冰，避「金虎辞旧」式套话。",
  "url":"https://www.szsgcm.com/content/?14983.html",
  "disp":"szsgcm.com/content/?14983.html",
  "note":"适用：③ 领导年会/员工大会致辞的风格选择与模块化写作。"},
 {"emoji":"🧭","title":"站高看远的领导发言提纲·万能结构+金句","cat":"发言提纲","rel":"exec","src":"secondary",
  "val":"万能发言提纲：开场定调(讲形势/目的/期待)→回顾成绩(进展/亮点/支撑)→查摆问题(卡点/深层因)→部署任务(方向/重点/措施/底线)→提要求(责任/作风/协同)→凝心收尾(目标/干劲/落实)。三层讲法：讲方向(做什么)/讲任务(怎么做,实到「一项目一专班」)/讲底线(不能怎样)。附常用金句（「方向明确关键在行动；任务清晰关键在落实」等）。",
  "howto":"发言按「定调→成绩→问题→任务→要求→收尾」六段套；任务段越实领导越满意（写清「谁盯办/限时」）；态度段用「讲担当/讲作风/讲合力」三句提气；金句点题收尾增强力量感。",
  "url":"https://www.verywps.com/forum.php?mod=viewthread&tid=95",
  "disp":"verywps.com/forum.php?mod=viewthread&tid=95",
  "note":"适用：③ 各类正式会议领导发言提纲结构与金句嵌入。"},
 {"emoji":"📋","title":"高效 Town Hall 议程模板+成功要点","cat":"议程模板","rel":"supervisor","src":"secondary",
  "val":"LiveUniversity 标准 Town Hall 议程：欢迎开场(5)→公司业绩更新(20)→战略举措(15)→员工 Q&A(30)→部门更新(15)→开放讨论反馈(10)→行动项与下一步(5)→闭幕(5)。成功要点：提前多渠道宣传并明确议程、营造欢迎包容氛围、用图表视频可视化、诚实答难题、会后发要点摘要+行动追踪（Asana/Trello）。度量：出勤率/反馈/行动落地。",
  "howto":"套模板时按议题重要性调时间，Q&A 至少留 1/3；会前发议程让员工带问题来；用可视化辅助；答不上来就承诺跟进；会后 24h 内发纪要+用项目管理工具跟行动项。",
  "url":"https://incompany.liveuniversity.com/liveuniversity-news/effective-business-town-hall-meeting-agenda-1767648931",
  "disp":"liveuniversity.com/.../effective-business-town-hall-meeting-agenda",
  "note":"适用：② 上下级全员会的完整议程模板与执行要点。"},
 {"emoji":"⏱️","title":"All-Hands 全流程时间线模板（Run-of-Show）","cat":"时间线","rel":"supervisor","src":"secondary",
  "val":"EventRundown 现成 run-of-show：8:00 AV 技术彩排→8:30 高管到场绿室→9:00 开门入座→9:15 CEO 开场(业绩+愿景)→9:40 工程更新→10:00 销售更新…含每个环节时长与负责人。最佳实践：部门更新≤15min、会前收问题、设专职计时员、全程录制、结尾给明确 CTA。FAQ：有效全员会 60-90min、须录播、议程提前 48-72h 发。",
  "howto":"直接套 run-of-show 当执行表；每环节配 exact time slot 与 owner，设计时员举牌提醒；混合制把时间线链接发给远程员工同频；结尾给「下季度该做什么不同」的明确行动。",
  "url":"https://eventrundown.com/free-event-timeline-templates/all-hands-town-hall-meeting-timeline-template-free",
  "disp":"eventrundown.com/.../all-hands-town-hall-meeting-timeline-template-free",
  "note":"适用：② 上下级全员会落地执行时间表（含 AV/绿室/录制）。"},
 {"emoji":"🗂️","title":"All-Hands/Town Hall 模板·何时用+角色分工","cat":"框架模板","rel":"supervisor","src":"secondary",
  "val":"BestMeetingPlanner 定义全员会=公司级聚会，领导讲战略+庆祝+开放 Q&A，45-60min 月/季频，是透明度与对齐主载体。何时用：跨 30-50 人需广通信/庆祝成就/重大变更（重组并购）/分布式团队。角色：CEO 开场定调、部门头 3-5min 亮点（每月轮值）、HR 主持认可、全员提 Q&A、 facilitator 控时 moderation。含 CloudMetrics 300 人案例。",
  "howto":"用「何时用」清单判断是否真需全员会（避免为开而开）；部门头更新限 3-5min 且每月轮值；facilitator 专职控时+主持匿名 Q&A；远程多时区选重叠窗口。",
  "url":"https://www.bestmeetingplanner.com/templates/all-hands-town-hall-meeting",
  "disp":"bestmeetingplanner.com/templates/all-hands-town-hall-meeting",
  "note":"适用：② 上下级全员会的定位、适用场景与角色分工。"},
 {"emoji":"🎯","title":"策划让员工愿意参与的 Town Hall（目标先行）","cat":"策划方法","rel":"supervisor","src":"secondary",
  "val":"event.com.sg 主张 Town Hall 是「领导时刻」非普通会。先定单一目标（更新/战略沟通/变革/ Engagement/领导可见/认可文化），再围绕互动搭议程：5 欢迎→20 领导更新→15 业务→20 Q&A→10 认可→5 闭幕（约 75min）。强调制作层：音频质量第一、直播多机位、舞台与观众屏、实时投票、技术彩排。常见坑：演讲太长/单向广播。",
  "howto":"先锁定「本轮唯一目标」再排议程，其余做支撑；保护 Q&A 与认可时段不被挤压；制作上音频>画面，远程观众常是多数须等同体验；技术彩排不可省。",
  "url":"https://event.com.sg?p=11517/",
  "disp":"event.com.sg?p=11517",
  "note":"适用：② 上下级全员会的「目标先行+制作层」策划法。"},
 {"emoji":"🎉","title":"年底员工大会怎么开·暖场+总结三段","cat":"实操流程","rel":"supervisor","src":"secondary",
  "val":"今日头条实操：环节1 暖场破冰用「回忆+互动」——年度回忆视频(员工日常/团建/客户感谢)5min 拉归属、年度关键词抢答(举手上台答小礼品)活跃；环节2 总结分三层——老板讲全局(1核心数据+3突破)、部门负责人 5min 讲「做了啥/遇困/咋解/谢谁」、员工代表 3min 讲最难忘一事；避「只报数据」，要讲成果说故事认辛苦。",
  "howto":"暖场用「回忆视频+关键词抢答」替代幼稚游戏，全员可参与不尴尬；总结让部门头带「感谢谁」、员工代表讲真实故事，比念数据更共鸣；控时别让总结变「数据堆砌会」。",
  "url":"https://m.toutiao.com/article/7566473464278712884",
  "disp":"toutiao.com/article/7566473464278712884",
  "note":"适用：② 上下级年底员工大会的暖场与总结三段式落地。"},
 {"emoji":"💬","title":"让企业会议更具互动性·提问+抽奖+主持","cat":"互动技巧","rel":"supervisor","src":"secondary",
  "val":"港成文化：互动关键在「嘉宾↔观众双向」——嘉宾向观众提问、观众向嘉宾提问、入场号牌抽奖、邀观众上台小游戏、嘉宾间分享经验。员工大会专属：主持诙谐幽默让会场轻松、增加现场抽奖(公平设计人人有机会)提积极性。还提明确目标+详细议程是高效前提。",
  "howto":"员工大会用「幽默主持+公平抽奖」调动（抽奖须设计成人人可中奖增重视感）；设「嘉宾↔观众」双向提问环节而非单向宣讲；互动为调动气氛服务，别喧宾夺主。",
  "url":"https://www.gcwhgl.com/index.php?a=index&aid=160&c=View&m=home",
  "disp":"gcwhgl.com/index.php?a=index&aid=160",
  "note":"适用：② 上下级员工大会的现场互动（主持幽默+抽奖+双向提问）。"},
 {"emoji":"🌈","title":"让 All-Hands 更出彩·视觉+互动+故事","cat":"创意玩法","rel":"supervisor","src":"secondary",
  "val":"瑞士电信（Swisscom）All-Hands 创意：①惊喜开场（AI 投影/震撼事实/ Quiz 开场抓注意力）②视觉设计（图表信息图比文字好记、引发情绪、强化专业与品牌归属）③互动（live 投票/匿名 Q&A/idea 墙/员工自讲项目）④故事化（讲公司故事/客户故事/成败故事建连接与骄傲）。强调全员会非形式，是透明与连接机会。",
  "howto":"开场用 Quiz 或震撼事实瞬间抓注意力；用信息图/视频替代大段文字；设匿名 Q&A 与 idea 墙让全员发声；穿插「客户/员工故事」承载数据，比念 PPT 更走心。",
  "url":"https://www.swisscom.ch/en/business/broadcast/media-events/digital-media-streaming/digital-media-blog/allhands-meeting.html",
  "disp":"swisscom.ch/.../allhands-meeting.html",
  "note":"适用：② 上下级全员会的创意玩法（视觉/互动/故事化），企业正式场景可复用。"},
 {"emoji":"🎊","title":"年会/员工大会现场互动玩法·全员参与","cat":"互动玩法","rel":"supervisor","src":"secondary",
  "val":"淘气互动：会前暖场弹幕留言/年度心得打卡/新年心愿上墙（扫码即发言，大屏滚动破冰聚人气）；流程间隙穿插全员答题/年度热点投票/团队风采比拼（题结合企业大事与文化）；收尾仪式全员祝福汇聚/大屏集体合影/全员幸运抽奖（高清大屏留影便传播）。原则：简单友好有温度，破上下级隔阂不喧宾夺主。",
  "howto":"员工大会暖场用「弹幕/心愿墙」扫码互动快速聚人气；间隙用结合企业年度大事的答题/投票稳节奏；收尾用集体合影+幸运抽奖定格高光；玩法贴合正式会务，不低俗不喧闹。",
  "url":"https://cms.taoqihudong.com/cms/news/3365.html",
  "disp":"taoqihudong.com/cms/news/3365.html",
  "note":"适用：② 上下级员工大会/年会的现场互动玩法（破层级隔阂、有温度）。"},
 {"emoji":"🏛️","title":"Town Hall 是什么·价值+常见坑+策略","cat":"基础认知","rel":"supervisor","src":"secondary",
  "val":"Yoroflow 基础篇：Town Hall=领导与员工开放论坛，含战略宣布/业绩回顾/Q&A/认可，核心价值在双向而非单向。数据：78% 员工认为提升透明度、82% 高管认为建信任。三大坑：单向广播(无互动)/收集反馈不闭环(生 cynicism)/信息过载。策略：先定「why」清目的与议程、嵌入 Q&A 与互动、闭环反馈(说清会变什么)、信息分块防过载。",
  "howto":"把全员会当「双向论坛」而非宣讲：议程必含 Q&A 与互动元素；收集到的反馈必须闭环（告知会变啥、为何）；内容分块给重点，别一次灌太多。",
  "url":"https://blogs.yoroflow.com/what-are-town-hall-meeting",
  "disp":"yoroflow.com/what-are-town-hall-meeting",
  "note":"适用：② 上下级全员会的基础认知、价值与三大常见坑。"},
]

def norm(u):
    u = u.strip().lower()
    u = re.sub(r'^https?://', '', u)
    u = re.sub(r'^www\.', '', u)
    u = re.sub(r'\?.*$', '', u)
    return u.rstrip('/')

def card_html(c):
    rel_badge = '<span class="badge r3">高管间</span>' if c['rel']=='exec' else '<span class="badge r2">上下级</span>'
    src_badge = '<span class="badge b1">一手</span>' if c['src']=='primary' else '<span class="badge b2">二手</span>'
    return (f'<div class="hl">\n'
            f'      <div class="top"><span class="emoji">{c["emoji"]}</span><h3>{c["title"]}</h3>'
            f'<span class="cat">{c["cat"]}</span>{rel_badge}{src_badge}</div>\n'
            f'      <p class="val">{c["val"]}</p>\n'
            f'      <details class="exec"><summary>怎么做</summary><div class="inner">{c["howto"]}</div></details>\n'
            f'      <div class="src">🔗 <a href="{c["url"]}" target="_blank">{c["disp"]}</a></div>\n'
            f'      <div class="note">{c["note"]}</div>\n'
            f'    </div>')

# ---- dedup against index.json ----
idx = json.load(open(IDX, encoding='utf-8'))
existing = {norm(e.get('url','')) for e in idx}
new_cards, dup = [], []
for c in CARDS:
    if norm(c['url']) in existing:
        dup.append(c['title'])
    else:
        new_cards.append(c)
N = len(new_cards)
M = len(dup)
print(f'[dedup] N={N} (added)  M={M} (dup skipped): {dup}')

# ---- build card blocks + tmp file ----
blocks = [card_html(c) for c in new_cards]
open(TMP, 'w', encoding='utf-8').write('\n'.join(blocks))

# ---- update cumulative wall ----
wall = open(WALL, encoding='utf-8').read()
GRID = '<div class="grid">'
i3 = wall.index('<div class="sec sec3">')
g3 = wall.index(GRID, i3) + len(GRID)
i2 = wall.index('<div class="sec sec2">')
g2 = wall.index(GRID, i2) + len(GRID)
exec_blocks = [b for b,c in zip(blocks,new_cards) if c['rel']=='exec']
sup_blocks  = [b for b,c in zip(blocks,new_cards) if c['rel']=='supervisor']
wall = wall[:g3] + '\n'.join(exec_blocks) + wall[g3:]
i2 = wall.index('<div class="sec sec2">')
g2 = wall.index(GRID, i2) + len(GRID)
wall = wall[:g2] + '\n'.join(sup_blocks) + wall[g2:]

# ---- recompute counts + update tags & hero ----
n3 = wall.count('badge r3')
n2 = wall.count('badge r2')
print(f'[wall] new counts: sec3(exec)={n3}  sec2(supervisor)={n2}  total={n3+n2}')
wall = re.sub(r'(<div class="sec sec3">[\s\S]*?<span class="tag">)\d+ 卡', lambda m: m.group(1)+f'{n3} 卡', wall, count=1)
wall = re.sub(r'(<div class="sec sec2">[\s\S]*?<span class="tag">)\d+ 卡', lambda m: m.group(1)+f'{n2} 卡', wall, count=1)
wall = re.sub(r'采集于 \d{4}-\d{2}-\d{2}（[^）]*）', f'采集于 {DATE}（第二十一轮补采 +{N}）', wall, count=1)
assert '📌 本页由 yitong 沉淀整理' in wall, 'footer missing!'
open(WALL, 'w', encoding='utf-8').write(wall)
print(f'[wall] written bytes={len(wall.encode("utf-8"))}')

# ---- update index.json ----
for c in new_cards:
    idx.append({
        "title": c['title'],
        "normKey": re.sub(r'\s+','',c['title']),
        "url": c['url'],
        "sourceType": c['src'],
        "relation": 'exec' if c['rel']=='exec' else 'supervisor',
        "summary": c['val'][:120],
        "topic": TOPIC,
        "date": DATE,
    })
json.dump(idx, open(IDX,'w',encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'[index] total={len(idx)}  staff-meeting={sum(1 for e in idx if e.get("topic")==TOPIC)}')

with open(os.path.join(BASE, '_at_r23_meta.json'),'w',encoding='utf-8') as f:
    json.dump({"topic":TOPIC,"round":ROUND,"date":DATE,"N":N,"M":M,
               "n3":n3,"n2":n2,"total":n3+n2,
               "new_titles":[c['title'] for c in new_cards]}, f, ensure_ascii=False, indent=2)
print('[meta] written _at_r23_meta.json')
