# -*- coding: utf-8 -*-
"""Open Day r41 build — 2026-09-09. Append 10 cards (②5: 4一手+1二手 / ③5: 1一手+4二手).
Updates: cumulative wall openday.html + incremental page openday-20260909.html + index.json + lexiang-entry-map.json.
No peer content. No WeCom. Relation only supervisor/exec.
"""
import json, re, os

BASE = r"C:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection"
ODIR = os.path.join(BASE, "openday")
WALL = os.path.join(ODIR, "openday.html")
INC  = os.path.join(ODIR, "openday-20260909.html")
IDX  = os.path.join(BASE, "index.json")
MAPF = os.path.join(BASE, "lexiang-entry-map.json")

# ---------- card renderer (mirrors wall style) ----------
def card(emoji, title, cat, rel, stype, val, how, url, note):
    rel_badge = "r2" if rel == "supervisor" else "r3"
    rel_txt = "上下级" if rel == "supervisor" else "高管间"
    st_badge = "b1" if stype == "primary" else "b2"
    st_txt = "一手" if stype == "primary" else "二手"
    return f'''      <div class="hl">
      <div class="top"><span class="emoji">{emoji}</span><h3>{title}</h3><span class="cat">{cat}</span><span class="badge {rel_badge}">{rel_txt}</span><span class="badge {st_badge}">{st_txt}</span></div>
      <p class="val">{val}</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">{how}</div></details>
      <div class="src">🔗 <a href="{url}" target="_blank">{url}</a></div>
      <div class="note">适用：{note}</div>
    </div>'''

# ===== ② 上下级 5 卡（4一手 + 1二手） =====
cards2 = []
cards2.append(card("🏛️", "茌平区2026年9月份政府开放活动预告（民政/行政审批/便民/文化书院/人社五场）",
  "政府开放日", "supervisor", "primary",
  "聊城市茌平区发布2026年9月政府开放活动预告,整合民政/行政审批/博平镇/人社等多部门五场活动:中华慈善日主题宣传(贾寨镇特教学校捐赠)、行政审批局『政务公开零距离』(参观窗口+讲解流程+倾听诉求)、博平镇便民服务中心『政务服务零距离』开放日(功能分区+高频业务讲解+线上演示+互动答疑+全流程体验)、博平镇文化书院『以小博大 文润博平』开放日(文化阵地参观+非遗展演+社区大学公益课+惠民座谈)、人社局失业保险政策政府开放日(窗口参观+政策宣讲+咨询答疑)。",
  "把『政府开放日』做成月度活动矩阵——用统一预告聚合多部门(民政/审批/镇街/人社)形成规模感;每场固定『现场参观+业务讲解+互动答疑』动作,把政务公开从单向发布变双向沟通;以文化书院/慈善日等柔性场景拉近距离,让群众按兴趣自选场次参与。",
  "http://www.chiping.gov.cn/channel_6948a669fde2425c009181b6/doc_6a8e523e2623f8717a537d9a.html",
  "② 政府开放日（茌平区政府官网一手），政府部门领导以政务服务者姿态,群众/企业/个体工商户/村民代表走进政务与便民现场,提升透明度与参与感。"))

cards2.append(card("🏙️", "泰安市2026年9月份政府开放活动计划（街道便民/科技金融政银企/税务/医保多板块）",
  "政府开放日", "supervisor", "primary",
  "泰安旅游经济开发区发布2026年9月政府开放活动计划,覆盖岱岳区多板块:粥店街道『政务公开零距离·便民服务暖民心』(便民服务中心参观+业务讲解+现场答疑,拉近政民距离)、科技局『科技金融政银企政策对接』(政策宣讲+银企现场对接)、税务局『新办纳税人辅导』(征纳互动体验+集中授课,靠前服务新办纳税人)、医保局『我陪群众走流程』(参观医保大厅+演示参保登记/报销/退休待遇核定+解读基金收支+互动答疑+建议征集)。",
  "把『政府开放日』做成城市级多板块协同——按街道/部门拆分主题(便民/科技金融/税务/医保)各做专场;用『我陪群众走流程』把领导/骨干变陪办员,从『你来讲』变『我陪办』;以银企对接/税务辅导等务实场景把开放日落到企业群众真需求。",
  "https://lykfq.taian.gov.cn/art/2026/9/1/art_45703_10307837.html",
  "② 政府开放日（泰安市政府官网一手），政府部门领导以城市服务者姿态,群众/企业/人大代表/政协委员走进政务与医保现场,提升公信力与办事体验。"))

