# -*- coding: utf-8 -*-
"""员工大会 R28 累计墙重建 + 当轮新卡生成（先解析既有卡，按关系档重组，干净去污染）。"""
import json, re, os

TOPIC = 'staff-meeting'
WALL = f'knowledge-collection/{TOPIC}/{TOPIC}.html'
DATE = '2026-08-27'
ROUND = 28

# ---------- 1. 解析既有卡 ----------
s = open(WALL, encoding='utf-8').read()

def split_cards(html):
    cards = []
    for m in re.finditer(r'<div class="hl">', html):
        i = m.end(); d = 1; j = i
        while j < len(html):
            if html[j:j+4] == '<div':
                d += 1; j += 4
            elif html[j:j+5] == '</div':
                d -= 1; j += 6
            else:
                j += 1
            if d == 0:
                break
        cards.append(html[m.start():j])
    return cards

all_cards = split_cards(s)
assert len(all_cards) == 295, f'expected 295 got {len(all_cards)}'

def rel_of(c):
    if 'badge r3' in c: return 'r3'
    if 'badge r2' in c: return 'r2'
    return 'r1'

exist_r3 = [c for c in all_cards if rel_of(c) == 'r3']
exist_r2 = [c for c in all_cards if rel_of(c) == 'r2']
print('parsed existing: r3=%d r2=%d total=%d' % (len(exist_r3), len(exist_r2), len(all_cards)))

# ---------- 2. 定义当轮 15 张新卡 ----------
def card(emoji, title, cat, rel, val, how, url, note):
    relname = '高管间' if rel == 'r3' else '上下级'
    display = url.replace('https://', '').replace('http://', '')
    return f'''<div class="hl">
      <div class="top"><span class="emoji">{emoji}</span><h3>{title}</h3><span class="cat">{cat}</span><span class="badge {rel}">{relname}</span><span class="badge b2">二手</span></div>
      <p class="val">{val}</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">{how}</div></details>
      <div class="src">🔗 <a href="{url}" target="_blank">{display}</a></div>
      <div class="note">适用：{note}</div>
    </div>'''

NEW = []

# ===== ③ 高管间（exec）6 张 =====
NEW.append(card('👔', 'CEO 在不确定时期的全员会该说什么·致辞内容范式', '高管致辞', 'r3',
  '演讲机构提炼 CEO 在动荡/不确定时期 town hall 应传递的核心：先承认不确定性而非粉饰，明确"我们在面对什么"，给出可执行的下一步与承诺，区分"已知/未知"，避免空洞打气；用具体故事替代口号，让全员感到被托住而非被忽悠。',
  '高管在全员会开篇先直面现实（"今年很难，我知道"），再讲清三件事——我们现在在哪、为什么、你作为一员能做什么/我作为 CEO 承诺什么；把"我不知道但会告诉你"当作信任杠杆；结尾落到具体可验证的承诺而非愿景口号。',
  'https://chartwellspeakers.com/what-should-a-ceo-say-at-a-company-town-hall-in-uncertain-times/',
  '③ 高管在业绩承压/组织变动/外部环境不确定时的全员会致辞内容框架（坦诚优先于粉饰）。'))

NEW.append(card('🤝', '用全员会（Town Hall）加固团队信任·CEO 信任杠杆', '信任建设', 'r3',
  '高管教练文章：Town Hall 是建立信任最高效的定期场景——当 CEO 现身、认真答问、承认未知、兑现跟进，信任随轮次累积；反之"只读稿/早退/不答难题"会一次性透支。把信任拆成"可见+可靠+可亲"三要素给出打法。',
  '把 town hall 当信任账户：每场固定"CEO 亲自开场+留足真 Q&A+会后 48h 内公开未答问题答案"三动作；用"我也在学/我也担心"式脆弱表达拉近，但配具体行动避免显得表演；连续 3-4 场稳定兑现，信任曲线才会上扬。',
  'https://jennyreilly.com/town-halls-strengthen-teams-trust/',
  '③ 高管把周期性全员会设计成"信任累积机制"而非信息广播（关系资产视角）。'))

