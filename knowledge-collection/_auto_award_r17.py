# -*- coding: utf-8 -*-
"""知识采集自动化 · 颁奖 十七轮 enrich（2026-08-18）。
生成增量页 + 追加汇总页 + 更新 index.json + Obsidian 笔记 + 00索引。"""
import os, json

WS = r"C:\Users\v_yitcai\WorkBuddy\20260728154244"
KC = os.path.join(WS, "knowledge-collection")
AWARD = os.path.join(KC, "award")
AWARD_HTML = os.path.join(AWARD, "award.html")
IDX = os.path.join(KC, "index.json")
RUN_NAME = "award-20260818.html"
RUN_PATH = os.path.join(AWARD, RUN_NAME)
NOTE = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\award\颁奖-知识卡汇总.md"
IDX00 = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
GP = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection"

# ---- 6 张新卡（剔除 peer，仅 ②supervisor / ③exec）----
CARDS = [
  dict(emoji="🛡️", title="颁奖典礼危机预案·技术故障/人员缺席/信息错漏应急响应", cat="风险管理", rel="r2",
       url="https://m.renrendoc.com/paper/492662828.html",
       val="颁奖/晚会现场的高频风险与标准应对——①设备故障（音响/灯光/投影/提词器）：技术组「双路热备」（主控+备用电脑同时连投影一键切换），核心功能故障后 5 分钟内恢复，备用无线麦≥2 充好电+讲台有线麦作「最后防线」；②人员缺席（获奖者/嘉宾/主持突发不到）：提前确认替补名单+临时调整方案，AB角交叉核对获奖名单与奖金发放；③信息错漏（名单/职位/奖项）：建立三级审核（原始录入→系统校验→人工终核），获奖名单宣读等关键环节 AB 角交叉核对；④医疗突发：现场配 AED+急救员，签就近医院合作协议；⑤舆情争议：预置公关声明模板+指定发言人，实时监测社媒。还含动线彩排（单侧入场-环形流动-多出口）、VIP/媒体/观众分区避免人流交叉。",
       inner="办颁奖前必做「风险清单+应急预案」：设备双备份+技术待命、替补名单、名单三级审核、AED/医疗点、舆情话术库；彩排阶段模拟断电/设备超负荷等极端情况做压力测试；核心环节（颁奖音乐/名单展示）线上线下两套方案可无缝切换。经理/HR 用这套替代「出事再救火」。",
       note="适用：② 经理/HR 主导的现场执行，把「颁奖翻车」从概率事件变成可控风险（③ 高管在场时事故影响放大，预案是硬底线）。"),
  dict(emoji="🎯", title="OKR与表彰闭环·「Recognition Rumble」游戏化跨部门认可+高管参与", cat="绩效闭环", rel="r3",
       url="https://www.betterworks.com/magazine/2025-performance-innovation-award-winners",
       val="Betterworks 2025「Make Work Better」奖案例——Sinclair Broadcast Group 把认可与 OKR 框架深度绑定：设计类似「NCAA 疯狂三月」的「Recognition Rumble」对决赛，游戏化跨部门认可，配周更+团队荣誉感+高管参与；VP of Business Transformation、OKR 总监、Program Analyst 三方牵头。结果：3 个月录得 2200+ 次认可、用户参与率从 ~4% 飙到 84%，把「达成 OKR 才配被看见」做成全员文化。核心洞察：OKR 是团队事件，认可要让「一起达成目标的人彼此庆祝」，高管卷入是把认可从 HR 事务升为战略信号的关键。",
       inner="把年度/季度表彰接进 OKR 节奏：设「OKR 大使奖/优秀团队奖」等以荣誉为主的奖项（参考旭辉 OKR 大使奖，每季度激励对 OKR 的理解与贡献）；用游戏化（bracket/积分榜）拉跨部门认可参与度；高管亲自下场颁奖/致辞传递「目标达成被看见」；让认可直接挂在目标与关键结果上（如 Profit.co 把 recognition 建在 OKR 工作流内）。",
       note="适用：③ 高管/HR 负责人把表彰接成战略执行杠杆，让 OKR 不再「考核完就忘」，用荣誉闭环强化目标共识。"),
  dict(emoji="🌍", title="全球/跨国颁奖包容性体验·时区/多语言/文化敏感/多元评审", cat="全球包容", rel="r3",
       url="https://awardforce.com/blog/articles/how-to-create-an-inclusive-awards-experience-for-a-global-audience",
       val="Award Force（全球评奖平台）给跨国颁奖的包容性清单——①多语言体验：数字材料多语种、用多语言评奖系统让参赛者/评委用母语导航，破除语言壁垒；②无障碍：键盘导航/读屏兼容/WCAG 2.2/移动友好，收费分层（免/低/阶梯）防经济排斥；③支付便利：多币种收款，避免跨境汇率隐藏费劝退发展中地区参赛者；④文化敏感：表单用文化适配术语、评委做包容培训、奖品按地区价值偏好定制（非一刀切）；⑤动态评估：多元评委 panel（「卓越有多种面孔」）、context-aware 加权评分（既看结果也看所走之路，避免只赞特权、忽略坚守）。核心：跨国颁奖要让人「被看见、被尊重」，而非被主流语言/时区/货币边缘化。",
       inner="办跨国/全球颁奖时：材料与系统多语种；选稳定可交互平台并配同声传译（如有外宾）；时区上给亚洲/澳洲等不便地区单独场次或回放（参考 Gallup「做两场」——一场覆盖欧洲、一场覆盖亚洲）；评委 panel 多元+context-aware 评分；奖品/术语按地区文化适配；用多币种/分层收费降低参与门槛。",
       note="适用：③ 高管/全球 HR 视角，把颁奖做成「无边界包容」而非「总部中心」，与虚拟/混合运营互补解决远程者被忽略。"),
  dict(emoji="🎬", title="员工荣誉视频SOP·标准化模板与制作流程", cat="视频SOP", rel="r2",
       url="https://wap.jiandaoyun.com/nblog/63369/",
       val="员工荣誉视频的标准化制作：①明确用途与受众（内部激励月度表彰 / 外部招聘推介）；②脚本大纲（开场→介绍→事迹→领导讲话→结尾祝福），列出所需素材（照片/短视频/文字）；③收集素材（获奖者工作影像+团队祝福语音/文字+公司 VI）；④初稿（Premiere/剪映套标准化结构+转场，分层布局）；⑤审核（邀 HR/相关部门核真实性与合规）；⑥输出多分辨率（内网公告栏/外部社媒同步）。风格按场景选：正式典礼型（年度盛典/大型表彰，仪式感强）/温情故事型（个人专访，强调成长）/创意趣味型（青年榜单）/动态数据型（销售业绩）。避坑：信息不完整、模板呆板、流程繁琐、品牌割裂——用标准化采集表单+预设可变字段一键填充+企业 VI 规范包解决。",
       inner="给获奖者拍荣誉视频走标准 SOP：提前 2 周启动、每人半天拍摄（工作素材+同事采访+领导点评）、剪辑后由本人确认避免信息错；按场景选风格（年度盛典正式型开场+穿插温情访谈）；用标准化模板+品牌 VI 包保证一致性；多分辨率导出适配内网/社媒。经理/HR 用这套把「念名字」升级为「看见他为什么优秀」。",
       note="适用：② 经理/HR 主导的荣誉视频制作，把颁奖从「名单朗读」变成「故事可视化」（③ 高管讲话片段是战略传递载体）。"),
  dict(emoji="💰", title="认可项目ROI·给CFO的财务商业论证结构", cat="预算ROI", rel="r3",
       url="https://ribirewards.com/blog/the-roi-of-employee-recognition-what-finance-actually-needs-to-see",
       val="向财务/CFO 证明认可预算的商业论证框架（RibiRewards）——Finance 不要「文化/士气」空话，要硬数据。结构化提案：①用财务语言定义问题（「去年走了 18 人 × $30k 替换成本=$540k 离职成本；离职访谈 60% 提『缺乏认可』」）；②列明投入（奖励 $10k+平台 $2k+管理 $3k=$15k）；③保守预测（研究指认可降自愿离职 15-30%；若多留 3 人省 $90k，ROI 500%）；④定义成功指标（自愿离职率/参与度/填补周期，季度追踪，12 月无 10% 改善则复盘）；⑤先 6 月试点（销售团队 20 人 $3k）再全公司铺开。关键：用本公司真实离职率与替换成本，行业均值说服不了 CFO。",
       inner="申请认可预算前，按「问题($)→投入→保守回报→成功指标→试点」五段写商业论证；用真实离职/替换成本而非行业均值；把节省（留存/招聘成本/生产率）量化成 CFO 语言；设明确复盘阈值（如 12 月留失无 ≥10% 改善就重估）；先用小团队 pilot 验证再全量。",
       note="适用：③ 高管/HR 向财务要预算的论证模板，把「认可」从 nice-to-have 变成可防守的战略投资。"),
  dict(emoji="📊", title="认可ROI运营模型·季度复算与可defending假设", cat="效果衡量", rel="r3",
       url="https://laud.cloud/employee-recognition-program-roi-metrics-formulas-and-benchmarks",
       val="认可 ROI 不是一次性 PPT，而是「活文档」运营模型（Laud.cloud）——示例：内部替换成本 $12k/人，避免 2 次离职省 $24k，年成本（软件 $6k+管理 $2.5k+奖励 $3k=$11.5k），ROI 109%；若不确定两次离职都受认可影响，就只模型 1 次并给高低两情景。关键纪律：①变更软件/定价/人数/混合办公时重算；②季度复盘（更新成本/刷新参与率·经理采纳·认可频率/看结果/查归因是否合理/调低中高情景）；③用一页总结成本·收益·假设·下一步；④每季末问「下季什么最能提 ROI」——答案常不是「花更多」，而是提经理采纳/降发布摩擦/更强 spotlight 平台/标准化类别。",
       inner="把认可 ROI 当运营模型而非一次汇报：定义 1 个成本基线+1 个效率指标+1 个人才结果，连续测 2-3 期；每季度复算（成本/参与/留任/归因）；给低·预期·高三情景而非单点；用保守归因（不确定就只算 1 次影响）；末了用一问驱动下一季优化（提经理采纳 > 加预算）。",
       note="适用：③ 高管/HR 运营认可项目，让 ROI 可 defending、可迭代，预算申请有持续数据支撑。"),
]