cards2.append(card("🏛️", "吴忠市审批服务管理局·公共资源交易中心2026年『政府开放日』（零距离体验审批·见证阳光交易）",
  "政府开放日", "supervisor", "primary",
  "吴忠市审批服务管理局、公共资源交易服务中心拟于2026年9月17日开展『政府开放日』,主题『零距离体验审批服务 全方位见证阳光交易』;邀请人大代表/政协委员/服务对象等市民代表走进市政务服务大厅(事项办理流程/企业服务站惠企功能/12345热线运行)与五六楼开评标区(公共资源交易现场),并通过微信公众号发邀请函+电子屏宣传;随后座谈介绍两中心工作、现场征求代表意见建议、答疑解惑。",
  "把『政府开放日』做成『审批+交易』双现场透明课——用政务大厅+开评标区双动线让公众同时看懂『办事』与『交易』两类公权力运行;以12345热线/企业服务站等具象触点降低理解门槛;座谈征集建议并限期反馈,把开放日变阳光政府信任工程。",
  "https://wuzhong.gov.cn/xxgk/zfxxgkml/zfkfr/hdgg/202609/t20260901_5328731.html",
  "② 政府开放日（吴忠市政府官网一手），审批与交易部门领导以阳光运行守护者姿态,市民/代表/服务对象零距离见证政务公开与公平交易。"))

cards2.append(card("🏭", "荣县科技和经济信息化局2026年『政务开放日』（政企同心·向新而行·走进智造企业）",
  "政企开放日", "supervisor", "primary",
  "自贡市荣县科技和经济信息化局将于2026年9月11日举办『政务开放日』,主题『政企同心·向新而行』,邀企业代表及关心工业经济的社会各界人士走进四川省荣县双龙陶业有限公司;采取『实地观摩+政策宣讲+圆桌恳谈』模式:看智造(参观企业,感受科技创新与数实融合对传统产业的变革)、听政策(聚焦新质生产力/大规模设备更新/高新技术企业认定等热点解读)、议发展(围绕『政企同心·向新而行』研讨,为下一步行动提供思路)。",
  "把『部门开放日』做成政企连心桥——用『走进企业+政策宣讲+圆桌恳谈』三段式让企业看懂产业政策红利;以新质生产力/设备更新/高企认定等真问题切入,把开放日变政企协同的务实场;小范围恳谈保证对话深度,是县级工科部门政务公开可复制模板。",
  "https://www.zg.gov.cn/zgsrmzf/zwkfr/pc/content/content_2094235075556098048.html",
  "② 政企开放日（荣县政府官网一手），工科部门领导以产业服务者姿态,企业代表/社会各界实地看智造、面对面议发展,深化政企互信。"))

