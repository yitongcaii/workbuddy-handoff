# -*- coding: utf-8 -*-
"""员工大会 r40 补采 build：注入 4×③ + 4×② 共 8 张新卡到累计墙，写 tmp 卡文件，追加 index.json。"""
import json, os, re

KC = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(KC, 'staff-meeting', 'staff-meeting.html')
TMP = os.path.join(KC, 'staff-meeting', '.run_newcards.tmp.html')
IDX = os.path.join(KC, 'index.json')
RUN_DATE = '2026-09-09'
ROUND = 'r40'

def card(emoji, title, cat, rel_badge, rel_label, src_badge, src_label, val, exec_txt, url, note):
    return f'''<div class="hl">
      <div class="top"><span class="emoji">{emoji}</span><h3>{title}</h3><span class="cat">{cat}</span><span class="badge {rel_badge}">{rel_label}</span><span class="badge {src_badge}">{src_label}</span></div>
      <p class="val">{val}</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">{exec_txt}</div></details>
      <div class="src">🔗 <a href="{url}" target="_blank">{url}</a></div>
      <div class="note">适用：{note}</div>
    </div>'''

# ---------- ③ 高管间 (4) ----------
c3_1 = card('🤖', 'AI 数字人 CEO 视频内通·高频常规更新（危机/重大变革须真人）', 'AI 数字人内通', 'r3', '高管间', 'b2', '二手',
  'KHABY AI——用 CEO 高保真数字分身按脚本生成内部视频，填补「高频小更新」空白：周更 2-3 分钟业务摘要、政策/流程变更、文化价值观短内容，多语言同步触达全球/倒班/异地团队，2-3 倍于纯文字邮件的打开与参与。关键边界：信息类（季度更新/政策/运营简报）可用数字人；危机应对、重大组织变革、文化里程碑等需要真实情感连接的时刻，仍须真人视频或现场。治理三基线：签署肖像授权（12 个月可续）、内容范围限定（禁财务指引/HR 动作如裁员重组/对外发布）、每段生成须高管或幕僚长审签；披露用语「脚本由 X 撰写并经其授权 AI 形象生成」。',
  '想用数字人补全员会「低频大仗之外的日常在场感」学 KHABY：先盘点应做却做不出的高频内容（周更业务摘要/政策解读/多地同步），建内容日历审计缺口；挑 1-2 位高管建高保真分身（5-15 分钟源视频训练）；平台按治理选 Synthesia（企业合规 SOC2）或 HeyGen（速度）；设固定节奏（周业务更新+月全员会摘要+季战略简报）；走现有渠道（Teams/Slack/内网/邮件）而非新开；每次发布前高管/幕僚长审签+AI 使用披露；度量打开率对比旧形式。硬边界：裁员/重组/危机/文化里程碑一律真人。适合跨地域集团日常内通提频，关键「数字人填日常空隙、真人守信任关头」。',
  'https://khaby.ai/use-cases/ai-avatar-internal-comms',
  '③ 高管/Comms 负责人 × 全员（KHABY AI 二手；AI 数字人内通，可作跨地域高频内通范本，须标注重大变革/危机真人边界）。')

c3_2 = card('🛡️', '高管 Q&A 难问题/敌意问题·四步应答（acknowledge→substance→constraints→next）', 'Q&A 难问题', 'r3', '高管间', 'b2', '二手',
  'Winning Presentations——全员会 Q&A 最危险的不是问题本身，是防御性回应。四步法：①Acknowledge 承认情绪不认框架（"我理解这让人焦虑"而非"这说法不公平"）；②Substance 60 秒实质原则——一句点结论、一句讲理由、一句说约束，停；③Name the gap 点出未尽之处（"这点今天给不了确定答复，但…"）；④Next step 给下一步（谁、何时回）。敌意问题常见误判是 over-explain 方法论（翻委员会/董事会/数据来源），房间听到的是 filibuster；60 秒实质原则比 4 分钟过度解释更短更稳。虚拟场改读聊天队列与主持人，每步前刻意停 2 秒显从容。',
  '被尖锐/敌意问题怼时学 Winning Presentations「四步+60 秒实质」：先认可情绪不认框架（"这担忧我理解"），再 60 秒给实质（结论→理由→约束），别翻方法论自证；点出信息缺口并给下一步（责任人+日期）；虚拟场让主持人原样读题、每步前停 2 秒。提前把高频难问题写成完整句并朗读润色、会前归档。适合重组/降本/争议议题全员会，关键「你要的是 300 人看见你如何承压，不是赢下提问者」。',
  'https://winningpresentations.com/tag/town-hall-question-response',
  '③ 高管/发言人 × 全员（Winning Presentations 二手；Q&A 难问题四步应答，可作高压全员会应答范本）。')

