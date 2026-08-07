# -*- coding: utf-8 -*-
import json, io, os, re

BASE = r"C:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection"
HTML = os.path.join(BASE, "openday", "openday.html")
IDX  = os.path.join(BASE, "index.json")

# ---------- 新卡片 HTML 片段（② 上下级 6 张 / ③ 高管间 5 张）----------
new_sec2 = """
    <div class="hl">
      <div class="top"><span class="emoji">🏭</span><h3>华丰科技四期「情融华丰·家倍温暖」家属开放日</h3><span class="cat">家属开放日</span><span class="badge r2">上下级</span><span class="badge b1">一手</span></div>
      <p class="val">华丰科技 2025 暑期家属开放日系列活动（公司官网）：自 7/18 首期至 8/8 第四期，连续四周周五与员工家庭相约，累计 153 个家庭、277 名家属走进园区。四期沿「认知→共情→共建」层层推进，每期坚守「指纹签到破冰+产线探秘+手工互动」核心，并融入专属特色（茶歇分享/财商小游戏/切蛋糕忆征程仪式）；以「家属视角」构建情感共鸣——展厅回溯历程、产线触摸科技温度，孩子为父母工作点赞、老人因安心环境踏实；猜灯谜/漆扇 DIY/艾草颈枕融合家风传承与健康关怀，让家属从旁观者变文化共建者。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">把家庭日做成「系列」而非一次性（四周接力沉淀家文化）；核心三件套（签到破冰/产线探秘/手工互动）稳定可复制；收官仪式（切蛋糕串联四期）强化身份认同；让家属从「看客」变「共建者」提升参与深度。</div></details>
      <div class="src">🔗 <a href="https://huafeng796.com/details.html?id=1955515597372121090" target="_blank">huafeng796.com/.../1955515597372121090</a></div>
      <div class="note">适用：② 科技制造企业多期次家属开放日范式，党委关怀+工会筹备，规模 150+ 家庭可抄。</div>
    </div>

    <div class="hl">
      <div class="top"><span class="emoji">🔬</span><h3>景嘉微2025「同心同行·乐享嘉时光」家庭开放日</h3><span class="cat">家属开放日</span><span class="badge r2">上下级</span><span class="badge b1">一手</span></div>
      <p class="val">景嘉微（长沙，国产 GPU 企业）2025 年度家庭开放日（公司官网）：60 余组、近 200 名家属参与。签到「幸福照片墙」开场→趣味魔术+宣传片→公司领导致辞（肯定员工+感谢家属）→游园会高潮（发电竞速赛/弹珠迷宫/欢乐神投手/红星竹编画非遗/小丑互动/娃娃机）→员工食堂品尝工作餐收尾。家属探秘展厅与生产车间，通过讲解员了解创新成果与技术实力，深度理解亲人日常价值。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">以「照片墙」定温情基调；魔术+宣传片快速聚拢注意力；领导致辞聚焦「感谢家属」而非业绩；游园会按年龄段分区（童趣竞技/创意工坊/甜蜜加油站）；以「吃一顿工作餐」收尾让家属触摸真实日常。</div></details>
      <div class="src">🔗 <a href="https://www.jingjiamicro.com/news/73.html" target="_blank">jingjiamicro.com/news/73.html</a></div>
      <div class="note">适用：② 高科技企业家庭开放日，200 人规模，非遗竹编等文化植入可借鉴。</div>
    </div>

    <div class="hl">
      <div class="top"><span class="emoji">🧬</span><h3>安科生物「安科嘉年华·秋日奇遇记」家属开放日</h3><span class="cat">家属开放日</span><span class="badge r2">上下级</span><span class="badge b1">一手</span></div>
      <p class="val">安科生物（合肥，生物医药）2025 家属开放日（公司官网）：200 余名员工及家属走进总部。董事长宋礼华现场互动合影，执行总裁姚建平致辞（「造福人类健康的伟大事业」+展示三十载成就+感谢坚守）；科学秀（空气炮/魔术/无重力漂浮）点燃孩子热情；游园会含棉花糖/投壶/套圈/中医问诊/中药香囊 DIY；特设公益义卖（所得助白血病儿童），让员工子女在分享中种下善意种子。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">董事长/总裁双层级出场强化重视；科学秀替代纯游戏契合生物医药调性；公益义卖把「责任文化」具象为亲子可参与动作；中医问诊+香囊 DIY 做健康关怀差异化。</div></details>
      <div class="src">🔗 <a href="https://ankebio.com/display_2866.html" target="_blank">ankebio.com/display_2866.html</a></div>
      <div class="note">适用：② 医药企业家庭开放日，公益元素+科学调性，避免幼稚游戏。</div>
    </div>

    <div class="hl">
      <div class="top"><span class="emoji">🛰️</span><h3>中国电科二十七所「同心筑梦 一路有你」家属开放日</h3><span class="cat">家属开放日</span><span class="badge r2">上下级</span><span class="badge b1">一手</span></div>
      <p class="val">中国电科二十七所、新防务公司家属开放日（央企官网）：特邀 2024-2025 年度优秀党员、优秀党务工作者直系亲属参与。家属参观紫鼎广场文化景观（所司历程与精神内核）、智慧农业试验场（科研成果转化）、无人机联试场（直观感受技术实力）、《初心的底色》宣传视频（国防电子初心使命）；结束后职工食堂用餐拉近距离。打破单位与家庭「距离感」，凝聚「携手奋进」力量。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">以「荣誉家属」（优秀党员/党务工作者直系亲属）为邀约对象，把开放日与表彰挂钩；科研场景（智慧农业/无人机）做适龄化讲解让孩子看懂父母工作；宣传片讲「初心使命」契合军工文化；食堂共餐降层级感。</div></details>
      <div class="src">🔗 <a href="https://www.cetc.com.cn/27/335529/335505/2115556/index.html" target="_blank">cetc.com.cn/.../2115556/index.html</a></div>
      <div class="note">适用：② 科研院所/军工单位家属开放日，涉密单位可开放非密科研成果展示，荣誉家属定向邀约。</div>
    </div>

    <div class="hl">
      <div class="top"><span class="emoji">⚡</span><h3>东方电气「智造零距离·能源科普行」企业开放日</h3><span class="cat">国企开放日</span><span class="badge r2">上下级</span><span class="badge b1">一手</span></div>
      <p class="val">东方电气（央企）以「感恩·见证·焕新」为主题集中开展企业开放日（公司官网）：东方电机 170 个家庭、1000 余名职工家属参加「清风健行」环厂健身跑+智造零距离；东方汽轮机 140 余名劳模工匠及家属走进数字集控中心/全重科技展厅/数字化车间，孩子做「钛合金小超人」试验+学灭火器；东方锅炉公众开放日 160 余人（政府/企事业单位/学校/供方/家属）；东方风电/东方国际职工家庭开放日。把大国重器、东汽精神与家风建设一体呈现。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">以「文化周」为容器集中办多场开放日，降本增效；家庭日绑定健身跑/劳模工匠元素做荣誉感；科普环节（材料实验室/安全小屋）让孩子「可感」；分人群（家属/公众/媒体）设计不同动线但共用「大国重器」叙事。</div></details>
      <div class="src">🔗 <a href="https://www.dec-ltd.cn/info/1515/12549.htm" target="_blank">dec-ltd.cn/info/1515/12549.htm</a></div>
      <div class="note">适用：②+③ 大型央企综合开放日，家属+公众+媒体多人群覆盖，能源/制造科普基调。</div>
    </div>

    <div class="hl">
      <div class="top"><span class="emoji">🚚</span><h3>江铃汽车「暑期家庭行」全民开放日（智造+研学）</h3><span class="cat">全民开放日</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">江铃汽车富山工厂「暑期家庭行」专场全民开放日（行业媒体）：100 多名全国访客与江铃员工家庭走进工厂，乘观光车进车间亲见钢板到整车的「奇幻蜕变」；全国技术能手现场讲「江铃智造」故事；12 秒完成车型切换、最快 15 次/分钟冲压、每 2 分钟下线一台车身等硬指标展示精益生产；为少年儿童定制研学路线，把「制造强国」种子种进孩子心里，家文化与企业文化融合。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">「观光车进车间」降低参观门槛且保证安全；用可量化硬指标（12 秒切换/2 分钟下线）讲智造实力比口号有力；把开放日与「研学」绑定吸引员工带娃+社会公众；技术能手现身说法替代领导单向宣讲。</div></details>
      <div class="src">🔗 <a href="https://www.chinatruck.org/news/202507/11_129743.html" target="_blank">chinatruck.org/.../11_129743.html</a></div>
      <div class="note">适用：② 制造型企业「员工家庭+社会公众」双客群开放日，研学路线做青少年科普。</div>
    </div>
"""

