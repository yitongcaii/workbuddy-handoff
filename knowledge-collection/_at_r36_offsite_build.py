# -*- coding: utf-8 -*-
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
TOPIC = "offsite"
SLUG = "offsite"
DATE = "20260906"
ROUND = "三十六轮"
RUN_LABEL = "三十六轮补采 +10"
VAULT_NOTE = "Offsite-团建务虚-知识卡汇总"

# ---- 10 cards (only supervisor / exec) ----
cards = [
 # ③ 高管间
 dict(emoji="🧭", title="战略务虚会六维规划框架（目的/人选/场地/议程/引导/问责 + AI与现金流模块）", cat="战略务虚规划",
      rel="exec", rel_text="高管间", src="二手", badge_r="r3", badge_b="b2", score=4,
      url="https://www.altaconsulting.ca/post/how-to-plan-strategic-retreat",
      val="高影响力战略务虚会需六维规划，并把 AI 赋能与现金流压力测试织进 retreat：①目的——设 2-3 个可量化目标（新定位/增长杠杆/组织重组），含「领导力 AI 赋能」「现金流约束」类目标；②人选——邀关键决策者，加 AI champion 与财务负责人入圈；③场地——降干扰+强网络（跑 AI demo）+战略思考空间；④议程——平衡战略规划/小组 breakout/个人反思/决策，专留 AI 学习+现金流深潜块；⑤引导——用框架+中立主持，引入 AI/财务双 facilitator；⑥问责——发纪要/定 owner/设 check-in/建仪表盘（战略+财务+AI 采纳指标）。排期 8-12 周：定目的→拟议程→发 pre-read→定后勤→提醒。AI 模块（为什么/直播 demo/沙盒/路线图）；现金流模块（现状复盘/2-3 what-if 情景建模/决策赋能/监控仪表盘）。",
      inner="六维规划:①目的设2-3个可量化目标(新定位/增长杠杆/组织重组)+含领导力AI赋能/现金流约束目标;②人选邀关键决策者+加AI champion/财务负责人;③场地降干扰+强网络(跑AI demo)+战略思考空间;④议程平衡(战略规划/小组breakout/个人反思/决策)+专留AI学习+现金流深潜块;⑤引导用框架+中立主持+引入AI/财务双facilitator;⑥问责(发纪要/定owner/设check-in/建仪表盘=战略+财务+AI采纳指标);排期8-12周:定目的→拟议程→发pre-read→定后勤→提醒;AI模块(为什么/直播demo/沙盒/路线图);现金流模块(现状复盘/2-3情景建模/决策赋能/监控仪表盘)。",
      note="适用：③高管间（经管会/高管团队战略务虚会）。二手源=咨询公司实操指南。补「务虚会务实三原则/闭环销号」之外「战略务虚会六维规划框架 + AI与现金流模块」这一现代版规划骨架；区别于平级团建，本卡是「高管战略务虚会怎么系统规划」。"),
 dict(emoji="🎯", title="战略解码 Hoshin Kanri（X-Matrix 四臂 + A3 catchball 上下博弈 + 月度复盘，把愿景落到年度重点）", cat="战略解码",
      rel="exec", rel_text="高管间", src="二手", badge_r="r3", badge_b="b2", score=4,
      url="https://workshopweaver.com/facilitation-methods/hoshin-kanri",
      val="Hoshin Kanri（方针管理，1960s 丰田）把长期愿景转成年度重点并逐级 cascade。两构件：①X-Matrix 一页连通「3-5年突破目标(南)/年度重点(西)/改善项目(北)/指标目标(东)」，符号标关系强度，空白关系=战略与执行脱节；②A3 catchball 上下博弈——领导提方向↔一线回容量/顾虑/修订再承诺，真谈判而非下压，建对齐与共有感。Workshop 八步：讲四臂→定突破目标「3-5年必须根本不同什么」→逼选年度重点 3-5→每个重点配改善项目+owner→定领先/滞后指标→标关系强度+查空白→审平衡→排 catchball+定月度 Hoshin Review。避坑：填完矩阵就跳过 catchball 必败；突破目标限 3-5；年度重点真选非全列；关系矩阵当诊断器；配月度复盘节奏。",
      inner="Hoshin Kanri两构件:①X-Matrix一页连通(3-5年突破目标/年度重点/改善项目/指标目标),符号标关系强度,空白=战略执行脱节;②A3 catchball上下博弈(领导提方向↔一线回容量/顾虑/修订再承诺),真谈判非下压,建对齐与共有感;workshop八步(讲四臂→定突破目标→逼选年度重点3-5→配改善项目+owner→定领先滞后指标→标关系强度查空白→审平衡→排catchball+月度Review);避坑(跳catchball必败/突破限3-5/年度重点真选/关系矩阵当诊断/配月度复盘)。",
      note="适用：③高管间（领导班子战略解码/年度重点对齐）。二手源=引导方法库（含可抄 workshop 脚本）。补「务虚会务虚」之外「战略如何解码到年度重点并逐级 catchball 对齐」这一落地机制（丰田方针管理）；区别于华为 DSTE（已采宏观流程），本卡是可操作的 X-Matrix+catchball 工作坊。"),
 dict(emoji="🗓️", title="战略会议全日议程模板（愿景对齐→小组breakout→优先级排序→行动规划，8小时认知节律）", cat="议程模板",
      rel="exec", rel_text="高管间", src="二手", badge_r="r3", badge_b="b2", score=4,
      url="https://chronolio.com/templates/strategy-session-agenda",
      val="战略会议全日框架引导高管团队走完长期愿景对齐/跨职能 breakout/优先级排序/行动归属。时间表：08:30 咖啡破冰→09:00 愿景对齐（市场背景/使命/年度营收目标）→10:15 跨职能 breakout（4-6人 candid 解决部门摩擦）→12:00 策略午餐（非正式跨组碰撞）→13:15 优先级排序（影响vs可行）→15:00 行动规划（定 owner/截止/KPI）→16:00 高管收尾→16:30 社交酒。铁律：严格时间表护认知精力、给引导者叫停跑题的抓手、把抽象创意转成季度 OKR。须含（到场破冰+愿景对齐+跨职能 breakout+策略午餐+影响可行排序+资源分配行动+收尾+会后酒）；避坑（无单一产出/塞太满/不落 owner/无跟进）。",
      inner="战略会议全日模板(护高管认知节律):08:30咖啡破冰→09:00愿景对齐(市场背景/使命/年度营收)→10:15跨职能breakout(4-6人candid解决部门摩擦)→12:00策略午餐(非正式跨组碰撞)→13:15优先级排序(影响vs可行)→15:00行动规划(owner/截止/KPI)→16:00高管收尾→16:30社交酒;铁律(严格时间表护精力/给引导者叫停跑题抓手/抽象创意转季度OKR);须含(破冰+愿景+breakout+午餐+排序+资源行动+收尾+会后酒);避坑(无单一产出/塞太满/不落owner/无跟进)。",
      note="适用：③高管间（高管战略务虚会/战略日议程）。二手源=议程模板工具站（含可抄全天时间表）。补「务虚会六大议题/裸心会」之外「战略会议全日时间盒议程」这一可操作时间表（按认知节律排布）；区别于 board retreat（治理向），本卡是「exec 战略日」的通用议程骨架。"),
 dict(emoji="🤝", title="并购后文化融合 workshop（行为风格解码→共创团队宪章，把「我们vs他们」变「我们」）", cat="并购文化融合",
      rel="exec", rel_text="高管间", src="二手", badge_r="r3", badge_b="b2", score=4,
      url="https://carrara-advisory.com/publications-workshops/p/workshop-from-two-cultures-to-one-team-post-integration-alignment",
      val="并购最大风险不是战略/系统而是人：文化错配占整合失败高达 70%（隐性抵触/重复劳动/决策节奏冲突/信任侵蚀）。全天 workshop（两个半日）治本——①解码 legacy 行为风格（DISC 四维：支配/影响/稳健/严谨在两司表现不同；自评+debrief→识别自身默认/压力触发/决策模式，识别对方组织同事；以好奇替评判）；②共创一队操作系统（标 legacy 文化冲突点：速度vs精确、直接vs外交式反馈；盲区；练结构化反馈/冲突/角色/决策；产出共同「团队宪章」嵌入新习惯+成功指标+问责）。适用并购整合领导团队/跨 legacy 项目组/HR·L&D·PMO 设计 playbook。",
      inner="并购最大风险是人(文化错配占整合失败高达70%:隐性抵触/重复劳动/决策节奏冲突/信任侵蚀);全天workshop(两半日)治本:①解码legacy行为风格(DISC四维在两司不同;自评+debrief→识别自身默认/压力触发/决策模式,识别对方同事;以好奇替评判);②共创一队操作系统(标legacy冲突点:速度vs精确/直接vs外交式反馈;盲区;练结构化反馈/冲突/角色/决策;产出共同团队宪章嵌入新习惯+指标+问责);适用(并购整合领导团队/跨legacy项目组/HR·L&D·PMO)。",
      note="适用：③高管间（并购后整合领导团队务虚/文化融合 offsite）。二手源=咨询公司 workshop 产品（含可抄两半日结构）。补「务虚会精神穿透」之外「并购后两文化如何融成一队」这一专项 offsite（行为风格解码+团队宪章）；区别于 Bain 并购变革（已采宏观 cascade），本卡是「文化融合 workshop」的可操作版。"),
 dict(emoji="🌅", title="战略 Offsite 定位与避坑（六大触发时机 / 过度塞议程·缺跟进·预算·虚拟脱节 四坑 / 最佳实践）", cat="战略offsite定位",
      rel="exec", rel_text="高管间", src="二手", badge_r="r3", badge_b="b2", score=4,
      url="http://www.naboo.app/en-us/blog/strategy-offsite",
      val="战略 offsite=离总部专设会，领导层论长期目标/竞争态势/组织挑战，混焦点+协作+前瞻；区别于董事会（治理合规）在鼓励开放对话+创意解题。麦肯锡：定期复盘战略的公司超额盈利概率高 33%。六触发：启新战略周期/应市场变局/渡转型（并购重组）/全球对齐/发布前对齐。四坑：议程塞太满（2天想解决一切稀释冲击）、缺跟进（洞察不变路线图）、预算失控、虚拟脱节稀释参与。最佳实践：先定目标（愿景or创新or对齐?）、结构+创意+纪律平衡、选址即战略信号。",
      inner="战略offsite=离总部专设会,领导层论长期目标/竞争态势/组织挑战,混焦点+协作+前瞻;区别于董事会(治理合规)在鼓励开放对话+创意解题;麦肯锡:定期复盘战略公司超额盈利高33%;六触发(启新战略周期/应市场变局/渡转型并购重组/全球对齐/发布前对齐);四坑(议程塞太满稀释冲击/缺跟进洞察不变路线图/预算失控/虚拟脱节稀释参与);最佳实践(先定目标愿景or创新or对齐?/结构+创意+纪律平衡/选址即战略信号)。",
      note="适用：③高管间（高管团队战略 offsite 定位决策）。二手源=活动策划平台博客。补「战略务虚会六维规划」之外「何时该办战略 offsite + 四大翻车坑 + 最佳实践」这一定位与风险框架；区别于具体议程模板，本卡是「办不办/为什么办/避开什么」的判断层。"),
 # ② 上下级
 dict(emoji="📊", title="企业团建成本预算工具集（4模板：基本信息/成本明细/执行跟踪/复盘，含10%应急备用金）", cat="预算工具集",
      rel="supervisor", rel_text="上下级", src="二手", badge_r="r2", badge_b="b2", score=4,
      url="https://renrendoc.com/paper/496587134.html",
      val="4 模板工具集：①项目基本信息表（名称/目标/人数/时长/地点/形式/负责人）；②项目成本预算明细表（成本类别/项/单位/数量/单价/小计/计算依据/负责人：场地租赁/导师/装备/餐饮/交通/保险/应急备用金=总预估10%）；③预算执行跟踪表（预算/实际/差异额/差异率/原因/记录人：例场地省500、餐饮超10%、应急省48%）；④成本复盘表（预算总额/实际/达成率/核心差异分析/改进建议）。关键要点：需求导向精准预估（历史数据/3-5家报价）；动态监控及时预警（异常差异标红查根因）；成本效益平衡（保核心成本项、压非核心装饰）。",
      inner="团建预算四模板:①项目基本信息(目标/人数/时长/地点/形式/负责人);②成本明细(类别/项/单位/数量/单价/小计/依据/责任人:场地+导师+装备+餐饮+交通+保险+应急备用金=总预估10%);③执行跟踪(预算/实际/差异额/率/原因/记录人,例餐饮超10%临时加海鲜);④成本复盘(总额/实际/达成率/差异分析/改进);要点(需求导向精准预估查3-5家报价/动态监控异常标红查根因/成本效益平衡保核心压装饰)。",
      note="适用：② 公司内部上下级场景（HR/行政 owner 编团建预算）。二手源=人人文库实务模板集。补「保险矩阵/合同审查」之外「团建成本预算四模板工具集（明细+跟踪+复盘）」这一预算编制缺口；非场地选型/保险。"),
 dict(emoji="📐", title="Offsite 预算 Google Sheets 模板（10%缓冲·人均实时·lean/planned/stretch 三情景）", cat="预算模板",
      rel="supervisor", rel_text="上下级", src="二手", badge_r="r2", badge_b="b2", score=4,
      url="https://teamrally.app/templates/budget",
      val="即用 Google Sheets 模板规划/追踪每笔成本——差旅/住宿/餐饮/活动/场地/swag/应急。内含：类目覆盖真实成本；计划vs实际列（漂移早发现）；人均汇总随人数实时重算；内置 10% 缓冲（cover 遗漏项）；情景行（lean/planned/stretch 三版供领导对话）。用法：复制→顶部设人数+目标人均→填各类计划成本实时出总计人均→预订后记实际。铁律：定价场地前先锁 all-in 数（对话诚实）；按确认 RSVP 而非邀请名单预算（75% 出席率让人均波动 1/3）；应急线不动用前不碰；领导只读共享、核心策划才可编。",
      inner="Offsite预算Sheets模板:类目覆盖(差旅/住宿/餐饮/活动/场地/swag/应急);计划vs实际列(漂移早发现);人均汇总随人数实时重算;内置10%缓冲(cover遗漏项);情景行(lean/planned/stretch三版供领导对话);用法(复制→顶部设人数+目标人均→填各类计划成本实时出总计人均→预订后记实际);铁律(定价场地前先锁all-in数/按确认RSVP而非邀请名单预算-75%出席率让人均波动1/3/应急线不动用前不碰/领导只读共享核心策划才可编)。",
      note="适用：② 公司内部上下级场景（HR/行政 owner 用表格控 offsite 预算）。二手源=模板工具站（Google Sheets 可抄）。补「团建预算四模板」之外「带10%缓冲+人均实时+三情景」的轻量表格模板；区别于 heavy Excel，本卡是「实时可控」的预算表。"),
 dict(emoji="🎤", title="会议引导 facilitation 六步 + 技法（round-robin/dot voting/parking lot，经理主持部门务虚会）", cat="引导技巧",
      rel="supervisor", rel_text="上下级", src="二手", badge_r="r2", badge_b="b2", score=4,
      url="https://resources.rework.com/libraries/employee-competencies/facilitation-skills",
      val="Facilitation=无职权影响力，塑流程让群体产出更优。六步：①定目的+议程（一句话「产出什么决策」，提前24h发带时段）；②立基本规则（一人讲/手机扣下/求承诺非仅共识）；③开场暖身（1分钟 check-in 建心理在场）；④引导讨论管发言权（盯话痨与沉默，round-robin/点名，跑题就标注 park）；⑤逼出决策+行动（确认决定/owner/时限，实时可见记录）；⑥收尾+跟进（3-5分钟复盘，24h内发书面摘要：决策/开放问题/行动项）。技法：round-robin（平衡声音）、dot voting（多选项定优先级）、parking lot（收跑题）、时间盒、小组 breakout、五指表决测认同。适用于经理主持 retro、Scrum master 迭代规划。",
      inner="引导facilitation六步(无职权影响力,塑流程让群体产出更优):①定目的+议程(一句话产出什么决策,提前24h发带时段);②立基本规则(一人讲/手机扣下/求承诺非仅共识);③开场暖身(1分钟check-in建心理在场);④引导讨论管发言权(盯话痨与沉默,round-robin/点名,跑题标注park);⑤逼出决策+行动(确认决定/owner/时限,实时可见记录);⑥收尾+跟进(3-5分钟复盘,24h内发书面摘要:决策/开放问题/行动项);技法(轮转平衡声音/点投票定优先级/parking lot收跑题/时间盒/小组breakout/五指表决测认同)。",
      note="适用：② 公司内部上下级场景（经理/主管主持部门务虚会·部门会）。二手源=HR 能力库（含可抄六步+技法）。补「务虚会六大议题/裸心会」之外「经理怎么 facilitate 一场部门务虚会」这一主持落地技能；区别于高管务虚（exec），本卡是「基层管理者引导术」。"),
 dict(emoji="🛡️", title="团建活动安全预案结构（领导小组/四原则/应急程序/报告链，政府发布可抄框架）", cat="安全预案",
      rel="supervisor", rel_text="上下级", src="一手", badge_r="r2", badge_b="b1", score=4,
      url="https://www.huainan.gov.cn/public/118325569/1259590707.html",
      val="淮南二十三中团建活动安全预案（政府发布，可迁移为公司团建安全预案框架）：一、领导小组（组长/副/成员，订方案、处意外；严重事故第一时间上报）。二、组织保障（出发前全员安全教育；听指挥不脱队；分散活动设小组长/安全负责人随时清点；饮食拒三无；留负责人联系方式保联络；守交规防走失）。三、突发事件四原则（人为本救援第一/沉着冷静互助/属地救护就近处置/及时报告信息畅）。四、处理程序（发生→拨110/120救护→送就近医院→报带队负责人→告家属→报保卫→报上级）。五、应急处置（报告通报含时间地点种类程度危害措施；向公安消防卫生求援；现场保护/疏散/安抚稳情绪）。把教体局→公司安全/HR、家属→员工家属即公司版。",
      inner="团建安全预案结构(政府发布框架可平移公司):①领导小组(组长/副/成员,订方案处意外,重伤第一时间上报);②组织保障(出发前全员安全教育/听指挥不脱队/分散活动设小组长安全负责人随时清点/饮食拒三无/留负责人联系方式/守交规防走失);③突发事件四原则(人为本救援第一/沉着冷静互助/属地救护就近处置/及时报告信息畅);④处理程序(发生→拨110/120救护→送就近医院→报带队负责人→告家属→报保卫→报上级);⑤应急处置(报告通报含时间地点种类程度危害措施/向公安消防卫生求援/现场保护疏散安抚稳情绪);教体局→公司安全HR/家属→员工家属即公司版。",
      note="适用：② 公司内部上下级场景（HR/行政 owner 写团建安全预案）。一手源=淮南市政府发布的安全预案（公文框架）。补「保险矩阵/受伤五因子」之外「团建安全预案的组织结构+四原则+报告链」这一应急预案骨架；区别于事后理赔，本卡是「事前预案+事中处置流程」。"),
 dict(emoji="💡", title="团建预算五维成本模型 + 三招破局（资源置换/优先级/动态调整，抓杠杆环节）", cat="预算方法论",
      rel="supervisor", rel_text="上下级", src="二手", badge_r="r2", badge_b="b2", score=4,
      url="https://www.renrendoc.com:8443/paper/505163878.html",
      val="成本构成「五维模型」（参考占比）：场地/场景费 20-30%(小)/15-25%(中)；物料/道具 10-15%/8-12%；师资/服务费 15-20%/12-18%；餐饮/交通 30-40%/25-35%；应急/预备 5-10%。预算管控「三招破局」：①资源置换——与摄影/餐饮等供应商协商「服务置换」，用企业宣传资源（公众号推文/线下展位）抵扣部分费用；②优先级排序——抓高杠杆环节（师资专业教练提升任务设计合理性、成果输出文化IP手册/记忆库长期复用），可优化环节（餐饮选简餐+特色小吃比高端宴席性价比高、道具用企业现有物料改造）；③动态调整——按「基础版+升级包」设计预算，依最终报名人数/赞助资源动态调整，建「预算追踪表」每笔支出同步更新剩余额度防超支。",
      inner="团建成本五维模型(参考占比):场地场景20-30%/15-25%;物料道具10-15%/8-12%;师资服务15-20%/12-18%;餐饮交通30-40%/25-35%;应急预备5-10%;三招破局:①资源置换(与摄影/餐饮供应商用企业宣传资源公众号推文/线下展位抵扣费用);②优先级(抓杠杆:师资专业教练+成果文化IP手册记忆库长期复用;可优化:餐饮简餐+特色小吃替高端宴席/道具用企业现有改造);③动态调整(基础版+升级包,按报名人数/赞助实时调,建预算追踪表每笔同步剩余防超支)。",
      note="适用：② 公司内部上下级场景（HR/行政 owner 做团建预算编制与管控）。二手源=人人文库策划方案模板。补「预算四模板/Sheets模板」之外「五维成本模型+三招破局」这一预算方法论（资源置换/优先级/动态调整）；区别于工具表，本卡是「怎么想预算结构、把钱花在杠杆上」。"),
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

old_sec3 = html.count('class="hl"', 0, sec2_header)
old_sec2 = html.count('class="hl"', sec2_header, footer_pos)
print("before: sec3=%d sec2=%d" % (old_sec3, old_sec2))

if "altaconsulting.ca/post/how-to-plan-strategic-retreat" in html:
    print("WALL already has R36 cards, skip card injection")
else:
    html = html[:sec2_header] + exec_cards + html[sec2_header:footer_pos] + sup_cards + html[footer_pos:]
new_sec3 = html.count('class="hl"', 0, html.find('<div class="sec sec2">'))
new_sec2 = html.count('class="hl"', html.find('<div class="sec sec2">'), html.rfind('<footer>'))
print("after: sec3=%d sec2=%d total=%d" % (new_sec3, new_sec2, new_sec3+new_sec2))

html = html.replace('<span class="tag">%d 卡</span>' % old_sec3, '<span class="tag">%d 卡</span>' % new_sec3, 1)
html = html.replace('<span class="tag">%d 卡</span>' % old_sec2, '<span class="tag">%d 卡</span>' % new_sec2, 1)

prose_tail = ("团建受伤五因子/异地保险四层） ｜ 2026-09-05 三十五轮补采 +10（裸心会深度研讨/务虚会成果闭环销号/"
              "务虚会务实三原则/务虚会精神一线穿透/C-suite结论级联 + 供应商合同审查/force majeure谈判/国际签证合规/"
              "保险按活动类型矩阵/组织者责任险双轨）")
add = (" ｜ 2026-09-06 三十六轮补采 +10（战略务虚会六维规划+AI现金流模块 / Hoshin Kanri X矩阵+catchball / "
       "战略会议全日议程模板 / 并购后文化融合workshop / 战略offsite定位与避坑 + 团建预算四模板工具集 / "
       "Google Sheets预算10%缓冲 / 部门务虚会facilitation六步 / 团建安全预案四原则 / 团建预算五维模型三招破局）")
if prose_tail in html:
    html = html.replace(prose_tail, prose_tail+add, 1)
else:
    print("WARN prose_tail not found")
open(html_path, "w", encoding="utf-8").write(html)
print("updated wall:", html_path)

# ---------- 2. increment page ----------
head = html[:html.index('</head>')+7]
inc = head + '\n<body>\n<div class="wrap">\n'
inc += '<div class="hero"><h1>Offsite 团建务虚 · 三十六轮增量页</h1>'
inc += '<p>采集于 2026-09-06 ｜ 本轮 +%d（%d 高管间 + %d 上下级）｜ 仅 ②上下级 / ③高管间，已剔除平级/朋友向</p>' % (len(cards), n_exec, n_sup)
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
note = note.replace("知识卡汇总（252 卡", "知识卡汇总（262 卡", 1)
note_tail = ("三十五轮补采 +10（裸心会深度研讨/务虚会成果闭环销号/务虚会务实三原则/务虚会精神一线穿透/"
            "C-suite结论级联 + 供应商合同审查/force majeure谈判/国际签证合规/保险按活动类型矩阵/组织者责任险双轨）。")
add_note = (" ｜ 2026-09-06 三十六轮补采 +10（战略务虚会六维规划+AI现金流模块 / Hoshin Kanri X矩阵+catchball / "
           "战略会议全日议程模板 / 并购后文化融合workshop / 战略offsite定位与避坑 + 团建预算四模板工具集 / "
           "Google Sheets预算10%缓冲 / 部门务虚会facilitation六步 / 团建安全预案四原则 / 团建预算五维模型三招破局）。")
if note_tail in note:
    note = note.replace(note_tail, note_tail+add_note, 1)
else:
    print("WARN note_tail not found")
round_section = "\n## 轮次 20260906·三十六轮（+%d）\n\n| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n" % len(cards)
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
mp[SLUG]["rounds"].append({"date": "2026-09-06", "entry_id": None,
    "name": "%s-%s.html" % (TOPIC, DATE),
    "note": "轮次页 R36 (+%d：%d③高管间+%d②上下级)｜乐享待补传(connector disconnected/token 401，待重连后补传并回填 entry_id)" % (len(cards), n_exec, n_sup)})
json.dump(mp, open(map_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("updated map R36")

# ---------- 7. last-topic ----------
open(os.path.join(BASE, "last-topic.txt"), "w", encoding="utf-8").write("破冰\n")
print("last-topic -> 破冰")
print("DONE")
