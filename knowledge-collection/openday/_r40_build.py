# -*- coding: utf-8 -*-
"""Open Day r40 build — 2026-09-08. Append 8 cards (②5全一手 / ③3二手), update wall+index."""
import json, re, os

BASE = r"C:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection"
WALL = os.path.join(BASE, "openday", "openday.html")
TMP  = os.path.join(BASE, "openday", ".run_newcards.tmp.html")
IDX  = os.path.join(BASE, "index.json")

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

# ===== ② 上下级 5 卡（全一手） =====
cards2 = []
cards2.append(card("🏛️", "平罗县2026年『政府开放日』系列活动（四主题分场次走进政务现场）",
  "政府开放日", "supervisor", "primary",
  "平罗县2026年『政府开放日』系列活动以『阳光政务惠民生,政群同心谋发展』为主题,分场次走进政务工作现场——农改中心现场观摩+座谈+问卷调查+政策宣讲(二轮土地延包/农村产权抵押贷款)、发改局智慧农业项目实地观摩、水务局第五排水沟生态修复现场讲解+座谈、医保局经办大厅沉浸式体验(参保登记/异地就医备案自助机实操)。活动以『观摩—座谈—问卷—宣讲』四段闭环,把政务公开从单向发布升级为共建共治共享的治理现场。",
  "把『政府开放日』做成四段闭环体验——用分主题分场次(农业/发改/水利/医保)覆盖多民生领域;每段固定『现场观摩→座谈交流→问卷征集→政策宣讲』动作,让群众从看客变参与者;以『零距离看投资/走看水利知水情/沉浸式体验医保』等具象主题降低参与门槛;用问卷调查把开放日变政策迭代入口。",
  "https://www.pingluo.gov.cn/xxgk/zfxxgkml/zfkfr/hdfa/202609/t20260901_5328747.html",
  "② 政府开放日（平罗县政府官网一手），政府部门领导以政务服务者姿态,群众/种养殖大户/经营主体代表走进政务现场,零距离建言献策、共建共治。"))

cards2.append(card("🏙️", "聊城市2026年9月政府开放活动预告（多部门整合·含『工地业主开放日』）",
  "政府开放日", "supervisor", "primary",
  "聊城市发布2026年9月政府开放活动预告,整合公安(反诈禁毒宣讲)、住建(历史文化名城条例普法/工地业主开放日『品质零距离,安心鉴匠心』)、水利(走近水利工程)、行政审批(政务服务体验日)等多部门活动;其中『工地业主开放日』组织业主实地参观在建工程,工程师带队讲解规划/材料/工艺样板,现场答疑并收集意见逐项整改反馈,实现『透明建造、安心收房』。",
  "把『政府开放日』升级为城市级月度活动矩阵——用统一预告聚合多部门(公安/住建/水利/审批)形成规模感;以『业主开放日』为代表把开放日延伸到民生痛点场景(建房收房),用『工程师带队讲解+现场答疑+意见整改闭环』把透明度落到具体工程;让群众按兴趣自选场次,降低参与成本。",
  "http://www.liaocheng.gov.cn/channel_6954999f55780b9e3bac7e11/doc_6a8e9ee615ef0e8436537d5f.html",
  "② 政府开放日（聊城市政府官网一手），政府部门领导以城市服务者姿态,市民/业主代表走进政务与工程现场,提升公信力与参与感。"))

cards2.append(card("🔬", "青岛科普场馆畅游月·18家高校院所向公众开放（省内首次聚合）",
  "科普开放日", "supervisor", "primary",
  "青岛市科协携手全市18家高校、科研院所启动『青岛科普场馆畅游月』,是省内首次聚合高校院所优质资源集中面向公众开放的科普行动;覆盖航空航天/海洋科技/人工智能/能源环保/生命科学/医学健康/天文观测/地质古生物等数十学科;平日『深藏不露』的重点实验室与院所展厅向公众敞开,提供免费科普讲解,市民可预约场次近距离感受科学真实面貌。",
  "把『实验室开放日』做成城市级科普嘉年华——用科协牵头聚合18家院所(跨高校/科研)形成资源矩阵;以『免费讲解+分场次预约』降低参与门槛;覆盖多学科(海洋/AI/生命/天文)满足不同好奇心;把『象牙塔里的国之底气』转化为『近在咫尺的城市温度』,让公众从看见到理解。",
  "https://new.qq.com/rain/a/20260903A0BHJ400",
  "② 科普开放日（青岛日报/大众新闻一手报道），科研机构领导以科学传播者姿态,市民/青少年走进实验室与院所展厅,拉近科研与公众距离。"))

