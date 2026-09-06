# -*- coding: utf-8 -*-
"""员工大会 r37 补采 build：注入 4×③ + 4×② 共 8 张新卡到累计墙，写 tmp 卡文件，追加 index.json。"""
import json, os, re

KC = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(KC, 'staff-meeting', 'staff-meeting.html')
TMP = os.path.join(KC, 'staff-meeting', '.run_newcards.tmp.html')
IDX = os.path.join(KC, 'index.json')
RUN_DATE = '2026-09-07'
ROUND = 'r37'

def card(emoji, title, cat, rel_badge, rel_label, src_badge, src_label, val, exec_txt, url, note):
    return f'''<div class="hl">
      <div class="top"><span class="emoji">{emoji}</span><h3>{title}</h3><span class="cat">{cat}</span><span class="badge {rel_badge}">{rel_label}</span><span class="badge {src_badge}">{src_label}</span></div>
      <p class="val">{val}</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">{exec_txt}</div></details>
      <div class="src">🔗 <a href="{url}" target="_blank">{url}</a></div>
      <div class="note">适用：{note}</div>
    </div>'''

# ---------- ③ 高管间 (4) ----------
c3_1 = card('📖', '高管变革沟通·用「执行叙事」把战略讲成故事（before/now/soon 三幕）', '高管变革叙事', 'r3', '高管间', 'b2', '二手',
  'Arbor 观点——70% 美国员工未敬业，光靠「战略要点+PPT 要点」无法驱动改变；有效做法是构建 executive narrative：把公司过去/现在/未来放进一个连贯故事（before→now→soon-to-be 三章），含情节/人物/高潮/结局，让战略可感；用个人故事拉近距离、说明「对员工意味着什么」，并邀请团队共创初稿、做受众分析、会后度量效果。把变革定位成对过往努力的尊重而非否定，领导更显人性化。',
  '高管讲战略变革别只发「要点备忘录」——先搭一个 before/now/soon 三幕故事：承认过去为什么这么做（尊重前人）、讲清现在卡在哪、描绘 soon-to-be 员工能参与塑造的未来；把个人经历揉进去让人信，会前邀关键干系人共创初稿、会后用调研度量叙事是否落地。',
  'https://online.arbor.edu/news/communicating-change-embrace-it-opportunity-not-threat',
  '③ 高管在全员会讲战略变革/转型（Arbor 教育学院二手；执行叙事框架，可作「战略变故事」沟通范本）。')

c3_2 = card('🧩', '领导讲故事的结构·张力→转折→新现实（故事 invites、信息 tells）', '领导故事结构', 'r3', '高管间', 'b2', '二手',
  'Liegeois 观点——大多数领导沟通是「信息」而非「故事」：使命标语+战略支柱+OKR，全在告诉员工想什么，没在让他们感受为何而动；故事才是驱动行为的。有效领导故事三段：先抛张力（问题/威胁/不确定）=抓住注意，再给转折（决定/发现/新视角）=故事为什么讲，最后落「新现实」（现在什么可能了）=邀请行动；先找故事再找 slide，越具体越可信（"新加坡会议室客户说我们只有30天"胜过"面临重大挑战"）。',
  '高管准备全员会讲话：别从 deck 开始，先问「我要让这屋人记住哪个瞬间、结束时感受到什么、现在不做哪件事」——那就是故事；结构用张力（我们曾错在哪）→转折（我们改了什么/学到什么）→新现实（做成后你能怎样），用具体人名场景替代抽象挑战。',
  'https://www.liegeoisdesigns.com/blog/embracing-storytelling-as-leadership',
  '③ 高管在全员会/All-Hands 用故事替代要点陈述（Liegeois 咨询二手；张力-转折-新现实故事架构）。')

c3_3 = card('🎯', '高管故事力四支柱·叙事智力+情绪校准+真实存在感+数据×情感（Gartner：叙事影响是高管标志）', '高管故事力', 'r3', '高管间', 'b2', '二手',
  'ISB 高管教育长文——Gartner 2024 领导力愿景将「通过故事传达战略」列为高绩效高管的核心特质；故事不是娱乐而是认知与战略沟通工具，帮团队在复杂/不确定中解读意义、对齐目标。四大支柱：①叙事智力（把复杂挑战蒸馏成有张力与方向的故事线）②情绪校准（在温暖/紧迫/脆弱/坚定间切换深化影响）③真实存在感（Frei：以真实+逻辑+共情建信任，故事显价值观而非表演）④精确清晰（Duarte「激进清晰」，去术语化）；融合分析推理与情感共鸣。',
  '高管练故事力抓四根支柱：把战略难点讲成「有 stake 和方向」的故事线而非罗列；按场合切换情绪温度；用真实经历显价值观（别演）；坚决去 jargon 做「激进清晰」。简言之——故事让人信、数据让人懂，二者缺一都推不动。',
  'https://execed.isb.edu/executive-perspectives/directory/storytelling-techniques-that-drive-results-a-comprehensive-guide-for-leaders',
  '③ 高管提升全员会叙事影响力（ISB exec ed 二手；故事力四支柱框架，可作高管沟通能力建设范本）。')