NEW.append(card('💬', '办一场真正"连得起来"的全员会·高管主持心法', '高管主持', 'r3',
  '产品团队从"连接"维度重构 town hall：传统模式是高管单向播报、员工被动接收；真正连接的做法是——开场抛一个全员关心的问题、把大量时间留给双向对话、用真实客户/员工故事替代数据罗列、高管主动下场答问并承认盲点。',
  '高管主持时先问"大家这周最在意什么"类开放问题暖场；议程以"故事+对话"为主而非"汇报+PPT"；安排 1-2 个一线员工真实案例上场；结尾高管亲自回答 3 个最尖锐的预征集问题，展示"我听进去了"。',
  'https://zohocloud.ca/connect/the-collective/how-to-run-town-hall-meetings-that-truly-connect.html',
  '③ 高管亲自主持/站台全员会时，从"播报"转向"连接"的主持框架。'))

NEW.append(card('📡', '远程环境下高管 Town Hall 沟通最佳实践', '远程沟通', 'r3',
  '声誉机构针对远程/混合办公总结高管 town hall 沟通要点：物理距离放大信任缺口，需更主动的透明（提前发议程+会后发纪要）、更刻意的互动设计（投票/分组讨论）、更一致的语调；高管不能"发了直播就完事"，要管理异步时段的信息公平。',
  '远程全员会要做到"三提前"（议程/材料/提问通道提前 24h）、"一公平"（异地与现场同权提问、同屏可见）、"全闭环"（纪要+未答问题跟进覆盖所有时区）；高管出镜稳定、语速放缓、多用具体例子对抗屏幕疏离感。',
  'https://therepuationagency.com.au/insights-and-news/best-practices-for-executive-town-hall-communications-in-remote-work-environments/',
  '③ 多地域/远程团队的高管全员会沟通（信息公平与异步闭环）。'))

NEW.append(card('🎯', '把 CEO 沟通变成真实员工参与·多位高管教练的范式转向', '沟通转型', 'r3',
  'Forbes Coaches Council 多位高管教练共识：员工 disconnect 往往不是频率问题而是"播报 vs 共创"问题。给出一系列可落地的领导沟通转向——从倡导到探询、从传达 what 到讲清 so what、从广播更新到共同意义建构、每场固定一问并 7 天内闭环。',
  '高管把全员会语言从"我宣布"改成"我邀请"：每场用一句"这对你意味着什么"收尾；把 survey 数据直接搬进 town hall 展示真实关切；设"7 天闭环"规则——会上提的问题 7 天内必回；用"我也在纠结/我学到什么"式个人化表达替代官方辞令。',
  'https://forbes.com/councils/forbescoachescouncil/2026/02/26/how-to-turn-ceo-communications-into-meaningful-employee-engagement',
  '③ 高管/HR 负责人把全员会从"信息推送"重构为"双向意义共建"（高层沟通治理）。'))

NEW.append(card('🎥', '直播全员会·现场 Live Q&A 平滑运行制片指南', '直播Q&A', 'r3',
  '活动制片团队基于真实直播经验总结：直播全员会的信任在 Q&A 环节被建立或摧毁。给出可执行的直播 Q&A 制片框架——问题如何采集（预征集+现场）、谁主持、留多少时间、平台功能（结构化提交+审核队列+投票+同权）、主讲人如何备答。',
  '直播全员会 Q&A 三件套——① 预征集降低风险并暴露真问题；② 设独立 moderator（绝不与主讲人合一）过滤/分组/控时；③ 主讲人答前复述问题（照顾远端）、答不上来就承诺日期。平台至少支持"结构化提交+审核+投票+现场/远端同权"，纯聊天框不适合高管场。',
  'https://jasperpictures.com.au/blog/how-to-run-a-smooth-live-qa-during-company-town-hall-streams',
  '③ 大型直播/混合全员会的高管 Q&A 制片与主持分工（现场可信度刚需）。'))

