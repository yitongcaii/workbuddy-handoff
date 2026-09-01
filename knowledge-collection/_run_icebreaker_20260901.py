# -*- coding: utf-8 -*-
import json, re, io

KC = "c:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection"
ICE = KC + "/icebreaker"
INC = ICE + "/icebreaker-20260901.html"
SUM = ICE + "/icebreaker.html"
IDX = KC + "/index.json"
VAULT_NOTE = "C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库/素材/icebreaker/破冰-知识卡汇总.md"

# ---- 1. extract cards from increment page (robust balanced-div parse) ----
html = open(INC, encoding="utf-8").read()
def extract_cards(h):
    cards = []
    i = 0
    while True:
        s = h.find('<div class="hl">', i)
        if s == -1:
            break
        depth = 0
        j = s
        while j < len(h):
            if h.startswith('<div', j):
                depth += 1
                j = h.find('>', j) + 1
                continue
            elif h.startswith('</div>', j):
                depth -= 1
                j += 6
                if depth == 0:
                    break
                continue
            else:
                j += 1
        cards.append(h[s:j])
        i = j
    return cards
all_cards = extract_cards(html)
exec_cards = [c for c in all_cards if 'badge r3' in c]
sup_cards = [c for c in all_cards if 'badge r2' in c]
print("extracted total=%d exec=%d sup=%d" % (len(all_cards), len(exec_cards), len(sup_cards)))

# ---- 2. inject into summary page ----
s = open(SUM, encoding="utf-8").read()
assert s.count('<div class="sec sec2"') == 1, "sec2 anchor not unique"
assert s.count('<footer>') == 1, "footer anchor not unique"
s = s.replace('<div class="sec sec2"', '\n'.join(exec_cards) + '\n<div class="sec sec2"', 1)
s = s.replace('<footer>', '\n'.join(sup_cards) + '\n<footer>', 1)
# update counts
s = s.replace('<span class="tag">89 卡</span>', '<span class="tag">93 卡</span>', 1)
s = s.replace('<span class="tag">141 卡</span>', '<span class="tag">147 卡</span>', 1)
# hero desc append
round_desc = (" ｜ 本轮补采 +10（2026-09-01）：高管入职书面领导宪章+30-60-90+CEO 握手 / "
              "C-Suite 授权书先于上任+情报简报 / 高管入职初见+1:1 倾听+半日信任工作坊 / 新任 CEO 90 天路线图（③）；"
              "越级会谈 HR 官方手册(一手)+问题银行 30min 模板+议程 20 问+中层不在场 / 新经理入职清单 1:1 机制+决策权书面化 / "
              "新经理首场员工会 45min / 新团队首会 6 要素（②）")
s = s.replace('（2026-08-28，②×1/③×3）：高管团队运营章程(Monkhouse)、董事会-CEO 运营协议(managingthefuture)、联席 CEO/共治协议(ceonextchapter)（③）；越级会谈·领导者实战手册(performanceninja)（②）</p>',
              '（2026-08-28，②×1/③×3）：高管团队运营章程(Monkhouse)、董事会-CEO 运营协议(managingthefuture)、联席 CEO/共治协议(ceonextchapter)（③）；越级会谈·领导者实战手册(performanceninja)（②）' + round_desc + '</p>', 1)
# footer 🔸 -> 📌 (compliance)
s = s.replace('🔸 本页由 yitong 沉淀整理 · 文化活动知识库', '📌 本页由 yitong 沉淀整理 · 文化活动知识库')
open(SUM, "w", encoding="utf-8").write(s)
print("summary page updated; sec3/exec=%d sec2/sup=%d" % (len(exec_cards), len(sup_cards)))