def card_html(c, in_grid=True):
    badges = f'<span class="badge {c["rel"]}">{"高管间" if c["rel"]=="r3" else "上下级"}</span><span class="badge b2">二手</span>'
    return f'''    <div class="hl">
      <div class="top"><span class="emoji">{c["emoji"]}</span><h3>{c["title"]}</h3><span class="cat">{c["cat"]}</span>{badges}</div>
      <p class="val">{c["val"]}</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">{c["inner"]}</div></details>
      <div class="src">🔗 <a href="{c["url"]}" target="_blank">{c["url"]}</a></div>
      <div class="note">适用：{c["note"]}</div>
    </div>'''

# ---------- 1) 增量页 ----------
sec3_cards = [c for c in CARDS if c["rel"]=="r3"]
sec2_cards = [c for c in CARDS if c["rel"]=="r2"]
inc_grid = "\n".join(card_html(c) for c in CARDS)
inc_html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>颁奖典礼 · 十七轮增量卡片（2026-08-18）</title>
<style>
:root{{--bg:#f4f6fb;--card:#ffffff;--ink:#1f2430;--sub:#5b6478;--accent:#6c5ce7;--accent2:#00b8d9;--chip:#eef0ff;}}
*{{box-sizing:border-box;margin:0;padding:0;}}
body{{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:linear-gradient(135deg,#eef1ff 0%,#e6f7ff 100%);color:var(--ink);padding:28px 18px;line-height:1.6;}}
.wrap{{max-width:1080px;margin:0 auto;}}
.hero{{background:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);border-radius:22px;padding:26px 30px;color:#fff;box-shadow:0 14px 40px rgba(108,92,231,.25);margin-bottom:22px;}}
.hero h1{{font-size:24px;font-weight:800;letter-spacing:1px;margin-bottom:6px;}}
.hero p{{font-size:13px;opacity:.95;}}
.relbar{{display:flex;gap:10px;flex-wrap:wrap;margin-top:12px;}}
.relbar span{{background:rgba(255,255,255,.2);border-radius:20px;padding:5px 14px;font-size:13px;font-weight:600;}}
.grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;}}
.hl{{background:var(--card);border-radius:18px;padding:18px 18px 16px;border-top:4px solid var(--accent);box-shadow:0 10px 32px rgba(108,92,231,.10);display:flex;flex-direction:column;gap:9px;}}
.top{{display:flex;align-items:center;gap:8px;flex-wrap:wrap;}}
.emoji{{font-size:22px;}}
.hl h3{{font-size:16px;font-weight:700;flex:1;min-width:120px;}}
.cat{{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:600;background:var(--chip);color:var(--accent);}}
.badge{{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:700;}}
.b2{{background:#fff1e6;color:#c0651a;}}
.r2{{background:#fff3e0;color:#c0651a;}}
.r3{{background:#f3e8ff;color:#7b2cbf;}}
.val{{font-size:13.5px;color:var(--sub);}}
.exec{{margin-top:2px;border-top:1px dashed #e2e8f0;padding-top:8px;}}
.exec summary{{cursor:pointer;font-size:13px;font-weight:600;color:var(--accent);}}
.exec .inner{{font-size:13px;color:var(--sub);margin-top:6px;padding-left:4px;}}
.src{{font-size:12px;word-break:break-all;}}
.src a{{color:var(--accent2);text-decoration:none;}}
.note{{font-size:12px;color:#94a3b8;border-left:3px solid #e2e8f0;padding-left:8px;}}
footer{{text-align:center;padding:24px;color:#94a3b8;font-size:13px;border-top:1px solid #e2e8f0;margin-top:40px;}}
</style>
</head><body>
<div class="wrap">
<p style="margin:0 0 16px"><a href="{GP}/award/award.html" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">🏆 返回颁奖累计卡片墙 →</a> &nbsp; <a href="{GP}/index.html" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">📚 返回知识库门户 →</a></p>
  <div class="hero">
    <h1>🏆 颁奖典礼 · 十七轮增量卡片（2026-08-18）</h1>
    <p>本轮新增 6 张（通过六维评估，剔除平级/朋友向①，仅 ②上下级 / ③高管间）；关系档：③高管间 4 张 + ②上下级 2 张。</p>
    <div class="relbar">
      <span>② 领导↔员工（上下级，supervisor）</span>
      <span>③ 领导↔领导（高管间，exec）</span>
    </div>
  </div>
  <div class="grid">
{inc_grid}
  </div>
<footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>
</div>
</body></html>
'''
with open(RUN_PATH, "w", encoding="utf-8") as f:
    f.write(inc_html)
print("增量页已写:", RUN_PATH, os.path.getsize(RUN_PATH), "字节")

# ---------- 2) 追加汇总页 award.html ----------
html = open(AWARD_HTML, encoding="utf-8").read()
# hero 追加轮次标记
html = html.replace("十六轮 enrich 2026-08-17(+4)", "十六轮 enrich 2026-08-17(+4) ｜ 十七轮 enrich 2026-08-18(+6)", 1)
# sec3 卡片插入到 <div class="sec sec2"> 之前（grid 闭合后）
sec3_html = "\n".join(card_html(c) for c in sec3_cards) + "\n  </div>\n"
html = html.replace("  <div class=\"sec sec2\">", sec3_html + "  <div class=\"sec sec2\">", 1)
# sec2 卡片插入到 <footer> 之前
sec2_html = "\n".join(card_html(c) for c in sec2_cards) + "\n  </div>\n"
html = html.replace("<footer>", sec2_html + "<footer>", 1)
with open(AWARD_HTML, "w", encoding="utf-8") as f:
    f.write(html)
print("汇总页已更新:", AWARD_HTML, os.path.getsize(AWARD_HTML), "字节")

# ---------- 3) index.json ----------
data = json.load(open(IDX, encoding="utf-8"))
before = len(data)
for c in CARDS:
    data.append(dict(
        title=c["title"],
        normKey=c["title"],
        url=c["url"],
        sourceType="secondary",
        relation="exec" if c["rel"]=="r3" else "supervisor",
        summary=c["val"][:120],
    ))
json.dump(data, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("index.json:", before, "->", len(data), "(+%d)" % (len(data)-before))

# ---------- 4) Obsidian 笔记 ----------
note = open(NOTE, encoding="utf-8").read()
note = note.replace("共 97 张", "共 103 张", 1)
round_sec = (
"\n## 轮次 2026-08-18（+6）\n"
"本轮新增（均通过六维评估、仅 ②上下级 / ③高管间）：\n"
)
for c in CARDS:
    tag = "③高管间" if c["rel"]=="r3" else "②上下级"
    round_sec += f"- {c['title']}（{tag}·二手）\n"
note = note.replace("## 卡片总表", round_sec + "\n## 卡片总表", 1)
# 追加剧增行到卡片总表（文件末尾）
new_rows = ""
for c in CARDS:
    rel_txt = "③高管间" if c["rel"]=="r3" else "②上下级"
    new_rows += f"| {c['title']}（award/award.html） | 4 | 二手 | {rel_txt} |  |\n"
links = (
"\n## 线上卡片墙（GitHub Pages）\n"
f"- 累计汇总页：{GP}/award/award.html\n"
f"- 本轮增量页（十七轮·2026-08-18）：{GP}/award/award-20260818.html\n"
)
note = note.rstrip("\n") + "\n" + new_rows + links
open(NOTE, "w", encoding="utf-8").write(note)
print("Obsidian 笔记已更新:", NOTE)

# ---------- 5) 00 索引 ----------
idx00 = open(IDX00, encoding="utf-8").read()
idx00 = idx00.replace("十六轮 enrich 2026-08-17(+4)", "十六轮 enrich 2026-08-17(+4) ｜ 十七轮 enrich 2026-08-18(+6)", 1)
idx00 = idx00.replace("**97 卡**", "**103 卡**", 1)
# 在颁奖典礼 section 的下一个 ## 主题： 之前插入 6 行
marker = "## 主题：颁奖典礼"
si = idx00.index(marker)
ni = idx00.index("## 主题：", si+10)
rows = ""
for c in CARDS:
    rel_txt = "③高管间" if c["rel"]=="r3" else "②上下级"
    rows += f"| {c['title']}（award/award.html） | 4 | 二手 | {rel_txt} |  |\n"
idx00 = idx00[:ni] + rows + idx00[ni:]
open(IDX00, "w", encoding="utf-8").write(idx00)
print("00 索引已更新:", IDX00)
print("DONE")