cards2.append(card("🚗", "联通智网科技2026年国企开放日『一核五维』体系（5G智能网联示范基地+跨界沙龙+科技兴农）",
  "国企开放日", "supervisor", "secondary",
  "联通智网科技紧扣集团『联通未来 创启新程』核心主题,创新构建『一核五维』国企开放日活动体系:以高质量党建为核心,党建铸魂/开放合作/跨界创新/产教融合/科技兴农五维落地;7-8月中国联通5G智能网联示范基地、智网科技总部数字展厅面向行业各界常态化开放,5G无人小巴/远程驾驶/智慧泊车/数字孪生悉数亮相,中科院/航天/交通/高校/车企/运营商等多单位专家沉浸式体验;8月28日举办『工程师跨界沙龙暨国企开放日——交通大模型与智能体专场』,发布『知途』交通大模型;联动北邮/北交/国科大等高校产教融合,并赴黑龙江饶河/河北沽源帮扶县把科创课堂送到田间地头。",
  "把『国企开放日』做成产业会客厅——用『一核五维』把党建红与科技蓝拧成体系;以5G智能网联示范基地做可体验实景场(无人小巴/远程驾驶/数字孪生),让创新成果可观可感可及;用跨界沙龙+产教融合+科技兴农三路延伸,把开放日从展厅延伸到课堂与田野,链接产业生态。",
  "https://new.qq.com/rain/a/20260902A0718L00",
  "② 国企开放日（腾讯新闻二手,中国联通官网同源线索），央企子公司领导以科技开放者姿态,政府/合作伙伴/科研院所/高校/帮扶地区代表走进车联网一线,展示央企创新形象。"))

# ===== ③ 高管间 5 卡（1一手 + 4二手） =====
cards3 = []
cards3.append(card("🏆", "《财富》领军者论坛 Fortune Leaders Forum 澳门开幕（百位商界领袖·复杂时代的领导力）",
  "国际领袖论坛", "exec", "secondary",
  "由《财富》杂志与澳娱综合共同主办的首届《财富》领军者论坛(Fortune Leaders Forum)于2026年9月8日在澳门上葡京开幕,百位顶尖商界领袖齐聚粤港澳大湾区,围绕『融合与复杂时代下的领导力』展开对话;澳娱综合常务董事何超凤致辞强调『清晰的目标是决定成败的关键』,澳门招商投资促进局主席谢永强在以『大湾区十年:机遇、创新与全球影响』为主题的圆桌发言,指出澳门独立关税区/自由港/独立法律体系使其在创新与人才流动上具备优势;论坛聚焦AI基础设施、能源转型与安全、数字金融、旅游变局、健康未来等热门领域。",
  "把『开放日/论坛』升级为领袖同侪对话场——以《财富》百年品牌+澳门自由港规格抬高对话层级;用『领导力×复杂性』战略命题(非产品发布)锚定议题;设大湾区圆桌让政商领袖围绕区域机遇共创;以闭门/高端形式保证坦诚度,让开放日成为校准战略的方向场。",
  "https://so.html5.qq.com/page/real/search_news?docid=70000021_4226aa0122c67352",
  "③ 国际商界领袖论坛（腾讯新闻二手），主办方以全球领导力连接者姿态,百位企业领袖围绕复杂时代的战略方向对话,商务化、以共同命题切入、层级清晰。"))

cards3.append(card("🌏", "2026鼓浪屿论坛·世界商业领袖共话全球投资（企业出海非商业类风险防控）",
  "跨国投资圆桌", "exec", "secondary",
  "作为第二十六届中国国际投资贸易洽谈会重要配套活动,『2026鼓浪屿论坛·世界商业领袖共话全球投资』9月7日在厦门国博会议中心举行,主题『企业出海非商业类风险防控』,汇聚政府/驻华机构/商协会/专业机构及龙头企业600余名嘉宾;主旨演讲环节马尔代夫驻华大使解读跨国合作机遇,安踏集团执行董事兼联席CEO吴永华、海辰储能联合创始人兼总裁王鹏程、达利食品总裁许阳阳分别代表运动/新能源/食品龙头分享全球化与出海风控实战;高端对话环节多位海内外政企/行业龙头/投资机构嘉宾围绕出海合规、跨国投资风险应对、全球供应链布局深度研讨,现场举行多场战略合作签约。",
  "把『开放日』做成跨国投资对话场——以投洽会国家级平台抬高规格;用『出海非商业类风险防控』战略命题锚定(合规/地缘/文化风险);设主旨演讲+高端对话+产业推介+签约全链条,让政府/大使/龙头CEO/投资机构同台(非产品推销);把开放日变安全高效跨境投资的信任枢纽。",
  "https://news.qq.com/rain/a/20260908A055GL00",
  "③ 跨国投资圆桌（腾讯新闻二手,中国商务新闻网同源），主办方以对外开放连接者姿态,驻华大使/龙头CEO/投资机构围绕出海战略对话,商务化、以共同目标切入、无幼稚游戏。"))