new_sec3 = """
    <div class="hl">
      <div class="top"><span class="emoji">🧫</span><h3>和元生物首届「投资者开放日」（CGT 临港基地）</h3><span class="cat">投资者开放日</span><span class="badge r3">高管间</span><span class="badge b1">一手</span></div>
      <p class="val">和元生物（OBiO，细胞与基因治疗 CDMO）首届投资者开放日（公司官网）：2025/12/3 上海临港基地，百余名机构/券商分析师/媒体/行业专家/中小投资者参与。实地探访集团展厅、GMP 车间、「和美」品牌产品体验；创始人董事长兼总经理潘讴东欢迎，副总董秘徐鲁媛系统阐述战略；特邀灼识咨询董事总经理解析全球细胞治疗趋势、东京科学大学博士分享再生医学，高管就行业/业务/经营热点逐一回应，展现治理透明度。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">把开放日当「年度 IR 固定动作」而非一次性；实地看 GMP 车间+产品体验「眼见为实」；创始人+董秘双层出场讲战略；引入第三方行业专家（灼识/高校）提升专业公信力；座谈坦诚高效获认可。</div></details>
      <div class="src">🔗 <a href="https://www.obiosh.com/gongsixinwen/4511" target="_blank">obiosh.com/gongsixinwen/4511</a></div>
      <div class="note">适用：③ 硬科技/生物医药上市公司投资者开放日，第三方专家背书+GMP 实地是亮点。</div>
    </div>

    <div class="hl">
      <div class="top"><span class="emoji">🏭</span><h3>上海电气「我是股东——走进沪市上市公司」</h3><span class="cat">投资者开放日</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
      <p class="val">上海电气携手上交所、申万宏源证券举办「我是股东——走进沪市上市公司」（媒体）：30 余名顶尖投资机构代表及个人股东走进上海汽轮机厂与上海锅炉厂。高端装备展示厅（重型燃气轮机/核电主泵/海上风电）勾勒能源装备史；叶片中心沉浸式体验「数制融合智慧透平生态」；绿色能源实验室实地看富 CO 合成气绿色甲醇装置与电解水制氢。以「主动式」沟通响应证监会 IR 指引，强化股东信任纽带。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">借监管「我是股东」品牌（上交所+券商联合）增公信力；实地进核心制造基地（汽轮机/锅炉厂）而非仅展厅；用「主动式沟通」框架回应监管要求；把开放日嵌入提高上市公司质量三年行动。</div></details>
      <div class="src">🔗 <a href="https://so.html5.qq.com/page/real/search_news?docid=70000021_279692eac6946252" target="_blank">so.html5.qq.com/.../279692eac6946252</a></div>
      <div class="note">适用：③ 上交所「我是股东」系列活动范式，监管+券商+公司三方共办，可复制。</div>
    </div>

    <div class="hl">
      <div class="top"><span class="emoji">🏭</span><h3>格力高入华30周年首启工厂媒体开放日</h3><span class="cat">媒体开放日</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
      <p class="val">格力高（Glico）进入中国三十周年，首次向媒体开放上海奉贤生产基地（财经媒体）：全面展示智能制造（百奇线 AI 视觉检测毫米级、AGV 物流、全流程数字看板）、本土研发（1999 年设首个海外研发中心）、绿色生产（屋顶光伏年发电减碳、RSPO 可持续棕榈油、FSC 包装）。从「在中国生产」到「为中国创造」的本土化可持续发展答卷，制造网络承载信任。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">以「周年里程碑」为契机首启媒体开放日，叙事张力强；用「智能制造-绿色工厂-健康消费」三条线讲 ESG 而非仅产能；本土研发+可持续认证（RSPO/FSC）做差异化信任点；媒体开放日偏「对外透明」而非内部家属，关系档归高管间/对外沟通。</div></details>
      <div class="src">🔗 <a href="https://www.cet.com.cn/wzsy/cyzx/10237166.shtml" target="_blank">cet.com.cn/wzsy/cyzx/10237166.shtml</a></div>
      <div class="note">适用：③ 跨国企业媒体开放日（PR/IR 对外沟通），周年节点+ESG 叙事范式。</div>
    </div>

    <div class="hl">
      <div class="top"><span class="emoji">🏛️</span><h3>成都「蓉城国企开放日·智造未来转型共生」</h3><span class="cat">政府主导开放日</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
      <p class="val">成都市国资委主办、成都产投集团承办「智造未来·转型共生」蓉城国企开放日（四川在线）：近 50 名企业、市民、媒体代表走进「四川省制造业智改数转赋能平台」。6300㎡ 展厅汇聚通威/东方电气/长虹等标杆案例与卡诺普焊接机器人等装备；平台如制造业「分诊台」，汇聚近 200 家服务商为 2600 余家企业「把脉开方」，10 个月办 400 余场公益活动、近万名群众参观。以「国企开放日」打通国资监管-企业-公众沟通。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">由国资委（监管方）主办而非企业自办，公信力最强；把开放日主题锚定「智改数转」区域战略而非单厂宣传；用「分诊台/健身方案」比喻降低理解门槛；公益活动+群众参观让国企透明常态化。</div></details>
      <div class="src">🔗 <a href="https://cbgc.scol.com.cn/news/6553333" target="_blank">cbgc.scol.com.cn/news/6553333</a></div>
      <div class="note">适用：③ 地方政府/国资委主导国企开放日，监管沟通+公众科普双目标，可作政企开放日范式。</div>
    </div>

    <div class="hl">
      <div class="top"><span class="emoji">🛍️</span><h3>中国中免2025年度投资者开放日（三亚免税城）</h3><span class="cat">投资者开放日</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
      <p class="val">中国中免 2025 年度投资者开放日「观潮起 见海阔」（IR 联盟转载）：逾 300 名主权基金/公募/私募/个人投资者参与。大会环节董事总经理、总会计师兼董秘、三亚免税店总经理等就封关政策、三亚国际免税城三期、竞争策略深入交流；现场调研首探三期项目实地及展厅沙盘、一期品牌旗舰店/会员服务区；设投资者专属优惠+代金券+有奖问答增强体验。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">超大场次（300+）投资者开放日，分「大会交流+实地调研」两段；高管层级覆盖总经理/总会计师/董秘/业务总经理；实地看三期项目沙盘「眼见为实」；购物礼遇做体验黏性（非单纯招待）。</div></details>
      <div class="src">🔗 <a href="https://www.irlianmeng.com/IR/index.php/Index/companyNewsListDetail?id=120024&type=4" target="_blank">irlianmeng.com/.../id=120024</a></div>
      <div class="note">适用：③ 消费/免税龙头投资者开放日，大规模+实地+礼遇体验，可抄分段设计。</div>
    </div>
"""

