# -*- coding: utf-8 -*-
"""Generate weekly report HTML for the knowledge-collection (文化活动知识库) automation.
Week window: 2026-08-10 (Mon) ~ 2026-08-13 (Thu) — the period with independent-page mode
+ per-topic subfolders + LeXiang new-wall repair paradigm.
"""
import os

WEEK_LABEL = "2026-08-10 ~ 2026-08-13（周一~周四）"

# ---- current cumulative wall state (grep: class=hl / badge r3 / badge r2 / badge b1 / badge b2) ----
topics = [
    # slug, name, hl, r3, r2, b1, b2, week_new, weekly_rounds
    ("staff-meeting", "员工大会",      120, 39, 89, 31, 89, 47, "六/十/十一/十二轮 (+11/+12/+11/+13)"),
    ("offsite",       "Offsite 务虚",  72,  44, 28,  3, 69, 10, "七轮 (+10)"),
    ("icebreaker",    "破冰",          69,  21, 48,  5, 64, 25, "七/八/九轮 (+7/+11/+7)"),
    ("award",         "颁奖",          69,  31, 57, 11, 58,  0, "本周 enrich（无新采）"),
    ("openday",       "Open Day 开放日",51, 17, 46, 20, 31, 36, "十/十一/十二轮 (+11/+12/+13)"),
    ("afternoontea",  "下午茶研讨",    71,  24, 47, 12, 59,  0, "本周 enrich（无新采）"),
]

total_hl = sum(t[2] for t in topics)
total_r3 = sum(t[3] for t in topics)
total_r2 = sum(t[4] for t in topics)
total_b1 = sum(t[5] for t in topics)
total_b2 = sum(t[6] for t in topics)
week_new = sum(t[7] for t in topics)
prim_rate = total_b1 / total_hl * 100

# ---- weekly engineering milestones ----
milestones = [
    ("独立页改造", "08-10 16:45", "每轮轮询生成【当轮独立页】，累计墙转为总索引；支持 GitHub/Obsidian/乐享三端独立落库。"),
    ("历史墙拆分", "08-10 17:37", "6 主题合并大墙拆分为 27 个批次独立页 + 6 个分页索引页（按采集顺序从早到晚），每主题约 10~12 张/页。"),
    ("乐享分页补齐", "08-10 18:37", "发现 27 批次页此前未传乐享，自建 streamable-http 客户端把 28 个真实拆分页全部以 file 条目传入「分页独立页」子文件夹。"),
    ("按主题分子文件夹", "08-11", "乐享「待清洗素材」根目录改为 6 个主题子文件夹，每主题独立累计墙 + 轮次页，清理重复混乱。"),
    ("乐享 reorg 修复范式", "08-12~13", "旧累计墙屡因 reorg 失效（403 / 50021001），固化为「在子文件夹新建墙取代旧墙 + 更新 lexiang-entry-map」范式。"),
    ("GitHub 推送恢复", "08-12 11:09", "SSH 曾被网关重置阻断，网络恢复后重推成功；同步沉淀「乐享预签名 URL 含 AKID 严禁入 git」避坑规则。"),
]

# ---- three-end sync status ----
sync = [
    ("GitHub Pages", "✅ 已同步", "全量 452 卡 + 各主题 runs/ 独立页；push 4c3dded（含员工大会 r12）。"),
    ("Obsidian 知识采集库", "✅ 已同步", "6 主题汇总笔记 + 素材/<slug>/runs/ 轮次笔记；00-知识采集索引对齐。"),
    ("乐享「待清洗素材」", "✅ 已同步", "whoami 探活 code:0（面板 disconnected 为滞后误报）；6 子文件夹各含新建累计墙 + 本周轮次独立页。"),
]

