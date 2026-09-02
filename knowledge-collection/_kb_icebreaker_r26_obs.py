# -*- coding: utf-8 -*-
"""破冰 r27 (2026-09-02) Obsidian 落库：汇总笔记 / 00 索引 / 本轮独立笔记。"""
import os

VAULT = r'C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库'
SUM = os.path.join(VAULT, '素材', 'icebreaker', '破冰-知识卡汇总.md')
IDX = os.path.join(VAULT, '00-知识采集索引.md')
RUNS = os.path.join(VAULT, '素材', 'icebreaker', 'runs')
os.makedirs(RUNS, exist_ok=True)
RUNNOTE = os.path.join(RUNS, '破冰-2026-09-02-第27轮-知识卡.md')

GP = 'https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/runs/icebreaker-2026-09-02-r27.html'
LOCAL = 'knowledge-collection/icebreaker/runs/icebreaker-2026-09-02-r27.html'
WALL = 'https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/icebreaker.html'

cards = [
    ("Google re:Work 团队效能五动态·心理安全为首 + 管理者落地动作（一手工具包）", "②上下级", "一手",
     "Google Project Aristotle 官方工具包：5 大团队效能动态(心理安全/依赖/清晰/意义/影响)+管理者落地三动作(共同词汇/论坛/领导承诺)，破冰与团队建设底层操作系统"),
    ("跨文化全球团队·用「团队规范共创」替代破冰游戏 + 开放式提问重构（HBR）", "②上下级", "二手",
     "co-create 团队规范(显式包容)替代无效破冰游戏；封闭提问重构为开放(「有什么担心」)，把分享困难正常化；文化智能+视角采择"),
    ("新经理团队建设·非正式仪式 + 零预算 + 远程三板斧（真正管用）", "②上下级", "二手",
     "非正式仪式(周一咖啡/周五 wins&fails/help-needed 看板)+零预算(步行1:1/技能互换/志愿)+远程(虚拟咖啡/异步庆祝/年度线下)，重日常轻活动"),
    ("新经理 90 天科学剧本·听→对齐→共创共赢 + 首日建心理安全", "②上下级", "二手",
     "90 天三段(听→书面对齐→共创共享胜仗)；首日心理安全四信号(示弱/把错当测试/邀异议/快速AAR)，引用 Gallup+Edmondson"),
    ("高管/董事会务虚·pre-mortem + unconference + 战争推演 + 48 小时规则", "③高管间", "二手",
     "pre-mortem(3年后惨败写历史)+unconference(议程共创)+fireside chat+war gaming+guided solitude+外部引导师；48h 内发决策/owner/期限"),
    ("企业务虚对董事会/管理层的价值·首日非工作活动 + DiSC + 外部引导师（澳董事学会）", "③高管间", "一手",
     "澳董事学会官方：离岗新视角→更好决策；首日非工作活动逼大脑离业务；DiSC 破人际壁垒；外部引导师把工作交还董事；年两次两天最佳"),
]

# ---------- 1) 汇总笔记 ----------
s = open(SUM, encoding='utf-8').read()
s = s.replace('date: 2026-09-01', 'date: 2026-09-02')
# 更新本轮增量页/本机源链接（旧 09-01）→ r27 09-02
s = s.replace('icebreaker-20260901.html', 'runs/icebreaker-2026-09-02-r27.html')
s = s.replace('本轮增量页（2026-09-01）', '本轮增量页（2026-09-02）')
# 卡片总表计数 230 -> 237（实际行数）
s = s.replace('## 卡片总表（230 卡 · 仅②/③）', '## 卡片总表（237 卡 · 仅②/③）')

narr = ("\n> 二十七轮补采 +6（2026-09-02，②×4/③×2）：Google re:Work 团队效能五动态(心理安全为首·一手工具包)/"
        "跨文化全球团队规范共创+开放式提问重构(BU Questrom·HBR)/新经理团队建设非正式仪式+零预算+远程三板斧("
        "FirstTimeManagers)/新经理 90 天科学剧本+首日心理安全四信号(Science of People)（②）；高管务虚 pre-mortem+"
        "unconference+war gaming+48h 规则(hayatkhabar)/企业务虚价值 首日非工作活动+DiSC+外部引导师(澳董事学会·一手)（③）\n\n"
        "## 二十七轮新增卡片（2026-09-02）\n"
        "| # | 卡片 | 关系档 | 一手/二手 | 核心要点 |\n|---|---|---|---|---|\n")
for i, (t, rel, st, summ) in enumerate(cards, start=232):
    narr += "| %d | %s | %s | %s | %s |\n" % (i, t, rel, st, summ)
s = s.rstrip('\n') + '\n' + narr
open(SUM, 'w', encoding='utf-8').write(s)
print('SUMMARY updated')

# ---------- 2) 00 索引（扁平表，追加 6 行） ----------
idx = open(IDX, encoding='utf-8').read()
rows = '\n'
for (t, rel, st, summ) in cards:
    rows += "| %s（icebreaker.html） | 4 | %s | %s | %s |\n" % (t, st, rel, summ)
idx = idx.rstrip('\n') + rows
open(IDX, 'w', encoding='utf-8').write(idx)
print('00-INDEX appended 6 rows')

# ---------- 3) 本轮独立笔记 ----------
note = (
    "---\ntitle: 破冰·第27轮知识卡（2026-09-02）\n"
    "tags: [知识采集, 自动化采集, 破冰, 团队信任, 上下级, 高管间]\ndate: 2026-09-02\n"
    "type: 自动化采集\nrelation: [supervisor, exec]\nsource_topic: 破冰\n---\n\n"
    "# 破冰 · 第 27 轮知识卡（2026-09-02）\n\n"
    "> 本轮 +6 卡（②上下级 ×4 / ③高管间 ×2），六维评估全过；一手 2（Google re:Work 工具包、澳董事学会官方）、二手 4。\n"
    "> 受众关系分层硬约束：仅 ②上下级 / ③高管间，已剔除 ①平级向内容。\n\n"
    "**独立页（GitHub Pages）**：[%s](%s)\n\n"
    "**本机源**：`%s`\n\n"
    "**累计总索引（卡片墙）**：[%s](%s)\n\n"
    "## 本轮卡片（6 张）\n\n"
    "| # | 卡片 | 关系档 | 一手/二手 | 核心要点 |\n|---|---|---|---|---|\n"
) % (GP, GP, LOCAL, WALL, WALL)
for i, (t, rel, st, summ) in enumerate(cards, start=1):
    note += "| %d | %s | %s | %s | %s |\n" % (i, t, rel, st, summ)
note += "\n> 说明：本笔记为 md 索引，不存 HTML 副本；源卡片墙/独立页见上方 GitHub Pages 链接与本机源路径。\n"
open(RUNNOTE, 'w', encoding='utf-8').write(note)
print('RUN NOTE created:', os.path.basename(RUNNOTE))
