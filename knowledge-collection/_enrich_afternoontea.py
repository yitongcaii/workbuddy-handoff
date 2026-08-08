# -*- coding: utf-8 -*-
import json, re, os

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "afternoontea", "afternoontea.html")
IDX = os.path.join(BASE, "index.json")

# ---------- 11 new cards (only ② supervisor / ③ exec, 0 peer) ----------
# fields: emoji, title, cat, rel('r3'|'r2'), rel_label, val, how, url, note
new_exec = [
    dict(emoji="🤝", title='奉贤「订单下午茶」·政府搭台企业跨界对接', cat="政企对接",
         val='奉贤区「四大产业专班」打造的「订单下午茶」：以茶叙形式开展，每期邀约 10 家左右重点企业，打破正式会议束缚，用茶歇/圆桌/田野咖啡等轻松场景构建坦诚的商业互动环境；政府退居幕后专注搭台，让企业做主角。自 2025-07 试点已办 10 场，直接促成订单超 2200 万元，从「相邻不相识」到「茶叙见商机」。',
         how='政府/产业专班做「连接器」而非主角；每期精匹配高相关企业(提前做功课)；茶叙+圆桌+自由对接三段式；以真实订单/合作意向为产出闭环。',
         url='https://fxdzb.fengxian.gov.cn/html/2026-02/06/content_60221_19285486.htm',
         note='适用：③ 政企/产业链高管以茶会商，政府搭台、企业唱戏的 B2B 对接范式（官方数字报一手源）。'),
    dict(emoji="🌐", title='新华三「生态大咖下午茶」·厂商×伙伴副总裁对话', cat="生态对话",
         val='B.P 商业伙伴总裁主持，新华三集团副总裁(生态合作营销部)与上海华东电脑副总裁就「无界生态」战略深度对谈：从合作基础(文化相近/创新互补)、疫情方舟护航帮扶、到新基建下如何共创更大未来；三方(厂商+伙伴+行业 KOL)以茶叙形式坦诚交流，呈现真实生态合作博弈与共赢逻辑。',
         how='设中立行业 KOL 主持控场；厂商与核心伙伴副总裁同台(对等)；围绕真实战略议题(而非宣传稿)深挖；把合作痛点与赋能计划摊开谈。',
         url='https://tech.163.com/20/1103/15/FQH3RPS100099A7M.html',
         note='适用：③ 厂商高管↔伙伴高管↔行业 KOL 生态对话，真实对话稿价值高。'),
    dict(emoji="🏭", title='珠海「产业论·总裁下午茶」·园区企业家圆桌供需对接', cat="总裁圆桌",
         val='香洲区云溪谷数字产业园「产业论·总裁下午茶」圆桌交流沙龙暨产服平台集群集中式供需对接：企业家们围坐轻松环境，深入交流发现产品/技术/资源互补与「1+1>2」合作机会，并互抛橄榄枝邀请合作；为忙碌中无暇认识「数字邻居」的企业家提供互信与合作基础搭建平台。',
         how='聚焦单一产业园区(地理邻近天然高相关)；圆桌沙龙而非台上讲台下；当场抛出合作意向并建跟进；产服平台集群集中式供需对接收尾。',
         url='http://zhuhaidaily.hizh.cn/html/2023-09/01/content_1213_8232498.htm',
         note='适用：③ 同园区企业家闭门对接，地理邻近+轻场景促成合作。'),
    dict(emoji="🏙️", title='徐家汇「商圈高管」下午茶·营商服务中心主题专场', cat="营商专场",
         val='徐汇区营商服务中心·徐家汇分中心「商圈高管」下午茶系列活动——以体育主题交流会切入：区体育局/街道/经济发展公司领导与商圈企业代表共聚，介绍体育公园/高端场地资源，对接企业及员工体育需求；现场揭牌「徐家汇杯」企业体育交流赛，建立重点企业人力资源朋友圈，拓宽「营商朋友圈」。',
         how='营商服务中心做信任背书与资源导入；用轻量主题(体育/文化)破冰而非硬招商；现场揭牌+建常态朋友圈承接；精准送达营商服务。',
         url='https://m.thepaper.cn/baijiahao_14889881',
         note='适用：③ 政府营商×商圈企业高管，主题专场+轻社交撬动政企关系。'),
]

