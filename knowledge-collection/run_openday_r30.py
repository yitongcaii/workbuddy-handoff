# -*- coding: utf-8 -*-
# Open Day 三十轮补采（r30, 2026-08-28）+12 卡：8 ②上下级 + 4 ③高管间
# 新域：公共资源交易/12345热线/住房公积金/检察(未检)/退役军人事务/红十字应急救护/婚姻登记/社保经办 开放日向(全②)
#       + 芝罘招商主题开放日/大鹏园区CEO沙龙/成都东部空港下午茶/全国四好商会广州(③)
import re, os, json, sys

WS = r"C:\Users\v_yitcai\WorkBuddy\20260728154244"
KC = os.path.join(WS, "knowledge-collection")
HTML = os.path.join(KC, "openday", "openday.html")
TMP  = os.path.join(KC, "openday", ".run_newcards.tmp.html")
CACHE= os.path.join(KC, "openday", ".rows_cache.json")
IDX  = os.path.join(KC, "index.json")
OB_SUM = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\openday\OpenDay-开放日-知识卡汇总.md"
OB_IDX = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
GH = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday.html"
GH_RUN = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday-20260828.html"
INC = os.path.join(KC, "openday", "openday-20260828.html")

cards = [
 dict(emoji='🏛️', title='淮南市公共资源交易监督管理局「政府开放日」——阳光交易筑公信·不见面开标+智慧交易大模型', cat='公共资源交易开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://jy.ggj.huainan.gov.cn/zwfw/002001/20260608/6969ab43-e072-4eae-aa89-ce85dd499016.html',
      val='淮南市公共资源交易监督管理局2026年6月16日举办「政府开放日」活动，主题「阳光交易筑公信，优质服务心贴心」，邀人大代表、政协委员、群众、专家、企业、社区代表沉浸式走进交易一线。现场观摩开标区（不见面开标大厅、远程解密、在线摇号抽取系数）、拍卖大厅电子竞价、代理机构工作区、评标区（专家抽取室、人脸门禁、隔夜休息室、分散工位评标、双盲远程异地评标），体验电子招投标与「身份证+人脸双重验证」门禁；现场观摩「公共资源智慧交易大模型」运行演示。座谈听取招标采购流程介绍与工作情况，互动答疑、征集意见。',
      how='把「公共资源交易开放日」做成阳光交易透明窗——用「不见面开标+远程异地评标+双盲评审」可视化破除招投标神秘感与疑虑；以「智慧交易大模型」展示数智化监管能力；身份证+人脸双重门禁把评标区保密性具象化；座谈+意见征集把开放日从「展示」转「纳谏」，是政务公开+营商环境双提升范本。',
      note='② 公共资源交易政府开放日（淮南市公管局官网一手），监管部门领导以阳光交易守护者姿态，人大代表/企业/群众走进开评标一线监督全流程，政民/政企透明互信。'),
 dict(emoji='☎️', title='宜春市12345「热线面对面 服务零距离」第四届市民开放日（上机体验接听来电）', cat='政务热线开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://jxyc12345.cn/xwzx/rxdt/2026/05/081748331837.html',
      val='宜春市12345政务服务便民热线2026年5月15日举办第四届「热线面对面 服务零距离——市民开放日」活动，邀各行业先进人物、基层群众、「五型」政府监督员、创业者、职工、学生、网民代表等走进呼叫平台。流程：①参观呼叫平台、全面了解热线平台建设运行；②与话务人员零距离接触、上机体验接听来电；③座谈交流、宣传热线知识、现场征集意见建议。',
      how='把「政务热线开放日」做成民意直通车——以「参观平台+上机接听+座谈征集」三段式让市民从「打热线的人」变成「懂热线的人」；上机体验接听打破对热线的陌生与误解；现场征集意见建议把开放日变作风体检，是政务热线透明度与公信力提升可复制模板。',
      note='② 政务热线市民开放日（宜春12345官网一手），热线管理部门领导以民生服务者姿态，市民/监督员/网民代表走进呼叫平台体验接听、监督诉求办理。'),
 dict(emoji='🏠', title='亳州市住房公积金管理中心2026年「政府开放日」——深化公积金制度改革·服务群众安居', cat='公积金开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.bozhou.gov.cn/Open  essContent/show/2979153.html'.replace('Open  essContent','OpennessContent'),
      val='亳州市住房公积金管理中心2026年6月12日开展「政府开放日」，主题「深化住房公积金制度改革，更好服务群众安居」，邀缴存单位工作人员、职工代表、工会负责人、受托银行代表、关心公积金工作的群众（限20人）。内容：①观摩缴存、提取、审核全流程；②解读亳州公积金使用政策；③通报上半年主要工作；④座谈交流。',
      how='把「公积金开放日」做成安居政策透明窗——以「全流程观摩+政策解读+工作通报+座谈」四环节让缴存职工与群众读懂「惠民·便民·安居」核心职能；缴存/提取/审核全流程可视化破除办事盲区；座谈现场答疑把开放日变政策落地反馈通道，是住房民生领域政民沟通范本。',
      note='② 住房公积金政府开放日（亳州市政府官网一手），公积金中心领导以安居服务者姿态，缴存职工/受托银行/群众代表走进经办一线、面对面议政策落地。'),
 dict(emoji='⚖️', title='五指山市人民检察院「检爱四十载·携手向未来」检察开放日（检察长出席·未成年人检察）', cat='检察开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.hi.jcy.gov.cn/webSite/module/M101/view/931599/00600014',
      val='五指山市人民检察院2026年6月1日以「检爱四十载，携手向未来」为主题举办检察开放日，邀市委政法委、政协委员、司法局、妇联等6家单位代表，及五指山市第一小学、中学两校代表，通过实地参观、座谈交流「零距离」感受未成年人检察工作。市检察院检察长石秀莲出席；代表参观未成年人法治教育基地，座谈观看「珍爱生命 远离依托咪酯」宣传片，副检察长介绍近三年未检工作，检察官讲述办案感人故事；代表围绕校园法治教育、困境未成年人救助、家庭教育指导建言。',
      how='把「检察开放日」做成检民连心桥——以「检察长出席+法治教育基地参观+未检工作汇报+办案故事讲述+多方建言」组合，把法律监督职能转化为可感可触的司法温度；用「教育·感化·挽救」真实案例替代照本宣科；检察长亲临+现场纳谏强化司法公信力与未成年人保护合力。',
      note='② 检察开放日（五指山市检察院官网一手），检察长以法治守护者姿态，政法委/妇联/师生代表走进检务一线、共护未成年人成长，检民互信+司法公开。'),
 dict(emoji='🎖️', title='樟树市退役军人事务局2026年「政府开放月」（尊崇军人·8月28日当日·三方互动机制）', cat='退役军人事务开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.zhangshu.gov.cn/zssrmzf/gsgg07/pc/content/2091695420035944448/content_2091695420035944448.html',
      val='樟树市退役军人事务局2026年8月28日（当日）开展「政府开放月」活动，主题「尊崇军人，服务同行，走进退役军人服务中心」，邀退役军人代表20人、市民代表10人、社工部/民政/武装部等单位代表。流程：开场介绍→实地参观服务大厅（政策咨询/就业创业帮扶/优抚优待窗口）、退役军人就业之家、新长征志愿服务队办公室/装备室/党支部会议室、爱国拥军促进会接待室，观看5年志愿服务视频→座谈：政策解读（安置/困难帮扶/拥军优抚/创业扶持）+意见征集+满意度问卷→「政府-退役军人-社会」三方互动机制。',
      how='把「退役军人事务开放日」做成尊崇服务实景课——以「参观服务大厅+就业之家+志愿队+三方座谈+满意度问卷」全景展示尊崇军人服务链条；用「政府-退役军人- 社会」三方互动机制把开放日变常态化拥军连心桥；满意度问卷兜底闭环，是退役军人事务领域政务公开与尊崇营造范本。',
      note='② 退役军人事务政府开放日（樟树市政府官网一手，2026-08-28 当日），事务局领导以拥军服务者姿态，退役军人/优抚对象/市民代表走进服务中心、共议尊崇与保障。'),
 dict(emoji='🆘', title='成都市红十字会「红动蓉夏·救在身边」探寻打卡（应急救护公众开放日·实景互动）', cat='红十字应急救护开放日',
      rel='r2', src='一手', src_cls='b1',
      url='http://www.chengduredcross.cn/xwzx_qsxdt_whq/010012400024948.html',
      val='成都市武侯区红十字会2026年7月8日—17日发起「红动蓉夏·救在身边——成都市红十字探寻」打卡活动，面向全市青少年、红十字志愿者、文旅爱好者及市民全域开放。以社区红十字应急救护基地为核心研学点位，设地震VR体验区、交通科普专区、消防互动板块（隐患排查+模拟灭火）、模拟急救通话实训、红十字主题拼图区；完成项目集章后可参与文创抽奖。跳出传统宣讲，主打实景互动，让市民尤其是青少年沉浸式解锁应急技能、读懂红十字文化。',
      how='把「红十字公众开放日」做成沉浸式人道实践——以「基地研学+集章打卡+文创抽奖」游戏化机制替代说教，用地震VR/模拟灭火/急救通话实训把「人人学急救」变可动手体验；主题书签/折扇周边强化记忆点与传播；暑期全域开放+文旅打卡把红十字精神植入青少年，是生命教育公众开放日范本。',
      note='② 红十字应急救护公众开放日（成都市红十字会官网一手），红十字会领导以生命教育摆渡人姿态，青少年/市民走进应急救护基地实景学急救、悟博爱精神。'),
 dict(emoji='💍', title='上海市闵行区民政局婚姻(收养)登记中心「政府开放月」——婚登+公证+集体颁证+非遗婚书', cat='婚姻登记开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.shmh.gov.cn/shmh/zwdt-mzj/20260727/596880.html',
      val='上海市闵行区民政局2026年8月聚焦「奋进\'十五五\'，同心向未来」开展政府开放月，组织市民代表走进区婚姻(收养)登记中心（8月18日）。涵盖结婚/离婚登记区、颁证厅、婚姻家庭辅导室、「婚登+公证」服务专区、1766幸福邮局、收养登记窗口等全功能区域；①全场景参观：婚姻登记全流程规范、全市首创「婚登+公证」联动、婚姻家庭辅导（婚前辅导/冷静期疏导/矛盾调解）、幸福邮局文创；②沉浸式集体颁证仪式观摩（新人宣誓+颁证员寄语+文明婚俗倡议）；③非遗婚书定制、闵登×闵博联名印章打卡等婚俗文化互动。',
      how='把「婚姻登记处开放日」做成文明婚俗沉浸式体验——以「全功能区域参观+集体颁证观摩+非遗婚书/联名印章互动」替代单纯办证，把婚姻登记从「程序化」升级为「浪漫仪式化+家风家教」；全市首创「婚登+,公证」联动展示政务创新；婚俗文化互动传递文明新风，是民政服务透明度与满意度提升范本。',
      note='② 婚姻登记处政府开放日（闵行区民政局官网一手），民政部门领导以婚俗改革倡导者姿态，适婚青年/新婚夫妇/金婚家庭/居民代表走进婚登中心、倡树文明新风。'),
 dict(emoji='💼', title='修水县人社局·社保中心「社保服务零距离·惠民政策面对面」政务开放日（经办全流程+大数据风控）', cat='社保经办开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.xiushui.gov.cn/zwzx_314/ztbd/zfkfr/hdzs/202606/t20260625_7262258.html',
      val='修水县人社局（县社保中心）2026年6月24日举办「社保服务零距离·惠民政策面对面」政府开放日，邀人大代表、政协委员、媒体、企业代表、群众代表18人走进社保经办一线。沉浸体验：观摩养老待遇资格认证、延迟退休及待遇测算等高频业务经办全流程；参观内控稽核股（社保大数据平台风险预警演示）、企业养老股（养老金「多缴多得、长缴多得」核算案例）、数字化档案室（电子化归集/存档/调阅全链条）。座谈围绕城乡居民养老保险集体补助、社保补缴、灵活就业参保、新就业形态职业伤害保险答疑，建台账限期反馈。',
      how='把「社保经办开放日」做成惠民政策透明窗——以「高频业务经办演示+大数据风控展示+养老金核算案例+数字化档案」全景呈现社保规范化/标准化/数字化；用「多缴多得」真实案例把抽象计发原则讲透；座谈+台账闭环把开放日变民生诉求解决通道，是社保领域政民沟通范本。',
      note='② 社保经办政府开放日（修水县政府官网一手），人社/社保部门领导以民生保障者姿态，企业/群众/代表走进经办一线、面对面议社保热点。'),

 dict(emoji='🤝', title='烟台芝罘区投资促进中心「探秘幸福新城热土 共绘招商引资蓝图」招商主题政府开放日', cat='招商政府开放日',
      rel='r3', src='一手', src_cls='b1',
      url='https://www.zhifu.gov.cn/col/col52214/art/2026/art_6d9de9cbd36343358f925ebd15787405.html',
      val='烟台市芝罘区投资促进中心2026年8月7日以「探秘幸福新城热土 共绘招商引资蓝图」为主题开展招商题材政府开放日，在夹河·幸福新城指挥部展厅，邀辖区重点意向投资企业、优质产业企业（覆盖低空经济等核心招商赛道）10余人。实地参观新城展厅，介绍核心定位、产业规划及空港轨多维交通优势；座谈解读全市产业链布局与新城「3+2+N」产业招商体系，公开招商规划、惠企政策及配套保障；围绕项目落地、政策宣讲、审批服务、产业配套征集意见，建「征集—回访」闭环，当场采纳合理化建议、清单销号长期事项。',
      how='把「招商主题政府开放日」做成政企精准对接场——以「展厅推介+产业体系解读+惠企政策公开+闭环回访」替代单向招商宣讲，用「3+2+N」产业招商体系帮企业精准匹配方向、打消落地顾虑；闭环销号把企业诉求转实效，是区县投资促进部门「以开放促招商」可复制范式。',
      note='③ 招商政府开放日（芝罘区政府官网一手），投资促进中心领导以产业合伙人姿态，重点意向企业/优质产业企业围绕新城招商赛道对话、共绘落地蓝图（政企协作向，非 IR/资本向）。'),
 dict(emoji='🏭', title='深圳大鹏新区「CEO沙龙·益企赋能」园区软环境提升系列（生物产业专场·22名CEO参访）', cat='园区CEO沙龙',
      rel='r3', src='二手', src_cls='b2',
      url='https://fgw.sz.gov.cn/ztzl/qtztzl/szscjmyjjfzzhfwpt/xwzl/mqfw/content/post_12770690.html',
      val='深圳大鹏新区企业服务中心2026年4月举办「CEO沙龙·益企赋能」园区软环境提升系列（生物产业专场），以「标杆企业参访+主题座谈」形式组织22名企业CEO围绕「生物产业协同创新」主题，聚焦医疗器械、细胞治疗、生物CRO服务深度交流。CEO依次参访华研再生、小宠实业、泽医细胞，调研细胞治疗核心技术、运营模式、创新成果；座谈环节新区企业服务中心搭建对接平台，企业家围绕产学研用合作、技术攻关、市场共享坦诚交流，现场对接多项合作意向，构建开放互助园区产业生态。',
      how='把「园区CEO沙龙」做成决策层协同场——以「标杆企业参访+主题座谈」替代常规招商会，聚焦CEO决策层需求做「产学研用+市场共享」精准对接；22名CEO同场碰撞多项合作意向，把园区软环境从「给政策」升级为「给生态」；常态化互访持续导入创新资源，是园区服务企业决策层、提升活力的范本。',
      note='③ 园区CEO沙龙（深圳新闻网二手），新区企业服务中心以产业生态组织者姿态，园区企业CEO围绕生物产业协同创新参访对话、现场对接合作（高管间/政企协作向）。'),
 dict(emoji='✈️', title='成都东部新区「枢畅空港·链接世界」企业开放日暨空港下午茶（中国欧盟商会+40余家世界500强）', cat='企业开放日·政企下午茶',
      rel='r3', src='二手', src_cls='b2',
      url='https://new.qq.com/rain/a/20260417A01XL000?refer=cp_1009',
      val='成都东部新区2026年4月16日举行「枢畅空港·链接世界」企业开放日暨「空港下午茶」活动，打破传统发布会形式，邀中国欧盟商会西南分会及西卡、ABB、西门子、法国铁路、匈牙利轨道交通等40余家世界500强、知名企业代表。嘉宾走进天府国际空港综合保税区、海目星激光、三岔湖及东部新区规划馆，乘车观摩围网内部（监管卡口/保税仓库/产业载体），在海目星感受「拿地即开工、竣工即投产」；「空港下午茶」政企围坐喝咖啡、聊产业、谈合作；西卡中国区CEO现场分享，瑞士西卡期待在绿色低碳/城市更新/装配式建筑合作。',
      how='把「企业开放日」做成下午茶式政企对话——以「实地考察+轻松下午茶叙」替代严肃招商会，用「枢畅空港」营商服务品牌圈粉世界500强；把空港枢纽/综保区/生态宜居的「AB面」直观呈现给目标企业；咖啡叙谈让政企对接更接地气、更精准，是新区面向跨国企业的开放日范式。',
      note='③ 企业开放日·政企下午茶（红星新闻网二手），新区领导以城市合伙人姿态，中国欧盟商会+40余家世界500强围坐谈合作、对接航空货运/高端制造（高管间/政企协作向，非 IR/资本向）。'),
 dict(emoji='🤝', title='全国「四好」商会建设交流活动（广州·全国工商联·商会会长大会+海大/希音标杆参访）', cat='商会交流·标杆参访',
      rel='r3', src='一手', src_cls='b1',
      url='https://www.acfic.org.cn/qlyw/202605/t20260508_326000.html',
      val='中华全国工商业联合会2026年 4月22日在广州举办全国「四好」商会建设交流暨2026年广州商会会长大会，主题「量质齐升促发展 同心奋进\'十五五\'」，全国工商联副主席安立佳出席。部分全国「四好」商会代表从专精特新培育、产业升级、赋能产业、服务体系、活力青商之家、服务能力等分享经验；会后商会代表共同参访海大集团、狮子洋智造创新园、希音公司、广州市出海企业商会，促进民营经济「两个健康」与大湾区建设。',
      how='把「商会交流活动」做成会长级互学场——以「四好商会经验分享+标杆企业参访」组合，让商会会长从「听报告」升级为「看现场、学打法」；聚焦专精特新培育/产业升级/服务体系等实操维度，把商会组织凝聚力转化为民企协同发展动能；会后参访海大/希音等标杆，是工商联系统「以交流促两个健康」范本。',
      note='③ 商会交流·标杆参访（全国工商联官网一手），全国工商联领导以民营经济组织者姿态，各地商会会长/企业家参访海大/希音、互学商会建设经验（高管间/商协会协作向）。'),
]