# ===== ② 上下级（supervisor）9 张 =====
NEW.append(card('🎤', '下次全员会现代剧本·目标/节奏/角色/互动全设计', '全员会策划', 'r2',
  '内部沟通工具方给出全员会现代 playbook：先定"北极星目标"（对齐/文化/连接三选一），据此砍掉不搭的议程；按受众分层讲（技术看成就、支持看客户影响、销售看市场）；月/季节奏+45-60 分钟尊重时间；设主持人/主讲/Q&A facilitator 三角色；会前造势、会中互动、会后延续成连续对话。',
  'HR/中层办全员会先写一句北极星目标再排议程；配"主持(MC)+主讲+Q&A facilitator"三角色分工（facilitator 专管问题排序，避免难题被淹没）；用 Slack/Teams 投票让群众投票定话题增加参与感；会前 leader 录 30 秒 teaser，会中 Slido/Mentimeter 实时提问+投票，会后发纪要+未答跟进。',
  'https://weekblast.com/blog/all-employee-meeting',
  '② 内部沟通/HR 从零策划一场全员会的通用剧本（目标先行+三角色+三段互动）。'))

NEW.append(card('✅', '改进全员会的 7 个实操点·透明/远程/反馈', '互动提质', 'r2',
  '绩效平台总结 7 个改进全员会的可执行点：充分准备（议程+视觉化指标+计时员）、按需换格式（让 emerging leaders 上台）、精简 Q&A（提前征集渠道）、透明真实（难题 100% 坦诚）、不漏远程（同权提问+录播）、会后立即收反馈、保持固定节奏。',
  '办全员会设"计时员"控场；CEO 每次必讲但给新锐 leader 露脸机会；Q&A 提前开征集通道产出高质量题；最难的问题也要 100% 透明答（躲=透支信任）；远程同权+录播；散会即发 1 题 pulse 调研；固定月/季节奏让员工有预期。',
  'https://reflektive.com/blog/improving-company-meeting-2',
  '② HR/中层提升全员会质量的 7 条清单（透明、远程同权、即时反馈）。'))

NEW.append(card('📋', '企业全员会（Town Hall）全流程最佳实践·筹备到跟进', '全流程SOP', 'r2',
  '综合指南给出 town hall 完整 SOP：筹备（定目的/排故事线议程/提前征集员工问题并投票/选平台测设备/教练领导）、会中（开场定调/心理安全欢迎批判性问题/领导更新+员工故事+Q&A/互动）、跟进（纪要+未答公开+调研）。强调"把议程当故事讲"而非 KPI 罗列。',
  '按"欢迎+战略主题→领导更新(5-7min)→客户/员工故事→Q&A 互动→表彰仪式"排故事线；用 Slido/表单提前征集并让员工投票选出 top 问题；会前教练领导"平衡事实与情绪、承认失败、讲人话"；会中设心理安全准则、欢迎尖锐问题；会后 48h 内发纪要+公开所有 Q&A（含未答）。',
  'https://communityciviccampus.net/town-hall-meeting-in-corporate',
  '② HR/行政从筹备到跟进跑通一场 town hall 的标准动作清单。'))

NEW.append(card('🎯', '办一场员工"真想去"的全员会·把最关心的事放最前', '形式设计', 'r2',
  '场地团队角度：没人想参加"又一个强制会"，除非内容值得。核心打法——把员工最在乎的那件事（方向/大消息/新项目）放开场而非 20 分钟 housekeeping 之后；让不同声音上台（项目负责人/新人/一线短讲）改变节奏；用投票/匿名/分组打破"只有敢说的人发声"；会后给对话留物理空间（茶歇/酒会）。',
  '排议程先问"员工散会后会对同事说哪句"就把那刻放前面；单个演讲≤一个清晰信息、换人即换节奏；Q&A 预征集+匿名+投票，留足时间认真答难题；场地选"最差座位也看得见听得清"的；正式环节后安排非正式聚集让同事/领导自然聊。',
  'https://kewgardens.venuecrew.com/article/planning-a-town-hall-people-actually-want-to-attend',
  '② 中层/HR 用"内容优先+多元声音+会后对话空间"提升全员会出席意愿。'))