# ---- 3. update index.json ----
new_entries = [
 {"title":"高管入职·书面领导宪章 + 30-60-90 节奏 + CEO 握手","normKey":"高管入职·书面领导宪章 + 30-60-90 节奏 + CEO 握手","url":"https://summitexecutivesearch.com/2026/07/17/executive-onboarding-best-practices-guide","sourceType":"secondary","relation":"exec","summary":"高管入职书面领导宪章(成果+决策权+约束)+利益方地图点名摩擦点+30-60-90节奏+CEO首月每周握手1:1，把高风险任命变运营结果","topic":"icebreaker"},
 {"title":"C-Suite 入职·授权书先于上任 + 情报简报 + 董事会-CEO 对齐","normKey":"C-Suite 入职·授权书先于上任 + 情报简报 + 董事会-CEO 对齐","url":"https://scionretainedsearch.com/2026/08/01/guide-to-c-suite-onboarding","sourceType":"secondary","relation":"exec","summary":"接受任命即出书面授权书(成果/决策/约束)+情报简报包+董事会-CEO显式对齐沟通节奏决策权监督边界+首30天一致问题诊断","topic":"icebreaker"},
 {"title":"高管入职·团队初见 + 1:1 倾听问题 + 半日信任工作坊","normKey":"高管入职·团队初见 + 1:1 倾听问题 + 半日信任工作坊","url":"http://www.spencerstuart.jp/research-and-insight/managing-technology-enabled-executive-onboarding-and-transitions","sourceType":"secondary","relation":"exec","summary":"Spencer Stuart高管入职:团队初见(CEO互介后留纯认识)+直属团队1:1前发倾听问题+半日心理测评信任工作坊+利益方地图按动机定沟通","topic":"icebreaker"},
 {"title":"新任 CEO 90 天路线图·董事会破冰 + 战略 Offsite + 100 天复盘","normKey":"新任 CEO 90 天路线图·董事会破冰 + 战略 Offsite + 100 天复盘","url":"https://www.galvinrowley.com.au/ceo-onboarding-plan","sourceType":"secondary","relation":"exec","summary":"新CEO首90天:D1-5董事会+执行团队1:1/W2-4跨职能简报+一线文化小组会/M2战略Offsite+速赢/100天董事会复盘/持续季度更新","topic":"icebreaker"},
 {"title":"越级会谈·HR 官方引导手册（问题库 + 留任访谈 + 数据背书）","normKey":"越级会谈·HR 官方引导手册（问题库 + 留任访谈 + 数据背书）","url":"https://sc.edu/about/offices_and_divisions/human_resources/docs/manager_guide_facilitating_impactful_skip_level_conversations.pdf","sourceType":"primary","relation":"supervisor","summary":"南卡大学HR官方越级会谈指南:数据背书(37%更投入/82%频互动/+25%早识别风险)+6类问题库+留任访谈模板+保密闭环纪律","topic":"icebreaker"},
 {"title":"越级会谈·问题银行 + 30 分钟模板（不评经理）","normKey":"越级会谈·问题银行 + 30 分钟模板（不评经理）","url":"https://cultureamp.com/blog/skip-level-meeting-guide","sourceType":"secondary","relation":"supervisor","summary":"CultureAmp越级会谈问题分经理支持/组织/变革三块+问经理哪做得好避人格审判不评绩效+30min模板多听少说","topic":"icebreaker"},
 {"title":"新经理入职清单·1:1 实操机制 + 决策权书面化","normKey":"新经理入职清单·1:1 实操机制 + 决策权书面化","url":"https://tallyfy.com/new-manager-onboarding-checklist/","sourceType":"secondary","relation":"supervisor","summary":"新经理入职清单:1:1实操机制(频率/何时听)+反馈不伤人+硬谈话+决策权书面化(预算/人事/流程阈值)","topic":"icebreaker"},
 {"title":"新经理首场员工会·45 分钟议程 + 会议节奏","normKey":"新经理首场员工会·45 分钟议程 + 会议节奏","url":"https://workleap.com/blog/new-manager-first-staff-meeting","sourceType":"secondary","relation":"supervisor","summary":"新经理首场员工会45min模板:破冰+团队优势挑战+想改想留+开放提问+首会后定会议频率平衡1:1","topic":"icebreaker"},
 {"title":"越级会谈·议程模板 + 20 问 + 中层不在场纪律","normKey":"越级会谈·议程模板 + 20 问 + 中层不在场纪律","url":"https://engagedly.com/blog/what-is-a-skip-level-meeting-and-how-to-conduct-one/","sourceType":"secondary","relation":"supervisor","summary":"Engagedly越级会谈:中层经理不在场(事后聚合主题分享)+30-45min议程+20问五类+会后聚合主题跨会谈向员工闭环","topic":"icebreaker"},
 {"title":"新团队首会·6 要素议程最佳实践","normKey":"新团队首会·6 要素议程最佳实践","url":"https://carreersupport.com/proposed-team-agenda-for-the-first-meeting/","sourceType":"secondary","relation":"supervisor","summary":"新团队首会6要素:自我介绍+破冰fun fact/团队视角/领导哲学/期望规则/Q&A/下一步+提前发议程限60-90min","topic":"icebreaker"},
]
d = json.load(open(IDX, encoding="utf-8"))
existing_urls = set(c.get("url","") for c in d)
added = 0
for e in new_entries:
    if e["url"] in existing_urls:
        print("SKIP dup url:", e["url"])
        continue
    d.append(e); added += 1
