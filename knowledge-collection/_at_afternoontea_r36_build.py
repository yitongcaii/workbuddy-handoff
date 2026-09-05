# -*- coding: utf-8 -*-
"""R36 enrich for 下午茶研讨 (afternoontea). 2026-09-06. 12 cards (③×3 + ②×9)."""
import json, os, io

BASE = os.path.dirname(os.path.abspath(__file__))
SUB = os.path.join(BASE, "afternoontea")
SUM = os.path.join(SUB, "afternoontea.html")
INC = os.path.join(SUB, "afternoontea-20260906.html")
IDX = os.path.join(BASE, "index.json")
OBS_NOTE = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\afternoontea\下午茶研讨-知识卡汇总.md"
OBS_00 = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
ROUND = "三十六轮 enrich 2026-09-06(+12)"
DATE = "2026-09-06"
PAGES = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/afternoontea"

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
        '      <div class="src">🔗 <a href="%s" target="_blank">%s</a></div>\n'
        '      <div class="note">适用：%s</div>\n'
        '    </div>\n'
    ) % (c["emoji"], c["title"], c["cat"], rcls, rel, scls, c["source"],
         c["val"], c["how"], c["url"], c["url"], c["note"])

# ③ 高管间 (exec) = 3  | ② 上下级 (supervisor) = 9
CARDS = [
 # ===== ③ 高管间 =====
 {"emoji":"🌉","relation":"高管间","source":"一手",
  "title":"广州「科创下午茶」走进香港·穗港科创协同跨境茶叙",
  "cat":"科创跨境茶叙",
  "val":"广州市科协联合香港机电工程署等在港办2026广州「科创下午茶」香港专场（主题「科创融湾区，AI筑未来」），市科协党组书记/香港机电工程署署长等致辞，超120名穗港科创专家、企业、金融机构代表参加；政策双向赋能+主题分享+项目路演，搭建穗港成果转化与招商引资对接平台，推动创新要素跨境流动。",
  "how":"办跨境科创茶叙学广州「科创下午茶进香港」：把茶叙搬到境外总部、用「政策宣讲+主题分享+项目路演」三段替代单纯座谈，让穗港两地科创领袖与资本在同一茶桌对接；适合大湾区/科协做跨境协同品牌，关键是「以茶为纽带」把招商与成果转化合二为一、跨境零距离。",
  "url":"https://kjj.gz.gov.cn/xwlb/yw/content/post_10850817.html",
  "note":"③ 广州市科协党组书记 × 香港机电工程署署长/穗港科创企业领袖（广州市科协官网一手；穗港跨境科创下午茶，可作大湾区协同茶叙范本）。"},
 {"emoji":"🏭","relation":"高管间","source":"一手",
  "title":"阿拉善高新区政企下午茶·项目审批服务专场「企业吹哨、部门报到」",
  "cat":"政企下午茶",
  "val":"阿拉善高新区办「审批赋能发展，协同共筑共赢」政企下午茶（项目审批专场），示范区管委会副主任与8家驻区重点企业代表、5个部门负责人围坐；聚焦项目审批全流程痛点，企业逐一提诉求、部门现场「把脉问诊」逐一回应，实现「一对一精准回应+多对一协同会商」，推动政务服务从被动响应转向主动赋能。",
  "how":"办政企下午茶学阿拉善「审批专场」定位：不泛泛而谈、单场只盯「项目审批」一类痛点，让管委会领导与重点企业代表围坐、企业提诉求部门当场接招；适合园区/高新区做精准纾困，关键是「专场化+现场把脉」把茶叙变成真解决问题的会。",
  "url":"https://gxq.als.gov.cn/art/2026/3/12/art_7041_526691.html",
  "note":"③ 管委会副主任 × 驻区重点企业负责人（阿拉善高新区管委会官网一手；项目审批专场政企茶叙，可作园区精准纾困范本）。"},
 {"emoji":"🍵","relation":"高管间","source":"二手",
  "title":"狮山总商会「得闲饮茶」茶话会·企业家共话「走出去/留下来/活下去」",
  "cat":"商会茶话会",
  "val":"狮山总商会「得闲饮茶」走进华兴玻璃，主题「华堂闲叙，兴商以韧」；企业家围绕国际形势影响，聚焦三大核心选择——跨区域发展(走出去)、本地增资扩产(留下来)与保守经营(活下去)深入探讨；并就数字化智能化改造降本增效、内循环产业链协同、一代二代常态化沟通机制达成共识；会长勉励抱团构建区域韧性。",
  "how":"办商会茶话会学狮山「得闲饮茶」：用粤式饮茶的松弛感替代正式座谈，让企业家围绕「走出去/留下来/活下去」真实经营选择题深聊、彼此支招；适合商会/行业协会做会员赋能，关键是「把经营真难题摆上茶桌」让同圈层企业家互解而非听讲座。",
  "url":"http://www.fsgcc.cn/shjs/shdt/content/post_1009060.html",
  "note":"③ 商会会长 × 会员企业家（佛山市工商联官网二手；粤式「得闲饮茶」企业家韧性对话，可作商会茶话会范本）。"},
 # ===== ② 上下级 =====
 {"emoji":"🏛️","relation":"上下级","source":"二手",
  "title":"桂林市四家班子离退休领导2026年新春茶话会·市委书记向老领导问计",
  "cat":"离退休茶话会",
  "val":"桂林市四家班子离退休领导2026年新春茶话会，市委书记李楚出席讲话、市长主持；李楚向老领导老同志致以问候，感谢其为桂林发展贡献，并介绍世界级旅游城市建设成效；希望老同志永葆政治本色、多提宝贵意见、贡献「银发力量」；市委市政府将持续用心用情做好老领导服务保障。",
  "how":"办离退休领导茶话会学桂林「市四家班子同场问计」：市委书记亲自出席向老领导通报发展成效、当面请教，把茶话会做成「致敬+问计」双轨；适合地方/机关做离退休干部关怀，关键是让老同志感受被尊重、被需要，把经验变「银发智库」。",
  "url":"https://finance.sina.cn/2026-02-28/detail-inhpkxuc6039883.d.html",
  "note":"② 市委书记 × 离退休老领导（新浪财经二手；四家班子离退休领导新春茶话会，可作机关致敬问计范本）。"},
 {"emoji":"🏔️","relation":"上下级","source":"一手",
  "title":"拉萨市离退休干部迎春节藏历新年茶话会·市委副书记与老同志共话发展",
  "cat":"离退休茶话会",
  "val":"拉萨市2026年离退休干部迎春节、藏历新年茶话会在乃仓酒店举行，市委副书记/组织部部长等出席与离退休干部共聚；受市委书记委托向全市离退休干部致以敬意，肯定其为拉萨发展的建设者见证者；强调2026年希望老同志发扬「离岗不离党、退休不褪色」精神，发挥政治经验威望优势建言献策、讲好拉萨故事。",
  "how":"办离退休干部茶话会学拉萨「双节同庆+委托致辞」：把春节与藏历新年并办、市委领导受书记委托向老同志致意，突出「离岗不离党」的政治礼遇；适合民族地区/机关做老干部关怀，关键是用节庆温度+政治尊重让离退休同志有归属感、愿献智。",
  "url":"https://www.lasa.gov.cn/lasa/lsyw/202602/a5585b1040444a01a62125ea691782ec.shtml",
  "note":"② 市委副书记/组织部部长 × 离退休干部（拉萨市政府官网一手；藏历新年离退休干部茶话会，可作民族地区机关关怀范本）。"},
 {"emoji":"🌿","relation":"上下级","source":"一手",
  "title":"武冈市离退休干部2026年迎春茶话会·市委书记现场听老同志建言",
  "cat":"离退休茶话会",
  "val":"武冈市离退休干部2026年迎春茶话会，市委书记出席讲话、市长通报全市经济社会发展情况；离退休干部代表先后发言对武冈发展提意见建议，现场暖意融融；市委书记感谢老领导打下坚实基础，希望其发挥政治经验威望优势出谋划策、协助做好群众工作、促进年轻干部成长；要求各级用心用情落实老干部政策待遇。",
  "how":"办离退休干部茶话会学武冈「书记听建言+部署保障」：市长先通报发展实情、再开放老同志现场提建议、市委书记当场回应并部署老干部服务保障；适合县级机关做温情收口，关键是「真听意见+真落实待遇」把茶话会做成代际衔接与稳定器。",
  "url":"https://www.wugang.gov.cn/wugang/nswdt/202602/d58140ec848b4ec0b799fd7a25d72497.shtml",
  "note":"② 市委书记/市长 × 离退休干部（武冈市政府官网一手；县级离退休干部迎春茶话会，可作基层机关关怀范本）。"},
 {"emoji":"🏅","relation":"上下级","source":"一手",
  "title":"沈鼓集团劳模广场揭牌暨「弘扬劳模先进精神」劳模茶话会·董事长与劳模同席",
  "cat":"劳模茶话会",
  "val":"沈鼓集团举行劳模广场揭牌仪式暨劳模先进茶话会，党委书记/董事长兼CEO戴继双、总裁等集团领导与劳模代表共同揭牌并座谈；戴继双向劳模致以敬意，感谢其示范引领与突出贡献，希望劳模持续发挥先锋模范带头作用；要求健全常态化联系劳模机制、完善人才培养与激励体系，营造全员学习劳模浓厚氛围。",
  "how":"办企业劳模茶话会学沈鼓「地标揭牌+茶话座谈」双仪式：先建劳模广场作精神地标、再让董事长与劳模围坐同席，把荣誉可视化、把关怀坐实到桌前；适合有劳模梯队的企业做代际传承，关键是「让劳模被看见+领导当面致敬」激发全员见贤思齐。",
  "url":"https://www.shengu.com.cn/m/zhanhuidongtai/2107.html",
  "note":"② 集团党委书记/董事长 × 劳模代表（沈鼓集团官网一手；劳模广场揭牌+茶话会，可作企业劳模传承范本）。"},
 {"emoji":"🍃","relation":"上下级","source":"二手",
  "title":"江北区总工会劳模工匠端午主题沙龙·「以茶修心」涵养匠心",
  "cat":"劳模工匠沙龙",
  "val":"宁波江北区总工会、区劳模工匠协会联合办「以茶修心，以劳践行」端午主题沙龙，全区二十余名劳模工匠代表以茶为媒、以匠会友；全国劳模/协会会长致辞，指出品茶之道与匠人之路同理（静心沉淀、精益求精）；评茶师讲解白茶品鉴，工匠们在茶香中舒缓压力、分享藏茶心得、凝聚共识；协会将持续搭技术攻关与师徒结对平台。",
  "how":"办劳模工匠沙龙学江北「以茶修心+匠心共鸣」：用端午茶叙替代表彰大会，让劳模工匠在品茗中卸压、以茶喻匠（静心沉淀=深耕致远）自然引出工匠精神；适合工会做劳模关爱，关键是「轻仪式+强共鸣」把政治荣誉落到身心舒缓与师徒传承。",
  "url":"https://nb.ifeng.com/c/8tW9RtKj6Ws",
  "note":"② 区总工会/劳模工匠协会 × 劳模工匠代表（凤凰网宁波二手；端午茶修心劳模工匠沙龙，可作工会匠心关爱范本）。"},
 {"emoji":"🤝","relation":"上下级","source":"一手",
  "title":"青羊区新联会2026「聚同心 谋发展」主题汇智茶叙·统战部与新阶层围坐",
  "cat":"新阶层茶叙",
  "val":"青羊区委统战部指导、区新联会主办「航程有你·新心相联」2026「聚同心 谋发展」主题汇智茶叙，区委统战部副部长与新联会会长、各分会负责人等30余位代表围坐；会长总结2025工作并展望2026，代表结合产业协同、人才引育、航空配套建言；副部长强调发挥思想政治引领、搭建政企社资源共享平台、擦亮「新心相联」品牌。",
  "how":"办新阶层茶叙学青羊「汇智茶叙」：统战部领导与新阶层代表围坐、以「主题分享+自由交流」替代宣贯，让新阶层人士围绕区域发展真建言；适合统战/新联会做联谊赋能，关键是「轻茶叙+重汇智」把组织凝聚力转化成发展建议。",
  "url":"https://www.sctyzx.gov.cn/cd/202603/54320651.html",
  "note":"② 区委统战部副部长 × 新的社会阶层代表（四川统一战线官网一手；新联会汇智茶叙，可作统战新阶层联谊范本）。"},
 {"emoji":"🎓","relation":"上下级","source":"一手",
  "title":"贵州商学院「书记院长与高层次人才面对面」交流茶话会·校领导现场答疑",
  "cat":"人才茶话会",
  "val":"贵州商学院通识教育学院办「凝聚智慧，共话发展——书记院长与高层次人才面对面」交流茶话会（人才日之际），学院党委书记、院长与高层次人才/教师代表参与；人才代表结合教学科研、团队建设、生活保障畅谈感悟、围绕人才引育建言；针对校院二级管理、绩效改革等难点，书记院长逐一耐心回应、现场答疑解惑，畅通与高层次人才沟通渠道。",
  "how":"办人才茶话会学贵商「书记院长面对面」：把高层次人才请到茶桌前、校领导现场回应绩效改革等真难点，用「轻松氛围+现场答疑」替代单向汇报；适合高校/院所做人才留存，关键是「领导当面接招真问题」让人才感受被尊重、渠道被畅通。",
  "url":"https://www.gzcc.edu.cn/tsxy/contents/3164/1889.html",
  "note":"② 学院党委书记/院长 × 高层次人才代表（贵州商学院官网一手；书记院长与人才面对面茶话会，可作高校人才关怀范本）。"},
 {"emoji":"🌾","relation":"上下级","source":"二手",
  "title":"铁岭市「铁心等你 智汇新质 乡约未来」人才茶话会·组织部向专家致谢问需",
  "cat":"人才茶话会",
  "val":"铁岭市委组织部主办「铁心等你 智汇新质 乡约未来」人才茶话会，指出全市强力推进「工业强市、文旅兴市、环境立市」战略离不开专家人才智慧奉献；强调比以往更渴求人才、更珍惜人才，要健全「调度、评估、述职」闭环机制确保人才诉求有人管；会上为21位高层次优秀人才颁发引才大使聘书并开展座谈交流。",
  "how":"办人才茶话会学铁岭「组织部主办+闭环机制」：市委组织部直接牵头、向专家当面致谢并颁发引才大使聘书，把「人才诉求有人管有人办」的闭环承诺落到茶桌；适合地方组织部门做人才生态，关键是「领导机关主动走近人才+制度化回应」让人才当家人。",
  "url":"https://new.qq.com/rain/a/20260304A08OO500?refer=cp_1009",
  "note":"② 市委组织部 × 高层次优秀人才（腾讯新闻二手；组织部主办人才茶话会+引才大使，可作地方人才生态范本）。"},
 {"emoji":"🌸","relation":"上下级","source":"二手",
  "title":"禅城高层次人才新春茶话会·区领导与人才围坐早茶共话发展",
  "cat":"人才茶话会",
  "val":"禅城区举行2026年高层次人才新春茶话会，区委常委/副区长与科技教育医疗文化等领域高层次人才代表欢聚，在围坐交流中畅叙情谊共话禅城新篇章；区领导代表区委区政府致新春问候、回顾发展成效，并热切期盼人才做好禅城「代言人」「推介官」吸引更多人才项目落地；茶话会后人才代表共参与「行通济」民俗巡游。",
  "how":"办人才茶话会学禅城「早茶围坐+城市代言」：把新春茶话会放进轻松早茶场景、区领导与人才边品茶边聊城市未来，并借「行通济」民俗把关怀延伸到文化体验；适合地方政府做人才「强磁场」，关键是「以一座城诚意+轻场景」让人才有归属感、愿做推介官。",
  "url":"https://new.qq.com/rain/a/20260306A05WJV00?refer=cp_1009",
  "note":"② 区委常委/副区长 × 高层次人才代表（腾讯新闻二手；高层次人才新春早茶围坐，可作地方人才关怀范本）。"},
]