c3_4 = card('🔺', '高管叙事「3C」框架·挑战·选择·改变（叙事先于决策，填补认知空白）', '高管叙事3C', 'r3', '高管间', 'b2', '二手',
  'Communications Collective 2026 观点——现代领导不能只靠「冷静/准确/谨慎」，员工要理解领导怎么想、信什么、不确定时怎么决；故事是核心领导力技能而非个性。有效领导故事含 3C：Challenge（挑战）、Choice（选择）、Change（改变），Jacinda Ardern 即先定「我是何种领导、为何这样决」的叙事框架，使后续决策都被预定义透镜解读；个人叙事须与组织使命对齐（价值聚焦而非自我聚焦）才不损权威；不叙事的沉默会被他人填补认知空白、放大风险。',
  '高管在全员会前先讲清「我是谁、信什么、面临挑战时怎么选」的 3C 叙事框架，让后续战略决策有连贯解释、减少猜测；叙事聚焦组织价值而非个人英雄，避免表演感；沉默比讲错更危险——别人会替你填故事。',
  'https://communicationscollective.com.au/?p=2783',
  '③ 高管在全员会建立可信领导身份（Communications Collective 二手；3C 叙事框架，可作「叙事先于决策」范本）。')

# ---------- ② 上下级 (4) ----------
c2_1 = card('🔁', '全员会会后闭环·Recap+反馈调研+行动跟进+ROI 度量（NPS/满意度/行为改变）', '会后闭环', 'r2', '上下级', 'b2', '二手',
  'Marketing Scoop 指南——全员会价值在会后才发生：会后 24h 内发 recap（关键决策/行动项/资源链接/录播）；用调研/NPS/满意度收反馈并据其迭代形式；把反馈变行动（公开回应会上问题、给 owner 与 deadline）；用邮件/Slack/团队 huddle 持续强化关键信息、庆祝进展防能量流失；度量 attendance/engagement/feedback/action 四维度证明 ROI；举 Zappos（怪装游戏强化价值观）、HubSpot（主题 deck+互动）、Drift（"Drift Love" 同事互夸+CEO 热座）为范例。',
  '办全员会别让价值止步现场：24h 内发 recap（决策+行动项+录播），调研收满意度并据以改版，把会上问题公开回应、每项行动落 owner+deadline，用日常渠道持续强化关键讯息；用 NPS/行为改变度量证明投入产出，避免「人来了就结束」。',
  'https://www.marketingscoop.com/marketing/the-all-hands-meeting-your-guide-to-aligning-and-inspiring-your-team/',
  '② HR/行政 × 全员（Marketing Scoop 二手；会后闭环+ROI 度量，可作「会议不止于现场」范本）。')

c2_2 = card('🏛️', 'Town Hall 本质与避坑·5段议程+远程优先+3大常见错误（录制不能替代书面 recap）', 'Town Hall 避坑', 'r2', '上下级', 'b2', '二手',
  'Legislate.ai 指南——Town Hall 不是广播而该是「方向+提问+上下文+反馈」；与 all-hands 区别在更重双向对话与 Q&A。5 段议程：CEO 开场→业务更新→人员/文化更新→聚焦主题→提问环节（提前收匿名问题/投票）；远程混合团队需提前发议程、slide 可读、重复被问问题再答、会后发简短书面 recap；3 大错误：会议过长（部门轮流加 slide 变汇报马拉松）、用模糊更新躲真问题、收了问题从不跟进。具体（"投哪个市场"）胜笼统（"投资增长"）建信任。',
  '办 Town Hall 学 legislate「双向对话优先」：议程末段留足匿名/投票提问，远程员工做「一等公民」（盯 chat、早邀远程提问、别只讲屋里笑话）；会后必发书面 recap（录制不能替代）；避三坑——超时、躲真问题、收问不跟进。',
  'https://www.legislate.ai/blog/town-hall-meeting-meaning-examples-teams',
  '② 行政/HR × 全员（Legislate.ai 二手；Town Hall 本质+远程优先+避坑，可作「双向对话」范本）。')

