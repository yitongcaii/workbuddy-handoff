# -*- coding: utf-8 -*-
# Obsidian 落库（员工大会 R18）：汇总笔记追加段 + 00索引追加行 + 新建独立笔记
import os

SUMMARY = r'C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\staff-meeting\员工大会-知识卡汇总.md'
IDX00   = r'C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md'
RUNS    = r'C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\staff-meeting\runs'

# (title, relation_display_summary, source_display, oneliner, relation_display_idx, summary_idx)
CARDS = [
 ("季度业务回顾（QBR）嵌入全员会（customerexperience·诚实暴露未达标+根因+下一步共创）", "②+③", "二手",
  "QBR做进全员会：10页上限、Slide4必含诚实miss、Slide7「做错了什么」具体、Slide9行动项owner+date当场读、会后24h发，决策驱动非数据倾倒。",
  "②上下级 / ③高管间", "customerexperience.io：QBR嵌入全员会，诚实暴露未达标+根因owner+下一步共创（二手）"),
 ("QBR执行摘要一页纸模板（toolkitcafe·Headline/财务快照/Top3 wins/risks/decisions）", "③", "二手",
  "toolkitcafe 高管季度定调页：Headline一句话+财务快照(±%)+Top3 wins+Top3 risks+必决事项，纪律化QBR达标率2.5x。",
  "③高管间", "toolkitcafe：QBR执行摘要一页纸（Headline/财务快照/Top3 wins/risks/decisions），会议开场钩子（二手）"),
 ("追觅俞浩「高调战略」：全员信息透明·信息直达末梢（m.x-techcon·每层级损耗20%）", "②+③", "二手",
  "追觅CEO俞浩：战略每经一层损耗20%，推行全员信息透明（战略会开放/事业部月例会对跨部门开放/新想法发全员群），扩至20万人更高效治理。",
  "②上下级 / ③高管间", "m.x-techcon：追觅俞浩「高调战略」全员信息透明，每层级信息损耗20%破解（二手）"),
 ("iM金融黄秉宇董事长CEO Town Hall（digitaltoday·与百名员工面对面+互动公益+不限题QA）", "③", "二手",
  "iM金融董事长Town Hall：与约百名员工面对面听一线、轻互动(游戏/公益)破冰、不限题QA+现场颁奖，常态化沟通+文化载体。",
  "③高管间", "digitaltoday：iM金融黄秉宇董事长CEO Town Hall，与百名员工面对面+互动公益+不限题QA（二手）"),
 ("员工倾听策略：Town Hall + Skip-level（vantagecircle·跨越直属上级的倾听）", "②+③", "二手",
  "vantagecircle 倾听组合：Town Hall做全员开放对话+Skip-level高管越级听未过滤一线+360反馈+单一工具，双通道近现场。",
  "②上下级 / ③高管间", "vantagecircle：员工倾听策略 Town Hall+Skip-level，跨越直属上级的倾听（二手）"),
 ("全员会参与度度量与ROI（Airmeet·KPI/情绪/sentiment·会前会中会后三段）", "②", "二手",
  "Airmeet 度量：弃「出席率=参与」，盯投票参与/清晰度/eNPS/留存等KPI，会前兴趣→会中实时→会后情绪三段追踪+基准对比。",
  "②上下级", "Airmeet：全员会参与度度量与ROI（KPI/情绪/sentiment，会前会中会后三段）（二手）"),
 ("Slido for Microsoft Teams 一站式互动（blog.slido·投票/匿名QA/词云·远程与现场同权）", "②", "二手",
  "Slido嵌入Teams侧边栏跑投票/匿名Q&A/词云，远程现场同权(线上app/现场扫码)，20%时间给Q&A+匿名提真话率，原生免切屏。",
  "②上下级", "blog.slido：Slido for Teams 一站式互动（投票/匿名QA/词云，远程与现场同权）（二手）"),
 ("Vevox × Microsoft Teams 匿名投票问答（vevox·侧边栏集成·免切换屏幕）", "②", "二手",
  "Vevox集成Teams跑匿名投票/测验/Q&A不切屏，upvote排序+moderation，侧栏标签或九位码加入，作匿名互动底座。",
  "②上下级", "vevox：Vevox×Teams 匿名投票问答（侧边栏集成，免切换屏幕）（二手）"),
 ("全员会互动技巧2026（AhaSlides·匿名QA 74%、24h纪要、200人拆分组）", "②", "二手",
  "AhaSlides：开场投票/词云破冰、每10-15分钟重置注意力、匿名Q&A(74%更愿真话)、200人拆小组、会后24h recap。",
  "②上下级", "AhaSlides：全员会互动技巧（匿名QA 74%、24h纪要、200人拆分组）（二手）"),
 ("全员会 production 制胜（event.com.sg·音频/直播制作/混合平权/技术彩排）", "②", "二手",
  "event.com.sg：音频第一、直播多机位+稳定编码、全员技术彩排、混合专用远程moderator+远程问题进同一Q&A池，制作早规划。",
  "②上下级", "event.com.sg：全员会 production 制胜（音频/直播制作/混合平权/技术彩排）（二手）"),
 ("互动目标→形式匹配（event.com.sg·先定目标再选互动·避为花样而花样）", "②", "二手",
  "event.com.sg：先定目标(沟通/认可/文化/变革/知识)再选形式，匹配强化信息、为花样而花样则分散，认可段留给记忆点。",
  "②上下级", "event.com.sg：互动目标→形式匹配（先定目标再选互动，拒为花样而花样）（二手）"),
]