new_sup = [
    dict(emoji="☕", title='海底捞「喝咖啡」复盘·管理者与下属咖啡 SOP', cat="咖啡复盘",
         val='海底捞「喝咖啡」制度：店长与责任人(及相关上下游/协作方)离开办公室到安静咖啡厅，绝不翻旧账，只谈三件事——归因(客观因素)/方案(具体 Action)/时效(立军令状)；加「+1」必须有会议纪要归档发给所有人。把焦点从「谁的错」转向「怎么改」，是一次深度教练辅导(Coaching)。',
         how='选对人(相关协作方都叫上)；定对场(绝不在办公室)；控流程「3+1」法则(复盘→策略→承诺+归档)；小团队可用「乐捐」替代罚款做痛感回馈团队。',
         url='https://www.toutiao.com/article/7646020975519203850',
         note='适用：② 管理者与责任人咖啡复盘，把追责会变教练辅导，落地性强。'),
    dict(emoji="☕", title='惠普「喝咖啡的时间」·高管每月 6-8 名员工面谈', cat="管理面谈",
         val='惠普「喝咖啡的时间」制度：每个高层每月必须单独找 6-8 名员工喝咖啡聊天，每次不少于 2 小时，及时听取员工对公司各方面的意见建议；高管完成面谈后须写沟通报告，把未解决的重大问题上报公司决策委员会。这是典型的上级↔下级一对一沟通(管理面谈)。',
         how='制度化固定频度(每月每人 6-8 名)；时长充足(≥2h)保证深度；面谈后写报告上报决策委形成闭环；用咖啡场景消解汇报感。',
         url='https://ishare.ifeng.com/c/s/v0022oupyCyYvBNk5VtdRxccVoI5jk9gk0GuKe1WS7RwrZU__',
         note='适用：② 高管一对一倾听员工，制度化+上报闭环是经典范式。'),
    dict(emoji="💡", title='冯国华一对一锦囊·会议归下属、地点在工位', cat="1on1教练",
         val='领教工坊冯国华给企业家的一对一高杠杆锦囊：1on1 前应视为「下属的会议」——由下属准备议程并提前 24h 发上司；地点最好选在下属办公位或就近会议室；之中寒暄→双方协议期待→聆听同理→提问启发→留 2 分钟审视目标；之后发纪要、按约定提供支持资源、定时审核进度。',
         how='翻转 ownership：议程由下属准备；地点下沉到下属工位降压迫感；频度按熟悉度(n-1 每月至少 1 次，新人/挑战者加密)；留白 2 分钟做目标审视与后续计划。',
         url='https://jy.usx.edu.cn/news/view/aid/307656/tag/cydh',
         note='适用：② 企业家/管理者 1on1 框架，把会议主权交给下属提升质量。'),
    dict(emoji="🚨", title='华为预警谈心四步·管理者一对一留人闭环', cat="留人谈心",
         val='华为核心人才保留机制：日常观察(对照六大离职信号建简易记录)→发现异常 24h 内私下一对一约谈(避公开、先听后问)→分类解决(工作/心态/薪资/发展，承诺必兑现)→回访闭环。按人群分层沟通频次：新人高频、老员工月 1 次、核心骨干每半月深度一对一。',
         how='建离职信号日常观察表；异常 24h 内私密约谈保护隐私；先倾听不打断；分类给出方案并给时间节点；承诺必兑现防画饼；按人群定频次。',
         url='https://www.toutiao.com/article/7650403293104980499',
         note='适用：② 管理者一对一预警谈心，把留人做在离职前，闭环强。'),
    dict(emoji="🤝", title='山东章鼓协同启航茶话会·总经理与新部门圆桌', cat="跨部门协同",
         val='山东章鼓为新成立的计划管理部/销售管理部/精益办三部门策划「协同启航」茶话会：总经理、副总经理兼技术总监等多位高管悉数到场，与同事们围桌而坐；六张圆桌围绕「个人成长如何与团队目标同频」「如何为变化设计友好接收界面」等深度话题展开，并在「协作火花墙」呈现真实思考，共识在杯盏间达成。',
         how='高管亲自到场(非派代表)显重视；圆桌深度话题替代汇报；「协作火花墙」可视化共识；定制伴手礼传递长期承诺。',
         url='https://www.jinguxun.com/article/7556843',
         note='适用：② 高管与新部门员工跨部门协同茶话会，真实落地案例。'),
    dict(emoji="🪨", title='耿村煤矿三日七日谈心·新职工全周期关怀', cat="新职工关怀",
         val='耿村煤矿开拓一队建新职工跟踪培养体系：入职第三天班组重点摸排食宿/强度适配/岗位适应，化解生活难题；入职第七天队管理人员开展「一对一」深度谈心，精准梳理思想动态、疏导心理压力、明晰成长路径；依托班前会/班组群公开表彰点滴进步，让付出被看见、成长被激励。',
         how='三日跟进(生活适配)+七日谈心(思想动态)双节点；管理人员一对一非群体；公开表彰新职工进步强化认同；班前会/群组持续正向反馈。',
         url='https://new.qq.com/rain/a/20260714A08G5I00?refer=cp_1009',
         note='适用：② 新职工入职关怀谈心，国企一线可复制的「三日+七日」机制。'),
    dict(emoji="🔋", title='宁德时代主管面谈·班长3次谈心关怀机制', cat="新职工关怀",
         val='宁德时代贵州基地职工关爱计划：建立「老带新办 7 件事、班长 3 次谈心、主管 1 次面谈」关怀机制，从入职引导、岗位培训、生活帮扶、心理疏导多维度为新员工提供全周期关怀，让新员工「入职有人帮、遇事有人管」，快速融入并适应岗位。党建带工建延伸至各班组的「党群一体化」体系支撑。',
         how='分层关怀(班长 3 次+主管 1 次)保证触达密度；老带新 7 件事清单化；从生活到心理全维度；党群一体化体系兜底。',
         url='https://new.qq.com/rain/a/20260507A02OAC00?refer=cp_1009',
         note='适用：② 新员工全周期关怀，班长+主管双线谈心密度高。'),
]

