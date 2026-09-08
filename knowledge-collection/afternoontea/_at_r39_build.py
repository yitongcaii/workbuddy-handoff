# -*- coding: utf-8 -*-
"""下午茶研讨 afternoontea r39 build — 2026-09-08. Append 8 cards (②5 / ③3), update wall+index."""
import json, re, os

BASE = r"C:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection"
WALL = os.path.join(BASE, "afternoontea", "afternoontea.html")
TMP  = os.path.join(BASE, "afternoontea", ".run_newcards.tmp.html")
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

# ===== ② 上下级 5 卡 =====
cards2 = []
cards2.append(card("🍵", "东莞控股首期『共说新语』高管茶话会（圆桌围坐·真对话无负担）",
  "高管茶话会", "supervisor", "secondary",
  "东莞控股8月28日举行首期『共说新语』高管茶话会，公司党委副书记、总裁与来自总部及下属单位的基层员工代表圆桌围坐，主题『新赛道·新机会·新成长』。活动秉持『真对话、无负担』原则，不设主持、不固定发言顺序、发言不记名，近两小时坦诚交流从宏观战略方向到具体业务转型、从体系优化到个体成长，员工畅所欲言。两位高管专注倾听并即时回应，鼓励大家拥抱变化；活动将常态长效推进、覆盖多元岗位，让每位员工声音被听见、被重视。",
  "把『高管茶话会』做成无压力对话场——用『三不』原则(不设主持/不固定顺序/发言不记名)卸下心理包袱；圆桌围坐替代主席台，让基层员工敢直言；主题锚定『新赛道·新成长』等真问题而非空泛团建；高管即时回应而非记录归档，把『听见』变成『被重视』的体验；以常态长效+覆盖多元岗位避免一阵风，推动个人与公司同频共振。",
  "https://www.toutiao.com/article/7680531641370001960",
  "② 高管↔基层员工（今日头条二手），公司高管以平等对话者姿态，基层员工代表围坐畅言战略与成长，打破层级壁垒、凝聚『十五五』共识。"))

cards2.append(card("🌿", "富春环保『对话·环保青鹰』高管与青年员工面对面（破冰+生日会）",
  "高管青年面对面", "supervisor", "secondary",
  "富春环保举办『对话·环保青鹰』座谈，公司党委副书记、总经理等高管与青年员工围坐，打破层级壁垒。活动设破冰预热(每人用两个关键词形容自我特质与公司感受)、成长对话(高管以『过来人』身份、接地气真实故事务实答疑)、暖心寄语(赠励志书籍)、集体生日会四环节，兼具思想碰撞的深度与双向奔赴的温情。高管摒弃模板化官方答复，用真实成长故事逐一回应，同步开展生日会拉近彼此距离。",
  "把『高管面对面』升级为温情成长场——用破冰关键词(两个词形容自我+公司)快速消解陌生感；成长对话环节让高管以『过来人』而非『领导』身份答疑，弃模板化官话；叠加集体生日会等情感锚点，让座谈既有干货又有温度；以『党建+人才』融合定位常态化搭建青年交流平台，让青年在企业沃土安心扎根。",
  "https://m.sohu.com/a/1054423246_122014422",
  "② 高管↔青年员工（搜狐二手），公司高管以成长引路人姿态，青年员工大胆提问建言，打破层级、双向奔赴。"))

cards2.append(card("🌱", "华都检测新人茶话会·前期问卷做定制化职业赋能",
  "新人茶话会", "supervisor", "secondary",
  "华都检测以一场新人茶话会轻启秋日序章，公司管理层与近10位来自985/211高校的新伙伴围坐，主线『精准赋能成长、定制规划未来』。前期向新员工发放职业规划问卷，精细化调研岗位认知、个人优势、职业发展意向、成长困惑与期待；现场领导基于问卷逐一开展定制化职业指导，深度拆解各岗位成长体系、晋升路径与发展机遇，从短期目标到长期格局为新人勾勒清晰蓝图，让迎新不流于形式。",
  "把『新人茶话会』做成定制化赋能——会前先发职业规划问卷摸准每人优势与困惑，避免泛泛而谈；现场领导按问卷做一对一精准指导，拆解岗位成长体系/晋升路径；从『怎么干、往哪走、如何成长』逐层讲透，让新人打消入职迷茫；自由交流环节新老员工答疑拉近距离，落实『以人为本、赋能成长』的人才理念。",
  "https://www.toutiao.com/article/7680418588867527194",
  "② 管理层↔新人（今日头条二手），公司管理层以职业引路人姿态，校招新人在轻松对话中锚定成长坐标、与企业同频。"))