cards3.append(card("⚡", "2026年太原能源低碳发展论坛（双碳引领·5场国际会议+外商投资企业圆桌+大使茶座）",
  "国际能源论坛", "exec", "secondary",
  "2026年太原能源低碳发展论坛9月4-5日在太原举办,由外交部、国家能源局与山西省政府共同主办,主题『双碳引领能源转型 创新加速绿色未来』,恰逢论坛十周年与『十五五』开局;坚持『国家级、国际性、专业化』,设开幕式暨高级别会议、5场国际会议(主宾国论坛/国际地热论坛/能源全产业链转型国际论坛/『投资中国 对话山西』外商投资企业圆桌论坛/绿色金融与企业碳管理创新实践论坛)、7场平行论坛及6场主题活动;汇聚120余位国外嘉宾(柬埔寨/格鲁吉亚等部级官员、多国驻华使节、上合组织/世界能源理事会负责人、特斯拉/液化空气/西门子等跨国企业负责人),并设国际圆桌对话会、『大使茶座』走进山西暨『能源低碳』国际对话。",
  "把『开放日/论坛』做成能源外交高端对话平台——以部委+省政府主办抬升国家级规格;用『投资中国 对话山西』外商投资企业圆桌+『大使茶座』把开放日变招商引资与国际合作入口;跨国企业负责人+驻华使节+国际组织同台议能源转型,以专业议题(碳管理/绿色金融)替代寒暄。",
  "https://sx.people.com.cn/BIG5/n2/2026/0901/c189130-41682978.html",
  "③ 国际能源高端论坛（人民网二手），主办方以能源外交引领者姿态,部委/使节/跨国企业负责人围绕绿色转型对话,商务化、以国家与产业共同目标切入。"))

cards3.append(card("🌐", "WBCSD Two Lakes Dialogue 2026·武汉（CEO/C-suite 气候与碳市场高管对话）",
  "可持续高管对话", "exec", "primary",
  "世界可持续发展工商理事会(WBCSD)主办的 Two Lakes Dialogue 2026 于9月16-17日在武汉万达瑞华酒店举行,是汇聚企业领袖、政策制定者、投资者与创新者的高层国际平台,与2026中国碳市场大会同期;参会资格主要面向CEO、董事会主席及其他C-suite高管;通过全体大会、执行层圆桌、社交晚宴与私下会谈,围绕气候、碳市场、产业转型与可持续增长推进务实协作;议题覆盖碳市场与气候标准对齐、Scope 3与绿色供应链、可再生能源与清洁燃料、低碳交通物流、绿色投资与ESG风险;设中国碳排放权注册登记结算机构、国网武汉电-碳-金融服务中心、宜昌产业实地参访。",
  "把『开放日/对话』做成C-suite可持续战略场——以WBCSD国际组织+中国碳市场大会规格锁定高管层级;用执行层圆桌+私下会谈(非公开宣讲)保证对话深度;议题直击碳市场/绿色供应链/ESG出海等真实经营命题;实地参访把战略对话落到中国绿色增长场景。",
  "https://www.wbcsd.org/events/wbcsd-two-lakes-dialogue-2026-edition/",
  "③ 可持续高管对话（WBCSD官网一手），国际组织以全球可持续连接者姿态,CEO/董事会主席围绕气候与碳市场战略对话,商务化、以长期价值共同目标切入、层级清晰。"))

