# -*- coding: utf-8 -*-
# 员工大会 · 第二十七轮补采（r27, 2026-08-26）+8 卡：5 ②上下级 + 3 ③高管间
# 新域：调研后领导力AMA / 全球时区包容 / 沉默英雄即时认可 / 混合式包容性引导 / 领导讲话创意 / 员工大会议程全流程 / 问高管问责跟踪 / 年会会议宴一体
import re, os, json, subprocess, sys, urllib.request, urllib.error

WS = r"C:\Users\v_yitcai\WorkBuddy\20260728154244"
KC = os.path.join(WS, "knowledge-collection")
HTML = os.path.join(KC, "staff-meeting", "staff-meeting.html")
TMP  = os.path.join(KC, "staff-meeting", ".run_newcards.tmp.html")
IDX  = os.path.join(KC, "index.json")
OB_SUM = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\staff-meeting\员工大会-知识卡汇总.md"
OB_IDX = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
OB_RUN = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\staff-meeting\runs\员工大会-2026-08-26-第二十七轮-知识卡.md"
GH = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/staff-meeting.html"
GH_RUN = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/runs/staff-meeting-2026-08-26-r27.html"

cards = [
 dict(emoji='\U0001F4CA', title='调研后领导力 AMA·把敬业度报告变双向对话', cat='调研后AMA',
      rel='r2', src='二手', src_cls='b2',
      url='https://www.specific.app/blog/great-questions-for-leadership-ama-how-to-turn-employee-engagement-survey-results-into-meaningful-conversations-1',
      val='发布敬业度调研结果后员工几乎总有追问；若领导直接翻篇，员工会感到被敷衍。办「调研后领导力 AMA」= 把数据变对话：按 Action Plans（领导者将基于反馈做什么具体改变）/ Clarification（结果中看似矛盾处）/ Timeline & Resources（何时、投什么资源）/ Personal Accountability（领导如何自我问责）四类组织问题；用对话式调研页（conversational survey）让员工自然提交，比表单更易说真话。2024 全球仅 21% 员工真正投入，标准问卷不够，人们渴望诚实双向对话。',
      how='发完敬业度报告别只贴结论。立刻办一场领导力 AMA：把问题按「行动规划 / 澄清 / 时间表资源 / 个人问责」四类组织，提前用对话式工具收集（匿名降低恐惧）；领导当场答「我们会基于反馈做什么具体改变」「谁跟踪进展」，把数据变承诺。让员工感到「被听见」而非「被问卷」。',
      note='② HR/组织者/中层（Specific 二手）；调研后领导力 AMA——把敬业度报告变双向对话，四类问题+对话式收集，信任修复闭环。'),
 dict(emoji='\U0001F30D', title='全球全员会时区包容·轮转时段+异步替代+录播', cat='全球时区',
      rel='r3', src='二手', src_cls='b2',
      url='https://skytime.live/news/how-to-plan-a-meeting-across-time-zones',
      val='跨时区全员会的黄金法则：①轮转不便时段——让不同时区的人轮流扛最差时段，别总让同一区域牺牲；②善用异步——状态更新/周报/FYI 用书面+录屏（Loom）替代 live 会议，跨区真正需要同步的（决策/敏感谈话/团建）才开会；③每月一次全员 live+轮转最差时段；④UTC 写进邀请、用城市名而非固定 UTC 偏移排 recurring（避开 DST 漂移）；⑤文化注意——德/北欧严守边界、日本 punctuality、印度弹性、巴西重关系。多数跨时区会议本不该是会议。',
      how='办全球全员会，先定「轮转最差时段」规则（别总让同一区扛凌晨）；状态/FYI 类用书面+3 分钟录屏替代 live；确需同步的（决策/敏感/团建）才开每月一次 live 并轮转；邀请写 UTC+城市名避 DST 坑；尊重各地会议文化（德北欧守边界、日本准时）。',
      note='③ 跨国高管/全球 HR（Skytime 二手）；全球全员会时区包容——轮转最差时段+异步替代+录播+UTC 城市名+文化注意，跨区不牺牲任何人。'),
 dict(emoji='\U0001F496', title='全员会即时认可·"沉默英雄"互荐 + shout-out 提士气', cat='即时认可',
      rel='r2', src='二手', src_cls='b2',
      url='https://www.wrenly.ai/blog/all-hands-meetings-everything-you-need-to-know',
      val='全员会别只讲业务，要把它当提士气、强文化的场。具体法：①固定节奏+提前邀约（定频成传统，季初发邀请）；②AV 前置排查（别让全员等 10 分钟 Zoom）；③设 moderator 串场（介绍主讲+引导对话）；④互动（实时投票/词云/quiz/脉冲调研）；⑤"Silent Hero"活动——让每人提名「上月为你或团队默默付出的人」，全员会公开 shout-out，比领导独讲更有温度；⑥问「你最骄傲的文化是什么」引发认同。morale 是全员会的隐藏 KPI。',
      how='全员会塞一个「沉默英雄」环节：会前收集每人提名（谁默默帮了你/团队），会上公开 shout-out 这些无名贡献者；配实时投票/词云/quiz 保持互动；设 moderator 控场、AV 提前测。让「被看见」替代「被汇报」，士气才起来。',
      note='② HR/组织者/中层（Wrenly 二手）；全员会即时认可——"沉默英雄"互荐+shout-out+互动工具提士气，morale 是隐藏 KPI。'),
 dict(emoji='\U0001F91D', title='混合式全员会包容性引导·远程优先+杜绝"会后会"+无障碍', cat='混合包容',
      rel='r3', src='二手', src_cls='b2',
      url='https://blog.asa.team/complete-2025-guide-to-hybrid-meetings-setup-inclusive-facilitation-and-troubleshooting/amp',
      val='混合全员会最大坑=远程员工变二等公民。包容性引导清单：①远程优先发言——开场先问「屏幕上的朋友有要说的吗」再叫现场；②杜绝"会后会"——散会后现场人继续聊出的决策/担忧，必须拉回共享频道，否则制造两类员工（有全貌 vs 没有）；③无障碍默认开字幕、关键场次约译员、读关键数字让低视力者不脱节；④轮转时段分担时区负担；⑤AI 纪要作单一真相源（转录+行动项+可搜索）。remote-first 规则从设计上保公平。',
      how='办混合全员会，立「远程优先」铁律：点名顺序先远程后现场；散会后的"会后会"讨论必须回流共享频道（别让远程人第二天才知道）；默认开字幕+关键场约译员；用 AI 纪要作全员可查的单一真相源。把包容写进规范，而非靠自觉。',
      note='③ 高管/IT/HR（ASA Team 2025 指南二手）；混合式全员会包容性——远程优先发言+杜绝会后会+无障碍字幕+AI 单一真相源，别造两类员工。'),
 dict(emoji='\U0001F3A8', title='领导讲话创意·自嘲调侃+行业梗+数据化激励+互动式承诺', cat='讲话创意',
      rel='r3', src='二手', src_cls='b2',
      url='https://m.renrendoc.com/paper/497054098.html',
      val='领导大会讲话创意库：①个人成就分享——讲员工突破难题/晋升蜕变/平衡家庭的具体案例，激发对标；②团队成果可视化——用数据对比（季度绩效/客户满意度）+成员感言视频具象凝聚力；③未来愿景描绘——结合智能化/绿色趋势给前瞻性使命感；④数据化激励——引阶段性成果（客户增长率/项目完成度）设下阶段挑战（"上月超额 20%，这次能否破 30%"）；⑤互动式承诺——全员举手宣誓/电子承诺书强化决心；⑥自嘲式调侃（"我第一次汇报手抖像触电"）+行业梗（IT 调侃"下周需求又要改版本"）+实时投票，拉近距离、幽默收尾。',
      how='领导讲话别只念稿。掺「自嘲+行业梗」破冰拉近距离（"我第一次汇报手抖像触电"）；用「数据对比+成员感言视频」让团队成果可视化；结尾用「数据化挑战+互动式承诺」（举手宣誓/电子签）把听众变参与者；幽默收尾比严肃结尾更让人记住。',
      note='③ 高管/讲话稿撰写（人人文库二手）；领导大会讲话创意——自嘲调侃+行业梗+数据化激励+互动式承诺，拉近距离、强记忆。'),
 dict(emoji='\U0001F4CB', title='员工大会议程全流程·开场致辞→述职→目标责任书→互动提问→分组讨论', cat='议程全流程',
      rel='r2', src='二手', src_cls='b2',
      url='https://mip.renrendoc.com/paper/406813109.html',
      val='标准员工大会议程模板（含时间轴）：①开场主持+总经理开幕辞；②各部门负责人年终述职（每人限时）；③公司未来发展规划（高层解读战略+年度目标分解，部门领目标责任书并承诺）；④互动交流——员工现场提问领导解答+分组讨论"如何贡献目标"、代表分享；⑤大会总结+总经理结束致辞。会前：成立筹备组、统计名单、场地布置（横幅/绿植/音响/签到）、资料准备。把「目标责任书+公开承诺」嵌进大会，让战略从领导独讲变全员认领。',
      how='员工大会按「开幕辞→述职→战略+目标责任书→互动提问+分组讨论→总结闭幕」五段走；关键动作：各部门领「年度目标责任书」并现场承诺，把战略拆成可认领的动作；互动段用「现场提问+分组讨论代表分享」让一线声音进场。会前筹备组+场地+资料三件套别省。',
      note='② HR/行政/中层（人人文库二手）；员工大会议程全流程——开幕辞→述职→战略+目标责任书→互动提问+分组讨论→闭幕，战略变全员认领。'),
 dict(emoji='\U0001F5CA', title='问高管正确姿势·分层问题+区分方向与承诺+跨轮跟踪', cat='提问纪律',
      rel='r2', src='二手', src_cls='b2',
      url='https://www.thequestionvault.com/questions-to-ask-your-ceo-in-a-town-hall',
      val='员工在全员会向 CEO 提问的纪律：①一句话一问、可公开答（问流程/优先级/权衡，别问个人薪酬/具体客户）；②要「一个数字/日期/责任人」——具体目标比价值总结难糊弄；③区分方向与承诺——"我们在看"和"已立项 3 月启动"听着像，只有后者可规划；④跨轮跟踪——连续三次全员会都出现的优先级才是真战略，出现一次就消失的只是张幻灯片；⑤"你最希望今天没人问的问题是什么"只在坦诚文化里用，否则易冷场；⑥会后跟进把承诺变行动。把提问变成问责工具。',
      how='引导员工在全员会问高管「要一个数字/日期/责任人」的具体问题，而非泛泛而谈；教大家区分「方向」与「承诺」（"在看"≠"已立项"）；鼓励做跨轮笔记——连续三次全员会都出现的优先级才是真战略；会后把承诺追成行动。提问是问责，不是表演。',
      note='② 员工/组织者/中层（The Question Vault 二手）；问高管正确姿势——具体可答+区分方向与承诺+跨轮跟踪+会后跟进，把提问变问责工具。'),
 dict(emoji='\U0001F37E', title='年会/员工大会议程·开幕辞+述职+表彰+祝酒（会议宴一体）', cat='年会议程',
      rel='r2', src='二手', src_cls='b2',
      url='https://www.ruiwen.com/cehuafangan/8477423.html',
      val='2025 年会/员工大会议程模板（会议+宴一体）：①全员大会——总经理开幕辞→各负责人年终述职→总经理宣读表彰决定→先进个人/集体领奖+感言+合影；②晚宴——总经理祝酒词→共同举杯→用餐+活动；③全员参与——"每人都要表演"破冰。活动目：总结回顾上一年、部署下一年、表彰先进、增进团结、促进文化。把「表彰」嵌进大会高潮（颁奖背景乐+合影），宴会成为情感连接场（领导与员工零距离、消弭工作矛盾）。会议+宴一体化设计，比纯会议更易凝聚。',
      how='办年会式员工大会，走「开幕辞→述职→表彰（先进领奖+感言+合影）→祝酒宴→全员参与活动」五步；把表彰做成高潮（背景乐+合影），宴会变成领导与员工零距离的情感连接场；设"每人都参与"环节破冰。会议+宴一体，比纯开会更易凝心。',
      note='② HR/行政/中层（瑞文网二手）；年会/员工大会议程——开幕辞+述职+表彰+祝酒宴+全员参与，会议宴一体凝聚，表彰做高潮。'),
]

