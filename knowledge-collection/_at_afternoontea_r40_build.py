# -*- coding: utf-8 -*-
"""R40 enrich for 下午茶研讨 (afternoontea). 2026-09-09. 8 cards (③×3 + ②×5)."""
import json, os, io, subprocess, sys

BASE = os.path.dirname(os.path.abspath(__file__))
SUB = os.path.join(BASE, "afternoontea")
SUM = os.path.join(SUB, "afternoontea.html")
INC = os.path.join(SUB, "afternoontea-20260909.html")
TMP = os.path.join(SUB, ".run_newcards.tmp.html")
IDX = os.path.join(BASE, "index.json")
OBS_NOTE = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\afternoontea\下午茶研讨-知识卡汇总.md"
OBS_00 = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
RUNS_NOTE = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\afternoontea\runs\下午茶研讨-2026-09-09-第四十轮-知识卡.md"
ROUND = "四十轮 enrich 2026-09-09(+8)"
DATE = "2026-09-09"
PAGES = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/afternoontea"
RUN_PAGE = PAGES + "/runs/afternoontea-2026-09-09-r40.html"

CSS = """<style>
:root{
  --bg:#f4f6fb; --card:#ffffff; --ink:#1f2430; --sub:#5b6478;
  --accent:#6c5ce7; --accent2:#00b8d9; --chip:#eef0ff;
}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:linear-gradient(135deg,#eef1ff 0%,#e6f7ff 100%);color:var(--ink);padding:28px 18px;line-height:1.6;}
.wrap{max-width:1080px;margin:0 auto;}
.hero{background:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);border-radius:22px;padding:30px 32px;color:#fff;box-shadow:0 14px 40px rgba(108,92,231,.25);margin-bottom:22px;}
.hero h1{font-size:28px;font-weight:800;letter-spacing:1px;margin-bottom:8px;}
.hero p{font-size:14px;opacity:.95;}
.relbar{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px;}
.relbar span{background:rgba(255,255,255,.2);border-radius:20px;padding:5px 14px;font-size:13px;font-weight:600;}
.sec{margin:30px 0 12px;display:flex;align-items:center;gap:10px;}
.sec h2{font-size:19px;font-weight:800;}
.sec .tag{font-size:12px;padding:4px 12px;border-radius:12px;font-weight:700;}
.sec3 .tag{background:#f3e8ff;color:#7b2cbf;} .sec3 h2{color:#7b2cbf;}
.sec2 .tag{background:#fff3e0;color:#c0651a;} .sec2 h2{color:#c0651a;}
.sec .desc{font-size:12.5px;color:var(--sub);margin-left:2px;}
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;}
.hl{background:var(--card);border-radius:18px;padding:18px 18px 16px;border-top:4px solid var(--accent);box-shadow:0 10px 32px rgba(108,92,231,.10);display:flex;flex-direction:column;gap:9px;}
.top{display:flex;align-items:center;gap:8px;flex-wrap:wrap;}
.emoji{font-size:22px;}
.hl h3{font-size:16px;font-weight:700;flex:1;min-width:120px;}
.cat{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:600;background:var(--chip);color:var(--accent);}
.badge{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:700;}
.b2{background:#fff1e6;color:#c0651a;}
.b1{background:#e6f9ed;color:#1a9e5a;}
.r1{background:#eaf2ff;color:#2b6cb0;}
.r2{background:#fff3e0;color:#c0651a;}
.r3{background:#f3e8ff;color:#7b2cbf;}
.val{font-size:13.5px;color:var(--sub);}
.exec{margin-top:2px;border-top:1px dashed #e2e8f0;padding-top:8px;}
.exec summary{cursor:pointer;font-size:13px;font-weight:600;color:var(--accent);}
.exec .inner{font-size:13px;color:var(--sub);margin-top:6px;padding-left:4px;}
.src{font-size:12px;word-break:break-all;}
.src a{color:var(--accent2);text-decoration:none;}
.note{font-size:12px;color:#94a3b8;border-left:3px solid #e2e8f0;padding-left:8px;}
footer{text-align:center;padding:24px;color:#94a3b8;font-size:13px;border-top:1px solid #e2e8f0;margin-top:40px;}
</style>"""

