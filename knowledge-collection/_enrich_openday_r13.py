# -*- coding: utf-8 -*-
# 知识采集自动化 · Open Day 十三轮补采（2026-08-14）
# 追加 13 张新卡到 openday.html sec2 网格 + 更新 index.json + Obsidian 笔记
import os, re, json

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KC = os.path.join(WS, "knowledge-collection")
WALL = os.path.join(KC, "openday", "openday.html")
IDX  = os.path.join(KC, "index.json")
TMP  = os.path.join(KC, "openday", ".run_newcards.tmp.html")

OBS_SUMMARY = "C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库/素材/openday/OpenDay-开放日-知识卡汇总.md"
OBS_INDEX  = "C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库/00-知识采集索引.md"
OBS_RUN    = "C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库/素材/openday/runs/OpenDay-2026-08-14-第十三轮-知识卡.md"

DATE = "2026-08-14"
ROUND = 13

# 全部 ② 上下级（地铁/轨交开放日、环保设施（污水厂）开放日、图书馆/文化馆开放日、
# 气象/地震科普基地开放日、公交集团开放日、工业旅游透明工厂开放日，领导以伙伴/专业姿态开门）
CARDS = [
 dict(emoji="🚇", title="沈阳地铁 3 号线「热线暖心相伴 畅享品质出行」市民开放日", cat="地铁开放日",
      rel=["r2"], src="secondary", source="people",
      url="https://ln.people.com.cn/n2/2026/0626/c400014-41621670.html",
      val="6月25日沈阳地铁 3 号线开通倒计时关键节点，20 余名市民代表受邀走进崭新车站，参与 96200 服务热线主题开放日，沉浸式探秘地铁运营幕后：参观智能调度、票务运维、设备保障、热线诉求受理处置全链条幕后工作体系；从一通咨询电话、一条出行建议，到后台登记、分流处置、闭环落实、回访反馈，完整服务闭环直观呈现；现场征集便民优化建议，转化为车站服务升级、热线效能提升、出行配套完善的务实举措。",
      howto="地铁开放日=「热线/调度幕后参观+服务闭环呈现+现场建议征集」；用「打破线上壁垒、市民走出屏幕走进现场」破解沟通隔阂；把群众出行痛点（通勤/就医/求学）与线路价值绑定，显民生温度；建议即纳入整改清单，把开放变信任建设。",
      note="② 城市轨交民生服务开放日，领导以开放姿态听民声、纳民意，民生恳谈范式。"),
 dict(emoji="🚇", title="无锡地铁 2026「政府开放月」专场（探秘科技密码与服务温度）", cat="地铁开放日",
      rel=["r2"], src="secondary", source="163",
      url="https://c.m.163.com/news/a/L1BNU7LU0514RDBQ.html",
      val="2026「政府开放月」无锡地铁专场邀 30 名市民走进「幕后」零距离探秘：第一站企业文化展厅（线路延伸与城市交通格局变化）；第二站模拟车站（模拟闸机/站台/车站控制室，学安全乘车与客运组织）；第三站模拟沙盘（等比例缩小，直观呈现线路走向/列车调度/信号控制）；第四站地铁运用库（列车停放/维护/检修全流程）。从发展历程到运营管理、乘车安全到列车检修，全方位认识线路平稳运行背后的系统支撑。",
      howto="地铁开放日按「展厅→模拟车站→沙盘→运用库」四站递进，用模拟装置把抽象运营变可触可感；团体预约控规模保讲解质量；以「科技赋能运营、责任守护安全、服务温暖出行」三线贯穿，既科普又建信任。",
      note="② 地铁集团政府开放月专场，市民深度探秘+科普，领导以专业姿态开门。"),
 dict(emoji="🚇", title="深圳地铁 13 号线二期北延「媒体开放日」抢先试乘（一站一景）", cat="地铁开放日",
      rel=["r2"], src="secondary", source="sznews",
      url="https://www.sznews.com/news/content/mb/2026-06/26/content_32102950.htm",
      val="深圳地铁 13 号线二期北延段通过竣工验收与安全评估、即将贯通运营前，举行媒体开放日，记者与市民代表抢先试乘凤凰城站/月亮路站/新庄站等，揭秘「一站一景」特色设计（凤凰羽翼/星河顶/国粹中医等主题）；全线 GOA4 级全自动运行+智能鹰眼巡检+开放式智能客服中心（AI 问询+低位服务台）+第三卫生间/母婴室，光明⇋南山 45 分钟跨区通勤。",
      howto="新线开通前「媒体+市民试乘」是城市轨交开放日经典范式；以「一站一景」艺术化设计做传播爆点；把全自动运行/智能客服/无障碍设施作为「科技+温度」双卖点；媒体先体验再传播，借节点放大城市交通红利。",
      note="② 城市轨交新线媒体/市民开放日，媒体传播+公众体验，领导以建设者姿态展示城市红利。"),
 dict(emoji="💧", title="首创环保集团 2026「首都国企开放日」绿色工厂探秘（供水/污水/再生水/垃圾发电）", cat="环保设施开放日",
      rel=["r2"], src="secondary", source="sina",
      url="https://finance.sina.com.cn/wm/2026-06-02/doc-inhzzivp1601459.shtml",
      val="2026「首都国企开放日」（北京市国资委主办，主题「启新程·兴国企」）恰逢六五环境日，首创环保集团启动公众开放活动，多项目同步开放：供水厂、污水处理厂、再生水厂、水环境治理、垃圾焚烧发电、环保科普教育基地；实地探访「污水变清流」「垃圾变能源」全流程，环保知识小课堂+绿色创意 DIY+环保互动打卡；北京东坝再生水厂（花园式厂区+智能加药+智慧运营平台，国家「十三五」水专项示范工程）、龙庆城西再生水厂（多媒体沙盘+实验互动区）。",
      howto="环保设施开放日=「实地探秘+科普课堂+互动体验」三件套；把「污水变清流/垃圾变能源」的不可逆过程做成可视化震撼；花园式厂区打破工厂刻板印象；用小程序「环保设施向公众开放」常态化预约，把一次性活动变长效开放。",
      note="② 环保国企开放日，政府/社区/学生/亲子多受众，科创赋能+生态惠民站位高。"),
 dict(emoji="💧", title="北京排水集团 2026 北排环保设施 8、9 月预约开放（碳中和示范厂+亚洲最大地下再生水厂）", cat="环保设施开放日",
      rel=["r2"], src="secondary", source="bjd",
      url="https://peking.bjd.com.cn/content/s6a63759fe4b03fa51a81ff8b.html",
      val="北京排水集团发布 8、9 月环保设施对外开放日程：高安屯再生水厂（设计 20 万吨/日，碳中和示范厂）、高碑店再生水厂（百万吨级、北京最大、准四类水体）、槐房再生水厂（亚洲最大全地下 MBR，60 万立方米/日，花园式地面）、清河第二再生水厂（半地下花园式）、左安门雨水泵站（防洪排水）、北排环教中心（4502㎡ 展馆，走近排水/京城水印/浊水清印展厅）。各点位按月排期、市民预约参观，把排水文化、科普教育、爱国主义教育融为一体。",
      howto="环保设施开放做成「按月排期+预约制+多点位菜单」的长效开放，而非单日盛会；用「亚洲最大全地下/碳中和示范」等标签建立专业信任；配套环教中心把参观沉淀为展览与研学，延展单次活动价值。",
      note="② 市政排水国企常态化环保开放日，科普+爱国教育+长效开放，领导以专业姿态开放。"),
 dict(emoji="💧", title="南平市 2026 六五环境日环保设施开放集锦（污水/监测/危废处置）", cat="环保设施开放日",
      rel=["r2"], src="primary", source="np.gov",
      url="https://manager.np.gov.cn/cms/html/jyqrmzf/2026-06-10/1188839724.html",
      val="2026 六五环境日（主题「全面绿色转型，共建美丽中国」），南平市生态环境部门统筹辖区环保设施开放单位集中开展科普实践：延平区实验小学师生走进塔下污水处理厂看污水「浊」到「清」；建阳环境监测站把生物显微镜/浮游植物标本带到潭山公园向市民普及「水体生态哨兵」；邵武绿益新环保带志愿者沉浸式打卡中控室/生产厂区看危废规范化处置；武夷山马厂洲污水厂邀 60 余名市民「污水探秘」；建瓯城西污水厂邀人大/政协/法院志愿者开展「污水变清流」主题开放。",
      howto="环保设施开放日做「全域统筹+分点集锦」，以六五环境日为节点一次性铺开；把监测仪器/标本搬到公园做「移动科普」降低门槛；邀请人大政协法院志愿者参与，兼顾监督与科普；青少年实地看治污流程播撒绿色种子。",
      note="② 地市级生态环境系统环保设施公众开放日（政府官网一手），透明增进了解+公众参与凝聚共识。"),
 dict(emoji="📚", title="潍坊市图书馆 2026「市民开放日」解锁书香新体验（《全民阅读促进条例》实施日）", cat="图书馆开放日",
      rel=["r2"], src="secondary", source="wfcmw",
      url="https://www.wfcmw.cn/334174/2026/01/42420850.html",
      val="2月1日《全民阅读促进条例》正式实施当天，潍坊市图书馆以「品质焕新·阅见未来」为主题举办「品质提升年」市民开放日，全馆各区域开放深度探访：参观古籍保护成果、体验尼山书院国学活动；现场解锁 AI 馆员服务、城市书房等智慧阅读模式、提升数字阅读技能；特设文旅推介区、XR 数字艺术展等打造文旅融合潮趣书香市集；填写调查问卷、投递「金点子」以共建者身份为图书馆发展建言；同步开展少儿英语阅读、茶艺品鉴、谱牒文献精品展等十余项活动。",
      howto="图书馆开放日=「阵地开放+智慧体验+文旅市集+金点子建言」；借法规实施节点（全民阅读促进条例）做传播；用 AI 馆员/XR 数字艺术展把传统场馆变潮趣；现场问卷+金点子把市民变「共建者」而非旁观者。",
      note="② 公共图书馆市民开放日，文化惠民+智慧阅读+公众共建，领导以服务者姿态开门。"),
 dict(emoji="🎭", title="高明区文化馆 2026 开放日活动（全国文化馆服务宣传周·人民的终身美育学校）", cat="文化馆开放日",
      rel=["r2"], src="secondary", source="qq",
      url="https://new.qq.com/rain/a/20260523A08ZHU00",
      val="2026 全国文化馆服务宣传周主场活动在厦门举行（主题「文化馆：人民的终身美育学校」），高明区文化馆作为广东省唯一县级文化馆代表入围。借盛会契机，高明区文化馆开放日活动 5月18日启动持续至24日，5月23日特办「小城故事」开放日：六大板块同步（陶艺展示/美术书法比赛/乡镇美育成果展/公益培训家长开放日/精品文艺演出/近三年服务成果展）；坚持开放共享、扎根基层，引导群众从「文化旁观者」变为「美育参与者」。",
      howto="文化馆开放日借「全国服务宣传周」节点放大声量；用「六大板块」覆盖展示/比赛/培训/演出/成果，把场馆能力全景打开；「公益培训家长开放日」把常态服务透明化；核心是把群众从旁观者变参与者，提升文化获得感。",
      note="② 基层文化馆开放日，公共文化服务场景打开+群众美育参与，领导以组织者姿态开门。"),
 dict(emoji="🌤️", title="中国气象局 2026 世界气象日京区单位开放（气象科技展馆+风云卫星+观测场）", cat="气象科普开放日",
      rel=["r2"], src="primary", source="cma",
      url="https://www.cma.gov.cn/2011xwzx/zdbk/jdbkxw/202603/t20260317_7659071.html",
      val="2026 世界气象日（主题「测今日气象，护明日家园」），中国气象局（3月21日）与北京市气象探测中心/观象台（3月21日）对社会公众开放：开放气象科普活动区、气象设备展示区、中国气象科技展馆、气象观测场；通过互动/直播/答题/打卡/读书了解气象观测/预报/服务/数据，参观风云卫星、雷达、气象探测无人机等装备模型；北京市观象台开放地面观测场、高空放球场、气象科普馆、应急指挥车、气象历史公园，开展科技展与二十四节气主题活动。实名预约、分时段免费参观。",
      howto="国家级科普基地开放日=「展馆+装备+观测场+互动答题打卡」；用风云卫星/雷达/无人机等大国重器做吸引力；实名分时段预约控规模保安全；把世界气象日节点与科普结合，面向青少年播撒科学种子。",
      note="② 国家级气象科普基地公众开放日（气象局官网一手），专家对话+科技互动，领导以科普者姿态开放。"),
 dict(emoji="🌪️", title="梧州市气象局 2026 世界气象日开放（沉浸式科普+校园科普集市+主播体验）", cat="气象科普开放日",
      rel=["r2"], src="primary", source="cma",
      url="http://gx.cma.gov.cn/wzs/dsyw_9915/202604/t20260407_7714265.html",
      val="2026 世界气象日，梧州市气象局、气象学会在榜山气象科普教育基地开展气象开放活动，与 4 所中小学以「沉浸式科普+科技互动」为市民尤其是青少年提供平台，吸引近 500 人参与；开放气象观测场和气象科普展厅，宣传地基垂直遥感装备、北斗探空系统；科协「机器狗」智能讲解员；首次亮相的校园科普集市由师生与气象工作者共同做「春分立蛋/伯努利原理/水循环演示/拼中国地图/风之谷实验室」等沉浸式展示；设风云气象扭蛋互动区、气象主播体验区、「气象物语」文创定制；同步新媒体直播「云参观」近 700 人在线。",
      howto="气象开放日把「专家讲解+校园集市+互动扭蛋+主播体验+文创」组合，用青少年熟悉的语言降维科普；机器狗讲解员/主播体验区制造记忆点；直播「云参观」突破线下名额限制；联合中小学做共建，把一次活动变长期科学教育。",
      note="② 地市级气象科普基地公众开放日（气象局官网一手），青少年沉浸式科普+互动体验。"),
 dict(emoji="🌍", title="九江地震监测中心站 2026 科普开放日（防灾减灾日+世界计量日·测氡仪比测台站）", cat="地震科普开放日",
      rel=["r2"], src="primary", source="jxsdzj",
      url="https://www.jxsdzj.gov.cn/jxsdzjj/tzgg925/pc/content/content_2051824609623281664.html",
      val="第18个全国防灾减灾日（主题「人人讲安全、个个会应急」）与「世界计量日」期间，九江地震监测中心站开展科普开放日（5月11-20日，每批限60人预约）：站内建于1972年，辖九江/上饶/景德镇地震监测运维、震情跟踪、应急响应，为中国地震局认定的「九江测氡仪比测台站」，推动测量结果可信可比、为科学决策提供精准计量数据；面向大中学生志愿者、大中小学生团体及社会群众开放，中小学生需集体组织或家长陪同。",
      howto="地震科普开放日=「台站参观+防灾减灾知识普及+计量信任科普」；用「测氡仪比测台站」等专业资质建立科学信任；限60人预约控规模保安全；紧扣防灾减灾日节点，把开放日变成自救互救能力培育场。",
      note="② 地震监测科普基地公众开放日（地震局官网一手），防震减灾科普+专业信任，专家以导师姿态开放。"),
 dict(emoji="🚌", title="九江市国资委 2026「政府开放日」走进九江公交（智慧调度+新能源维保+开门纳谏）", cat="公交开放日",
      rel=["r2"], src="primary", source="jiujiang.gov",
      url="https://www.jiujiang.gov.cn/zwzx/ztbd/2026zfkf/hdbd/202607/t20260703_7268256.html",
      val="6月25日九江市国资委以「扛牢国企担当便利市民出行」为主题在市公交公司举办 2026「政府开放日」，10 余名群众代表受邀走进九江公交：公交集团负责人介绍新能源公交更新、场站改造、智慧公交平台、城乡公交一体化等民生实事；运营部门解读学生优惠乘车、定制专线、节假日便民专线及线路优化规划；座谈答疑环节代表围绕线路增减、候车设施、车辆舒适度、准点率等踊跃提问，国资委与公交集团逐一解答并登记意见；随后分批参观智慧调度指挥中心、新能源公交车维保车间、纯电动公交整车内饰，观摩安全检修流程。",
      howto="公交集团开放日=「负责人讲民生成果+运营政策解读+座谈答疑纳谏+实地参观调度/维保」；用「智慧调度+新能源维保」展示硬实力；座谈把群众痛点（准点率/接驳）现场登记转化；国资委牵头彰显主动接受监督、开门纳谏。",
      note="② 公交国企政府开放日（九江市政府官网一手），民生窗口+开门纳谏+信任重建范式。"),
 dict(emoji="🏭", title="太仓 2026 工业旅游公交专线（元气森林透明工厂+莱卡尔烘焙城堡+耐克零碳园区）", cat="工业旅游开放日",
      rel=["r2"], src="secondary", source="ifeng",
      url="https://js.ifeng.com/c/8tFuCjeVwKk",
      val="第16个中国旅游日（5月19日），太仓工业旅游公交专线开通：一条环线 9 站串起 10 余家企业与工厂，坐公交从烛艺工坊逛到深海蟹仓、烘焙城堡、气泡水王国、百年老字号肉松铺。元气森林太仓工厂设全透明参观走廊，自动化机械臂/无菌灌装/智能检测全流程一目了然，并推「透明工厂奇遇记」工业研学（气泡水实验+环保创意工坊）；莱卡尔烘焙城堡 1500㎡ DIY 研学教室隔玻璃看自动化生产线并动手做面包；耐克中国物流中心（亚洲最大零碳智慧物流园）设工厂店。公交专线把分散工厂串成「线性体验」，实现「走进去是工厂、买出来是特产」。",
      howto="工业旅游开放日用「公交专线串联分散工厂」破解工业旅游资源碎片化；透明参观走廊让消费者亲眼见证产品诞生、以最透明方式建立品质信任；「前店后厂」把参观直接变消费闭环；DIY 研学把工厂变亲子科普课堂。",
      note="② 工业旅游/透明工厂公众开放日，公交串厂+透明生产+前店后厂，企业以伙伴姿态开放建立品牌信任。"),
]

