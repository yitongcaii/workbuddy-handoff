# -*- coding: utf-8 -*-
import json, re, os

def safe_write(path, content):
    d = os.path.dirname(path)
    tmp = os.path.join(d, ".tmp_%s" % os.path.basename(path))
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(content)
    os.replace(tmp, path)  # atomic on same volume


KC = r"c:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection"
VAULT = r"c:/Users/v_yitcai/Documents/Obsidian/知识采集库"

# ---------- 5 new cards (HTML blocks, 2-space indent for grid children) ----------
def card(emoji, title, cat, badges, val, how, url, short, note):
    return (
        '    <div class="hl">\n'
        '      <div class="top"><span class="emoji">%s</span><h3>%s</h3>'
        '<span class="cat">%s</span>%s<span class="badge b2">二手</span></div>\n'
        '      <p class="val">%s</p>\n'
        '      <details class="exec"><summary>怎么做</summary><div class="inner">%s</div></details>\n'
        '      <div class="src">\u2757 <a href="%s" target="_blank">%s</a></div>\n'
        '      <div class="note">%s</div>\n'
        '    </div>' % (emoji, title, cat, badges, val, how, url, short, note)
    )

b23 = '<span class="badge r2">上下级</span><span class="badge r3">高管间</span>'
b3  = '<span class="badge r3">高管间</span>'
b2  = '<span class="badge r2">上下级</span>'

# sec3 cards (exec + dual)
c1 = card("🛠️", "数字化员工认可平台选型对比（Bonusly/Kudos/WorkTango 等）", "工具平台", b23,
    "盘点主流员工认可 SaaS 的选型维度与差异——Bonusly（点对点+积分，Slack/Teams 深度集成，$2.7/人/月）、Kudos（每条认可映射公司价值观、生成文化数据）、WorkTango（认可+敬业度调研+目标一体化，看板联动认可与 engagement）、Nectar（约 Bonusly 一半价的高性价比）、Awardco（Amazon 全球奖励目录）。选型五问：功能深度/易用采纳/集成(Slack·Teams·HRIS)/分析能力/价格透明；远程与混合团队需关注积分商城与多语言本地化奖励。",
    "先定「是否要积分商城+是否要 survey 联动」再选型；远程团队优先 Bonusly/Nectar（Slack 集成强）；要文化数据看板选 Kudos；要认可+敬业度一体化选 WorkTango；把年度颁奖盛典的微认可下沉为日常高频、管理层带头。",
    "http://bonusly.com/post/top-15-employee-recognition-software-platforms",
    "bonusly.com/post/top-15-employee-recognition-software-platforms",
    "适用：②+③ HR/管理层选型认可平台，把颁奖的微认可日常化、数据化。")

c3 = card("⚖️", "颁奖奖金税务合规风险与个税处理", "合规风控", b23,
    "颁奖/年会发现金奖、实物奖、抽奖均有明确税务边界——现金与实物奖品并入「工资薪金所得」由单位代扣代缴个税；未扣缴则企业所得税不得税前扣除，构成偷税面临补税+滞纳金+0.5-3倍罚款；「现场抓钱」式随机发奖因金额不透明、无法计入薪酬，风险最高。省级以下政府/部门一次性奖励按「偶然所得」20% 计征；母公司转付奖金由支付方代扣。合规要点：奖金纳入工资总额预扣、留存合规凭证、税前不含税奖金需还原计税。",
    "颁奖前与财务/税务对齐发放形式（现金/实物/积分）；统一计入薪酬并代扣个税，避免「现场抓钱」式不透明发放；年会抽奖奖品并入工资薪金；折扣券/代金券等优惠性福利除外；重大表彰预算先做税务测算再批。",
    "http://www.cjtax.cn/a/202510/12rb4lvllw3b4.shtml",
    "cjtax.cn/a/202510/12rb4lvllw3b4.shtml",
    "适用：③+② 颁奖/年会发奖的税务合规红线，CFO/HR 必须前置对齐。")

