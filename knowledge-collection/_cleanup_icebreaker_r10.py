# -*- coding: utf-8 -*-
import os, re, json

WS = "c:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection"
VAULT = "C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库"

# 7 new cards (corrected R10, replaced 12-duplicate mistake)
cards = [
    {"title":"跨文化/远程高管入职·前100天信任与权限地图","rel":"exec","src":"二手",
     "sum":"外国企业聘外籍高管，文化模型冲突是头号失败源：共识决策 vs 个人决断、层级尊重 vs 直接沟通；招聘时即明确「聘你来改文化还是融入」，CEO 须发信号支持；有意远程入职可优于同址——强迫把信任机制写进流程"},
    {"title":"家族企业 C-suite 入职·文化翻译官+关系资本","rel":"exec","src":"二手",
     "sum":"家族企业（多代/关系导向/潜规则深）空降 C 级，成败在文化/信任/所有权动态；五步：战略+文化双清晰、配「文化翻译官」资深董事当导师、90天关系资本建账、避开家族政治雷区、用早期双赢证明价值"},
    {"title":"COO-CEO 二号位对齐·从签约前到任期持续信任","rel":"exec","src":"二手",
     "sum":"COO 是 C-suite 最危险座位，命运系于 CEO 风格；对齐是生死线非加分项；签约前当过滤器：澄清角色定位、书面 charter（决策权/分歧升级）、测 CEO 决策风格与信任底线，任期持续用季度对齐复盘"},
    {"title":"CEO-COO 工作协议·代理授权宪章（边界决策权）","rel":"exec","src":"二手",
     "sum":"最佳搭档保有共享运营地图并显式定义边界决策权；坑=过于简单分工造「意外双政府」；解法=边界定义决策权：CEO 拥战略/文化/外部、COO 拥运营/人/财务，跨界决策走升级协议"},
    {"title":"新任领导者战略入职·信任与连续性路线图","rel":"exec","src":"二手",
     "sum":"最有效过渡从入职第一天建信任；三加速法：结构化 90 天入职路线图（阶段目标/关键关系网/早期成果/留足倾听）、让介绍见面成信任契机、连续性地图保业务不脱节"},
    {"title":"新经理首次团队会议·议程模板与准备清单","rel":"supervisor","src":"二手",
     "sum":"新经理首会不是民主讨论而是建立共识起点；准备清单：上级/跨职能 1:1 调研期望底线、回顾 6-12 月 OKR/反馈/bug 找痛点、起草五环节核心议程（现状洞察/核心原则/未来方向/承诺/跟进）"},
    {"title":"低绩效团队 90 天转身·GROW 模型路线图","rel":"supervisor","src":"二手",
     "sum":"接手低绩效团队，90 天结构化计划用 GROW（Goal/Reality/Options/Way Forward）建信任拿结果；前30天定位起点（1:1 识优弱/听而不判/审计卡点/快速赢），31-60天对齐现实选项，61-90天固化路径"},
]

def rel_cn(rel): return "③高管间" if rel=="exec" else "②上下级"
def write_atom(path, text):
    tmp = path + ".tmp"
    with open(tmp,"w",encoding="utf-8") as f: f.write(text)
    os.replace(tmp, path)

# ---------- 1) 00-索引.md ----------
p = os.path.join(VAULT,"00-知识采集索引.md")
s = open(p,encoding="utf-8").read()
last = s.rfind("(icebreaker.html)")
endl = s.rfind("\n", 0, last) + 1  # start of last icebreaker row
rowend = s.find("\n", endl)
newrows = ""
for c in cards:
    newrows += f"| {c['title']}（icebreaker.html） | 5 | {c['src']} | {rel_cn(c['rel'])} | {c['sum'][:90]} |\n"
s = s[:rowend] + newrows + s[rowend:]
write_atom(p, s)
print("00-索引 +7 rows OK")

# ---------- 2) 破冰-知识卡汇总.md ----------
p = os.path.join(VAULT,"素材/icebreaker/破冰-知识卡汇总.md")
s = open(p,encoding="utf-8").read()
# header line: +12 -> +7
s = s.replace("十轮补采 +12（2026-08-14）","十轮补采 +7（2026-08-14·修正替换误产12重复卡）")
s = s.replace("## 卡片总表（79 卡 · 仅②/③）","## 卡片总表（86 卡 · 仅②/③）")
s = s.replace("**②上下级（52 卡）**","**②上下级（54 卡）**").replace("**③高管间（27 卡）**","**③高管间（32 卡）**")
# insert 7 rows after card 79
anchor = '| 79 | "空降兵"如何管理新团队·向上管理先于向下（icebreaker.html）'
idx = s.find(anchor)
end = s.find("\n", idx)
ins = ""
for i,c in enumerate(cards,80):
    ins += f"| {i} | {c['title']} | {rel_cn(c['rel'])} | {c['src']} | {c['sum'][:100]} |\n"
s = s[:end+1] + ins + s[end+1:]
# add 第十轮 round section before "## 关联"
round_sec = '''## 本轮独立页（第十轮 · 2026-08-14 · 修正）
- **独立页（7 卡）**：[icebreaker-20260814.html · GitHub Pages](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/icebreaker-20260814.html)
- **本机源**：`knowledge-collection/icebreaker/icebreaker-20260814.html`（本轮新增 7 卡：③5 / ②2；修正：替换上轮误产的 12 张重复卡）
- 本轮独立笔记：[[知识采集库/素材/icebreaker/runs/破冰-2026-08-14-第十轮-知识卡]]

'''
s = s.replace("## 关联", round_sec + "## 关联", 1)
write_atom(p, s)
print("破冰 note OK (79->86)")

# ---------- 3) portal index.html ----------
p = os.path.join(WS,"index.html")
s = open(p,encoding="utf-8").read()
s = s.replace('<div class="cnt">62 卡</div>\n        <div class="emoji">🧊</div>',
              '<div class="cnt">86 卡</div>\n        <div class="emoji">🧊</div>')
assert "86 卡" in s and "62 卡" not in s.split("🧊")[0] or "86 卡" in s
write_atom(p, s)
print("portal 破冰 62->86 OK")

# ---------- 4) lexiang-entry-map.json ----------
p = os.path.join(WS,"lexiang-entry-map.json")
m = json.load(open(p,encoding="utf-8"))
ib = m["icebreaker"]
ib["wall"]["note"] = "R10 累计墙（86卡）"
for r in ib["rounds"]:
    if r.get("date")=="2026-08-14":
        r["name"]="icebreaker-20260814.html"
        r["note"]="轮次页 R10 (+7｜修正：替换误产12重复卡)"
        # entry_id filled after lexiang re-upload
json.dump(m, open(p,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
print("lexiang map wall note + R10 name/note OK (entry_id pending upload)")
print("CLEANUP DONE")
