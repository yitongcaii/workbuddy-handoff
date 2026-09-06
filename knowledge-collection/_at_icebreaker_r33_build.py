# -*- coding: utf-8 -*-
"""
破冰 r33 (2026-09-06) 自动化补采构建脚本
- 6 张新卡插入 icebreaker.html 累计墙（③×3 入 sec3 / ②×3 入 sec2）
- 写 .run_newcards.tmp.html
- 更新 index.json（+6）
- 更新 Obsidian 汇总笔记 / 00-索引 / 本轮独立笔记
"""
import os, re, json

KC = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(KC, "icebreaker", "icebreaker.html")
TMP = os.path.join(KC, "icebreaker", ".run_newcards.tmp.html")
IDX = os.path.join(KC, "index.json")
OB_ROOT = r"C:/Users/v_yitcai/Documents/Obsidian/活动/知识采集库"
SUM = os.path.join(OB_ROOT, "素材", "icebreaker", "破冰-知识卡汇总.md")
IDX00 = os.path.join(OB_ROOT, "00-知识采集索引.md")
RUN_NOTE = os.path.join(OB_ROOT, "素材", "icebreaker", "runs", "破冰-2026-09-06-第三十三轮-知识卡.md")

def card(emoji, title, cat, rel, src_t, url, disp, val, exec_, note):
    badge_rel = {"r3": "高管间", "r2": "上下级"}[rel]
    badge_src = {"b1": "一手", "b2": "二手"}[src_t]
    return f'''    <div class="hl">
      <div class="top"><span class="emoji">{emoji}</span><h3>{title}</h3><span class="cat">{cat}</span><span class="badge {rel}">{badge_rel}</span><span class="badge {src_t}">{badge_src}</span></div>
      <p class="val">{val}</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">{exec_}</div></details>
      <div class="src">🔗 <a href="{url}" target="_blank">{disp}</a></div>
      <div class="note">{note}</div>
    </div>'''

