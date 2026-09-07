# -*- coding: utf-8 -*-
"""颁奖 三十六轮 enrich（2026-09-07）构建脚本。
仅保留 ②上下级 / ③高管间 两档，剔除平级/朋友向。
产出：增量页 award-20260907.html + 注入累计墙 award.html + index.json + Obsidian 笔记 + 00索引 + lexiang map。
"""
import re, os, json

BASE = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(BASE, 'award', 'award.html')
INC = os.path.join(BASE, 'award', 'award-20260907.html')
TMP = os.path.join(BASE, 'award', '.run_newcards.tmp.html')
IDX = os.path.join(BASE, 'index.json')
MAP = os.path.join(BASE, 'lexiang-entry-map.json')
NOTE = r'C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\award\颁奖-知识卡汇总.md'
IDX00 = r'C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md'
RUN_DATE = '2026-09-07'
ROUND_LABEL = '三十六轮'
ROUND_TAG = '+11'

CSS = '''<style>
:root{--bg:#f4f6fb;--card:#ffffff;--ink:#1f2430;--sub:#5b6478;--accent:#6c5ce7;--accent2:#00b8d9;--chip:#eef0ff;}
*{box-sizing:border-box;margin:0;padding:0;}
body{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:linear-gradient(135deg,#eef1ff 0%,#e6f7ff 100%);color:var(--ink);padding:28px 18px;line-height:1.6;}
.wrap{max-width:1080px;margin:0 auto;}
.hero{background:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);border-radius:22px;padding:30px 32px;color:#fff;box-shadow:0 14px 40px rgba(108,92,231,.25);margin-bottom:22px;}
.hero h1{font-size:26px;font-weight:800;letter-spacing:1px;margin-bottom:8px;}
.hero p{font-size:14px;opacity:.95;}
.relbar{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px;}
.relbar span{background:rgba(255,255,255,.2);border-radius:20px;padding:5px 14px;font-size:13px;font-weight:600;}
.back{display:inline-block;margin:0 0 14px;font-size:13px;color:var(--accent2);text-decoration:none;font-weight:600;}
.sec{margin:30px 0 12px;display:flex;align-items:center;gap:10px;}
.sec h2{font-size:19px;font-weight:800;}
.sec .tag{font-size:12px;padding:4px 12px;border-radius:12px;font-weight:700;}
.sec3 .tag{background:#f3e8ff;color:#7b2cbf;} .sec3 h2{color:#7b2cbf;}
.sec2 .tag{background:#fff3e0;color:#c0651a;} .sec2 h2{color:#c0651a;}
.sec1 .tag{background:#eaf2ff;color:#2b6cb0;} .sec1 h2{color:#2b6cb0;}
.sec .desc{font-size:12.5px;color:var(--sub);margin-left:2px;}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;}
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
</style>'''