c2_3 = card('🗂️', '企业全员大会组织技巧·30天倒计时/风险预案/AV 配置/分级通知（实操 PPT）', '大会组织SOP', 'r2', '上下级', 'b2', '二手',
  '人人文库《企业全员大会组织技巧》PPT——把会前 30 天拆为策划期(D-30)/筹备期(D-15)/冲刺期(D-7)三阶段、每阶段 5–8 项交付物验收；主题用「主标题+副标题」含动词（如「聚势·谋远——年度战略解码大会」）+ 主 KV；含 12 类风险预案（场地变更/设备故障/嘉宾缺席，标应对+责任人+启用条件）、200+ 细项物资矩阵（电子 PPT 模板/实体桌签）、AB 角责任书、每日 17:00 站会+Trello 看板；C-level 用一对一类邮件+短信+专属会务经理，企业微信/钉钉每周 2 次进度提醒。',
  '办大型全员大会照此 SOP：会前 30 天三段式里程碑管控、主题「动词+副标题」定传播、12 类风险逐一配预案与责任人、物资分电子/实体列 200+ 清单、C-level 走专属直达通道；关键是把「行政杂活」变可验收的项目管理，避免会前一团乱。',
  'https://www.renrendoc.com/paper/456227424.html',
  '② 行政/会务 × 中大型全员大会（人人文库二手；30天倒计时SOP+风险预案，可作大会组织实操范本）。')

c2_4 = card('📣', '多渠道宣贯策略·提升员工大会参与度（内网/邮件/社交平台+奖励机制+口碑）', '会前宣传', 'r2', '上下级', 'b2', '二手',
  'MBA 智库——提高员工大会参与度需多渠道组合：公司内部通讯/员工邮件/官网/内部社交平台全覆盖确保信息到人；会前订详细宣传计划（内容/方式/时间）；制吸引人的海报/宣传视频抓眼球；让领导或知名员工带头宣传做口碑传播；设参与奖励（抽奖/证书/学习机会）激励；按员工特点偏好做个性化定制提升认同感。宣贯不是会前发个通知，而是持续造势让「想来」发生。',
  '提全员大会参与度学 MBA 智库「多渠道+奖励+口碑」：会前用邮件/内网/内部社交平台组合拳持续触达，制海报短视频造势，拉领导/意见领袖带头宣传做口碑，设抽奖或证书等参与奖励；按人群做个性化触达，把「被动通知」变「主动想来」。',
  'https://www.mbalib.com/ask/question-bc25b6df4afac191b7bd642ce026c239.html',
  '② 行政/HR × 全员（MBA 智库二手；多渠道宣贯提升参与度，可作会前造势范本）。')

cards_3 = [c3_1, c3_2, c3_3, c3_4]
cards_2 = [c2_1, c2_2, c2_3, c2_4]
all_cards = cards_3 + cards_2

# ---------- 注入累计墙 ----------
html = open(WALL, encoding='utf-8').read()

# sec3 grid：在 <div class="sec sec3"> 之后的第一个 <div class="grid"> 后插入
i3 = html.index('<div class="sec sec3">')
g3 = html.index('<div class="grid">', i3)
insert_3 = ''.join(cards_3)
html = html[:g3+len('<div class="grid">')] + '\n' + insert_3 + html[g3+len('<div class="grid">'):]

# sec2 grid：在 <div class="sec sec2"> 之后的第一个 <div class="grid"> 后插入
i2 = html.index('<div class="sec sec2">')
g2 = html.index('<div class="grid">', i2)
insert_2 = ''.join(cards_2)
html = html[:g2+len('<div class="grid">')] + '\n' + insert_2 + html[g2+len('<div class="grid">'):]

# 计数更新：128→132 / 255→259
html = html.replace('    <span class="tag">128 卡</span>', '    <span class="tag">132 卡</span>', 1)
html = html.replace('    <span class="tag">255 卡</span>', '    <span class="tag">259 卡</span>', 1)

# hero 追加本轮段
html = html.replace('三十六轮 enrich 2026-09-06(+7)</p>', '三十六轮 enrich 2026-09-06(+7)｜ 三十七轮 enrich 2026-09-07(+8)</p>', 1)

# 顶部增量页链接 r36→r37
html = html.replace('runs/staff-meeting-2026-09-06-r36.html', 'runs/staff-meeting-2026-09-07-r37.html', 1)

