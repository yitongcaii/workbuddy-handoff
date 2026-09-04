# -*- coding: utf-8 -*-
import json, os, datetime

BASE = os.path.dirname(os.path.abspath(__file__))
TOPIC = "offsite"
SLUG = "offsite"
DATE = "20260905"
ROUND = "三十五轮"
RUN_LABEL = "三十五轮补采 +10"
VAULT_NOTE = "Offsite-团建务虚-知识卡汇总"

# ---- 10 cards (only supervisor / exec) ----
cards = [
 # ③ 高管间
 dict(emoji="💭", title="务虚会「裸心会」式深度研讨（抛开职级·聚焦使命愿景·思维自由碰撞）", cat="深度研讨",
      rel="exec", rel_text="高管间", src="二手", badge_r="r3", badge_b="b2", score=4,
      url="https://tianqinzixunjituan.com/a/xinwen/1528.html",
      val="天勤咨询集团2026半年度经营分析暨战略务虚会的一手实践：下半场直接以2025年务虚会敲定的核心改善方向为刚性基线，逐条验收落地进度、直面未完成问题；在「轻松但不失专业」的氛围中，大家抛开职级，聚焦集团使命、愿景、核心价值观展开「裸心会」式研讨——「我们的核心壁垒3年后是否依然坚挺？」「如何让年轻合伙人在炮火中快速成长？」没有标准答案，只有思维自由碰撞。这套设计补了高管务虚会最常见的「层级压制」翻车：一把手在场时副职与年轻高管不敢说真问题。裸心会以「抛开职级」的明示规则+使命愿景级问题（非当日KPI）打开心理安全闸门，让战略盲区被看见。区别于平级破冰/团建娱乐（那是平级消遣），裸心会是在高管层内部以「去层级化深度对话」撬动战略共识。",
      inner="务虚会下半场设「裸心会」专属时段:明示「抛开职级、只对使命愿景负责」规则;问题升到使命愿景层(核心壁垒/年轻合伙人成长/专业护城河)而非当日KPI;一把手先示弱抛自己的困惑而非定调;年轻高管与副职轮流主导议题;产出记「共识」不记「指示」;现场不拍照不外传,保护坦诚。",
      note="适用：③高管间（领导班子/经管会）。二手源=咨询集团官方回顾。补「务虚不越权/保密」之外「高管层内部去层级化深度对话」这一被忽视的共识生成机制；区别于平级破冰/团建娱乐，本卡是「高管裸心会」这一战略共识场景。"),
 dict(emoji="🔄", title="务虚会成果「部署-跟踪-反馈-销号」全闭环（目标量化/问题导向/跟踪反馈/纳入月度考核）", cat="闭环管理",
      rel="exec", rel_text="高管间", src="一手", badge_r="r3", badge_b="b1", score=4,
      url="https://www.shx.chinanews.com.cn/news/2026/0306/109738.html",
      val="延长气田采气三厂（中新网陕西一手）把务虚会成果转化为「部署-跟踪-反馈-销号」全闭环：以63项提升措施为抓手、109个任务节点为支撑，聚焦精细勘探开发等四大主线，明晰各单位各岗位核心职责、工作标准、推进要求；成立专项领导小组，构建「领导小组统筹、科室大队落实、各岗位协同」联动机制；实行任务清单化管理、常态化督导检查，落实情况纳入月度绩效考核，建立「部署-跟踪-反馈-销号」全闭环，确保推进不脱节、落实不打折扣。直击务虚会最大通病——开完一纸纪要就凉。硬约束是「三挂钩」：任务清单化（可查）+常态化督导（可盯）+纳入月度绩效（可罚），把务虚成果从「金点子」变成「硬成效」。",
      inner="务虚会结束即出《成果任务落实方案》;措施拆为「提升措施+任务节点」两级;每任务定责任单位/岗位/标准/时限;成立专项领导小组统筹;清单化管理+常态化督导;落实情况纳月度绩效考核;建「部署-跟踪-反馈-销号」四步闭环,完成贴红标销号。",
      note="适用：③高管间（领导班子+职能负责人）。一手源=中新网陕西官方报道。补「务虚会要开得务实」原则之外「成果落地四步闭环+绩效挂钩」这一执行骨架；区别于华为DSTE（已采），本卡是「国企基层厂级务虚会闭环」的轻量可抄版。"),
 dict(emoji="📌", title="务虚会要开得「务实」（目标导向具体化/问题导向实战化/成果转化常态化）", cat="务实方法论",
      rel="exec", rel_text="高管间", src="一手", badge_r="r3", badge_b="b1", score=4,
      url="https://big5.china.com.cn/gate/big5/iot.china.com.cn/content/2024-02/07/content_42696193.html",
      val="中国网《「务虚会」要开得「务实」》提炼三条硬规矩：①目标导向的务实——明确发展目标、确立符合实际顺趋势的战略定位，结合实际情况分解目标，每项战略目标都有具体量化指标和实现路径，避免空洞口号式表述；②问题导向的务实——讨论发展规划紧紧围绕存在的问题挑战展开，对症下药提针对性强操作性强的方案，不避不谈、不纸上谈兵，深挖根源求破解之道；③成果转化的务实——会后务必将共识决策转化为具体工作部署实施方案，明确责任人和时间表，建有效跟踪反馈机制定期检查督促。核心方法论：「以虚率实、虚实结合」，每次务虚都为下一步务实行动提供清晰方向与有力支撑。这是务虚会设计的「元原则」，可写进任何务虚会制度总则。",
      inner="开务虚会前先立三条规矩:目标具体化(每战略目标配量化指标+实现路径,禁口号);问题实战化(直面真问题对症下药,禁避重就轻);成果转化常态化(会后出实施方案+责任人+时间表+跟踪反馈机制);全程「以虚率实」,每次务虚必须产出下一步可执行的务实部署。",
      note="适用：③高管间。一手源=中国网评论（引《之江新语》「既重务实又善务虚」）。补「务虚制度化四步法」之外「务虚会设计的三条元原则（目标/问题/转化）」，是写务虚会制度的通用总则，非某次具体会议。"),
 dict(emoji="📡", title="务虚会精神一线穿透（数字平台全周期管控+掌中宝宣传手册+任务上墙透明督办）", cat="宣贯穿透",
      rel="exec", rel_text="高管间", src="一手", badge_r="r3", badge_b="b1", score=4,
      url="https://ktgs.sxycpc.com/info/1083/9320.htm",
      val="延长石油气田公司（一手）把集团务虚会精神从「会议」穿透到「一线岗位」的三招：①数字大脑——务虚会重点任务嵌入数字化管理平台，任务从分解、执行、跟踪到考核全周期线上管控，进度条/责任人/时间节点实时跳动；②掌中宝——发放《务虚会工作宣传手册》巴掌折页，简明语言+图表梳理核心要求与厂级重点任务，队里开会学习、班组晨会宣贯当教材，确保每位职工清楚「干什么/为什么/怎么干」；③任务上墙——办公区立「务虚会月度任务清单」墙，任务名/责任领导/落实班组/计划完成时间一目了然，完成贴红标，集体监督转动力。再加「公司下达+自主讨论」双轨（中心自主梳理融合任务清单），让落地有抓手。这是高管务虚会「向上定调、向下穿透」的可迁移宣贯体系。",
      inner="务虚会精神穿透三招:数字平台(任务分解-执行-跟踪-考核全周期线上闭环,进度条实时);掌中宝(巴掌手册简明图表,班组晨会宣贯教材);任务上墙(月度清单墙透明督办,完成贴红标);加「公司下达+自主讨论」双轨让基层有自选动作;层层穿透到岗位而非停留在文件。",
      note="适用：③高管间（领导班子定调→职能/厂队宣贯→一线岗位）。一手源=延长石油气田公司官方稿。补「闭环管理」之外「务虚会精神如何穿透到一线」这一宣贯体系（数字平台+掌中宝+上墙），是高管务虚会向下传导的可抄模板。"),
 dict(emoji="📣", title="高管 offsite 结论层层穿透·C-suite 沟通级联（把决策译成日常执行/多格式重复/自下而上反馈闭环）", cat="结论宣贯",
      rel="exec", rel_text="高管间", src="二手", badge_r="r3", badge_b="b2", score=4,
      url="https://pamelajgreen.com/scaling-communication-as-you-scale-your-organization-a-guide-for-c-suite-leaders",
      val="高管 offsite 最大的浪费之一是：会议室里达成共识，回到公司没人知道变了什么。C-suite 沟通级联的关键纪律：①把战略译成日常执行——训练各级 leader 用自己的话 reinforce 决策同时保持核心信息一致，把抽象战略转成具体 KPI 与 operational goals；②重复不是冗余——团队每天吸收几十条信息，关键信息要多次、多格式（全员会/team meeting/1:1/onboarding deck/内部 dashboard）触达才成真；③自下而上反馈闭环——季度敬业度调研+关键节点匿名洞察环+轮值 skip-level，让 context 上行而非只下行；④谁决策、谁 communicate、谁 cascade 要 codify（写进制度而非靠默契）。这把 offsite 的「产出」从一份纪要变成组织的能力。",
      inner="offsite结论级联四律:①译执行(各级leader用自己话reinforce决策,战略转KPI/operational goals,核心信息一致);②多格式重复(全员会+team meeting+1:1+onboarding+内部dashboard,关键信息多次触达);③自下而上反馈(季度调研+匿名洞察+轮值skip-level,context上行);④codify(谁决策/谁communicate/谁cascade写进制度);检测:问三层「你听到了什么」验证穿透。",
      note="适用：③高管间（经管会/高管团队对外与对下沟通）。二手源=C-suite 沟通顾问。补「务虚会精神一线穿透」西方版（级联系统+重复非冗余+反馈上行），与国企宣贯（数字平台/掌中宝）互为中外印证；非议程/facilitation。"),
 # ② 上下级
 dict(emoji="📝", title="Offsite 供应商合同审查清单（服务范围/付款/取消费/免责/force majeure/争议解决）", cat="合同审查",
      rel="supervisor", rel_text="上下级", src="二手", badge_r="r2", badge_b="b2", score=4,
      url="https://www.sprintlaw.com/articles/retreat-terms-of-service-what-to-review-before-signing",
      val="行政/采购 owner 签 offsite 供应商合同前必查六块（Sprintlaw）：①服务范围——包不包含全部餐饮/住宿/交通/活动/材料？有无隐藏加项；②付款条款——定金/分期/到期日/滞纳金，是否要求全款预付；③取消费与退款——定金可退吗？取消截止与退款比例？能否转让名额；④责任与免责——provider 的受伤/财产/取消责任豁免范围，你接受什么风险；⑤不可抗力（force majeure）——自然灾害/政府限制/疫情能否退或改期；⑥争议解决——仲裁/调解优先？适用哪州法律、哪里起诉。最大坑：不读细则（餐饮/接送不含致意外支出）、假设所有 retreat 规则相同、忽略保险要求（合同可能要求单独活动险）、忽略州法差异。可谈：严格取消政策可谈部分退款或转让。",
      inner="签offsite合同前查六块:①服务范围(餐饮/住宿/交通/活动/材料是否全包,隐藏加项);②付款(定金/分期/滞纳金/是否全款预付);③取消费退款(定金可退?截止与比例?能否转让);④责任免责(受伤/财产/取消豁免范围);⑤force majeure(自然灾害/政府限制/疫情退或改期);⑥争议解决(仲裁优先?适用法/管辖);坑:不读细则/假设同规则/忽略保险要求/忽略州法;严取消可谈部分退款或转让。",
      note="适用：② 公司内部上下级场景（行政/采购 owner 签 offsite 供应商合同）。二手源=法律 SaaS 实务指南。补「场地议价7杠杆/选型评分矩阵」之外「合同签署前六块审查清单」这一签约风控缺口；非场地选型。"),
 dict(emoji="⚡", title="Force Majeure 不可抗力条款谈判要点（列具体事件/不履约免罚/衰减费豁免/书面通知时限）", cat="不可抗力",
      rel="supervisor", rel_text="上下级", src="二手", badge_r="r2", badge_b="b2", score=4,
      url="https://www.ascentlawfirm.com/force-majeure-in-a-contract",
      val="offsite 场地/酒店合同最易被忽略却最致命的条款是 force majeure（Ascent Law Firm）：①列具体事件——法院狭义解释，只覆盖列出及类似事件，须明确列自然灾害/战争/恐袭/罢工/疫病/交通中断致≥25%参会人无法到场；加 catch-all 兜底；②阈值用「inadvisable/commercially impracticable/illegal/impossible」而非仅「impossible」（后者门槛过高，很多「不宜办但仍能办」的情形不保）；③不仅免取消责任，也要免「履约不足」责任（未达最低房/餐饮承诺的衰减费 attrition），否则减量也赔钱；④书面通知时限——出事即书面通知对方并说明原因，留证、先协商再准备法律战。谈判提示：这是最 contentious 的条款之一，别秒接酒店初稿；「不会发生在我们身上」心态已过时（后疫情共识）。",
      inner="force majeure谈判四要点:①列具体事件(自然灾害/战争/恐袭/罢工/疫病/交通中断≥25%缺席)+catch-all兜底,法院只认列出及类似;②阈值用inadvisable/impracticable/illegal而非仅impossible(后者过严);③免「不履约」也要免「履约不足」责任(衰减费attrition,减量也赔钱);④出事即书面通知留证,先协商;别秒接初稿,这是最contested条款。",
      note="适用：② 公司内部上下级场景（行政/法务 owner 审场地合同）。二手源=美国会议法律所。补「供应商合同审查清单」中 force majeure 这一单条的深化谈判要点；非 general 合同。"),
 dict(emoji="🛂", title="国际 Offsite 签证与出入境合规（商务访客签证/母公司邀请函/医疗险/90天上限/不本地就业）", cat="出入境合规",
      rel="supervisor", rel_text="上下级", src="二手", badge_r="r2", badge_b="b2", score=4,
      url="https://www.acciyo.com/top-business-visa-destinations-for-corporate-offsites-2025/",
      val="跨国团队 offsite 的隐形雷区是签证与出入境合规（Acciyo/Deel）：①选对签证——多数用 business visitor visa（覆盖会议/培训/团建），VoA 限制多；申根需 Letter of Invitation（母公司发邀请函写明目的/日期/担费，常 suffices）；②每人随身文件包——6个月以上有效期护照+往返机票+母公司邀请函（目的/费用担保）+住宿证明+医疗险（申根强制≥€30,000）；③双护照风险——非美/欧/英籍员工须逐个查目的地国政府网站，提前6-8周启动；④红线——不超停留上限（申根90天/墨西哥180天）、绝不在当地就业或接本地报酬（remote work for home co 通常视为 business visitor 延伸，但拿本地钱即违规）；⑤bleisure 趋势——业务后可 leisure 停留不超上限。HR/行政须建国别签证矩阵+行前审批+实时追踪。",
      inner="国际offsite签证合规:①选business visitor visa(VoA限制多),申根需母公司邀请函(目的/日期/担费);②每人文件包(护照6月+/往返票/邀请函/住宿/医疗险申根强制€30k);③非标护照逐个查目的国,提前6-8周;④红线(不超停留上限/绝不在当地就业拿本地钱);⑤bleisure业务后leisure不超上限;HR建国别签证矩阵+行前审批+实时追踪。",
      note="适用：② 公司内部上下级场景（HR/行政 owner 办跨国 offsite）。二手源=商旅签证指南。补「异地保险四层」之外「国际 offsite 出入境签证合规」这一跨境风控缺口；区别于国内团建。"),
 dict(emoji="🛡️", title="团建/Offsite 保险按活动类型配置矩阵（赛事/拓展/骑行/水上/旅行社责任险+雇主责任险）", cat="保险矩阵",
      rel="supervisor", rel_text="上下级", src="二手", badge_r="r2", badge_b="b2", score=4,
      url="https://liaocheng.dzwww.com/gnxw/202607/t20260731_17981661.htm",
      val="企业团建按活动风险分险种买保险（大众网聊城/保游）：①赛事运动（飞盘/球赛/龙舟/业余竞赛）——保游赛事无忧运动险，4元/天起，承保年龄1-90岁，意外医疗0免赔100%赔，含个人责任；②拓展训练（营地游戏/团队协作）——保游「勇者无惧」拓展训练险，2.2元/天起，15-50万多档，含救护/医疗运送；③骑行/城市定向——赛事无忧或专项骑行险；④高风险体验（卡丁车/丛林飞跃/攀岩）——先核对是否承保再选专项；⑤水上（桨板/帆船/冲浪）——乘风破浪水域险；⑥旅行社打包团建——旅行社责任险2026版（境内1400元/年起，累计200-2000万）+项目专项。底层：公司已有雇主责任险（覆盖员工工伤）+公众责任险（第三方），但活动专项险须按项目补。理赔关键点：项目写清楚+现场照片+医院材料+用药清单+报案时限。",
      inner="团建保险按活动类型配置:赛事(飞盘/球赛/龙舟)→赛事无忧运动险4元/天起,0免赔100%赔,含个人责任;拓展训练→勇者无惧2.2元/天起含救护运送;骑行→专项骑行险;高风险(卡丁车/攀岩)先核保再选专项;水上→水域险;旅行社打包→旅行社责任险2026版+项目专项;底层雇主责任险+公众责任险已有但活动专项须补;理赔留项目说明/现场照/医院材料/用药清单。",
      note="适用：② 公司内部上下级场景（HR/行政 owner 按团建项目买保险）。二手源=大众网聊城（保游产品实务）。补「异地保险四层」之外「按活动类型分险种配置矩阵」这一采购落地缺口；非 general 保险概念。"),
 dict(emoji="🔗", title="团建组织者责任险 vs 参与者个人意外险双轨（旅行社责任险≠个人险/组织者责任保障核对清单）", cat="责任双轨",
      rel="supervisor", rel_text="上下级", src="二手", badge_r="r2", badge_b="b2", score=4,
      url="https://m.sohu.com/a/1056811293_120403563",
      val="团建保险最易被一句话带过的坑：以为「有保险」就够（搜狐/保游）：①旅行社承接——按《旅行社条例》须投旅行社责任险，保障依法对游客人身/财产及委派导游领队的赔偿责任（境内1400元/年起，累计200-2000万/人20-150万），但它不能替代参与者个人险；员工飞盘扭伤，旅行社是否担责看活动安排/场地/管理，个人运动意外险按自身保障赔；②团建/拓展公司承接（非旅行社）——旅行社责任险不对口，须配组织者责任险/活动责任险/公众责任；采购须核对：被保险人是否实际签约执行公司、保单是否覆盖活动日期与场地、飞盘/骑行/拓展/车辆是否申报、单人/单次事故限额、教练兼职外包是否纳入、竞赛/高空/水上/机动是否除外；③双轨原则——责任险处理「组织方是否有责任」，个人险处理「参与者自身是否发生事故」，二者解决的问题不同，都要配。",
      inner="团建保险双轨:①旅行社承接→旅行社责任险(法定,境内1400/年起,累计200-2000万)但不能替代个人险;②拓展/团建公司承接→旅行社责任险不对口,配组织者/活动/公众责任险;采购核对(被保险人是否实际执行方/覆盖日期场地/项目是否申报/单人单次限额/教练外包纳入/高危是否除外);③双轨(责任险管「组织方有责」+个人险管「参与者自身事故」)都要配,别一句「有保险」带过。",
      note="适用：② 公司内部上下级场景（HR/行政 owner 向供应商采购团建保险）。二手源=搜狐（保游实务）。补「保险按活动类型矩阵」之外「组织者责任险 vs 参与者个人险双轨」这一采购核对缺口；明确「有保险≠够」。"),
]

