# -*- coding: utf-8 -*-
import re, os

BASE = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(BASE, 'icebreaker', 'icebreaker.html')
TMP = os.path.join(BASE, 'icebreaker', '.run_newcards.tmp.html')

def card(emoji, title, cat, rel_badge, rel_label, src_badge, val, how, src, note):
    disp = src.replace('https://', '').replace('http://', '')
    return f'''    <div class="hl">
      <div class="top"><span class="emoji">{emoji}</span><h3>{title}</h3><span class="cat">{cat}</span><span class="badge {rel_badge}">{rel_label}</span><span class="badge {src_badge}">二手</span></div>
      <p class="val">{val}</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">{how}</div></details>
      <div class="src">🔗 <a href="{src}" target="_blank">{disp}</a></div>
      <div class="note">适用：{note}</div>
    </div>
'''

# ③ 高管间 (exec) — 2 cards
c_exec = [
card('🧠', '高管务虚开场活动库（连接与对齐升级）', '活动库', 'r3', '高管间', 'b2',
 'Offsite（团建务虚 SaaS）整理的高管/领导会议开场活动库——Compliment Circle（轮流给同伴正向反馈）、CI: The Crime Investigators（解谜协作）、Barter Puzzle（谈判式拼图交易）、Chat Waterfall（全员同时发答案的惊喜感）、Emoji Check-In（表情打卡情绪温度）、Your Amazing Future（结对谈十年愿景）。把破冰从「尴尬游戏」升级成有目的的连接/对齐动作，并可接虚拟版（Theme Song / Virtual Background / One Word at a Time）。',
 '领导务虚/Retreat 开场选 1-2 个低门槛活动定调（Compliment Circle 建信任、Emoji Check-In 测情绪温度）；把活动与本次会议目标挂钩（战略对齐用 Your Amazing Future、协作用 Barter Puzzle）；虚拟场次用 Chat Waterfall / One Word at a Time 保全员参与；活动后 5min debrief 把感受连回工作议题。',
 'https://www.offsite.com/blog/leadership-activities-teams',
 '③ 高管务虚/Retreat 开场活动库——Compliment Circle/CI/Barter Puzzle/Chat Waterfall/Emoji Check-In 等把破冰升级成有目的的连接与对齐动作，可接虚拟版；活动与会议目标挂钩+5min debrief 连回议题（高管间，活动库二手）。'),
card('🗺️', '领导力静修 10 步全程规划（含 48h 复盘+KPI）', '规划框架', 'r3', '高管间', 'b2',
 'Offsite 的领导力静修（Retreat）10 步规划法——从目标/KPI 定义→破冰开场→技能工作坊（情商/演讲/决策）→团队建设（寻宝/烹饪赛/户外）→社区参与（公益）→健康正念→晚间社交→技术「断电」模拟环节→物流清单（交通/住宿/餐饮/AV/引导师分设）→48h 匿名复盘+KPI 追踪（决策速度/跨职能沟通/士气 30·60 天）。把一次性活动变成「绩效周期起点」而非孤岛事件。',
 '先定成功标准再选活动；Day1 下午或晚间做社区参与/公益作自然团建；多日静修至少排 1 个无屏幕模拟环节（更深焦点）；物流协调与引导师分设两人（别混）；离开后 2 周检查点回顾承诺、后续例会引用决议；用专业策划师补内部短板。',
 'https://www.offsite.com/leadership-retreats',
 '③ 领导力静修（Retreat）全程规划——10 步从目标/KPI→破冰→工作坊→团建→公益→健康→社交→技术断电→物流分设→48h 匿名复盘+30/60 天 KPI 追踪，把一次性活动变成绩效周期起点（高管间，规划框架二手）。'),
]