def card_html(c):
    rel = c["relation"]
    rcls = "r3" if rel == "高管间" else "r2"
    scls = "b1" if c["source"] == "一手" else "b2"
    return (
        '    <div class="hl">\n'
        '      <div class="top"><span class="emoji">%s</span><h3>%s</h3>'
        '<span class="cat">%s</span><span class="badge %s">%s</span>'
        '<span class="badge %s">%s</span></div>\n'
        '      <p class="val">%s</p>\n'
        '      <details class="exec"><summary>怎么做</summary><div class="inner">%s</div></details>\n'
        '      <div class="src">\U0001F4C1 <a href="%s" target="_blank">%s</a></div>\n'
        '      <div class="note">适用：%s</div>\n'
        '    </div>\n'
    ) % (c["emoji"], c["title"], c["cat"], rcls, rel, scls, c["source"],
         c["val"], c["how"], c["url"], c["url"], c["note"])

# ③ 高管间 (exec) = 3  | ② 上下级 (supervisor) = 5
CARDS = [
 # ===== ③ 高管间 =====
 {"emoji":"\U0001F942","relation":"高管间","source":"一手",
  "title":"2026达沃斯·财新CEO午餐会·30位政商领袖闭门午宴圆桌",
  "cat":"国际CEO闭门午餐会",
  "val":"财新传媒在世界经济论坛2026年年会期间举办第十四届「财新·达沃斯CEO午餐会」，连续14年成国际化高规格强互动闭门活动；为30余位海内外高级政府代表、商业领军人物及知名学者提供对话平台，围绕「探寻有效增长之道」设午宴+主持引导圆桌，分议题含新工业与创新链、科技与资本、可持续金融绿色转型、城市与社会信任；嘉宾含茅台王莉、宁德时代蒋理、腾讯汤道生、哈佛Allison、澳大利亚前总理陆克文等。",
  "how":"办高管闭门午餐会学财新「强互动圆桌+主持人点火」：邀约制把30位政商学界领袖拉到同一张午宴桌，用「主旨演讲→午宴圆桌→自由交流」三段式、主持人点火式提问激发深度对话；适合媒体/智库/商会做顶级圈层活动，关键是「闭门+强互动+高规格同侪」让CEO级敢谈真问题。",
  "url":"https://conferences.caixin.com/2025/caixinceoluncheon_davos2026/",
  "note":"③ 财新传媒 × 海内外高级政府代表/商业领军人物/学者（财新官方一手；达沃斯CEO午餐会闭门圆桌，可作国际顶级CEO对话范本）。"},
 {"emoji":"\U0001F37D","relation":"高管间","source":"一手",
  "title":"CEO-only Lunch·仅CEO/总经理月度同侪午餐机制",
  "cat":"高管同侪午餐机制",
  "val":"「CEO-only lunch」是保加利亚发起的CEO同侪午餐项目，每月一次（暑期休），每场仅10席、仅CEO或总经理可入场；每位CEO有5分钟介绍自家业务，餐后留1小时咖啡茶「networking session」，议题含国家品牌出海、加入欧元区前景、改善营商环境、共同商业倡议；2026年已办至第21届，参与者含Adecco、Lufthansa Technik、Shell、Schneider Electric、Hilton等跨国CEO。",
  "how":"办高管同侪午餐学「CEO-only lunch」极简机制：严格准入（仅CEO/GM、限10人、月度制）+每人5分钟业务自介+餐后咖啡茶深聊，把networking做成低负担高频次同侪圈；适合商会/CEO俱乐部做高管关系经营，关键是「小而密+同侪对等+无客户无下属」让CEO敢聊战略与困惑。",
  "url":"http://www.ceoonlylunch.com/",
  "note":"③ CEO/总经理 × 同行CEO（项目官网一手；CEO-only lunch 月度同侪午餐机制，可作高管私域圈层范本）。"},
 {"emoji":"\U0001F338","relation":"高管间","source":"二手",
  "title":"凌奥女企业家围坐茶话会·妇联主席与女企共谋发展",
  "cat":"园区女企业家茶话会",
  "val":"凌奥集团妇联携手园区女企业家在创意产业园办「与春天相约 聚力绽芳华」女企业家围坐茶话会，十余位来自银行、有机食品、高端服饰、非遗泥人张、孵化器、酒店、律所等领域女企业家代表欢聚；多位女企分享发展历程与跨界AI影视剪辑、音疗等新规划，民生银行推介便民金融服务，泥人张非遗传承人讲21年扎根园区，凌奥妇联主席赵万霞表态搭建巾帼众创空间与常态化交流平台、做创业路上伙伴。",
  "how":"办园区女企业家茶话会学凌奥「妇联搭台+跨业互哺」：园区妇联主席与女企围坐、让不同行业女企轮流亮业务与跨界新规划、银行现场推服务，把茶叙做成资源互补客群共享的联盟起点；适合产业园/妇联做女性创业赋能，关键是「以园聚人+以业互哺」让女企找到伙伴与机遇。",
  "url":"https://m.toutiao.com/article/7621753677245678120",
  "note":"③ 凌奥妇联主席（园区管理）× 女企业家代表（今日头条二手；女企业家围坐茶话会，可作园区妇联赋能范本）。"},
 # ===== ② 上下级 =====
 {"emoji":"\U0001F9EC","relation":"上下级","source":"一手",
  "title":"江西稀土2026迎新春茶话会·董事长与全员话初心",
  "cat":"迎新春茶话会",
  "val":"中稀江西稀土2026迎新春茶话会以「凝心聚力话初心，策马扬鞭启新程」为主题，公司领导与本部全体员工欢聚；座谈环节各部门员工代表立足岗位坦诚建言、围绕业务提质效能提升产业赋能献良策，二胡独奏《赛马》、马年成语接龙、稀土知识快问快答等趣味互动凝聚团队；党委书记董事长黄华勇作总结讲话，肯定全年实干担当、寄语拿「马的干劲速度担当」抓实每项工作，向员工及家属致新春祝福。",
  "how":"办迎新春茶话会学江西稀土「领导与全员欢聚+主题互动」：把董事长总结寄语与员工代表献良策放在同一场、用马年主题趣味互动（成语接龙/知识竞答）暖场凝聚，再领导擂鼓式动员；适合集团/国企做新春团建，关键是「领导在场+员工发声+轻互动暖场」让全员既被看见又被激励。",
  "url":"https://gz-re.com/n3322/c201766/content.html",
  "note":"② 集团党委书记/董事长 × 本部全体员工（中稀江西稀土官网一手；迎新春茶话会，可作集团全员新春范本）。"},
 {"emoji":"\U0001F332","relation":"上下级","source":"一手",
  "title":"远诚咨询新春茶话会·董事长与同仁围坐回望启新",
  "cat":"企业新春茶话会",
  "val":"远诚工程咨询「欢聚·暖意·启新程」新春茶话会，董事长丰总回顾2019–2025奋斗征程、擘画2026蓝图，坦言行业低迷仍锤炼出敢打硬仗团队；设「心愿签送祝福」抽签结缘传情、「谐音梗游戏+看图猜电影」爆笑破冰，同事互送鼓励、对公司在成长突破共创佳绩许愿；现场致敬奔波项目现场与一线驻场同事，把欢笑感动化作攻坚底气。",
  "how":"办企业新春茶话会学远诚「董事长回望+轻仪式破冰」：董事长直面行业低谷讲真实复盘、用「心愿签/谐音梗游戏」替代单向汇报破冰，并现场致敬一线驻场同事；适合中小咨询/工程公司做新春凝聚，关键是「领导说真话+轻互动卸压+致敬一线」让团队在低潮期仍感被托住。",
  "url":"https://m.yuanchengzx.com/displaynews.html?id=6650536904868672",
  "note":"② 董事长 × 全体同仁（远诚咨询官网一手；新春茶话会，可作中小企业新春关怀范本）。"},
 {"emoji":"\U0001F6F2","relation":"上下级","source":"一手",
  "title":"长江公司工会2026马年新春茶话会·一把手与职工同台",
  "cat":"工会新春茶话会",
  "val":"上港集团长江公司工会办「长帆破浪迎马岁」2026迎新春茶话会，公司党委书记董事长总经理致辞回首2025长江战略市场开拓服务创新成果、寄语以万马奔腾活力奋进十五五；以年度精彩视频开篇，设「方言献福猜猜乐/AI唱词猜金曲/新春逛园大闯关/祥意身传贺新岁」等结合港口业务特色的互动，领导与职工默契配合展现团队协作，在轻松氛围凝聚人心鼓舞士气。",
  "how":"办工会新春茶话会学长航「一把手致辞+业务定制互动」：党委书记董事长总经理与职工同场、用「方言/AI唱词/业务闯关」等贴合主业游戏替代通用破冰，领导与职工组队配合；适合国企工会做新春庆祝，关键是「领导同台+业务味互动」让职工在欢笑中认同战略、凝聚干劲。",
  "url":"https://dj.sipg.com.cn/jlwm/107873.jhtml",
  "note":"② 公司党委书记/董事长/总经理 × 全体职工（上港集团党建网一手；工会新春茶话会，可作国企工会范本）。"},
 {"emoji":"\U0001F49E","relation":"上下级","source":"二手",
  "title":"草埠湖镇青年干部七夕茶话会·镇领导与新人破冰",
  "cat":"青年干部茶话会",
  "val":"当阳市草埠湖镇新时代文明实践所办七夕青年干部茶话会，本地与外地新入职青年干部齐聚，设趣味破冰（数字炸弹/传声筒/我画我猜）打破新老本地外地隔阂，茶话交流环节已有经验青年干部分享基层为民服务心得、新人谈初入岗位体会并获本地生活资源分享；镇党委政府以节日为纽带关心青年成长、消除陌生感提高凝聚力。",
  "how":"办青年干部茶话会学草埠湖「节日破冰+经验传帮」：用七夕节点做无压力茶叙、以数字炸弹等轻游戏打破新老本地外地隔阂，再让有经验青年干部分享、新人敞开心声并收本地生活攻略；适合乡镇/机关做新干部融入，关键是「以节破冰+以老带新+生活关怀」让外地新人快速扎根。",
  "url":"https://news.hubeidaily.net/pc/c_5882623.html",
  "note":"② 镇党委/政府领导 × 本地及外地新入职青年干部（湖北日报二手；青年干部七夕茶话会，可作基层青年关怀范本）。"},
 {"emoji":"\U0001F343","relation":"上下级","source":"二手",
  "title":"中国茶叶博物馆「一把手与青年面对面」·馆领导与新人茶叙",
  "cat":"青年员工座谈",
  "val":"中国茶叶博物馆「茶韵聚青力·清风筑同心」青年员工座谈会在梅家坞茶文化村举办，近五年新入职员工骨干与馆领导关工委领导走进茶山访红色足迹，开展「一把手与青年面对面」座谈；青年员工围坐分享入职收获困惑与期许，部门负责人讲导师带徒/跨岗交流/技能比武等培养举措，馆长包静以「入职五年是分水岭」送务实成长课，融情聚力兼授廉洁初心。",
  "how":"办青年员工座谈学茶博馆「行走课堂+一把手面对面」：把座谈搬进茶山（访周总理纪念室/老索道）做行走的初心课，再馆领导与近五年新人围坐、用「随手拍分享+导师带徒路径」替代汇报，馆长给分水岭式成长课；适合文博/事业单位做青年培养，关键是「场景化破冰+一把手平等对话+清晰成长路径」让青年有方向有归属。",
  "url":"https://www.sohu.com/a/1029563325_121107011",
  "note":"② 馆领导/关工委领导 × 近五年新入职青年员工（搜狐二手；中国茶叶博物馆一把手与青年面对面，可作文博青年培养范本）。"},
]

