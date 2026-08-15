# -*- coding: utf-8 -*-
# 员工大会 第十五轮补采：向 index.json 追加 12 条 staff-meeting 条目
import json, re, os

BASE = os.path.dirname(os.path.abspath(__file__))
IDX = os.path.join(BASE, 'index.json')

def nk(t):
    # 归一化 key：去空白、去首尾引号类标点
    t = t.strip()
    for ch in ['【','】','「','」','『','』','《','》','“','”','"','“','”','·','（','）','(' ,')']:
        t = t.replace(ch, '')
    return t

NEW = [
  dict(title="中航集团（国航）2026年中工作会（国航官网一手）",
       url="https://www.airchinagroup.com/cnah/xwzx/zhxw/07/701262.shtml",
       sourceType="primary", relation="supervisor,exec",
       summary="央企官网一手：7月24日中航集团2026年中工作会，董事长作《坚定信心 接续奋斗》总结讲话、总经理作年中报告，视频形式+40个分会场。系统提出建设世界一流企业「十个一流」，单列「一流的文化引领」（使命驱动/精神传承/以人为本/和合协同）。",
       source="国航官网"),
  dict(title="兵器工业集团2026年中工作会（集团官网一手）",
       url="http://www.norincogroup.com.cn/art/2026/7/24/art_84_573850.html",
       sourceType="primary", relation="supervisor,exec",
       summary="军工央企官网一手：7月23日兵器工业集团2026年中工作会，董事长作工作报告、总经理主持并作会议总结。树立「好于行业/竞争对手/历史同期」导向，推进「136」发展战略六项目标，将「文化品牌卓越」纳入战略目标清单。",
       source="兵器工业集团官网"),
  dict(title="中国中化2026年中工作会（能源新闻网权威报道）",
       url="https://cpnn.com.cn/news/nyqy/202607/t20260729_1905184.html",
       sourceType="secondary", relation="supervisor,exec",
       summary="权威媒体逐字报道：中国中化7月27-28日年中工作会，董事长作《把方向、管大局、保落实》讲话，用「三个优于」先稳预期，从十个方面部署战略，以「十五五」规划为指引推动科技创新与产业创新融合。",
       source="中国电力新闻网"),
  dict(title="小米核心干部千人大会：价值观「真诚 热爱」八条诠释",
       url="https://web.vip.miui.com/page/info/mio/mio/detail?postId=42451434",
       sourceType="primary", relation="supervisor",
       summary="一手样本：2023年9月小米千人核心干部大会，发布新十年战略并对价值观「真诚 热爱」作八条诠释（信任第一=坦诚沟通摊桌上说、共创共识=决策后充分沟通why），把价值观落成可执行条目，作为核心干部文化对齐范式。",
       source="小米社区"),
  dict(title="华为心声社区「吐槽大会」与自我批判机制（人民日报案例）",
       url="https://www.peopleapp.com/rmharticle/30020505549",
       sourceType="secondary", relation="supervisor,exec",
       summary="案例：任正非倡导「心声社区」内部匿名吐槽平台（不删帖不追查），高层以身作则公开自我批判（蓝军报告发全员+揽责），配民主生活会+限时督办闭环，用自由批评建立内部信任。",
       source="人民号/企业管理"),
  dict(title="Town Hall 主持人/控场：一致口径·坏消息·敏感问题",
       url="http://www.exec.com/learn/town-hall-meeting",
       sourceType="secondary", relation="supervisor,exec",
       summary="exec.com 主持指南：指定有控场能力的主持人，会前列「最棘手问题+标准应答」；敏感/政治性问题由主持人统一口径 deflect 避免高管即兴踩雷；会后发纪要+录音全员可溯；坏消息场景保持积极、讲清「为什么」、给希望。",
       source="exec.com"),
  dict(title="高效全员会：指定主持人·远程代言人·游戏化参与",
       url="https://dev.predictiveindex.com/blog/the-complete-guide-to-leading-effective-all-hands-meetings",
       sourceType="secondary", relation="supervisor",
       summary="Predictive Index 完整指南：设单一 moderator 控屏控时；为远程团队指派 champion 作「远程声音」；用 Mentimeter/小奖品游戏化提问；多部门负责人轮番上台；会后24h内发书面总结（关键指标+决策+Top问答）。",
       source="Predictive Index"),
  dict(title="全员会讲故事：七元素结构 + 财务透明消除模糊厌恶",
       url="https://tettra.com/article/all-hands-meeting",
       sourceType="secondary", relation="supervisor",
       summary="Tettra 指南：用轻松人性面暖场；以故事的七要素（背景/触发/难题/转折/危机/高潮/结局）讲战略why；主动披露财务健康消除模糊焦虑（人对模糊的厌恶>对风险的厌恶）；未来计划放结尾造期待；全程留Q&A+录制回放。",
       source="Tettra"),
  dict(title="Town Hall 四幕叙事框架（产品高管版）",
       url="https://www.productboard.com/product-management-prompts-library/product-town-hall-narrative/",
       sourceType="secondary", relation="exec",
       summary="Productboard 叙事结构：定调→第一幕 Reality Check（诚实说在哪/什么难）→第二幕 Strategy（讲reasoning与trade-off，非念路线图）→第三幕 Team Story（点名具体贡献）→第四幕 The Ask；Q&A 主动抛最难问题并诚实答。",
       source="Productboard"),
  dict(title="全员会 PPT 模板 +「不装问题」技术 + 会后24h总结",
       url="https://findskills.co/skills/internal-narrative",
       sourceType="secondary", relation="supervisor",
       summary="findskills 模板：月度全员会6页结构（状态/进展/骄傲/没做成/接下来/Q&A）；末尾留「no-BS questions」匿名收最难问题当众诚实答，比精美PPT更建信任；CEO答所问、不知就承诺时限去查；会后24h书面总结回扣承诺。",
       source="findskills"),
  dict(title="好的全员会做对的7件事（LinkedIn 框架）",
       url="https://www.linkedin.com/posts/amy-l-g_all-hands-comes-from-the-old-maritime-call-activity-7472981494429499394-9Ewk",
       sourceType="secondary", relation="supervisor",
       summary="Amy Gibson 高赞框架：全员会=信任建设而非信息宣读——锚定现场/亮记分牌/把外部客户请进来/点名一个赢/说出难事/一起向前看/开放提问；难事诚实两分钟比精美更新更可信；人记得的是连接感而非每个指标。",
       source="LinkedIn"),
  dict(title="全球 Town Hall 多时区同步策略（行业协会样本）",
       url="https://imasons.org/activity/imasons-global-town-hall",
       sourceType="secondary", relation="supervisor,exec",
       summary="iMasons 首次全球 Town Hall 给出「全球统一 start times」表（各时区本地时间一目了然），无法同刻到场的用录制+同声传译补课，议程全球一致（战略/财务/参与方式），让分散团队共享同一叙事。",
       source="iMasons"),
]

d = json.load(open(IDX, encoding='utf-8'))
existing_urls = {x.get('url') for x in d}
existing_nk = {x.get('normKey') for x in d}
added = []
skipped = []
for e in NEW:
    if e['url'] in existing_urls:
        skipped.append(e['url']); continue
    entry = dict(e)
    entry['normKey'] = nk(e['title'])
    entry['topic'] = 'staff-meeting'
    d.append(entry)
    added.append(e['title'])
    existing_urls.add(e['url'])

json.dump(d, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('ADDED:', len(added))
for t in added: print('  +', t)
print('SKIPPED:', len(skipped))
sm = [x for x in d if x.get('topic')=='staff-meeting']
print('staff-meeting total now:', len(sm))
print('index.json total now:', len(d))
