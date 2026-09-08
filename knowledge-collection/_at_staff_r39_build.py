# -*- coding: utf-8 -*-
"""员工大会 r39 补采 build：注入 4×③ + 4×② 共 8 张新卡到累计墙，写 tmp 卡文件，追加 index.json。"""
import json, os, re

KC = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(KC, 'staff-meeting', 'staff-meeting.html')
TMP = os.path.join(KC, 'staff-meeting', '.run_newcards.tmp.html')
IDX = os.path.join(KC, 'index.json')
RUN_DATE = '2026-09-08'
ROUND = 'r39'

def card(emoji, title, cat, rel_badge, rel_label, src_badge, src_label, val, exec_txt, url, note):
    return f'''<div class="hl">
      <div class="top"><span class="emoji">{emoji}</span><h3>{title}</h3><span class="cat">{cat}</span><span class="badge {rel_badge}">{rel_label}</span><span class="badge {src_badge}">{src_label}</span></div>
      <p class="val">{val}</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">{exec_txt}</div></details>
      <div class="src">🔗 <a href="{url}" target="_blank">{url}</a></div>
      <div class="note">适用：{note}</div>
    </div>'''

# ---------- ③ 高管间 (4) ----------
c3_1 = card('🎬', '新领导首次全员会操盘·目标先行+会前邀员工参与+会后闭环', '新领导首会', 'r3', '高管间', 'b2', '二手',
  'Justworks 实操指南——首次全员会不是「信息发布会」而是「团队对齐仪式」。四步：①定首要目标（战略对齐还是答疑）；②会前数周用调研收集员工心声、让议程由他们关心的事塑形；③用「愿景→部门更新→具体战果+挑战→Q&A」平衡结构；④会后 1-2 天发要点回顾、收反馈、兑现承诺。指定制片人管时序与技术，让讲者专注互动。',
  '办新领导首次全员会学 Justworks「目标先行+会前邀员工参与+会后闭环」：会前数周用调研听员工关心什么、议程由心声塑形；会上用「愿景→部门更新→战果与挑战→Q&A」平衡结构；指定制片人管时序与技术让领导专注；会后 1-2 天发 recap、收反馈、兑现承诺。适合新 CEO/GM 上任首秀，关键是「让员工感到被听见而非被宣读」。',
  'https://www.justworks.com/blog/how-to-run-your-first-all-hands-meeting',
  '③ 新领导/CEO × 全员（Justworks 二手；首次全员会操盘手册，可作新领导上任首秀范本）。')

c3_2 = card('🔀', '变革沟通计划·高管叙事与员工落地分开写+多渠道矩阵', '变革沟通计划', 'r3', '高管间', 'b2', '二手',
  'Changeadaptive——变革沟通计划要把受众切成高管/员工分别写信息（高管=市场领先定位，员工=工作流会变但有培训）；渠道矩阵覆盖 Town Hall（大规模宣布）/邮件（结构化书面）/内网门户（持续更新枢纽）/领导视频（个性化建信任）/一对一面谈（高影响干系人）/调研+Q&A（双向）；时间线分前-中-后三段；角色清晰：高管讲「为什么」与战略理由，经理对团队讲「意味着什么」。',
  '做变革沟通计划学 Changeadaptive「分层信息+多渠道矩阵」：把受众切成高管/员工分别写（高管=领先定位，员工=工作流会变但有培训）；渠道组合 Town Hall+邮件+内网+领导视频+面谈+调研 Q&A；时间线覆盖会前认知/会中更新/会后庆祝反馈；角色=高管讲 Why、经理讲 So-what、专人管渠道。适合组织变革/重组，关键「多通道覆盖+双向反馈」而非一封全员邮件。',
  'https://changeadaptive.com/?p=3978',
  '③ 高管/变革负责人 × 全员（Changeadaptive 二手；变革沟通计划，可作重组/转型全员沟通范本）。')