# ---- 卡片定义（仅 ②上下级 / ③高管间）----
# rel: 'r2'=上下级(supervisor), 'r3'=高管间(exec)
CARDS = [
 dict(emoji='🏅', title='百合光电2026年中优秀员工暨优秀干部表彰大会（部门推荐→评审→公示→首设干部奖→总经理讲话）', cat='表彰流程', rel='r2',
   val='百合光电2026年中表彰：严格遵循"部门推荐→综合评审→公示确认"流程；新增"2026年中优秀干部"专项奖（首次年中设干部表彰，回应管理力量）；16位优秀员工覆盖生产/技术/市场/职能，领导颁证+奖金+合影；各事业部/职能负责人及总经理刘总依次讲话，肯定先进、研判机遇挑战、勉励传承价值观。把表彰做成"流程公正+干部同表彰+领导战略解码"的标准范本。',
   exec_txt='HR/行政办年中表彰：先立公正流程(部门推荐→评审→公示)→增设管理干部专项奖(回应管理力量)→领导颁证+奖金+合影→总经理/负责人讲话做战略解码与价值观传承；让表彰既树标杆又传递方向。',
   url='http://www.baiheoe.com/newshow/1/The-baihe-2026-9-3',
   note='② HR/行政办年中表彰（上下级、公正流程+干部同表彰+领导战略解码，非平级游戏）。二手·百合光电官方报道。',
   sourceType='secondary', relation='supervisor'),
 dict(emoji='🎂', title='贝德服装集团2026先进表彰暨25周年庆典（执行副总裁宣读·十年忠诚奖/一带一路十年功勋奖·代表发言·茶歇）', cat='周年庆典', rel='r2',
   val='贝德2026先进表彰暨25周年庆典：执行副总裁高佩娜宣读表彰决定，表彰年度先进集体与个人；奖项含优秀团队/班组、业绩先锋/创新团队、最具创新奖、数字化先锋、质量立厂奖、工匠奖、十年忠诚奖、一带一路五年/十年功勋奖等；四位获奖代表登台分享；设精致茶歇共话情谊。把25周年做成"忠诚里程碑+全球化贡献"的荣誉盛典。',
   exec_txt='HR/高管办周年表彰：高管宣读表彰决定→设长期忠诚/海外功勋等里程碑奖→获奖代表发言造榜样→茶歇环节凝向心力；把周年庆与忠诚认可绑定，强化归属感。',
   url='https://c.m.163.com/news/a/KNTTCTG00552KN3A.html',
   note='② HR/高管办周年表彰（上下级、忠诚里程碑奖+代表发言+茶歇，尊重不越界）。二手·网易新闻案例。',
   sourceType='secondary', relation='supervisor'),
 dict(emoji='🥇', title='广东溢达纺织38年黄金金牌传统（满10/20/30/40年铸黄金刻名·副总经理讲话）', cat='长期服务', rel='r2',
   val='广东溢达自1988年起每年给服务满10/20/30/40年员工授黄金铸造金牌、刻员工姓名、嵌定制基座；已坚持38年，仅2023-2025近5600人获奖（10年4000+/20年1200+/30年300+/40年2）；副总经理石平波称"企业长期发展是马拉松，靠坚守"。把长期服务奖做成可传承的"实物信物+姓名镌刻"仪式，规避只发钱缺记忆点。',
   exec_txt='HR/高管设长期服务金牌：按司龄分档(10/20/30/40年)→黄金实物刻姓名+定制基座→年度仪式由管理层亲颁→高层讲话把坚守上升为企业精神；实物信物比现金更留记忆。',
   url='https://new.qq.com/rain/a/20260215A03PQL00',
   note='② HR/高管设长期服务金牌（上下级、黄金刻名实物信物+管理层亲颁，仪式感强）。二手·腾讯新闻/经济参考报。',
   sourceType='secondary', relation='supervisor'),
 dict(emoji='💌', title='顺丰长期服务感谢金（王卫个人名义·10年工龄+亲笔信·2026年会家属参与）', cat='长期服务', rel='r2',
   val='顺丰长期服务奖：2025年王卫以个人名义设"长期服务感谢金"，按工龄分三档(10-15年1000/15-20年2000/超20年3000元)+亲笔感谢信；2026深莞区年会1300余名获奖者受表彰，首次邀家属参与、客户现场致谢。把老板个人出资+家属见证+客户致谢做成"组织韧性+人才资本"的信任机制。',
   exec_txt='老板/高管设长期服务感谢金：个人出资+按司龄分档现金+亲笔信→年会表彰邀家属参与、客户致谢→把"被看见"从个人感受升级为家庭与客户的共同见证；信任感远超普发奖金。',
   url='https://pages.baidu.com/show?id=52bc330735664724f24e8337',
   note='② 老板个人出资长期服务奖（上下级、感谢金+亲笔信+家属客户见证，信任机制）。二手·百度百科。',
   sourceType='secondary', relation='supervisor'),
 dict(emoji='🍔', title='香港麦当劳年度员工晚宴·500+长期服务奖（行政总裁致辞·管理层台前为同事喝彩）', cat='长期服务', rel='r2',
   val='香港麦当劳一连三晚年度员工晚宴，颁逾500个长期服务奖(150+服务满20年)、200+年度杰出员工奖；行政总裁黎韦詩致辞感谢长期同事；各分店团队挥灯牌欢呼，把颁奖做成员工"应援大会"。核心：管理层走到台前亲自为同事喝彩，拉近前线与管理层距离，把"长期服务"塑造成年轻一代愿追的成就标记。',
   exec_txt='HR/高管办年度员工晚宴：颁长期服务奖+年度杰出奖→管理层走下台前为同事喝彩(非仅台上颁)→团队应援式欢呼→总裁致辞把长期服务塑造成成就标记；用"管理层亲近"补物质激励。',
   url='https://resources.ctgoodjobs.hk/article/46690',
   note='② HR/高管办员工晚宴（上下级、管理层台前喝彩+长期服务塑造成就标记，拉近管理层距离）。二手·CTgoodjobs。',
   sourceType='secondary', relation='supervisor'),
 dict(emoji='🏆', title='长城餐饮集团金牌回馈·董事主席感谢32年团队（按司龄分级20/25/30克999金）', cat='长期服务', rel='r2',
   val='新加坡长城餐饮集团向100+服务年资员工送999黄金金牌：10-14年20克/15-19年25克/满20年30克，按司龄分级；董事主席郭观华称"感谢团队32年顺逆同在"。把长期服务奖做成"老板个人感恩+黄金实物分级"，且杰出摊位另奖1500元由头手分配。高层直接感谢，规避HR流程化冷漠。',
   exec_txt='老板/高管做长期服务金牌回馈：按司龄分级发黄金实物→董事主席亲自致谢(点名32年同行)→杰出单位另设现金奖由一线头手分配；老板个人感恩比制度发文更打动人。',
   url='https://zaobao.com/news/singapore/story20260211-8445274',
   note='② 董事主席个人感恩长期服务金牌（上下级、按司龄分级黄金+老板亲谢，非平级）。二手·联合早报。',
   sourceType='secondary', relation='supervisor'),
 dict(emoji='🔧', title='Awardco 提名项目设计蓝图 + CEO自设「无名英雄奖」（幕后贡献被看见）', cat='提名机制', rel='r2',
   val='Awardco 设计蓝图：提名项目=组织内"众包可见性"，三支柱——目标(强化价值观/突出幕后/促协作/激创新)、模型(谁提名:全员>经理/peer-only)、机制(具体事例+文件/视频佐证+评审层级+即时feed还是戏剧揭晓)。案例：某CEO自设"Ball Bearing Award(滚珠轴承奖)"表彰IT/财务/运营等幕后团队，信号"最基础的贡献常来自不被看见的人"，全员提名让领导看见本看不到的卓越。',
   exec_txt='HR/高管搭提名项目：先定目标(突出幕后/强化价值观)→选模型(全员提名最能挖出领导盲区)→立机制(具体事例+佐证+评审层级+揭晓节奏)→可设CEO冠名"无名英雄奖"专门照亮IT/财务/运营等基础贡献；提名过程本身就是故事金矿。',
   url='https://www.awardco.com/fr-ca/blog/beyond-employee-of-the-year-designing-a-nomination-program-to-fit-your-company-culture',
   note='② HR/高管搭提名项目+CEO无名英雄奖（上下级、众包可见性照亮幕后，非peer互评游戏）。二手·Awardco 官方博客。',
   sourceType='secondary', relation='supervisor'),
 dict(emoji='📊', title='MyCulture.ai 数据驱动团队奖项·价值观即可观察行为（混合证据模型）', cat='奖项设计', rel='r2',
   val='MyCulture.ai：2026 用数据重构团队奖项——价值观奖失败主因是"先宣布后定义"，须把价值观变可观察行为(创新=会议/立项/实验/peer支持的具体动作)；用"评估先行+行为证明(要求具体事例非形容词)+职业挂钩(拉伸任务/导师)+跨职能队列对比"的混合证据模型，避免人气投票。奖项配比参考体育：40-50%绩效/25-30%品格领导/15-20%贡献文化/10-15%趣味家庭。',
   exec_txt='HR/高管做数据驱动奖项：把价值观拆成可观察行为(先定义后宣布)→用评估+经理观察+peer提名(附具体事例)混合证据→与职业发展挂钩→跨职能队列对比防偏差；让奖项成为"测量系统"而非人气赛。',
   url='https://www.myculture.ai/blog/awards-for-teams',
   note='② HR/高管做数据驱动奖项（上下级、价值观可观察化+混合证据防人气投票，治理视角）。二手·MyCulture.ai 博客。',
   sourceType='secondary', relation='supervisor'),
 dict(emoji='🌟', title='RLC Honors 2026 利雅得·终身成就奖（前Gucci CEO/女企业家领袖获颁·行业标杆）', cat='终身成就', rel='r3',
   val='2026 RLC Honors(利雅得)：Marco Bizzarri(前Gucci CEO、现企业家投资人)获"奢侈品零售卓越终身成就奖"，表彰其将Gucci重塑为全球文化力量；Ingie Chalhoub(Etoile Group创始人兼总裁)获"女性领导力开拓终身成就奖"，表彰其对中东奢侈品生态的塑造。行业盛典汇聚全球与区域零售领袖，以终身成就奖树跨代标杆。',
   exec_txt='协会/高管办行业终身成就奖：由行业组织在全球盛典颁授→表彰重塑行业/开拓领域的领袖(前CEO/创始人)→以"终身领导力标杆"定位；用于行业精神资产与跨代引领。',
   url='https://www.etnet.com.hk/www/tc/news/globenewswire_news_detail.php?newsid=1001164409&lang=en',
   note='③ 协会/高管办行业终身成就奖（高管间、领袖获颁+行业标杆，商务化）。二手·etnet/GlobeNewswire。',
   sourceType='secondary', relation='exec'),
 dict(emoji='🤝', title='林福山获世界杰出企业家终身成就奖·受委全球顾问委员会联席主席（政商领袖见证）', cat='终身成就', rel='r3',
   val='林木生集团执行主席丹斯里林福山获"世界杰出企业家终身成就奖"并受委世界商业总会全球顾问委员会联席主席；颁奖暨委任典礼于吉隆坡香格里拉举行，由马六甲州元首及联邦法院前首席大法官共同见证。其称此殊荣是对集团团队、合作伙伴与利益相关者共同努力的肯定，将促进国际更紧密合作与可持续商业。',
   exec_txt='高管/企业家获颁终身成就奖：由国际商协在世界级场合颁授+政要见证→同步委以顾问/联席主席等治理角色→定位"个人里程碑+团队与伙伴共荣"；把奖项转化为国际影响力杠杆。',
   url='https://www.chinapress.com.my?p=5055605/',
   note='③ 企业家获颁终身成就奖+受委治理职（高管间、政商见证+国际影响力杠杆，商务）。二手·中国报。',
   sourceType='secondary', relation='exec'),
 dict(emoji='🏛️', title='中国品牌人物终身成就奖（马蔚华/宋志平/郎志正·中国品牌节盛典颁授）', cat='终身成就', rel='r3',
   val='品牌联盟"TopBrand 中国品牌人物终身成就奖"于中国品牌人物年会荣耀盛典首设并颁授：马蔚华(招行零售标杆+公益教育)、宋志平(中国上市公司协会会长、双料世界500强掌门)、郎志正(国际质量科学院院士、国务院原参事)获此殊荣。盛典汇聚全国品牌领袖、专家学者，以终身成就奖礼赞"穿越周期"的企业家精神与质量信仰。',
   exec_txt='机构/高管办品牌终身成就奖：在年度品牌盛典首设并颁授→表彰横跨商业与公共领域的标杆企业家(金融/制造/质量)→以"穿越周期的力量"主题升华；用于行业精神引领与机构公信力。',
   url='https://zt.brandcn.com/niandurenwu',
   note='③ 机构办品牌终身成就奖（高管间、企业家标杆+行业精神引领，商务化）。二手·品牌联盟。',
   sourceType='secondary', relation='exec'),
]

