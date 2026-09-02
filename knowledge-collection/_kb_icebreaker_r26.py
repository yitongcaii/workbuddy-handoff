# -*- coding: utf-8 -*-
"""破冰 r26 (2026-09-02) 渲染脚本：累计墙注入 + index.json 落库 + 独立页生成。"""
import json, os, re, subprocess, sys

KC = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(KC, 'icebreaker', 'icebreaker.html')
TMP = os.path.join(KC, 'icebreaker', '.run_newcards.tmp.html')
IDX = os.path.join(KC, 'index.json')
GEN = os.path.join(KC, 'gen_run_page.py')
DATE = '2026-09-02'
ROUND = 26
TOPIC = 'icebreaker'
TOPIC_NAME = '破冰'

# ---------- 6 张新卡 HTML 块 ----------
cards_html = {
'r3': [
'''    <div class="hl">
      <div class="top"><span class="emoji">🔥</span><h3>高管/董事会务虚·pre-mortem + unconference + 战争推演 + 48 小时规则</h3><span class="cat">高管务虚设计</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
      <p class="val">高管务虚会要当「战略仪器」而非团建。6 个真正建联结的活动（忘掉尴尬破冰）：①pre-mortem——「3 年后大 initiative 惨败，写历史」，释放异议、暴露隐性风险，比硬推更早发现坑；②unconference/open space——议程由参与者到场共创，谁都能抛真关心的话题，浮出「房间里的大象」；③fireside chat——主持式访谈一位高管/董事讲领导历程、失败与教训（非主旨演讲）；④simulation/war gaming——分组扮公司与最狠对手互相攻防，暴露战略盲点又建同袍情；⑤guided solitude——1 小时独处反思再分享，平衡主导发言者、让内向思考者深贡献；⑥外部引导师——CEO/主席别自己 facilitate（否则无法全参与、权力动态失衡），花钱请外人问「蠢问题」、控冲突。48 小时规则：会后 48h 内发决策+owner+期限摘要，否则 momentum 死；3 个月后董事会复盘「我们说要做的，做了吗」。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">高管务虚用 pre-mortem(3年后惨败写历史)+unconference(议程共创)+fireside chat(讲失败)+war gaming(分饰对手)+guided solitude(独处);聘外部引导师;48h 内发决策/owner/期限,3 月后复盘。</div></details>
      <div class="src">🔗 <a href="https://hayatkhabar.com/leadership-retreats-that-work-aligning-strategy-beyond-the-boardroom/" target="_blank">hayatkhabar.com/leadership-retreats-that-work-aligning-strategy-beyond-the-boardroom</a></div>
      <div class="note">适用：③ 高管/董事会务虚——pre-mortem+unconference+fireside chat+war gaming+guided solitude+外部引导师+48 小时规则（高管间，商务化战略仪器，非游戏，二手）。</div>
    </div>''',
'''    <div class="hl">
      <div class="top"><span class="emoji">🏛️</span><h3>企业务虚对董事会/管理层的价值·首日非工作活动 + DiSC + 外部引导师（澳董事学会）</h3><span class="cat">企业务虚价值</span><span class="badge r3">高管间</span><span class="badge b1">一手</span></div>
      <p class="val">澳大利亚董事学会(AICD)引多位 chair/CEO 谈企业务虚：把董事会/管理层从日常干扰中隔离、投入战略，决策质量更高；务虚「头一天」刻意安排与内容无关的活动（帆船/探险/海岸远征），逼大脑离开业务模式、变开放，更易接纳异见——「要到第二天中午才走出自己脑子」。关键配方：①平衡价值(离岗新视角 vs 随时在线压力)；②目标对齐(先定目的、团队共建议程、问团队要 input、备强人预案)；③DiSC 等测评破人际壁垒、建关系；④fireside chat/团队晚宴在非正式空间深聊；⑤志愿/公益建意义与同袍；⑥外部引导师「懂组织、能把工作交还」董事，让其被指派、被赋能、被问责。频率：私企每年两次两天务虚最佳，越频越成「团队」而非散人。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">企业务虚请董事/高管离岗、首日排非工作活动(逼大脑离业务);用 DiSC 破人际壁垒;fireside chat/晚宴深聊;聘外部引导师「把工作交还」董事(被指派+问责);私企每年两次两天最佳。</div></details>
      <div class="src">🔗 <a href="https://www.aicd.com.au/organisational-culture/business-ethics/the-power-of-corporate-retreats-in-strengthening-culure" target="_blank">aicd.com.au/.../the-power-of-corporate-retreats-in-strengthening-culure</a></div>
      <div class="note">适用：③ 董事会/高管务虚——澳董事学会官方谈务虚价值：首日非工作活动+DiSC+fireside chat+外部引导师(把工作交还董事)+年两次两天，离岗新视角→更好决策（高管间/治理层，行业机构官方内容=一手）。</div>
    </div>''',
],
'r2': [
'''    <div class="hl">
      <div class="top"><span class="emoji">📊</span><h3>Google re:Work 团队效能五动态·心理安全为首 + 管理者落地动作（一手工具包）</h3><span class="cat">团队效能工具包</span><span class="badge r2">上下级</span><span class="badge b1">一手</span></div>
      <p class="val">Google Project Aristotle 两年研究 180+ 团队，结论：谁在团队里不如团队如何运作重要；第一大驱动是心理安全。re:Work 官方工具包给出 5 大团队效能动态——①心理安全（敢冒险/出错/提难问题不担责）；②依赖度（角色责任清晰、计划透明）；③结构与清晰（目标沟通+议程+OKR）；④意义（对杰出工作公开感谢+帮人）；⑤影响（共创愿景让每人知工作如何贡献用户/组织）。管理者落地动作：建立共同词汇（定义团队行为规范）、创论坛谈团队动力学（HRBP/引导师）、拉领导承诺持续改进；具体：solicit input、分享工作风格偏好、看 Amy Edmondson 心理安全 TED、澄清角色、公开感谢。这是团队建设/破冰的「底层操作系统」——先有安全与清晰，游戏才有效。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">用 re:Work「5 动态」诊断团队短板（心理安全/依赖/清晰/意义/影响）；管理者每周做三件小事：solicit input+分享自身工作风格+公开具体感谢；把「团队规范」写成一页共同词汇，每季度回看。先安全后活动。</div></details>
      <div class="src">🔗 <a href="https://rework.withgoogle.com/intl/en/guides/understand-team-effectiveness" target="_blank">rework.withgoogle.com/intl/en/guides/understand-team-effectiveness</a></div>
      <div class="note">适用：② 经理↔团队——Google re:Work 官方 Project Aristotle 工具包，5 大团队效能动态（心理安全为首）+ 管理者落地三动作（共同词汇/论坛/领导承诺），作为破冰与团队建设的底层操作系统（上下级，工具官方文档=一手）。</div>
    </div>''',
'''    <div class="hl">
      <div class="top"><span class="emoji">🌐</span><h3>跨文化全球团队·用「团队规范共创」替代破冰游戏 + 开放式提问重构（HBR）</h3><span class="cat">跨文化团队</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">BU Questrom 借 HBR 案例讲全球/跨文化团队建信任：传统「信任建设活动」往往不持久（bonding 没留住）。更稳的做法是 co-create 团队规范——让团队一起定行为准则，且要显式包容（不默认主导文化偏好）：如「任何产品发布 campaign 须 6 周内至少在 3 个市场测试」，平衡速度与严谨。提问方式决定心理安全：把封闭「有任何问题吗」（诱导沉默）改成开放「我们有什么担心」（暗示问题本就该被提出）；把「遇到挑战吗」改成「刚熬过艰难季度，我想听你的挑战」——把分享困难正常化、变预期。研究显示过度强调差异反而伤知识共享，须用文化智能+视角采择（想象他人动机而非共情）保持聚焦共同目标。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">跨文化/异地团队别靠一次性破冰游戏；带团队 co-create 3-5 条行为规范（显式包容、平衡两类优先级）；把封闭提问重构为开放（「有什么担心」而非「有问题吗」）；用视角采择保持聚焦任务。</div></details>
      <div class="src">🔗 <a href="https://www.bu.edu/questrom/blog/hbr-leading-global-teams-effectively" target="_blank">bu.edu/questrom/blog/hbr-leading-global-teams-effectively</a></div>
      <div class="note">适用：② 经理↔跨文化/异地团队——用「团队规范共创」替代无效破冰游戏 + 开放式提问重构（把沉默诱导改为困难正常化）+ 文化智能/视角采择（上下级，HBR 案例复盘，二手）。</div>
    </div>''',
'''    <div class="hl">
      <div class="top"><span class="emoji">🛠️</span><h3>新经理团队建设·非正式仪式 + 零预算 + 远程三板斧（真正管用）</h3><span class="cat">新经理团队建设</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">多数团队建设建议错在「重活动轻日常」。新经理真正管用的做法：①非正式仪式（团队自生、非 HR 强推）——周一咖啡闲聊(15min 不谈工作)/周五 wins&fails(每人 1 胜 1 败)/help-needed 看板(谁卡谁发、他人自愿帮)/新员工传统(首周有人带吃午饭+给「真实团队指南」)/内部梗；关键是持续+自愿，别脚本化。②零预算——lunch-and-learn(带话题带饭)/步行 1:1(肩并肩比面对面更敢说)/技能互换(设计师跟开发 shadow)/一起志愿。③远程——虚拟咖啡随机配对(15min 非工作)/摄像头文化(鼓励不强制)/异步庆祝频道/一年 1-2 次线下留社交空档。最被低估的真相：每天做的（开好会/诚实反馈/说到做到/真关心人）比任何季度活动重要千倍。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">新经理别先排活动；先立 1-2 个轻仪式(咖啡/wins&fails/help-needed 看板)看哪个粘住；零预算用步行 1:1+技能互换+志愿；远程用虚拟咖啡+异步庆祝+年度线下；保护空间别脚本。</div></details>
      <div class="src">🔗 <a href="https://firsttimemanagers.com/articles/building-team-trust/team-building-for-new-managers" target="_blank">firsttimemanagers.com/articles/building-team-trust/team-building-for-new-managers</a></div>
      <div class="note">适用：② 新经理↔团队——非正式仪式(周一咖啡/周五 wins&fails/help-needed 看板)+零预算(步行1:1/技能互换/志愿)+远程三板斧(虚拟咖啡/异步庆祝/年度线下)，重日常轻活动（上下级，新经理实战，二手）。</div>
    </div>''',
'''    <div class="hl">
      <div class="top"><span class="emoji">📅</span><h3>新经理 90 天科学剧本·听→对齐→共创共赢 + 首日建心理安全</h3><span class="cat">新经理90天</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">科学背书的新经理 90 天：D1-30 听（1:1 每人、别急着改）；D31-60 对齐——书面锁定与老板的 top3 季度产出+「好」长啥样（口头的会漂、书面的不漂）、设运营节奏(周1:1/周 huddle/月复盘)、把期望落到团队与个人；D61-90 落地一个「共同胜仗」——拉团队进解法、功劳共享，追个人英雄的新经理容易滑向微管、蚀信任。底层从第一天建心理安全：①示弱（「我没有所有答案，需要你帮定优先级」给全员 permission 做凡人）；②把首个错误当对你的测试（好奇「发生什么/学到什么」而非 blame，全队在看）；③主动邀异议（决策讨论结尾问「谁看法不同」并谢发声者）；④快速复盘 AAR(预期/实际/下次不同)。引用 Gallup(「知道期望」最强敬业预测之一)+Edmondson 心理安全。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">90 天分三段：听→书面对齐(锁 top3+节奏)→共创共享胜仗(非个人英雄)；从 Day1 用四信号建心理安全：示弱/把错当测试/邀异议/快速 AAR。</div></details>
      <div class="src">🔗 <a href="https://www.scienceofpeople.com/first-90-days-as-a-manager" target="_blank">scienceofpeople.com/first-90-days-as-a-manager</a></div>
      <div class="note">适用：② 新经理↔团队——科学背书 90 天(听→书面对齐→共创共享胜仗)+ 首日心理安全四信号(示弱/把错当测试/邀异议/AAR)，引用 Gallup+Edmondson（上下级，二手·研究综述）。</div>
    </div>''',
]
}