EXEC = [c for c in CARDS if c["relation"] == "高管间"]
SUP = [c for c in CARDS if c["relation"] == "上下级"]
assert len(EXEC) == 3 and len(SUP) == 5, (len(EXEC), len(SUP))
print("exec=%d sup=%d total=%d" % (len(EXEC), len(SUP), len(CARDS)))

# ---------- 1. increment page (legacy) ----------
def build_page(cards_exec, cards_sup):
    sec3 = "".join(card_html(c) for c in cards_exec)
    sec2 = "".join(card_html(c) for c in cards_sup)
    tpl = (
        '<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '<title>下午茶研讨 · 知识采集卡片墙（四十轮 2026-09-09）</title>\n'
        + CSS + '\n</head>\n<body>\n<div class="wrap">\n'
        '<div class="hero">\n'
        '    <h1>\U0001F375 下午茶研讨 · 知识采集卡片墙（四十轮增量）</h1>\n'
        '    <p>__ROUND__｜ 受众关系分层（仅②上下级 / ③高管间）｜ 一手/二手标注 ｜ 历史去重 ｜ 六维评估</p>\n'
        '    <div class="relbar">\n'
        '      <span>② 领导↔员工（上下级，supervisor）</span>\n'
        '      <span>③ 领导↔领导（高管间，exec）</span>\n'
        '    </div>\n'
        '  </div>\n'
        '<div class="sec sec3">\n'
        '    <h2>③ 领导↔领导（高管间 · exec）</h2>\n'
        '    <span class="tag">__N3__ 卡</span>\n'
        '    <span class="desc">商务化、以专业/共同目标切入，避免幼稚游戏</span>\n'
        '  </div>\n  <div class="grid">\n__SEC3__  </div>\n'
        '<div class="sec sec2">\n'
        '    <h2>② 领导↔员工（上下级 · supervisor）</h2>\n'
        '    <span class="tag">__N2__ 卡</span>\n'
        '    <span class="desc">尊重、不隐私暴露、建信任不越界</span>\n'
        '  </div>\n  <div class="grid">\n__SEC2__  </div>\n'
        '<footer>\U0001F4CC 本页由 yitong 沉淀整理 · 文化活动知识库</footer>\n'
        '</div>\n</body>\n</html>\n'
    )
    return (tpl
            .replace("__ROUND__", ROUND)
            .replace("__N3__", str(len(cards_exec)))
            .replace("__SEC3__", sec3)
            .replace("__N2__", str(len(cards_sup)))
            .replace("__SEC2__", sec2))