def norm_url(u):
    u = u.strip().lower()
    u = re.sub(r'^https?://', '', u)
    u = re.sub(r'/\?.*$', '', u)
    u = re.sub(r'#.*$', '', u)
    if u.endswith('/'):
        u = u[:-1]
    return u

def card_html(c):
    rel_text = '上下级' if c['rel'] == 'r2' else '高管间'
    src_badge = 'b1' if c['sourceType'] == 'primary' else 'b2'
    src_text = '一手' if c['sourceType'] == 'primary' else '二手'
    return f'''    <div class="hl">
      <div class="top"><span class="emoji">{c['emoji']}</span><h3>{c['title']}</h3><span class="cat">{c['cat']}</span><span class="badge {c['rel']}">{rel_text}</span><span class="badge {src_badge}">{src_text}</span></div>
      <p class="val">{c['val']}</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">{c['exec_txt']}</div></details>
      <div class="src">🔗 <a href="{c['url']}" target="_blank">{c['url']}</a></div>
      <div class="note">适用：{c['note']}</div>
    </div>
'''

# ===== 1) 去重：读 index.json 已有 URL =====
with open(IDX, encoding='utf-8') as f:
    idx = json.load(f)
existing_urls = set()
for e in idx:
    u = e.get('url')
    if u:
        existing_urls.add(norm_url(u))

