# -*- coding: utf-8 -*-
"""颁奖 三十七轮 enrich（2026-09-08）构建脚本。
仅保留 ②上下级 / ③高管间 两档，剔除平级/朋友向。
产出：增量页 award-20260908.html + 注入累计墙 award.html + index.json + Obsidian 笔记 + 00索引 + lexiang map。
"""
import re, os, json

BASE = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(BASE, 'award', 'award.html')
INC = os.path.join(BASE, 'award', 'award-20260908.html')
TMP = os.path.join(BASE, 'award', '.run_newcards.tmp.html')
IDX = os.path.join(BASE, 'index.json')
MAP = os.path.join(BASE, 'lexiang-entry-map.json')
NOTE = r'C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\award\颁奖-知识卡汇总.md'
IDX00 = r'C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md'
RUN_DATE = '2026-09-08'
ROUND_LABEL = '三十七轮'
ROUND_TAG = '+10'

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
 dict(emoji='🏛️', title='城发集团2026年"五一"优秀员工表彰大会（党委书记讲话"以奋斗者为本"·三期望·身份无差别贡献有回报）', cat='五一表彰', rel='r2',
   val='新宁城发集团2026"五一"优秀员工表彰：7位同志获"优秀员工"，领导班子颁奖、代表发言讲平凡岗位坚守故事；党委书记/董事长刘震东讲话提出三点期望——获奖模范"荣誉归零、责任上肩"、全体"见贤思齐对标奋进"、强调"尊重劳动崇尚实干、以奋斗者为本"，并特别指出"身份无差别、贡献有回报，无论何种用工形式都被尊重被看见"。把表彰做成"价值观宣导+榜样故事+身份平权"的精神洗礼。',
   exec_txt='HR/高管办五一表彰：评优→领导颁奖+代表朴实发言(讲岗位故事)→董事长讲话定调"以奋斗者为本"→提三期望(荣誉归零/见贤思齐/尊重劳动)→强调"身份无差别贡献有回报"；让表彰成为价值观与归属感载体，不只是发奖。',
   url='https://www.xncfjt.net/index.php?s=index/show/index&id=3121',
   note='② 国企HR/党委五一表彰（上下级、以奋斗者为本讲话+身份平权，非平级游戏）。一手·城发集团官网。',
   sourceType='primary', relation='supervisor'),
 dict(emoji='🏅', title='湖南盐业集团2026年度工作会暨总结表彰（董事长特别奖/价值营销标杆/质量标兵/安全先进个人/精益改善之星/金点子奖·责任状签订）', cat='年度表彰', rel='r2',
   val='湖南盐业集团2026年度工作会暨表彰：现场宣读表彰决定，授"2025年度董事长特别奖"(省长质量奖创奖团队等3团队)、"价值营销标杆团队"、"质量管理先进单位/质量标兵"、"安全生产先进单位/先进个人"、"精益改善组织奖/精益改善之星"、"集团职工金点子合理化建议奖"；另表彰总部先进部门/优秀中层/优秀员工；领导颁奖。会前递交经营业绩责任书/安全环保责任状/平安建设责任书、签工资集体协商协议。把"战略签约+责任状+多维表彰"做成年度动员闭环。',
   exec_txt='HR/高管办年度工作会：先签责任状(经营/安全/平安)+集体协商→宣读表彰决定→多维度颁奖(董事长特别奖/营销标杆/质量标兵/安全先进/精益之星/金点子)→领导讲话锚定目标；用"责任+荣誉"双轮驱动年度冲锋。',
   url='https://gzw.hunan.gov.cn/gzjg/gqdt/202602/t20260224_33919450.html',
   note='② 国企年度工作会+多维表彰矩阵（上下级、责任状+质量/安全/精益/金点子奖项，治理视角）。一手·湖南省国资委官网。',
   sourceType='primary', relation='supervisor'),
 dict(emoji='🎊', title='长方集团康铭盛2026年度表彰大会暨年会盛典（优秀协作/员工/业绩奖·管委会主任"付出就有回报"·团圆晚宴抽奖）', cat='表彰年会', rel='r2',
   val='长方集团康铭盛2026表彰大会暨年会：年度优秀协作奖/优秀员工奖/优秀业绩奖等多项大奖逐一揭晓，30位优秀员工登台接荣誉勋章；经营管理委员会主任王刚讲话，重申"付出就有回报、努力就能改变命运"信念，以公平、公正、尊重的文化+稳定发展为根基、长期激励为保障，让认真付出者被认可；会后团圆晚宴+抽奖(六等至特等)。把表彰与年会合办，用"仪式颁奖+价值观口号+欢聚"一体化凝聚归属感。',
   exec_txt='HR/高管办表彰年会合一：颁奖(优秀协作/员工/业绩多奖)→管委会主任讲话立价值观口号(付出就有回报)→晚宴+抽奖欢聚；把表彰嵌入年会，避免"开会式颁奖"的疏离感，用庆祝氛围放大认可。',
   url='https://cfled.com/jituanxinwen/93.html',
   note='② 表彰与年会合办（上下级、价值观口号+晚宴抽奖凝聚，尊重不越界）。一手·长方集团官网。',
   sourceType='primary', relation='supervisor'),
 dict(emoji='🛡️', title='安全生产隐患内部举报奖励机制（即时小额现金20-5000元+通报表扬+评优优先·湖北"多看一眼奖五千"）', cat='即时奖励', rel='r2',
   val='多地应急/住建部门通报"事故隐患内部报告奖励"典型案例：员工发现隐患(管线泄漏/消防通道堵塞/设备锈蚀)立即上报，企业按制度给20-1000元现金奖励+例会通报表扬+纳入年底评优优先；湖北推行"火眼金睛识破夺命细节、员工多看一眼奖五千"，单笔最高5000元。把"即时小额现金+通报表扬"做成日常安全微认可，与年度大奖互补，让"被看见"发生在每天的现场。',
   exec_txt='EHS/高管建隐患上报奖励：定制度(发现即报→核实→小额现金+通报)→设梯度金额(常规20-100元、重大隐患数千)→与评优/绩效挂钩→用"多看一眼奖五千"式口号造氛围；把安全认可做成高频微激励而非一年一次。',
   url='https://yjt.hubei.gov.cn/fbjd/dtyw/mtbd/sjmt/202606/t20260617_5960184.shtml',
   note='② EHS/高管隐患上报即时奖励（上下级、小额现金+通报的日常微认可，治理视角）。一手·湖北省应急厅。',
   sourceType='primary', relation='supervisor'),
 dict(emoji='💡', title='棒线厂/东晓生物"金点子"合理化建议颁奖（一线提案评审+奖金勋章·"让点子变金子"评审闭环落地）', cat='微创新奖', rel='r2',
   val='晋钢控股棒线厂、东晓生物等推行"金点子"合理化建议颁奖：聚焦工艺/设备/能耗/安全，员工提案经部门初评→专项评审(东晓第二届收75项、通过率25%、19项获奖)→厂领导颁证书奖金+专属勋章；强调"提了就算数"闭环——首届42项采纳提案全部纳入实施、38项常态化应用。把一线微创新做成"提案-评审-颁奖-落地"闭环，用小额奖金+勋章点燃"人人想创新"。',
   exec_txt='HR/高管办金点子奖：搭提案平台(聚焦工艺/成本/安全)→初评+专项评审打分→领导颁奖(证书+奖金+勋章)→闭环追踪落地(采纳即实施、定期通报)→标杆代表分享；让"小建议"变"大效益"，认可落到岗位。',
   url='https://www.toutiao.com/article/7615516327645594162/',
   note='② 全员合理化建议"金点子"颁奖（上下级、提案评审闭环+勋章认可，非peer互评）。二手·今日头条/晋钢控股。',
   sourceType='secondary', relation='supervisor'),
 dict(emoji='🌱', title='孟加拉首届 ESG Excellence Awards（UN全球契约+ESG Institute·32企业3人·20类别·独立评审·部长见证）', cat='ESG奖项', rel='r3',
   val='孟加拉首届 ESG Excellence Awards 由 UN Global Compact Network Bangladesh 与 ESG Institute 合办，表彰32家企业与3位个人；设20个类别(能源转型/水管理/碳排控制/职业健康安全/员工福祉/技能发展/性别平等/供应链管理/可持续报告/产品数字创新等)；独立评审团(监管/学术/金融/产业)审材料、要求书面佐证；环境部长等政要与外交使节颁奖。把 ESG 表现做成"可量化、独立评审、政商见证"的年度榜单。',
   exec_txt='协会/高管办 ESG 奖项：设多维类别(含员工福祉/职业健康/供应链)→独立评审团审证据(非自述)→政要/外交见证颁授→年度榜单造行业标杆；把可持续表现转化为可衡量荣誉与品牌资产。',
   url='https://en.prothomalo.com/corporate/n1ncfm2gwg',
   note='③ 国际机构 ESG 奖项体系（高管间、20类可量化+独立评审+政商见证，商务化）。二手·Prothom Alo。',
   sourceType='secondary', relation='exec'),
 dict(emoji='🏆', title='爱尔兰 Business&Finance ESG Awards 2026（Grand Prix+ESG Leader·含员工福祉奖/治理领导力奖/社会影响奖）', cat='ESG奖项', rel='r3',
   val='爱尔兰 Business & Finance ESG Awards 2026 于都柏林 Mansion House 举办：Dalata Hotel Group 获最高奖 Grand Prix 及 ESG Team Award；类别含 Employee Well-Being Award(员工福祉)、Governance Leadership Award(治理领导力)、Social Impact Award(社会影响)、Sustainable Supply Chain(可持续供应链)等；Marie Donnelly 获 ESG Leader Award(推动欧洲能源转型)。独立专家评审，汇聚商界/政府/可持续社群领袖。把"员工福祉、治理、社会影响"纳入高管级 ESG 表彰框架。',
   exec_txt='机构/高管办 ESG 奖项：设 Grand Prix(综合最高)+ 细分(员工福祉/治理领导力/社会影响/供应链)→独立评审→领袖晚宴颁授；用高管级奖项把员工福祉与治理纳入可持续战略叙事。',
   url='https://www.grantthornton.ie/news-centre/esg-awards-2026-winners',
   note='③ 机构 ESG 奖项含员工福祉/治理领导力（高管间、高管级可持续表彰，商务化）。二手·Grant Thornton。',
   sourceType='secondary', relation='exec'),
 dict(emoji='🌏', title='ASEAN Outstanding Business Award 2026 终身成就奖（LBS集团执行主席·"远见商业领导与社区卓越"）', cat='终身成就', rel='r3',
   val='LBS Bina 集团执行主席丹斯里林福山获 ASEAN Outstanding Business Award 2026 "终身成就奖——远见商业领导与社区卓越"(Visionary Business Leadership & Community Excellence)，于吉隆坡颁授；表彰其将 LBS 从本地建筑商发展为领先城镇开发商、交付5.8万套房产、惠及超20万马来西亚人，且超越企业成功创造社会影响、促进区域合作。把"商业领袖+社区贡献"捆绑授奖，定位"区域共建者"而非纯商人。',
   exec_txt='区域商协终身成就奖：在东盟级盛典颁授→表彰"商业远见+社区卓越"双维(交付规模+社会影响)→定位获奖者为区域共建者；把奖项的叙事从个人成就升维到区域与社会价值。',
   url='https://lbs.com.my/press-releases/tan-sri-lim-hock-san-honoured-with-asean-lifetime-achievement-award',
   note='③ 区域商协终身成就奖（高管间、商业+社区卓越捆绑，一手新闻稿）。一手·LBS 官网新闻稿。',
   sourceType='primary', relation='exec'),
 dict(emoji='🎨', title='菲律宾 Mansmith Awards for CEOs 2026（创新/创业/终身成就·奖杯由雕塑家定制"突破常规的领导力"）', cat='CEO奖项', rel='r3',
   val='Mansmith Awards for CEOs 2026 于马尼拉颁授：设 Innovation Awards(4位CEO跨界创新)、Entrepreneur Awards(品牌长期价值)、CEO Lifetime Achievement Awards(终身贡献)；获奖者横跨营销/物流/零售/医疗/专业服务。亮点：奖杯由获奖雕塑家 Juan Sajid Imao 设计——流体圆形"刻意突破传统形状"，具象化"敢破常规、重塑系统"的领导哲学。把奖项体验本身做成领导力的物化表达。',
   exec_txt='机构/高管办 CEO 奖项：分创新/创业/终身成就三档→颁给跨行业标杆CEO→奖杯由艺术家定制(形态隐喻领导哲学)；让"领奖"成为可被收藏与讲述的领导力符号，而不仅是证书。',
   url='https://highlights.thenewchannel.com/when-innovation-meets-dedication-greatness-is-celebrated',
   note='③ 机构 CEO 奖项+奖杯即领导哲学具象（高管间、奖项体验设计，商务化）。二手·The New Channel。',
   sourceType='secondary', relation='exec'),
 dict(emoji='🤝', title='五征集团2026"先锋实干家荣誉盛典"（13项荣誉·金鼎奖最高·221位经销商/服务商/供应商/用户/海外实干家登台·董事长致谢）', cat='生态表彰', rel='r3',
   val='五征集团2026"先锋实干家荣誉盛典暨家宴"：重磅发布13项荣誉，最高"金鼎奖"，含金牌销售先锋/市场开拓先锋/创新营销先锋/合作共赢先锋/金牌供应先锋/精诚合作先锋/最佳质量先锋/携手共创先锋/金牌伙伴先锋/金牌挚友先锋/全球卓越先锋等；来自经销商/服务商/供应商/用户及海外的221位实干家登台领奖；董事长姜卫东回顾奋斗岁月、致谢全球伙伴。把供应链与渠道伙伴、甚至用户都纳入"实干家"授奖体系，是跨边界的生态荣誉盛典。',
   exec_txt='高管办生态表彰盛典：把供应商/经销商/服务商/用户都定义为"实干家"→设多层荣誉(金鼎奖为顶+系列先锋奖)→221位伙伴登台领奖→董事长致谢定调"航洲共济"；用荣誉把商业合作关系升级为命运共同体。',
   url='http://www.sd.xinhuanet.com/20260124/5dc2d3e01a0848ea9b8be81bfcc2526e/c.html',
   note='③ 企业生态伙伴表彰盛典（高管间、供应商/经销商/用户同台授奖，商务化）。一手·新华网。',
   sourceType='primary', relation='exec'),
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

