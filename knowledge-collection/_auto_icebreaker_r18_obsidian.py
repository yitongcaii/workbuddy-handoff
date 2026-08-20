# -*- coding: utf-8 -*-
"""破冰 r18：更新 Obsidian 三端笔记（汇总/索引/轮次）。带幂等保护。"""
import os, io

def io_open(p):
    return io.open(p, encoding='utf-8').read().split('\n')
def io_write(p, lines):
    io.open(p, 'w', encoding='utf-8').write('\n'.join(lines))

VAULT = r'C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库'
SUM = os.path.join(VAULT, '素材', 'icebreaker', '破冰-知识卡汇总.md')
IDX = os.path.join(VAULT, '00-知识采集索引.md')
RUNS = os.path.join(VAULT, '素材', 'icebreaker', 'runs')
RUN_NOTE = os.path.join(RUNS, '破冰-2026-08-20-第十八轮-知识卡.md')

RUN_PAGE = 'https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/runs/icebreaker-2026-08-20-r18.html'
WALL_PAGE = 'https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/icebreaker.html'
LOCAL_RUN = 'knowledge-collection/icebreaker/runs/icebreaker-2026-08-20-r18.html'

rows = [
 ("新领导同化 NLA 流程·HR/OD 引导的团队对齐","③高管间","二手","NLA 四步：HR/OD 引导→无领导团队单独会议收真实顾虑→教练式反馈给领导→联合会对齐+共享协议；降低新领导早期失败率"),
 ("领导力入职 30-60-90 框架·听先于领导","③高管间","二手","领导入职四阶段：会前备30-60-90计划→D1-30听先于领导→D30-60定向与速赢→D60-90战略贡献；前30天只听不急着改"),
 ("高管入职 90 天·三阶段建信任不破势","③高管间","二手","高管入职三阶段：听学(D1-30,建心理安全)→对齐沟通(D31-60,可见速赢印证)→领导加速(D61-90)；避第一周大改等坑"),
 ("高管退修会 2.0·五步法+团队宪章（新 CEO 百天）","③高管间","二手","高影响力高管退修会五步：组织目的→团队目的(宪章)→角色问责→干系人对齐→学习绩效；新CEO前100天借退修会定调，会前诊断定议程"),
 ("高管 Offsite 规划·季度节奏+决策导向","③高管间","二手","高管 offsite 议程锚定「必做决策」而非汇报；季度节奏(Q1定方向/Q2评估/Q3重校/Q4复盘)防对齐漂移；领导归属感/信任为隐性产出"),
 ("高管 Offsite·四类挑战+3天结构","③高管间","二手","高管 offsite 面向四类拐点挑战(对齐/高压领导/转型/凝聚力)；3天递进：重对齐→凝聚力与判断→整合承诺；会前诊断+离场后整合成效"),
 ("团队宪章 Team Charter·共创北极星（目的/角色/决策/冲突）","②上下级","一手","Miro官方：团队宪章五要素(目标/角色/沟通/决策/冲突)；共创五步且全员签署；远程/分布式团队必做，定期回顾成活文档(一手)"),
 ("团队宪章分步指南·中立引导+绿卡/红卡行为","②上下级","二手","团队宪章七步：全员参与(中立引导师平衡声音)→定调→走模板(绿卡鼓励/红卡零容忍行为)→提示卡深化→清晰记录→让宪章活→约定回顾"),
 ("团队宪章 Wiki 模板·可复制的协作协议骨架","②上下级","二手","GitHub开源宪章wiki模板：成员/工作协议/分歧处理/沟通仪式/角色/反馈；把assume good intent翻转为防权力失衡写进协议，新经理拿来即用"),
 ("跨职能团队会议·破筒仓+三 Amigos（心理安全）","②上下级","二手","跨职能启动用三Amigos(开发+测试+产品)早协作破筒仓；验收标准/风险写码前定；retro含质量视角；结构化会议使生产bug降约40%"),
 ("项目 Kickoff 议程·RACI+决策日志（虚拟差异）","②上下级","二手","Kickoff议程含RACI；必产决策日志式文档(范围/RACI/决策/行动项)24h内发防争议；虚拟场加ground rules+co-host+实时共享+录像"),
 ("项目 Kickoff 议程·填例+可视化决策（60 分钟）","②上下级","二手","60分钟Kickoff十段；真实填例把out-of-scope/依赖/owner钉死；决策可视化记录+每段确认，防周三月翻案；远程共屏实时记录"),
]
r18_head = (' ｜ 十八轮补采 +12（2026-08-20）：团队宪章共创(Miro官方·一手)/分步指南(growth-space)/Wiki模板(GitHub)'
            '（②③）；新领导同化 NLA 流程(InstituteOD)/领导入职30-60-90(GalleryHR)/高管入职90天三阶段(NextOne)（③）；'
            '高管退修会2.0五步+团队宪章(Odgers)/季度节奏决策导向(Metavent)/四类挑战3天结构(ElliottRector)（③）；'
            '跨部门启动破筒仓(StudyRaid)/项目Kickoff RACI+决策日志(AlexBerman)/可视化决策(Laxis)（②）')
r18_desc = ('十八轮补采（+12，全二手除 Miro 宪章为官方一手）新开——团队宪章共创(Miro官方·一手)/分步指南(growth-space)/Wiki模板(GitHub)（②③）；'
            '新领导同化 NLA 流程(InstituteOD)/领导入职30-60-90框架(GalleryHR)/高管入职90天三阶段(NextOne)（③）；'
            '高管退修会2.0五步+团队宪章(Odgers)/季度节奏决策导向(Metavent)/四类挑战3天结构(ElliottRector)（③）；'
            '跨部门启动破筒仓(StudyRaid)/项目Kickoff RACI+决策日志(AlexBerman)/可视化决策(Laxis)（②）。')