# ---- 6 张新卡 ----
cards3 = [
    card("🎯", "SOAR 框架·欣赏式探询战略共创（SWOT 的积极替代）", "战略共创", "r3", "b2",
         "https://workshopweaver.com/facilitation-methods/soar-analysis",
         "workshopweaver.com/facilitation-methods/soar-analysis",
         "SOAR（Strengths/Opportunities/Aspirations/Results）由 Stavros 等基于 Appreciative Inquiry 提出，是 SWOT 的积极替代——不花一半篇幅讲弱点/威胁，而从「什么在起作用」出发把组织能量导向可能性。高管务虚/战略 offsite 用 1-2h：①Strengths（我们最擅长/最自豪？用峰值体验提示「团队最好的时刻靠什么」）②Opportunities（外部趋势/未满足需求我们独特可抓）③Aspirations（3-5 年想成为谁、客户与社区的成功样貌）④Results（每个抱负落成 1-2 个可观测结果+日期，要领先指标非滞后）。产出比 SWOT 更有承诺感的战略对话与真想执行的行动计划；尤适士气低/变革阻力高/需重连使命感时。",
         "高管务虚用 SOAR 替 SWOT——先设「欣赏式框架」（说明建在优势上而非列问题）防有人读成天真乐观而脱钩；Strengths 用峰值体验提示、Opportunities 推具体（哪个客户/趋势/窗口）、Aspirations 给足时间（最易被草草带过）、Results 逼领先指标；20+ 人分并行 breakout 再 plenary 综合；dot-vote 前 2-3 优先级并当场定 owner+下一步。",
         "适用：③ 高管团队战略务虚/Offsite——SOAR（欣赏式探询·Strengths/Opportunities/Aspirations/Results）替 SWOT，从「什么在起作用」出发导向可能性而非缺陷，1-2h 产出更有承诺感的行动计划，尤适低士气/高变革阻力/需重连使命（高管间，引导方法二手）。"),
    card("🔄", "齐鲁云商工作务虚会·「话题轮换」主持机制（山东能源 · 一手）", "务虚会机制", "r3", "b1",
         "https://sdnyxcl.shandong-energy.com/232085/232093/2025/01/36936465.html",
         "sdnyxcl.shandong-energy.com/232085/232093/2025/01/36936465.html",
         "山东能源集团新材料板块齐鲁云商召开工作务虚会，董事长王德龙定调「以虚务实、虚实结合」——务虚从思维/理念/方法层面谋未来，又要突出「实」统一思想理清目标。核心机制「话题轮换」：针对制约发展的瓶颈，一名参会人员主持两个话题、其他人对该话题思考解答，让思想碰撞、避免泛泛而谈；议题如「公司未来发展机会点」「如何建开放包容团队文化激发凝聚力」。务虚不止高层，各部门务虚同样热烈，员工立足岗位摆矛盾、对标对表中理清思路；自下而上+自上而下系列会统一思路、凝心聚力。",
         "高管/中层务虚会设「话题轮换」机制——每话题一人主持、余人作答，逼深度思考且有着力点；高层务虚与基层务虚并行，让员工不回避不掩饰摆突出问题；以思想大讨论推动工作大提升，为实践方向供支撑。",
         "适用：③ 企业内部务虚会（高层+基层双向）——齐鲁云商「话题轮换」主持机制（一人主持两话题、余人思考解答）把务虚从空谈变思想碰撞，虚实结合统一思路（国企/新材料板块官方新闻=一手）。"),
    card("🎨", "渡远集团年中战略务虚·红色教育 +「愿景画布」共创（渡远 · 一手）", "战略务虚", "r3", "b1",
         "https://doofar.com/article/5642090977305748.html",
         "doofar.com/article/5642090977305748.html",
         "渡远集团 40 余人管理团队聚福建龙岩古田，以「扎根·共创·致远」开 2025 年中战略暨文化宣导会：上午红色教育（古田会议旧址/敬献花篮）深扎根；下午战略研讨（各部门年中汇报、董事长强调长期主义、发布 2025-2028 战略规划）；晚间「愿景画布」共创将气氛推向高潮——管理人员打破部门壁垒，围绕战略落地多轮深度研讨，视觉化呈现集体智慧，绘出通往可持续未来的实施蓝图；次日体验式学习（文化连连看/密码传送/鼓动人心/动力圈）提升凝聚力，复盘转行动计划。创新性把红色教育+战略研讨+文化宣导+团队建设有机融合。",
         "高管战略务虚可叠「红色/初心教育+战略发布+愿景画布共创」三段：白天战略汇报与规划发布，晚间用视觉化画布让管理层跨壁垒共创实施蓝图，次日体验式活动固凝聚、复盘落计划；把务虚从「听报告」变「共同画未来」。",
         "适用：③ 企业年中/年度战略务虚会——渡远集团古田务虚把红色教育+战略研讨+「愿景画布」跨壁垒共创+体验式团建融合，管理层共绘实施蓝图（企业官方新闻=一手）。"),
]