cards3.append(card("🤖", "新加坡亚洲云与AI基础设施展·AI高管午餐会（从AI试点到企业影响力·闭门圆桌）",
  "AI高管闭门会", "exec", "secondary",
  "2026年9月29日中午,新加坡滨海湾金沙将举办『Wonderful AI高管午餐会』,主题『缩小差距:从AI试点到企业影响力』,汇聚新加坡高级技术与商业领袖,围绕AI从实验走向生产、成为企业核心能力这一关键命题展开闭门讨论;背景是新加坡企业AI实验行动迅速,但试点与规模生产间的差距持续拉大,各部门孤立工具难创企业级价值;午餐会为受邀嘉宾提供坦诚的同行交流平台,从技术(已在哪些环节创造可衡量价值/哪些集成缺口导致成果隔离)、部署(试点迈向大规模生产的变化/上线后所有权与责任)、伙伴关系(哪些内外部合作最具价值)三维度探讨;由Wonderful新加坡总经理亚历山大·克莱因伯格(前Twitter/Meta/Google亚太高管)主持。",
  "把『开放日/午餐会』做成高管闭门同侪场——以『从试点到规模化』这一真实痛点锚定(非技术炫技);用私密午餐会+闭门圆桌保证坦诚度;按技术/部署/伙伴关系三维结构化讨论,让CXO围绕『如何把AI变企业能力』共创;定向受邀(非公开)维持高管层级纯度。",
  "https://www.showguide.cn/n/20105262169.html",
  "③ AI高管闭门午餐会（盈拓展览导航二手），主办方以AI落地连接者姿态,新加坡技术与商业领袖围绕企业AI规模化对话,商务化、以经营命题切入、层级清晰。"))

# ===== 1. wall insert =====
html = open(WALL, encoding='utf-8').read()

def find_grid_close(h, open_pos):
    i = open_pos + len('<div class="grid">')
    d = 1
    while i < len(h):
        if h[i:i+4] == '<div': d += 1; i += 4
        elif h[i:i+6] == '</div>': d -= 1; i += 6
        else: i += 1
        if d == 0:
            return i
    return -1

sec2 = html.find('<div class="sec sec2">')
g2 = html.find('<div class="grid">', sec2)
c2 = find_grid_close(html, g2)
assert c2 > 0, "sec2 grid close not found"
html = html[:c2] + '\n'.join(cards2) + '\n' + html[c2:]

g3 = html.rfind('<div class="grid">')
c3 = find_grid_close(html, g3)
assert c3 > 0, "sec3 grid close not found"
html = html[:c3] + '\n'.join(cards3) + '\n' + html[c3:]

# recompute exact grid card counts
n2 = html[g2:c2].count('<div class="hl">') + len(cards2)
n3 = html[g3:c3].count('<div class="hl">') + len(cards3)
html = html.replace('<span class="tag">277 卡</span>', f'<span class="tag">{n2} 卡</span>', 1)
html = html.replace('<span class="tag">65 卡</span>', f'<span class="tag">{n3} 卡</span>', 1)

# hero round append
HERO_TAIL = "四十轮补采 2026-09-08(+8：平罗县/聊城市/青岛科普畅游月/重庆西部科学城/天津生物智造·政务与科普开放日5②全一手 ｜ 37国AI能力建设圆桌/WGL全球本土化大会/可持续发展商业大会·3③0一手+3二手)</p>"
NEW_HERO = "四十轮补采 2026-09-08(+8：平罗县/聊城市/青岛科普畅游月/重庆西部科学城/天津生物智造·政务与科普开放日5②全一手 ｜ 37国AI能力建设圆桌/WGL全球本土化大会/可持续发展商业大会·3③0一手+3二手)｜ 四十一轮补采 2026-09-09(+10：茌平区/泰安市/吴忠市/荣县·政务与政企开放日4②全一手 ｜ 联通智网科技\"一核五维\"国企开放日·1②二手 + 《财富》领军者论坛澳门/2026鼓浪屿论坛·世界商业领袖/太原能源低碳发展论坛/WBCSD Two Lakes Dialogue 武汉/新加坡AI高管午餐会·5③1一手+4二手)</p>"
assert HERO_TAIL in html, "hero tail anchor not found"
html = html.replace(HERO_TAIL, NEW_HERO, 1)