c3_3 = card('📣', '变革期领导沟通·会前会+会后会+故事化+过度沟通', '变革领导沟通', 'r3', '高管间', 'b2', '二手',
  'HFMA（Jill Geisler）——变革期领导沟通三招：①「会前会」先找几位受同事信任的影响者透风、邀其问尖锐问题，他们成你的翻译者；②「会后会」领导与副手走场一对一，听大群里不敢问的；③把信息当货币——宁可过度沟通，别让谣言填空。用 master narrative（组织的「我们是谁、为何做」）讲真实故事而非冷报告卖变革。',
  '变革期开全员会学 HFMA「会前会+会后会+故事化+过度沟通」：会前先与几位受尊重的影响者 1:1 透风、请他们问尖锐问题，他们帮你翻译意图；会中真诚清晰；会后领导走场一对一清误解、安恐惧；把信息当货币宁可多讲；用「我们是谁、为何做」的 master narrative 讲真实故事。适合艰难变革（重组/降本），关键「别只靠备忘录，人需要被当面看见」。',
  'https://www.hfma.org/?p=35465',
  '③ 领导/经理 × 全员（HFMA 二手；变革期领导沟通三招，可作艰难变革全员会范本）。')

c3_4 = card('📝', '职工大会领导讲话稿·受众分层翻译+「我们」叙事+三段式', '领导讲话稿', 'r3', '高管间', 'b2', '二手',
  '人人文库实务——职工大会领导讲话稿要「受众分层翻译」：基层职工强调收入/技能/通道（"班组奖金池扩容+外部研修"），管理团队强调管理效能/团队荣誉（"成本管控成效显著优先评优"）。身份平衡权威与亲和：用「我们」替代「我/你们」强化共同体；关键指令用号召式非命令式；结构=开场破冰→主体分层（现状辩证/目标量化/路径责任到人）→结尾升华。',
  '写职工大会领导讲话稿学人人文库「受众分层+我们叙事+三段式」：对基层讲收入/技能/通道、对管理讲效能/荣誉分开写；用「我们车间/我们的目标」替代「你/你们」软化距离；关键指令用号召式（"让我们以零差错标准…"）而非命令；结构走开场共情→主体分层（现状辩证/目标量化/路径到人）→结尾升华。适合 Annual/表彰/攻坚动员全员会，关键「把企业目标翻译成职工的切身利益点」。',
  'https://m.renrendoc.com/paper/499514132.html',
  '③ 领导干部 × 职工（人人文库二手；职工大会讲话稿受众分层，可作领导讲话稿范本）。')

# ---------- ② 上下级 (4) ----------
c2_1 = card('📡', '虚拟 town hall 直播制作·全球可达+省 50% 成本+合规归档', '虚拟直播制作', 'r2', '上下级', 'b2', '二手',
  'webcasting.com.au——虚拟 town hall 直播把全员会从「物理聚集」升级「全球可达」。收益：远程/地区/混合员工都能实时参与提包容；省场地差旅餐费最高 50%；实时投票/审核 Q&A/聊天提参与；开放沟通强信任文化；录制归档用于入职/复盘/合规存证。流程=定制策划→技术彩排→直播日(备份网络+技术驻场)→会后点播。',
  '办虚拟 town hall 学 webcasting「直播+互动+归档」：用专业直播让全球/远程/混合员工同场参与（不止被动听）；实时投票+审核 Q&A+聊天提参与；省场地差旅最高 50%；直播后留点播归档用于新人 onboarding 与合规存证；流程配定制策划+技术彩排+备份网络+技术驻场。适合跨地域集团全员会，关键「把 broadcast 变 dialogue 而非单向宣讲」。',
  'http://webcasting.com.au/town-hall-meetings',
  '② IT/行政 × 全员（webcasting 二手；虚拟 town hall 直播制作，可作跨地域全员会技术范本）。')