# ---------- HTML 注入 ----------
html = io.open(HTML, encoding="utf-8").read()

# 更新 hero 副标题
html = html.replace(
    "采集于 2026-08-06 ｜ 本轮 enrich 2026-08-07（+9）｜ 六维评估（含关系适配度）｜ 一手/二手标注 ｜ 历史去重 ｜ 受众关系分层（仅②上下级 / ③高管间）",
    "采集于 2026-08-06 ｜ 首轮 enrich 2026-08-07（+9）｜ 二轮补采 2026-08-08（+11）｜ 六维评估（含关系适配度）｜ 一手/二手标注 ｜ 历史去重 ｜ 受众关系分层（仅②上下级 / ③高管间）"
)
# 更新分区计数
html = html.replace('<span class="tag">12 卡</span>', '<span class="tag">18 卡</span>')
html = html.replace('<span class="tag">10 卡</span>', '<span class="tag">15 卡</span>')
# 注入新卡片（sec2 在 ③ 注释前；sec3 在 footer 前）
html = html.replace("  <!-- ============ ③ 领导↔领导 ============ -->", new_sec2 + "  <!-- ============ ③ 领导↔领导 ============ -->")
html = html.replace("  <footer>", new_sec3 + "  <footer>")

io.open(HTML, "w", encoding="utf-8").write(html)
print("HTML updated. sec2=18, sec3=15")