def card_html(c):
    url_disp = c['url'].replace('https://','').replace('http://','')
    rel_text = '上下级' if c['rel']=='r2' else '高管间'
    return (f'    <div class="hl">\n'
            f'      <div class="top"><span class="emoji">{c["emoji"]}</span><h3>{c["title"]}</h3>'
            f'<span class="cat">{c["cat"]}</span><span class="badge {c["rel"]}">{rel_text}</span>'
            f'<span class="badge {c["src_cls"]}">{c["src"]}</span></div>\n'
            f'      <p class="val">{c["val"]}</p>\n'
            f'      <details class="exec"><summary>怎么做</summary><div class="inner">{c["how"]}</div></details>\n'
            f'      <div class="src">\U0001F517 <a href="{c["url"]}" target="_blank">{url_disp}</a></div>\n'
            f'      <div class="note">适用：{c["note"]}</div>\n'
            f'    </div>')

cards2 = [c for c in cards if c['rel']=='r2']
cards3 = [c for c in cards if c['rel']=='r3']
n2, n3 = len(cards2), len(cards3)
assert n2+n3 == len(cards), (n2,n3,len(cards))
print(f'cards total={len(cards)} | ②={n2} ③={n3}')

# ---------- WALL injection (current wall: sec3 BEFORE sec2, single set each) ----------
html = open(HTML, encoding='utf-8').read()
S3 = html.find('class="sec sec3"')
S2 = html.find('class="sec sec2"')
assert S3 != -1 and S2 != -1 and S3 < S2, 'section headers not found / wrong order'