cards2.append(card("🧪", "重庆西部科学城科技节·10处真实科研实验室面向中小学生开放",
  "科普开放日", "supervisor", "primary",
  "第六届西部(重庆)科学城科技节以『探城市科创肌理,启全域科普新风』为主题,9月5—19日分场次开放种质创制大科学中心、北京大学重庆大数据研究院、凤麟核中子科学研究院等10处真实科研机构;面向中小学生设『科学体验营(走进科研一线)+科学会客厅(首席科学家讲座)+科学手工坊(动手实验)+科学1分钟短视频』流程,科研人员当面解答『一粒种子如何保存几十年/AI怎样看懂影像/中子如何穿透金属』。",
  "把『实验室开放日』做成青少年科创启蒙动线——用真实科研机构(非普通科技馆)制造稀缺感;固定『体验营→会客厅→手工坊→合影』四步,让孩子从观摩到动手到产出(科学短视频);邀请首席科学家/教授做互动讲座,把高深科研翻译成孩子能懂的问题;全程免费+分场次控规模保质量。",
  "https://www.cqrb.cn/contry/dy72/2026-09-03/2766460_pc.html",
  "② 科普开放日（重庆日报一手），科研机构领导以科学启蒙者姿态,中小学生与亲子家庭走进一线实验室,播撒探索种子。"))

cards2.append(card("🧬", "天津『生物智造·聚力未来』科普开放日（面向小学生免费）",
  "科普开放日", "supervisor", "primary",
  "合成生物国家技术创新中心联合天津多家科普基地推出『生物智造,聚力未来|播种·科普开放日』,面向小学生免费开放;设创新产品展示区(化妆品/食品饲料/生物材料/生物装备多元成果讲解)与科普互动实验区(科研人员在指导下亲手开展趣味实验、观察生物现象);响应全国科普月,以沉浸式观展+动手实践助力青少年成长,为生物领域后备人才积蓄力量。",
  "把『科普开放日』做成沉浸式生物启蒙——用国家技术创新中心牵头联动多科普基地形成权威背书;以『产品展示+动手实验』双区设计,让孩子既看成果又做实验;面向小学生免费开放降低门槛;把生物制造这一国家战略(绿色转型/战略安全)转化为青少年可感知的科学好奇心。",
  "https://ketao.tten.cn/News/DetailShow.aspx?NewsId=93A07BA2-3F2F-40A5-B29D-2891034BF488",
  "② 科普开放日（合成生物国家技术创新中心一手），科研机构领导以科学播种者姿态,小学生走进生物世界,在心中播下创新探索的种子。"))

# ===== ③ 高管间 3 卡（二手） =====
cards3 = []
cards3.append(card("🌐", "37国代表在京共探全球人工智能能力建设研讨班·全球合作圆桌",
  "国际圆桌/治理", "exec", "secondary",
  "由外交部主办、北京大学承办的『人工智能能力建设研讨班』在北京开班,来自全球37个南方国家政府高级别代表与AI核心政策制定者齐聚,开展6天深度交流;设AI安全治理/技术前沿/应用创新/国际合作4大方向、9场讲座、6场参访、1场圆桌;圆桌会议邀请产学研服四方代表,围绕AI全球合作与治理规则深度对话,现场对接各国数字化转型需求;参访沿『基础研究—创新生态—前沿赛道—产业落地』主线走进通用人工智能研究院/中关村展示中心/首钢园科幻集聚区等。",
  "把『开放日』升级为国际能力共建对话场——以国家部委+顶尖高校承办抬高规格;用『讲座+参访+圆桌』三段式(学→看→议)替代单向展示;圆桌聚焦『全球合作与治理规则』战略命题,邀产学研服同台(非产品推销);把参访设计成『基础研究→产业落地』完整链条叙事,让外宾既看成果又对接真实需求。",
  "https://www.toutiao.com/article/7683010553714901510/",
  "③ 国际AI治理圆桌（北京日报/头条二手），主办方以国家AI开放合作引领者姿态,多国政府高官与产学研领袖围绕全球治理规则对话,商务化、以共同目标切入。"))