# ---------- 1) 汇总笔记：追加 R18 段 + 改 177→188 / 170→188 / +10→+11 ----------
s = open(SUMMARY, encoding='utf-8').read()
sec = "\n## 轮次 20260817（十八轮补采 +11）\n\n| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n"
for t, rd, sd, _, _, _ in CARDS:
    sec += "| %s | %s | %s |\n" % (t, rd, sd)
anchor = "## 适用与备注"
assert anchor in s, "summary note missing anchor"
s = s.replace(anchor, sec + "\n" + anchor, 1)
s = s.replace("全量 177 张见卡片墙 HTML", "全量 188 张见卡片墙 HTML", 1)
s = s.replace("（含本轮 +10）", "（含本轮 +11）", 1)
# 主表子标题计数对齐真实值
s = s.replace("③ 领导↔领导（高管间 · exec）— 50 卡", "③ 领导↔领导（高管间 · exec）— 60 卡", 1)
s = s.replace("② 领导↔员工（上下级 · supervisor）— 117 卡（本表增量更新，全量 117 张见卡片墙 HTML）",
              "② 领导↔员工（上下级 · supervisor）— 128 卡（本表增量更新，全量 128 张见卡片墙 HTML）", 1)
open(SUMMARY, 'w', encoding='utf-8').write(s)
print("summary note updated (+11 section, 177->188, subheads 60/128)")

# ---------- 2) 00 索引：在 "## 模板规范" 前追加 11 行 ----------
i0 = open(IDX00, encoding='utf-8').read()
rows = ""
for t, _, sd, _, rdisp, summ in CARDS:
    rows += "| %s（staff-meeting.html） | 4 | %s | %s | %s |\n" % (t, sd, rdisp, summ)
TEMPLATE = "## 模板规范"
assert TEMPLATE in i0, "00 index missing template anchor"
i0 = i0.replace("\n" + TEMPLATE, "\n" + rows + "\n" + TEMPLATE, 1)
open(IDX00, 'w', encoding='utf-8').write(i0)
print("00 index updated (+11 rows)")

# ---------- 3) 新建第十八轮独立笔记 ----------
os.makedirs(RUNS, exist_ok=True)
n3 = sum(1 for c in CARDS if '③' in c[1])
n2 = sum(1 for c in CARDS if '②' in c[1])
runnote = '''---
title: 员工大会-2026-08-17-第十八轮-知识卡
type: 自动化采集
date: 2026-08-17
tags: [知识采集, 员工大会, 十八轮]
relation: [supervisor, exec]
---

# 员工大会 · 第十八轮补采知识卡（2026-08-17，+11）

> 本轮独立页（GitHub Pages）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/runs/staff-meeting-2026-08-17-r18.html
> 本地路径：`knowledge-collection/staff-meeting/runs/staff-meeting-2026-08-17-r18.html`
> 累计总索引（卡片墙）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/staff-meeting.html

## 本轮 11 张卡（③高管间 5 / ②上下级 6，按受众关系分层，剔除①平级/朋友向）

| 卡 | 适用关系 | 一手/二手 | 一句话定位 |
|---|---|---|---|
'''
for t, rd, sd, ol, _, _ in CARDS:
    runnote += "| %s | %s | %s | %s |\n" % (t, rd, sd, ol)
runnote += '''
## 本轮侧重
- ③ 高管间：季度业务复盘新载体（customerexperience QBR 诚实暴露未达标+根因owner、toolkitcafe 一页纸定调页）+ 中国科技/金融 CEO 真实透明实践（追觅俞浩「每层级损耗20%」全员透明、iM金融黄秉宇百人面对面 Town Hall）+ 高管越级倾听（vantagecircle Town Hall+Skip-level 双通道）。
- ② 上下级：全员会「度量—工具—互动—制作」四件套补强——参与度度量与ROI（Airmeet KPI/情绪三段）、Teams 原生互动底座（Slido/Vevox 匿名投票Q&A免切屏）、全程结构化互动（AhaSlides 匿名74%+24h纪要+200人拆组）、现场制作与混合平权（event.com.sg 音频/直播/技术彩排）、互动「目标→形式」匹配设计。
- 硬约束已落实：剔除①平级/朋友向、家庭日/家属开放日、投资者/资本市场/IR 域；relation 仅 supervisor/exec；本轮全为二手权威源（外部方法论/工具官方/媒体案例）。
'''
path = os.path.join(RUNS, '员工大会-2026-08-17-第十八轮-知识卡.md')
open(path, 'w', encoding='utf-8').write(runnote)
print("round note created:", path, "| n3=%d n2=%d" % (n3, n2))