# ---- 1. 汇总笔记（幂等）----
s = io_open(SUM)
changed = False
if '十八轮补采 +12（2026-08-20）' not in '\n'.join(s):
    for i,l in enumerate(s):
        if l.startswith('> 采集于'):
            s[i] = l.rstrip() + r18_head + '\n'; break
    s = [l.replace('## 卡片总表（156 卡 · 仅②/③）','## 卡片总表（168 卡 · 仅②/③）') for l in s]
    if not any(l.startswith('| 157 |') for l in s):
        s = s + [''] + ['| %d | %s | %s | %s | %s |' % (n,t,rel,src,core) for n,(t,rel,src,core) in enumerate(rows, start=157)]
    changed = True
io_write(SUM, s)

# ---- 2. 00-知识采集索引.md（幂等）----
ix = io_open(IDX)
# heading
for i,l in enumerate(ix):
    if l.startswith('## 主题：破冰（') and '十八轮补采 2026-08-20(+12)' not in l:
        ix[i] = l.rstrip() + ' ｜ 十八轮补采 2026-08-20(+12)）\n'; break
ix = [l.replace('**156 卡**','**168 卡**') for l in ix]
ix = [l.replace('③高管间 52 卡 / ②上下级 104 卡','③高管间 58 卡 / ②上下级 110 卡') for l in ix]
ix = [l.replace('一手 5 + 二手 151','一手 6 + 二手 162') for l in ix]
if r18_desc[:20] not in '\n'.join(ix):
    for i,l in enumerate(ix):
        if '十六轮补采（+7，全二手）新开' in l and '文化vitale' in l and r18_desc[:20] not in l:
            ix[i] = l.rstrip() + r18_desc; break
# 表格追加
if '团队宪章 Team Charter·共创北极星（icebreaker.html）' not in '\n'.join(ix):
    ib_start = next(i for i,l in enumerate(ix) if l.startswith('## 主题：破冰（'))
    tbl_rows = []
    for t,rel,src,core in rows:
        q = '5' if src=='一手' else '4'
        tbl_rows.append('| %s（icebreaker.html） | %s | %s | %s | %s |' % (t, q, src, rel, core))
    # 找 icebreaker 段落后第一个 `## 主题：`；没有则追加到文件末尾
    nx = None
    for i,l in enumerate(ix):
        if i>ib_start and l.startswith('## 主题：'):
            nx = i; break
    if nx is None:
        ix = ix + [''] + tbl_rows
    else:
        ix[nx:nx] = tbl_rows + ['']
io_write(IDX, ix)

# ---- 3. 轮次独立笔记 ----
os.makedirs(RUNS, exist_ok=True)
run_md = []
run_md.append('---')
run_md.append('title: 破冰·第十八轮知识卡（2026-08-20）')
run_md.append('tags: [知识采集, 自动化采集, 破冰, 团队信任, 上下级, 高管间]')
run_md.append('date: 2026-08-20')
run_md.append('type: 自动化采集')
run_md.append('relation: [supervisor, exec]')
run_md.append('source_topic: 破冰')
run_md.append('round: 18')
run_md.append('---')
run_md.append('')
run_md.append('# 破冰 · 第十八轮知识卡（2026-08-20）')
run_md.append('')
run_md.append('> 本轮 +12 卡（③高管间 6 / ②上下级 6），全二手除 Miro 团队宪章为官方一手；累计墙 168 卡（③58 / ②110）。')
run_md.append('')
run_md.append('**独立页（GitHub Pages）**：[%s](%s)' % (RUN_PAGE, RUN_PAGE))
run_md.append('**独立页（本机）**：`%s`' % LOCAL_RUN)
run_md.append('**累计总索引墙（GitHub Pages）**：[%s](%s)' % (WALL_PAGE, WALL_PAGE))
run_md.append('')
run_md.append('## 本轮 12 卡')
run_md.append('')
run_md.append('| # | 卡片 | 关系档 | 一手/二手 | 核心要点 |')
run_md.append('|---|---|---|---|---|')
for n,(t,rel,src,core) in enumerate(rows, start=1):
    run_md.append('| %d | %s | %s | %s | %s |' % (n, t, rel, src, core))
run_md.append('')
run_md.append('## 覆盖角度')
run_md.append('- **团队宪章 / Ways of Working 共创**（②③）：Miro 官方指南·五要素+全员签署 / growth-space 七步+绿红卡行为 / GitHub wiki 模板骨架——把隐性协作规则显性化。')
run_md.append('- **新领导融入 90 天**（③）：NLA 同化流程（HR/OD 引导+团队单独会议）/ 30-60-90 听先于领导框架 / 高管入职三阶段建信任不破势。')
run_md.append('- **高管退修会设计**（③）：Odgers 2.0 五步+团队宪章 / Metavent 季度节奏+决策导向 / ElliottRector 四类挑战+3天结构。')
run_md.append('- **跨部门 / 项目 Kickoff**（②）：StudyRaid 三 Amigos 破筒仓 / AlexBerman RACI+决策日志 / Laxis 填例+可视化决策。')
io_write(RUN_NOTE, run_md)

print('OK obsidian | summary_changed=%s idx_has_r18=%s run_note=%s' % (changed, '十八轮补采 2026-08-20(+12)' in '\n'.join(ix), os.path.exists(RUN_NOTE)))