NEW.append(card('⚠️', '全员会最该避开的 6 件事·主持人与会后闭环', '避坑清单', 'r2',
  '互动工具方列全员会 6 大雷区与正解：避免信息倾倒/无互动/无主持/超时/只高管讲/会后即忘。给出对应做法——开场用互动破冰、设友好 facilitator（不必是 CEO）、把最想说的放前、留 15-20min Q&A、会后发纪要+补答未答问题。',
  '全员会设独立 host 控场控时、让安静声音也被听见；用 Mentimeter 类工具开场先互动让后续 Q&A 更自然；开头就抛核心消息而非暖场铺垫；Q&A 至少留 15-20min；"离开会议"按钮后连接不停——发含 slides 的友好 summary，没答完的 Questions 在跟进里补答。',
  'https://mentimeter.com/es-ES/blog/great-leadership/6-things-to-avoid-in-your-all-hands-meeting',
  '② HR/中层办全员会的避坑清单（主持、互动、会后闭环）。'))

NEW.append(card('📊', '用实时投票+结构化 Q&A 跑通 60 分钟全员会·含样例议程', '实时投票', 'r2',
  '投票工具方给出"用匿名投票戳破公开沉默"的具体方案与一份 60 分钟样例议程：开场前发通道与首题；开场 pulse 测基线并坦诚面对不舒服的数据；中段 check-in 投票动态调整后续；Q&A 用"提交+投票排序"的 ranked queue 替代开放麦；结尾 word cloud 收情绪；会后导出全量问题公开未答。',
  '按样例跑——会前 2min 发通道+首题；开场 3min 亮开场匿名投票结果并诚实回应（哪怕数据难看）；宣讲 20min；中段 2min 投票"哪块想多讲"实时调；Q&A 25min 走 top-upvoted ranked queue（匿名+ moderator 去重）；结尾 5min word cloud；会后导出问题清单公开未答——这一条本身就建信任。',
  'https://pollqr.com/blog/live-polling-employee-town-halls',
  '② HR/中层用实时投票+结构化 Q&A 把"沉默的大多数"变成可见信号（含可直接抄的 60min 议程）。'))

NEW.append(card('🤐', '为什么传统全员会 Q&A 失灵·匿名参与的心理学与 2-4 倍提效', '匿名提问', 'r2',
  '匿名 Q&A 工具方用数据戳破传统 Q&A：仅 27% 员工在全员会问出真问题，举手/麦克风让大多数人因"社交与职业风险"沉默，且提问者偏高管层。匿名把参与率拉高 2-4 倍、问题更具体、基层声音获得与高管同等权重；前提是"架构级匿名"（连主办方都看不到是谁）。',
  '办全员会 Q&A 用架构级匿名通道（不是挂名 Google Form/Slido 后台可溯源）；会前 24-48h 开匿名提交窗口让员工想清楚并互相点赞；现场按热度排 queue；匿名让基层敢问"裁员/薪酬公平/战略方向"级真问题，投票让集体关切浮到顶部——比谁抢到麦民主得多。',
  'https://hushworknow.com/blog/how-to-run-live-anonymous-qa-session',
  '② HR/中层用"真匿名"撬动全员会真话（参与率与问题质量的机制解释）。'))

NEW.append(card('💡', '职工大会互动提问环节怎么排·互动工具方实操建议', '互动工具', 'r2',
  '国内互动（淘气互动）工具方针对职工大会/全员会给出互动提问环节落地建议：用扫码/小程序让全员手机端实时提问与点赞排序，避免"举麦只敢问软问题"；支持匿名降低顾虑；现场大屏实时滚动问题与热度，主持人按热度抽取回答；会后可导出全部问题留痕跟进。',
  '国内办职工大会/全员会，用扫码互动把"提问"搬到手机——全员匿名或实名提交、互相点赞排热度、大屏实时滚动；主持人不靠举麦而按热度抽题，基层真问题（薪酬/加班/战略）才能冒头；会后导出问题清单做跟进闭环，比传统举麦民主且可追溯。',
  'https://cms.taoqihudong.com/cms/news/2296.html',
  '② 国内语境职工大会/全员会的手机端互动提问落地（扫码+匿名+热度排序+大屏）。'))