# ---- highlight cards (this week's fresh picks) ----
highlights = [
    ("员工大会", "中交一航局官方全员会", "一手", "supervisor,exec", "央企官方 2026 工作会范式，作为员工大会真实案例沉淀。"),
    ("员工大会", "裁员后 Town Hall 沟通脚本", "二手", "exec", "unicornlabs 裁员后全员会逐字脚本，③高管间艰难消息沟通范式。"),
    ("员工大会", "新 CEO 上任内部传播四轨作战", "二手", "exec", "comm-ext 新领导更替内部传播框架，CEO 首百天沟通即战略。"),
    ("Open Day", "中国石化 2026 公众开放日", "二手", "supervisor", "胜利油田启动，央企媒体/客户/品牌开放日正规域。"),
    ("Open Day", "最高检检察开放日制度范式", "一手", "supervisor,exec", "spp.gov.cn 官方一手，政法开放日四级联动标准范式。"),
    ("Open Day", "腾讯企鹅 AI 开放日", "二手", "supervisor", "toutiao 转载，自家产品 AI 开放日，文化品牌向。"),
    ("Open Day", "南开/哈工大国家重点实验室开放日", "一手", "supervisor", "skleoc.nankai / mse.hit 官网一手，高校科研开放日。"),
    ("破冰", "阿里裸心会", "二手", "exec", "youjiangshi 高管层坦诚对话范式，替代幼稚破冰游戏。"),
    ("破冰", "高管 trust retreat 不靠游戏", "二手", "exec", "matthiasorgler 8 实践（Personal Histories/Lifeline/示弱）。"),
    ("Offsite", "美田集团组织诊断 + 字节 2025 务虚会", "一手", "exec", "new.qq 一手组织诊断 + 163 字节务虚会，战略解码真实案例。"),
]

def rel_badge(rel):
    if "exec" in rel and "supervisor" in rel:
        return '<span class="chip chip-r23">高管间·上下级</span>'
    if "exec" in rel:
        return '<span class="chip chip-r3">高管间</span>'
    return '<span class="chip chip-r2">上下级</span>'

def src_badge(src):
    return '<span class="chip chip-b1">一手</span>' if src == "一手" else '<span class="chip chip-b2">二手</span>'

rows = ""
for slug, name, hl, r3, r2, b1, b2, wn, wr in topics:
    pct_r3 = r3 / hl * 100
    pct_b1 = b1 / hl * 100
    rows += f"""
    <div class="trow">
      <div class="tname">{name}</div>
      <div class="tnum strong">{hl}</div>
      <div class="tnum">{wn}</div>
      <div class="tbar"><div class="fill r3" style="width:{pct_r3:.0f}%"></div><span>③ {r3}</span></div>
      <div class="tbar"><div class="fill r2" style="width:{r2/hl*100:.0f}%"></div><span>② {r2}</span></div>
      <div class="tbar"><div class="fill b1" style="width:{pct_b1:.0f}%"></div><span>一手 {b1}</span></div>
      <div class="tweek">{wr}</div>
    </div>"""

mil_html = ""
for i, (t, d, desc) in enumerate(milestones, 1):
    mil_html += f"""
    <div class="mil">
      <div class="mil-no">{i}</div>
      <div class="mil-body"><div class="mil-h"><b>{t}</b><span class="mil-d">{d}</span></div><div class="mil-desc">{desc}</div></div>
    </div>"""

sync_html = ""
for name, st, desc in sync:
    sync_html += f"""
    <div class="sync"><div class="sync-h"><b>{name}</b><span class="sync-st">{st}</span></div><div class="sync-desc">{desc}</div></div>"""