PAGES = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/offsite"

def card_html(c):
    return (
        '    <div class="hl">\n'
        '      <div class="top"><span class="emoji">%s</span><h3>%s</h3>'
        '<span class="cat">%s</span><span class="badge %s">%s</span>'
        '<span class="badge %s">%s</span></div>\n'
        '      <p class="val">%s</p>\n'
        '      <details class="exec"><summary>怎么做</summary><div class="inner">%s</div></details>\n'
        '      <div class="src">🔗 <a href="%s" target="_blank">%s</a></div>\n'
        '      <div class="note">%s</div>\n'
        '    </div>\n'
    ) % (c["emoji"], c["title"], c["cat"], c["badge_r"], c["rel_text"],
         c["badge_b"], c["src"], c["val"], c["inner"], c["url"], c["url"], c["note"])

exec_cards = "".join(card_html(c) for c in cards if c["rel"]=="exec")
sup_cards = "".join(card_html(c) for c in cards if c["rel"]=="supervisor")
n_exec = sum(1 for c in cards if c["rel"]=="exec")
n_sup = sum(1 for c in cards if c["rel"]=="supervisor")
print("cards: exec=%d sup=%d total=%d" % (n_exec, n_sup, len(cards)))

# ---------- 1. update summary wall offsite.html ----------
html_path = os.path.join(BASE, TOPIC, TOPIC+".html")
html = open(html_path, encoding="utf-8").read()
sec3_header = html.find('<div class="sec sec3">')
sec3_grid = html.find('<div class="grid">', sec3_header)
sec2_header = html.find('<div class="sec sec2">')
sec2_grid = html.find('<div class="grid">', sec2_header)
footer_pos = html.rfind('<footer>')