c5 = card("📣", "颁奖盛典·雇主品牌与招聘转化引擎", "雇主品牌", b3,
    "把员工表彰盛典做成对外雇主品牌资产：麦当劳「McDiploma 毕业典礼」为未上过大学的餐厅经理补办毕业礼，超越雇主角色提供深层情感满足，引发全城热议——活动期求职申请量 +77%、成功录用率 +109%、免费媒体曝光价值超 120 万美元，并逆转员工净流失趋势（+312%）。启示：表彰的「情感体验+故事化传播」能直接转化为招聘漏斗与雇主评分。",
    "选有情感穿透力的表彰主题（补办毕业礼/家庭日荣耀）；设计可传播的「故事瞬间」供媒体/社媒二次传播；把获奖者故事做成雇主品牌内容（短视频/公关稿）；对外传播对标「优秀雇主」评选，将内部荣誉转化为招聘吸引力。",
    "https://effie-greaterchina.cn/news/show-7421.html",
    "effie-greaterchina.cn/news/show-7421.html",
    "适用：③ 高管/品牌视角，把表彰盛典升级为雇主品牌与招聘转化杠杆。")

# sec2 cards (supervisor)
c2 = card("🎮", "gamification·积分商城即时激励体系", "游戏化激励", b2,
    "用「积分+勋章+排行榜」游戏化方式建立公开透明的即时反馈：管理者手机端随时发积分（选行为项+填理由+寄语），员工实时到账并可选推送团队群公开表扬；积分商城对接实物/虚拟/福利权益（高端体检·额外假期·弹性福利），积分行为数据看板识别「高活跃/沉默」群体、优化激励策略；积分与绩效关联后主动性提升 2-3 倍，核心人才流失降 15-25%。",
    "把企业价值观具象为勋章体系（如「北斗七星币」）；日常行为即时激励下沉到门店/一线；积分排名作年度评优参考；商城运营做「每月 6 号特价兑换」拉活跃；沉默积分用户触发定向激励。",
    "http://www.bote.com.cn/case/information_12372.shtml",
    "bote.com.cn/case/information_12372.shtml",
    "适用：② 经理主导的日常游戏化即时激励，让认可「随时发生」而非年终一次。")

c4 = card("🔧", "制造业一线蓝领表彰·「金蓝领」激励范式", "一线表彰", b2,
    "制造业把表彰对准一线技术工人，破解「重研发轻一线」：中车戚墅堰所产改搭 6 层 18 级职业阶梯+「技师+工程师」双师型，一线工匠凭实绩与高管/博士同台领奖，技能工人平均工资较产改初增 63%；湖南石化「双数年份评劳模·单数评工匠」+疗休养，竞赛「全员盲抽·贴近实战」让普通操作工站聚光灯；金澳兰把评优从一年改半年一评、荣誉墙张榜+晋升疗休养优先。核心：让「能干的人有名有利有奔头」。",
    "表彰对象向一线操作工/技师倾斜，设「蓝领工艺创新成果奖」等专项；评优周期缩短（年→半年）保持激励热度；荣誉墙张榜+晋升/疗休养绑定；劳动竞赛结果与评优晋升挂钩，让普通工人凭本事赢认可赢通道。",
    "https://www.thepaper.cn/newsDetail_forward_33216539",
    "thepaper.cn/newsDetail_forward_33216539",
    "适用：② 制造业/产线一线员工表彰，把技能工人推上 C 位、打通成长通道。")

sec3_cards = "\n".join([c1, c3, c5])
sec2_cards = "\n".join([c2, c4])

# ---------- 1. award.html ----------
html_path = os.path.join(KC, "award", "award.html")
html = open(html_path, encoding="utf-8").read()

# hero line
assert "五轮 enrich 2026-08-09(+5) ｜" in html
html = html.replace("五轮 enrich 2026-08-09(+5) ｜",
                    "五轮 enrich 2026-08-09(+5) ｜ 六轮 enrich 2026-08-10(+5) ｜", 1)