new_cards = [c for c in CARDS if norm_url(c['url']) not in existing_urls]
dup_skipped = len(CARDS) - len(new_cards)
N = len(new_cards)
M = 0  # 本轮无历史 URL 命中，仅新增
print(f'[dedup] candidate={len(CARDS)} new={N} skipped(URL命中)={dup_skipped}')

# ===== 2) 增量页 award-20260907.html =====
r3 = [c for c in new_cards if c['rel'] == 'r3']
r2 = [c for c in new_cards if c['rel'] == 'r2']
r3_html = ''.join(card_html(c) for c in r3)
r2_html = ''.join(card_html(c) for c in r2)
inc_body = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>颁奖典礼 · 第36轮（独立页）</title>
{CSS}
</head>
<body>
<div class="wrap">
  <a class="back" href="../award.html">← 返回累计总索引 award.html</a>
  <div class="hero">
    <h1>🏆 颁奖典礼 · 第36轮（独立页）</h1>
    <p>采集于 2026-09-07 ｜ 本轮新增 {N} 卡（③高管间 {len(r3)} / ②上下级 {len(r2)}）｜ 六维评估 ｜ 一手/二手标注 ｜ 受众关系分层（仅②③，剔除①）｜ 累计总索引见 <a href="../award.html" style="color:#fff;text-decoration:underline;">award.html</a></p>
    <div class="relbar">
      <span>② 领导↔员工（上下级）</span>
      <span>③ 领导↔领导（高管间）</span>
    </div>
  </div>
  <div class="sec sec3">
    <h2>③ 领导↔领导（高管间，exec）</h2>
    <span class="tag">{len(r3)} 卡</span>
  </div>
  <div class="grid">
{r3_html}  </div>
  <div class="sec sec2">
    <h2>② 领导↔员工（上下级，supervisor）</h2>
    <span class="tag">{len(r2)} 卡</span>
  </div>
  <div class="grid">
{r2_html}  </div>
  <footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>
