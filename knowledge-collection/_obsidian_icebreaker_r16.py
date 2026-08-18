# -*- coding: utf-8 -*-
"""r16 Obsidian 落库：破冰-知识卡汇总.md 追加 7 行 + 计数；00-知识采集索引.md 追加 7 行 + 计数；
新建 runs/破冰-2026-08-18-第十六轮-知识卡.md。"""
import os

KB = r"C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库"
SUMMARY = os.path.join(KB, "素材", "icebreaker", "破冰-知识卡汇总.md")
IDX = os.path.join(KB, "00-知识采集索引.md")
RUNS = os.path.join(KB, "素材", "icebreaker", "runs", "破冰-2026-08-18-第十六轮-知识卡.md")

# 7 张净新增卡（顺序：③3 + ②4），与累计墙/card 表一致
NEW_ROWS = [
    ("139", "高管 Offsite 五块议程·30 天强化才 stick（buildingteams）", "③高管间", "二手",
     "五块顺序：定『30天后哪点必须不同』→Reset the Flag(2-3优先级)→honest conversation(CEO参与非裁判)→变决策(owner+deadline+defend)→Set the Standard+30天强化；无强化块=多数offsite不stick"),
    ("140", "领导力 Offsite 2.5 天议程·外部引导师 ROI（bondeo）", "③高管间", "二手",
     "8-16人2.5天(修道院感场地避度假村)；必带诚实成绩单+一页战略草稿+top10人才评估+top3赌注+7天预读+手机入篮；always请外部引导师(多解锁30-40%坦率)"),
    ("141", "领导团队凝聚力工作坊·2-3h 结构+避坑（culturevitale）", "③高管间", "二手",
     "价值/领导身份→团队效能评估→同侪教练圈→建设性分歧；2-3h结构+五大避坑(先诊断/裂痕团队外部引导师/安全建好再脆弱/防groupthink)；高管以真peer参与"),
    ("142", "留任访谈(Stay Interview)·11 问建信任留人（经理↔员工）", "②上下级", "二手",
     "11问按『喜欢→不喜欢→平衡→留任意愿→成长→我能做什么→理想职位→离职念头』；私密无评判+不做空承诺+会后闭环快赢；新人60天后、关键岗定期"),
    ("143", "留任访谈模板·量表+选择题+关系诊断（轻量可落地）", "②上下级", "二手",
     "9道混合题型(多选/1-10量表/开放)量化归属感/真话安全感/优势发挥/离职倾向；咖啡闲聊非审讯、说真话无后果、问后必行动闭环"),
    ("144", "冲突后团队信任修复工作坊·90 分钟剧本（SBI+Lencioni）", "②上下级", "二手",
     "90min：Lencioni定位最痛2-3 dysfunction→SBI清场对话(具体有日期瞬间、接收者不辩解、资深先接)→承诺卡→散会前锁定3周后30min复盘"),
    ("145", "重建团队凝聚力·经理实操 7 步（目标/倾听/规则/认可）", "②上下级", "二手",
     "7步：共享目标→透明沟通+积极倾听→非工作语境团建→清晰准则→文化庆祝认可→快速中立解冲突→持续个人贡献认可"),
]