hl_html = ""
for topic, title, src, rel, desc in highlights:
    hl_html += f"""
    <div class="hcard">
      <div class="htop"><span class="htopic">{topic}</span>{src_badge(src)}{rel_badge(rel)}</div>
      <div class="htitle">{title}</div>
      <div class="hdesc">{desc}</div>
    </div>"""

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>知识采集库 · 本周周报（{WEEK_LABEL}）</title>
<style>
  :root{{--c1:#7c5cff;--c2:#19c2c9;--bg:#f6f7fb;--ink:#1f2440;--mut:#6b7290;--card:#fff;}}
  *{{box-sizing:border-box;margin:0;padding:0}}
  body{{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:var(--bg);color:var(--ink);padding:32px 20px 60px;line-height:1.6}}
  .wrap{{max-width:1080px;margin:0 auto}}
  .hero{{background:linear-gradient(120deg,var(--c1),var(--c2));color:#fff;border-radius:24px;padding:34px 36px;box-shadow:0 18px 40px rgba(124,92,255,.25)}}
  .hero h1{{font-size:27px;letter-spacing:.5px;margin-bottom:8px}}
  .hero .sub{{opacity:.92;font-size:14px}}
  .kpis{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin:22px 0}}
  .kpi{{background:var(--card);border-radius:18px;padding:18px 16px;box-shadow:0 6px 18px rgba(31,36,64,.06);border-top:4px solid var(--c1)}}
  .kpi:nth-child(2){{border-top-color:var(--c2)}}
  .kpi:nth-child(3){{border-top-color:#ff9d54}}
  .kpi:nth-child(4){{border-top-color:#3ecf8e}}
  .kpi .v{{font-size:30px;font-weight:800;background:linear-gradient(120deg,var(--c1),var(--c2));-webkit-background-clip:text;background-clip:text;color:transparent}}
  .kpi .l{{font-size:13px;color:var(--mut);margin-top:4px}}
  .sec-t{{font-size:18px;font-weight:800;margin:30px 4px 14px;display:flex;align-items:center;gap:8px}}
  .sec-t::before{{content:"";width:8px;height:20px;border-radius:4px;background:linear-gradient(var(--c1),var(--c2))}}
  .panel{{background:var(--card);border-radius:18px;padding:8px 18px;box-shadow:0 6px 18px rgba(31,36,64,.06)}}
  .trow{{display:grid;grid-template-columns:1.3fr .6fr .6fr 1.5fr 1.5fr 1.5fr 1.6fr;align-items:center;gap:8px;padding:12px 4px;border-bottom:1px solid #eef0f6}}
  .trow:last-child{{border-bottom:none}}
  .tname{{font-weight:700}}
  .tnum{{font-weight:700;text-align:center;color:var(--mut)}}
  .tnum.strong{{color:var(--c1);font-size:17px}}
  .tbar{{position:relative;height:18px;background:#eef0f6;border-radius:9px;overflow:hidden;font-size:11px;color:#3a4060}}
  .tbar .fill{{position:absolute;left:0;top:0;height:100%;border-radius:9px}}
  .tbar .fill.r3{{background:linear-gradient(90deg,#a78bfa,#7c5cff)}}
  .tbar .fill.r2{{background:linear-gradient(90deg,#ffb074,#ff9d54)}}
  .tbar .fill.b1{{background:linear-gradient(90deg,#5be3a0,#3ecf8e)}}
  .tbar span{{position:relative;z-index:2;padding-left:8px;line-height:18px}}
  .tweek{{font-size:11px;color:var(--mut)}}
  .grid2{{display:grid;grid-template-columns:1fr 1fr;gap:14px}}
  .mil{{display:flex;gap:12px;background:var(--card);border-radius:16px;padding:14px 16px;box-shadow:0 6px 18px rgba(31,36,64,.06)}}
  .mil-no{{flex:0 0 30px;height:30px;border-radius:50%;background:linear-gradient(120deg,var(--c1),var(--c2));color:#fff;font-weight:800;display:flex;align-items:center;justify-content:center;font-size:14px}}
  .mil-body{{flex:1}}
  .mil-h{{display:flex;justify-content:space-between;align-items:baseline}}
  .mil-h b{{font-size:15px}}
  .mil-d{{font-size:12px;color:var(--c2);font-weight:700}}
  .mil-desc{{font-size:13px;color:var(--mut);margin-top:3px}}
  .sync{{background:var(--card);border-radius:16px;padding:14px 16px;box-shadow:0 6px 18px rgba(31,36,64,.06);border-left:4px solid #3ecf8e}}
  .sync-h{{display:flex;justify-content:space-between;align-items:baseline}}
  .sync-st{{color:#1a9e63;font-weight:800;font-size:13px}}
  .sync-desc{{font-size:13px;color:var(--mut);margin-top:4px}}
  .hgrid{{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}}
  .hcard{{background:var(--card);border-radius:16px;padding:15px 16px;box-shadow:0 6px 18px rgba(31,36,64,.06);border-top:3px solid var(--c1)}}
  .htop{{display:flex;align-items:center;gap:6px;flex-wrap:wrap;margin-bottom:6px}}
  .htopic{{font-size:12px;font-weight:800;color:var(--c2)}}
  .htitle{{font-size:15px;font-weight:700;margin-bottom:4px}}
  .hdesc{{font-size:12.5px;color:var(--mut)}}
  .chip{{font-size:11px;padding:2px 9px;border-radius:999px;font-weight:700}}
  .chip-r3{{background:#efe7ff;color:#7c5cff}}
  .chip-r2{{background:#ffeede;color:#e07b1f}}
  .chip-r23{{background:#e7f0ff;color:#3a6fd8}}
  .chip-b1{{background:#e3faf0;color:#1a9e63}}
  .chip-b2{{background:#fff3e0;color:#d98a1f}}
  .note{{background:#fff8ec;border-left:4px solid #ff9d54;border-radius:12px;padding:14px 16px;font-size:13px;color:#8a5a16;margin-top:6px}}
  .note b{{color:#a8631a}}
  .footer{{text-align:center;color:var(--mut);font-size:12.5px;margin-top:34px;padding-top:18px;border-top:1px solid #eef0f6}}
</style>
</head>
<body>
<div class="wrap">
  <div class="hero">
    <h1>📚 文化活动知识采集库 · 本周周报</h1>
    <div class="sub">统计周期：{WEEK_LABEL} ｜ 6 主题自动化轮询（6h/轮）｜ 关系档：仅 ②上下级 + ③高管间（剔除①平级/朋友向）</div>
  </div>

  <div class="kpis">
    <div class="kpi"><div class="v">{total_hl}</div><div class="l">全库累计知识卡</div></div>
    <div class="kpi"><div class="v">{week_new}</div><div class="l">本周新增（净增）</div></div>
    <div class="kpi"><div class="v">6</div><div class="l">覆盖主题数</div></div>
    <div class="kpi"><div class="v">{prim_rate:.0f}%</div><div class="l">一手源占比（{total_b1} 张）</div></div>
  </div>

  <div class="sec-t">主题进度概览</div>
  <div class="panel">
    <div class="trow" style="color:var(--mut);font-size:12px;font-weight:700;border-bottom:2px solid #e6e9f2">
      <div>主题</div><div class="tnum">累计</div><div class="tnum">本周</div>
      <div>③ 高管间</div><div>② 上下级</div><div>一手源</div><div>本周轮次</div>
    </div>
    {rows}
  </div>

  <div class="sec-t">本周工程里程碑</div>
  <div class="grid2">
    {mil_html}
  </div>

  <div class="sec-t">三端同步状态</div>
  <div class="grid2">
    {sync_html}
  </div>

  <div class="sec-t">本周高光卡精选（10 张）</div>
  <div class="hgrid">
    {hl_html}
  </div>

  <div class="sec-t">数据债 / 待办</div>
  <div class="note">
    <b>① icebreaker：</b>44 张墙卡在 index.json 中 topic=None（R8 重建墙未全量回填标签），墙本身 69 卡完整、去重以墙为准不受影响，下次轮次补一轮 topic 回填。<br>
    <b>② index.json topic 标签不全：</b>offsite/award 等部分条目 topic=None，全量 451 条与墙 452 卡差 1 为数据债，不影响展示。<br>
    <b>③ 乐享旧墙残留：</b>各主题此前累计墙因 reorg 失效（403 / 50021001），已新建墙取代，lexiang-entry-map 内残留失效 entry 待清理标记。<br>
    <b>④ Open Day 累计墙 a6ba9c18 仍有效：</b>其余各主题新墙 in-place 更新中，reorg 时需复跑「新建取代」范式。
  </div>

  <div class="footer">📌 本页由 yitong 沉淀整理 · 文化活动知识库</div>
</div>
</body>
</html>"""

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "weekly-report-2026-08-10_13.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(html)
print("written:", out, "| bytes:", len(html.encode("utf-8")))
print(f"totals: hl={total_hl} r3={total_r3} r2={total_r2} b1={total_b1} b2={total_b2} week_new={week_new} prim%={prim_rate:.1f}")
