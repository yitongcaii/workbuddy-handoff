# -*- coding: utf-8 -*-
# 员工大会 · 第二十六轮补采（r26, 2026-08-25）+8 卡：5 ②上下级 + 3 ③高管间
# 新域：会后行动项闭环 / 一线吐槽会闭环 / 圆桌问政(三真原则) / 安全主讲(听众变主讲) / 降本坦诚(不裁员全员共创) / CEO说不知道 / CEO个人反馈嵌战略 / 变革叙事三阶
import re, os, json, subprocess, sys, urllib.request, urllib.error

WS = r"C:\Users\v_yitcai\WorkBuddy\20260728154244"
KC = os.path.join(WS, "knowledge-collection")
HTML = os.path.join(KC, "staff-meeting", "staff-meeting.html")
TMP  = os.path.join(KC, "staff-meeting", ".run_newcards.tmp.html")
IDX  = os.path.join(KC, "index.json")
OB_SUM = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\staff-meeting\员工大会-知识卡汇总.md"
OB_IDX = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
OB_RUN = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\staff-meeting\runs\员工大会-2026-08-25-第二十六轮-知识卡.md"
GH = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/staff-meeting.html"
GH_RUN = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/runs/staff-meeting-2026-08-25-r26.html"

cards = [
 dict(emoji='\U0001F4D2', title='会后行动项追踪闭环·责任人制+流程联动+周期复盘', cat='会后闭环',
      rel='r2', src='二手', src_cls='b2',
      url='https://landian.cq.cn/content.aspx?p=3102',
      val='会议纪要/行动项把「说过的话」变「做成的事」三法：①责任人制——每项行动项明确跟进人，每次会议先 review 上次纪要进展，责任人从被动接受到主动推动；②纪要+流程联动——用系统把行动项直接生成任务流（分配+提醒+周期），管理者实时看进度；③周期性复盘——每两周复盘障碍/难推进项，模糊行动项拆细到一周内可完成。本质是把会议结论变成可追踪任务流，不靠「已读」兜底。',
      how='全员会散会≠结束。会后立即出结构化纪要（决策/行动项[责任人+时限+交付物]/待决项），24h 内分发；用飞书任务/多维表格把行动项变成带逾期提醒的任务流、责任到人；下次会议首项=review 上次行动项进展；每两周小复盘把模糊项拆细。让「开过会」真正「落了地」。',
      note='② 行政/PMO/会议组织者（landian 博客二手）；责任人制+流程联动+周期复盘三法，把全员会行动项变成可追踪任务流、下次会先 review 进展。'),
 dict(emoji='\U0001F4AC', title='一线员工「吐槽会」闭环·倾听-反馈-解决-关怀', cat='一线恳谈',
      rel='r2', src='二手', src_cls='b2',
      url='https://m.dzplus.dzng.com/share/general/0/NEWS3575438SDXLBNTXVFOIN',
      val='胜利油田供水分公司东城水务项目部「员工吐槽会」——无客套、只谈心声：老员工提「食堂想吃点现蒸粗粮」、技术员提「报表系统不兼容重复录入」。以「书记谈话日+吐槽会」为载体，建「倾听—反馈—解决—关怀」闭环：基层干部现场听、逐条记；问题清单化、闭环式落实；王师傅健康食谱诉求 3 天落实（窝窝头红薯上桌），小曲报表痛点半月实现「一次录入多端共享」；今年收集 23 条办结 20 条，暂未解决的例会给进度说明+合理解释。配 EAP 心理疏导多维发力，吐槽泄压、建言聚力。',
      how='办一线员工吐槽会，别搞成汇报会。定「不追责、只解决」基调，让员工敞开提工作心声/急难愁盼；基层干部现场听、逐条记；问题清单化、闭环式落实，能快的极速办（健康食谱 3 天、报表半月），暂不能办的在例会给明确进度+合理解释；配 EAP 疏情绪。让「带着问题来、满载舒心回」成常态。',
      note='② 基层管理者/工会/HR（大众新闻·胜利油田一手案例二手）；吐槽会「倾听-反馈-解决-关怀」闭环+清单化极速落实+3 天响应，一线减压赋能。'),
 dict(emoji='\U0001FAC1', title='圆桌问政/听政问政会·一线职工坐议事席(三真原则)', cat='一线问政',
      rel='r2', src='二手', src_cls='b2',
      url='https://www.163.com/dy/article/KN1Q80D905568W0A.html',
      val='中国二十二冶装配式分公司年度听政问政会——一张圆桌模糊职级界限，31 名一线职工代表与公司领导班子围桌，围绕企业发展/技术创新/薪酬福利/人才晋升等十大方面提 54 项具体问题，现场逐一回应。工会「三真原则」：说真话不受责、提真问题不遮掩、求真解决不敷衍。自 2021 年累计提意见建议 381 条，落实率与反馈满意度始终保持 100%。职工感慨「以前觉得管理是领导的事，现在普通职工也能参与决策了」。工会角色从权益维护向创新发动者深化，2025 年梳理申报职工创新成果 7 项获集团级以上荣誉、创效逾百万。',
      how='把「听政问政会」做成一线职工坐上议事席的真实问政：圆桌消职级感，一线代表围绕经营/技术/薪酬/晋升提具体问题，领导班子现场逐一回应；立「三真原则」（说真话不受责、提真问题不遮掩、求真解决不敷衍）；建议建账、限时办结、100% 反馈；工会从「维权」转向「创新发动」，把一线智慧系统梳理成成果。让职工从「被动听」变「参与决策」。',
      note='② 工会/基层管理者/HR（中工网·中国二十二冶一手案例二手）；圆桌问政+三真原则+100% 落实率，一线职工参与决策、工会转创新发动者。'),
 dict(emoji='\u26D1\uFE0F', title='安全主题全员会「听众变主讲」·一线员工从听众变主讲人', cat='安全文化',
      rel='r2', src='二手', src_cls='b2',
      url='http://www.ntwenming.com/content/2026-05/04/content_36814900.htm',
      val='江苏祥源电气把安全教育从「一人讲、众人听」改成「今天我主讲」轮值制——每位员工不论资历，至少在班组安全活动中当一次主讲人，讲风险点/规程解读/未遂事件复盘；配「风险大家找」无指责原则征集（反馈只防风险不处罚），一线「金点子」印成《岗位常见风险警示汇编》，员工见自己建议变「正式教材」归属感飙升；南通文明网案例。本质是把一线员工从被动听众变成主动安全主讲人，用「身边人讲身边事」替代空洞说教。',
      how='安全主题全员会/班前会，别只让安全员念文件。推「今天我主讲」轮值：每人至少讲一次（风险点/规程/未遂事件复盘）；设「风险大家找」无指责原则（提隐患不处罚、只防风险），把一线金点子印成风险警示汇编；用「身边人讲身边事」替代说教，员工因讲者是朝夕同事更易共鸣。听众变主讲人，安全文化才入心。',
      note='② 安全管理部门/班组长/HR（南通文明网二手）；「今天我主讲」轮值+无指责隐患征集+身边人讲身边事，一线员工从安全听众变主讲人。'),
 dict(emoji='\U0001F4A1', title='降本增效压力下的全员会坦诚沟通·不裁员目标+全员提方案', cat='经营坦诚',
      rel='r2', src='二手', src_cls='b2',
      url='https://www.carnegie.com.tw/media-coverage.php?ORDER=16',
      val='卡内基案例：2008 金融海啸一大陆台商公司订单减四成、总部令降本 15%，总经理不开除式砍人，而是开全员会坦诚讲困境+总部要求，诉诸崇高动机——「同舟共济、一位员工都不裁」；各部门用卡内基法开创新会议，基层提 232 个降本方案、106 个立案执行，工程师改闲置旧设备省下 345 万（原需 360 万买 3 台新设备），最终达标且零裁员，温家宝总理特地参访。证明经营压力下，坦诚沟通+崇高动机+全员共创，比冷酷裁员更能破局。',
      how='经营下行要开全员会，别遮掩也别只甩「降本指标」。总经理/CEO 先坦诚讲真实困境与总部要求（Fact），再诉崇高动机——「一位员工都不裁」「同舟共济」；把降本变成全员创新命题，用结构化会议收集一线方案（232 提 106 立），工程师改闲置设备省大钱；用「不裁员+全员共创」替代裁员恐慌。坦诚+目标感，比冷酷砍人更能稳住军心。',
      note='② 总经理/CEO/HR（卡内基训练媒体二手）；经营压力全员会坦诚讲困境+不裁员目标+全员提降本方案（232 提 106 立、零裁员），替代裁员恐慌。'),
 dict(emoji='\U0001F48F', title='CEO 说「我不知道」·radical honesty 全员会', cat='诚实沟通',
      rel='r3', src='二手', src_cls='b2',
      url='https://avantage-ta.com/the-power-of-radical-honesty-in-modern-business',
      val='Berlin 某 85 人 B2B HR SaaS 公司产品转型遇阻、营收持平，新任 CEO 不开战略发布会，而是办两小时无 PPT「State of the Company」——live、无稿、直说哪些成了/哪些明显没成/哪些真还不知道，邀请提问并直接答甚至关于 runway 与 timeline 的尖锐问题。结果非但没恐慌，三周内三名私下面试的资深工程师撤回申请，客服因有了诚实话术（含不确定性）客户沟通大幅改善，转型加速。数据：高信任透明职场生产率 +72%、离职 -50%、满意度 +56%、敬业 +76%；员工强烈信任领导者的比例是 4 倍敬业、58% 更低离职意向。',
      how='全员会遇不确定，CEO 别用漂亮话管理信息。试一次无 PPT、无稿的「State of the Company」：直说成了什么、明显没成什么、真还不知道什么；邀请并直接答尖锐问题（含 runway/timeline）。诚实哪怕含不确定，给员工具体可回应之事，比沉默/模糊更聚人。多数「诚实会引发恐慌」的恐惧是被证伪的——不确定无上下文才制造恐慌。',
      note='③ CEO/高管（avantage-ta 咨询二手）；radical honesty 全员会——无 PPT 两小时直说「不知道」、答尖锐问题，诚实沟通带来 +72% 生产率/4 倍敬业，替代裁员恐慌。'),
 dict(emoji='\U0001F5A7', title='CEO 把个人反馈嵌进战略宣讲·modeling vulnerability', cat='领导示弱',
      rel='r3', src='二手', src_cls='b2',
      url='https://mitsloanindia.com/article/were-doing-ceo-feedback-wrong/',
      val='MIT Sloan 案例：一 CEO（John）经历 360 反馈后，没单独开「自我改进秀」，而是在全员大会战略宣讲中，把「个人正在改的 3 条反馈」与「公司 3 大战略优先级」并列展示在一张 slide 上，每条反馈链到具体战略目标。「我想让大家知道，反馈不只关于你，更是我们如何更好支持业务」。研究支持：把绩效目标连到业务优先级助公司达战略。modeling vulnerability 给团队授权——人们反应极好，因领导先示弱、团队才敢说真话。可从「只跟 2-3 人分享」起步降风险。',
      how='高管做全员会，别只讲战略不露自己。把「自己正在改的个人反馈」嵌进战略宣讲 slide，与公司战略优先级并列、每条链到具体目标——「反馈不只关于你，更是我们怎么更好支持业务」。这等于领导先示弱、团队才敢说真话（modeling vulnerability）。怕尬可从只跟 2-3 人分享起步；研究证员工强烈信任领导=4 倍敬业。',
      note='③ CEO/高管（MIT Sloan Management Review 二手）；把个人 360 反馈嵌进全员会战略宣讲、与战略优先级并列，modeling vulnerability 给团队授权说真话。'),
 dict(emoji='\U0001F504', title='变革叙事 Town Hall·连续性+直视问题+变革理由(HBR)', cat='变革沟通',
      rel='r3', src='二手', src_cls='b2',
      url='https://nplus.wiki/hbr-guide-to-leading-through-change/docs/03-communicating-change/03-storytelling-bold-change',
      val='HBR 变革沟通叙事三阶：①肯定过往美好的部分——员工最怕「未来公司不再是认同的那家」，同时强调连续性(continuity)效果最好；案例 Uber 新 CEO Dara 首场 town hall 不指向过去失误、不扮救世主，而是承诺「保留让 Uber 成为自然之力的锋芒」，掌声雷动。②直视不美好的部分——若已失信任需重建，兼具乐观(更好明天信念)+诚实(对过去错误负全责、承认对人代价)；案例 Riot Games 官网极直白道歉。③提明确有说服力的变革理由——中段最像失败(Kanter 定律)，须给坚实理由让人继续走。案例 Domino’s「Pizza Turnaround」直面「送到后你还得吃它」的难吃真相。',
      how='变革期办全员会，叙事按三阶：①先肯定+强调连续性——别只讲要改的，先说「哪些不变」，消员工「公司不再是认同的那家」的恐惧（Uber Dara 承诺保留锋芒）；②直视问题——已失信任就兼乐观+诚实，对过去错误负全责（Riot 直白道歉）；③给坚实变革理由——中段最像失败，必须让人知道「为什么值得继续走」（Domino’s 直面难吃真相再反转）。叙事对了，变革才推得动。',
      note='③ CEO/高管/变革负责人（HBR 指南二手）；变革期 Town Hall 叙事三阶——连续性(Uber Dara)/直视问题(Riot)/变革理由(Domino’s)，消恐惧、重建信任、给理由。'),
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

html = open(HTML, encoding='utf-8').read()
cur2 = html.count('badge r2">上下级<')
cur3 = html.count('badge r3">高管间<')
print(f'current wall: ②={cur2} ③={cur3} (hl divs={html.count(chr(34)+"hl"+chr(34))})')

def find_grid_close(h, sec_start):
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

# inject ③ at end of sec3 grid
i3 = html.find('class="sec sec3"')
close3 = find_grid_close(html, i3)
html = html[:close3] + ''.join(card_html(c) for c in cards3) + html[close3:]
# inject ② at end of sec2 grid
i2 = html.find('class="sec sec2"')
close2 = find_grid_close(html, i2)
html = html[:close2] + ''.join(card_html(c) for c in cards2) + html[close2:]

# update sec tag counts
m2 = re.search(r'(<div class="sec sec2">.*?<span class="tag">)(\d+)( 卡)', html, re.S)
assert m2, 'sec2 tag not found'
html = html[:m2.start()] + m2.group(1) + str(cur2+n2) + m2.group(3) + html[m2.end():]
m3 = re.search(r'(<div class="sec sec3">.*?<span class="tag">)(\d+)( 卡)', html, re.S)
assert m3, 'sec3 tag not found'
html = html[:m3.start()] + m3.group(1) + str(cur3+n3) + m3.group(3) + html[m3.end():]

# hero append r26 segment
HERO_ANCHOR = '采集于 2026-08-23（第二十五轮 +7）'
assert HERO_ANCHOR in html, 'hero anchor not found'
SEG = '｜ 二十六轮补采 2026-08-25(+8，会后行动闭环/一线吐槽会/圆桌问政/安全主讲/降本坦诚/CEO说不知道/CEO个人反馈/变革叙事·5②3③)'
html = html.replace(HERO_ANCHOR, HERO_ANCHOR + SEG, 1)

open(HTML, 'w', encoding='utf-8').write(html)
footer_ok = '本页由 yitong 沉淀整理' in html
print(f'OK wall updated: ②={cur2+n2} ③={cur3+n3} (hl now {html.count(chr(34)+"hl"+chr(34))}), footer={footer_ok}')

# .run_newcards.tmp.html
with open(TMP, 'w', encoding='utf-8') as f:
    for c in cards:
        f.write(card_html(c) + '\n')
print(f'OK {TMP} written ({os.path.getsize(TMP)}B)')

# gen_run_page.py -> runs/staff-meeting-2026-08-25-r26.html
gen = os.path.join(KC, "gen_run_page.py")
RUN_PATH = os.path.join(KC, "staff-meeting", "runs", "staff-meeting-2026-08-25-r26.html")
r = subprocess.run(["python", gen, "--topic", "staff-meeting", "--topic-name",
                    "\u5458\u5de5\u5927\u4f1a", "--date", "2026-08-25", "--round", "26",
                    "--cards-file", TMP, "--out", RUN_PATH], capture_output=True, text=True)
print("gen_run_page:", r.returncode, r.stdout.strip(), (r.stderr.strip()[:200] if r.stderr else ""))

# index.json
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

# ===== Obsidian summary note =====
sum_txt = open(OB_SUM, encoding='utf-8').read()
# bump category counts
m3c = re.search(r'(### ③ [^\n]*— )(\d+)( 卡)', sum_txt)
assert m3c, 'summary ③ count not found'
sum_txt = sum_txt[:m3c.start()] + m3c.group(1) + str(int(m3c.group(2))+n3) + m3c.group(3) + sum_txt[m3c.end():]
m2c = re.search(r'(### ② [^\n]*— )(\d+)( 卡)', sum_txt)
assert m2c, 'summary ② count not found'
sum_txt = sum_txt[:m2c.start()] + m2c.group(1) + str(int(m2c.group(2))+n2) + m2c.group(3) + sum_txt[m2c.end():]
# append round section at end
round_section = (f'\n## 轮次 2026-08-25（+{len(cards)}）\n\n'
                 f'| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n')
for c in cards:
    rel = '高管间' if c['rel']=='r3' else '上下级'
    round_section += f'| {c["title"]} | {rel} | {c["src"]} |\n'
sum_txt = sum_txt.rstrip() + '\n' + round_section
open(OB_SUM, 'w', encoding='utf-8').write(sum_txt)
print(f'OK summary note updated (③+{n3} ②+{n2}, round section appended)')

# ===== Obsidian 00-index =====
idx_txt = open(OB_IDX, encoding='utf-8').read()
# header round list
HDR_TAIL = '二十五轮补采 2026-08-23（+7）'
assert HDR_TAIL in idx_txt, '00-index header tail not found'
idx_txt = idx_txt.replace(HDR_TAIL, HDR_TAIL + '｜ 二十六轮补采 2026-08-25(+8）', 1)
# total count 255 -> 263
assert '**255 卡**' in idx_txt, '255 卡 not found'
idx_txt = idx_txt.replace('**255 卡**', '**263 卡**', 1)
# breakdown 88 / 137
m88 = re.search(r'(③高管间\([^)]*\)\s*)88( 卡)', idx_txt)
assert m88, '88 卡 not found'
idx_txt = idx_txt[:m88.start()] + m88.group(1) + str(88+n3) + m88.group(3) + idx_txt[m88.end():]
m137 = re.search(r'(②上下级\([^)]*\)\s*)137( 卡)', idx_txt)
assert m137, '137 卡 not found'
idx_txt = idx_txt[:m137.start()] + m137.group(1) + str(137+n2) + m137.group(3) + idx_txt[m137.end():]
# append 8 rows before next "## 主题："
NEXT = idx_txt.find('## 主题：', idx_txt.find('二十六轮补采'))
assert NEXT != -1
rows = ''.join(
    f'| {c["title"]}（staff-meeting.html） | 4 | {c["src"]} | {"③高管间" if c["rel"]=="r3" else "②上下级"} | {c["cat"]}：{c["val"][:30]} |\n'
    for c in cards)
idx_txt = idx_txt[:NEXT] + rows + '\n' + idx_txt[NEXT:]
open(OB_IDX, 'w', encoding='utf-8').write(idx_txt)
print(f'OK 00-index updated (header+263+88->{88+n3}+137->{137+n2}+8 rows)')

# ===== Obsidian runs note =====
os.makedirs(os.path.dirname(OB_RUN), exist_ok=True)
run_md = f'''---
title: 员工大会 第二十六轮知识卡
tags: [知识采集, 员工大会, 自动化采集, 轮次]
date: 2026-08-25
type: 自动化采集
---

# 员工大会 · 第二十六轮补采（2026-08-25）

- 本轮新增 **{len(cards)} 卡**（②上下级 {n2} · ③高管间 {n3}），0 peer（硬约束）
- 一手 0 / 二手 {len(cards)}（本轮源均为媒体/机构二手，公司内部官方一手源稀缺）
- 累计墙：staff-meeting.html 255 → 263 卡（② {137+n2} / ③ {88+n3}）
- 新域：会后行动项闭环 / 一线吐槽会闭环 / 圆桌问政(三真原则) / 安全主讲(听众变主讲) / 降本坦诚(不裁员全员共创) / CEO说不知道 / CEO个人反馈嵌战略 / 变革叙事三阶
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

# ===== Step 8: GitHub Pages 同步 =====
sync = os.path.join(os.path.dirname(KC), "sync_knowledge_github.py")
try:
    rs = subprocess.run([sys.executable, sync], capture_output=True, text=True, timeout=300)
    print("sync_knowledge_github:", rs.returncode, (rs.stdout.strip()[-300:] if rs.stdout else ""), (rs.stderr.strip()[:200] if rs.stderr else ""))
except Exception as e:
    print("\u26a0\ufe0f GitHub 同步异常（告警不阻断）：" + str(e)[:200])

# ===== Step 9/10: 乐享上传（whoami 探活，不依赖连接器状态面板）=====
MCP_JSON = os.path.expanduser("~/.workbuddy/mcp.json")
LEXIANG_URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"
FOLDER = "a753a4ebc526495c9e9b2e2fb3cac314"   # 员工大会子文件夹（待清洗素材下）
WALL_FILE_ID = "a1415122f8034d8d988fb06e41be44ac"
WALL_ENTRY_ID = "f3b5ea59395e49ca859f8726142742c2"
RUN_NAME = os.path.basename(RUN_PATH)  # staff-meeting-2026-08-25-r26.html

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
    sm["rounds"].append({"date": "2026-08-25", "entry_id": rid, "name": RUN_NAME,
                         "note": "轮次页 R26 (+8：会后行动闭环/一线吐槽会/圆桌问政/安全主讲/降本坦诚/CEO说不知道/CEO个人反馈/变革叙事·5②3③)"})
    json.dump(mapf, open(os.path.join(KC, "lexiang-entry-map.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("已回写 lexiang-entry-map.json")
except Exception as e:
    print("\u26a0\ufe0f 乐享上传跳过（warning，不中断）：" + str(e)[:300])

# ===== 推进 last-topic.txt =====
LT = os.path.join(KC, "last-topic.txt")
with open(LT, "r", encoding="utf-8") as f:
    cur_topic = f.read().strip()
NEXT_TOPIC = "Offsite"
if cur_topic == "\u5458\u5de5\u5927\u4f1a":
    with open(LT, "w", encoding="utf-8") as f:
        f.write(NEXT_TOPIC + "\n")
    print(f"last-topic.txt 推进：{cur_topic} -> {NEXT_TOPIC}")
else:
    print(f"\u26a0\ufe0f last-topic.txt 当前为「{cur_topic}」非预期「员工大会」，未自动推进（请人工确认）")

print("\n=== R26 完成：新增", len(cards), "卡（②", n2, "/③", n3, "），墙现", cur2+n2, "② /", cur3+n3, "③ ===")