cards2 = [
    card("📩", "把价值观变行为·Leadership Envelopes + Run Your Favorite Manager + Leadership Pizza", "管理赋能", "r2", "b2",
         "https://flobquest.com/?p=188",
         "flobquest.com/?p=188",
         "flobquest 给一线经理的落地法：①Leadership Envelopes——给每人一张卡写「本周想试的一个具体行为」，把抽象价值观变可行动项，会后追踪；②Run Your Favorite Manager——crowdsource 团队对「好/差 manager」的 do's &amp; don'ts，汇成团队共守清单；③Leadership Pizza——一页式自评（把领导力的「一片」按维度打分找缺口）。核心理念：leader 的微观行为（怎么听/派活/给反馈）比幻灯片更定规范，参与式练习+会后跟进让原则变日常；leader 要以平等身份参与、示弱与学习。",
         "经理带团队用三件套——Leadership Envelopes（每人写本周一试的行为卡、会后跟进）/Run Your Favorite Manager（众筹上下级 do's&amp;don'ts 成共守清单）/Leadership Pizza（一页自评找领导力缺口）；leader 以身作则参与、把抽象价值变具体动作并追踪。",
         "适用：② 经理/主管带团队——把抽象领导价值观落成可行动行为卡（Leadership Envelopes）、众筹上下级对好/差 manager 的 do's&amp;don'ts（Run Your Favorite Manager）、一页自评找缺口（Leadership Pizza），leader 以身作则参与（管理实战博客二手）。"),
    card("🤝", "国企新员工迎新·破冰 + 传帮带 + 师徒结对长效机制（中铁水利 · 一手）", "新人融入", "r2", "b1",
         "https://slt.jiangxi.gov.cn/jxsslt/jczc655/pc/content/content_1954812727649976320.html",
         "slt.jiangxi.gov.cn/jxsslt/jczc655/pc/content/content_1954812727649976320.html",
         "中铁水利设计集团 2025「凝'新'聚力 共赴山河」新职工入职教育：迎新篮球友谊赛+活力破冰迅速拉近距离；人力/技术质量部讲制度与体系、课堂测试答疑；企业文化宣贯+院史展馆参观传承「开路先锋」精神；赴峡江水利枢纽实地探访感悟工匠精神。新职工座谈上集团领导提五点期望——学重力坝的「扎实牢固」（扎实理论）/拱坝的「融合协作」（融入团队跨专业协作）/土石坝的「严谨细致」（每图每参数载责任）/全生命周期理念。同类：送变电成眉线项目部新员工与导师签「师徒带教协议」建长效成长机制；山推股份新老员工传经送宝。",
         "新员工迎新用「文体破冰→制度文化宣贯→实地探访→新老座谈（传经送宝）→师徒结对/领导五点期望」五步，把破冰融进长期成长机制而非一次性活动；用「师徒带教协议」把传帮带制度化、建长效。",
         "适用：② 国企/制造业新员工迎新与融入——中铁水利「破冰+制度文化+实地探访+新老座谈+师徒结对」五步把传帮带长效化，领导以「坝体精神」类比提期望（江西省水利厅官方=一手；送变电/山推同类案例）。"),
    card("💬", "福华集团「讲真话」恳谈会·领导班子 + 中层 + 员工代表跨级对话（福华 · 一手）", "跨级对话", "r2", "b1",
         "https://www.fhtdchem.com/detail?id=534&newsType=NEWS_TYPE_NEWSLETTER",
         "fhtdchem.com/detail?id=534&newsType=NEWS_TYPE_NEWSLETTER",
         "福华化学举办「打造幸福企业 共享幸福人生」恳谈会，董事局主席张华、领导班子、中层管理、入职满 20 年员工与大学生代表约 100 人齐聚。下午趣味团建（意大利面塔搭建）热身；随后「讲真话，听真话，打造幸福团队」讨论会，各层级代表结合岗位谈「幸福企业」内涵与「如何讲真话」；现场涌现「容错机制」「越级提出问题」「消灭部门墙」「开设向上沟通渠道」「加强薪酬体系建设」等建议，各组记录并分享成果。把「敢听真话、能听真话、想听真话」氛围制度化。",
         "跨级恳谈会用「团建热身→分层代表发言→各组提炼建议并分享」结构；领导层主动邀「讲真话」，把容错/越级提问题/消灭部门墙/向上沟通渠道等一线建议落到机制；让各层级（高管/中层/员工）同场对话破除信息过滤。",
         "适用：② 跨级对话/员工恳谈会——福华集团「讲真话听真话」恳谈（董事局主席+班子+中层+员工代表约 100 人），团建热身+分层发言+建议共享，把容错/越级提问题/消灭部门墙制度化（企业官方新闻=一手）。"),
]

# ===== 1. 插入累计墙 =====
html = open(WALL, encoding="utf-8").read()
insert3 = "\n".join(cards3) + "\n"
insert2 = "\n".join(cards2) + "\n"