all_cards = cards_html['r3'] + cards_html['r2']

# ---------- index.json 条目 ----------
def norm(u):
    u = u.strip().lower()
    u = re.sub(r'^https?://', '', u)
    u = re.sub(r'^www\.', '', u)
    u = u.split('#')[0].rstrip('/')
    return u

def mknorm(title):
    return re.sub(r'\s+|·|、|，|,', '', title)

idx_entries = [
    {"title":"Google re:Work 团队效能五动态·心理安全为首 + 管理者落地动作（一手工具包）",
     "url":"https://rework.withgoogle.com/intl/en/guides/understand-team-effectiveness",
     "sourceType":"primary","relation":"supervisor","topic":TOPIC,
     "summary":"Google Project Aristotle 两年研究 180+ 团队：谁在团队不如团队如何运作，第一大驱动是心理安全。re:Work 官方工具包给 5 大效能动态(心理安全/依赖/结构与清晰/意义/影响)+管理者落地三动作(共同词汇/论坛谈团队动力学/领导承诺持续改进)。作为破冰与团队建设的底层操作系统。"},
    {"title":"跨文化全球团队·用「团队规范共创」替代破冰游戏 + 开放式提问重构（HBR）",
     "url":"https://www.bu.edu/questrom/blog/hbr-leading-global-teams-effectively",
     "sourceType":"secondary","relation":"supervisor","topic":TOPIC,
     "summary":"BU Questrom 借 HBR 案例：传统信任建设活动不持久，改用 co-create 团队规范(显式包容、平衡速度与严谨)；把封闭提问「有任何问题吗」重构为开放「我们有什么担心」，把分享困难正常化；用文化智能+视角采择保持聚焦共同目标。"},
    {"title":"新经理团队建设·非正式仪式 + 零预算 + 远程三板斧（真正管用）",
     "url":"https://firsttimemanagers.com/articles/building-team-trust/team-building-for-new-managers",
     "sourceType":"secondary","relation":"supervisor","topic":TOPIC,
     "summary":"新经理管用的团队建设重日常轻活动：非正式仪式(周一咖啡/周五 wins&fails/help-needed 看板/新员工传统/内部梗，持续+自愿)；零预算(步行1:1/技能互换/志愿)；远程(虚拟咖啡/异步庆祝/年度线下)。每天做的比季度活动重要千倍。"},
    {"title":"新经理 90 天科学剧本·听→对齐→共创共赢 + 首日建心理安全",
     "url":"https://www.scienceofpeople.com/first-90-days-as-a-manager",
     "sourceType":"secondary","relation":"supervisor","topic":TOPIC,
     "summary":"科学背书新经理 90 天：D1-30 听；D31-60 书面对齐(top3 产出+运营节奏)；D61-90 共创共享胜仗(非个人英雄)。首日建心理安全四信号：示弱/把首个错误当测试/主动邀异议/快速 AAR。引用 Gallup+Edmondson。"},
    {"title":"高管/董事会务虚·pre-mortem + unconference + 战争推演 + 48 小时规则",
     "url":"https://hayatkhabar.com/leadership-retreats-that-work-aligning-strategy-beyond-the-boardroom/",
     "sourceType":"secondary","relation":"exec","topic":TOPIC,
     "summary":"高管务虚当战略仪器：pre-mortem(3年后惨败写历史释放异议)、unconference(议程共创浮出大象)、fireside chat(讲失败)、war gaming(分饰对手)、guided solitude(独处)、外部引导师(CEO 别自 facilitate)；48h 内发决策/owner/期限，3 月后复盘。"},
    {"title":"企业务虚对董事会/管理层的价值·首日非工作活动 + DiSC + 外部引导师（澳董事学会）",
     "url":"https://www.aicd.com.au/organisational-culture/business-ethics/the-power-of-corporate-retreats-in-strengthening-culure",
     "sourceType":"primary","relation":"exec","topic":TOPIC,
     "summary":"澳董事学会(AICD)官方：企业务虚离岗新视角→更好决策；首日排非工作活动逼大脑离业务；DiSC 破人际壁垒；fireside chat/晚宴深聊；外部引导师把工作交还董事(被指派+问责)；私企每年两次两天最佳。"},
]
for e in idx_entries:
    e['normKey'] = mknorm(e['title'])