c3_3 = card('🎭', '高管全员会 临场气场·肢体语言（占空间+眼神+能量先于内容）', '临场气场', 'r3', '高管间', 'b2', '二手',
  'Mazterpiece——高管在全员会的可信度，开场前已由身体判定。三点可练：①Claim your footprint 占住空间再拿麦——用满台的边与角而非只站中央，缩在一点等于默认「自己不属于这」；②Let eyes do the work 持续眼神接触（即便思考时停顿也看人）比任何金句更建信任，排练时就要改掉抬头看天花板；③Arrive switched on 能量先于内容——走到台前 flat、三分钟才热身，已丢掉盒型会议厅里最重的首因。底层逻辑：姿势不是性格是杠杆，挺肩扩胸/双脚开立会反向校准你的神经系统与观众判断。',
  '想让全员会「人未开口已掌场」学 Mazterpiece「占空间+眼神+能量先于内容」：上台前把肩打开、双脚开立占满台面边角而非缩一点；思考停顿也保持眼神接触、别抬头看天花板；走到台前就带着能量，别等三分钟才热身；把姿势当可调杠杆反复练而非寄望天生 charisma。适合新领导首秀/年度全员会，关键「气场是可训练的肢体决策，不是人格天赋」。',
  'https://mazterpiece.com/the-executives-guide-to-public-speaking-body-language',
  '③ 高管/发言人 × 全员（Mazterpiece 二手；临场气场肢体语言，可作高管登台呈现范本）。')

c3_4 = card('📅', '全员会 频率/节奏 决策（月度理想·季度大·危机周更·Q&A≥30%）', '频率节奏', 'r3', '高管间', 'b2', '二手',
  'RoamJobs——全员会频率取决于规模与变革速度：高速成长初创常周更对齐剧变；成熟公司多落月度，超大型组织季更+部门会补位；远程越多越该频（是组织凝聚关键触点）。黄金区间 30-60 分钟（45 分钟最佳），议程 3-4 个话题（业绩 10′+战略/聚焦 10′+表彰 5′+Q&A 20-30′），Q&A 至少占 1/3；会前 2-3 天发议程、用 Slido 匿名预收问题；无论选何频率必须稳定——随意取消=释放「沟通只在有事时重要」的信号。',
  '定全员会节奏学 RoamJobs「按变革速度定频+稳定为铁律」：初创剧变周更、成熟月度、超大季更+部门补；锁 45 分钟、议程 3-4 题、Q&A≥30%；会前 2-3 天发议程+匿名收题；最忌随意取消或跳过——那等于告诉全员「沟通不是真重视」。适合定年度沟通日历，关键「频率可以不同，稳定不能破」。',
  'https://roamjobs.com/terms/all-hands',
  '③ 高管/内部沟通负责人 × 全员（RoamJobs 二手；全员会频率节奏决策，可作沟通日历范本）。')

# ---------- ② 上下级 (4) ----------
c2_1 = card('🏢', 'RTO 返office 全员会沟通·live forum 而非邮件+先听后推+区分两类体验', 'RTO 沟通', 'r2', '上下级', 'b2', '二手',
  'Ragan（Stellantis 案例）——RTO 真正的考验不是政策是否合理，而是员工是否觉得领导理解他们在被要求什么。要点：①用现场全员会而非邮件宣布（实时传递语气、nuance、可即时回应，邮件给不了）；②推之前真的去听——做调研、开焦点小组、搞清不同群体担心什么，哪怕结果不被所有人喜欢，被听见就大幅降抵触；③绝不简化受众：对「从没远程过」与「习惯了远程」的员工是两种截然不同的人生体验，不承认这点的人会觉得被忽视或不公；④宣布后下一步是挪出时间物理在场，与团队面对面。',
  '推 RTO 用全员会沟通学 Ragan/Stellantis「现场宣布+先听后推+区分体验」：政策用 live forum 而非邮件（语气/nuance/即时回应邮件给不了）；推出前做调研与焦点小组、搞清不同群体担心；明确承认「常驻 office」与「习惯远程」是两种体验、别一刀切；宣布后领导挪时间物理在场、与团队面对面。适合返 office 全员沟通，关键「人信不信政策，取决于是否觉得被真正听见」。',
  'https://www.ragan.com/?p=337621/',
  '② 领导/HRBP × 全员（Ragan 二手；RTO 返 office 全员会沟通，可作返岗沟通范本）。')