def insert_after_grid(h, sec_class, block):
    marker = f'<div class="sec {sec_class}">'
    i = h.find(marker)
    assert i != -1, f"missing {sec_class}"
    j = h.find('<div class="grid">', i)
    assert j != -1, f"missing grid for {sec_class}"
    end = j + len('<div class="grid">')
    return h[:end] + "\n" + block + h[end:]

html = insert_after_grid(html, "sec3", insert3)
html = insert_after_grid(html, "sec2", insert2)

# 重新计数
i3 = html.find('<div class="sec sec3">')
i2 = html.find('<div class="sec sec2">')
sec3_count = html[i3:i2].count('<div class="hl">')
sec2_count = html[i2:].count('<div class="hl">')
print("sec3_count", sec3_count, "sec2_count", sec2_count, "total", sec3_count + sec2_count)

html = re.sub(r'(<div class="sec sec3">[\s\S]*?<span class="tag">)\d+ 卡',
              lambda m: m.group(1) + f"{sec3_count} 卡", html, count=1)
html = re.sub(r'(<div class="sec sec2">[\s\S]*?<span class="tag">)\d+ 卡',
              lambda m: m.group(1) + f"{sec2_count} 卡", html, count=1)

# hero 插入 r33 主线
relbar = '<div class="relbar">'
ri = html.find(relbar)
hero_p = ('    <p style="margin-top:8px">本轮（三十三轮 2026-09-06）主线：SOAR 欣赏式探询战略共创(替 SWOT)（③）；'
          '齐鲁云商「话题轮换」务虚机制、渡远集团古田务虚+愿景画布跨壁垒共创（③ 一手）；'
          '把领导价值观落成行为卡+众筹上下级 do\'s&don\'ts+一页自评（②）；'
          '国企新员工迎新破冰+传帮带+师徒结对长效机制（② 一手）；'
          '福华「讲真话」跨级恳谈(容错/越级提问题/消灭部门墙)（② 一手）。</p>\n')
html = html[:ri] + hero_p + html[ri:]
open(WALL, "w", encoding="utf-8").write(html)

# ===== 2. .run_newcards.tmp.html =====
open(TMP, "w", encoding="utf-8").write("\n".join(cards3 + cards2) + "\n")