# 00-index 行格式（质量分统一 5）
IDX_ROWS = [
    ("高管 Offsite 五块议程·30 天强化才 stick（buildingteams）", "icebreaker.html", "5", "二手", "③高管间",
     "五块：定『30天后哪点必须不同』→Reset the Flag→honest conversation(CEO参与非裁判)→变决策→Set the Standard+30天强化"),
    ("领导力 Offsite 2.5 天议程·外部引导师 ROI（bondeo）", "icebreaker.html", "5", "二手", "③高管间",
     "8-16人2.5天(修道院感场地避度假村)；必带成绩单+战略草稿+top10人才+top3赌注+7天预读+手机入篮；always请外部引导师"),
    ("领导团队凝聚力工作坊·2-3h 结构+避坑（culturevitale）", "icebreaker.html", "5", "二手", "③高管间",
     "价值/领导身份→团队效能评估→同侪教练圈→建设性分歧；2-3h结构+五大避坑(先诊断/外部引导师/防groupthink)"),
    ("留任访谈(Stay Interview)·11 问建信任留人（skillhubs）", "icebreaker.html", "5", "二手", "②上下级",
     "11问按喜欢→不喜欢→平衡→留任意愿→成长→我能做什么→理想职位→离职念头；私密无评判+会后闭环"),
    ("留任访谈模板·量表+选择题+关系诊断（stribehq）", "icebreaker.html", "5", "二手", "②上下级",
     "9道混合题型量化归属感/真话安全感/优势发挥/离职倾向；咖啡闲聊非审讯、说真话无后果、问后必行动闭环"),
    ("冲突后团队信任修复工作坊·90 分钟剧本（SBI+Lencioni）", "icebreaker.html", "5", "二手", "②上下级",
     "90min：Lencioni定位最痛2-3 dysfunction→SBI清场对话(具体有日期/接收者不辩解/资深先接)→承诺卡→散会前锁定3周后30min复盘"),
    ("重建团队凝聚力·经理实操 7 步（archetype）", "icebreaker.html", "5", "二手", "②上下级",
     "7步：共享目标→透明沟通+积极倾听→非工作语境团建→清晰准则→文化庆祝认可→快速中立解冲突→持续个人贡献认可"),
]

# ---------- 1) 汇总笔记 ----------
s = open(SUMMARY, encoding="utf-8").read()
assert "｜ 十五轮补采 +8（2026-08-18）" in s, "summary intro 十五轮 not found"
s = s.replace("｜ 十五轮补采 +8（2026-08-18）", "｜ 十五轮补采 +8（2026-08-18）｜ 十六轮补采 +7（2026-08-18 晚）", 1)
assert "## 卡片总表（138 卡 · 仅②/③）" in s, "summary table header not found"
s = s.replace("## 卡片总表（138 卡 · 仅②/③）", "## 卡片总表（145 卡 · 仅②/③）", 1)
summary_rows = "\n".join(
    f"| {n} | {title} | {rel} | {src} | {point} |" for (n, title, rel, src, point) in NEW_ROWS
)
if not s.endswith("\n"):
    s += "\n"
s += summary_rows + "\n"
open(SUMMARY, "w", encoding="utf-8").write(s)

# ---------- 2) 00-索引 ----------
t = open(IDX, encoding="utf-8").read()
assert "## 主题：破冰（" in t
t = t.replace("· 十五轮补采 2026-08-18）", "· 十五轮补采 2026-08-18 · 十六轮补采 2026-08-18 晚）", 1)
assert "**138 卡**" in t
t = t.replace("**138 卡**", "**145 卡**", 1)
assert "③高管间 47 卡 / ②上下级 92 卡" in t
t = t.replace("③高管间 47 卡 / ②上下级 92 卡", "③高管间 49 卡 / ②上下级 96 卡", 1)
assert "（workhuman·②）。" in t
t = t.replace("（workhuman·②）。",
              "（workhuman·②）。十六轮补采（+7，全二手）新开——留任访谈 Stay Interview 11 问(skillhubs·②)、留任访谈轻量量表模板(stribehq·②)、冲突后 90 分钟信任修复工作坊 SBI+Lencioni(unicornlabs·②)、重建团队凝聚力 7 步(archetype·②)、高管 Offsite 五块+30 天强化(buildingteams·③)、领导力 Offsite 2.5 天外部引导师 ROI(bondeo·③)、领导团队凝聚力工作坊 2-3h+culturevitale 避坑（③）。", 1)
# 在 icebreaker 末行（越级会谈问题库 rapport 先行）后插入 7 行
marker = "| 越级会谈问题库·建 rapport + 团队反馈 + 对直属上级反馈（icebreaker.html） | 5 | 二手 | ②上下级 | 三段：rapport 破冰→团队反馈→对经理反馈；rapport 先行再要坦诚，中立桥接不越权 |"
assert marker in t, "00-index icebreaker last row not found"
idx_rows = "\n".join(
    f"| {title}（{html}） | {score} | {src} | {rel} | {point} |" for (title, html, score, src, rel, point) in IDX_ROWS
)
t = t.replace(marker, marker + "\n" + idx_rows, 1)
open(IDX, "w", encoding="utf-8").write(t)

