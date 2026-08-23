# -*- coding: utf-8 -*-
"""颁奖典礼 二十四轮补采 (2026-08-24) — 渲染增量 + 追加进累计墙 + 更新 index.json + Obsidian + 乐享上传
仅 ②上下级 / ③高管间，0 peer。本论增量页 award-2026-08-24-r24.html。
乐享：award 主题在乐享以「每轮独立页」落库（folder_id=f585d1b78510459db0ce807cc9688448），
并 best-effort 更新累计墙（若 folder 内存在 award.html 条目则更新，否则跳过，不阻断）。"""
import json, os, re, subprocess, urllib.request, urllib.error

BASE = os.path.dirname(os.path.abspath(__file__))
AT_DIR = os.path.join(BASE, "award")
CUM = os.path.join(AT_DIR, "award.html")
IDX = os.path.join(BASE, "index.json")
DATE = "2026-08-24"
RUN_NAME = "award-2026-08-24-r24.html"
RUN_PATH = os.path.join(AT_DIR, "runs", RUN_NAME)
TMP = os.path.join(AT_DIR, ".run_newcards.tmp.html")
ROUND = 24

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---- 本轮新增卡（仅 ②上下级 / ③高管间，0 peer；8张全 NEW，URL 均经 dedup 校验未命中 index）----
# 关系档：③高管间 2 张（全二手）+ ②上下级 6 张（全二手）。填补空白：主题构思 / 物料设计 / 直播传播 / 故事传播 / 反模式 / 经理话术 / 高管致辞 / 全球执行。
CARDS = [
    {
        "emoji": "\U0001F3AF",
        "title": "颁奖典礼主题构思·让主题呼应战略而非空口号",
        "cat": "主题构思",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "颁奖主题不能停在「团结奋进/共创辉煌」这类谁都记不住的口号，应与企业当年战略或文化符号强绑定。三种落地法：①从战略提炼——技术驱动型公司用「代码之外，皆为热爱」，销售型团队用「破浪者说」；②叙事式策划——把企业的发展历程与员工成长故事结合（如众安年陈盛典「踏浪逐新」航海主题+IP形象+外滩打卡，阜丰「酵动全球·尽展丰芒」出海主题+文化长廊长卷）；③双场景联动——户外打卡区（社交分享）+室内盛典（仪式感）兼顾社交与私密。蓝互营销案例：把十周年表彰会提炼为「一颗种子」主题，每位老员工=种子，从种子到结果做动线，获奖者收到定制绿植催泪。主题一旦定，所有物料/布景/串词都围绕它展开，形成统一表达。",
        "how": "定颁奖主题别拍脑袋喊口号。先问「今年公司最想让全员记住什么」（战略/文化符号），再把主题落成可视觉化的一个意象（航海/种子/星光），让 IP、舞台、串词全部围绕它；用「户外打卡+室内盛典」双区照顾社交与仪式；主题定完就锁死，所有物料一致表达，避免各说各话。",
        "url": "https://tsight.io/articles/18572140",
        "note": "适用：② 行政/HR/品牌/活动策划（策划机构二手；主题提炼三法+战略绑定+叙事式+双场景联动，可作颁奖主题构思方法论）。",
    },
    {
        "emoji": "\U0001F3AD",
        "title": "奖杯/奖牌/证书视觉物料设计定制避坑（材质×尺寸×版权）",
        "cat": "物料设计",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "奖杯奖牌定制常见 5 大坑：①超低价引流（薄合金+缩水电镀，数月发黑掉色）→要求材质说明+样品实拍；②效果图精美、大货货不对版→锁定潘通色号/尺寸参数、留存确认设计文件；③报价模糊层层加价（刻字/底座/礼盒/模具/加急费）→要全包一口价清单；④交期随意承诺→合同写明最晚交货日+延期处理；⑤物流破损无人担→确认包装标准+破损补发。设计三原则：①深度融入企业 IP/logo/产品造型，可拼接/旋转/开合增加互动；②刻上姓名+获奖理由+日期做独一无二；③材质匹配调性（水晶通透=年会创新奖，木质温润=传统/聘书；木配暖色、水晶配冷色）。避坑清单：先定场景材质、精确量内页尺寸（10寸≠A4 高频误区）、善用免费 3D 设计、确认是否含内页、预留 15-20 天工期（紧急提前沟通加急）。",
        "how": "定制奖杯奖牌，先列「场景材质+内页尺寸+文案终稿+LOGO源文件」四件套再下单；避开超低价引流与模糊报价（要全包一口价）；合同锁死交期与延期条款；设计融入企业 IP、刻获奖者姓名与理由、材质匹配调性；务必预留 15-20 天工期，颁奖前 3-5 天弹性，绝不前一天才下单（仪式感底色是从容）。",
        "url": "https://www.kangruigift.com/public/customnews/2026guangdongjiangbeidingzhi.html",
        "note": "适用：② 行政/采购/活动执行（文创定制厂商二手；5坑清单+设计三原则+工期避坑，可作奖杯奖牌定制采购 SOP）。",
    },
    {
        "emoji": "\U0001F4E1",
        "title": "颁奖典礼直播/短视频二次传播 SOP（含 KPI 与翻录）",
        "cat": "直播传播",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "直播颁奖把「在场仪式感」放大为「全员可参与+可传播」。执行要点：①平台分层——全员公开用 YouTube/Vimeo/社交媒体，内部用 Teams/Zoom，按安全选公开/私有/密码；②把线上观众当主角——从一开始规划机位/音频/字幕/lower-third/主持人 cue 都照顾远程；③彩排——至少 1 次全要素技术排练（纠发音/冷场/死链）；④翻录再传播——做 60 秒高光 reel、把获奖者页/证书发邮件、把 clips 发社媒；案例：30 分钟虚拟颁奖 reveal，2 次排练+OBS，结果 420 直播观看、12 条 clips、85 互动、次月提名 +14%。KPI：直播观看率/提名量/聊天参与/回放/分享/下轮参与。避坑：带宽不足降码率、音频 normalization 到 -6dB、聊天派 moderator+慢速模式防跑偏。",
        "how": "做颁奖直播，先定「公开 or 内部」平台与 KPI（观看/提名/互动/回放），把线上观众纳入动线规划（机位/字幕/cue）；至少 1 次全要素彩练；典礼后立刻翻 60 秒高光+获奖者页+邮件，把一次性仪式变持续传播。把「提名量环比」当效果指标，证明认可投入值。",
        "url": "https://walloffame.cloud/live-stream-your-awards-how-to-host-an-engaging-virtual-cere",
        "note": "适用：② 行政/HR/雇主品牌/内部沟通（虚拟颁奖平台二手；平台分层+翻录 SOP+KPI+案例，可作颁奖直播执行指南）。",
    },
    {
        "emoji": "\U0001F4E3",
        "title": "颁奖后传播·获奖者故事专访 SOP（让榜样「有回声」）",
        "cat": "故事传播",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "评优失效三大症结之一是「榜样无回声」——奖颁完、合影、发奖金就结束，优秀在哪/怎么学无人追问，榜样只属于个人不属组织。破法：把颁奖当「内容生产的起点」而非终点。①24h 内出回顾推文+获奖者故事专访（人物稿/短视频），把「做了什么」讲成「为什么值」，沉淀可学的方法；②设固定栏目（内刊/知识库/公众号「奋斗者说」），每期 1-2 个获奖者深度故事，配具体场景与数据；③让获奖者做内部分享/带教，把个人经验变团队资产；④用提名理由反向提炼「组织当前最想要的行为」，回灌下轮评选标准。常见失焦：致词抢镜、得奖理由笼统、奖太多稀释重点——都对传播不利。",
        "how": "颁奖别止于当晚。建立「颁奖后 24h 出故事+固定栏目持续连载+获奖者内部分享」三段式，让榜样有回声：把获奖事迹写成可学的方法（具体场景+数据），用栏目沉淀，让获奖者带教把个人经验变组织资产；用提名理由反向校准下轮评选标准。避免「奖颁完就收聚光灯」。",
        "url": "https://www.toutiao.com/article/7602817604655088166/",
        "note": "适用：② 行政/HR/文化/内部传播（头条评论二手；评优失灵三症结+榜样有回声 SOP，可作颁奖后传播机制）。",
    },
    {
        "emoji": "⚠️",
        "title": "颁奖翻车反模式案例集（5大NG+评先五忌）",
        "cat": "反模式",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "企业颁奖常见翻车点实录：①致词抢颁奖锋头（主管致词过长，焦点从「表扬员工」变「主管讲话」）→致词精简、放在颁奖前后衔接；②得奖理由太笼统（只唱名颁奖，无具体事迹）→颁奖前由主持/主管讲 1-2 句具体表现；③奖项太多太杂稀释重点（数十个奖一视同仁，年度大奖失隆重）→奖项分级、重要奖置高潮+完整仪式；④摄影漏拍关键画面（漏颁奖瞬间/表情，事后无素材）→提前给摄影机位清单；⑤现场冷清缺掌声引导（照本宣科无互动）→背景乐+主持炒热+感言环节。评选侧「五忌」：轮流坐庄、网络投票刷票、分配指标凑数、集中力量造完人、领导私下圈人——后者已演化成单位亚腐败。主办人专属 5 失误：流程拖延/灯错/名错、名单未双岗核对、设备未提前测、主持稿未排演、无 Plan B。",
        "how": "避开颁奖翻车，先记「颁奖是给员工的不是给主管的」：致词压短、得奖理由讲具体事迹、奖项分级把年度大奖放高潮、摄影提前列机位清单、主持带背景乐炒热场+引导掌声；评选侧坚决防「轮流坐庄/刷票/内定」，程序透明有公示。主办人自己做 check：名单双岗核对、设备提前一周测+当天总检、主持稿逐字排演、备 Plan B（缺席代领/视频播不出/贵宾迟到）。",
        "url": "https://eastpoint.com.tw/%e8%a1%a8%e6%8f%9a%e5%a4%a7%e6%9c%83%e5%b8%b8%e8%a6%8bng%e4%ba%8b%e9%a0%85%ef%bc%9a%e9%80%99%e4%ba%9b%e7%b4%b0%e7%af%80%e5%ae%b9%e6%98%93%e5%a4%b1%e7%84%a6",
        "note": "适用：② 行政/HR/活动执行/评选负责人（台湾活动机构+党建网二手；5NG+评先五忌+主办5失误，可作颁奖避坑清单）。",
    },
    {
        "emoji": "\U0001F4AC",
        "title": "经理日常 micro-recognition 话术库（即时、具体、可抄）",
        "cat": "经理话术",
        "rel": "r2", "rel_text": "上下级",
        "src": "b2", "src_text": "二手",
        "val": "日常 micro-recognition 比年度盛典更能留人——关键是「具体+及时+真诚」，泛泛「Good job」无效。可抄话术库：①场景化肯定——「你把客户需求讲清楚了，帮我们省了时间」「早期草稿很扎实，给我们可建的基础」；②成长型——「你每周都在进步，细节越来越强」「你主动要反馈还落实了，差别很大」；③团队/低谷——「我们一起交付的，协作让这成为可能」「这段时间很难，你的投入被看见也很重要」；④9 句高力量句式——「你让复杂的事变简单」「我信任你的判断」「你注意到别人忽略的细节」「你抬高了全队的标准」「那份额外努力真的有用」「你改变了我对这事的理解」「真高兴你在这队」；⑤12 个 manager-ready 脚本（Slack 一句话/1:1 稍长/书面认可），覆盖 onboarding 助力、加班风险（表扬+减负）、高质量交付、跨团队调解、超额达标、新人早期影响、创意解题、可靠 quiet contributor、学以致用。原则：命名行为+说明影响+（可选）下一步；及时（贴近动作最有冲击）；双向（鼓励 peer 互认）；别过度（假了反而空）。",
        "how": "经理日常颁奖（micro-recognition）照话术库抄：用「命名行为+说明影响」结构，避免空泛「不错」；在 Slack/站会/1:1 随时发，越贴近动作越有力量；对加班风险的人「表扬+主动减负」防捧杀；用 9 句高力量句式（信任判断/抬高标准/改变我的想法）替代套路夸；鼓励 peer 互认，别只上级对下。记住：具体+及时+真诚，过度反而空心。",
        "url": "https://cultbranding.com/9-simple-phrases-that-can-make-your-team-feel-appreciated",
        "note": "适用：② 一线经理/TL/HR（品牌文化机构+HR 媒体二手；9句式+12脚本+场景化话术库，可作经理日常认可话术锦囊）。",
    },
    {
        "emoji": "\U0001F3A1",
        "title": "CEO/高管颁奖致辞金句与结构模板（exec keynote）",
        "cat": "高管致辞",
        "rel": "r3", "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "高管颁奖致辞（exec keynote）三板斧：①开场定调——把成就归集体、把荣誉给个人，如「我们共同的交付让人骄傲，今晚属于超越预期的你」（motivational opener 模板可抄）；②表彰个人卓越——用「不只在数字，更在他对同事与文化的影响」结构，点名具体项目+可量化结果+精神内核（recognizing individual excellence 范例）；③颁奖呈词模板——「很荣幸代表[公司]颁发[奖项]，这是第[N]届，表彰在[领域]做出杰出[影响]的人；提名者都极[特质]，但有一人因[生涯贡献]脱颖而出，奖品归[姓名]，有请上台」（award presentation speech template，标准化可套）。收尾 vote of thanks：经典专业/温暖个人/激励领导三型可抄（「这份荣誉属于并肩的团队与家人的支持」）。中文领导致辞范式：年终总结式（市场+研发+团队三维成绩+表彰缩影+新战略三大发力）、科技型（「科技赋能未来」呼应创新）。注意：高管致辞忌空话堆砌、忌只念数据，要落到「人」与「行为」。",
        "how": "写高管颁奖致辞，套「集体成就→点名个人→精神升华」结构：开场把功劳归团队、把光给获奖者；表彰段用「具体项目+量化结果+文化影响」三件套，不空喊；颁奖呈词用标准模板（第几届/表彰领域/为何是他/有请上台）避免临场卡壳；收尾用 vote-of-thanks 三型之一落到团队与家人。高管致辞贵在「见人见行为」，忌数据堆砌与套话。",
        "url": "https://speecheshq.com/end-of-year-awards-ceremony-speech-samples/",
        "note": "适用：③ CEO/高管/CHRO/总裁办（演讲模板站二手；开场/表彰/呈词/vote-of-thanks 四型+中文领导致辞范式，可作高管颁奖致辞金句库）。",
    },
    {
        "emoji": "\U0001F310",
        "title": "全球跨时区颁奖执行·出海/跨国团队荣誉同步（含高管全球颁奖）",
        "cat": "全球执行",
        "rel": "r3", "rel_text": "高管间",
        "src": "b2", "src_text": "二手",
        "val": "跨国/出海团队颁奖把「总部认可」同步到全球时区，是高管级荣誉信号。执行要点：①实体奖杯仍关键——数字徽章关页面即消失，实体奖留桌面天天被看见；提前 1-2 天寄到获奖者手、直播开箱（live unboxing）造共享时刻；跨国寄送要算海关与更长时效；②平台选「多设备+互动（投票/聊天/直播问答）+沉浸设计（3D/品牌社交墙）」，用实时翻译+错峰排期照顾国际参与者；③时长 60-90 分钟封顶（再长注意力掉），用 co-host 控节奏、nominee 视频铺垫、家属朋友扩观众；④录制备选——live 有断连风险，许多主办方预录获奖感言、主持 live，兼顾可靠与即时反应；⑤高管全球颁奖战略——把全球颁奖当「文化信号+人才保留杠杆」，让海外团队感到与总部同频。KPI：跨区域观看率/提名渗透/留存相关。",
        "how": "办跨国/出海颁奖，实体奖杯提前 1-2 天寄到、直播开箱造全球共享时刻（算海关时效）；平台要支持实时翻译+错峰排期+互动；时长控 60-90 分、co-host 控场、nominee 视频铺垫；live 断连风险用「预录感言+主持 live」对冲；把全球颁奖当高管级文化信号与留人杠杆，让海外团队与总部同频。避免「只给总部的人颁奖」。",
        "url": "https://awards.com/how-to-do-a-virtual-awards-ceremony",
        "note": "适用：③ 高管/HRD/海外业务负责人（虚拟颁奖机构二手；实体奖+跨境寄送+实时翻译+高管全球颁奖战略，可作跨国团队颁奖执行指南）。",
    },
]