# section counts
assert html.count('<span class="tag">19 卡</span>') == 1
html = html.replace('<span class="tag">19 卡</span>', '<span class="tag">22 卡</span>', 1)
assert html.count('<span class="tag">20 卡</span>') == 1
html = html.replace('<span class="tag">20 卡</span>', '<span class="tag">22 卡</span>', 1)

# insert sec3 cards before sec3 grid close (the </div> right before ② comment)
marker = '\n  </div>\n\n  <!-- ============ ② 上下级 ============ -->'
assert html.count(marker) == 1, "sec3 marker not unique"
idx = html.index(marker)
gc = html.rindex('\n  </div>', 0, idx)   # sec3 grid close
html = html[:gc] + "\n" + sec3_cards + html[gc:]

# insert sec2 cards before sec2 grid close (the </div> right before footer)
m = re.search(r'(\n  </div>)(\s*)(<footer>)', html)
assert m, "sec2 grid close before footer not found"
html = html[:m.start()] + "\n" + sec2_cards + html[m.start():]

safe_write(html_path, html)
print("award.html updated -> 44 cards (sec3 22 / sec2 22)")

# ---------- 2. index.json ----------
idx_path = os.path.join(KC, "index.json")
data = json.load(open(idx_path, encoding="utf-8"))
before = len(data)

def norm(t):
    return re.sub(r'[\s·+，。、（）()/：:；;]', '', t)

new_entries = [
    {"title":"数字化员工认可平台选型对比（Bonusly/Kudos/WorkTango 等）",
     "normKey":norm("数字化员工认可平台选型对比（Bonusly/Kudos/WorkTango 等）"),
     "url":"http://bonusly.com/post/top-15-employee-recognition-software-platforms",
     "sourceType":"secondary","relation":"supervisor,exec",
     "summary":"主流认可SaaS选型维度与差异(Bonusly点对点积分/Kudos价值观映射/WorkTango认可+敬业度一体/Nectar性价比/Awardco全球奖励)；远程团队关注积分商城与多语言本地化"},
    {"title":"gamification·积分商城即时激励体系",
     "normKey":norm("gamification·积分商城即时激励体系"),
     "url":"http://www.bote.com.cn/case/information_12372.shtml",
     "sourceType":"secondary","relation":"supervisor",
     "summary":"积分+勋章+排行榜游戏化即时反馈；管理者手机端发积分、积分商城对接实物/虚拟/福利；数据看板识别高活跃/沉默群体；与绩效关联后主动性提升2-3倍、核心人才流失降15-25%"},
    {"title":"颁奖奖金税务合规风险与个税处理",
     "normKey":norm("颁奖奖金税务合规风险与个税处理"),
     "url":"http://www.cjtax.cn/a/202510/12rb4lvllw3b4.shtml",
     "sourceType":"secondary","relation":"supervisor,exec",
     "summary":"现金/实物/抽奖奖品并入工资薪金代扣个税；未扣缴则所得税不得扣除、面临补税+0.5-3倍罚款；省级以下一次性奖励按偶然所得20%计；现场抓钱式随机发奖风险最高"},
    {"title":"制造业一线蓝领表彰·「金蓝领」激励范式",
     "normKey":norm("制造业一线蓝领表彰·「金蓝领」激励范式"),
     "url":"https://www.thepaper.cn/newsDetail_forward_33216539",
     "sourceType":"secondary","relation":"supervisor",
     "summary":"中车戚墅堰所6层18级职业阶梯+双师型、一线工匠与高管同台领奖、平均工资增63%；湖南石化双数评劳模单数评工匠；金澳兰评优半年一评+荣誉墙张榜，让技能工人有名有利有奔头"},
    {"title":"颁奖盛典·雇主品牌与招聘转化引擎",
     "normKey":norm("颁奖盛典·雇主品牌与招聘转化引擎"),
     "url":"https://effie-greaterchina.cn/news/show-7421.html",
     "sourceType":"secondary","relation":"exec",
     "summary":"麦当劳McDiploma补办毕业礼引发全城热议：求职申请+77%、录用率+109%、媒体曝光超120万美元、员工净流失逆转+312%；表彰的情感体验+故事化传播转化为招聘漏斗与雇主评分"},
]
# dedup guard against existing urls
existing_urls = {e["url"] for e in data}
added = 0
for e in new_entries:
    if e["url"] in existing_urls:
        print("SKIP dup url:", e["url"])
        continue
    data.append(e); added += 1
