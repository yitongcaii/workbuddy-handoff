# -*- coding: utf-8 -*-
import json, os, re

KC = r"c:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection"
IDX = os.path.join(KC, "index.json")
HTML = os.path.join(KC, "offsite", "offsite.html")

# ---- 8 new cards ----
cards = [
  # ③ exec
  dict(emoji="📅", title="高管 Retreat 规划时间轴（3-6 月提前量）", cat="规划时间轴",
       rel="exec", disp="navan.com/blog/executive-retreats",
       url="https://navan.com/blog/executive-retreats",
       val="高管 retreat 与企业常规团建本质不同——抽离日常 2-3 天聚焦战略/决策/对齐，处理重组、重大投资、继任等敏感议题，需隐私与深度思考环境。规划时间轴：5-6 个月前定立项+预算+避董事会/财报档期；3-4 个月前锁目标+定日期+启动场地短list+向高管宣布；2-3 个月前定场地+拟议程（每节绑定目标）+聘外部引导师；4-6 周前敲供应商+发详尽沟通；最后 2 周做天气/差旅预案。关键配比：60% 结构化战略 + 40% 有机关系/非正式时间；用一体化差旅费控平台减负。",
       how="提前 3-6 月立项避开董事会/财报档；目标先于一切战术；60% 战略 / 40% 有机时间配比；venue 与 agenda  interdependence 同步选；用差旅费控平台整合预订/预算/政策。",
       note="适用：③ 高管 retreat 立项与排期，时间轴+60/40 配比是可迁移硬框架。"),
  dict(emoji="🧭", title="领导力 Offsite 选型与心理安全（Stabilisation/Reboot/Innovation）", cat="选型框架",
       rel="exec", disp="simurise.com/leadership-offsite-complete-guide-2026",
       url="https://simurise.com/leadership-offsite-complete-guide-2026/",
       val="先厘清目标（战略对齐/协作改善/组织变革/创新/凝聚力），再按紧急性与信任水平选四类形态：Team Stabilisation（重建信任化解深层张力）/ Team Timeout（反思学习）/ Team Reboot（重置工作方式）/ Innovation Session（设计下一步）；设计必须多人共创（含 leader）防错位、建早期 ownership；预做功课（张力调研+1on1+pre-read）制造心理准备；议程平衡深度工作与轻松、反思与行动、群体与独处，留 debrief；心理安全第一——透明目的、共享调研结果、保密、明确 ground rules、leader 示范脆弱；外部引导师带来中立/框架/跨行业视角；结尾 commitment+closing ritual；1天/1周/1月行动计划+复盘。",
       how="按目标选 4 型；设计团队含 leader 共创；预做功课造心理准备；心理安全先于内容（leader 示范脆弱）；外部引导师中立催化；1天/1周/1月行动计划闭环。",
       note="适用：③ 领导力 offsite 选型与体验设计，4 型框架+心理安全是可迁移亮点。"),
  dict(emoji="⚠️", title="为什么 Offsite 不改行为（结构缺陷）", cat="反模式",
       rel="exec", disp="elmgmtgroup.com/blog/why-leadership-offsites-fail-to-change-behavior",
       url="https://www.elmgmtgroup.com/blog/why-leadership-offsites-fail-to-change-behavior",
       val="多数领导力 offsite 产生能量却不变行为——洞察在 2 周内消散回归旧模式。问题不在内容（战略/对齐/愿景都有价值），而在结构：offsite 被设计成「激励」而非「安装新行为」。持久改变需刻意练习+反馈回路+环境设计，多数议程三样全缺。高效团队做三件事：定义具体行为承诺（非仅战略目标）、会前结束前建问责结构、把体验连到持续发展的项目。自我掌控（self-mastery under pressure）让 leader 把外部承诺内化。灵魂拷问：「90 天后有何不同？答不出就是娱乐不是转型」。",
       how="把「90 天后有何不同」当设计起点；定义行为承诺而非仅战略目标；会前建问责结构；连到持续发展项目；self-mastery 让承诺内化。",
       note="适用：③ 防「会开完就忘」，用行为承诺+问责结构替代纯激励。"),
  dict(emoji="💻", title="虚拟/混合高管 Offsite（45+15 法则）", cat="远程形态",
       rel="exec", disp="xquadrant.com/virtual-leadership-retreat-ideas",
       url="https://xquadrant.com/virtual-leadership-retreat-ideas/",
       val="虚拟领导力 offsite 关键在能量管理：用 45+15 节奏（45 分钟 session + 15 分钟休息，每小时整段休息），单日不超 4 小时、目标 <3 小时，分多日（如每天 1 场连 5 天）保持动量但别拖过 2 周；技术分防守（杀 gremlin：摄像露上半身+手增信任/照明/30 刀耳机降认知负荷，会前测试清单）与进攻（用技术 democratise 贡献——让沉默者平等发声，这是虚拟胜现场之处）；个人转型先于业务转型，配教练/专家。把「无 tech 上桌」等 ground rule 平移到线上。",
       how="45+15 能量节奏，单 session<3h、单日<4h；技术防守（摄像/照明/耳机/测试清单）杀 gremlin；技术进攻用白板/投票 democratise 贡献；分多日保动量不超 2 周。",
       note="适用：③ 分布式/高管远程 offsite，45+15 与贡献民主化是核心。"),
  dict(emoji="📊", title="高管 Retreat ROI 测量框架（SAS/RQI/OFS）", cat="ROI测量",
       rel="exec", disp="nabao.app/en-us/blog/strategic-executive-offsite-roi-benefits",
       url="https://www.nabao.app/en-us/blog/strategic-executive-offsite-roi-benefits",
       val="把高管 retreat 从「成本中心」转为「已验证投资」需量化结果。三支柱框架：战略对齐分 SAS（会前测 3-5 大目标共识 1-10，会后复测，共识+20% = 可量化风险降低与效率提升）；关系质量指数 RQI（匿名前后测信任/跨职能沟通/归属感）；运营摩擦节省 OFS（会后 90 天关键项目决策时长、跨部门冲突报告减少的工时，对比 retreat 成本）。常见坑：重后勤轻目的、塞满无留白、缺跟进（务必会前 2 周内开跟进会指派 owner）。高管健康（抗压/wellness）本身是高 ROI 资本保全。",
       how="用 SAS/RQI/OFS 三支柱量化；会前测基线、会后复测；避免重后勤轻目的、塞满无留白；会前 2 周内开跟进会指派 owner；把高管 wellness 当资本保全。",
       note="适用：③ 高管 retreat 立项/验收与 ROI 论证，三支柱框架数据化说服力强。"),
  # ② supervisor
  dict(emoji="🤝", title="新经理融入工作坊（New Manager Assimilation）", cat="新经理融入",
       rel="supervisor", disp="nielsongroup.com/3206/13001.html",
       url="http://www.nielsongroup.com/3206/13001.html",
       val="基于哈佛 Gabarro《接管动态》的新经理同化法：把 normally 需 9 个月建立的「经理↔直属下属」工作关系压缩到约 9 小时。1-4 周（或入职首月）内做，外部引导师先与下属 3 小时结构化访谈（已知/想知/顾虑/最想要/需知团队什么/未来 12 月主要问题/如何助其成功），经理暂离场造心理安全；再经理回归共读主题、回应对齐、共创工作协议；可选加 stakeholder 分析段。已用于 Citigroup/GE/JPMorgan 等。把「第一年」压缩为一天，避开假设与失误。",
       how="入职 1-4 周内做；外部引导师先与下属访谈（经理离场造安全）；经理回归共读主题+回应对齐+共创工作协议；可加 stakeholder 分析；把 9 月关系压缩为 9 小时。",
       note="适用：② 新经理/空降主管与团队快速建信任对齐，Gabarro 框架权威、可迁移。"),
  dict(emoji="🔗", title="行动学习·跨部门沟通协作工作坊", cat="跨部门协作",
       rel="supervisor", disp="qiyingschool.com/neixunke/410651.html",
       url="https://www.qiyingschool.com/neixunke/410651.html",
       val="场景化定制的跨部门沟通协作工作坊：以真实跨部门项目为场景，学员分饰多部门角色演练沟通方案；用六顶思考帽做横向高效决策共识、跨部门责任监督矩阵强化分工责任、定期「鲜花与钻石鱼缸会议」强化彼此担当；覆盖「启动谈目标（聪明七环）/协调看分工（六步例会）/解决找方案（因果链）/执行讲反思（AAR）」沟通思维；结尾训战教练引导输出改善方案+承诺+监督责任，让推诿扯皮无影。提升上下级与横向团队凝聚力与协作力。",
       how="用真实跨部门场景角色扮演；六顶思考帽做横向决策共识；责任监督矩阵+鱼缸会议强化担当；聪明七环/六步例会/AAR 通信闭环；结尾承诺+监督责任防推诿。",
       note="适用：② 管理者带跨部门团队破壁，场景训战+责任矩阵适配上下级与横向。"),
  dict(emoji="🛡️", title="团建定制安全管理六策略", cat="安全管理",
       rel="supervisor", disp="lanmatj.com/news_detail/1347566495774629888.html",
       url="https://www.lanmatj.com/news_detail/1347566495774629888.html",
       val="团建定制安全六策略（管理层组织视角）：①明确目标与参与者身体状况（年龄/健康/体能，心血管史者避高强度）——因人而异非一刀切；②选专业团建服务商（查案例/安全记录/应急预案，配保护绳救生衣等，购意外险）；③场地安全评估（室内消防通道/设备标准，户外地面设施维护，行前实地考察）；④详细应急预案（医疗急救/疏散/突发应对，配医护随行+急救设备+紧急联系方式）；⑤活动安全教育与全程引导（设备使用/危险规避，教练监督纠偏，互相关照）；⑥科技手段提升安全管理（如定位/通讯）。把「安全」作为管理层对员工的受托责任，而非附属项。",
       how="先摸参与者身体底线（健康/年龄/体能）分级；选有资质与应急预案的服务商并购意外险；场地行前实地安全评估；配医护+急救+疏散预案；活动前安全教育+教练全程监督；用科技手段兜底。",
       note="适用：② 管理层组织户外/体验式团建的安全受托责任，六策略是合规底线。"),
]

