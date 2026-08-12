# -*- coding: utf-8 -*-
# 知识采集自动化 · Open Day 十二轮补采（2026-08-13）
# 追加 13 张新卡到 openday.html sec2 网格 + 更新 index.json + Obsidian 笔记
import os, re, json

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KC = os.path.join(WS, "knowledge-collection")
WALL = os.path.join(KC, "openday", "openday.html")
IDX  = os.path.join(KC, "index.json")
TMP  = os.path.join(KC, "openday", ".run_newcards.tmp.html")

OBS_SUMMARY = "C:/Users/v_yitcai/Documents/Obsidian/知识采集库/素材/openday/OpenDay-开放日-知识卡汇总.md"
OBS_INDEX  = "C:/Users/v_yitcai/Documents/Obsidian/知识采集库/00-知识采集索引.md"
OBS_RUN    = "C:/Users/v_yitcai/Documents/Obsidian/知识采集库/素材/openday/runs/OpenDay-2026-08-13-第十二轮-知识卡.md"

DATE = "2026-08-13"
ROUND = 12

# 全部 ② 上下级（公众/客户/媒体/政府/文博/医院/高校/社区开放日，领导以伙伴/专业姿态开门）
CARDS = [
 dict(emoji="🐧", title="腾讯「企鹅开放日」首次面向公众开放（AI 生活化场景）", cat="产品开放日",
      rel=["r2"], src="secondary", source="toutiao",
      url="https://www.toutiao.com/article/7645699763064554011",
      val="腾讯总部园区（深圳前海大铲湾）首次面向公众开放，以「Hi Buddy，给生活加点 AI」为主题设园区户外公共区域；微信/微信读书/腾讯 SSV/QQ/腾讯新闻/腾讯地图/腾讯理财通/和平精英/无畏契约/腾讯混元/元宝/ima/腾讯文档/腾讯青科实训营/腾讯未保等 16 个产品把 AI 能力从屏幕后带到用户眼前，呈现「大型 AI Buddy 见面会」；「AI 创造市集」让用户三分钟手搓小程序、用心情生成专属 BGM；「企鹅虾友大会」集合 WorkBuddy/腾讯会议/企业微信/Ardot/混元等十余款产品，深度 AI 玩家一站式打卡；这是腾讯「用户为本」理念的集中呈现，总部园区设计之初立意与城市共生、与市民共享。",
      howto="开放日选「城市共生」叙事而非单纯炫技；把产品能力做成可上手互动（手搓小程序/生成 BGM）比演示更打动人；分「大众市集+硬核玩家大会」两档分层接待；用 IP 快闪+限时主题餐饮把科技空间变成好逛好吃的文旅新空间。",
      note="② 互联网/科技企业面向公众的 AI 产品开放日，领导以「伙伴/朋友」姿态零距离对话，技术普惠叙事。"),
 dict(emoji="📡", title="中国联通 2026 国企开放日（北京启动·全国联动）", cat="国企开放日",
      rel=["r2"], src="secondary", source="gmw",
      url="https://tech.gmw.cn/2026-07/17/content_38891990.htm",
      val="以「联通未来 创启新程」为主题的 2026 中国联通国企开放日北京启动，立足「十五五」开局，集中展示新型信息基础设施、前沿数字技术、产业数字化、民生保障等科创成果；校企协同育人成亮点——联合北京邮电大学启动「网络强国 科技报国」大思政课校企联合实践平台；坚持党建引领、全国联动，7-8 月各省级分公司陆续开放智算中心、前沿研发实验室、算力网络枢纽、智慧产业示范场景等硬核科创载体，面向政府、高校师生、产业链伙伴、社会群众及媒体开放。",
      howto="国企开放日=「科创实景+党建引领+生态共建」三位一体；把开放日上升为「大思政课/校企联合平台」做长期产学研协同；全国联动分省特色开放（智算中心/实验室/算力枢纽），用实景替代 PPT；广泛吸纳社会各界意见。",
      note="② 央企科创企业开放日，政府/高校/产业链/媒体多受众分层，科创赋能站位高。"),
 dict(emoji="🛰️", title="中国联通福建省分公司 2026 国企开放日（科创+产学研座谈+非遗）", cat="国企开放日",
      rel=["r2"], src="secondary", source="people",
      url="https://fj.people.com.cn/n2/2026/0717/c181466-41641734.html",
      val="7月15日中国联通福建省分公司举办「联通未来 创启新程」2026 国企开放日，地方政府、协会、高校师生、行业客户及媒体百余人走进联通，沉浸式感受科创魅力；硬核科技·全景赋能展区（科技创新/算力数据/AI/工业互联网/联合创新实验室/低空经济/数智医疗）+ 安全铸盾展区（墨攻 AI 安全智能体，联动 4000+ 安全 SKILL、9000+ 专业工具）+ 数智生活展区（联通魔方/智家/看家/云盘）；与 CCF 福州分部举办「首届 CCF 走进中国联通」座谈会；特别安排非遗漆扇制作体验，传统非遗与现代科技融合。",
      howto="展区按「硬核科技→安全→生活」三递进，用机械狗/AI 智能体等互动环节把抽象能力变直观；座谈会做产学研深入探讨；非遗体验环节柔化科技冷感、拉近距离。",
      note="② 省分公司国企开放日，政/校/客/媒四类受众，互动体验+产学研座谈。"),
 dict(emoji="🏛️", title="五华区翠湖博物馆群落国际博物馆日（六大场馆联动）", cat="博物馆开放日",
      rel=["r2"], src="secondary", source="qq",
      url="https://new.qq.com/rain/a/20260521A079UR00",
      val="第 50 个国际博物馆日（主题「博物馆：联结世界的桥梁」），五华区博物总馆统筹翠湖博物馆群落六大场馆（抗战胜利纪念堂/云南解放纪念馆/云南起义纪念馆/聂耳故居/昆明朱德旧居/昆明胡志明旧居），推出主题展览+互动闯关+文物征集+集章打卡四大板块；六大场馆联动沉浸式闯关（唱主题歌/家风跳房子/历史连连看/心愿卡），集齐碎片兑限量徽章+集章卡；朱德旧居启动红色文物征集（面向社会公开征集）；同步文物保护法宣传。",
      howto="多馆联动做「集章打卡+闯关」把参观变游戏；用「文物征集」把单向展示变公众参与共建；借国际博物馆日节点一次性开放+定制讲解专场。",
      note="② 文博/公共文化机构公众开放日，沉浸互动+公众参与，红色文旅活化。"),
 dict(emoji="🏺", title="榆林市国际博物馆日系列活动（全市联动·数字云桥）", cat="博物馆开放日",
      rel=["r2"], src="secondary", source="toutiao",
      url="https://www.toutiao.com/article/7641189833896886818/",
      val="第 50 个国际博物馆日，榆林市文旅局统筹全市博物馆/纪念馆/文博单位 5.11-5.22 推出多场活动；主场「以桥为脉 博物兴榆」设溯源/边塞/黄河/红色/非遗/未来六大主题展区，集齐六章兑限量徽章+上线「榆林文博数字云桥」24h 云展厅；多馆联动（神木市博物馆明星文物寻宝 NFC 打卡/石峁遗址申遗主题展/民俗博物馆「重回互市」角色行囊+易物游戏+徽章）；「小小讲解员」免费讲解。",
      howto="用「主题展区+集章护照」把全市文博串成可玩动线；上线数字云展厅实现「一次活动全年可看」；角色扮演+易物游戏把历史变可参与；培养「小小讲解员」做青少年浸润。",
      note="② 地市级文博公众开放日，全市联动+数字延展+青少年参与。"),
 dict(emoji="🖼️", title="广州近 80 家博物馆国际博物馆日联动（首开地标+沉浸剧游）", cat="博物馆开放日",
      rel=["r2"], src="secondary", source="nfnews",
      url="https://epaper.nfnews.com/nfdaily/html/202605/19/content_10170740.html",
      val="第 50 个国际博物馆日，广州「无界博物·阅见广州」主会场在春园26号（百年侨园首次面向公众开放）启幕，全市近 80 家博物馆联动；春园26号「修旧如旧」活化+《春园回响》沉浸式剧游让观众化身「剧中人」；南越王博物院古埃及文物+数字艺术、广州艺术博物院「一念敦煌」1:1 石窟复制、广州海事博物馆中非艺术展等重磅大展；公众活动「可参与·可感知·可带走」（DIY 扇子/瓦当手作/粤语 IP 萌态出圈）；首发文博公益卡「鳌游卡」享门票/特展/文创优惠。",
      howto="把历史建筑「首度开放+沉浸剧游」做爆点；多馆联动推重磅大展+可上手手作；发「公益卡」把单次活动变长期引流；用「可带走」文创强化记忆。",
      note="② 城市级文博公众开放日，首开地标+沉浸剧游+全城联动+公益卡。"),
 dict(emoji="🏥", title="滨州市人民医院公众开放日（医师节·社会监督+医患互信）", cat="医院开放日",
      rel=["r2"], src="secondary", source="qq",
      url="https://new.qq.com/rain/a/20260812A03OQT00",
      val="第九个中国医师节前夕，滨州市人民医院组织公众「开放日」，特邀人大代表、政协委员、患者及家属、媒体、群众代表走进医院，实地参观医疗服务流程、便民举措、特色科室（一站式服务中心/e龄通智慧助老/MMC 标准化代谢病管理/医学美容/睡眠医学/中医护理门诊），主动接受社会监督、拉近医患距离；院长等院领导陪同，把意见建议转化为改进服务的具体行动。",
      howto="医院开放日=「领导陪同+实地走流程+特色科室体验+意见收集」；用一站式服务中心/智慧助老等便民场景直观展示；现场记录建议纳入改进清单，把开放变信任建设。",
      note="② 医疗卫生机构公众开放日，领导以开放姿态接受监督、建医患互信。"),
 dict(emoji="🧠", title="北京天坛医院建院 70 周年公众开放日（科研转化+同行协作）", cat="医院开放日",
      rel=["r2"], src="secondary", source="weibo",
      url="https://weibo.com/2640433283/5328971861594399",
      val="首都医科大学附属北京天坛医院建院 70 周年，8月23日举办公众开放日，集中展示医疗服务、运营管理、教育教学、科研创新与成果转化成效；活动含参观院史馆、王忠诚纪念馆、神经影像研究中心、科技成果转化展区、显微神经外科培训中心、门诊大厅、互联网医疗中心、患者综合服务区、国际医疗部等；面向医务界同仁（优先）、预约报名、约 100 人、不收费，加强医疗机构/科研院所/社会组织沟通协作。",
      howto="院庆开放日=「院史+科研+转化+服务」全链条展示；以「同行交流+成果转化」定位吸引专业受众；预约制控规模保质量，把开放日做成行业协作平台。",
      note="② 三甲医院院庆公众/同行开放日，科研转化+同行协作，领导以专业姿态开放。"),
 dict(emoji="🏛️", title="嘉定区 2026 政府开放月（50 项目+护照打卡+开放集市）", cat="政府开放月",
      rel=["r2"], src="primary", source="shanghai.gov",
      url="https://www.shanghai.gov.cn/jdq/20260731/9e5f3bf9d29044488e8c8a98e1dbb01c.html",
      val="嘉定区2026「政府开放月」7月30日启动，主题「奋进十五五，同心向未来」，规模历年最大，50 个开放项目覆盖产业经济/城市建设/民生保障/绿色生态四大专题，全区街镇委办局参与；亮点「政府开放月护照打卡」——含 43 家政务公开主体简介+活动菜单+政务新媒体二维码，集满 15 章获纪念证书；现场「政府开放集市」各单位设点介绍职能和便民服务、面对面答疑、为重大行政决策建言；同期发布「十五五」规划目录清单、上线活动专栏。",
      howto="政府开放月=「专题项目+护照打卡+开放集市」组合；用「护照集章」游戏化驱动市民参与全域开放；把政务公开做成可对话可建言的集市而非单向宣讲；发布规划目录清单+线上专栏延展。",
      note="② 区级政府政务公开开放月，公众参与+政民互动+重大行政决策建言。"),
 dict(emoji="🔄", title="姚圩镇政府开放日（角色互换·实景找茬·现场办结）", cat="政府开放日",
      rel=["r2"], src="primary", source="yushui.gov",
      url="https://www.yushui.gov.cn/yushui/ldxxlyjqqnr/2026-07/17/content_cdbc0ea6770948459ad48185bbf10e04.shtml",
      val="新余市姚圩镇 2026「政府开放日」以「阳光政务·与您同行」为主题，创新「群众当一次政务工作人员、干部当一次办事群众、现场找茬、现场解惑、现场办结」角色互换+实景模拟+问题攻坚：第一阶段政务大厅开放探秘（群众自由参观、窗口一对一随问随答看完整后台流程）；第二阶段 10 名群众换位体验材料初审/录入/自助机操作；干部模拟老年人不会操作等真实痛点；第三阶段「政务找茬」座谈会分三类处置（现场能改/短期能改/长期优化）。",
      howto="用「双向角色互换+实景模拟」破解群众不理解干部、干部不接地气的双向隔阂；干部主动演痛点短板显诚意；「找茬」座谈分三类限时处置（现场/短期/台账）把开放变实效整改。",
      note="② 基层政府开放日，角色互换+实景找茬，政务透明+信任重建范式。"),
 dict(emoji="🧪", title="南开大学元素有机化学国家重点实验室公众开放日", cat="实验室开放日",
      rel=["r2"], src="primary", source="nankai",
      url="https://skleoc.nankai.edu.cn/info/1327/6315.htm",
      val="南开大学元素有机化学全国重点实验室公众开放日（国际博物馆日前后），面向市民、大中小学生，含开幕式+科普报告（显示屏幕进化/动物自己找药吃等）+「探秘化学乐园」趣味实验（魔法冰山/化学彩虹/七彩爆珠/流星雨）+尖端科研仪器开放（高分辨核磁/场发射透射电镜/高分辨质谱/单晶衍射仪，专业老师讲解）；到场赠化学元素主题文创。",
      howto="实验室开放日=「科普报告+趣味实验+尖端仪器开放+文创」四段；把抽象科研变「看得见摸得着」的互动实验；开放大型仪器+专业讲解揭微观世界；文创周边强化参与记忆与传播。",
      note="② 高校国家重点实验室公众开放日，科学家精神+青少年科普，教授以导师姿态开放。"),
 dict(emoji="🔧", title="哈工大材料焊接全国重点实验室开放日（科技周·大国工匠叙事）", cat="实验室开放日",
      rel=["r2"], src="primary", source="hit",
      url="https://mse.hit.edu.cn/2026/0602/c16847a393278/page.htm",
      val="哈尔滨工业大学材料结构精密焊接与连接全国重点实验室响应全国科技活动周，6月6日开展面向社会「实验室开放日」，主题「奋进十五五 科技谱新篇」；含焊接实验室科技展览馆（党领导下焊接科技强国富民之路）+ 科普讲座（上午/下午各一场）+ 焊接新技术新成果实物/照片/视频/实验室参观；面向大学生/高中生/中小学生/普通市民，10 人以上团体预约，搭建科技工作者与青少年交流平台。",
      howto="实验室开放日=「科技展览馆+科普讲座+成果参观」；用「大国工匠/强国建设」叙事串联科研与家国情怀；分上午下午两场同内容便利市民；团体预约控规模保讲解质量。",
      note="② 高校工科国家重点实验室公众开放日，科技周+青少年科创热情，教授专业开放。"),
 dict(emoji="🏘️", title="石牌岭社区「公共空间开放日」暨端午主题活动（居民共建）", cat="社区开放日",
      rel=["r2"], src="secondary", source="hbgdby",
      url="http://www.hbgdby.cn/shequchuanzhen/955.html",
      val="武汉市武昌区石牌岭社区联合湖北广播电视报，在全新升级的社区党群服务中心举办「岭聚同心粽飘香」公共空间开放日暨端午主题活动，230 余名居民/志愿者/共建单位/非遗传承人参与，见证治理阵地升级后首次大型开放；依托「五岭」共治品牌（议治岭/聚能岭/便邻岭/共享岭/同心岭），融合非遗剪纸体验（60 余幅）+ 新阵地功能参观（舞蹈室/儿童活动区/康养区，居民代表任临时讲解员）+ 端午包粽（近 500 个）+ 收集建议 30 余条；阵地面积扩展近 40%，当天全面开放。",
      howto="社区开放日=「品牌解读+非遗体验+阵地参观+民俗包粽+建议收集」；用「居民任临时讲解员」把被动参观变主动共建；边开放边收集改进建议（30+ 条）体现治理闭环；升级阵地首开即全面开放聚人气。",
      note="② 社区公共空间/党群服务中心开放日，居民共建+邻里融合，领导/社区以伙伴姿态开门。"),
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

    # 2) 更新 sec2 标签计数 33 -> 46
    html=html.replace('    <span class="tag">33 卡</span>', '    <span class="tag">46 卡</span>', 1)

    # 3) 更新 hero p（追加十二轮说明）
    hero_p_start=html.index('<div class="hero">')
    p_start=html.index('<p>', hero_p_start)
    p_end=html.index('</p>', p_start)
    hero_note='｜ 十二轮补采 2026-08-13(+13：博物馆/纪念馆公众开放日+医院公众开放日+政府开放月/政务公开+高校实验室开放日+社区公共空间开放日+腾讯企鹅开放日)'
    html=html[:p_end]+hero_note+html[p_end:]

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

    # 6) Obsidian 汇总笔记更新
    summ=open(OBS_SUMMARY,encoding="utf-8").read()
    summ=summ.replace("共 38 张","共 51 张")
    summ=summ.replace("**38 卡**","**51 卡**").replace("一手 16 + 二手 22","一手 20 + 二手 31")
    summ=summ.replace("②上下级 33 卡 / ③高管间 5 卡","②上下级 46 卡 / ③高管间 5 卡")
    summ=summ.replace("**38 卡**，已剔除平级","**51 卡**，已剔除平级")
    # 追加 r12 独立页链接
    summ=summ.replace(
      "- 当轮独立页（第十一轮）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/runs/openday-2026-08-12-r11.html",
      "- 当轮独立页（第十一轮）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/runs/openday-2026-08-12-r11.html\n- 当轮独立页（第十二轮）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/runs/openday-2026-08-13-r12.html")
    # 在卡片总表末尾追加 13 行（在「## 卡片墙（HTML 交互版）」之前）
    rows="".join(
        f"| {c['title']}（openday.html） | 4 | {'一手' if c['src']=='primary' else '二手'} | ②上下级 | {c['val'][:60]}…\n"
        for c in CARDS)
    summ=summ.replace("## 卡片墙（HTML 交互版）", rows+"\n## 卡片墙（HTML 交互版）")
    # 适用&备注追加本轮说明
    summ=summ.replace("硬排除：家庭日/家属开放日、投资者/资本市场/IR/证监局开放日（非 HRBP 企业文化活动向）。",
      "硬排除：家庭日/家属开放日、投资者/资本市场/IR/证监局开放日（非 HRBP 企业文化活动向）。十二轮（2026-08-13）新增聚焦「博物馆/纪念馆公众开放日」（五华翠湖群落/榆林/广州近 80 家联动，集章打卡+沉浸剧游+数字云桥）、「医院公众开放日」（滨州市人民医院社会监督+医患互信/天坛医院院庆科研转化+同行协作）、「政府开放月/政务公开」（嘉定 50 项目+护照打卡+开放集市/姚圩镇角色互换+实景找茬）、「高校实验室开放日」（南开元素有机化学/哈工大材料焊接国家重点实验室，科普报告+趣味实验+尖端仪器开放）、「社区公共空间开放日」（石牌岭党群服务中心居民共建）、「腾讯企鹅开放日」（总部园区首度公众开放+AI 产品市集）。")
    open(OBS_SUMMARY,"w",encoding="utf-8").write(summ)
    print(f"summary note updated: {OBS_SUMMARY}")

    # 7) 00-索引更新
    idx0=open(OBS_INDEX,encoding="utf-8").read()
    # header 行追加十二轮
    idx0=idx0.replace(
      "｜ 2026-08-12 十一轮补采 +12（环保设施/政法/电力/媒体/消防/客户开放日向）",
      "｜ 2026-08-12 十一轮补采 +12（环保设施/政法/电力/媒体/消防/客户开放日向）｜ 2026-08-13 十二轮补采 +13（博物馆/纪念馆公众开放日+医院公众开放日+政府开放月/政务公开+高校实验室开放日+社区公共空间开放日+腾讯企鹅开放日）")
    idx0=idx0.replace("**38 卡**，已剔除平级","**51 卡**，已剔除平级").replace("一手 16 + 二手 22","一手 20 + 二手 31")
    idx0=idx0.replace("②上下级(客户/媒体/品牌/公众开放日/环保设施/政法/电力/消防/客户...) 33 卡 / ③高管间(媒体/央企品牌...) 5 卡",
                      "②上下级 46 卡 / ③高管间 5 卡")
    # 找 Open Day 卡片表末尾追加 13 行
    s=idx0.find("## 主题：Open Day")
    tstart=idx0.find("| 卡 |", s)
    # 表尾：从 tstart 起找最后一个以 | 开头的行
    seg=idx0[tstart:]
    lines=seg.split("\n")
    last=0
    for k,ln in enumerate(lines):
        if ln.strip().startswith("|"): last=k
    # 在 last 行之后插入
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
title: Open Day 开放日 第十二轮 知识卡
tags: [知识采集, Open Day 开放日, 自动化采集, 轮次]
date: 2026-08-13
type: 自动化采集
round: 12
---

# Open Day 开放日 · 第十二轮补采知识卡（2026-08-13）

> 本轮为「Open Day 开放日」主题第 12 轮自动补采，新增 **13 张**知识卡（②上下级 13；一手 4 / 二手 9）。
> ⚠️ 硬过滤已生效：家庭日/家属开放日、投资者/资本市场/IR/证监局开放日不采。

## 独立页（GitHub Pages · 公开）
https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/runs/openday-2026-08-13-r12.html

## 本机路径
knowledge-collection/openday/runs/openday-2026-08-13-r12.html

## 累计总索引（卡片墙）
https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday.html

## 本轮卡片表（13 张）
| # | 卡 | 一手/二手 | 适用关系 | 来源 |
|---|---|---|---|---|
{tbl}
## 本轮聚焦点
- 博物馆/纪念馆公众开放日：五华翠湖博物馆群落（六大场馆联动+集章闯关+文物征集）、榆林（全市联动+数字云桥+小小讲解员）、广州（近 80 家联动+首开地标沉浸剧游+公益卡）。
- 医院公众开放日：滨州市人民医院（医师节社会监督+医患互信，领导陪同走流程）、天坛医院（院庆 70 周年+科研转化+同行协作）。
- 政府开放月/政务公开：嘉定（50 项目+护照打卡+开放集市+重大行政决策建言）、姚圩镇（角色互换+实景找茬+现场办结，破解双向隔阂）。
- 高校实验室开放日：南开元素有机化学、哈工大材料焊接（国家重点实验室，科普报告+趣味实验+尖端仪器开放+大国工匠叙事）。
- 社区公共空间开放日：石牌岭社区党群服务中心（居民任临时讲解员+非遗+建议收集 30+ 条）。
- 腾讯企鹅开放日：总部园区首度公众开放+16 产品 AI 市集+硬核玩家大会，互联网企业面向公众的 AI 产品开放日范式。
"""
    open(OBS_RUN,"w",encoding="utf-8").write(md)
    print(f"run note created: {OBS_RUN}")
    print("DONE enrich")

if __name__=="__main__":
    main()