def card_html(c, indent=4):
    sp = " " * indent
    sp2 = " " * (indent + 2)
    rel_badge = '<span class="badge {0}">{1}</span>'.format(c["rel"], c["rel_text"])
    src_badge = '<span class="badge {0}">{1}</span>'.format(c["src"], c["src_text"])
    return (
        sp + '<div class="hl">\n'
        + sp2 + '<div class="top"><span class="emoji">' + esc(c["emoji"]) + '</span>'
        + '<h3>' + esc(c["title"]) + '</h3><span class="cat">' + esc(c["cat"]) + '</span>'
        + rel_badge + src_badge + '</div>\n'
        + sp2 + '<p class="val">' + esc(c["val"]) + '</p>\n'
        + sp2 + '<details class="exec"><summary>怎么做</summary><div class="inner">' + esc(c["how"]) + '</div></details>\n'
        + sp2 + '<div class="src">\U0001F517 <a href="' + esc(c["url"]) + '" target="_blank">' + esc(c["url"]) + '</a></div>\n'
        + sp2 + '<div class="note">' + esc(c["note"]) + '</div>\n'
        + sp + '</div>\n'
    )

def find_grid_close(h, sec_start):
    gi = h.find('<div class="grid">', sec_start)
    assert gi != -1, "grid not found"
    depth = 0
    i = gi + len('<div class="grid">')
    while i < len(h):
        if h.startswith('<div', i):
            depth += 1
            i = h.find('>', i) + 1
        elif h.startswith('</div>', i):
            if depth == 0:
                return i
            depth -= 1
            i += 5
        else:
            i += 1
    raise RuntimeError("unbalanced")