def grid_close(h, sec_start):
    gi = h.find('<div class="grid">', sec_start)
    assert gi != -1, "grid not found"
    depth = 0; i = gi + len('<div class="grid">')
    while i < len(h):
        if h.startswith('<div', i):
            depth += 1; i = h.find('>', i) + 1
        elif h.startswith('</div>', i):
            if depth == 0: return i
            depth -= 1; i += 5
        else: i += 1
    raise RuntimeError("unbalanced")

def grid_hl(h, sec_start):
    gi = h.find('<div class="grid">', sec_start)
    return h[gi:grid_close(h, sec_start)].count('class="hl"')

cur3 = grid_hl(html, S3)   # ③ grid actual card count (fixes stale tag)
cur2 = grid_hl(html, S2)   # ② grid actual card count
print(f'grid actual before: ②={cur2} ③={cur3}')

# inject ③ into sec3 grid end ; then re-find S2 (index shifted by insertion) ; inject ②
close3 = grid_close(html, S3)
html = html[:close3] + ''.join(card_html(c) for c in cards3) + html[close3:]
S2 = html.find('class="sec sec2"')   # re-find: shifted by sec3 insertion
close2 = grid_close(html, S2)
html = html[:close2] + ''.join(card_html(c) for c in cards2) + html[close2:]