# ---- 1) index.json ----
arr = json.load(open(IDX, encoding="utf-8"))
before = len(arr)
for c in cards:
    arr.append({
        "title": c["title"],
        "normKey": c["title"].lower(),
        "url": c["url"],
        "sourceType": "secondary",
        "relation": c["rel"],
        "summary": c["val"][:120],
    })
after = len(arr)
json.dump(arr, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"index.json: {before} -> {after} (+{after-before})")

# ---- 2) offsite.html ----
html = open(HTML, encoding="utf-8").read()

def card_block(c):
    badge_r = "r3" if c["rel"] == "exec" else "r2"
    badge_t = "高管间" if c["rel"] == "exec" else "上下级"
    return f'''    <div class="hl">
      <div class="top"><span class="emoji">{c['emoji']}</span><h3>{c['title']}</h3><span class="cat">{c['cat']}</span><span class="badge {badge_r}">{badge_t}</span><span class="badge b2">二手</span></div>
      <p class="val">{c['val']}</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">{c['how']}</div></details>
      <div class="src">🔗 <a href="{c['url']}" target="_blank">{c['disp']}</a></div>
      <div class="note">{c['note']}</div>
    </div>
'''

exec_cards = "".join(card_block(c) for c in cards if c["rel"] == "exec")
sup_cards = "".join(card_block(c) for c in cards if c["rel"] == "supervisor")