# ---- 1) 写临时新卡块 ----
open(TMP, "w", encoding="utf-8").write("".join(card_html(c) for c in CARDS))
print("临时新卡块已写:", TMP)

# ---- 2) 墙注入 ----
html = open(CUM, encoding="utf-8").read()
before = html.count('<div class="hl">')
cards_sec3 = [c for c in CARDS if c["rel"] == "r3"]
cards_sec2 = [c for c in CARDS if c["rel"] == "r2"]
assert cards_sec3 and cards_sec2
i3 = html.find('class="sec sec3"')
close3 = find_grid_close(html, i3)
html = html[:close3] + "".join(card_html(c) for c in cards_sec3) + html[close3:]
i2 = html.find('class="sec sec2"')
close2 = find_grid_close(html, i2)
html = html[:close2] + "".join(card_html(c) for c in cards_sec2) + html[close2:]
# hero
hero_old = "二十三轮 enrich 2026-08-23(+10)"
hero_new = "二十三轮 enrich 2026-08-23(+10) ｜ 二十四轮 enrich 2026-08-24(+8)"
assert hero_old in html, "hero marker not found"
html = html.replace(hero_old, hero_new, 1)
open(CUM, "w", encoding="utf-8").write(html)
after = html.count('<div class="hl">')
r2b = html.count('badge r2'); r3b = html.count('badge r3')
b1b = html.count('badge b1'); b2b = html.count('badge b2')
footer_ok = "\U0001F4CC \u672c\u9875\u7531 yitong" in html
print("累计墙卡片数:", after, "(+", after - before, ") | r2:", r2b, "r3:", r3b, "| b1:", b1b, "b2:", b2b, "| footer:", footer_ok)