NEW.append(card('🗂️', '全员会标准议程模板·60 分钟时间盒与分工', '议程模板', 'r2',
  '项目管理工具方给出可直接套用的全员会议程模板与时间盒：开场(5min 欢迎+今日主题)→领导战略更新(10min)→部门/团队亮点(15min)→客户或员工故事(5min)→实时投票/互动(5min)→Q&A(15min)→收尾与行动项(5min)；附"谁来讲/讲什么/限时"分工表与准备清单。',
  '拿 60min 模板直接排：开场 5min 定调、领导战略更新 10min（讲结论+意义非念稿）、团队亮点 15min（让 1-2 个团队讲故事）、客户/员工故事 5min、实时投票 5min、Q&A 15min（独立 facilitator 管）、收尾 5min 明确行动项与负责人；会前发 agenda+准备清单，设计时员。',
  'https://monday.com/blog/project-management/meeting-agenda-template',
  '② HR/中层需要"拿来即用"的全员会议程时间盒与分工模板。'))

# ---------- 3. 写当轮新卡临时文件（供 gen_run_page 模式A） ----------
tmp = f'knowledge-collection/{TOPIC}/.run_newcards.tmp.html'
open(tmp, 'w', encoding='utf-8').write('\n'.join(NEW))
new_r3 = [c for c in NEW if rel_of(c) == 'r3']
new_r2 = [c for c in NEW if rel_of(c) == 'r2']
print('new cards: r3=%d r2=%d total=%d' % (len(new_r3), len(new_r2), len(NEW)))

# ---------- 4. 重建累计墙 ----------
sec3_start = s.find('<div class="sec sec3">')
preamble = s[:sec3_start]
footer = s[s.rfind('<footer>'):]

# 更新 hero 行 + 增量页链接
preamble = preamble.replace('采集于 2026-08-26（第二十七轮 +11）',
                            f'采集于 {DATE}（第二十八轮 +{len(NEW)}）')
preamble = preamble.replace('href="staff-meeting-20260826.html"',
                            'href="runs/staff-meeting-2026-08-27-r28.html"')

all_r3 = exist_r3 + new_r3
all_r2 = exist_r2 + new_r2

def sec_block(cls, label, count, cards):
    cards_html = '\n'.join(cards)
    return f'''  <div class="sec {cls}">
    <h2>{label}</h2>
    <span class="tag">{count} 卡</span>
  </div>
  <div class="grid">
{cards_html}
  </div>
'''

body = (sec_block('sec3', '③ 领导↔领导（高管间 · exec）', len(all_r3), all_r3)
        + sec_block('sec2', '② 领导↔员工（上下级 · supervisor）', len(all_r2), all_r2))

new_wall = preamble + body + footer
open(WALL, 'w', encoding='utf-8').write(new_wall)
print('WALL written: r3=%d r2=%d total=%d bytes=%d' % (len(all_r3), len(all_r2), len(all_r3)+len(all_r2), len(new_wall)))

# ---------- 5. 追加 index.json ----------
idx = json.load(open('knowledge-collection/index.json', encoding='utf-8'))
def add_entry(title, url, sourceType, relation, summary):
    norm = re.sub(r'^https?://', '', url).lower()
    norm = re.sub(r'^www\.', '', norm).rstrip('/')
    for x in idx:
        u = x.get('url','')
        n = re.sub(r'^https?://','',u).lower()
        n = re.sub(r'^www\.','',n).rstrip('/')
        if n == norm:
            return False
    idx.append({'title': title, 'normKey': title, 'url': url,
                'sourceType': sourceType, 'relation': relation, 'summary': summary,
                'topic': TOPIC})
    return True