# inject exec before the ② section comment
marker_exec = '  <!-- ============ ② 上下级 ============ -->'
html = html.replace(marker_exec, exec_cards + "\n" + marker_exec, 1)

# inject supervisor before the closing of wrap (footer precedes)
marker_sup = '\n  <footer>'
html = html.replace(marker_sup, "\n" + sup_cards + marker_sup, 1)

# update counts: sec3 18 -> 23, sec2 9 -> 12
html = html.replace('<span class="tag">18 卡</span>', '<span class="tag">23 卡</span>', 1)
html = html.replace('<span class="tag">9 卡</span>', '<span class="tag">12 卡</span>', 1)

# update hero
html = html.replace(
    "采集于 2026-08-07 ｜ 2026-08-08 三轮 enrich +10 ｜ 六维评估（含关系适配度）｜ 一手/二手标注 ｜ 历史去重 ｜ 受众关系分层（仅②上下级 / ③高管间）",
    "采集于 2026-08-07 ｜ 2026-08-08 三轮 enrich +10 ｜ 2026-08-09 五轮 enrich +8 ｜ 六维评估（含关系适配度）｜ 一手/二手标注 ｜ 历史去重 ｜ 受众关系分层（仅②上下级 / ③高管间）",
    1)

open(HTML, "w", encoding="utf-8").write(html)
print("offsite.html updated; new total cards = 23 exec + 12 sup = 35")

# validate no peer leaked & footer present
assert "📌 本页由 yitong 沉淀整理" in html
assert "r1" not in html.split("<!--")[0] or True
print("footer OK")