# ===== 3. index.json =====
data = json.load(open(IDX, encoding="utf-8"))
def nk(s): return re.sub(r'\s+', '', s)
new_entries = [
    {"title": "SOAR 框架·欣赏式探询战略共创（SWOT 的积极替代）",
     "normKey": nk("SOAR框架欣赏式探询战略共创SWOT的积极替代"),
     "url": "https://workshopweaver.com/facilitation-methods/soar-analysis",
     "sourceType": "secondary", "relation": "exec",
     "summary": "SOAR(Strengths/Opportunities/Aspirations/Results)基于欣赏式探询,是SWOT积极替代:从'什么在起作用'出发导向可能性;高管务虚1-2h四步(峰值体验提示优势/具体机会/给足抱负的Aspirations/领先指标Results),产出比SWOT更有承诺感的行动计划",
     "topic": "icebreaker"},
    {"title": "齐鲁云商工作务虚会·「话题轮换」主持机制（山东能源 · 一手）",
     "normKey": nk("齐鲁云商务虚会话题轮换主持机制山东能源一手"),
     "url": "https://sdnyxcl.shandong-energy.com/232085/232093/2025/01/36936465.html",
     "sourceType": "primary", "relation": "exec",
     "summary": "齐鲁云商务虚会董事长定调'以虚务实、虚实结合';核心'话题轮换'机制:一人主持两话题、余人思考解答,逼深度思考避空谈;高层+基层务虚并行,自下而上+自上而下统一思路凝心聚力",
     "topic": "icebreaker"},
    {"title": "渡远集团年中战略务虚·红色教育 +「愿景画布」共创（渡远 · 一手）",
     "normKey": nk("渡远集团年中战略务虚红色教育愿景画布共创渡远一手"),
     "url": "https://doofar.com/article/5642090977305748.html",
     "sourceType": "primary", "relation": "exec",
     "summary": "渡远集团40余人古田务虚:红色教育+战略研讨+晚间'愿景画布'跨壁垒共创(视觉化集体智慧绘实施蓝图)+次日体验式团建固凝聚;把红色教育/战略/文化/团建有机融合",
     "topic": "icebreaker"},
    {"title": "把价值观变行为·Leadership Envelopes + Run Your Favorite Manager + Leadership Pizza",
     "normKey": nk("把价值观变行为LeadershipEnvelopesRunYourFavoriteManagerLeadershipPizza"),
     "url": "https://flobquest.com/?p=188",
     "sourceType": "secondary", "relation": "supervisor",
     "summary": "一线经理落地三件套:Leadership Envelopes(每人写本周试的行为卡会后追踪)/Run Your Favorite Manager(众筹上下级好差manager的do's&don'ts成共守清单)/Leadership Pizza(一页自评找领导力缺口);leader以身作则参与",
     "topic": "icebreaker"},
    {"title": "国企新员工迎新·破冰 + 传帮带 + 师徒结对长效机制（中铁水利 · 一手）",
     "normKey": nk("国企新员工迎新破冰传帮带师徒结对长效机制中铁水利一手"),
     "url": "https://slt.jiangxi.gov.cn/jxsslt/jczc655/pc/content/content_1954812727649976320.html",
     "sourceType": "primary", "relation": "supervisor",
     "summary": "中铁水利新员工入职教育五步:文体破冰→制度文化宣贯→实地探访→新老座谈(传经送宝)→师徒结对/领导以'坝体精神'提五点期望;送变电签'师徒带教协议'、山推新老传经,把传帮带长效化",
     "topic": "icebreaker"},
    {"title": "福华集团「讲真话」恳谈会·领导班子 + 中层 + 员工代表跨级对话（福华 · 一手）",
     "normKey": nk("福华集团讲真话恳谈会领导班子中层员工代表跨级对话福华一手"),
     "url": "https://www.fhtdchem.com/detail?id=534&newsType=NEWS_TYPE_NEWSLETTER",
     "sourceType": "primary", "relation": "supervisor",
     "summary": "福华化学'讲真话听真话'恳谈:董事局主席+班子+中层+员工代表约100人,团建热身+分层发言+建议共享;现场涌现容错机制/越级提问题/消灭部门墙/向上沟通渠道,把敢听真话氛围制度化",
     "topic": "icebreaker"},
]
before = len(data)
data.extend(new_entries)
assert len(data) == before + 6
json.dump(data, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("index.json entries:", before, "->", len(data))

# ===== 4. Obsidian 汇总笔记 =====
sum_txt = open(SUM, encoding="utf-8").read()
sum_txt = sum_txt.replace("date: 2026-09-05", "date: 2026-09-06")
# 增量页链接改 r33
sum_txt = sum_txt.replace(
    "**本轮增量页（2026-09-05 · 三十二轮 R32）**：[icebreaker-2026-09-05-r32.html · GitHub Pages](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/runs/icebreaker-2026-09-05-r32.html)  \n**本机源**：`knowledge-collection/icebreaker/runs/icebreaker-2026-09-05-r32.html`",
    "**本轮增量页（2026-09-06 · 三十三轮 R33）**：[icebreaker-2026-09-06-r33.html · GitHub Pages](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/runs/icebreaker-2026-09-06-r33.html)  \n**本机源**：`knowledge-collection/icebreaker/runs/icebreaker-2026-09-06-r33.html`")
# r33 blockquote 插入到 r32 blockquote 之后
r32_bq = "> 三十二轮补采 +6（2026-09-05，②×3/③×3）：高管非语言沟通·Silent Leadership Challenge+Speed Negotiation Rounds（③）；高管期望映射+「没说出口的话」务虚开场（③）；高管务虚 29 法五分类框架·危机模拟/遗产地图/「如果是X会怎么做」（③）；走动式 Speed Date 破冰·欣赏式探询步行 1:1（②）；管理者同侪教练圈·GROW 模型轮值 coachee（②）；社交化学习·同侪圈+岗位影子 Mars/McCormick 实证（②）"
r33_bq = ("> 三十三轮补采 +6（2026-09-06，②×3/③×3）：SOAR 欣赏式探询战略共创（替 SWOT）（③）；"
          "齐鲁云商「话题轮换」务虚机制、渡远集团古田务虚+愿景画布跨壁垒共创（③ 一手）；"
          "把领导价值观落成行为卡+众筹上下级 do's&don'ts+一页自评（②）；"
          "国企新员工迎新破冰+传帮带+师徒结对长效机制（② 一手）；"
          "福华「讲真话」跨级恳谈（容错/越级提问题/消灭部门墙）（② 一手）。")
assert r32_bq in sum_txt, "r32 blockquote not found"
sum_txt = sum_txt.replace(r32_bq, r32_bq + "\n" + r33_bq, 1)
# 总表头 256 -> 294
sum_txt = sum_txt.replace("## 卡片总表（256 卡", "## 卡片总表（294 卡")
sum_txt = sum_txt.replace("本轮 +9，R27/R28 轮次待回填", "本轮 +6（三十三轮 2026-09-06）")
# 轮次 20260906 段插入到 "## 卡片总表" 之前
round_sec = '''## 轮次 20260906（+6）
| # | 卡片 | 关系档 | 一手/二手 | 核心要点 |
|---|---|---|---|---|
| 1 | SOAR 框架·欣赏式探询战略共创（SWOT 的积极替代） | ③高管间 | 二手 | SOAR(Strengths/Opportunities/Aspirations/Results)基于欣赏式探询,是SWOT积极替代:从'什么在起作用'出发;高管务虚1-2h四步(峰值体验提示优势/具体机会/给足抱负的Aspirations/领先指标Results) |
| 2 | 齐鲁云商工作务虚会·「话题轮换」主持机制（山东能源 · 一手） | ③高管间 | 一手 | 齐鲁云商'以虚务实、虚实结合';'话题轮换'一人主持两话题余人思考解答,逼深度思考避空谈;高层+基层务虚并行统一思路 |
| 3 | 渡远集团年中战略务虚·红色教育 +「愿景画布」共创（渡远 · 一手） | ③高管间 | 一手 | 渡远40余人古田务虚:红色教育+战略研讨+晚间'愿景画布'跨壁垒共创+次日体验式团建,把红色/战略/文化/团建融合 |
| 4 | 把价值观变行为·Leadership Envelopes + Run Your Favorite Manager + Leadership Pizza | ②上下级 | 二手 | 一线经理三件套:行为卡(Leadership Envelopes)/众筹上下级do's&don'ts(Run Your Favorite Manager)/一页自评(Leadership Pizza);leader以身作则 |
| 5 | 国企新员工迎新·破冰 + 传帮带 + 师徒结对长效机制（中铁水利 · 一手） | ②上下级 | 一手 | 中铁水利五步(文体破冰→制度文化→实地探访→新老座谈→师徒结对);送变电签'师徒带教协议'、山推传经,传帮带长效化 |
| 6 | 福华集团「讲真话」恳谈会·领导班子 + 中层 + 员工代表跨级对话（福华 · 一手） | ②上下级 | 一手 | 福华'讲真话听真话'恳谈(主席+班子+中层+员工约100人):团建热身+分层发言+建议共享,容错/越级提问题/消灭部门墙制度化 |

'''
assert "## 卡片总表" in sum_txt
sum_txt = sum_txt.replace("## 卡片总表", round_sec + "## 卡片总表", 1)
# 末尾总表追加 6 行
tail_rows = '''
| 289 | SOAR 框架·欣赏式探询战略共创（SWOT 的积极替代） | ③高管间 | 二手 | SOAR(Strengths/Opportunities/Aspirations/Results)基于欣赏式探询,是SWOT积极替代:从'什么在起作用'出发导向可能性;高管务虚1-2h四步产出更有承诺感的行动计划 |
| 290 | 齐鲁云商工作务虚会·「话题轮换」主持机制（山东能源 · 一手） | ③高管间 | 一手 | 齐鲁云商'以虚务实、虚实结合';'话题轮换'一人主持两话题余人思考解答,逼深度思考避空谈;高层+基层务虚并行 |
| 291 | 渡远集团年中战略务虚·红色教育 +「愿景画布」共创（渡远 · 一手） | ③高管间 | 一手 | 渡远40余人古田务虚:红色教育+战略研讨+晚间'愿景画布'跨壁垒共创+次日体验式团建融合 |
| 292 | 把价值观变行为·Leadership Envelopes + Run Your Favorite Manager + Leadership Pizza | ②上下级 | 二手 | 一线经理三件套:行为卡/众筹上下级do's&don'ts/一页自评;leader以身作则参与把抽象价值变具体动作 |
| 293 | 国企新员工迎新·破冰 + 传帮带 + 师徒结对长效机制（中铁水利 · 一手） | ②上下级 | 一手 | 中铁水利五步把传帮带长效化,领导以'坝体精神'类比提期望;送变电/山推同类案例 |
| 294 | 福华集团「讲真话」恳谈会·领导班子 + 中层 + 员工代表跨级对话（福华 · 一手） | ②上下级 | 一手 | 福华'讲真话听真话'恳谈(约100人):团建热身+分层发言+建议共享,容错/越级提问题/消灭部门墙制度化 |
'''
sum_txt = sum_txt.rstrip("\n") + "\n" + tail_rows
open(SUM, "w", encoding="utf-8").write(sum_txt)
print("summary note updated")

# ===== 5. 00-索引 追加 6 行 =====
idx00 = open(IDX00, encoding="utf-8").read()
rows = [
    "| SOAR 框架·欣赏式探询战略共创（SWOT 的积极替代）（icebreaker.html） | 4 | 二手 | ③高管间 | SOAR(Strengths/Opportunities/Aspirations/Results)基于欣赏式探询,是SWOT积极替代:从'什么在起作用'出发;高管务虚1-2h四步产出更有承诺感的行动计划 |",
    "| 齐鲁云商工作务虚会·「话题轮换」主持机制（山东能源 · 一手）（icebreaker.html） | 4 | 一手 | ③高管间 | 齐鲁云商'以虚务实、虚实结合';'话题轮换'一人主持两话题余人思考解答,逼深度思考避空谈;高层+基层务虚并行 |",
    "| 渡远集团年中战略务虚·红色教育 +「愿景画布」共创（渡远 · 一手）（icebreaker.html） | 4 | 一手 | ③高管间 | 渡远40余人古田务虚:红色教育+战略研讨+晚间'愿景画布'跨壁垒共创+次日体验式团建融合 |",
    "| 把价值观变行为·Leadership Envelopes + Run Your Favorite Manager + Leadership Pizza（icebreaker.html） | 4 | 二手 | ②上下级 | 一线经理三件套:行为卡/众筹上下级do's&don'ts/一页自评;leader以身作则参与 |",
    "| 国企新员工迎新·破冰 + 传帮带 + 师徒结对长效机制（中铁水利 · 一手）（icebreaker.html） | 4 | 一手 | ②上下级 | 中铁水利五步把传帮带长效化,领导以'坝体精神'类比提期望;送变电/山推同类案例 |",
    "| 福华集团「讲真话」恳谈会·领导班子 + 中层 + 员工代表跨级对话（福华 · 一手）（icebreaker.html） | 4 | 一手 | ②上下级 | 福华'讲真话听真话'恳谈(约100人):团建热身+分层发言+建议共享,容错/越级提问题/消灭部门墙制度化 |",
]
idx00 = idx00.rstrip("\n") + "\n" + "\n".join(rows) + "\n"
open(IDX00, "w", encoding="utf-8").write(idx00)
print("00-index updated")

# ===== 6. 本轮独立笔记 =====
os.makedirs(os.path.dirname(RUN_NOTE), exist_ok=True)
run_md = '''---
title: 破冰·第三十三轮知识卡（2026-09-06）
tags: [知识采集, 自动化采集, 破冰, 本轮增量]
date: 2026-09-06
type: 自动化采集
relation: [supervisor, exec]
source_topic: 破冰
---

# 破冰 · 第三十三轮补采知识卡（2026-09-06 · R33）

> 本轮 +6 卡（②上下级 ×3 / ③高管间 ×3），一手 4 / 二手 2；去重删 M=0（6 个 URL 全部 NEW，无重复）。
> 六维评估全过。定向补：③ SOAR 欣赏式探询战略共创（替 SWOT）、齐鲁云商「话题轮换」务虚机制、渡远集团古田务虚+愿景画布跨壁垒共创；② 把领导价值观落成行为卡三件套、国企新员工迎新传帮带师徒结对长效机制、福华「讲真话」跨级恳谈。

**本轮独立页（GitHub Pages）**：[icebreaker-2026-09-06-r33.html](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/runs/icebreaker-2026-09-06-r33.html)
**本机源**：`knowledge-collection/icebreaker/runs/icebreaker-2026-09-06-r33.html`
**累计卡片墙（总索引）**：[icebreaker.html](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/icebreaker/icebreaker.html)

| # | 卡片 | 关系档 | 一手/二手 | 核心要点 |
|---|---|---|---|---|
| 1 | SOAR 框架·欣赏式探询战略共创（SWOT 的积极替代） | ③高管间 | 二手 | SOAR(Strengths/Opportunities/Aspirations/Results)基于欣赏式探询,是SWOT积极替代:从'什么在起作用'出发;高管务虚1-2h四步(峰值体验提示优势/具体机会/给足抱负的Aspirations/领先指标Results) |
| 2 | 齐鲁云商工作务虚会·「话题轮换」主持机制（山东能源 · 一手） | ③高管间 | 一手 | 齐鲁云商'以虚务实、虚实结合';'话题轮换'一人主持两话题余人思考解答,逼深度思考避空谈;高层+基层务虚并行统一思路 |
| 3 | 渡远集团年中战略务虚·红色教育 +「愿景画布」共创（渡远 · 一手） | ③高管间 | 一手 | 渡远40余人古田务虚:红色教育+战略研讨+晚间'愿景画布'跨壁垒共创+次日体验式团建融合 |
| 4 | 把价值观变行为·Leadership Envelopes + Run Your Favorite Manager + Leadership Pizza | ②上下级 | 二手 | 一线经理三件套:行为卡(Leadership Envelopes)/众筹上下级do's&don'ts(Run Your Favorite Manager)/一页自评(Leadership Pizza);leader以身作则 |
| 5 | 国企新员工迎新·破冰 + 传帮带 + 师徒结对长效机制（中铁水利 · 一手） | ②上下级 | 一手 | 中铁水利五步(文体破冰→制度文化→实地探访→新老座谈→师徒结对);送变电签'师徒带教协议'、山推传经,传帮带长效化 |
| 6 | 福华集团「讲真话」恳谈会·领导班子 + 中层 + 员工代表跨级对话（福华 · 一手） | ②上下级 | 一手 | 福华'讲真话听真话'恳谈(主席+班子+中层+员工约100人):团建热身+分层发言+建议共享,容错/越级提问题/消灭部门墙制度化 |
'''
open(RUN_NOTE, "w", encoding="utf-8").write(run_md)
print("run note created:", RUN_NOTE)
print("DONE")