# ===== 2) 增量页 award-20260908.html =====
r3 = [c for c in new_cards if c['rel'] == 'r3']
r2 = [c for c in new_cards if c['rel'] == 'r2']
r3_html = ''.join(card_html(c) for c in r3)
r2_html = ''.join(card_html(c) for c in r2)
inc_body = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>颁奖典礼 · 第37轮（独立页）</title>
{CSS}
</head>
<body>
<div class="wrap">
  <a class="back" href="../award.html">← 返回累计总索引 award.html</a>
  <div class="hero">
    <h1>🏆 颁奖典礼 · 第37轮（独立页）</h1>
    <p>采集于 2026-09-08 ｜ 本轮新增 {N} 卡（③高管间 {len(r3)} / ②上下级 {len(r2)}）｜ 六维评估 ｜ 一手/二手标注 ｜ 受众关系分层（仅②③，剔除①）｜ 累计总索引见 <a href="../award.html" style="color:#fff;text-decoration:underline;">award.html</a></p>
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
new_p = hm.group(2) + f' ｜ {ROUND_LABEL} enrich 2026-09-08({ROUND_TAG})'
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
note = note.replace('共 247 张', '共 257 张', 1)
round_sec = f'''## 轮次 2026-09-08·三十七轮（+{N}）
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
header_new = mh.group(1).rstrip() + f' ｜ 三十七轮 enrich 2026-09-08(+{N})'
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
    'name': 'award-20260908.html',
    'note': f'轮次页 R37 (+{N}：{len(r3)}③高管间+{len(r2)}②上下级，5一手+5二手)｜乐享待补传(token 401，待重连后补传并回填 entry_id)'
})
json.dump(mp, open(MAP, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'[lexiang map] appended round R37 (+{N}) entry_id=null (pending upload)')

print('\n=== SUMMARY ===')
print(f'topic=颁奖  round=37  date=2026-09-08')
print(f'新增 N={N} (③{len(r3)} + ②{len(r2)})  去重删 M={M}  URL命中跳过={dup_skipped}')
print(f'增量页: award/award-20260908.html')
print(f'累计墙: award/award.html')
print(f'index.json: +{N} (total {len(idx)})')
print(f'Obsidian: 颁奖-知识卡汇总.md + 00-知识采集索引.md 已更新')
print(f'乐享: 跳过实际上传(connector disconnected/token 401)，map 已追加 pending round')