cards3.append(card("🌍", "WGL 2026第八届全球本土化大会·深圳（平台高管与品牌操盘者同场）",
  "全球化高管峰会", "exec", "secondary",
  "由WaveGlocal主办的WGL 2026第八届全球本土化大会9月10日在深圳举行,主题『全球本土化新纪元:从扎根到参天』;汇聚全球平台(Meta/Google/Criteo/Shopify等)、品牌企业、投资机构与全球化服务商,通过《全球本土化指数报告2026》首发、主题演讲、圆桌对话与展位展示,探讨中国品牌全球化下一阶段;设『全球趋势前瞻/新市场破局/规模化增长』三大论坛,连接趋势判断与经营实践。",
  "把『行业开放日』做成全球化同侪决策场——以权威指数报告首发制造内容锚点;用『平台高管+品牌操盘者』同场交叉对话(趋势vs经营);设三大论坛对应企业出海真实命题(破局/增长/本地化);以圆桌对话替代宣讲,让CXO围绕『在当地留下来、持续长大』的战略问题共创。",
  "https://www.jiemian.com/article/15061369.html",
  "③ 全球化高管峰会（界面新闻二手），主办方以行业连接者姿态,平台与品牌CXO围绕本土化战略对话,商务化、以经营命题切入、层级清晰。"))

cards3.append(card("🌱", "2026可持续发展商业大会·上海（两场战略圆桌+智库产业资本签约）",
  "可持续商业峰会", "exec", "secondary",
  "2026可持续发展商业大会在上海举行,以『新质创新共筑可持续未来』为主题;设两场高水平圆桌——『新质生产力与可持续创新』(智能制造/绿色技术/数字经济维度深度对话)与『新引擎,企业国际竞争力构建』(全球化布局/品牌升级/跨境合作);可持续商业战略思维体系创立者吕建中阐释从股东利益最大化转向经济/社会/环境复合价值的新型战略;大会期间举行智库+产业+资本战略合作签约。",
  "把『商业开放日』做成可持续战略对话场——以『新质生产力+企业国际竞争力』双圆桌锚定战略命题;邀学者/企业家/资本方同台(非产品发布);用『可持续商业战略思维』框架把理念系统融入战略规划全链条;以智库+产业+资本签约把对话转化为合作,让开放日成为新商业文明入口。",
  "https://economy.gmw.cn/2026-08/24/content_38960386.htm",
  "③ 可持续商业峰会（光明网二手），主办方以新商业文明引领者姿态,企业家与学者围绕可持续战略对话,商务化、以复合价值共同目标切入。"))

# ===== 1. wall insert =====
html = open(WALL, encoding='utf-8').read()

def find_grid_close(h, open_pos):
    # open_pos points at '<div class="grid">'
    i = open_pos + len('<div class="grid">')
    d = 1
    while i < len(h):
        if h[i:i+4] == '<div': d += 1; i += 4
        elif h[i:i+6] == '</div>': d -= 1; i += 6
        else: i += 1
        if d == 0:
            return i  # position right after the matching </div>
    return -1

# sec2 grid: next grid after sec2 header
sec2 = html.find('<div class="sec sec2">')
g2 = html.find('<div class="grid">', sec2)
c2 = find_grid_close(html, g2)
assert c2 > 0, "sec2 grid close not found"
html = html[:c2] + '\n'.join(cards2) + '\n' + html[c2:]

# sec3 grid: LAST grid (before </body>)
g3 = html.rfind('<div class="grid">')
c3 = find_grid_close(html, g3)
assert c3 > 0, "sec3 grid close not found"
html = html[:c3] + '\n'.join(cards3) + '\n' + html[c3:]