new3 = cur3 + n3
new2 = cur2 + n2

def bump_tag(h, sec_start, new_n):
    seg = h[sec_start:sec_start+400]
    m = re.search(r'<span class="tag">\d+ 卡', seg)
    assert m, 'tag not found'
    return h[:sec_start+m.start()] + f'<span class="tag">{new_n} 卡' + h[sec_start+m.end():]

html = bump_tag(html, S3, new3)
html = bump_tag(html, S2, new2)

# hero: wall was corrupted to "第二十七轮 +11" (bogus); this IS r27, fix count to +8
html = re.sub(r'第二十七轮 \+\d+', '第二十七轮 +8', html, count=1)
assert '本页由 yitong 沉淀整理' in html, 'footer missing'
open(HTML, 'w', encoding='utf-8').write(html)
print(f'OK wall updated: ②={new2} ③={new3} (hl now {html.count(chr(34)+"class=hl"+chr(34))})')

# ---------- .run_newcards.tmp.html ----------
with open(TMP, 'w', encoding='utf-8') as f:
    for c in cards:
        f.write(card_html(c) + '\n')
print(f'OK {TMP} written ({os.path.getsize(TMP)}B)')

# ---------- gen_run_page.py -> runs/staff-meeting-2026-08-26-r27.html ----------
gen = os.path.join(KC, "gen_run_page.py")
RUN_PATH = os.path.join(KC, "staff-meeting", "runs", "staff-meeting-2026-08-26-r27.html")
r = subprocess.run([sys.executable, gen, "--topic", "staff-meeting", "--topic-name",
                    "\u5458\u5de5\u5927\u4f1a", "--date", "2026-08-26", "--round", "27",
                    "--cards-file", TMP, "--out", RUN_PATH], capture_output=True, text=True)