# tag counts
old_sec3 = html.count('class="hl"', 0, sec2_header)
old_sec2 = html.count('class="hl"', sec2_header, footer_pos)
print("before: sec3=%d sec2=%d" % (old_sec3, old_sec2))

# inject (idempotent guard: skip if R35 cards already present)
if "tianqinzixunjituan.com/a/xinwen/1528.html" in html:
    print("WALL already has R35 cards, skip card injection")
else:
    html = html[:sec2_header] + exec_cards + html[sec2_header:footer_pos] + sup_cards + html[footer_pos:]
new_sec3 = html.count('class="hl"', 0, html.find('<div class="sec sec2">'))
new_sec2 = html.count('class="hl"', html.find('<div class="sec sec2">'), html.rfind('<footer>'))
print("after: sec3=%d sec2=%d total=%d" % (new_sec3, new_sec2, new_sec3+new_sec2))

# update tag spans
import re
html = html.replace('<span class="tag">%d 卡</span>' % old_sec3, '<span class="tag">%d 卡</span>' % new_sec3, 1)
html = html.replace('<span class="tag">%d 卡</span>' % old_sec2, '<span class="tag">%d 卡</span>' % new_sec2, 1)

# update hero prose
prose_tail = "三十四轮补采 +7（中文务虚会制度化四步法·务虚不越权·不出纪要保密设计 + offsite酒精行为准则/供酒政策模板/团建受伤五因子/异地保险四层）"
add = (" ｜ 2026-09-05 三十五轮补采 +10（裸心会深度研讨/务虚会成果闭环销号/务虚会务实三原则/"
       "务虚会精神一线穿透/C-suite结论级联 + 供应商合同审查/force majeure谈判/国际签证合规/"
       "保险按活动类型矩阵/组织者责任险双轨）")