c2_2 = card('🚀', 'IPO 里程碑全员会·org meeting 当日 townhall+quiet period+只谈业务不谈发行', 'IPO 全员会', 'r2', '上下级', 'b2', '二手',
  'New Street IR / Gilmartin——IPO 流程以 org meeting（组织会议）正式起跑，SEC 此后视一切为公司 promotional，故多数公司当日即开全员 townhall：讲为何上市（时机/融资）、如何契合公司故事弧、管理层多兴奋；讲「成为上市公司意味着什么」（股票可交易、带来的机会）；明确新政策——严格限制对外讨论工作流/决策/沟通、指定唯一对外联系人；HR 提前做内幕交易培训。黄金法则：绝不能显得「上市失败」——故用 townhall 而非邮件作首次沟通。Quiet period 内员工禁谈潜在 IPO；S-1 公开翻转后发邮件庆贺并提示严格静默期，建 FAQ、开 townhall 讲历程/理由/含义/下一步。',
  '筹备 IPO 全员沟通学 New Street/Gilmartin「当日 townhall+quiet period 纪律」：org meeting 当天开全员会讲为何上市、上市意味着什么、对外唯一联系人；HR 提前做内幕交易与 MNPI 培训；S-1 公开翻转后邮件庆贺并提示静默期、建 FAQ、再开 townhall 讲历程与下一步；全程只谈业务与里程碑、绝口不提估值/时间表/发行本身；对外统一发言人。适合拟上市全员沟通，关键「让全员知情而非被蒙、但严守合规边界防 gun-jumping」。',
  'https://newstreetir.com/?p=389',
  '② 领导/IR/HR × 全员（New Street IR 二手；IPO 里程碑全员会，可作拟上市内通范本）。')

c2_3 = card('📋', '全员会 Q&A 准备模板·message themes+likely/sensitive questions+follow-up', 'Q&A 准备模板', 'r2', '上下级', 'b2', '二手',
  'HogoNext——可复用的全员会 Q&A 准备 doc：①Message themes——主信息/什么在变/什么不变/保持的语气；②Likely questions——问题+员工为何问+草稿答案+所需数据/来源+负责人；③Sensitive questions——问题+安全回答边界+是否需法务/HR 审+如何 bridge 回主信息；④Questions to avoid over-answering——话题+为何不全答+获批措辞；⑤Follow-up plan——未答问题负责人+recap 形式+截止日+反馈渠道。示例：Q3 全员会，CEO 主信息「增长慢于预期但聚焦盈利客户群」，敏感题「裁员来了吗」安全边界「今天不宣布裁员，我们在管支出以避免更剧烈动作」。',
  '办全员会前用 HogoNext「Q&A 准备模板」填空：先定 message themes（主信息/变与不变/语气）；列 likely questions（为何问+草稿+数据+负责人）与 sensitive questions（安全边界+法务/HR 审+bridge 话术）；标出 over-answering 禁区与获批措辞；定 follow-up plan（未答谁跟/recap 形式/截止/反馈渠道）。适合任何带难议题的全员会，关键「把应答准备成文，现场不靠临场发挥」。',
  'https://hogonext.com/templates/town-hall-qa-prep',
  '② 内部沟通/HRBP × 全员（HogoNext 二手；Q&A 准备模板，可作全员会筹备范本）。')

c2_4 = card('📊', '全员会效果度量·KPI（出席70%+/参与60%+/情绪75%+/观看50-70%/行动25%+）', '效果度量', 'r2', '上下级', 'b2', '二手',
  'Airmeet——全员会别只凭感觉，用 KPI 证价值：出席率（目标 70%+）、参与率（60%+，主动互动）、情绪分（75% 正面）、平均观看时长（50-70% 场次）、行为行动率（25%+，会后真去做的比例）。虚拟/混合场还能拿实时热图、地理参与、掉线模式、聊天/emoji 情绪、Q&A 主题趋势；工具层用实时投票+Q&A 分析、参与仪表盘、会后即时 pulse 调研（延迟发完成率骤降）。ROI=（事件回报−事件成本）/成本×100，先定战略目标（对齐/变革采纳/文化/知识）再配 KPI。被听见的员工产出 best work 概率高 4.6 倍。',
  '证明全员会「没白开」学 Airmeet「KPI+复盘」：定出席 70%+/参与 60%+/情绪 75%+/观看 50-70%/行动 25%+ 基准；虚拟场拉实时热图与掉线模式找内容疲劳点；会后即时发 pulse（别拖，延迟完成率掉）；跨场次比 CEO 讲话/团队更新/Q&A 各段参与差异；ROI=（回报−成本）/成本。适合向管理层证明内通预算、持续优化议程，关键「持续度量的团队比把交付当终点的团队迭代快得多」。',
  'https://www.airmeet.com/hub/blog/measuring-employee-engagement-in-townhalls-and-internal-events',
  '② 内部沟通/HR × 全员（Airmeet 二手；全员会效果度量 KPI，可作复盘范本）。')

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