safe_write(idx_path, json.dumps(data, ensure_ascii=False, indent=2))
print("index.json: %d -> %d (added %d)" % (before, len(data), added))

# ---------- 3. Obsidian 颁奖-知识卡汇总.md ----------
note_path = os.path.join(VAULT, "素材", "award", "颁奖-知识卡汇总.md")
txt = open(note_path, encoding="utf-8").read()
# abstract
txt = txt.replace("（共 39 张，首轮12 + 二次补采7 + 乐享内部一手1（花草团队SOP&SLA）+ 三轮 enrich 8 + 四轮 enrich 6 + 五轮 enrich 5）",
                   "（共 44 张，首轮12 + 二次补采7 + 乐享内部一手1（花草团队SOP&SLA）+ 三轮 enrich 8 + 四轮 enrich 6 + 五轮 enrich 5 + 六轮 enrich 5）", 1)
# table rows
rows = [
"| 数字化员工认可平台选型对比（award/award.html） | 4 | 二手 | ②+③ | 主流认可SaaS选型(Bonusly点对点积分/Kudos价值观映射/WorkTango认可+敬业度一体/Nectar性价比/Awardco全球奖励) |",
"| gamification·积分商城即时激励体系（award/award.html） | 4 | 二手 | ②上下级 | 积分+勋章+排行榜游戏化即时反馈；手机端发积分、积分商城对接福利；数据看板识别高活跃/沉默群体 |",
"| 颁奖奖金税务合规风险与个税处理（award/award.html） | 5 | 二手 | ②+③ | 现金/实物/抽奖并入工资薪金代扣个税；未扣缴所得税不得扣除；现场抓钱式随机发奖风险最高 |",
"| 制造业一线蓝领表彰·「金蓝领」激励范式（award/award.html） | 4 | 二手 | ②上下级 | 中车6层18级职业阶梯+双师型、一线工匠与高管同台领奖；湖南石化双数评劳模单数评工匠；金澳兰半年一评 |",
"| 颁奖盛典·雇主品牌与招聘转化引擎（award/award.html） | 4 | 二手 | ③高管间 | 麦当劳McDiploma补办毕业礼：求职+77%/录用+109%/媒体曝光120万美元/净流失逆转+312% |",
]
anchor = "| 优秀员工携家属出席表彰+家属关爱（award/award.html） | 4 | 二手 | ②上下级 | 路达/太古：携家属见证+家属关爱游/连线爱人，三方认同 |"
assert anchor in txt, "table anchor not found"
ins = "\n".join(rows)
txt = txt.replace(anchor, anchor + "\n" + ins, 1)
# 适用&备注 paragraph - append six-round note
old_tail = "五轮 enrich 补：颁奖典礼危机预案与控场话术SOP、多元包容(D&I)奖项设计框架、表彰大会内部传播与复盘闭环SOP、高管层把员工家属请进表彰盛典、优秀员工携家属出席表彰+家属关爱。"
new_tail = old_tail + "六轮 enrich 补：数字化员工认可平台选型对比(Bonusly/Kudos/WorkTango/Nectar/Awardco)、gamification积分商城即时激励体系、颁奖奖金税务合规风险与个税处理、制造业一线蓝领「金蓝领」激励范式、颁奖盛典作为雇主品牌与招聘转化引擎(McDiploma)。"
assert old_tail in txt
txt = txt.replace(old_tail, new_tail, 1)
safe_write(note_path, txt)
print("Obsidian 颁奖-知识卡汇总.md updated (44 cards)")