# ---------- 1) 累计墙注入 ----------
html = open(WALL, encoding='utf-8').read()

def insert_after_grid(html, sec_class, blocks):
    m = re.search(r'<div class="sec %s">' % sec_class, html)
    if not m:
        raise RuntimeError('section %s not found' % sec_class)
    g = html.find('<div class="grid">', m.end())
    if g < 0:
        raise RuntimeError('grid for %s not found' % sec_class)
    # insert right after the opening <div class="grid">
    insert_pos = g + len('<div class="grid">')
    html = html[:insert_pos] + '\n' + '\n'.join(blocks) + '\n' + html[insert_pos:]
    return html

html = insert_after_grid(html, 'sec3', cards_html['r3'])
html = insert_after_grid(html, 'sec2', cards_html['r2'])

# 更新 sec3 / sec2 卡片计数
html = html.replace('<div class="sec sec3"><h2>③ 领导↔领导（高管间 · exec）</h2><span class="tag">92 卡</span>',
                    '<div class="sec sec3"><h2>③ 领导↔领导（高管间 · exec）</h2><span class="tag">94 卡</span>')
html = html.replace('<div class="sec sec2"><h2>② 领导↔员工（上下级 · supervisor）</h2><span class="tag">147 卡</span>',
                    '<div class="sec sec2"><h2>② 领导↔员工（上下级 · supervisor）</h2><span class="tag">151 卡</span>')