meta = [
 ('CEO 在不确定时期的全员会该说什么·致辞内容范式','https://chartwellspeakers.com/what-should-a-ceo-say-at-a-company-town-hall-in-uncertain-times/','secondary','exec','不确定时期 CEO 全员会致辞：坦诚优先于粉饰，先承认现实再给可执行下一步与承诺'),
 ('用全员会（Town Hall）加固团队信任·CEO 信任杠杆','https://jennyreilly.com/town-halls-strengthen-teams-trust/','secondary','exec','把 town hall 当信任账户：CEO 现身+真 Q&A+48h 内公开未答，连续兑现累积信任'),
 ('办一场真正"连得起来"的全员会·高管主持心法','https://zohocloud.ca/connect/the-collective/how-to-run-town-hall-meetings-that-truly-connect.html','secondary','exec','高管主持从播报转向连接：开放问题暖场+故事对话+一线案例+亲答尖锐题'),
 ('远程环境下高管 Town Hall 沟通最佳实践','https://therepuationagency.com.au/insights-and-news/best-practices-for-executive-town-hall-communications-in-remote-work-environments/','secondary','exec','远程全员会三提前一公平全闭环：异地现场同权提问+异步信息公平'),
 ('把 CEO 沟通变成真实员工参与·多位高管教练的范式转向','https://forbes.com/councils/forbescoachescouncil/2026/02/26/how-to-turn-ceo-communications-into-meaningful-employee-engagement','secondary','exec','Forbes 教练共识：从播报转共创，每场一问+7 天闭环+个人化表达'),
 ('直播全员会·现场 Live Q&A 平滑运行制片指南','https://jasperpictures.com.au/blog/how-to-run-a-smooth-live-qa-during-company-town-hall-streams','secondary','exec','直播 Q&A 制片：预征集+独立 moderator+复述问题+结构化提交投票同权'),
 ('下次全员会现代剧本·目标/节奏/角色/互动全设计','https://weekblast.com/blog/all-employee-meeting','secondary','supervisor','全员会现代 playbook：北极星目标先行+三角色分工+三段互动'),
 ('改进全员会的 7 个实操点·透明/远程/反馈','https://reflektive.com/blog/improving-company-meeting-2','secondary','supervisor','改进全员会 7 点：计时员+新锐露脸+提前征集 Q&A+100% 透明+远程同权'),
 ('企业全员会（Town Hall）全流程最佳实践·筹备到跟进','https://communityciviccampus.net/town-hall-meeting-in-corporate','secondary','supervisor','town hall 完整 SOP：筹备故事线+心理安全+会后 48h 公开所有 Q&A'),
 ('办一场员工"真想去"的全员会·把最关心的事放最前','https://kewgardens.venuecrew.com/article/planning-a-town-hall-people-actually-want-to-attend','secondary','supervisor','提升出席意愿：内容优先+多元声音上台+会后对话空间'),
 ('全员会最该避开的 6 件事·主持人与会后闭环','https://mentimeter.com/es-ES/blog/great-leadership/6-things-to-avoid-in-your-all-hands-meeting','secondary','supervisor','全员会避坑：独立 host+开场互动+核心消息前置+15-20min Q&A+会后闭环'),
 ('用实时投票+结构化 Q&A 跑通 60 分钟全员会·含样例议程','https://pollqr.com/blog/live-polling-employee-town-halls','secondary','supervisor','匿名投票戳破沉默+60min 样例议程+ranked queue Q&A+会后导出未答'),
 ('为什么传统全员会 Q&A 失灵·匿名参与的心理学与 2-4 倍提效','https://hushworknow.com/blog/how-to-run-live-anonymous-qa-session','secondary','supervisor','仅 27% 问真问题；架构级匿名把参与率拉高 2-4 倍、基层声音获同等权重'),
 ('职工大会互动提问环节怎么排·互动工具方实操建议','https://cms.taoqihudong.com/cms/news/2296.html','secondary','supervisor','国内职工大会手机端互动：扫码提问+匿名+热度排序+大屏滚动+会后留痕'),
 ('全员会标准议程模板·60 分钟时间盒与分工','https://monday.com/blog/project-management/meeting-agenda-template','secondary','supervisor','拿来即用的 60min 全员会议程时间盒与分工模板'),
]
added = 0
for t,u,st,rel,summ in meta:
    if add_entry(t,u,st,rel,summ):
        added += 1
json.dump(idx, open('knowledge-collection/index.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
print('index.json added=%d total=%d' % (added, len(idx)))
