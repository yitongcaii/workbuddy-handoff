# -*- coding: utf-8 -*-
import os
VAULT="C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库"
p=os.path.join(VAULT,"00-知识采集索引.md")
lines=open(p,encoding="utf-8").read().split("\n")
titles=[
"跨文化/远程高管入职·前100天信任与权限地图",
"家族企业 C-suite 入职·文化翻译官+关系资本",
"COO-CEO 二号位对齐·从签约前到任期持续信任",
"CEO-COO 工作协议·代理授权宪章（边界决策权）",
"新任领导者战略入职·信任与连续性路线图",
"新经理首次团队会议·议程模板与准备清单",
"低绩效团队 90 天转身·GROW 模型路线图",
]
# 1) remove misplaced rows (those containing a unique title)
kept=[l for l in lines if not any(t in l for t in titles)]
# 2) build new rows
newrows=[
"| 跨文化/远程高管入职·前100天信任与权限地图（icebreaker.html） | 5 | 二手 | ③高管间 | 外国企业聘外籍高管，文化模型冲突是头号失败源：共识决策 vs 个人决断、层级尊重 vs 直接沟通；招聘时即明确「聘你来改文化还是融入」，CEO 须发信号支持；有意远程入职可优于同址 |",
"| 家族企业 C-suite 入职·文化翻译官+关系资本（icebreaker.html） | 5 | 二手 | ③高管间 | 家族企业（多代/关系导向/潜规则深）空降 C 级，成败在文化/信任/所有权动态；五步：战略+文化双清晰、配「文化翻译官」资深董事当导师、90天关系资本建账、避开家族政治雷区、用早期双赢证明价值 |",
"| COO-CEO 二号位对齐·从签约前到任期持续信任（icebreaker.html） | 5 | 二手 | ③高管间 | COO 是 C-suite 最危险座位，命运系于 CEO 风格；对齐是生死线非加分项；签约前当过滤器：澄清角色定位、书面 charter（决策权/分歧升级）、测 CEO 决策风格与信任底线 |",
"| CEO-COO 工作协议·代理授权宪章（边界决策权）（icebreaker.html） | 5 | 二手 | ③高管间 | 最佳搭档保有共享运营地图并显式定义边界决策权；坑=过于简单分工造「意外双政府」；解法=边界定义决策权：CEO 拥战略/文化/外部、COO 拥运营/人/财务，跨界决策走升级协议 |",
"| 新任领导者战略入职·信任与连续性路线图（icebreaker.html） | 5 | 二手 | ③高管间 | 最有效过渡从入职第一天建信任；三加速法：结构化 90 天入职路线图（阶段目标/关键关系网/早期成果/留足倾听）、让介绍见面成信任契机、连续性地图保业务不脱节 |",
"| 新经理首次团队会议·议程模板与准备清单（icebreaker.html） | 5 | 二手 | ②上下级 | 新经理首会不是民主讨论而是建立共识起点；准备清单：上级/跨职能 1:1 调研期望底线、回顾 6-12 月 OKR/反馈/bug 找痛点、起草五环节核心议程 |",
"| 低绩效团队 90 天转身·GROW 模型路线图（icebreaker.html） | 5 | 二手 | ②上下级 | 接手低绩效团队，90 天结构化计划用 GROW（Goal/Reality/Options/Way Forward）建信任拿结果；前30天定位起点（1:1 识优弱/听而不判/审计卡点/快速赢） |",
]
# 3) find last 破冰 row in kept
lastidx=-1
for i,l in enumerate(kept):
    if "（icebreaker.html）" in l: lastidx=i
assert lastidx>=0, "no icebreaker row found"
out=kept[:lastidx+1]+newrows+kept[lastidx+1:]
tmp=p+".tmp"
open(tmp,"w",encoding="utf-8").write("\n".join(out))
os.replace(tmp,p)
print("00-索引 fixed: lastidx=",lastidx,"total lines now",len(out))
