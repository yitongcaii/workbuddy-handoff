# -*- coding: utf-8 -*-
"""R38 enrich for 下午茶研讨 (afternoontea). 2026-09-07. 12 cards (③×7 + ②×5)."""
import json, os, io

BASE = os.path.dirname(os.path.abspath(__file__))
SUB = os.path.join(BASE, "afternoontea")
SUM = os.path.join(SUB, "afternoontea.html")
INC = os.path.join(SUB, "afternoontea-20260907b.html")
IDX = os.path.join(BASE, "index.json")
OBS_NOTE = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\afternoontea\下午茶研讨-知识卡汇总.md"
OBS_00 = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
ROUND = "三十八轮 enrich 2026-09-07(+12)"
DATE = "2026-09-07"
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

# ③ 高管间 (exec) = 7  | ② 上下级 (supervisor) = 5
CARDS = [
 # ===== ③ 高管间 =====
 {"emoji":"🤝","relation":"高管间","source":"一手",
  "title":"福安市企业家新春茶话会·书记市长与乡贤企业家围坐招商",
  "cat":"政企新春茶话会",
  "val":"福安市举行企业家新春茶话会，市委书记黄其山、市长许春林等市四套班子领导与驻外商会乡贤、驻外人才工作站、在外乡贤及本地企业家代表欢聚；市长作招商推介并通报发展成效，强调建立服务企业「四通四到」机制、落实「五个一」政务服务行动纲领，打响「如我在商，营在福安」品牌；现场颁发人文摄影奖，寄语乡贤当好发展「合伙人」「智囊团」「金话筒」。",
  "how":"办政企新春茶话会学福安「四套班子同场+招商推介」：让书记市长与乡贤企业家围坐，把招商说明会融进茶叙、用「四通四到/五个一」机制把营商环境承诺落到桌面；适合县域做乡贤经济，关键是「以乡情聚人+以机制留商」让在外企业家愿回乡投资。",
  "url":"http://www.fjfa.gov.cn/zwgk/yw/fayw/202602/t20260224_2442930.htm",
  "note":"③ 市委书记/市长 × 驻外商会乡贤/本地企业家（福安市政府官网一手；政企新春茶话会+招商推介，可作县域乡贤经济范本）。"},
 {"emoji":"🍊","relation":"高管间","source":"二手",
  "title":"内江市「甜城下午茶」首期·市委书记与企业家围坐圆桌制度化沟通",
  "cat":"制度化政企茶叙",
  "val":"内江首期「甜城下午茶」企业服务日，市委书记冯发贵与20余位企业家围坐圆桌、企业家占C位；提出制度化沟通约定「固定333、常态12345」（每月第三周周三15时固定举办、诉求可拨12345）、「想来就来说完再见」「当场答复回音闭环」；现场企业家抢麦提原料保供、数据共享、电力扩容等痛点，部门负责人当场接招拍板。",
  "how":"办政企茶话会学内江「甜城下午茶」制度化四招：围坐式去主席台+企业家C位+视频连线上异地企业+「固定时间/当场拍板/件件回音」闭环；适合地市做企业服务日，关键是把一次性座谈变成「月月有约、事事有回音」的制度，让企业家敢提真问题。",
  "url":"https://www.scjjrb.com/2026/05/14/99463789.html",
  "note":"③ 市委书记 × 重点企业家（四川经济网二手；「甜城下午茶」制度化政企沟通，可作地市企业服务日范本）。"},
 {"emoji":"🏜️","relation":"高管间","source":"二手",
  "title":"敦煌「商聚沙州·亲清共话」企业下午茶·营商闭环机制",
  "cat":"亲清营商茶叙",
  "val":"敦煌市2026年第四期「商聚沙州·亲清共话」企业下午茶在政务服务中心「亲清营商环境服务站」举办，市商务局、市场监管局、税务局等部门负责人与6家民营企业代表围坐，以清茶拉近距离、坦诚交流；建立「诉求收集—现场答复—台账督办—进度反馈」闭环处置机制，已收集31条意见诉求、答复31条，擦亮「亲清下午茶」营商服务品牌。",
  "how":"办亲清下午茶学敦煌「服务站+闭环机制」：把茶叙搬进政务大厅「亲清营商环境服务站」、部门负责人与民企代表围坐，用「收集—答复—督办—反馈」四步闭环把诉求件件落地；适合县市做营商品牌，关键是「以茶破冰+以闭环见诚信」让民企敢说话、难题有人管。",
  "url":"https://m.thepaper.cn/newsDetail_forward_33783439",
  "note":"③ 商务局/市场监管局/税务局负责人 × 民营企业代表（澎湃新闻二手；「亲清下午茶」营商闭环机制，可作县市营商服务范本）。"},
 {"emoji":"🚗","relation":"高管间","source":"二手",
  "title":"巴中市「巴商茶间荟」政银企融资对接·行业专场一对一",
  "cat":"政银企融资对接",
  "val":"巴中市第11期「巴商茶间荟」专题子活动以「政银企融资对接」为主题，在先锋汽车产业园举行；市汽车行业协会、先锋/万信/金华泰等10家重点汽车企业负责人，与市财政局、市工商联、市融资服务中心及工行、建行、农商行等多家金融机构信贷负责人面对面；市财政局现场解读融资政策、各机构推介信用贷/库存融资/天府服保贷等产品，「一对一」对接达成初步合作意向。",
  "how":"办政银企融资茶叙学巴中「巴商茶间荟」常态化专场：依托固定品牌平台、按行业（汽车）设子题，把政府/工商联/财政与银行信贷负责人和企业家拉到同一茶桌「一对一」对接；适合地市做融资纾困，关键是「品牌化+行业专场+现场授信」把融资对接做成可预期常态。",
  "url":"http://bzgsl.gov.cn/list.asp?NewsID=12900",
  "note":"③ 市工商联/财政局/融资服务中心 × 汽车企业负责人 × 银行信贷负责人（巴中市工商联官网二手；「巴商茶间荟」政银企融资对接，可作常态化解困范本）。"},
 {"emoji":"💡","relation":"高管间","source":"一手",
  "title":"江海区女企业家茶话会「闪闪发亮的姐姐」·妇联与女企围坐解题",
  "cat":"女企业家茶话会",
  "val":"江门市江海区妇联联合区企业发展服务中心在产业园「企业加油站」办「闪闪发亮的姐姐」女企业家主题茶话会，区妇联负责人与十余位女企业家围坐；先走产业共享展厅感知区域机遇，再座谈敞开心扉聊技术创新、市场拓展、人才引进、融资等共性挑战，以「一人提问、众人献策」破题；区企业服务中心介绍惠企举措，现场设职场形象小课堂，为女性创业者营造放松充电空间。",
  "how":"办女企业家茶话会学江海「姐妹茶叙+实战解题」：区妇联与女企围坐、用「一人提问众人献策」替代单向宣讲，把形象课堂等轻仪式融进赋能；适合妇联/园区做女性创业关怀，关键是「以松弛场景卸压+以跨行业视角支招」让女企找到共鸣与方向。",
  "url":"http://www.jianghaiqu.net/jhqfl_113/gzdt_148172/202602/t1059200.html",
  "note":"③ 区妇联负责人 × 女企业家代表（江海区政府官网一手；「闪闪发亮的姐姐」女企业家茶话会，可作妇联赋能范本）。"},
 {"emoji":"🌏","relation":"高管间","source":"一手",
  "title":"中山市侨联侨界新春茶话会·主席与海外侨胞以茶引智",
  "cat":"侨界茶话会",
  "val":"中山市侨联举办第39届慈善万人行后的侨界新春茶话会，市侨联主席与来自美加澳等13个国家和地区的近30名侨胞乡亲围坐；宣介省市高质量发展大会精神、通报侨联年度工作，侨胞倡议当好中外交流「桥梁纽带」、引技术引项目回流；市侨联表态做侨胞「主力军/贴心人/实干家」，带着资源、项目、人才回来共享发展红利。",
  "how":"办侨界茶话会学中山「以茶叙侨情+以桥引智」：侨联主席与海外侨胞围坐汤圆叙乡情，把高质量发展机遇讲透、把「引技术引项目引人才」邀请说实；适合侨乡/统战做引资引智，关键是「以乡情为纽带+以家乡机遇为钩」让侨胞愿当中外桥梁、带资源回流。",
  "url":"http://zsql.org.cn/article/view/cateid/57/id/38258.html",
  "note":"③ 市侨联主席 × 海外侨胞乡亲（中山市侨联官网一手；侨界新春茶话会，可作侨联引资引智范本）。"},
 {"emoji":"🤝","relation":"高管间","source":"一手",
  "title":"茂名市港澳台同胞迎春茶话会·统战部长与同胞三大角色寄语",
  "cat":"港澳台同胞茶话会",
  "val":"茂名市举办2026年港澳台同胞迎春茶话会，由市委台港澳办主办，市委常委、统战部长吴卫华出席讲话，市人大/政府/政协领导及台胞台商台属、港澳同胞、企业代表、港澳社团负责人等约220人参加；传达港澳台工作精神、回顾发展成效，寄语同胞做国家统一维护者、高质量发展建设者、交流融合推动者，持续优化营商环境支持港澳台企业在茂发展。",
  "how":"办港澳台同胞茶话会学茂名「统战部长主场+三大角色寄语」：市委统战部长与220名港澳台同胞围坐、把政策精神与家乡成效讲清，再逐一寄望「维护者/建设者/推动者」三角色；适合统战/台港澳办做联谊，关键是「以家国叙事聚共识+以营商承诺稳信心」让同胞愿投资扎根。",
  "url":"http://www.maoming.gov.cn/zwgk/zwhd/content/post_1581301.html",
  "note":"③ 市委常委/统战部长 × 港澳台同胞/企业代表（茂名市政府官网一手；港澳台同胞迎春茶话会，可作统战联谊范本）。"},
 # ===== ② 上下级 =====
 {"emoji":"🏭","relation":"上下级","source":"一手",
  "title":"中铝股份劳模工匠座谈会·董事长与劳模围坐致敬部署",
  "cat":"劳模工匠座谈",
  "val":"中铝股份「五一」前召开劳模工匠座谈会，党委书记、董事长何文建出席讲话，向各级各类先进集体和先进工作者祝贺、向全体职工致敬；强调强化政治引领、坚持人民至上增进民生福祉、聚焦人才强企锻造一流队伍、厚植文化基因、争做实干先锋；劳模工匠代表作交流发言，有关部门负责人参加，弘扬劳模精神劳动精神工匠精神。",
  "how":"办企业劳模工匠座谈学「中铝五一座谈」：董事长与劳模工匠围坐、把「致敬+部署」双轨做成思想政治引领与人才强企的载体，提出建好「四支」人才队伍、深化产业工人改革；适合央企/国企做先进表彰，关键是「领导当面致敬+把劳模精神落到人才机制」让先进有荣誉、职工有方向。",
  "url":"https://www.chalco.com.cn/xwdt/gsyw/202605/t20260507_168544.html",
  "note":"② 集团党委书记/董事长 × 劳模工匠代表（中铝股份官网一手；五一劳模工匠座谈，可作国企先进引领范本）。"},
 {"emoji":"🏙️","relation":"上下级","source":"一手",
  "title":"福田区五一劳模工匠宣讲暨座谈·领导与劳模围坐凝力",
  "cat":"劳模宣讲座谈",
  "val":"福田区在河套深港职工服务中心办「聚力筑新程 实干创未来」五一劳模工匠宣讲暨座谈，市总工会副主席、区委副书记、区总工会主席等领导与劳模工匠、职工代表齐聚；3位劳模登台讲一线奋斗故事（教育/能源/建筑数字化），座谈环节区总工会通报劳模培育与产改成效、听取劳模发言并致以敬意，强调发挥示范引领、当好职工「娘家人」。",
  "how":"办劳模工匠活动学福田「宣讲+座谈」双环节：先让劳模登台讲真实奋斗故事感染全场，再领导与劳模围坐听建议、表敬意，把「劳模培育/技能提升/新就业关爱」成效现场通报；适合城区工会做五一庆祝，关键是「以故事动人+以座谈凝力」让劳模精神可感、职工归属感更强。",
  "url":"https://www.szft.gov.cn/bmxx_qt/qzgh/ghdt/content/post_12758418.html",
  "note":"② 区总工会/区委领导 × 劳模工匠代表（福田区政府官网一手；五一劳模工匠宣讲暨座谈，可作城区工会范本）。"},
 {"emoji":"🌿","relation":"上下级","source":"一手",
  "title":"青浦区「人才面对面」迎新春·区长与高层次人才问需问计",
  "cat":"人才面对面",
  "val":"青浦区举行「人才面对面」迎新春活动（2026「跨界·青峰π」人才面对面系列首场），区委副书记、区长与区委常委、组织部部长同各领域高层次人才齐聚；区长指出人才是「第一资源」、青浦正打造长三角创新枢纽，将升级人才政策、完善创新创业全周期服务，希望人才推介青浦吸引项目落地；组织华为、美的、网易等重点企业人才搭建政府与人才情感桥梁、问需问计于才。",
  "how":"办人才面对面学青浦「区长主场+系列化」：把人才迎新做成「跨界·青峰π」系列首场、区长与组织部长同高层次人才围坐问需问计，并用重点企业人才营造「第二故乡」认同；适合新城/枢纽城区做人才生态，关键是「领导直接听才+制度化系列」让人才献策有通道、归属有依托。",
  "url":"https://www.shqp.gov.cn/shqp/zwhd/20260213/1351911.html",
  "note":"② 区委副书记/区长 × 高层次人才代表（青浦区政府官网一手；「人才面对面」迎新春，可作城区人才生态范本）。"},
 {"emoji":"🍵","relation":"上下级","source":"二手",
  "title":"仁寿一中青年教师交流沙龙·书记校长与新教师便利贴心声",
  "cat":"青年教师沙龙",
  "val":"仁寿一中南校区办青年教师暖心沙龙，校党委书记、校长、副校长与近三年入职新教师围坐畅谈成长；新教师卸下拘谨聊校园趣事与教学小困惑，在便利贴写心里话，马倩老师分享成长经历「多向前辈请教、博采众长」；党委书记解读「青衿致远」主题、叮嘱新教师守校风初心、平衡工作生活，学校做成长最坚实后盾。",
  "how":"办青年教师沙龙学仁寿一中「暖心围坐+便利贴心声」：校党委书记校长与新教师茶叙、用便利贴收集真实困惑与期待替代汇报，再让骨干老师「传经送宝」；适合学校做新教师融入，关键是「领导平等落座+轻仪式倾听」让新教师敢说真话、短期内找到节奏与归属感。",
  "url":"https://life.china.com/2026-03/27/content_557752.html",
  "note":"② 校党委书记/校长 × 近三年新入职教师（中华网生活二手；青年教师暖心沙龙，可作学校新教师关怀范本）。"},
 {"emoji":"🍎","relation":"上下级","source":"二手",
  "title":"达州中学新进教师茶话会·领导赠礼前辈传经",
  "cat":"新教师茶话会",
  "val":"四川省达州中学杨柳校区新春前夕办新进教师茶话会，校级领导、全体中层干部、年级主任与新进教师齐聚；副校长代表学校致欢迎、优秀老师倾囊相授成长心得，党支部书记赠新春福袋与暖心礼物，执行校长寄语青年教师牢记育人初心、为学校发展注入青春动能；新教师逐一自我介绍、畅谈入职体会。",
  "how":"办新教师茶话会学达州中学「领导赠礼+前辈传经」：校级领导与新教师围坐、用福袋礼物传递关怀、让优秀教师现场分享成长，把迎新做成有温度的融入仪式；适合中小学做新教师归属，关键是「领导在场+前辈陪伴+实物关怀」让新教师倍感重视、快速扎根。",
  "url":"http://www.chinareports.org.cn/index/news/76413.html",
  "note":"② 校级领导/党支部书记 × 新进教师（中国报道网二手；新进教师茶话会，可作学校迎新关怀范本）。"},
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
        '<title>下午茶研讨 · 知识采集卡片墙（三十八轮 2026-09-07）</title>\n'
        + CSS + '\n</head>\n<body>\n<div class="wrap">\n'
        '<div class="hero">\n'
        '    <h1>🍵 下午茶研讨 · 知识采集卡片墙（三十八轮增量）</h1>\n'
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
old_hero = "三十七轮 enrich 2026-09-07(+12)</p>"
new_hero = "三十七轮 enrich 2026-09-07(+12)｜ 三十八轮 enrich 2026-09-07(+12)</p>"
assert old_hero in wall, "hero anchor not found"
wall = wall.replace(old_hero, new_hero, 1)

# update counts
assert '<span class="tag">112 卡</span>' in wall
assert '<span class="tag">194 卡</span>' in wall
wall = wall.replace('<span class="tag">112 卡</span>', '<span class="tag">119 卡</span>', 1)
wall = wall.replace('<span class="tag">194 卡</span>', '<span class="tag">199 卡</span>', 1)

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
note = note.replace("（302 卡 · 上下级/高管间）", "（314 卡 · 上下级/高管间）", 1)
note = note.replace("date: 2026-09-06", "date: 2026-09-07", 1)
note = note.replace(
    "累计 302 卡（③高管间 112 / ②上下级 194）。",
    "累计 314 卡（③高管间 119 / ②上下级 199）。", 1)

exec_titles = " / ".join(c["title"] for c in EXEC)
sup_titles = " / ".join(c["title"] for c in SUP)
round_block = (
    "\n## 轮次 2026-09-07（+12）\n\n"
    "> 三十八轮 enrich：新增 12 卡（③ 高管间 +7：" + exec_titles +
    "；② 上下级 +5：" + sup_titles +
    "）。无 peer，relation 仅取 supervisor/exec。\n"
    "> 线上预览：" + PAGES + "/afternoontea.html ｜ 本轮增量页：" + PAGES + "/afternoontea-20260907b.html\n"
)
acc_idx = note.find("累计 314 卡")
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
last = idx00.rfind("（afternoontea.html）")
assert last != -1
endl = idx00.find("\n", last)
idx00 = idx00[:endl+1] + newblock + idx00[endl+1:]
with io.open(OBS_00, "w", encoding="utf-8") as f:
    f.write(idx00)
print("updated 00-index, +%d rows" % len(rows))
print("DONE")