def rel_badges(rels):
    m={"r1":"平级","r2":"上下级","r3":"高管间"}
    return "".join(f'<span class="badge {r}">{m[r]}</span>' for r in rels)

def src_badge(st):
    return '<span class="badge b1">一手</span>' if st=="primary" else '<span class="badge b2">二手</span>'

def display_url(u):
    d=u.split("//",1)[-1].replace("www.","",1) if u.startswith("http") else u
    d=d.rstrip("/")
    return d[:78]+"…" if len(d)>78 else d

def card_html(c):
    rel=rel_badges(c["rel"])
    sb=src_badge(c["src"])
    return f'''                <div class="hl">
      <div class="top"><span class="emoji">{c['emoji']}</span><h3>{c['title']}</h3><span class="cat">{c['cat']}</span>{rel}{sb}</div>
      <p class="val">{c['val']}</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">{c['howto']}</div></details>
      <div class="src">🔗 <a href="{c['url']}" target="_blank">{display_url(c['url'])}</a></div>
      <div class="note">适用：{c['note']}</div>
    </div>
'''

def main():
    html=open(WALL,encoding="utf-8").read()
    new_blocks="".join(card_html(c) for c in CARDS)

    # 幂等守卫：若首张新卡标题已在墙内，跳过 wall/index/tmp 更新（避免重复插入）
    already = CARDS[0]["title"] in html
    if not already:
        # 1) 找到 sec2 网格并将新卡插入其闭合 </div> 之前
        sec2_pos=html.index('<div class="sec sec2">')
        gs=html.index('<div class="grid">', sec2_pos)
        depth=0; j=gs
        while j<len(html):
            if html[j:j+4]=='<div': depth+=1; j+=4
            elif html[j:j+6]=='</div>':
                depth-=1; j+=6
                if depth==0: break
            else: j+=1
        close_pos=j-6
        html=html[:close_pos]+new_blocks+"\n"+html[close_pos:]

        # 2) 更新 sec2 标签计数 46 -> 59
        html=html.replace('    <span class="tag">46 卡</span>', '    <span class="tag">59 卡</span>', 1)

        # 3) 更新 hero p（追加十三轮说明）
        hero_p_start=html.index('<div class="hero">')
        p_start=html.index('<p>', hero_p_start)
        p_end=html.index('</p>', p_start)
        hero_note='｜ 十三轮补采 2026-08-14(+13：地铁/轨交开放日+环保设施(污水厂)开放日+图书馆/文化馆开放日+气象/地震科普基地开放日+公交集团开放日+工业旅游透明工厂开放日)'
        html=html[:p_end]+hero_note+html[p_end:]
        # 同步更新 hero p 开头的总计数 51 -> 64
        html=html.replace('累计 51 卡','累计 64 卡',1)

        open(WALL,"w",encoding="utf-8").write(html)
        print(f"wall updated: {WALL}")

        # 4) 写 .run_newcards.tmp.html
        open(TMP,"w",encoding="utf-8").write(new_blocks)
        print(f"tmp newcards: {TMP}")

        # 5) 更新 index.json
        idx=json.load(open(IDX,encoding="utf-8"))
        for c in CARDS:
            idx.append({
                "title":c["title"],"normKey":c["title"],"url":c["url"],
                "sourceType":c["src"],"relation":"supervisor","summary":c["val"][:240],
                "topic":"openday","source":c["source"],
            })
        json.dump(idx,open(IDX,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
        print(f"index.json appended {len(CARDS)} -> total {len(idx)}")
    else:
        print("wall/index already contains r13 cards, skip re-insert")

    # 6) Obsidian 汇总笔记更新
    summ=open(OBS_SUMMARY,encoding="utf-8").read()
    summ=summ.replace("共 51 张","共 64 张")
    summ=summ.replace("**51 卡**","**64 卡**").replace("一手 20 + 二手 31","一手 24 + 二手 40")
    summ=summ.replace("②上下级 46 卡 / ③高管间 5 卡","②上下级 59 卡 / ③高管间 5 卡")
    summ=summ.replace("**51 卡**，已剔除平级","**64 卡**，已剔除平级")
    # 追加 r13 独立页链接
    summ=summ.replace(
      "- 当轮独立页（第十二轮）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/runs/openday-2026-08-13-r12.html",
      "- 当轮独立页（第十二轮）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/runs/openday-2026-08-13-r12.html\n- 当轮独立页（第十三轮）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/runs/openday-2026-08-14-r13.html")
    # 在卡片总表末尾追加 13 行（在「## 卡片墙（HTML 交互版）」之前）
    rows="".join(
        f"| {c['title']}（openday.html） | 4 | {'一手' if c['src']=='primary' else '二手'} | ②上下级 | {c['val'][:60]}…\n"
        for c in CARDS)
    summ=summ.replace("## 卡片墙（HTML 交互版）", rows+"\n## 卡片墙（HTML 交互版）")
    # 适用&备注追加本轮说明
    summ=summ.replace("硬排除：家庭日/家属开放日、投资者/资本市场/IR/证监局开放日（非 HRBP 企业文化活动向）。",
      "硬排除：家庭日/家属开放日、投资者/资本市场/IR/证监局开放日（非 HRBP 企业文化活动向）。十三轮（2026-08-14）新增聚焦「地铁/轨交开放日」（沈阳 3 号线热线主题/无锡地铁政府开放月专场/深圳 13 号线新线媒体试乘，幕后调度+服务闭环+科技温度）、「环保设施（污水/再生水/垃圾发电）开放日」（首创环保首都国企开放日/北排 8-9 月预约开放/南平六五环境日集锦，污水变清流+花园式厂区）、「图书馆/文化馆开放日」（潍坊市图书馆市民开放日+高明区文化馆服务宣传周，智慧阅读+群众美育参与）、「气象/地震科普基地开放日」（中国气象局世界气象日/梧州沉浸式科普集市/九江地震监测中心站，风云卫星+主播体验+防灾减灾）、「公交集团开放日」（九江公交政府开放日，智慧调度+新能源维保+开门纳谏）、「工业旅游透明工厂开放日」（太仓工业旅游公交专线，元气森林透明工厂+前店后厂）。")
    open(OBS_SUMMARY,"w",encoding="utf-8").write(summ)
    print(f"summary note updated: {OBS_SUMMARY}")

    # 7) 00-索引更新
    idx0=open(OBS_INDEX,encoding="utf-8").read()
    idx0=idx0.replace(
      "｜ 2026-08-13 十二轮补采 +13（博物馆/纪念馆公众开放日+医院公众开放日+政府开放月/政务公开+高校实验室开放日+社区公共空间开放日+腾讯企鹅开放日）",
      "｜ 2026-08-13 十二轮补采 +13（博物馆/纪念馆公众开放日+医院公众开放日+政府开放月/政务公开+高校实验室开放日+社区公共空间开放日+腾讯企鹅开放日）｜ 2026-08-14 十三轮补采 +13（地铁/轨交+环保设施(污水厂)+图书馆/文化馆+气象/地震科普基地+公交集团+工业旅游透明工厂开放日）")
    idx0=idx0.replace("**51 卡**，已剔除平级","**64 卡**，已剔除平级").replace("一手 20 + 二手 31","一手 24 + 二手 40")
    idx0=idx0.replace("②上下级 46 卡 / ③高管间 5 卡","②上下级 59 卡 / ③高管间 5 卡")
    # 找 Open Day 卡片表末尾追加 13 行
    s=idx0.find("## 主题：Open Day")
    tstart=idx0.find("| 卡 |", s)
    seg=idx0[tstart:]
    lines=seg.split("\n")
    last=0
    for k,ln in enumerate(lines):
        if ln.strip().startswith("|"): last=k
    insert_pos=tstart+sum(len(lines[i])+1 for i in range(last+1))
    newrows="".join(
        f"| {c['title']}（openday.html） | 4 | {'一手' if c['src']=='primary' else '二手'} | ②上下级 | {c['val'][:40]}…\n"
        for c in CARDS)
    idx0=idx0[:insert_pos]+newrows+idx0[insert_pos:]
    open(OBS_INDEX,"w",encoding="utf-8").write(idx0)
    print(f"00-index updated: {OBS_INDEX}")

    # 8) 新建本轮独立笔记 md
    tbl="".join(
        f"| {i+1} | {c['title']} | {'一手' if c['src']=='primary' else '二手'} | ②上下级 | {c['url']}\n"
        for i,c in enumerate(CARDS))
    md=f"""---
title: Open Day 开放日 第十三轮 知识卡
tags: [知识采集, Open Day 开放日, 自动化采集, 轮次]
date: 2026-08-14
type: 自动化采集
round: 13
---

# Open Day 开放日 · 第十三轮补采知识卡（2026-08-14）

> 本轮为「Open Day 开放日」主题第 13 轮自动补采，新增 **13 张**知识卡（②上下级 13；一手 4 / 二手 9）。
> ⚠️ 硬过滤已生效：家庭日/家属开放日、投资者/资本市场/IR/证监局开放日不采。

## 独立页（GitHub Pages · 公开）
https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/runs/openday-2026-08-14-r13.html

## 本机路径
knowledge-collection/openday/runs/openday-2026-08-14-r13.html

## 累计总索引（卡片墙）
https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday.html

## 本轮卡片表（13 张）
| # | 卡 | 一手/二手 | 适用关系 | 来源 |
|---|---|---|---|---|
{tbl}
## 本轮聚焦点
- 地铁/轨交开放日：沈阳 3 号线热线主题（幕后调度+服务闭环+现场纳谏）、无锡地铁政府开放月专场（展厅→模拟车站→沙盘→运用库四站递进）、深圳 13 号线新线媒体试乘（一站一景+全自动运行+智能客服）。
- 环保设施（污水/再生水/垃圾发电）开放日：首创环保首都国企开放日（多项目同步+污水变清流+花园式厂区）、北排 8-9 月预约开放（亚洲最大全地下再生水厂+环教中心长效开放）、南平六五环境日集锦（全域统筹+移动科普+志愿者监督）。
- 图书馆/文化馆开放日：潍坊市图书馆市民开放日（AI 馆员+XR 数字艺术展+金点子建言）、高明区文化馆服务宣传周（六大板块+群众美育参与）。
- 气象/地震科普基地开放日：中国气象局世界气象日（风云卫星+观测场+分时段预约）、梧州沉浸式科普集市（机器狗讲解+主播体验+校园共建）、九江地震监测中心站（测氡仪比测台站+防灾减灾）。
- 公交集团开放日：九江公交政府开放日（智慧调度+新能源维保+开门纳谏）。
- 工业旅游透明工厂开放日：太仓工业旅游公交专线（元气森林透明工厂+前店后厂+DIY 研学）。
"""
    open(OBS_RUN,"w",encoding="utf-8").write(md)
    print(f"run note created: {OBS_RUN}")
    print("DONE enrich")

if __name__=="__main__":
    main()