if prose_tail in html:
    html = html.replace(prose_tail, prose_tail+add, 1)
else:
    print("WARN prose_tail not found")
open(html_path, "w", encoding="utf-8").write(html)
print("updated wall:", html_path)

# ---------- 2. increment page ----------
head = html[:html.index('</head>')+7]
inc = head + '\n<body>\n<div class="wrap">\n'
inc += '<div class="hero"><h1>Offsite 团建务虚 · 三十五轮增量页</h1>'
inc += '<p>采集于 2026-09-05 ｜ 本轮 +%d（%d 高管间 + %d 上下级）｜ 仅 ②上下级 / ③高管间，已剔除平级/朋友向</p>' % (len(cards), n_exec, n_sup)
inc += '<div class="relbar"><span>② 领导↔员工（上下级，supervisor）</span><span>③ 领导↔领导（高管间，exec）</span></div></div>\n'
inc += '\n    <div class="sec sec3">\n    <h2>③ 领导↔领导（高管间 · exec）</h2>\n'
inc += '<span class="tag">%d 卡</span>\n    <span class="desc">本轮新增高管间卡</span>\n  </div>\n' % n_exec
inc += '  <div class="grid">\n' + exec_cards + '  </div>\n'
inc += '\n    <div class="sec sec2">\n    <h2>② 领导↔员工（上下级 · supervisor）</h2>\n'
inc += '<span class="tag">%d 卡</span>\n    <span class="desc">本轮新增上下级卡</span>\n  </div>\n' % n_sup
inc += '  <div class="grid">\n' + sup_cards + '  </div>\n'
inc += '<footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>\n</div>\n</body>\n</html>\n'
inc_path = os.path.join(BASE, TOPIC, "%s-%s.html" % (TOPIC, DATE))
open(inc_path, "w", encoding="utf-8").write(inc)
print("increment page:", inc_path, len(inc), "bytes")

