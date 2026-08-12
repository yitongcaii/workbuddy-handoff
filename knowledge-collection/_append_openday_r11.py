# -*- coding: utf-8 -*-
import json, os

base = os.path.join(os.path.dirname(__file__))
idx_path = os.path.join(base, 'index.json')

with open(idx_path, encoding='utf-8') as f:
    data = json.load(f)

before = len(data)

entries = [
    {
        "title": "毕节环保设施向公众开放日（医疗废物/垃圾焚烧/污水/监测）",
        "normKey": "毕节环保设施向公众开放日（医疗废物/垃圾焚烧/污水/监测）",
        "url": "https://www.bijie.gov.cn/bm/bjssthjj/dt/bmdt/202603/t20260330_89921013.html",
        "sourceType": "primary",
        "relation": "supervisor",
        "summary": "毕节市生态环境局联合七星关分局在学雷锋志愿服务月开展「环保设施向公众开放日」，邀市东街道居民与贵州工程应用技术学院学生分批走进医疗废物处置中心、垃圾焚烧发电厂、生态环境监测中心、垃圾填埋场、第一污水处理厂，沉浸式了解城市生态治理；「居民+学生」双专场、「实地参观+现场讲解+互动答疑」形式，让公众了解环保设施运行原理与城市生态治理成效，提升环保参与感与责任感。",
        "topic": "openday",
        "source": "bijie.gov.cn"
    },
    {
        "title": "漳州环保设施向公众开放日（多县区污水/再生能源/监测站）",
        "normKey": "漳州环保设施向公众开放日（多县区污水/再生能源/监测站）",
        "url": "https://www.zhangzhou.gov.cn/cms/html/zzsrmzfbgsgfxwjk/2026-06-12/1502162222.html",
        "sourceType": "primary",
        "relation": "supervisor",
        "summary": "漳州六五环境日期间有序开展环保设施向公众开放：芗城组织师生走进空气自动监测站科普PM2.5/臭氧；龙文组织职校98名师生分两批进东墩污水处理厂看「由浊变清」全流程；龙海组织居民走进再生能源公司看垃圾「变废为电」；长泰组织24家重点涉水企业代表进西区污水厂强化主体责任；漳浦组织师生进圣元环保电力。多县区同步、分众设计。",
        "topic": "openday",
        "source": "zhangzhou.gov.cn"
    },
    {
        "title": "检察开放日制度范式（2025全国7500余场/30.5万人/四级联动）",
        "normKey": "检察开放日制度范式（2025全国7500余场/30.5万人/四级联动）",
        "url": "https://www.spp.gov.cn/zdgz/202601/t20260129_717121.shtml",
        "sourceType": "primary",
        "relation": "supervisor,exec",
        "summary": "最高检披露：2025年全国检察机关共举办7500余场检察开放日、30.5万人参加；自2010年办「深入推进检务公开」检察开放日以来15年已办49场，2025年围绕「民法典实施五周年」「未成年人综合司法保护」「刑罚执行监督」主题以四级联动方式组织3次；各地结合实际自主开展形式多样开放日，让「纸上的法律」变「鲜活普法教材」，类案公开提示身边犯罪「陷阱」。",
        "topic": "openday",
        "source": "spp.gov.cn"
    },
    {
        "title": "「检爱四十载·携手向未来」全国四级检察机关检察开放日（未成年人检察40周年）",
        "normKey": "「检爱四十载·携手向未来」全国四级检察机关检察开放日（未成年人检察40周年）",
        "url": "https://www.spp.gov.cn//zdgz/202606/t20260628_730673.shtml",
        "sourceType": "primary",
        "relation": "supervisor",
        "summary": "2026年「六一」前后，最高检统一部署、全国3000多个检察院同步开展「检爱四十载·携手向未来」检察开放日：北京四中/六十五中近50名中学生走进最高检第50次开放日；兵团/青海/陕西等地检察院让学生演法治情景剧、聘「小小法治宣传员」、成立「国门小卫士」普法队，从「照本宣科」走向「心灵共振」的沉浸式法治之旅。",
        "topic": "openday",
        "source": "spp.gov.cn"
    },
    {
        "title": "荆州区「政法开放日·平安零距离」（法院+检察+公安+司法+综治联合）",
        "normKey": "荆州区「政法开放日·平安零距离」（法院+检察+公安+司法+综治联合）",
        "url": "http://www.jingzhouqu.gov.cn/xwzx/jzqx/202512/t20251206_1056127.shtml",
        "sourceType": "primary",
        "relation": "supervisor",
        "summary": "荆州区委政法委联合区法院/检察院/公安分局/司法局举办「政法开放日·平安零距离」，30名党代表/人大代表/政协委员/群众代表沉浸走访：派出所看接处警+快反演练+智慧巡防；司法所看人民调解+法律援助；法院体验「一站式」诉讼+要素式诉状+涉企绿色通道；检察院看12309+典型案例；综治中心看速裁法庭+心理咨询。「看得见、听得懂、能评价」搭建政法与群众桥梁。",
        "topic": "openday",
        "source": "jingzhouqu.gov.cn"
    },
    {
        "title": "国网临海「逐光之旅」社会责任开放日（中国品牌日+多元资本核算+利益相关方对话）",
        "normKey": "国网临海「逐光之旅」社会责任开放日（中国品牌日+多元资本核算+利益相关方对话）",
        "url": "https://cs.zjol.com.cn/jms/202505/t20250519_31002196.shtml",
        "sourceType": "secondary",
        "relation": "supervisor",
        "summary": "国网临海市供电公司以「与山海共生 与能源永续」为主题办2025中国品牌日暨「逐光之旅」社会责任开放日：介绍「耀明」电力品牌与「逐光·bright」社会责任可持续发展品牌，展示清洁能源消纳/智慧电网/公益实践；发布多元资本核算报告（经济/社会/环境多维价值）；利益相关方沟通会上企业代表/媒体/社会责任专家围绕「能源永续与社会责任」建言；实地参观企业文化展厅和汇丰变感受智能电网。",
        "topic": "openday",
        "source": "zjol.com.cn"
    },
    {
        "title": "韶关供电局2025国企开放日（客户代表发言+青年员工说唱+变电站探访）",
        "normKey": "韶关供电局2025国企开放日（客户代表发言+青年员工说唱+变电站探访）",
        "url": "https://www.nfnews.com/content/mom4NpjW6V.html",
        "sourceType": "secondary",
        "relation": "supervisor",
        "summary": "韶关供电局2025国企开放日：中国移动韶关分公司副总经理作为客户代表发言，感谢供电保障（基站/数据中心/云鹏变电站）；青年员工以「青春赋能芯时代」说唱展现电网人创新风貌；启动仪式用节能环保「摸屏启动」由嘉宾点亮屏幕；技术人员带队深入变电站设备区讲解关键设备原理/智能巡检/安全保障，嘉宾近距离感受现代化电网科技含量。",
        "topic": "openday",
        "source": "nfnews.com"
    },
    {
        "title": "山东消防队站开放日（济南训练基地·近2万市民沉浸体验）",
        "normKey": "山东消防队站开放日（济南训练基地·近2万市民沉浸体验）",
        "url": "https://sd.people.com.cn/BIG5/n2/2025/1112/c397967-41409385.html",
        "sourceType": "secondary",
        "relation": "supervisor",
        "summary": "2025山东消防队站开放日活动在济南消防救援支队训练基地举办，近2万名市民/儿童开启「触摸消防·学习消防·体验消防」沉浸式安全之旅：登101米登高平台车/云梯车了解装备作用；消防指战员介绍器材名称功能，搜救犬完成服从/箱体搜救/攀爬科目；市民穿战斗服/持水枪打靶/操作电动剪扩钳夹乒乓球/学结绳；消防科普基地讲报警逃生，心肺复苏模拟演练；消防元素与非遗/地域特色融合，知识融入游戏+文创。",
        "topic": "openday",
        "source": "people.com.cn"
    },
    {
        "title": "贵州轮胎「最美之旅」客户开放日（100位门店客户·灯塔工厂+山水+恳谈）",
        "normKey": "贵州轮胎「最美之旅」客户开放日（100位门店客户·灯塔工厂+山水+恳谈）",
        "url": "https://www.gztyre.com/news/news-detail-10060.htm",
        "sourceType": "primary",
        "relation": "supervisor",
        "summary": "贵州轮胎2025年度「最美之旅」：全国100位终端门店客户聚贵阳，5天4夜深度体验——首站深入三期智能工厂看智能分拣/无人仓储/在线追溯（中国轮胎行业首家「灯塔工厂」），体会「中国智造」速度；合作伙伴恳谈会分享渠道通门店APP、探讨新媒体流量赋能；随后穿越织金洞/黄果树/小七孔山水，以「持久共赢」隐喻合作如自然奇迹需时间沉淀，定格对未来的憧憬。",
        "topic": "openday",
        "source": "gztyre.com"
    },
    {
        "title": "国药集团2026「解码国药智造」媒体开放日（中国品牌日·上海）",
        "normKey": "国药集团2026「解码国药智造」媒体开放日（中国品牌日·上海）",
        "url": "https://www.shyndec.com/shxdzy/gsxwlb/2026/5/I1506344524509609984.html",
        "sourceType": "primary",
        "relation": "exec",
        "summary": "国药集团「解码国药智造」2026媒体开放日（官网）：借「中国品牌日」契机邀20余家媒体走进上海，实地探访国药医工总院（新药研发/中试放大/AI合成生物）、国药现代浦东制造中心（制剂车间/QC实验室/渗透泵控释）、中国生物上海所（流感疫苗/抗体研发产业化）；媒体座谈会围绕疫苗接种/AI赋能新药研发/海外拓展深入交流；同步办「国药匠心·品牌筑梦」品牌开放+上生新所沉浸式品牌展馆对公众开放。",
        "topic": "openday",
        "source": "shyndec.com"
    },
    {
        "title": "东安动力媒体开放日（新能源动力总成产线+技术脱口秀+双转子点火）",
        "normKey": "东安动力媒体开放日（新能源动力总成产线+技术脱口秀+双转子点火）",
        "url": "https://news.10jqka.com.cn/20260617/c677546271.shtml",
        "sourceType": "secondary",
        "relation": "exec",
        "summary": "东安动力（600178）媒体开放日（同花顺报道）：邀人民网/新华社/科技日报等中央及地方主流媒体走进企业，开放新能源动力总成数字化智能产线，生产线负责人任「探秘官」拆解高精度加工/智能装配/在线检测；主题分享改「技术脱口秀」形式，管理研发生产市场负责人聊混动节能/智能制造/社会责任；现场举行双转子增压发动机R10TE点火仪式填补大功率转子发动机空白；资深工程师/一线工匠/青年骨干微访谈讲匠心。",
        "topic": "openday",
        "source": "10jqka.com.cn"
    },
    {
        "title": "北玻2026「六零绿色建材日」公众开放日（媒体+行业专家·花园式园区）",
        "normKey": "北玻2026「六零绿色建材日」公众开放日（媒体+行业专家·花园式园区）",
        "url": "https://glass.northglass.com/newsInfo/872.html",
        "sourceType": "primary",
        "relation": "exec",
        "summary": "北玻股份2026「六零绿色建材日」公众开放日（官网）：由《中国建材》杂志协调20余家中央及地方媒体记者，与中国建材联合会/国检集团/洛阳玻璃行业协会专家齐聚北玻高端装备产业园；参观510亩花园式园区（绿化12万㎡，颠覆装备制造工厂印象）、三元流风机检测中心（CNAS国家认可实验室）、玻璃深加工自动化连线；董事长率团队接待，各业务负责人系统介绍核心产品与「双碳」战略契合点，围绕创新与绿色战略与媒体深度交流。",
        "topic": "openday",
        "source": "northglass.com"
    },
]

# dedup by url
existing_urls = {e.get('url') for e in data}
added = 0
for e in entries:
    if e['url'] in existing_urls:
        print('SKIP dup:', e['url'])
        continue
    data.append(e)
    existing_urls.add(e['url'])
    added += 1

with open(idx_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'before={before} after={len(data)} added={added}')