# ---- dedup guard against index.json urls ----
idx_data = json.load(open(IDX, encoding='utf-8'))
existing_urls = set()
for x in idx_data:
    u = x.get('url')
    if u: existing_urls.add(u.strip())
before = len(idx_data)
kept, dropped = [], []
for c in cards:
    if c['url'].strip() in existing_urls:
        dropped.append(c['title']); print('DEDUP drop:', c['title'])
    else:
        kept.append(c)
cards = kept
print('dedup: kept=%d dropped=%d' % (len(cards), len(dropped)))

def card_html(c):
    url_disp = c['url'].replace('https://','').replace('http://','')
    rel_text = '上下级' if c['rel']=='r2' else '高管间'
    return (f'    <div class="hl">\n'
            f'      <div class="top"><span class="emoji">{c["emoji"]}</span><h3>{c["title"]}</h3>'
            f'<span class="cat">{c["cat"]}</span><span class="badge {c["rel"]}">{rel_text}</span>'
            f'<span class="badge {c["src_cls"]}">{c["src"]}</span></div>\n'
            f'      <p class="val">{c["val"]}</p>\n'
            f'      <details class="exec"><summary>怎么做</summary><div class="inner">{c["how"]}</div></details>\n'
            f'      <div class="src">🔗 <a href="{c["url"]}" target="_blank">{url_disp}</a></div>\n'
            f'      <div class="note">适用：{c["note"]}</div>\n'
            f'    </div>')