# ② 上下级 (supervisor) — 5 cards
c_sup = [
card('📖', '个人历史练习 Personal Histories（心理安全基石·HBR）', '心理安全', 'r2', '上下级', 'b2',
 'Harvard Business Review 引用的经典练习 Personal Histories——每人分享 2-3 段个人生命故事（在哪长大、一个热爱、一次转折），小组内 15-30 分钟轮流讲。把同事从「职位」还原成「人」，是建立心理安全与信赖的低成本高杠杆动作；比硬编码团建游戏更不尴尬、更易持续。',
 '新团队/跨职能组前 30min 做——提前给提示（成长地/热爱的事/一次失败），4-6 人小组轮流讲、只倾听不点评；领导先讲自己的（示弱定调）；接 Rose & Thorn（本周一玫瑰一刺）日常化；可季度复做加深。',
 'https://giveriver.com/blog/team-bonding-exercise-ultimate-guide',
 '② 新组建/跨职能团队建立心理安全与信赖——Personal Histories（每人讲 2-3 段人生故事把同事还原成「人」）是 HBR 引用的心理安全基石，30min 低门槛不尴尬可持续，领导先示弱定调（上下级，破冰方法二手）。'),
card('🎭', '跨部门即兴工作坊「Yes, and」信任构建', '信任构建', 'r2', '上下级', 'b2',
 '即兴戏剧核心原则「Yes, and」（先接住对方再叠加）被用作跨部门信任构建工具——无脚本无安全网，逼人实时倾听、真诚回应、互相托底。跨部门同事首次真正协作时，这套心态直接迁移成更开放、更协作的工作关系；比强制娱乐团建更落地。',
 '邀引导师带 60-90min 即兴工作坊，混编财务/市场/运营/HR 等不同部门；从简单「Yes, and」传球开始，进阶双人情景共创；强调「不否定只叠加」；结束 debrief 把练习心态映射到真实跨部门项目；领导参与时同样平等不特权。',
 'https://boomforbusiness.nl/blog/7-team-building-activities-that-strengthen-trust-between-departments',
 '② 跨部门信任构建——即兴工作坊「Yes, and」（先接住再叠加）逼人实时倾听互相托底，混编部门无脚本协作，心态迁移真实跨部门项目；领导平等参与不特权（上下级，信任构建二手）。'),
card('🔄', '岗位互换日 + 午餐轮盘（零预算拆孤岛）', '拆孤岛', 'r2', '上下级', 'b2',
 '两个低门槛、可制度化的跨部门连接法——①Lunch Roulette：系统随机配对不同部门员工共进午餐（配话题卡），把「认识彼此角色」变成轻松日常；②Department Swap Day：员工志愿去另一部门跟岗一整天，亲眼看 workflows、问问题、搭把手，建立同理心与跨职能理解。都无需预算、可季度固定。',
 'Lunch Roulette 用表单/工具随机配对+给 3 个开场问题（「你部门最被误解的一点？」）；Swap Day 按兴趣/相关性配对、提前对齐 host、当天只观察+轻协助、结束短会分享「我学到什么、怎么看全盘」；两法都可季度化做成文化基础设施而非一次性。',
 'https://teambuildingworld.com/interdepartmental-team-activities/',
 '② 跨部门日常连接（零预算可制度化）——Lunch Roulette 随机配对午餐+话题卡、Department Swap Day 跟岗一整天建同理心，都季度固定成文化基础设施；领导可视参与（上下级，拆孤岛二手）。'),
card('🧩', '按隔阂类型匹配协作活动格式（选型框架）', '选型框架', 'r2', '上下级', 'b2',
 '拆孤岛不靠「随便玩」，而靠「按隔阂类型匹配活动格式」——沟通慢用 Giant Jenga 快决策挑战暴露瓶颈；部门争影响力用 Horse Racing 共识游戏练统一决策；互不了解 workflows 用 Scavenger Hunt 共创解题建同理；全组织协弱用公司级 quiz/多活动项目一次重置互动模式。并把协作活动当行为改变催化剂而非孤岛事件。',
 '先诊断「我们到底卡在哪类隔阂」再选格式；活动后 debrief 抓洞察、链接到真实项目；季度复做+轮换组队+高管可见参与；把产出（共识/地图/清单）接回实际工作，避免「玩完就忘」。',
 'https://www.thebigsmokeevents.com/?p=4437/',
 '② 跨部门协作活动选型框架——按隔阂类型匹配格式（沟通慢→Giant Jenga/争影响力→Horse Racing/不了解流程→Scavenger Hunt/全组织→公司级 quiz），活动当行为改变催化剂+季度复做+高管可见（上下级，选型框架二手）。'),
card('🍳', '跨部门协作 5 类活动菜单（2026·含时长/人数/单价）', '活动菜单', 'r2', '上下级', 'b2',
 '2026 年跨部门协作 5 类可落地活动菜单（含时长/人数/单价）——①协作烹饪赛（3h/10-50 人/$75，隐喻职场协作）②逃生舱解谜（1.5h/6-12 人/$30，压力下的跨部门沟通）③户外探险课（4h/15-100 人/$100，自然里削层级）④公益共建（3-5h/20-100 人/$50，为共同善协作）⑤创新黑客松（1-2 天/30-150 人/$150，跨职能共创）。研究称聚焦团建的组织跨部门沟通 +25%。',
 '按预算/人数/远程与否选型（远程优先逃生舱虚拟版/黑客松虚拟版）；烹饪赛/户外提前 2 月订场；公益提前 3 月对接机构；黑客松备食宿保能量；关键不是玩得开心而是「产出可迁移」——每活动配 debrief 把协作洞察接回工作。',
 'https://learn.offsiteio.com/team-building-activities/5-team-building-activities-that-maximize-cross-department-collaboration-in-2026',
 '② 跨部门协作活动菜单（2026·含时长/人数/单价）——烹饪赛/逃生舱/户外课/公益共建/黑客松五类，按预算人数远程与否选型、配 debrief 把洞察接回工作；远程优先虚拟版（上下级，活动菜单二手）。'),
]