cards2.append(card("🫖", "浙江东方『工会主席下午茶』一对一心贴心民主管理",
  "工会主席下午茶", "supervisor", "secondary",
  "浙江东方金融控股集团工会创新『工会主席下午茶』，每月第二周周五由工会主席泡一壶茶与约好的职工代表相对而坐。没有严肃会议桌、没有层层汇报的拘谨，只有开诚布公的倾诉与倾听，半年多来成为连接企业管理层与职工心声的纽带。一线骨干在轻松氛围中敞开心扉提职业瓶颈与建议，转化为公司启动人才盘点、优化晋升机制的参考；职工『金点子』(如组建量化投资团队)直送班子审议，工会从『发福利、搞活动』转向企业发展的『助推器』。",
  "把『民主管理』做成一对一茶叙——工会主席主动『下访』式邀约，用舒适宽松环境让『沉默的大多数』敢说真话；固定每月第二周周五形成稳定预期；一对一深度聊(约1小时)替代集体座谈，挖出真困惑真建议；把茶水间声音转化为人才盘点/机制优化/班子审议的具体动作，让工会从福利部变助推器，喝出民主管理诚意。",
  "https://finance.sina.com.cn/jjxw/2025-12-25/doc-inhcyrup9067264.shtml",
  "② 工会主席↔职工（新浪财经二手），工会主席以『娘家人』姿态一对一倾听，把职工心声转化为企业治理改进，喝出民主管理诚意。"))

cards2.append(card("☕", "国际实践 Leader–Employee Coffee Chat Playbook（领导—员工咖啡聊法）",
  "leader-employee咖啡聊法", "supervisor", "secondary",
  "国际管理实践总结『领导—员工咖啡聊』体系，把非正式一对一咖啡/茶会话作为核心领导动作。给出可复用动作：Listening Latte(20分钟单主题倾听、领导最后说、公开记录跟进)、Espresso Briefs(关键更新限5分钟逼出清晰)、Barista Rotations(轮值选饮品培养ownership)、Brewed Brainstorms(15分选项+5分投票+10分承诺)、Decaf Debriefs(高强度后低刺激复盘)。强调领导多听少说、不防卫、关掉手机、真诚在场，把咖啡时刻变成连接与绩效的入口。",
  "把『咖啡聊』做成领导行为规范——固定周期(周/双周)约30分钟内一对一，明确『这是员工的时间』；会前看背景、会中多听少说+追问不辩解；用Listening Latte(单主题倾听、领导最后讲、公开跟进)把茶水间变真话入口；用Espresso Briefs逼简短清晰、Brewed Brainstorms用仪式感加速决策；会后对 concerns 真跟进，让『被听见』落地为行动。",
  "https://simpleworkapps.com/blog/coffee-chat-with-employees/",
  "② 领导↔员工（国际管理实践二手），把非正式咖啡/茶会话系统化为领导动作，多听少说、会后真跟进，跨文化可直接套用。"))

# ===== ③ 高管间 3 卡（全二手） =====
cards3 = []
cards3.append(card("🌸", "Lean In Shanghai『乐恰地，自在成长』女性职业发展沙龙",
  "女性高管沙龙", "exec", "secondary",
  "Lean In Shanghai携手拉菲在沪上独栋洋房举办『乐恰地，自在成长』女性职业发展沙龙，35位来自不同领域的女性企业家、管理者、投资人与决策者围坐。三位嘉宾(出海业务线VP/精品酒业总经理/二代接班人)分享职业突围真实故事，南法下午茶+白葡萄酒品鉴中展开圆桌对话，围绕跳出情怀内耗、打造个人不可替代性、他人期许与自我追求的平衡等课题，同频姐妹双向赋能、从容成长。",
  "把『女性高管沙龙』做成同频互助场——用独栋洋房+下午茶/葡萄酒品鉴营造静奢松弛氛围，降低商务社交压力；限35人小圈层保交流质量；嘉宾分享(职业突围真实故事)+圆桌对话(共性成长课题)双结构，让不同赛道女性多维碰撞；以『Lean In』互助文化把单次活动沉淀为长期女性领导力社群。",
  "https://www.fortunetimes.sg/cn?p=57099",
  "③ 女性高管/企业家间（时代财智二手），主办方以女性互助连接者姿态，跨行业女性决策者围绕职业与人生课题同频共创，商务化、以成长共鸣切入。"))

