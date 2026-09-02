# -*- coding: utf-8 -*-
# 修正 r32：删墙里重复 CFO 卡（与旧卡同 URL affinitytravel），计数回退 +5
import os, re, subprocess

KC = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(KC, "offsite", "offsite.html")
TMP = os.path.join(KC, "offsite", ".run_newcards.tmp.html")
OBS_SUM = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\offsite\Offsite-团建务虚-知识卡汇总.md"
OBS_00 = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
RUNS_NOTE = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\offsite\runs\Offsite-2026-09-02-第三十二轮-知识卡.md"
RUNPAGE = os.path.join(KC, "offsite", "runs", "offsite-2026-09-02-r32.html")

CFO_URL = "affinitytravel.co/blog/how-to-build"

def find_blocks(html):
    blocks = []
    for m in re.finditer(r'<div class="hl">', html):
        s = m.start(); i = m.end(); d = 1; j = i
        while j < len(html):
            if html[j:j+4] == '<div':
                d += 1; j += 4
            elif html[j:j+5] == '</div':
                d -= 1; j += 6
            else:
                j += 1
            if d == 0:
                break
        blocks.append((s, j))
    return blocks

# ---------- 1) 墙：删最后一个 CFO 重复卡 ----------
html = open(WALL, encoding="utf-8").read()
before = html.count('<div class="hl">')
blocks = find_blocks(html)
href_sub = f'href="https://www.{CFO_URL}'
dup_idx = [k for k, b in enumerate(blocks) if href_sub in html[b[0]:b[1]]]
print("dup CFO block indices (href match):", dup_idx)
# 真实 3 个：173=旧立项卡 / 207=中层对齐Lab(不同主题,同源但非重复) / 228=本轮注入的CFO重复卡
# dup 判据：标题主题相同(均=向CFO争取offsite预算论证) → 173 与 228 重复，删后注入的 228，留更早更全的 173；207 主题不同保留。
assert len(dup_idx) >= 2, f"预期 ≥2 个 CFO 卡(href)，实际 {len(dup_idx)}"
assert html[blocks[dup_idx[-1]][0]:blocks[dup_idx[-1]][1]].count('向 CFO/财务争取 Offsite 预算批准') >= 1
k = dup_idx[-1]  # 删除最后注入的重复卡
s, e = blocks[k]
html = html[:s] + html[e:]
after = html.count('<div class="hl">')
print(f"[wall] hl before={before} after={after}")
# 计数回退
html = html.replace(">137 卡<", ">136 卡<", 1)
html = html.replace(">95 卡<", ">94 卡<", 1)
# hero 回退 +7 -> +5 并去掉 CFO
hero_old = " ｜ 2026-09-02 三十二轮补采 +7（神经多元友好型offsite/向CFO争取预算批准商业论证框架/团队对齐工作坊决策非讨论/绿色可持续offsite落地/2026 ELT务虚室5现场信号/专业务虚执行vs内部DIY）"
hero_new = " ｜ 2026-09-02 三十二轮补采 +5（神经多元友好型offsite/团队对齐工作坊决策非讨论/绿色可持续offsite落地/2026 ELT务虚室5现场信号/专业务虚执行vs内部DIY）"
assert hero_old in html, "hero_old not found"
html = html.replace(hero_old, hero_new, 1)
open(WALL, "w", encoding="utf-8").write(html)
print("[wall] sec3=136 sec2=94 total=", html.count('<div class="hl">'))

# ---------- 2) TMP：去掉 CFO 块，重生成独立页 ----------
tmp_blocks = find_blocks(open(TMP, encoding="utf-8").read())
tmp_html = open(TMP, encoding="utf-8").read()
tmp_dup = [k for k, b in enumerate(tmp_blocks) if href_sub in tmp_html[b[0]:b[1]]]
assert len(tmp_dup) == 1
ts, te = tmp_blocks[tmp_dup[0]]
new_tmp = tmp_html[:ts] + tmp_html[te:]
open(TMP, "w", encoding="utf-8").write(new_tmp)
print("[tmp] cards now=", new_tmp.count('<div class="hl">'))
r = subprocess.run(
    ["python", os.path.join(KC, "gen_run_page.py"),
     "--topic", "offsite", "--topic-name", "Offsite 团建务虚",
     "--date", "2026-09-02", "--round", "32",
     "--cards-file", TMP, "--out", RUNPAGE],
    capture_output=True, text=True, shell=True,
)
print("[run-page]", r.returncode, r.stdout.strip(), r.stderr.strip()[:200])