</div>
</body>
</html>
'''
with open(INC, 'w', encoding='utf-8') as f:
    f.write(inc_body)
with open(TMP, 'w', encoding='utf-8') as f:
    f.write(''.join(card_html(c) for c in new_cards))
print(f'[inc] wrote {INC} ({N} cards: {len(r3)}③ + {len(r2)}②)')

# ===== 3) 注入累计墙 award.html =====
html = open(WALL, encoding='utf-8').read()
grids = list(re.finditer(r'<div class="grid">', html))
assert len(grids) >= 2, f"expected >=2 grids, got {len(grids)}"
def matching_close(h, start):
    i = h.index('>', start) + 1
    d = 0
    while i < len(h):
        if h[i:i+4] == '<div':
            d += 1; i += 4
        elif h[i:i+6] == '</div>':
            d -= 1; i += 6
            if d == 0:
                return i
        else:
            i += 1
    raise RuntimeError('no close')
sec3_start = grids[0].start()
sec3_close = matching_close(html, sec3_start)
sec2_start = grids[1].start()
sec2_close = matching_close(html, sec2_start)
r3_cards = ''.join(card_html(c) for c in new_cards if c['rel'] == 'r3')
r2_cards = ''.join(card_html(c) for c in new_cards if c['rel'] == 'r2')
html = html[:sec3_close] + r3_cards + html[sec3_close:]
sec2_close2 = sec2_close + len(r3_cards)
html = html[:sec2_close2] + r2_cards + html[sec2_close2:]
# hero 轮次段
hm = re.search(r'(<div class="hero">.*?<p>)(.*?)(</p>)', html, re.S)
assert hm, 'hero p not found'
new_p = hm.group(2) + f' ｜ {ROUND_LABEL} enrich 2026-09-07({ROUND_TAG})'
html = html[:hm.start()] + hm.group(1) + new_p + hm.group(3) + html[hm.end():]
open(WALL, 'w', encoding='utf-8').write(html)
print('[wall] total hl now:', re.findall(r'<div class="hl">', html).__len__())
print('[wall] r3:', html.count('badge r3'), 'r2:', html.count('badge r2'))
print('[wall] footer ok:', '📌 本页由 yitong 沉淀整理' in html)

# ===== 4) index.json 追加 =====
for c in new_cards:
    nk = re.sub(r'[\s\-–—·，。、：:；;（）()【】\[\]/\\]', '', c['title'])
    idx.append({
        'title': c['title'],
        'normKey': nk,
        'url': c['url'],
        'sourceType': c['sourceType'],
        'relation': c['relation'],
        'topic': 'award',
        'summary': c['note'],
    })
with open(IDX, 'w', encoding='utf-8') as f:
    json.dump(idx, f, ensure_ascii=False, indent=2)
print(f'[index.json] appended {N} entries (total {len(idx)})')

# ===== 5) Obsidian 颁奖-知识卡汇总.md =====
note = open(NOTE, encoding='utf-8').read()
note = note.replace('共 236 张', '共 247 张', 1)
round_sec = f'''## 轮次 2026-09-07·三十六轮（+{N}）
本轮新增（均通过六维评估、仅 ②上下级 / ③高管间）：
'''
for c in new_cards:
    rel_text = '②上下级' if c['rel'] == 'r2' else '③高管间'
    src_text = '一手' if c['sourceType'] == 'primary' else '二手'
    round_sec += f"- {c['title']}（award/award.html） | {rel_text} | {src_text}\n"
m = re.search(r'\n## 轮次 ', note)
assert m, 'round section not found'
note = note[:m.start()] + round_sec + note[m.start():]
open(NOTE, 'w', encoding='utf-8').write(note)
print(f'[obsidian note] inserted round section (+{N})')

# ===== 6) 00-知识采集索引.md =====
idx00 = open(IDX00, encoding='utf-8').read()
mh = re.search(r'^(## 主题：颁奖典礼.*)$', idx00, re.M)
assert mh, 'award section header not found'
header_new = mh.group(1).rstrip() + f' ｜ 三十六轮 enrich 2026-09-07(+{N})'
idx00 = idx00[:mh.start()] + header_new + idx00[mh.end():]
sep = '| 卡 | 质量分 | 一手/二手 | 适用关系 | 一句话定位 |\n|---|---|---|---|---|'
assert sep in idx00, 'award table header not found'
rows = ''
for c in new_cards:
    rel_text = '②上下级' if c['rel'] == 'r2' else '③高管间'
    src_text = '一手' if c['sourceType'] == 'primary' else '二手'
    rows += f"| {c['title']}（award/award.html） | 4 | {src_text} | {rel_text} |  |\n"
idx00 = idx00.replace(sep, sep + rows, 1)
open(IDX00, 'w', encoding='utf-8').write(idx00)
print(f'[00-index] header + {N} rows appended')

# ===== 7) lexiang-entry-map.json 追加 pending round =====
mp = json.load(open(MAP, encoding='utf-8'))
award_map = mp['award']
award_map['rounds'].append({
    'date': RUN_DATE,
    'entry_id': None,
    'name': 'award-20260907.html',
    'note': f'轮次页 R36 (+{N}：{len(r3)}③高管间+{len(r2)}②上下级，0一手+{N}二手)｜乐享待补传(connector disconnected/token 401，待重连后补传并回填 entry_id)'
})
json.dump(mp, open(MAP, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'[lexiang map] appended round R36 (+{N}) entry_id=null (pending upload)')

print('\n=== SUMMARY ===')
print(f'topic=颁奖  round=36  date=2026-09-07')
print(f'新增 N={N} (③{len(r3)} + ②{len(r2)})  去重删 M={M}  URL命中跳过={dup_skipped}')
print(f'增量页: award/award-20260907.html')
print(f'累计墙: award/award.html')
print(f'index.json: +{N} (total {len(idx)})')
print(f'Obsidian: 颁奖-知识卡汇总.md + 00-知识采集索引.md 已更新')
print(f'乐享: 跳过实际上传(connector disconnected/token 401)，map 已追加 pending round')