# 计数更新：140→144 / 267→271
html = html.replace('    <span class="tag">140 卡</span>', '    <span class="tag">144 卡</span>', 1)
html = html.replace('    <span class="tag">267 卡</span>', '    <span class="tag">271 卡</span>', 1)

# hero 追加本轮段
html = html.replace('三十九轮 enrich 2026-09-08(+8)</p>', '三十九轮 enrich 2026-09-08(+8)｜ 四十轮 enrich 2026-09-09(+8)</p>', 1)

# 顶部增量页链接 r39→r40
html = html.replace('runs/staff-meeting-2026-09-08-r39.html', 'runs/staff-meeting-2026-09-09-r40.html', 1)

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
  ('AI 数字人 CEO 视频内通·高频常规更新（危机/重大变革须真人）', 'https://khaby.ai/use-cases/ai-avatar-internal-comms', 'secondary', 'exec', 'KHABY AI：CEO 高保真数字分身按脚本生成内部视频，填补高频小更新空白（周更业务摘要/政策解读/多地同步，2-3 倍文字邮件参与）；信息类可用、危机/重大变革/文化里程碑须真人；治理三基线：肖像授权+内容范围限定+高管审签+AI 使用披露。'),
  ('高管 Q&A 难问题/敌意问题·四步应答（acknowledge→substance→constraints→next）', 'https://winningpresentations.com/tag/town-hall-question-response', 'secondary', 'exec', 'Winning Presentations：Q&A 四步法——承认情绪不认框架+60 秒实质（结论→理由→约束）+点出未尽+给下一步；敌意问题误判是 over-explain 方法论（像 filibuster）；虚拟场读聊天队列、每步前停 2 秒。'),
  ('高管全员会 临场气场·肢体语言（占空间+眼神+能量先于内容）', 'https://mazterpiece.com/the-executives-guide-to-public-speaking-body-language', 'secondary', 'exec', 'Mazterpiece：高管可信度开场前已由身体判定；占住空间再拿麦（用满台边角非只站中央）、持续眼神接触（思考停顿也看人）、能量先于内容（走到台前就带能量）；姿势是可训练杠杆非性格天赋。'),
  ('全员会 频率/节奏 决策（月度理想·季度大·危机周更·Q&A≥30%）', 'https://roamjobs.com/terms/all-hands', 'secondary', 'exec', 'RoamJobs：频率按规模与变革速度——初创剧变周更、成熟月度、超大季更+部门补；锁 45 分钟、议程 3-4 题、Q&A≥30%；会前 2-3 天发议程+匿名收题；随意取消=释放「沟通只在有事时重要」信号。'),
  ('RTO 返office 全员会沟通·live forum 而非邮件+先听后推+区分两类体验', 'https://www.ragan.com/?p=337621/', 'secondary', 'supervisor', 'Ragan(Stellantis)：RTO 考验是员工是否觉得被理解；用现场全员会而非邮件宣布（语气/nuance/即时回应）、推前做调研焦点小组真去听、承认「常驻 office」与「习惯远程」是两种体验、宣布后领导物理在场面对面。'),
  ('IPO 里程碑全员会·org meeting 当日 townhall+quiet period+只谈业务不谈发行', 'https://newstreetir.com/?p=389', 'secondary', 'supervisor', 'New Street IR/Gilmartin：IPO 以 org meeting 起跑、当日开全员 townhall 讲为何上市/上市意味着什么/对外唯一联系人；HR 提前做内幕交易培训；S-1 翻转后邮件庆贺+静默期+FAQ+townhall；全程只谈业务不谈估值/时间表/发行；防 gun-jumping。'),
  ('全员会 Q&A 准备模板·message themes+likely/sensitive questions+follow-up', 'https://hogonext.com/templates/town-hall-qa-prep', 'secondary', 'supervisor', 'HogoNext：可复用 Q&A 准备 doc——message themes(主信息/变与不变/语气)+likely questions(为何问+草稿+数据+负责人)+sensitive questions(安全边界+法务/HR 审+bridge)+over-answering 禁区+follow-up plan(未答谁跟/recap/截止/反馈)。'),
  ('全员会效果度量·KPI（出席70%+/参与60%+/情绪75%+/观看50-70%/行动25%+）', 'https://www.airmeet.com/hub/blog/measuring-employee-engagement-in-townhalls-and-internal-events', 'secondary', 'supervisor', 'Airmeet：用 KPI 证全员会价值——出席 70%+/参与 60%+/情绪 75%+/观看 50-70%/行动 25%+；虚拟场拉实时热图与掉线模式找疲劳点；会后即时 pulse（延迟完成率掉）；ROI=(回报−成本)/成本；被听见的员工 best work 概率高 4.6 倍。'),
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