print("gen_run_page:", r.returncode, r.stdout.strip(), (r.stderr.strip()[:200] if r.stderr else ""))
assert r.returncode == 0, "gen_run_page failed"

# ---------- index.json (URL dedup) ----------
idx_data = json.load(open(IDX, encoding='utf-8'))
before = len(idx_data)
existing_urls = {e.get("url","").lower().rstrip("/") for e in idx_data}
added = 0
for c in cards:
    u = c["url"].lower().rstrip("/")
    if u in existing_urls:
        print("SKIP dup url:", u); continue
    idx_data.append({
        'title': c['title'], 'normKey': c['title'], 'url': c['url'],
        'sourceType': 'primary' if c['src']=='一手' else 'secondary',
        'relation': 'supervisor' if c['rel']=='r2' else 'exec',
        'summary': c['val'][:120], 'topic': 'staff-meeting',
    })
    existing_urls.add(u); added += 1
json.dump(idx_data, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'OK index.json {before} -> {len(idx_data)} (+{added})')

# ---------- Obsidian summary note (append 轮次 section) ----------
sum_txt = open(OB_SUM, encoding='utf-8').read()
round_section = (f'\n\n## 轮次 2026-08-26（+{len(cards)}）\n\n'
                 f'| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n')
for c in cards:
    rel = '高管间' if c['rel']=='r3' else '上下级'
    round_section += f'| {c["title"]} | {rel} | {c["src"]} |\n'
sum_txt = sum_txt.rstrip() + '\n' + round_section
open(OB_SUM, 'w', encoding='utf-8').write(sum_txt)
print(f'OK summary note appended (轮次 2026-08-26 +{len(cards)})')

# ---------- Obsidian 00-index (append 8 rows to master table before first "## 主题：") ----------
idx_txt = open(OB_IDX, encoding='utf-8').read()
pos = idx_txt.find('## 主题：')
assert pos != -1, '00-index "## 主题：" not found'
rows = ''.join(
    f'| {c["title"]}（staff-meeting.html） | 4 | {c["src"]} | {"③高管间" if c["rel"]=="r3" else "②上下级"} | {c["cat"]}：{c["val"][:30]} |\n'
    for c in cards)
idx_txt = idx_txt[:pos] + rows + '\n' + idx_txt[pos:]
open(OB_IDX, 'w', encoding='utf-8').write(idx_txt)
print(f'OK 00-index appended +{len(cards)} rows (before first "## 主题：")')

# ---------- Obsidian runs note ----------
os.makedirs(os.path.dirname(OB_RUN), exist_ok=True)
run_md = f'''---
title: 员工大会 第二十七轮知识卡
tags: [知识采集, 员工大会, 自动化采集, 轮次]
date: 2026-08-26
type: 自动化采集
---

# 员工大会 · 第二十七轮补采（2026-08-26）

- 本轮新增 **{len(cards)} 卡**（②上下级 {n2} · ③高管间 {n3}），0 peer（硬约束）
- 一手 0 / 二手 {len(cards)}（本轮源均为媒体/机构二手，公司内部官方一手源稀缺）
- 累计墙：staff-meeting.html（主集 ② {cur2+n2} / ③ {cur3+n3}）+ 当轮独立页
- 新域：调研后领导力AMA / 全球时区包容 / 沉默英雄即时认可 / 混合式包容性引导 / 领导讲话创意 / 员工大会议程全流程 / 问高管问责跟踪 / 年会会议宴一体
- 硬排除：平级/朋友向（①）内容（用户硬约束）；安全HRBP文化知识库源（采集禁令）

## 本轮卡片

| 卡 | 质量分 | 一手/二手 | 适用关系 | 一句话定位 |
|---|---|---|---|---|
'''
for c in cards:
    one = c['note'].split('：',1)[1].rstrip('）。').strip() if '：' in c['note'] else c['note']
    run_md += f'| {c["title"]}（[staff-meeting.html]({GH})） | 4 | {c["src"]} | {"③高管间" if c["rel"]=="r3" else "②上下级"} | {one} |\n'