open(WALL, 'w', encoding='utf-8').write(html)
print("WALL updated ->", WALL, "| size", len(html))
print("wall card count now:", html.count('<div class="hl">'), "| sec2 tag", n2, "| sec3 tag", n3)

# ===== 2. incremental page (standalone, self-contained) =====
style_block = open(WALL, encoding='utf-8').read()
style_block = style_block[style_block.find('<style>'):style_block.find('</style>')+len('</style>')]
inc_html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Open Day 开放日 · 第四十一轮增量页（2026-09-09）</title>
{style_block}
</head>
<body>
<div class="wrap">
  <div class="hero">
    <h1>🚪 Open Day 开放日 · 第四十一轮增量页</h1>
    <p>采集于 2026-09-09 ｜ 轮次 R41 ｜ 新增 10 张（②上下级 5 / ③高管间 5）｜ 仅含上下级与高管间，已剔除平级/朋友向。</p>
    <div class="relbar">
      <span>② 领导↔员工（上下级，supervisor）</span>
      <span>③ 领导↔领导（高管间，exec）</span>
    </div>
  </div>
  <div class="sec sec2"><h2>② 领导↔员工（上下级 · supervisor）</h2><span class="tag">{n2} 卡</span><span class="desc">本轮回增 5 张</span></div>
  <div class="grid">
{chr(10).join(cards2)}
  </div>
  <div class="sec sec3"><h2>③ 领导↔领导（高管间 · exec）</h2><span class="tag">{n3} 卡</span><span class="desc">本轮回增 5 张</span></div>
  <div class="grid">
{chr(10).join(cards3)}
  </div>