# hero 追加本轮说明
roundNote = (' ｜ 二十六轮补采 +6（2026-09-02）：Google re:Work 团队效能五动态(心理安全为首·一手工具包)/'
             '跨文化全球团队规范共创+开放式提问重构(BU Questrom·HBR)/新经理团队建设非正式仪式+零预算+远程三板斧('
             'FirstTimeManagers)/新经理 90 天科学剧本+首日心理安全四信号(Science of People)/高管务虚 pre-mortem+'
             'unconference+war gaming+48h 规则(hayatkhabar)/企业务虚价值 首日非工作活动+DiSC+外部引导师(澳董事学会·一手)')
html = html.replace('</p>\n    <div class="relbar">', roundNote + '</p>\n    <div class="relbar">')

open(WALL, 'w', encoding='utf-8').write(html)
print('WALL updated: sec3+%d sec2+%d' % (len(cards_html['r3']), len(cards_html['r2'])))

# ---------- 2) 临时新卡文件 ----------
open(TMP, 'w', encoding='utf-8').write('\n'.join(all_cards))
print('TMP written: %d cards' % len(all_cards))

# ---------- 3) index.json 去重 + 落库 ----------
data = json.load(open(IDX, encoding='utf-8'))
existing = set(norm(x.get('url','')) for x in data)
new_n = 0
dup_m = 0
for e in idx_entries:
    if norm(e['url']) in existing:
        dup_m += 1
        print('DUP skip:', e['url'])
    else:
        data.append(e)
        existing.add(norm(e['url']))
        new_n += 1
json.dump(data, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('INDEX: total=%d new=%d dup=%d' % (len(data), new_n, dup_m))

print('NEW=%d DUP=%d' % (new_n, dup_m))