# write tmp file (run cards, order: exec first then sup to mirror gen_run_page grouping)
with open(TMP, 'w', encoding='utf-8') as f:
    f.write(''.join(c_exec) + ''.join(c_sup))
print('TMP written, cards=', len(c_exec) + len(c_sup))

# --- update wall ---
html = open(WALL, encoding='utf-8').read()

def insert_into_grid(html, grid_index, blocks):
    """Insert blocks before the matching close of the grid_index-th <div class="grid"> (0-based)."""
    positions = [m.start() for m in re.finditer(r'<div class="grid">', html)]
    pos = positions[grid_index]
    # bracket match from pos
    i = pos + len('<div class="grid">')
    d = 1
    j = i
    while j < len(html):
        if html[j:j+4] == '<div':
            d += 1; j += 4
        elif html[j:j+6] == '</div>':
            d -= 1; j += 6
        else:
            j += 1
        if d == 0:
            break
    # j is at the char after the matching </div>; insert blocks before that </div>
    close_start = j - 6
    return html[:close_start] + ''.join(blocks) + html[close_start:]

# sec3 grid is first grid (index 0), sec2 grid is second (index 1)
html = insert_into_grid(html, 0, c_exec)
html = insert_into_grid(html, 1, c_sup)

# hero update
hero_seg = '｜ 三十四轮补采 +7（2026-09-07）：个人历史练习(心理安全·HBR)/跨部门即兴「Yes,and」信任/岗位互换日+午餐轮盘/按隔阂类型匹配协作格式/跨部门5类活动菜单（②）；高管务修开场活动库/领导力静修10步规划（③）'
# append inside the hero <p>...</p> (the first <p> after hero h1)
m = re.search(r'(<div class="hero">.*?<h1>.*?</h1>\s*<p>)(.*?)(</p>)', html, re.S)
if m:
    new_p = m.group(1) + m.group(2) + hero_seg + m.group(3)
    html = html[:m.start()] + new_p + html[m.end():]
else:
    print('WARN hero not updated')

open(WALL, 'w', encoding='utf-8').write(html)
print('WALL updated. hl count =', html.count('class="hl"'))