# ---------- 3) runs 笔记 ----------
runs_md = """---
title: 破冰·第十六轮知识卡（2026-08-18 晚）
tags: [知识采集, 自动化采集, 破冰, 上下级, 高管间]
date: 2026-08-18
type: 自动化采集
relation: [supervisor, exec]
source_topic: 破冰
round: 16
---

# 破冰 · 第十六轮知识卡（2026-08-18 晚 · +7）

> 自动化采集第十六轮，主题「破冰」。本轮净新增 7 卡：③高管间 3 / ②上下级 4，**全部二手**（该主题②③一手稀缺）。
> 受众关系分层硬约束：已剔除平级/朋友向（①），仅保留 ②上下级 / ③高管间。
> 去重说明：scavify 高管 Offsite 决策议程为累计墙已有卡（URL 已在墙内），本轮不重复注入；另有 2 张此前 index 孤儿卡（buildingteams/bondeo 高管 Offsite 议程）本轮回填进累计墙补齐。

**独立页（线上）**：[icebreaker-2026-08-18-r16.html · GitHub Pages](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/runs/icebreaker-2026-08-18-r16.html)
**本机源**：`knowledge-collection/icebreaker/runs/icebreaker-2026-08-18-r16.html`
**累计卡片墙**：[icebreaker.html · GitHub Pages](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/icebreaker.html)
**汇总笔记**：[[知识采集库/素材/icebreaker/破冰-知识卡汇总]]

## 本轮 7 卡

| # | 卡片 | 关系档 | 一手/二手 | 核心要点 |
|---|---|---|---|---|
| 139 | 高管 Offsite 五块议程·30 天强化才 stick（buildingteams） | ③高管间 | 二手 | 五块：定『30天后哪点必须不同』→Reset the Flag(2-3优先级)→honest conversation(CEO参与非裁判)→变决策(owner+deadline+defend)→Set the Standard+30天强化 |
| 140 | 领导力 Offsite 2.5 天议程·外部引导师 ROI（bondeo） | ③高管间 | 二手 | 8-16人2.5天(修道院感场地避度假村)；必带诚实成绩单+一页战略草稿+top10人才评估+top3赌注+7天预读+手机入篮；always请外部引导师(多解锁30-40%坦率) |
| 141 | 领导团队凝聚力工作坊·2-3h 结构+避坑（culturevitale） | ③高管间 | 二手 | 价值/领导身份→团队效能评估→同侪教练圈→建设性分歧；2-3h结构+五大避坑(先诊断/裂痕团队外部引导师/防groupthink)；高管以真peer参与 |
| 142 | 留任访谈(Stay Interview)·11 问建信任留人（经理↔员工） | ②上下级 | 二手 | 11问按喜欢→不喜欢→平衡→留任意愿→成长→我能做什么→理想职位→离职念头；私密无评判+会后闭环 |
| 143 | 留任访谈模板·量表+选择题+关系诊断（轻量可落地） | ②上下级 | 二手 | 9道混合题型量化归属感/真话安全感/优势发挥/离职倾向；咖啡闲聊非审讯、说真话无后果、问后必行动闭环 |
| 144 | 冲突后团队信任修复工作坊·90 分钟剧本（SBI+Lencioni） | ②上下级 | 二手 | 90min：Lencioni定位最痛2-3 dysfunction→SBI清场对话(具体有日期瞬间、接收者不辩解、资深先接)→承诺卡→散会前锁定3周后30min复盘 |
| 145 | 重建团队凝聚力·经理实操 7 步（目标/倾听/规则/认可） | ②上下级 | 二手 | 7步：共享目标→透明沟通+积极倾听→非工作语境团建→清晰准则→文化庆祝认可→快速中立解冲突→持续个人贡献认可 |

## 关联
- 汇总：[[知识采集库/素材/icebreaker/破冰-知识卡汇总]]（破冰主题段）
- 索引：[[00-知识采集索引]]（破冰主题段）
"""
os.makedirs(os.path.dirname(RUNS), exist_ok=True)
open(RUNS, "w", encoding="utf-8").write(runs_md)

print("OK obsidian | summary 145 rows | idx +7 rows | runs note created")