EXEC = [c for c in CARDS if c["relation"] == "高管间"]
SUP = [c for c in CARDS if c["relation"] == "上下级"]
print("exec=%d sup=%d total=%d" % (len(EXEC), len(SUP), len(CARDS)))

# ---------- 1. increment page ----------
def build_page(cards_exec, cards_sup):
    sec3 = "".join(card_html(c) for c in cards_exec)
    sec2 = "".join(card_html(c) for c in cards_sup)
    tpl = (
        '<!DOCTYPE html>\n<html lang="zh-CN">\n<head>\n<meta charset="UTF-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        '<title>下午茶研讨 · 知识采集卡片墙（三十六轮 2026-09-06）</title>\n'
        + CSS + '\n</head>\n<body>\n<div class="wrap">\n'
        '<div class="hero">\n'
        '    <h1>🍵 下午茶研讨 · 知识采集卡片墙（三十六轮增量）</h1>\n'
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
        '<footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>\n'
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

# ---------- 2. inject into summary wall ----------
with io.open(SUM, "r", encoding="utf-8") as f:
    wall = f.read()

# update hero round text
old_hero = "三十五轮 enrich 2026-09-05(+8)</p>"
new_hero = "三十五轮 enrich 2026-09-05(+8)｜ 三十六轮 enrich 2026-09-06(+12)</p>"
assert old_hero in wall, "hero anchor not found"
wall = wall.replace(old_hero, new_hero, 1)

# update counts
assert '<span class="tag">103 卡</span>' in wall
assert '<span class="tag">179 卡</span>' in wall
wall = wall.replace('<span class="tag">103 卡</span>', '<span class="tag">106 卡</span>', 1)
wall = wall.replace('<span class="tag">179 卡</span>', '<span class="tag">188 卡</span>', 1)

# insert exec cards after first grid, sup cards after sec2 grid
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
print("updated summary wall:", SUM)

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
# header / 累计 update
note = note.replace("（278 卡 · 上下级/高管间）", "（290 卡 · 上下级/高管间）", 1)
note = note.replace("date: 2026-09-05", "date: 2026-09-06", 1)
note = note.replace(
    "累计 278 卡（③高管间 103 / ②上下级 179；一手 94 + 二手 184）。",
    "累计 290 卡（③高管间 106 / ②上下级 188）。", 1)

exec_titles = " / ".join(c["title"] for c in EXEC)
sup_titles = " / ".join(c["title"] for c in SUP)
round_block = (
    "\n## 轮次 2026-09-06（+12）\n\n"
    "> 三十六轮 enrich：新增 12 卡（③ 高管间 +3：" + exec_titles +
    "；② 上下级 +9：" + sup_titles +
    "）。无 peer，relation 仅取 supervisor/exec。\n"
    "> 线上预览：" + PAGES + "/afternoontea.html ｜ 本轮增量页：" + PAGES + "/afternoontea-20260906.html\n"
)
# insert after 累计 line
acc_idx = note.find("累计 290 卡")
nl = note.find("\n", acc_idx)
note = note[:nl+1] + round_block + note[nl+1:]
with io.open(OBS_NOTE, "w", encoding="utf-8") as f:
    f.write(note)
print("updated obsidian note:", OBS_NOTE)

# ---------- 5. 00-index ----------
with io.open(OBS_00, "r", encoding="utf-8") as f:
    idx00 = f.read()
rows = []
for c in CARDS:
    rel = "③高管间" if c["relation"] == "高管间" else "②上下级"
    src = "一手" if c["source"] == "一手" else "二手"
    rows.append("| %s（afternoontea.html） | 4 | %s | %s | %s |" % (c["title"], src, rel, c["val"][:55]))
newblock = "\n".join(rows) + "\n"
# append after last afternoontea.html line
last = idx00.rfind("（afternoontea.html）")
assert last != -1
endl = idx00.find("\n", last)
idx00 = idx00[:endl+1] + newblock + idx00[endl+1:]
with io.open(OBS_00, "w", encoding="utf-8") as f:
    f.write(idx00)
print("updated 00-index, +%d rows" % len(rows))
print("DONE")