run_md += f'''
## 链接
- 累计卡片墙：{GH}
- 当轮独立页：{GH_RUN}
- 主题汇总笔记：[[知识采集库/素材/staff-meeting/员工大会-知识卡汇总|员工大会-知识卡汇总]]
'''
open(OB_RUN, 'w', encoding='utf-8').write(run_md)
print(f'OK runs note: {OB_RUN} ({os.path.getsize(OB_RUN)}B)')

print('DONE pipeline core.')

# ---------- GitHub Pages 同步 ----------
sync = os.path.join(WS, "sync_knowledge_github.py")
try:
    rs = subprocess.run([sys.executable, sync], capture_output=True, text=True, timeout=300)
    print("sync_knowledge_github:", rs.returncode, (rs.stdout.strip()[-300:] if rs.stdout else ""), (rs.stderr.strip()[:200] if rs.stderr else ""))
except Exception as e:
    print("\u26a0\ufe0f GitHub 同步异常（告警不阻断）：" + str(e)[:200])

# ---------- 乐享上传（whoami 探活，不依赖连接器状态面板）----------
MCP_JSON = os.path.expanduser("~/.workbuddy/mcp.json")
LEXIANG_URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"
FOLDER = "a753a4ebc526495c9e9b2e2fb3cac314"   # 员工大会子文件夹（待清洗素材下）
WALL_FILE_ID = "a1415122f8034d8d988fb06e41be44ac"
WALL_ENTRY_ID = "f3b5ea59395e49ca859f8726142742c2"
RUN_NAME = os.path.basename(RUN_PATH)  # staff-meeting-2026-08-26-r27.html