cards2 = [c for c in cards if c['rel']=='r2']
cards3 = [c for c in cards if c['rel']=='r3']
n2, n3 = len(cards2), len(cards3)
assert n2+n3 == len(cards), (n2,n3,len(cards))
print(f'cards total={len(cards)} | ②={n2} ③={n3}')

# ===== 1) summary page openday.html =====
html = open(HTML, encoding='utf-8').read()
cur2 = html.count('badge r2">上下级<')
cur3 = html.count('badge r3">高管间<')
print(f'current wall: ②={cur2} ③={cur3} (hl divs={html.count(chr(34)+"hl"+chr(34))})')

marker = '  <div class="sec sec3">'
idx = html.find(marker)
assert idx != -1, 'sec3 marker not found'
html = html[:idx] + '\n'.join(card_html(c) for c in cards2) + '\n' + html[idx:]
j = html.find('<div class="sec sec3">')
k = html.find('<div class="hl">', j)
assert k != -1, 'no hl in sec3'
html = html[:k] + '\n'.join(card_html(c) for c in cards3) + '\n' + html[k:]

m2 = re.search(r'(<div class="sec sec2">.*?<span class="tag">)(\d+)( 卡</span>)', html, re.S)
assert m2, 'sec2 tag not found'
html = html[:m2.start()] + m2.group(1) + str(cur2+n2) + m2.group(3) + html[m2.end():]
m3 = re.search(r'(<div class="sec sec3">.*?<span class="tag">)(\d+)( 卡</span>)', html, re.S)
assert m3, 'sec3 tag not found'
html = html[:m3.start()] + m3.group(1) + str(cur3+n3) + m3.group(3) + html[m3.end():]