inc_html = build_page(EXEC, SUP)
with io.open(INC, "w", encoding="utf-8") as f:
    f.write(inc_html)
print("wrote increment:", INC, len(inc_html), "bytes")

# ---------- 1b. run page cards temp + gen_run_page.py ----------
with io.open(TMP, "w", encoding="utf-8") as f:
    f.write("".join(card_html(c) for c in CARDS))
print("wrote temp cards:", TMP)
gen = os.path.join(BASE, "gen_run_page.py")
r = subprocess.run([sys.executable, gen, "--topic", "afternoontea",
                    "--topic-name", "下午茶研讨",
                    "--date", DATE, "--round", "40",
                    "--cards-file", TMP], capture_output=True, text=True)
print("gen_run_page:", r.returncode, r.stdout.strip(), r.stderr.strip()[:300])

# ---------- 2. inject into summary wall ----------
with io.open(SUM, "r", encoding="utf-8") as f:
    wall = f.read()
old_hero = ("三十九轮 enrich 2026-09-08(+8：东莞控股高管茶话会三不原则/富春环保高管+青年+生日会/华都检测新人问卷精准指导/浙江东方工会主席一对一/国际leader-employee咖啡聊法·5② ｜ LeanIn女性职业沙龙/大数思享企业家闭门茶道/西青外企女性精英圆桌·3③)</p>")
new_hero = old_hero[:-4] + ("｜ 四十轮 enrich 2026-09-09(+8：财新达沃斯CEO午餐会/CEO-only Lunch月度同侪午餐/凌奥女企业家围坐·3③ ｜ 江西稀土迎新春/远诚咨询新春/长江公司工会新春/草埠湖镇青年干部七夕/茶博馆一把手与青年面对面·5②)</p>")
assert old_hero in wall, "hero anchor not found"
wall = wall.replace(old_hero, new_hero, 1)
assert '<span class="tag">122 卡</span>' in wall
assert '<span class="tag">204 卡</span>' in wall
wall = wall.replace('<span class="tag">122 卡</span>', '<span class="tag">125 卡</span>', 1)
wall = wall.replace('<span class="tag">204 卡</span>', '<span class="tag">209 卡</span>', 1)
g_open = '<div class="grid">'
gi1 = wall.find(g_open)
assert gi1 != -1
pos1 = gi1 + len(g_open)
wall = wall[:pos1] + "".join(card_html(c) for c in EXEC) + wall[pos1:]
sec2_pos = wall.find('<div class="sec sec2">')
assert sec2_pos != -1
gi2 = wall.find(g_open, sec2_pos)
assert gi2 != -1
pos2 = gi2 + len(g_open)
wall = wall[:pos2] + "".join(card_html(c) for c in SUP) + wall[pos2:]
assert "📌 本页由 yitong 沉淀整理 · 文化活动知识库" in wall
with io.open(SUM, "w", encoding="utf-8") as f:
    f.write(wall)