cards3.append(card("🍃", "大数思享『完整人生』企业家闭门茶道漫旅（哲学+茶道·限流25人）",
  "企业家闭门沙龙", "exec", "secondary",
  "大数思享企业家俱乐部打造小众高端闭门私享沙龙『完整人生：一场穿越教育、资本、文化的哲学与茶道漫旅』，限流20—25人。特邀上海财经大学哲学系教授与上海市茶业行业协会副会长坐镇，以哲学思维升维商业认知、以传统茶道沉淀内心心力，为企业家在变局中提供静心修心、认知破局、同频链接的高阶私享场。全程纯分享、无宣讲、无路演、零低效社交。",
  "把『企业家沙龙』做成闭门修心场——严控20—25人小众闭门保障深度与圈层纯粹；用『哲学+茶道』双嘉宾设计，一手升维认知、一手沉淀心力，回应企业家思维固化与焦虑；明确『无宣讲无路演零低效社交』规则，把相聚还原为纯粹链接；以高端场地+审核准入筛选同频掌舵人。",
  "https://bj.huodongxing.com/event/4865785493600",
  "③ 企业家间（活动行二手），俱乐部以圈层连接者姿态，企业掌舵人在哲学与茶道中向内求索、同频链接，商务化、以认知破局与长期主义切入。"))

cards3.append(card("💐", "西青区外企女性精英圆桌会（政企搭台·政策+异业协同）",
  "女性精英圆桌", "exec", "secondary",
  "西青区商务局联合区妇联在精灵smart展厅举办2026首场『外企女性精英圆桌会暨内外贸一体化提振消费交流会』，主题『芳华致远，聚力前行』，邀请神钢铝材、大和电器等9家外企及商贸金融领域女性企业家代表30余人。区商务局现场解读『发票抽奖』『异业联盟』等政策，企业代表分享职场心得与跨界协同，中国银行专家给理财建议；花艺插花、粘土手工与茶歇交流中放松身心、增进友谊。",
  "把『女性精英圆桌』做成政企精准服务场——政府(商务局/妇联)搭台邀外企女性高管/企业家，用政策解读(发票抽奖/异业联盟)送上务实礼包；圆桌分享职场心得+跨界协同引发共鸣；穿插花艺、茶歇等轻互动打破坚冰、增进友谊；以『女企业家联盟』为纽带持续赋能，把单次活动变区域巾帼合力入口。",
  "https://www.toutiao.com/article/7614747814748324402/",
  "③ 女性高管/企业家间（今日头条二手），政府以赋能者姿态搭台，外企女性精英与企业家围绕发展协同对话，商务化、以政策+资源+情谊三明治切入。"))

# ===== 1. wall insert =====
html = open(WALL, encoding='utf-8').read()

def find_grid_after(h, sec_start):
    # first '<div class="grid">' after sec_start, return position of its opening tag
    g = h.find('<div class="grid">', sec_start)
    return g

def grid_close(h, open_pos):
    i = open_pos + len('<div class="grid">')
    d = 1
    while i < len(h):
        if h[i:i+4] == '<div': d += 1; i += 4
        elif h[i:i+6] == '</div>': d -= 1; i += 6
        else: i += 1
        if d == 0:
            return i
    return -1

sec3 = html.find('<div class="sec sec3">')
sec2 = html.find('<div class="sec sec2">')
assert sec3 > 0 and sec2 > 0, "sec markers not found"
# sec3 is exec (first section), sec2 is supervisor (second)
g3 = find_grid_after(html, sec3)
c3 = grid_close(html, g3)
assert c3 > 0, "sec3 grid close not found"
html = html[:c3] + '\n'.join(cards3) + '\n' + html[c3:]