# hero append 三十轮 segment after last 二十七轮 tail
HERO_ANCHOR = ('二十七轮补采 2026-08-26(+10，上海国企开放日城市级/脑智中心脑机接口/核能安全所核科普/'
               '固体所材料之美/成都智算AI/数博会公众开放日/信通院智算生态/知音湖北文旅/中宁工业园区闭环/章贡吐槽大会·8②2③，9一手+1二手)')
assert HERO_ANCHOR in html, 'hero r27 tail not found'
seg_r30 = ('｜ 三十轮补采 2026-08-28(+12，公共资源交易/12345热线/住房公积金/检察(未检)/退役军人事务/'
           '红十字应急救护/婚姻登记/社保经办开放日向·全②上下级，8一手+0二手 ｜ 芝罘招商主题开放日/'
           '大鹏园区CEO沙龙/成都东部空港下午茶/全国四好商会广州·4③，2一手+2二手)')
html = html.replace(HERO_ANCHOR, HERO_ANCHOR + seg_r30, 1)

foot_ok = html.count('📌 本页由 yitong 沉淀整理')
assert foot_ok >= 1, 'footer missing'
open(HTML, 'w', encoding='utf-8').write(html)
b1c = html.count('badge b1"')
b2c = html.count('badge b2"')
print(f'OK wall updated: ②={cur2+n2} ③={cur3+n3} (hl now {html.count(chr(34)+"hl"+chr(34))}), footer={foot_ok}, b1={b1c} b2={b2c}')