class LexiangMCP:
    def __init__(self, token):
        self.token = token; self.session = None
    def _post(self, payload, retries=3):
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(LEXIANG_URL, data=data, method="POST")
        req.add_header("Content-Type", "application/json")
        req.add_header("Accept", "application/json, text/event-stream")
        req.add_header("Authorization", self.token)
        if self.session: req.add_header("Mcp-Session-Id", self.session)
        last = None
        for _ in range(retries):
            try:
                resp = urllib.request.urlopen(req, timeout=120)
                sid = resp.headers.get("mcp-session-id")
                if sid: self.session = sid
                return self._parse(resp.read().decode("utf-8", "replace"))
            except urllib.error.HTTPError as e:
                last = "HTTP {0}: {1}".format(e.code, e.read().decode("utf-8", "replace")[:400]); continue
            except Exception as e:
                last = str(e); continue
        raise RuntimeError("POST fail: " + last)
    def _parse(self, raw):
        raw = raw.strip()
        if raw.startswith("data:"):
            raw = "\n".join(l[5:].strip() for l in raw.splitlines() if l.startswith("data:"))
        try: return json.loads(raw)
        except Exception: return json.loads(raw[raw.find("{"):])
    def initialize(self):
        return self._post({"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"wb-uploader","version":"1.0"}}})
    def initialized(self):
        try: self._post({"jsonrpc":"2.0","method":"notifications/initialized"})
        except Exception: pass
    def call(self, name, args):
        return self._post({"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":name,"arguments":args}})
    def biz(self, resp):
        res = resp.get("result")
        if not res: raise RuntimeError("no result: " + json.dumps(resp, ensure_ascii=False)[:300])
        text = ""
        for c in (res.get("content") or []):
            if c.get("type") == "text": text = c.get("text", ""); break
        try: return json.loads(text)
        except Exception: return {"_raw_text": text}

def put_bytes(url, data, retries=3):
    last = None
    for _ in range(retries):
        try:
            req = urllib.request.Request(url, data=data, method="PUT")
            req.add_header("Content-Type", "text/html")
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.status
        except Exception as e:
            last = str(e); continue
    raise RuntimeError("PUT fail: " + str(last))

try:
    token = json.load(open(MCP_JSON, encoding="utf-8"))["mcpServers"]["lexiang"]["headers"]["Authorization"]
    mc = LexiangMCP(token); mc.initialize(); mc.initialized()
    try:
        w = mc.call("whoami", {})
        print("whoami:", json.dumps(mc.biz(w), ensure_ascii=False)[:120])
    except Exception as e:
        print("whoami 跳过:", str(e)[:120])

    # (a) 更新累计墙文件本体
    wall_bytes = open(HTML, "rb").read()
    r = mc.call("file_apply_upload", {"file_id": WALL_FILE_ID, "parent_entry_id": WALL_ENTRY_ID,
                                      "name": "staff-meeting.html", "extension":"html",
                                      "mime_type":"text/html", "upload_type":"PRE_SIGNED_URL",
                                      "size": str(len(wall_bytes))})
    biz = mc.biz(r)
    if biz.get("code") != 0:
        raise RuntimeError("apply_upload(wall) FAIL {0}".format(biz.get("message")))
    sess = biz["data"]["session"]
    sid = sess.get("session_id") or sess.get("id")
    url = sess.get("upload_url") or sess["objects"][0]["upload_url"]
    st = put_bytes(url, wall_bytes)
    if st != 200: raise RuntimeError("PUT(wall) status " + str(st))
    r2 = mc.call("file_commit_upload", {"session_id": sid})
    biz2 = mc.biz(r2)
    if biz2.get("code") != 0: raise RuntimeError("commit(wall) FAIL " + str(biz2.get("message")))
    print("乐享累计墙已更新 OK")

    # (b) 新建本轮独立页条目
    run_bytes = open(RUN_PATH, "rb").read()
    r = mc.call("file_apply_upload", {"parent_entry_id": FOLDER, "name": RUN_NAME,
                                      "extension":"html", "mime_type":"text/html",
                                      "upload_type":"PRE_SIGNED_URL", "size": str(len(run_bytes))})
    biz = mc.biz(r)
    if biz.get("code") != 0:
        raise RuntimeError("apply_upload(run) FAIL {0}".format(biz.get("message")))
    sess = biz["data"]["session"]
    sid = sess.get("session_id") or sess.get("id")
    url = sess.get("upload_url") or sess["objects"][0]["upload_url"]
    st = put_bytes(url, run_bytes)
    if st != 200: raise RuntimeError("PUT(run) status " + str(st))
    r2 = mc.call("file_commit_upload", {"session_id": sid})
    biz2 = mc.biz(r2)
    if biz2.get("code") != 0: raise RuntimeError("commit(run) FAIL " + str(biz2.get("message")))
    rid = biz2["data"]["entry"]["id"]
    print("乐享新建独立页 OK entry_id=", rid)

    # 回写 lexiang-entry-map.json
    mapf = json.load(open(os.path.join(KC, "lexiang-entry-map.json"), encoding="utf-8"))
    sm = mapf.setdefault("staff-meeting", {"folder_id": FOLDER, "rounds": []})
    sm["folder_id"] = FOLDER
    if "wall" not in sm:
        sm["wall"] = {"entry_id": WALL_ENTRY_ID, "file_id": WALL_FILE_ID, "name": "staff-meeting.html"}
    sm["rounds"].append({"date": "2026-08-26", "entry_id": rid, "name": RUN_NAME,
                         "note": "轮次页 R27 (+8：调研后领导力AMA/全球时区包容/沉默英雄即时认可/混合式包容性引导/领导讲话创意/员工大会议程全流程/问高管问责跟踪/年会会议宴一体·5②3③)"})
    json.dump(mapf, open(os.path.join(KC, "lexiang-entry-map.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("已回写 lexiang-entry-map.json")
except Exception as e:
    print("\u26a0\ufe0f 乐享上传跳过（warning，不中断）：" + str(e)[:300])

# ---------- 推进 last-topic.txt ----------
with open(os.path.join(KC, "last-topic.txt"), "r", encoding="utf-8") as f:
    cur_topic = f.read().strip()
NEXT_TOPIC = "Offsite"
if cur_topic == "\u5458\u5de5\u5927\u4f1a":
    with open(os.path.join(KC, "last-topic.txt"), "w", encoding="utf-8") as f:
        f.write(NEXT_TOPIC + "\n")
    print("last-topic.txt 推进：%s -> %s" % (cur_topic, NEXT_TOPIC))
else:
    print("\u26a0\ufe0f last-topic.txt 当前为「%s」非预期「员工大会」，未自动推进（请人工确认）" % cur_topic)

print("\n=== R27 完成 ===")