print("updated summary wall:", SUM, "cards=", wall.count('<div class="hl">'))

# ---------- 3. index.json ----------
with io.open(IDX, "r", encoding="utf-8") as f:
    data = json.load(f)
before = len(data)
for c in CARDS:
    nk = "".join(ch for ch in c["title"] if ch.isalnum() or '\u4e00' <= ch <= '\u9fff').lower()
    data.append({
        "title": c["title"],
        "normKey": nk,
        "url": c["url"],
        "sourceType": "primary" if c["source"] == "一手" else "secondary",
        "relation": "exec" if c["relation"] == "高管间" else "supervisor",
        "summary": c["val"][:60],
        "topic": "afternoontea"
    })
with io.open(IDX, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=1)
print("index.json +%d (before=%d after=%d)" % (len(CARDS), before, len(data)))

# ---------- 4. Obsidian note ----------
with io.open(OBS_NOTE, "r", encoding="utf-8") as f:
    note = f.read()
note = note.replace("（322 卡 · 上下级/高管间）", "（330 卡 · 上下级/高管间）", 1)
note = note.replace("date: 2026-09-08", "date: 2026-09-09", 1)
note = note.replace(
    "累计 322 卡（③高管间 122 / ②上下级 204）。",
    "累计 330 卡（③高管间 125 / ②上下级 209）。", 1)