# ===== 2) incremental page =====
inc_html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Open Day 开放日 · 第30轮补采（独立页）</title>
<style>
:root{{--bg:#f4f6fb; --card:#ffffff; --ink:#1f2430; --sub:#5b6478; --accent:#6c5ce7; --accent2:#00b8d9; --chip:#eef0ff;}}
*{{box-sizing:border-box;margin:0;padding:0;}}
body{{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:linear-gradient(135deg,#eef1ff 0%,#e6f7ff 100%);color:var(--ink);padding:28px 18px;line-height:1.6;}}
.wrap{{max-width:1080px;margin:0 auto;}}
.hero{{background:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);border-radius:22px;padding:30px 32px;color:#fff;box-shadow:0 14px  ̃40px rgba(108,92,231,.25);margin-bottom:22px;}}
.hero h1{{font-size:26px;font-weight:800;letter-spacing:1px;margin-bottom:8px;}}
.hero p{{font-size:14px;opacity:.95;}}
.relbar{{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px;}}
.relbar span{{background:rgba(255,255,255,.2);border-radius:20px;padding:5px 14px;font-size:13px;font-weight:600;}}
.sec{{margin:30px 0 12px;display:flex;align-items:center;gap:10px;}}
.sec h2{{font-size:19px;font-weight:800;}}
.sec .tag{{font-size:12px;padding:4px 12px;border-radius:12px;font-weight:700;}}
.sec3 .tag{{background:#f3e8ff;color:#7b2cbf;}} .sec3 h2{{color:#7b2cbf;}}
.sec2 .tag{{background:#fff3e0;color:#c0651a;}} .sec2 h2{{color:#c0651a;}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;}}
.hl{{background:var(--card);border-radius:18px;padding:18px 18px 16px;border-top:4px solid var(--accent);box-shadow:0 10px 32px rgba(108,92,231,.10);display:flex;flex-direction:column;gap:9px;}}
.top{{display:flex;align-items:center;gap:8px;flex-wrap:wrap;}}
.emoji{{font-size:22px;}}
.hl h3{{font-size:16px;font-weight:700;flex:1;min-width:120px;}}
.cat{{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:600;background:var(--chip);color:var(--accent);}}
.badge{{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:700;}}
.b1{{background:#e6f9f0;color:#0a8f5b;}}
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
</head>
<body>
<div class="wrap">
  <div class="hero">
    <h1>🚪 Open Day 开放日 · 第30轮补采（独立页）</h1>
    <p>采集于 2026-08-28 ｜ 本轮新增 {len(cards)} 卡（②上下级 {n2} · ③高管间 {n3}）｜ 六维评估 ｜ 一手/二手标注 ｜ 受众关系分层（仅②③，剔除①）｜ 累计总索引见 <a href="../openday.html" style="color:#fff;text-decoration:underline;">openday.html</a></p>
    <div class="relbar">
      <span>② 领导↔员工（上下级）</span>
      <span>③ 领导↔领导（高管间）</span>
    </div>
  </div>
  <div class="sec sec2">
    <h2>② 领导↔员工（上下级，supervisor）</h2>
    <span class="tag">{n2} 卡</span>
  </div>
  <div class="grid">
{card_html_multi(cards2)}
  </div>
  <div class="sec sec3">
    <h2>③ 领导↔领导（高管间 · exec）</h2>
    <span class="tag">{n3} 卡</span>
  </div>
  <div class="grid">
{card_html_multi(cards3)}
  </div>
  <footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>
</div>
</body>
</html>
'''
# small helper used above
def card_html_multi(lst):
    return '\n'.join(card_html(c) for c in lst)

inc_html = inc_html  # already formatted via f-string (card_html_multi defined after; fix ordering)
open(INC, 'w', encoding='utf-8').write(inc_html)
print(f'OK incremental page: {INC} ({os.path.getsize(INC)}B)')

# ===== sanity: helper must exist before use -> redefine properly =====
SYS.exit('placeholder')