c2_2 = card('🚀', 'Town Hall 影响力 4 策略·会前预热+经理翻译+会后跟进', 'Town Hall 影响力', 'r2', '上下级', 'b2', '二手',
  'Oxeon Cross——Town Hall 影响力 4 策略：①会前造期待（提前 2 周征集/投票议题、预览但不剧透、用经理渠道/内网短视频多触点）；②帮中坚经理「翻译」信息（给工具包：关键信息+FAQ+团队化话术+续聊空间）；③跟进承诺（简短 recap 列 3-4 要点+承诺记录+未答问题解答+数周后进度更新）；④把会议当沟通生态一环而非孤立事件。',
  '提升 town hall 影响力学 Oxeon「会前预热+经理翻译+会后跟进」：会前 2 周邀员工提交/投票议题、用经理渠道+内网短视频多触点造期待；给中坚经理工具包（关键信息+FAQ+团队化话术）让他们把公司叙事翻成团队现实；会后发 3-4 点 recap+承诺记录+未答 Q 解答+数周进度更新。适合季度全员会，关键「会议不该在散场时结束，而是沟通生态一环」。',
  'https://oxeancross.com/en/blog/improve-town-hall-impact',
  '② 内部沟通/HR × 全员（Oxeon Cross 二手；Town Hall 影响力 4 策略，可作季度全员会提质范本）。')

c2_3 = card('🛡️', '武装传声筒·变革成败在中间层经理（授权而非转发管道）', '经理赋能变革', 'r2', '上下级', 'b2', '二手',
  'Leadership Story Bank——变革成败在「中间层经理」：员工不从 CEO 听变革，而从直属经理听。但多数组织把经理当「转发管道」而非战略受众——他们和团队同时收到邮件、没时间准备、无 FAQ 工具。解法：给经理早获取信息+允许提问+FAQ/话术工具+处理情绪空间+反馈回路；把经理当变革共创者而非传声筒。',
  '推组织变革学 Leadership Story Bank「武装传声筒」：把一线经理当头号受众而非末端渠道——早给他们信息（别和团队同时收到）、给允许提问的空间、给 FAQ/话术/示例工具包、给处理自身情绪的空间、给向上反馈回路；让经理把信息翻成团队现实而非机械转发。适合涉及结构/角色/薪酬的变革，关键「经理可信，信息才落地；经理漏，信息就碎」。',
  'https://www.leadershipstorybank.com/arming-the-messenger-why-managers-matter-in-change',
  '② HRBP/变革团队 × 经理（Leadership Story Bank 二手；经理是变革最关键受众，可作变革沟通范本）。')

c2_4 = card('🔁', '全员会 3 个范式转移·从议题到效果 / 推送变拉动 / 一刀切变个性化', '全员会范式转移', 'r2', '上下级', 'b2', '二手',
  'Gathering Effect——全员会 3 个范式转移让它「真的有用」：①从议题到效果（先问「会后想让人想/感/做/承诺什么不同」，用效果当筛子砍无关 slide）；②从推送到拉动（给员工角色：追踪主题/写反思/共享收获，用讨论提示/白板共创，以问题开场）；③从一刀切到个性化（会前讲「为何此刻重要」、会后开 after-show 小群复盘、收尾做清晰总结）。',
  '让全员会不沦为「交付机制」学 Gathering Effect「三转移」：从议题→效果（先定会后想让人有何不同，用效果筛议程）；从推送→拉动（给员工角色、用问题开场、共创而非单向宣贯）；从一刀切→个性化（会前讲为何此刻重要、会后开 after-show 小群消化、收尾做清晰总结）。适合常规季度全员会提质，关键「会是为受众设计的，不是为讲者」。',
  'https://www.gatheringeffect.com/insights/threeshifts-makeallhands-work',
  '② 活动/内部沟通 × 全员（Gathering Effect 二手；全员会 3 范式转移，可作常规全员会提质范本）。')

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