# update section tag counts
html = html.replace('<span class="tag">272 卡</span>', '<span class="tag">277 卡</span>', 1)
html = html.replace('<span class="tag">62 卡</span>', '<span class="tag">65 卡</span>', 1)

# hero round append
HERO_TAIL = "三十轮补采 2026-08-28(+10，国资委城市级集中开放/保密边界三线法/贵州联通三进三体验乡村振兴/玉溪社会责任日/中铁物资沉浸式精神共育/兴安盟政企闭环/徐福街道营商恳谈/首创多元场馆/动线四步法+讲解词/5G专网+舆情应急SOP·7②3③，2一手+8二手)</p>"
NEW_HERO = "三十轮补采 2026-08-28(+10，国资委城市级集中开放/保密边界三线法/贵州联通三进三体验乡村振兴/玉溪社会责任日/中铁物资沉浸式精神共育/兴安盟政企闭环/徐福街道营商恳谈/首创多元场馆/动线四步法+讲解词/5G专网+舆情应急SOP·7②3③，2一手+8二手)｜ 四十轮补采 2026-09-08(+8：平罗县/聊城市/青岛科普畅游月/重庆西部科学城/天津生物智造·政务与科普开放日5②全一手 ｜ 37国AI能力建设圆桌/WGL全球本土化大会/可持续发展商业大会·3③0一手+3二手)</p>"
assert HERO_TAIL in html, "hero tail anchor not found"
html = html.replace(HERO_TAIL, NEW_HERO, 1)

open(WALL, 'w', encoding='utf-8').write(html)
print("WALL updated ->", WALL, "| size", len(html))

# verify card count
cc = html.count('<div class="hl">')
print("wall card count now:", cc)

# ===== 2. tmp newcards file (all 8) =====
open(TMP, 'w', encoding='utf-8').write('\n'.join(cards2 + cards3))
print("TMP written ->", TMP)

# ===== 3. index.json append =====
idx = json.load(open(IDX, encoding='utf-8'))
items = idx if isinstance(idx, list) else idx.get('items', [])
prev_total = len(items)
prev_op = len([x for x in items if x.get('topic') == 'openday'])

def summ(title, bullets):
    return f"**文章摘要**  \n本文为 Open Day（开放日）知识采集卡片，主题：{title}。\n\n**文章重点总结**  \n" + "\n".join(bullets) + "\n"