</div>
<footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>
</body>
</html>'''
open(INC, 'w', encoding='utf-8').write(inc_html)
print("INC page ->", INC, "| size", len(inc_html))

# ===== 3. index.json append =====
idx = json.load(open(IDX, encoding='utf-8'))
items = idx if isinstance(idx, list) else idx.get('items', [])
prev_total = len(items)
prev_od = len([x for x in items if x.get('topic') == 'openday'])

def summ(title, bullets):
    return f"**文章摘要**  \n本文为 Open Day（开放日）知识采集卡片，主题：{title}。\n\n**文章重点总结**  \n" + "\n".join(bullets) + "\n"

new_entries = [
  {"emoji":"🏛️","title":"茌平区2026年9月份政府开放活动预告（民政/行政审批/便民/文化书院/人社五场）","rel":"supervisor","st":"primary",
   "url":"http://www.chiping.gov.cn/channel_6948a669fde2425c009181b6/doc_6a8e523e2623f8717a537d9a.html",
   "summary":["聊城市茌平区发布2026年9月政府开放活动预告,整合民政/行政审批/博平镇/人社五场活动。","行政审批局『政务公开零距离』参观窗口+讲解流程+倾听诉求;博平镇便民服务中心开放日全流程体验。","文化书院『以小博大 文润博平』开放日含非遗展演+社区大学公益课+惠民座谈。","人社局失业保险政策开放日做窗口参观+政策宣讲+咨询答疑,把政务公开变双向沟通。"]},
  {"emoji":"🏙️","title":"泰安市2026年9月份政府开放活动计划（街道便民/科技金融政银企/税务/医保多板块）","rel":"supervisor","st":"primary",
   "url":"https://lykfq.taian.gov.cn/art/2026/9/1/art_45703_10307837.html",
   "summary":["泰安旅游经济开发区发布2026年9月政府开放活动计划,覆盖岱岳区多板块。","粥店街道『政务公开零距离·便民服务暖民心』便民服务中心参观+业务讲解+现场答疑。","科技局『科技金融政银企政策对接』政策宣讲+银企现场对接;税务局『新办纳税人辅导』征纳互动体验。","医保局『我陪群众走流程』领导/骨干变陪办员,从『你来讲』变『我陪办』。"]},
  {"emoji":"🏛️","title":"吴忠市审批服务管理局·公共资源交易中心2026年『政府开放日』（零距离体验审批·见证阳光交易）","rel":"supervisor","st":"primary",
   "url":"https://wuzhong.gov.cn/xxgk/zfxxgkml/zfkfr/hdgg/202609/t20260901_5328731.html",
   "summary":["吴忠市审批服务管理局、公共资源交易服务中心9月17日开展『政府开放日』,主题『零距离体验审批服务 全方位见证阳光交易』。","邀请代表走进政务大厅(事项办理/企业服务站/12345热线)与五六楼开评标区(公共资源交易现场)。","通过公众号发邀请函+电子屏宣传,座谈介绍两中心工作、征求代表意见建议、答疑解惑。","用政务大厅+开评标区双动线让公众同时看懂『办事』与『交易』两类公权力运行。"]},
  {"emoji":"🏭","title":"荣县科技和经济信息化局2026年『政务开放日』（政企同心·向新而行·走进智造企业）","rel":"supervisor","st":"primary",
   "url":"https://www.zg.gov.cn/zgsrmzf/zwkfr/pc/content/content_2094235075556098048.html",
   "summary":["自贡市荣县科技和经济信息化局9月11日举办『政务开放日』,主题『政企同心·向新而行』。","邀企业代表及社会各界走进四川省荣县双龙陶业有限公司,采取『实地观摩+政策宣讲+圆桌恳谈』模式。","看智造(科技创新与数实融合变革)、听政策(新质生产力/设备更新/高企认定解读)、议发展(研讨下一步行动)。","以新质生产力/设备更新/高企认定等真问题切入,是县级工科部门政务公开可复制模板。"]},
  {"emoji":"🚗","title":"联通智网科技2026年国企开放日『一核五维』体系（5G智能网联示范基地+跨界沙龙+科技兴农）","rel":"supervisor","st":"secondary",
   "url":"https://new.qq.com/rain/a/20260902A0718L00",
   "summary":["联通智网科技构建『一核五维』国企开放日体系:高质量党建为核心,五维落地。","7-8月5G智能网联示范基地、总部数字展厅常态化开放,5G无人小巴/远程驾驶/数字孪生悉数亮相。","8月28日举办『工程师跨界沙龙暨国企开放日——交通大模型与智能体专场』,发布『知途』交通大模型。","联动北邮/北交/国科大产教融合,并赴黑龙江饶河/河北沽源帮扶县把科创课堂送到田间地头。"]},
  {"emoji":"🏆","title":"《财富》领军者论坛 Fortune Leaders Forum 澳门开幕（百位商界领袖·复杂时代的领导力）","rel":"exec","st":"secondary",
   "url":"https://so.html5.qq.com/page/real/search_news?docid=70000021_4226aa0122c67352",
   "summary":["《财富》杂志与澳娱综合共同主办的首届《财富》领军者论坛9月8日澳门上葡京开幕。","百位顶尖商界领袖围绕『融合与复杂时代下的领导力』对话;澳娱常务董事何超凤强调清晰目标决定成败。","澳门招商投资促进局主席谢永强在大湾区圆桌发言,谈澳门自由港/独立法律体系优势。","论坛聚焦AI基础设施/能源转型与安全/数字金融/旅游变局/健康未来,以领导力战略命题锚定。"]},
  {"emoji":"🌏","title":"2026鼓浪屿论坛·世界商业领袖共话全球投资（企业出海非商业类风险防控）","rel":"exec","st":"secondary",
   "url":"https://news.qq.com/rain/a/20260908A055GL00",
   "summary":["『2026鼓浪屿论坛·世界商业领袖共话全球投资』9月7日厦门举行,主题『企业出海非商业类风险防控』。","汇聚政府/驻华机构/商协会/龙头600余名嘉宾;安踏/海辰储能/达利食品CEO分享全球化与出海风控实战。","高端对话环节围绕出海合规、跨国投资风险应对、全球供应链布局深度研讨。","现场多场战略合作签约,把开放日变安全高效跨境投资的信任枢纽。"]},
  {"emoji":"⚡","title":"2026年太原能源低碳发展论坛（双碳引领·5场国际会议+外商投资企业圆桌+大使茶座）","rel":"exec","st":"secondary",
   "url":"https://sx.people.com.cn/BIG5/n2/2026/0901/c189130-41682978.html",
   "summary":["2026太原能源低碳发展论坛9月4-5日太原举办,外交部/国家能源局/山西省政府共同主办。","主题『双碳引领能源转型 创新加速绿色未来』,设5场国际会议+7场平行论坛+6场主题活动。","『投资中国 对话山西』外商投资企业圆桌论坛+『大使茶座』走进山西暨能源低碳国际对话。","汇聚120余位国外嘉宾(部级官员/驻华使节/特斯拉/西门子跨国企业负责人)议能源转型。"]},
  {"emoji":"🌐","title":"WBCSD Two Lakes Dialogue 2026·武汉（CEO/C-suite 气候与碳市场高管对话）","rel":"exec","st":"primary",
   "url":"https://www.wbcsd.org/events/wbcsd-two-lakes-dialogue-2026-edition/",
   "summary":["WBCSD主办 Two Lakes Dialogue 2026 于9月16-17日武汉举行,与2026中国碳市场大会同期。","参会资格主要面向CEO、董事会主席及其他C-suite高管,高层国际平台。","通过全体大会、执行层圆桌、社交晚宴与私下会谈推进气候/碳市场/产业转型务实协作。","议题覆盖碳市场对齐/Scope 3绿色供应链/清洁燃料/低碳物流/绿色投资与ESG风险。"]},
  {"emoji":"🤖","title":"新加坡亚洲云与AI基础设施展·AI高管午餐会（从AI试点到企业影响力·闭门圆桌）","rel":"exec","st":"secondary",
   "url":"https://www.showguide.cn/n/20105262169.html",
   "summary":["2026年9月29日新加坡滨海湾金沙举办『Wonderful AI高管午餐会』,主题『从AI试点到企业影响力』。","汇聚新加坡高级技术与商业领袖,围绕AI从实验走向生产、成为企业核心能力闭门讨论。","按技术/部署/伙伴关系三维结构化探讨,由前Twitter/Meta/Google亚太高管主持。","私密午餐会+闭门圆桌保证坦诚度,定向受邀维持高管层级纯度。"]},
]

for e in new_entries:
    items.append({
        "title": e["title"],
        "normKey": e["title"].replace(" ", ""),
        "url": e["url"],
        "relation": e["rel"],
        "source": "web-search",
        "sourceType": e["st"],
        "summary": summ(e["title"], e["summary"]),
        "topic": "openday",
        "date": "2026-09-09",
        "round": 41,
    })

json.dump(idx, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f"INDEX updated: total {prev_total} -> {len(items)} (+{len(items)-prev_total}) | openday {prev_od} -> {len([x for x in items if x.get('topic')=='openday'])}")

# ===== 4. lexiang-entry-map.json (pending round, entry_id=null, token 401 expected) =====
mp = json.load(open(MAPF, encoding='utf-8'))
od = mp["openday"]
od.setdefault("rounds", []).append({
    "date": "2026-09-09",
    "entry_id": None,
    "name": "openday-20260909.html",
    "note": "轮次页 R41 (+10：4②1一手+6③1一手+4二手，待上传，token 401 过期，待重连乐享 MCP 后补传并回填 entry_id)"
})
json.dump(mp, open(MAPF, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print("MAP updated: openday rounds now", len(od["rounds"]))
print("DONE r41 build")