# 计数更新：136→140 / 263→267
html = html.replace('    <span class="tag">136 卡</span>', '    <span class="tag">140 卡</span>', 1)
html = html.replace('    <span class="tag">263 卡</span>', '    <span class="tag">267 卡</span>', 1)

# hero 追加本轮段
html = html.replace('三十八轮 enrich 2026-09-08(+8)</p>', '三十八轮 enrich 2026-09-08(+8)｜ 三十九轮 enrich 2026-09-08(+8)</p>', 1)

# 顶部增量页链接 r38→r39
html = html.replace('runs/staff-meeting-2026-09-08-r38.html', 'runs/staff-meeting-2026-09-08-r39.html', 1)

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
  ('新领导首次全员会操盘·目标先行+会前邀员工参与+会后闭环', 'https://www.justworks.com/blog/how-to-run-your-first-all-hands-meeting', 'secondary', 'exec', 'Justworks：首次全员会=团队对齐仪式；定首要目标、会前数周用调研收集员工心声塑议程、用「愿景→部门更新→战果与挑战→Q&A」平衡结构、会后发 recap+收反馈+兑现承诺、指定制片人管时序。'),
  ('变革沟通计划·高管叙事与员工落地分开写+多渠道矩阵', 'https://changeadaptive.com/?p=3978', 'secondary', 'exec', 'Changeadaptive：受众切高管/员工分别写；渠道矩阵 Town Hall+邮件+内网+领导视频+面谈+调研 Q&A；时间线前中后三段；高管讲 Why、经理讲 So-what、专人管渠道。'),
  ('变革期领导沟通·会前会+会后会+故事化+过度沟通', 'https://www.hfma.org/?p=35465', 'secondary', 'exec', 'HFMA(Jill Geisler)：会前先与受信任影响者 1:1 透风、会后会领导走场一对一、把信息当货币宁可过度沟通、用 master narrative 讲真实故事卖变革。'),
  ('职工大会领导讲话稿·受众分层翻译+我们叙事+三段式', 'https://m.renrendoc.com/paper/499514132.html', 'secondary', 'exec', '人人文库：对基层讲收入/技能/通道、对管理讲效能/荣誉分开写；用「我们」替代「我/你们」；号召式指令；结构=开场破冰→主体分层→结尾升华。'),
  ('虚拟 town hall 直播制作·全球可达+省 50% 成本+合规归档', 'http://webcasting.com.au/town-hall-meetings', 'secondary', 'supervisor', 'webcasting：专业直播让全球/远程/混合员工同场参与；实时投票+审核 Q&A+聊天；省场地差旅最高 50%；会后点播归档用于 onboarding 与合规存证。'),
  ('Town Hall 影响力 4 策略·会前预热+经理翻译+会后跟进', 'https://oxeancross.com/en/blog/improve-town-hall-impact', 'secondary', 'supervisor', 'Oxeon Cross：会前 2 周征集/投票议题多触点造期待；给中坚经理工具包翻译信息；会后 recap+承诺记录+未答 Q 解答+数周进度更新。'),
  ('武装传声筒·变革成败在中间层经理（授权而非转发管道）', 'https://www.leadershipstorybank.com/arming-the-messenger-why-managers-matter-in-change', 'secondary', 'supervisor', 'Leadership Story Bank：员工从直属经理听变革；给经理早获取信息+提问空间+FAQ 工具包+情绪空间+反馈回路，当共创者非传声筒。'),
  ('全员会 3 个范式转移·从议题到效果/推送变拉动/一刀切变个性化', 'https://www.gatheringeffect.com/insights/threeshifts-makeallhands-work', 'secondary', 'supervisor', 'Gathering Effect：从议题→效果(用效果筛议程)；从推送→拉动(给员工角色/问题开场/共创)；从一刀切→个性化(会前讲为何此刻重要/会后 after-show 小群/收尾清晰总结)。'),
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