# ---------- 3. index.json ----------
idx_path = os.path.join(BASE, "index.json")
idx = json.load(open(idx_path, encoding="utf-8"))
existing_urls = {e.get("url") for e in idx}
added = 0
for c in cards:
    if c["url"] in existing_urls:
        print("SKIP dup url:", c["url"]); continue
    idx.append({
        "title": c["title"], "normKey": c["title"], "url": c["url"],
        "sourceType": "primary" if c["src"]=="一手" else "secondary",
        "relation": c["rel"], "summary": c["val"][:120], "topic": TOPIC,
    })
    added += 1
    existing_urls.add(c["url"])
json.dump(idx, open(idx_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("index.json appended:", added, "-> total", len(idx))

# ---------- 4. Obsidian note ----------
vault = "C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库"
note_path = os.path.join(vault, "素材", SLUG, VAULT_NOTE+".md")
note = open(note_path, encoding="utf-8").read()
note = note.replace("知识卡汇总（242 卡", "知识卡汇总（252 卡", 1)
# append round line to last prose blockquote (the one with 三十四轮)
note = note.replace(
  "三十四轮补采 +7（中文务虚会制度化四步法/务虚不越权/不出纪要保密设计 + 酒精行为准则/供酒政策模板/团建受伤五因子/异地保险四层）。",
  "三十四轮补采 +7（中文务虚会制度化四步法/务虚不越权/不出纪要保密设计 + 酒精行为准则/供酒政策模板/团建受伤五因子/异地保险四层）。｜ 2026-09-05 三十五轮补采 +10（裸心会深度研讨/务虚会成果闭环销号/务虚会务实三原则/务虚会精神一线穿透/C-suite结论级联 + 供应商合同审查/force majeure谈判/国际签证合规/保险按活动类型矩阵/组织者责任险双轨）。",
  1)
# insert new round section before first "## 轮次"
round_section = "\n## 轮次 20260905·三十五轮（+%d）\n\n| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n" % len(cards)
for c in cards:
    round_section += "| %s（offsite.html） | %s | %s |\n" % (c["title"], c["rel_text"], c["src"])
round_section += "\n"
first_round = note.find("## 轮次")
note = note[:first_round] + round_section + note[first_round:]
open(note_path, "w", encoding="utf-8").write(note)
print("updated obsidian note:", note_path)

# ---------- 5. 00-index ----------
idx00_path = os.path.join(vault, "00-知识采集索引.md")
t = open(idx00_path, encoding="utf-8").read()
sec_start = t.find("## 主题：Offsite")
# find end of this section = next "## 主题：" after sec_start
nxt = t.find("## 主题：", sec_start+5)
end = nxt if nxt != -1 else len(t)
rows = ""
for c in cards:
    rows += "| %s（offsite.html） | %d | %s | %s | %s |\n" % (c["title"], c["score"], c["src"], c["rel_text"], c["val"][:60])
t = t[:end] + rows + t[end:]
open(idx00_path, "w", encoding="utf-8").write(t)
print("updated 00-index")

# ---------- 6. lexiang map ----------
map_path = os.path.join(BASE, "lexiang-entry-map.json")
mp = json.load(open(map_path, encoding="utf-8"))
mp[SLUG]["rounds"].append({"date": "2026-09-05", "entry_id": None,
    "name": "%s-%s.html" % (TOPIC, DATE),
    "note": "轮次页 R35 (+%d：%d③高管间+%d②上下级)｜乐享待补传(connector disconnected/token 401，待重连后补传并回填 entry_id)" % (len(cards), n_exec, n_sup)})
json.dump(mp, open(map_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("updated map R35")

# ---------- 7. last-topic ----------
open(os.path.join(BASE, "last-topic.txt"), "w", encoding="utf-8").write("破冰\n")
print("last-topic -> 破冰")
print("DONE")