g2 = find_grid_after(html, sec2)
c2 = grid_close(html, g2)
assert c2 > 0, "sec2 grid close not found"
html = html[:c2] + '\n'.join(cards2) + '\n' + html[c2:]

# update section tag counts: sec3 '119 卡' -> '122 卡'; sec2 '199 卡' -> '204 卡'
assert '<span class="tag">119 卡</span>' in html, "sec3 tag not found"
assert '<span class="tag">199 卡</span>' in html, "sec2 tag not found"
html = html.replace('<span class="tag">119 卡</span>', '<span class="tag">122 卡</span>', 1)
html = html.replace('<span class="tag">199 卡</span>', '<span class="tag">204 卡</span>', 1)

# hero round append
HERO_TAIL = "三十八轮 enrich 2026-09-07(+12)</p>"
NEW_HERO = ("三十八轮 enrich 2026-09-07(+12)｜ 三十九轮 enrich 2026-09-08(+8：东莞控股高管茶话会三不原则/富春环保高管+青年+生日会/华都检测新人问卷精准指导/浙江东方工会主席一对一/国际leader-employee咖啡聊法·5② ｜ LeanIn女性职业沙龙/大数思享企业家闭门茶道/西青外企女性精英圆桌·3③)</p>")
assert HERO_TAIL in html, "hero tail anchor not found"
html = html.replace(HERO_TAIL, NEW_HERO, 1)

open(WALL, 'w', encoding='utf-8').write(html)
print("WALL updated ->", WALL, "| size", len(html))
print("wall card count now:", html.count('<div class="hl">'))

# ===== 2. tmp newcards file (all 8) =====
open(TMP, 'w', encoding='utf-8').write('\n'.join(cards2 + cards3))
print("TMP written ->", TMP)

# ===== 3. index.json append =====
idx = json.load(open(IDX, encoding='utf-8'))
items = idx if isinstance(idx, list) else idx.get('items', [])
prev_total = len(items)
prev_at = len([x for x in items if x.get('topic') == 'afternoontea'])

def summ(title, bullets):
    return f"**文章摘要**  \n本文为 下午茶研讨（Afternoon Tea Discussion）知识采集卡片，主题：{title}。\n\n**文章重点总结**  \n" + "\n".join(bullets) + "\n"