# ---- 3) 独立页（gen_run_page.py，显式 --out 防嵌套路径 bug）----
gen = os.path.join(BASE, "gen_run_page.py")
r = subprocess.run(["python", gen, "--topic", "award", "--topic-name",
                    "\u9881\u5956\u5178\u793c", "--date", DATE, "--round", str(ROUND),
                    "--cards-file", TMP, "--out", RUN_PATH], capture_output=True, text=True)
print("gen_run_page:", r.returncode, r.stdout.strip(), (r.stderr.strip()[:200] if r.stderr else ""))

# ---- 4) index.json ----
def normkey(t):
    out = []
    for ch in t.lower():
        if ch.isalnum() or "一" <= ch <= "鿿":
            out.append(ch)
    return "".join(out)

data = json.load(open(IDX, encoding="utf-8"))
existing_urls = {e.get("url", "").lower().rstrip("/") for e in data}
added = 0
for c in CARDS:
    u = c["url"].lower().rstrip("/")
    if u in existing_urls:
        print("SKIP dup url:", u); continue
    entry = {
        "title": c["title"],
        "normKey": normkey(c["title"]),
        "url": c["url"],
        "sourceType": "secondary" if c["src"] == "b2" else "primary",
        "relation": "exec" if c["rel"] == "r3" else "supervisor",
        "summary": c["cat"] + "：" + c["val"][:60],
        "topic": "award",
    }
    data.append(entry); added += 1; existing_urls.add(u)