open(WALL, 'w', encoding='utf-8').write(html)
print('WALL updated. len=', len(html))

# ---------- tmp 卡文件（供 gen_run_page.py）----------
open(TMP, 'w', encoding='utf-8').write(''.join(all_cards))
print('TMP written. cards=', len(all_cards))

# ---------- index.json 追加 ----------
def normkey(t):
    t = t.lower()
    t = re.sub(r'[^\w\u4e00-\u9fff]', '', t)
    return t

idx = json.load(open(IDX, encoding='utf-8'))
before = len(idx)

entries = [
  ('高管变革沟通·用「执行叙事」把战略讲成故事', 'https://online.arbor.edu/news/communicating-change-embrace-it-opportunity-not-threat', 'secondary', 'exec', 'Arbor：用 before/now/soon 三幕 executive narrative 把战略讲成故事，含情节人物高潮，个人故事拉近距离，会前共创初稿+会后度量，变革定位为尊重过往而非否定。'),
  ('领导讲故事的结构·张力→转折→新现实', 'https://www.liegeoisdesigns.com/blog/embracing-storytelling-as-leadership', 'secondary', 'exec', 'Liegeois：领导沟通多为「信息」非「故事」；有效故事三段=张力(抓注意)→转折(故事为何讲)→新现实(邀请行动)；先找故事再找 slide，越具体越可信。'),
  ('高管故事力四支柱·叙事智力+情绪校准+真实存在感+数据×情感', 'https://execed.isb.edu/executive-perspectives/directory/storytelling-techniques-that-drive-results-a-comprehensive-guide-for-leaders', 'secondary', 'exec', 'ISB exec ed：Gartner 将「故事传达战略」列为高管核心特质；四支柱=叙事智力/情绪校准/真实存在感(Frei)/精确清晰(Duarte 激进清晰)，融分析与情感。'),
  ('高管叙事「3C」框架·挑战·选择·改变', 'https://communicationscollective.com.au/?p=2783', 'secondary', 'exec', 'Communications Collective：领导故事含 3C=Challenge/Choice/Change，Ardern 先定叙事框架使决策被预读；叙事须对齐组织使命，沉默会被他人填认知空白。'),
  ('全员会会后闭环·Recap+反馈调研+行动跟进+ROI 度量', 'https://www.marketingscoop.com/marketing/the-all-hands-meeting-your-guide-to-aligning-and-inspiring-your-team/', 'secondary', 'supervisor', 'Marketing Scoop：会后 24h 发 recap，调研/NPS 收反馈，行动落 owner+deadline，日常渠道强化关键信息；度量 attendance/engagement/feedback/action 四维度证 ROI；Zappos/HubSpot/Drift 范例。'),
  ('Town Hall 本质与避坑·5段议程+远程优先+3大常见错误', 'https://www.legislate.ai/blog/town-hall-meeting-meaning-examples-teams', 'secondary', 'supervisor', 'Legislate.ai：Town Hall 重双向对话+Q&A；5 段议程 CEO 开场→业务→人员文化→聚焦主题→提问；远程做一等公民；3 大错误=超时/躲真问题/收问不跟进；录制不能替代书面 recap。'),
  ('企业全员大会组织技巧·30天倒计时/风险预案/AV/分级通知', 'https://www.renrendoc.com/paper/456227424.html', 'secondary', 'supervisor', '人人文库 PPT：会前 30 天拆三阶段里程碑管控，主题「动词+副标题」+主 KV，12 类风险预案，200+ 物资矩阵，AB 角责任书，C-level 专属直达通道。'),
  ('多渠道宣贯策略·提升员工大会参与度', 'https://www.mbalib.com/ask/question-bc25b6df4afac191b7bd642ce026c239.html', 'secondary', 'supervisor', 'MBA 智库：多渠道(内网/邮件/社交平台)组合触达+海报短视频造势+领导口碑带头+参与奖励+个性化定制，把「被动通知」变「主动想来」。'),
]

existing_urls = set(e.get('url','') for e in idx)
added = 0
for title, url, st, rel, summ in entries:
    if url in existing_urls:
        print('SKIP dup url:', url)
        continue
    idx.append({
        'title': title, 'normKey': normkey(title), 'url': url,
        'sourceType': st, 'relation': rel, 'summary': summ,
        'topic': '员工大会', 'slug': 'staff-meeting', 'round': ROUND, 'date': RUN_DATE,
    })
    added += 1

json.dump(idx, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'INDEX: before={before} added={added} after={len(idx)}')