# ---------- 4. 00-知识采集索引.md ----------
idx_md = os.path.join(VAULT, "00-知识采集索引.md")
t = open(idx_md, encoding="utf-8").read()
# section header
t = t.replace("## 主题：颁奖典礼（2026-08-06 首采 · 四轮 enrich 2026-08-08 · 五轮 enrich 2026-08-09）",
              "## 主题：颁奖典礼（2026-08-06 首采 · 四轮 enrich 2026-08-08 · 五轮 enrich 2026-08-09 · 六轮 enrich 2026-08-10）", 1)
# count block
t = t.replace("**39 卡**（首轮12 + 二次补采7 + 乐享内部一手1（花草团队SOP&SLA框架）+ 三轮 enrich 8 + 四轮 enrich 6 + 五轮 enrich 5；",
              "**44 卡**（首轮12 + 二次补采7 + 乐享内部一手1（花草团队SOP&SLA框架）+ 三轮 enrich 8 + 四轮 enrich 6 + 五轮 enrich 5 + 六轮 enrich 5；", 1)
# append 5 rows before Open Day section
rows0 = [
"| 数字化员工认可平台选型对比（award/award.html） | 4 | 二手 | ②+③ | Bonusly点对点积分/Kudos价值观映射/WorkTango认可+敬业度一体/Nectar性价比/Awardco全球奖励，远程团队关注积分商城与多语言本地化 |",
"| gamification·积分商城即时激励体系（award/award.html） | 4 | 二手 | ②上下级 | 积分+勋章+排行榜游戏化即时反馈；手机端发积分、积分商城对接实物/虚拟/福利；数据看板识别高活跃/沉默群体、与绩效关联后主动性提升2-3倍 |",
"| 颁奖奖金税务合规风险与个税处理（award/award.html） | 5 | 二手 | ②+③ | 现金/实物/抽奖并入工资薪金代扣个税；未扣缴所得税不得扣除、面临补税+0.5-3倍罚款；省级以下一次性奖励按偶然所得20%计；现场抓钱式风险最高 |",
"| 制造业一线蓝领表彰·「金蓝领」激励范式（award/award.html） | 4 | 二手 | ②上下级 | 中车6层18级职业阶梯+双师型、一线工匠与高管同台领奖、平均工资增63%；湖南石化双数评劳模单数评工匠；金澳兰半年一评+荣誉墙张榜 |",
"| 颁奖盛典·雇主品牌与招聘转化引擎（award/award.html） | 4 | 二手 | ③高管间 | 麦当劳McDiploma补办毕业礼引发全城热议：求职+77%/录用+109%/媒体曝光120万美元/净流失逆转+312% |",
]
anchor0 = "| 优秀员工携家属出席表彰+家属关爱（award/award.html） | 4 | 二手 | ②上下级 | 路达/太古：携家属见证+家属关爱游/连线爱人，三方认同 |"
assert anchor0 in t, "00-index award anchor not found"
t = t.replace(anchor0, anchor0 + "\n" + "\n".join(rows0), 1)
safe_write(idx_md, t)
print("00-知识采集索引.md updated (award 44 cards)")

# ---------- 5. portal index.html ----------
portal = os.path.join(KC, "index.html")
p = open(portal, encoding="utf-8").read()
assert p.count('<div class="cnt">39 卡</div>') >= 1
p = p.replace('<div class="cnt">39 卡</div>', '<div class="cnt">44 卡</div>', 1)
safe_write(portal, p)
print("portal index.html award count 39 -> 44")

# ---------- 6. last-topic.txt ----------
lt = open(os.path.join(KC, "last-topic.txt"), encoding="utf-8").read().strip()
print("last-topic before:", lt)
safe_write(os.path.join(KC, "last-topic.txt"), "Open Day\n")
print("last-topic after: Open Day")
print("DONE")