print("index.json 新增:", added, "-> 现", len(data), "条")
json.dump(data, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

# ---- 5) Obsidian 主题汇总笔记（newest-first：插到首个 ## 轮次 之前）----
VAULT = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库"
NOTE = os.path.join(VAULT, "素材", "award", "颁奖-知识卡汇总.md")
t = open(NOTE, encoding="utf-8").read()
assert "共 141 张" in t, "摘要 141 marker not found"
t = t.replace("共 141 张", "共 149 张", 1)
round_section = (
    "\n## 轮次 2026-08-24（+8）\n\n"
    "本轮新增（均通过六维评估、仅 ②上下级 / ③高管间）：\n"
)
for c in CARDS:
    rel = "高管间" if c["rel"] == "r3" else "上下级"
    src = "一手" if c["src"] == "b1" else "二手"
    round_section += "- {0}（award.html） | {1} | {2}\n".format(esc(c["title"]), rel, src)
first_round = t.find("## 轮次")
assert first_round != -1
t = t[:first_round] + round_section + t[first_round:]
open(NOTE, "w", encoding="utf-8").write(t)
print("Obsidian 主题汇总笔记已插入本轮 round 段（newest-first）+ 摘要计数 141->149")

# ---- 6) 00-索引（更新计数行 + 轮次标记 + 追加卡行）----
IDX0 = os.path.join(VAULT, "00-知识采集索引.md")
i0 = open(IDX0, encoding="utf-8").read()
apos = i0.find("## 主题：颁奖")
assert apos != -1
npos = i0.find("## 主题：", apos + 10)
assert npos != -1
# 计数行：141 卡 -> 149 卡（锚定在 award 区块内，防误改其他主题）
blk = i0[apos:npos]
assert "**141 卡**" in blk, "141 卡 marker not found in award block"
i0 = i0[:apos] + blk.replace("**141 卡**", "**149 卡**", 1) + i0[npos:]
# 轮次标记追加（heading 行）
marker_old = "二十三轮 enrich 2026-08-23(+10)"
marker_new = "二十三轮 enrich 2026-08-23(+10) ｜ 二十四轮 enrich 2026-08-24(+8)"
assert marker_old in i0, "round marker not found"
i0 = i0.replace(marker_old, marker_new, 1)
# append rows before next "## 主题："
rows = "".join(
    "| {0}（award/award.html） | 4 | {1} | {2} | {3} |\n".format(
        esc(c["title"]),
        "一手" if c["src"] == "b1" else "二手",
        "③高管间" if c["rel"] == "r3" else "②上下级",
        esc(c["cat"] + "：" + c["val"][:30]))
    for c in CARDS
)
i0 = i0[:npos] + rows + "\n" + i0[npos:]
open(IDX0, "w", encoding="utf-8").write(i0)
print("00-索引已更新（计数141->149+轮次+卡行）")

# ---- 7) 本轮独立笔记（runs/ 新建 md）----
os.makedirs(os.path.join(VAULT, "素材", "award", "runs"), exist_ok=True)
RUN_NOTE = os.path.join(VAULT, "素材", "award", "runs", "颁奖-2026-08-24-第二十四轮-知识卡.md")
n_r3 = sum(1 for c in CARDS if c["rel"] == "r3")
n_r2 = sum(1 for c in CARDS if c["rel"] == "r2")
rn = (
    "---\n"
    "title: 颁奖-2026-08-24-第二十四轮-知识卡\n"
    "type: 自动化采集\n"
    "date: 2026-08-24\n"
    "tags: [知识采集, 颁奖, 二十四轮]\n"
    "relation: [supervisor, exec]\n"
    "---\n\n"
    "# 颁奖典礼 · 第二十四轮补采（2026-08-24，+8）\n\n"
    "- **GitHub Pages 独立页**：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/runs/award-2026-08-24-r24.html\n"
    "- **本地路径**：`knowledge-collection/award/runs/award-2026-08-24-r24.html`\n"
    "- **累计卡片墙（总索引）**：`knowledge-collection/award/award.html`（[线上](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/award/award.html)）\n"
    "- **覆盖关系档**：③高管间 {0} 卡 / ②上下级 {1} 卡（无①平级）\n".format(n_r3, n_r2)
    + "- **乐享团队文件夹**：颁奖 子文件夹（f585d1b78510459db0ce807cc9688448，每轮独立页）\n\n"
    "## 本轮新增 8 卡\n\n"
    "| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n"
)
for c in CARDS:
    rel = "高管间" if c["rel"] == "r3" else "上下级"
    src = "一手" if c["src"] == "b1" else "二手"
    rn += "| {0} | {1} | {2} |\n".format(esc(c["title"]), rel, src)
rn += "\n> 本笔记仅索引，不拷 HTML 副本；完整卡片见上方 GitHub Pages 独立页。\n"
open(RUN_NOTE, "w", encoding="utf-8").write(rn)
print("本轮独立笔记已建:", RUN_NOTE)

# ---- 8) GitHub 同步 ----
sync = os.path.join(os.path.dirname(BASE), "sync_knowledge_github.py")
try:
    rs = subprocess.run(["python", sync], capture_output=True, text=True, timeout=300)
    print("sync_knowledge_github:", rs.returncode, (rs.stdout.strip()[-300:] if rs.stdout else ""), (rs.stderr.strip()[:200] if rs.stderr else ""))
except Exception as e:
    print("\u26a0\ufe0f GitHub 同步异常（告警不阻断）：" + str(e)[:200])

# ---- 9) 乐享上传（whoami 探活；award 新建每轮独立页 + best-effort 更新累计墙）----
MCP_JSON = r"C:/Users/v_yitcai/.workbuddy/mcp.json"
LEXIANG_URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"
FOLDER = "f585d1b78510459db0ce807cc9688448"  # award 子文件夹（待清洗素材下）

class LexiangMCP:
    def __init__(self, token):
        self.token = token; self.session = None
    def _post(self, payload, retries=3):
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(LEXIANG_URL, data=data, method="POST")
        req.add_header("Content-Type", "application/json")
        req.add_header("Accept", "application/json, text/event-stream")
        req.add_header("Authorization", self.token)
        if self.session: req.add_header("Mcp-Session-Id", self.session)
        last = None
        for _ in range(retries):
            try:
                resp = urllib.request.urlopen(req, timeout=120)
                sid = resp.headers.get("mcp-session-id")
                if sid: self.session = sid
                return self._parse(resp.read().decode("utf-8", "replace"))
            except urllib.error.HTTPError as e:
                last = "HTTP {0}: {1}".format(e.code, e.read().decode("utf-8", "replace")[:400]); continue
            except Exception as e:
                last = str(e); continue
        raise RuntimeError("POST fail: " + last)
    def _parse(self, raw):
        raw = raw.strip()
        if raw.startswith("data:"):
            raw = "\n".join(l[5:].strip() for l in raw.splitlines() if l.startswith("data:"))
        try: return json.loads(raw)
        except Exception: return json.loads(raw[raw.find("{"):])
    def initialize(self):
        return self._post({"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"wb-uploader","version":"1.0"}}})
    def initialized(self):
        try: self._post({"jsonrpc":"2.0","method":"notifications/initialized"})
        except Exception: pass
    def call(self, name, args):
        return self._post({"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":name,"arguments":args}})
    def biz(self, resp):
        res = resp.get("result")
        if not res: raise RuntimeError("no result: " + json.dumps(resp, ensure_ascii=False)[:300])
        text = ""
        for c in (res.get("content") or []):
            if c.get("type") == "text": text = c.get("text", ""); break
        try: return json.loads(text)
        except Exception: return {"_raw_text": text}

def put_bytes(url, data, retries=3):
    last = None
    for _ in range(retries):
        try:
            req = urllib.request.Request(url, data=data, method="PUT")
            req.add_header("Content-Type", "text/html")
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.status
        except Exception as e:
            last = str(e); continue
    raise RuntimeError("PUT fail: " + str(last))

try:
    token = json.load(open(MCP_JSON, encoding="utf-8"))["mcpServers"]["lexiang"]["headers"]["Authorization"]
    mc = LexiangMCP(token); mc.initialize(); mc.initialized()
    try:
        w = mc.call("whoami", {})
        print("whoami:", json.dumps(mc.biz(w), ensure_ascii=False)[:120])
    except Exception as e:
        print("whoami 跳过:", str(e)[:120])

    # best-effort 累计墙更新：列出 folder 子条目，找 award.html 墙条目
    try:
        lc = mc.call("entry_list_children", {"parent_id": FOLDER})
        biz_lc = mc.biz(lc)
        entries = biz_lc.get("data", {}).get("entries", []) if isinstance(biz_lc.get("data"), dict) else biz_lc.get("data", [])
        wall_entry = None
        for e in entries:
            nm = (e.get("name") or "").lower().replace(".html", "")
            if nm == "award":
                wall_entry = e; break
        if wall_entry:
            wall_id = wall_entry.get("id") or wall_entry.get("entry_id")
            target = wall_entry.get("target") or {}
            file_id = target.get("id") or target.get("file_id") or wall_entry.get("file_id")
            if wall_id and file_id:
                wall_bytes = open(CUM, "rb").read()
                r = mc.call("file_apply_upload", {"file_id": file_id, "parent_entry_id": wall_id,
                                                  "name": "award.html", "extension": "html",
                                                  "mime_type": "text/html", "upload_type": "PRE_SIGNED_URL",
                                                  "size": str(len(wall_bytes))})
                biz = mc.biz(r)
                if biz.get("code") != 0:
                    raise RuntimeError("apply_upload(wall) FAIL " + str(biz.get("message")))
                sess = biz["data"]["session"]
                sid = sess.get("session_id") or sess.get("id")
                url = sess.get("upload_url") or sess["objects"][0]["upload_url"]
                st = put_bytes(url, wall_bytes)
                if st != 200: raise RuntimeError("PUT(wall) status " + str(st))
                r2 = mc.call("file_commit_upload", {"session_id": sid})
                biz2 = mc.biz(r2)
                if biz2.get("code") != 0: raise RuntimeError("commit(wall) FAIL " + str(biz2.get("message")))
                print("乐享累计墙更新 OK entry_id=", wall_id)
            else:
                print("乐享累计墙条目缺 file_id，跳过墙更新（仅建独立页）")
        else:
            print("乐享 folder 内未发现 award.html 墙条目，跳过墙更新（仅建独立页）")
    except Exception as e:
        print("\u26a0\ufe0f 乐享累计墙更新跳过（warning，不中断）：" + str(e)[:200])

    # 新建本轮独立页
    run_bytes = open(RUN_PATH, "rb").read()
    r = mc.call("file_apply_upload", {"parent_entry_id": FOLDER, "name": RUN_NAME,
                                      "extension":"html", "mime_type":"text/html",
                                      "upload_type":"PRE_SIGNED_URL", "size": str(len(run_bytes))})
    biz = mc.biz(r)
    if biz.get("code") != 0:
        raise RuntimeError("apply_upload(run) FAIL {0}".format(biz.get("message")))
    sess = biz["data"]["session"]
    sid = sess.get("session_id") or sess.get("id")
    url = sess.get("upload_url") or sess["objects"][0]["upload_url"]
    st = put_bytes(url, run_bytes)
    if st != 200: raise RuntimeError("PUT(run) status " + str(st))
    r2 = mc.call("file_commit_upload", {"session_id": sid})
    biz2 = mc.biz(r2)
    if biz2.get("code") != 0: raise RuntimeError("commit(run) FAIL " + str(biz2.get("message")))
    rid = biz2["data"]["entry"]["id"]
    print("乐享新建独立页 OK entry_id=", rid)
    mapf = json.load(open(os.path.join(BASE, "lexiang-entry-map.json"), encoding="utf-8"))
    sm = mapf.setdefault("award", {"folder_id": FOLDER, "rounds": []})
    sm["folder_id"] = FOLDER
    sm["rounds"].append({"date": DATE, "entry_id": rid, "name": RUN_NAME, "note": "轮次页 R24 (+8：主题构思/物料设计/直播传播/故事传播/反模式/经理话术/高管致辞/全球执行)"})
    json.dump(mapf, open(os.path.join(BASE, "lexiang-entry-map.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("已回写 lexiang-entry-map.json")
except Exception as e:
    print("\u26a0\ufe0f 乐享上传跳过（warning，不中断）：" + str(e)[:300])

print("\n=== R24 完成：新增", added, "卡，墙现", after, "卡 ===")