exec_titles = " / ".join(c["title"] for c in EXEC)
sup_titles = " / ".join(c["title"] for c in SUP)
round_block = (
    "\n## 轮次 2026-09-09（+8）\n\n"
    "> 四十轮 enrich：新增 8 卡（③ 高管间 +3：" + exec_titles +
    "；② 上下级 +5：" + sup_titles +
    "）。无 peer，relation 仅取 supervisor/exec。\n"
    "> 线上预览：" + PAGES + "/afternoontea.html ｜ 本轮独立页：" + RUN_PAGE + "\n"
)
acc_idx = note.find("累计 330 卡")
assert acc_idx != -1, "new count line not found"
nl = note.find("\n", acc_idx)
note = note[:nl+1] + round_block + note[nl+1:]
with io.open(OBS_NOTE, "w", encoding="utf-8") as f:
    f.write(note)
print("updated obsidian note:", OBS_NOTE)

# ---------- 4b. runs independent note ----------
os.makedirs(os.path.dirname(RUNS_NOTE), exist_ok=True)
rows = []
for i, c in enumerate(CARDS, 1):
    rel = "③高管间" if c["relation"] == "高管间" else "②上下级"
    src = "一手" if c["source"] == "一手" else "二手"
    rows.append("| %d | %s | %s | %s | %s | %s |" % (i, c["title"], rel, src, c["cat"], c["url"]))
runs_md = (
    "---\ntitle: 下午茶研讨 第四十轮 知识卡\n"
    "tags: [知识采集, 下午茶, 活动/ai]\n"
    "date: 2026-09-09\ntype: 自动化采集\n"
    "relation: ②上下级 / ③高管间\n---\n\n"
    "# 下午茶研讨 · 第四十轮补采知识卡（独立笔记）\n\n"
    "> 采集于 2026-09-09 ｜ 8 卡（③高管间 3 / ②上下级 5）。\n"
    "> 独立页 GitHub Pages：" + RUN_PAGE + "\n"
    "> 本地路径：" + SUB + "/runs/afternoontea-2026-09-09-r40.html\n"
    "> 累计总索引：" + PAGES + "/afternoontea.html\n\n"
    "## 本轮卡表\n\n"
    "| # | 卡片 | 关系档 | 一/二手 | 分类 | 来源 |\n"
    "|--|--|--|--|--|--|\n" + "\n".join(rows) + "\n"
)
with io.open(RUNS_NOTE, "w", encoding="utf-8") as f:
    f.write(runs_md)
print("wrote runs note:", RUNS_NOTE)

# ---------- 5. 00-index ----------
with io.open(OBS_00, "r", encoding="utf-8") as f:
    idx00 = f.read()
rows00 = []
for c in CARDS:
    rel = "③高管间" if c["relation"] == "高管间" else "②上下级"
    src = "一手" if c["source"] == "一手" else "二手"
    rows00.append("| %s（afternoontea.html） | 4 | %s | %s | %s |" % (c["title"], src, rel, c["val"][:55]))
newblock = "\n".join(rows00) + "\n"
last = idx00.rfind("（afternoontea.html）")
assert last != -1
endl = idx00.find("\n", last)
idx00 = idx00[:endl+1] + newblock + idx00[endl+1:]
with io.open(OBS_00, "w", encoding="utf-8") as f:
    f.write(idx00)
print("updated 00-index, +%d rows" % len(rows00))
print("DONE")