# ---------- index.json 追加 11 条 ----------
entries = [
    {"title":"华丰科技四期「情融华丰·家倍温暖」家属开放日","normKey":"华丰科技四期情融华丰家倍温暖家属开放日","url":"https://huafeng796.com/details.html?id=1955515597372121090","sourceType":"primary","relation":"supervisor","summary":"公司官网：连续四周周五家属开放日，153家庭/277家属；认知→共情→共建四期递进，指纹签到+产线探秘+手工互动，收官切蛋糕仪式"},
    {"title":"景嘉微2025「同心同行·乐享嘉时光」家庭开放日","normKey":"景嘉微2025同心同行乐享嘉时光家庭开放日","url":"https://www.jingjiamicro.com/news/73.html","sourceType":"primary","relation":"supervisor","summary":"公司官网：60余组/近200家属；幸福照片墙+魔术+宣传片+领导致辞+游园会(发电竞速/红星竹编画)+员工食堂收尾"},
    {"title":"安科生物「安科嘉年华·秋日奇遇记」家属开放日","normKey":"安科生物安科嘉年华秋日奇遇记家属开放日","url":"https://ankebio.com/display_2866.html","sourceType":"primary","relation":"supervisor","summary":"公司官网：200余名家属；董事长+执行总裁双层级出场，科学秀+游园会，特设公益义卖助白血病儿童"},
    {"title":"中国电科二十七所「同心筑梦 一路有你」家属开放日","normKey":"中国电科二十七所同心筑梦一路有你家属开放日","url":"https://www.cetc.com.cn/27/335529/335505/2115556/index.html","sourceType":"primary","relation":"supervisor","summary":"央企官网：优秀党员/党务工作者直系亲属受邀；紫鼎广场+智慧农业+无人机联试场+初心宣传片，食堂共餐降层级"},
    {"title":"东方电气「智造零距离·能源科普行」企业开放日","normKey":"东方电气智造零距离能源科普行企业开放日","url":"https://www.dec-ltd.cn/info/1515/12549.htm","sourceType":"primary","relation":"supervisor","summary":"央企官网：170家庭/1000余家属环厂健身跑+智造零距离；劳模工匠家庭日+公众开放日(政府/学校/供方/家属)，大国重器+东汽精神"},
    {"title":"江铃汽车「暑期家庭行」全民开放日（智造+研学）","normKey":"江铃汽车暑期家庭行全民开放日智造研学","url":"https://www.chinatruck.org/news/202507/11_129743.html","sourceType":"secondary","relation":"supervisor","summary":"行业媒体：100+全国访客+员工家庭；观光车进车间(12秒车型切换/2分钟下线)，技术能手讲智造，少儿研学路线"},
    {"title":"和元生物首届「投资者开放日」（CGT 临港基地）","normKey":"和元生物首届投资者开放日cgt临港基地","url":"https://www.obiosh.com/gongsixinwen/4511","sourceType":"primary","relation":"exec","summary":"公司官网：百余名机构/分析师/媒体/中小投资者；GMP车间+产品体验+创始人董事长战略+灼识/高校第三方专家背书"},
    {"title":"上海电气「我是股东——走进沪市上市公司」","normKey":"上海电气我是股东走进沪市上市公司","url":"https://so.html5.qq.com/page/real/search_news?docid=70000021_279692eac6946252","sourceType":"secondary","relation":"exec","summary":"上交所+申万宏源主办；30余投资者进汽轮机厂/锅炉厂，核电主泵/绿色甲醇；主动式沟通响应证监会IR指引"},
    {"title":"格力高入华30周年首启工厂媒体开放日","normKey":"格力高入华30周年首启工厂媒体开放日","url":"https://www.cet.com.cn/wzsy/cyzx/10237166.shtml","sourceType":"secondary","relation":"exec","summary":"财经媒体：首次向媒体开放奉贤工厂；智能制造(AI视觉/AGV)+本土研发+RSPO/FSC绿色生产，周年节点ESG叙事"},
    {"title":"成都「蓉城国企开放日·智造未来转型共生」","normKey":"成都蓉城国企开放日智造未来转型共生","url":"https://cbgc.scol.com.cn/news/6553333","sourceType":"secondary","relation":"exec","summary":"成都市国资委主办；近50名企业/市民/媒体进智改数转赋能平台；分诊台比喻+400余场公益活动打通监管-企业-公众"},
    {"title":"中国中免2025年度投资者开放日（三亚免税城）","normKey":"中国中免2025年度投资者开放日三亚免税城","url":"https://www.irlianmeng.com/IR/index.php/Index/companyNewsListDetail?id=120024&type=4","sourceType":"secondary","relation":"exec","summary":"IR联盟转载：300+投资者；大会交流(总经理/总会计师/董秘)+实地调研三期沙盘，专属优惠+代金券体验黏性"},
]

with io.open(IDX, encoding="utf-8") as f:
    data = json.load(f)
before = len(data)
urls = {e.get("url") for e in data}
added = 0
for e in entries:
    if e["url"] in urls:
        continue
    data.append(e)
    urls.add(e["url"])
    added += 1
with io.open(IDX, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"index.json: {before} -> {len(data)} (added {added})")