new_entries = [
  {"emoji":"🏛️","title":"平罗县2026年『政府开放日』系列活动（四主题分场次走进政务现场）","rel":"supervisor","st":"primary",
   "url":"https://www.pingluo.gov.cn/xxgk/zfxxgkml/zfkfr/hdfa/202609/t20260901_5328747.html",
   "summary":["平罗县2026年『政府开放日』以『阳光政务惠民生,政群同心谋发展』为主题,分场次走进政务现场。","农改中心/发改局/水务局/医保局四主题,各设『现场观摩→座谈交流→问卷征集→政策宣讲』四段闭环。","医保局经办大厅提供参保登记/异地就医备案自助机实操的沉浸式体验。","把政务公开从单向发布升级为共建共治共享的治理现场,用问卷调查变政策迭代入口。"]},
  {"emoji":"🏙️","title":"聊城市2026年9月政府开放活动预告（多部门整合·含『工地业主开放日』）","rel":"supervisor","st":"primary",
   "url":"http://www.liaocheng.gov.cn/channel_6954999f55780b9e3bac7e11/doc_6a8e9ee615ef0e8436537d5f.html",
   "summary":["聊城市整合公安/住建/水利/行政审批多部门发布9月政府开放活动预告,形成城市级月度矩阵。","『工地业主开放日』组织业主实地参观在建工程,工程师带队讲解规划/材料/工艺样板。","现场答疑并收集意见逐项整改反馈,实现『透明建造、安心收房』。","用统一预告聚合多部门形成规模感,把开放日延伸到建房收房等民生痛点场景。"]},
  {"emoji":"🔬","title":"青岛科普场馆畅游月·18家高校院所向公众开放（省内首次聚合）","rel":"supervisor","st":"primary",
   "url":"https://new.qq.com/rain/a/20260903A0BHJ400",
   "summary":["青岛市科协携手18家高校院所启动『青岛科普场馆畅游月』,省内首次聚合科研院所集中开放。","覆盖航空航天/海洋科技/AI/生命科学/医学健康/天文观测等数十学科。","平日『深藏不露』的重点实验室与院所展厅向公众敞开,提供免费科普讲解。","用科协牵头聚合资源矩阵+分场次预约,把『国之底气』转化为『城市温度』。"]},
  {"emoji":"🧪","title":"重庆西部科学城科技节·10处真实科研实验室面向中小学生开放","rel":"supervisor","st":"primary",
   "url":"https://www.cqrb.cn/contry/dy72/2026-09-03/2766460_pc.html",
   "summary":["第六届西部(重庆)科学城科技节9月5—19日分场次开放10处真实科研机构(非普通科技馆)。","面向中小学生设『科学体验营+科学会客厅+科学手工坊+科学1分钟短视频』流程。","邀请首席科学家/教授做互动讲座,把高深科研翻译成孩子能懂的问题。","全程免费+分场次控规模保质量,从观摩到动手到产出,播撒探索种子。"]},
  {"emoji":"🧬","title":"天津『生物智造·聚力未来』科普开放日（面向小学生免费）","rel":"supervisor","st":"primary",
   "url":"https://ketao.tten.cn/News/DetailShow.aspx?NewsId=93A07BA2-3F2F-40A5-B29D-2891034BF488",
   "summary":["合成生物国家技术创新中心联合天津多科普基地推出『生物智造·聚力未来』科普开放日。","面向小学生免费开放,设创新产品展示区+科普互动实验区双区。","科研人员在指导下让孩子亲手开展趣味实验、观察生物现象。","把生物制造国家战略(绿色转型/战略安全)转化为青少年可感知的科学好奇心。"]},
  {"emoji":"🌐","title":"37国代表在京共探全球人工智能能力建设研讨班·全球合作圆桌","rel":"exec","st":"secondary",
   "url":"https://www.toutiao.com/article/7683010553714901510/",
   "summary":["外交部主办、北大承办的『人工智能能力建设研讨班』在北京开班,37个南方国家政府高官与AI政策制定者齐聚。","设AI安全治理/技术前沿/应用创新/国际合作4方向、9场讲座、6场参访、1场圆桌。","圆桌邀产学研服四方代表围绕AI全球合作与治理规则深度对话,现场对接各国需求。","参访沿『基础研究—创新生态—前沿赛道—产业落地』主线,把开放日升级为国际能力共建对话场。"]},
  {"emoji":"🌍","title":"WGL 2026第八届全球本土化大会·深圳（平台高管与品牌操盘者同场）","rel":"exec","st":"secondary",
   "url":"https://www.jiemian.com/article/15061369.html",
   "summary":["WaveGlocal主办WGL 2026第八届全球本土化大会9月10日深圳举行,主题『从扎根到参天』。","汇聚Meta/Google/Criteo/Shopify等全球平台、品牌企业、投资机构与全球化服务商。","《全球本土化指数报告2026》首发+三大论坛(趋势前瞻/新市场破局/规模化增长)+圆桌对话。","以『平台高管+品牌操盘者』同场交叉对话,让CXO围绕本土化战略问题共创。"]},
  {"emoji":"🌱","title":"2026可持续发展商业大会·上海（两场战略圆桌+智库产业资本签约）","rel":"exec","st":"secondary",
   "url":"https://economy.gmw.cn/2026-08/24/content_38960386.htm",
   "summary":["2026可持续发展商业大会在上海举行,主题『新质创新共筑可持续未来』。","设两场圆桌:『新质生产力与可持续创新』与『新引擎,企业国际竞争力构建』。","吕建中阐释从股东利益最大化转向经济/社会/环境复合价值的新型战略。","大会期间举行智库+产业+资本战略合作签约,把对话转化为合作。"]},
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
        "date": "2026-09-08",
        "round": 40,
    })

json.dump(idx, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f"INDEX updated: total {prev_total} -> {len(items)} (+{len(items)-prev_total}) | openday {prev_op} -> {len([x for x in items if x.get('topic')=='openday'])}")
print("DONE r40 build")