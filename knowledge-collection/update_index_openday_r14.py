# -*- coding: utf-8 -*-
"""Open Day 十四轮补采：向 index.json 追加 14 条 topic=openday 条目。"""
import json, os

IDX = 'index.json'

entries = [
    ("息烽公安「党建引领·警务实战」警营开放日",
     "https://www.xifeng.gov.cn/xwdt/bmdt/202606/t20260605_90486926.html", "primary", "supervisor",
     "息烽公安以「党建引领·新时代警务实战技能的跃升」为主题办警营开放日，群众代表走进警营看党建文化阵地、上手体验警用装备、看纪实短片，最后意见征集座谈并逐条登记吸纳建议。常态化开门纳谏、问计于民。"),
    ("云浮公安警营开放日暨「6·26」国际禁毒日主题宣传",
     "https://www.nfnews.com/content/j3kjYNMQyA.html", "secondary", "supervisor",
     "云浮公安在实战训练中心办警营开放日+国际禁毒日宣传，特警演练、数字警务情景展演、警用无人机、禁毒有奖互动（针对奶茶/糖果等新型伪装毒品科普）、搜毒警犬。硬核展演+互动普法的警民范式。"),
    ("青岛能源集团 2025「企业开放日」（燃气/供热·智慧能源）",
     "http://gzw.qingdao.gov.cn/xwzx/qydt/202508/t20250808_9991858.shtml", "primary", "supervisor",
     "青岛能源集团「强基聚力 创效惠民」企业开放日（中心会场+21分会场），首用「线上报名+线下邀请」，389名社区代表/社会监督员/媒体参与；劳模讲智慧供热平台+燃气锅炉工艺+海底管线安全，六大咨询台听用户声音，收集建议51条。国资委官网一手。"),
    ("十堰中燃「燃气安全开放日」（从保供到入户全流程）",
     "https://syiptv.com/article/show/329413", "secondary", "supervisor",
     "十堰中燃借安全生产月邀市民进调度中心/实操基地，探访燃气「从场站到家中」全流程：调度中心开放、管理层面对面沙龙、表具/故障代码手把手教学、应急器材体验。限定名额+公众号报名。"),
    ("抚州南城机场航空科普开放日（五一·实景体验）",
     "https://i.ifeng.com/c/8sk35lBJNyC", "secondary", "supervisor",
     "江航南城实训基地（抚州南城机场）五一面向市民办航空科普开放日，四大体验=机场运行观摩/科普讲解/职业文化解读/趣味互动，青少年进驾驶舱打卡、操作模拟机。场景即教材的公众科普。"),
    ("浦发银行「走进外滩12号」上海国企开放日",
     "https://so.html5.qq.com/page/real/search_news?docid=70000021_8746a7eba3298752", "secondary", "supervisor",
     "2026上海国企开放日「走进外滩12号」在浦发银行举办，市民参观百年建筑、体验普惠金融服务；IP文创+纪念印章+趣味金融游戏（桌上冰壶融入消保）；脱口秀开放麦讲反诈/非法借贷风险。历史IP+趣味消保的公众沟通。"),
    ("兴业银行「权益守护开放日」（网点消保课堂）",
     "https://www.jsw.com.cn/2026/0618/1961315.shtml", "secondary", "supervisor",
     "兴业银行全国网点同步办「权益守护开放日」：布展+咨询台+微课堂讲适老/反诈/维权，联合多方把教育阵地搬进社区/园区/校园/乡村「五进入」精准触达一老一少一新。消保宣教非投资者关系向。"),
    ("广饶农商银行「小小银行家」网点开放日（青少年财商）",
     "https://www.163.com/dy/article/HJE2VLIP0514R9KU.html", "secondary", "supervisor",
     "广饶农商银行邀小记者团及家长进营业部办网点开放日：看宣传片、体验自助设备、开户理财、学防伪人民币鉴别、提问抢答。真实场景+游戏化学习的青少年财商科普。"),
    ("青岛 2026「农业科技开放日」（政府开放月·农科院）",
     "https://www.qingdao.gov.cn/zwgk/xxgk/nync/ywfl/kjtg/202605/t20260529_10621652.shtml", "primary", "supervisor",
     "青岛市农科院办2026农业科技开放日（融合政府开放月），邀代表进科研一线：田间观摩+实验室探秘+技术讲解+互动体验，青砧苹果砧木/青研紫麦/智能温室新品种亮相，质检实验室开放。市政府一手。"),
    ("福州港开放日·江阴港区专场（智慧绿色港口）",
     "https://fzftz.fuzhou.gov.cn/zwgk/qydt/202507/t20250714_5047251.htm", "primary", "supervisor",
     "第2个福州港开放日江阴港区专场（中国航海日），公众/师生/媒体进集装箱作业现场乘车体验智慧港口、数智中心看智慧绿色平台动态演示、自动化设备现场操作。自贸区一手。"),
    ("天津港 2025 企业开放日（港城同心·千名市民进港区）",
     "https://www.ftutj.cn/tjgrbpaper/tjgrb/2025-10/20/content_99226364.html", "secondary", "supervisor",
     "天津港重开港73周年办2025企业开放日，邀千名市民进港区：智慧零碳码头、滚装码头国产车出口、东疆湾沙滩、国贸展区、津港印象5D影片，三条路线覆盖生产-生态-民生。港口报二手。"),
    ("阳谷县「政法机关开放日」（法院/检察/公安/司法全景）",
     "http://zfw.liaocheng.gov.cn/channel_t_283_16517/doc_674d0be744ac0bf0ea602dfc.html", "primary", "supervisor",
     "阳谷县政法系统办开放日，邀市民/代表/媒体/青少年进政法机关：法院模拟庭审、检察院快检实验室、公安警营开放日、司法局社区矫正中心。法检公司四机关联动+分群定制。政法委一手。"),
    ("光明区文化馆「文化和自然遗产日」非遗开放体验",
     "https://wtl.sz.gov.cn/ztzl_78228/zdly/sswhg/gzdt_81834/content/post_12845667.html", "primary", "supervisor",
     "光明区文化馆2026文化和自然遗产日非遗系列活动（7会场近3000人次）：吃用玩穿四维度体验、手作DIY、青少年醒狮/汉服、社区麒麟文化节、研学工坊惠民体验。深圳文旅一手。"),
    ("福州港开放日·宁德(湾坞)专场（政企研港产城融合沙龙）",
     "https://www.toutiao.com/article/7664607603448480265/", "secondary", "exec",
     "第3个福州港开放日宁德(湾坞)专场，福州港口发展中心+福安市政府主办，政企研多方同台论港产城融合路径，会前参观青拓集团展厅。高管间（exec）政企研对话范式，非投资者关系向。"),
]

d = json.load(open(IDX, encoding='utf-8'))
before = len(d)
before_topic = sum(1 for x in d if x.get('topic') == 'openday')
for title, url, st, rel, summ in entries:
    d.append({
        "title": title,
        "normKey": title,
        "url": url,
        "sourceType": st,
        "relation": rel,
        "summary": summ,
        "topic": "openday",
        "source": "web",
    })
after = len(d)
after_topic = sum(1 for x in d if x.get('topic') == 'openday')
json.dump(d, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'index.json: {before} -> {after} (+{after-before})')
print(f'openday topic: {before_topic} -> {after_topic} (+{after_topic-before_topic})')