new_entries = [
  {"emoji":"🍵","title":"东莞控股首期『共说新语』高管茶话会（圆桌围坐·真对话无负担）","rel":"supervisor","st":"secondary",
   "url":"https://www.toutiao.com/article/7680531641370001960",
   "summary":["东莞控股8月28日举行首期『共说新语』高管茶话会，党委副书记、总裁与基层员工代表圆桌围坐。","秉持『真对话、无负担』原则：不设主持、不固定发言顺序、发言不记名，近两小时坦诚交流。","从战略方向到业务转型、体系优化到个人成长，员工畅所欲言，高管即时回应鼓励拥抱变化。","活动将常态长效推进、覆盖多元岗位，让每位员工声音被听见、被重视。"]},
  {"emoji":"🌿","title":"富春环保『对话·环保青鹰』高管与青年员工面对面（破冰+生日会）","rel":"supervisor","st":"secondary",
   "url":"https://m.sohu.com/a/1054423246_122014422",
   "summary":["富春环保举办『对话·环保青鹰』座谈，高管与青年员工围坐打破层级壁垒。","设破冰预热(两关键词形容自我+公司)+成长对话(高管以过来人身份务实答疑)+暖心寄语+集体生日会。","高管摒弃模板化官话，用真实故事回应，生日会增进温情与凝聚力。","以『党建+人才』融合定位常态化搭建青年交流平台。"]},
  {"emoji":"🌱","title":"华都检测新人茶话会·前期问卷做定制化职业赋能","rel":"supervisor","st":"secondary",
   "url":"https://www.toutiao.com/article/7680418588867527194",
   "summary":["华都检测新人茶话会，管理层与近10位985/211新伙伴围坐，主线『精准赋能成长、定制规划未来』。","会前发放职业规划问卷，调研岗位认知、个人优势、发展意向与困惑。","现场领导基于问卷逐一做定制化职业指导，拆解成长体系与晋升路径。","从短期目标到长期格局勾勒清晰蓝图，让迎新不流于形式。"]},
  {"emoji":"🫖","title":"浙江东方『工会主席下午茶』一对一心贴心民主管理","rel":"supervisor","st":"secondary",
   "url":"https://finance.sina.com.cn/jjxw/2025-12-25/doc-inhcyrup9067264.shtml",
   "summary":["浙江东方金融控股集团工会创新『工会主席下午茶』，每月第二周周五主席与职工代表一对一而坐。","无会议桌、无层层汇报，半年多成为连接管理层与职工心声的纽带。","一线骨干敞开心扉提瓶颈建议，转化为人才盘点/晋升机制优化参考。","职工『金点子』直送班子审议，工会从『发福利』转向『发展助推器』。"]},
  {"emoji":"☕","title":"国际实践 Leader–Employee Coffee Chat Playbook（领导—员工咖啡聊法）","rel":"supervisor","st":"secondary",
   "url":"https://simpleworkapps.com/blog/coffee-chat-with-employees/",
   "summary":["国际管理实践总结『领导—员工咖啡聊』体系，把非正式一对一咖啡/茶会话作为核心领导动作。","可复用动作：Listening Latte(单主题倾听、领导最后说、公开跟进)/Espresso Briefs(5分钟逼清晰)。","Barista Rotations(轮值选饮品)/Brewed Brainstorms(15分选项+5分投票+10分承诺)/Decaf Debriefs(低刺激复盘)。","强调领导多听少说、不防卫、关手机、真诚在场，把咖啡时刻变连接与绩效入口。"]},
  {"emoji":"🌸","title":"Lean In Shanghai『乐恰地，自在成长』女性职业发展沙龙","rel":"exec","st":"secondary",
   "url":"https://www.fortunetimes.sg/cn?p=57099",
   "summary":["Lean In Shanghai携拉菲在沪上独栋洋房办『乐恰地，自在成长』女性职业沙龙，35位女性企业家/管理者/投资人围坐。","三位嘉宾(出海VP/精品酒业总经理/二代接班人)分享职业突围，南法下午茶+白葡萄酒品鉴中圆桌对话。","围绕跳出情怀内耗、打造不可替代性、他人期许与自我追求平衡等课题，同频姐妹双向赋能。","以『Lean In』互助文化把单次活动沉淀为长期女性领导力社群。"]},
  {"emoji":"🍃","title":"大数思享『完整人生』企业家闭门茶道漫旅（哲学+茶道·限流25人）","rel":"exec","st":"secondary",
   "url":"https://bj.huodongxing.com/event/4865785493600",
   "summary":["大数思享企业家俱乐部打造小众高端闭门私享沙龙『完整人生：哲学与茶道漫旅』，限流20—25人。","特邀上财哲学系教授与上海茶业行业协会副会长，以哲学升维商业认知、以茶道沉淀内心心力。","为企业家在变局中提供静心修心、认知破局、同频链接的高阶私享场。","全程纯分享、无宣讲、无路演、零低效社交，以审核准入筛选同频掌舵人。"]},
  {"emoji":"💐","title":"西青区外企女性精英圆桌会（政企搭台·政策+异业协同）","rel":"exec","st":"secondary",
   "url":"https://www.toutiao.com/article/7614747814748324402/",
   "summary":["西青区商务局联合区妇联办2026首场『外企女性精英圆桌会』，主题『芳华致远，聚力前行』。","邀神钢铝材、大和电器等9家外企及商贸金融女性企业家代表30余人。","区商务局解读『发票抽奖』『异业联盟』政策，企业代表分享职场心得与跨界协同，专家给理财建议。","花艺插花、粘土手工与茶歇交流中放松增进友谊，以女企业家联盟持续赋能。"]},
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
        "topic": "afternoontea",
        "date": "2026-09-08",
        "round": 39,
    })

json.dump(idx, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f"INDEX updated: total {prev_total} -> {len(items)} (+{len(items)-prev_total}) | afternoontea {prev_at} -> {len([x for x in items if x.get('topic')=='afternoontea'])}")
print("DONE r39 build")