json.dump(d, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("index.json added=%d total=%d" % (added, len(d)))

# ---- 4. Obsidian note: insert round section + 10 table rows ----
n = open(VAULT_NOTE, encoding="utf-8").read()
# a) insert round heading+blockquote before '## 卡片总表'
round_block = (
'\n> 二十六轮补采 +10（2026-09-01）：高管入职书面领导宪章+30-60-90+CEO 握手 / C-Suite 授权书先于上任+情报简报 / '
'高管入职初见+1:1 倾听+半日信任工作坊 / 新任 CEO 90 天路线图（③）；'
'越级会谈 HR 官方手册(一手)+问题银行 30min 模板+议程 20 问+中层不在场 / 新经理入职清单 1:1 机制+决策权书面化 / '
'新经理首场员工会 45min / 新团队首会 6 要素（②）\n'
'## 轮次 20260901（+10）\n'
)
n = n.replace('## 卡片总表', round_block + '## 卡片总表', 1)
# b) append 10 rows to table + update count
rows = [
 (222,"高管入职·书面领导宪章 + 30-60-90 节奏 + CEO 握手","③高管间","二手","上任前书面领导宪章(成果+决策权+约束)+利益方地图点名摩擦点+30-60-90节奏+CEO首月每周握手1:1"),
 (223,"C-Suite 入职·授权书先于上任 + 情报简报 + 董事会-CEO 对齐","③高管间","二手","接受任命即出书面授权书+情报简报包+董事会-CEO显式对齐沟通节奏决策权监督边界+首30天一致问题诊断"),
 (224,"高管入职·团队初见 + 1:1 倾听问题 + 半日信任工作坊","③高管间","二手","Spencer Stuart:团队初见(CEO互介后留纯认识)+1:1前发倾听问题+半日心理测评信任工作坊+利益方地图"),
 (225,"新任 CEO 90 天路线图·董事会破冰 + 战略 Offsite + 100 天复盘","③高管间","二手","新CEO首90天:D1-5董事会+执行团队1:1/W2-4跨职能简报/M2战略Offsite/100天董事会复盘"),
 (226,"越级会谈·HR 官方引导手册（问题库 + 留任访谈 + 数据背书）","②上下级","一手","南卡大学HR官方:数据背书(37%更投入/82%频互动/+25%早识别风险)+6类问题库+留任访谈模板+保密闭环"),
 (227,"越级会谈·问题银行 + 30 分钟模板（不评经理）","②上下级","二手","问题分经理支持/组织/变革三块+问经理哪做得好避人格审判不评绩效+30min模板多听少说"),
 (228,"新经理入职清单·1:1 实操机制 + 决策权书面化","②上下级","二手","1:1实操机制(频率/何时听)+反馈不伤人+硬谈话+决策权书面化(预算/人事/流程阈值)"),
 (229,"新经理首场员工会·45 分钟议程 + 会议节奏","②上下级","二手","45min模板:破冰+团队优势挑战+想改想留+开放提问+首会后定会议频率平衡1:1"),
 (230,"越级会谈·议程模板 + 20 问 + 中层不在场纪律","②上下级","二手","中层经理不在场(事后聚合主题分享)+30-45min议程+20问五类+会后聚合主题跨会谈向员工闭环"),
 (231,"新团队首会·6 要素议程最佳实践","②上下级","二手","6要素:自我介绍+破冰fun fact/团队视角/领导哲学/期望规则/Q&A/下一步+提前发议程限60-90min"),
]
row_md = "\n" + "\n".join("| %d | %s | %s | %s | %s |" % r for r in rows)
# find table end: last line starting with '|' before next non-table block
lines = n.split("\n")
# locate last card row
last_idx = None
for k in range(len(lines)-1, -1, -1):
    if lines[k].startswith("|") and re.match(r"\|\s*\d+\s*\|", lines[k]):
        last_idx = k; break
lines.insert(last_idx+1, row_md.strip())
n = "\n".join(lines)
n = n.replace("## 卡片总表（221 卡 · 仅②/③）", "## 卡片总表（231 卡 · 仅②/③）", 1)
open(VAULT_NOTE, "w", encoding="utf-8").write(n)
print("obsidian note updated: +10 rows, count 221->231")
print("DONE")