def card_html(c, rel_class, rel_label):
    return (
        '    <div class="hl">\n'
        f'      <div class="top"><span class="emoji">{c["emoji"]}</span><h3>{c["title"]}</h3>'
        f'<span class="cat">{c["cat"]}</span><span class="badge {rel_class}">{rel_label}</span><span class="badge b2">二手</span></div>\n'
        f'      <p class="val">{c["val"]}</p>\n'
        '      <details class="exec"><summary>怎么做</summary>'
        f'<div class="inner">{c["how"]}</div></details>\n'
        f'      <div class="src">🔗 <a href="{c["url"]}" target="_blank">{c["url"]}</a></div>\n'
        f'      <div class="note">适用：{c["note"]}</div>\n'
        '    </div>\n'
    )

exec_html = "".join(card_html(c, "r3", "高管间") for c in new_exec)
sup_html = "".join(card_html(c, "r2", "上下级") for c in new_sup)

# ---------- read html ----------
html = open(HTML, encoding="utf-8").read()

# insert exec cards before ② supervisor section marker
marker_exec = '  <!-- ============ ② 上下级 ============ -->'
assert marker_exec in html, "exec marker not found"
html = html.replace(marker_exec, exec_html + "\n" + marker_exec, 1)

# insert sup cards before footer (inside sec2 grid)
marker_sup = '  </div>\n\n  <footer>'
assert marker_sup in html, "sup/footer marker not found"
html = html.replace(marker_sup, sup_html + "  </div>\n\n  <footer>", 1)

# update counts
html = html.replace('<span class="tag">11 卡</span>', '<span class="tag">15 卡</span>', 1)
html = html.replace('<span class="tag">15 卡</span>', '<span class="tag">22 卡</span>', 1)

# update hero subtitle
old_hero = '三轮 enrich 2026-08-08（+5）｜ 六维评估'
new_hero = '三轮 enrich 2026-08-08（+5）｜ 四轮 enrich 2026-08-08（+11）｜ 六维评估'
assert old_hero in html
html = html.replace(old_hero, new_hero, 1)

open(HTML, "w", encoding="utf-8").write(html)
print("HTML updated. new size:", len(html.encode("utf-8")))

# ---------- index.json append + dedup ----------
idx = json.load(open(IDX, encoding="utf-8"))
existing_urls = {x.get("url") for x in idx}
existing_norm = {x.get("normKey") for x in idx}

def norm(t):
    return re.sub(r'[\s\u3000\W]+', '', t).lower()

added = 0
for c, rel in [(new_exec, "exec"), (new_sup, "supervisor")]:
    for c0 in c:
        url = c0["url"]
        nk = norm(c0["title"])
        if url in existing_urls or nk in existing_norm:
            print("SKIP dup:", c0["title"])
            continue
        idx.append({
            "title": c0["title"],
            "normKey": nk,
            "url": url,
            "sourceType": "secondary",
            "relation": rel,
            "summary": c0["val"][:60],
        })
        existing_urls.add(url); existing_norm.add(nk)
        added += 1

json.dump(idx, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("index.json total:", len(idx), "| added this round:", added)
