# -*- coding: utf-8 -*-
"""修复 award.html：把新增卡移入对应 grid 内（去掉错位 </div>）。"""
import os
KC = r"C:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection"
AWARD_HTML = os.path.join(KC, "award", "award.html")

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
def card_html(c):
    badges = f'<span class="badge {c["rel"]}">{"高管间" if c["rel"]=="r3" else "上下级"}</span><span class="badge b2">二手</span>'
    return f'    <div class="hl">\n      <div class="top"><span class="emoji">{c["emoji"]}</span><h3>{c["title"]}</h3><span class="cat">{c["cat"]}</span>{badges}</div>\n      <p class="val">{c["val"]}</p>\n      <details class="exec"><summary>怎么做</summary><div class="inner">{c["inner"]}</div></details>\n      <div class="src">🔗 <a href="{c["url"]}" target="_blank">{c["url"]}</a></div>\n      <div class="note">适用：{c["note"]}</div>\n    </div>'

sec3_block = "\n".join(card_html(c) for c in CARDS if c["rel"]=="r3")
sec2_block = "\n".join(card_html(c) for c in CARDS if c["rel"]=="r2")

html = open(AWARD_HTML, encoding="utf-8").read()

# sec3 fix: 当前 `</div>\n` + sec3_block + `\n  </div>\n  <div class="sec sec2">`
bad3 = "</div>\n" + sec3_block + '\n  </div>\n  <div class="sec sec2">'
good3 = sec3_block + '\n  </div>\n  <div class="sec sec2">'
assert bad3 in html, "sec3 anchor not found"
html = html.replace(bad3, good3, 1)

# sec2 fix: 当前 `</div>\n` + sec2_block + `\n  </div>\n<footer>`
bad2 = "</div>\n" + sec2_block + "\n  </div>\n<footer>"
good2 = sec2_block + "\n  </div>\n<footer>"
assert bad2 in html, "sec2 anchor not found"
html = html.replace(bad2, good2, 1)

open(AWARD_HTML, "w", encoding="utf-8").write(html)
o=html.count("<div"); c=html.count("</div>")
print("open<div>:",o,"close</div>:",c,"balance:",o-c)
print("hl:",html.count('class="hl"'),"footer yitong:",html.count("📌 本页由 yitong"))