# ---------- 3) 汇总笔记 ----------
s = open(OBS_SUM, encoding="utf-8").read()
s = s.replace("· 知识卡汇总（232 卡", "· 知识卡汇总（230 卡", 1)
s = s.replace("二手 260。", "二手 258。", 1)
s = s.replace(
    "三十一轮补采 +8（高管冲突治理/决策机制operating model/多新成员团队/心理安全前置+经理难对话/30-60-90落地/团队章程/混合远程平权） ｜ 2026-09-02 三十二轮补采 +7（神经多元友好型offsite/向CFO争取预算批准商业论证框架/团队对齐工作坊决策非讨论/绿色可持续offsite落地/2026 ELT务虚室5现场信号/专业务虚执行vs内部DIY）卡片墙 HTML：",
    "三十一轮补采 +8（高管冲突治理/决策机制operating model/多新成员团队/心理安全前置+经理难对话/30-60-90落地/团队章程/混合远程平权） ｜ 2026-09-02 三十二轮补采 +5（神经多元友好型offsite/团队对齐工作坊决策非讨论/绿色可持续offsite落地/2026 ELT务虚室5现场信号/专业务虚执行vs内部DIY）卡片墙 HTML：", 1)
# 去掉 r32 section 里的 CFO 行
s = s.replace("| 向 CFO/财务争取 Offsite 预算批准的商业论证框架（offsite.html） | 上下级 | 二手 |\n", "")
open(OBS_SUM, "w", encoding="utf-8").write(s)
print("[obs-sum] fixed")

# ---------- 4) 00 索引 ----------
z = open(OBS_00, encoding="utf-8").read()
z = z.replace("**232 卡**（2026-08-07 首采", "**230 卡**（2026-08-07 首采", 1)
z = z.replace(
    "2026-09-02 三十一轮补采 +8（高管冲突治理/决策机制operating model/多新成员团队/心理安全前置+经理难对话/30-60-90落地/团队章程/混合远程平权） ｜ 2026-09-02 三十二轮补采 +7（神经多元友好型offsite/向CFO争取预算批准商业论证框架/团队对齐工作坊决策非讨论/绿色可持续offsite落地/2026 ELT务虚室5现场信号/专业务虚执行vs内部DIY），已按「受众关系分层」",
    "2026-09-02 三十一轮补采 +8（高管冲突治理/决策机制operating model/多新成员团队/心理安全前置+经理难对话/30-60-90落地/团队章程/混合远程平权） ｜ 2026-09-02 三十二轮补采 +5（神经多元友好型offsite/团队对齐工作坊决策非讨论/绿色可持续offsite落地/2026 ELT务虚室5现场信号/专业务虚执行vs内部DIY），已按「受众关系分层」", 1)
z = z.replace("二手 228。按关系分层：③高管间 137 卡 / ②上下级 95 卡。",
              "二手 226。按关系分层：③高管间 136 卡 / ②上下级 94 卡。", 1)
z = z.replace("| 向 CFO/财务争取 Offsite 预算批准商业论证（支出重构为资本投资/留人成本$50-200k/真实ROI非感受）（offsite.html） | 4 | 二手 | ②上下级 | 重构为资本投资非文化费用;CFO三数(留人/敬业23%/59%增预算);事前定指标+问业务问题非感受 |\n", "")
open(OBS_00, "w", encoding="utf-8").write(z)
print("[obs-00] fixed")

# ---------- 5) runs 独立笔记 ----------
note = (
    "---\n"
    "title: Offsite-2026-09-02-第三十二轮-知识卡\n"
    "type: 自动化采集\n"
    "date: 2026-09-02\n"
    "tags: [知识采集, Offsite, 三十二轮]\n"
    "relation: [supervisor, exec]\n"
    "---\n\n"
    "# Offsite 团建务虚 · 第三十二轮补采（2026-09-02，+5）\n\n"
    "- **GitHub Pages 独立页**：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/offsite/runs/offsite-2026-09-02-r32.html\n"
    "- **本地路径**：`knowledge-collection/offsite/runs/offsite-2026-09-02-r32.html`\n"
    "- **累计卡片墙（总索引）**：`knowledge-collection/offsite/offsite.html`（[线上](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/offsite/offsite.html)）\n"
    "- **覆盖关系档**：③高管间 2 卡 / ②上下级 3 卡（无①平级）\n"
    "- **去重**：CFO 预算论证卡（affinitytravel 同 URL）与墙内旧卡「Offsite 立项商业论证·一页 business case 拿 CFO 签字」判重复，留旧删新，本轮净增 5 卡。\n"
    "- **乐享团队文件夹**：待清洗素材·Offsite 子目录（仅每轮独立页，token 失效待补传）\n\n"
    "## 本轮新增 5 卡\n\n"
    "| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n"
    "| 神经多元友好型 Offsite（包容性设计） | 上下级 | 二手 |\n"
    "| 团队对齐工作坊（决策非讨论/3-5 rocks/单一owner） | 上下级 | 二手 |\n"
    "| 绿色/可持续 Offsite 落地（eco认证/低废弃/本地采购/碳抵消） | 上下级 | 二手 |\n"
    "| 2026 ELT 务虚室现场信号 5 模式（AI/集体团队动力学/双轨视野） | 高管间 | 二手 |\n"
    "| 专业务虚执行 vs 内部 DIY（战略意图倒推/会后问责KPI） | 高管间 | 二手 |\n\n"
    "> 本笔记仅索引，不拷 HTML 副本；完整卡片见上方 GitHub Pages 独立页。\n"
)
open(RUNS_NOTE, "w", encoding="utf-8").write(note)
print("[runs-note] rewrote +5")
print("DONE")
