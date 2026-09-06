# -*- coding: utf-8 -*-
"""颁奖 三十五轮 enrich（2026-09-06 第二次轮次）构建脚本。
仅保留 ②上下级 / ③高管间 两档，剔除平级/朋友向。
产出：增量页 award-20260906b.html + 注入累计墙 award.html + index.json + Obsidian 笔记 + 00索引 + lexiang map。
"""
import re, os, json

BASE = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(BASE, 'award', 'award.html')
INC = os.path.join(BASE, 'award', 'award-20260906b.html')
TMP = os.path.join(BASE, 'award', '.run_newcards.tmp.html')
IDX = os.path.join(BASE, 'index.json')
MAP = os.path.join(BASE, 'lexiang-entry-map.json')
NOTE = r'C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\award\颁奖-知识卡汇总.md'
IDX00 = r'C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md'
RUN_DATE = '2026-09-06'
ROUND_LABEL = '三十五轮'
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
 dict(emoji='🏅', title='Adani 长期服务奖官方政策（10/15/20/25年里程碑·CEO/CPO亲颁+银章现金）', cat='长期服务', rel='r2',
   val='Adani Green 官方政策：连续服务里程碑 10/15/20/25 年；到点由 BU-HR+CEO 或等效 BU Head+集团 CPO 发感谢信、献花、安排与 Site/Location Head 会面；年度盛典颁 100g 银章（带 logo）；满 25 年邀见 Promoters/APEX 成员与集团 CPO。奖金：15年₹150,000 / 20年₹250,000 / 25年₹500,000 + 银章。高层参与显著提升荣誉份量。',
   exec_txt='HR/行政落长期服务奖：定连续司龄里程碑→高层(CEO/CPO/BU Head)亲颁+写感谢信→年度盛典统一授章→重大里程碑邀见最高层；奖金+纪念章双轨，避免只发钱缺仪式感。',
   url='https://www.adanigreenenergy.com/-/media/project/greenenergy/corporate-governance/policy/long-service-award-policy.pdf',
   note='② HR/行政设计长期服务奖（上下级忠诚认可，高层亲颁提升荣誉感）。一手·Adani Green 官方政策 PDF。',
   sourceType='primary', relation='supervisor'),
 dict(emoji='🗺️', title='价值分配系统·企业荣誉体系「全景地图」（殿堂级长期服务奖+治理层防腐）', cat='荣誉体系', rel='r2',
   val='荣誉体系=多层次立体网络：顶层殿堂级(年度/半年度·对标奥斯卡)含管理者特别奖/价值观大奖/长期服务奖(5银·10金·15钻，定制信物+红毯+家属受邀+纪录片内网刷屏)；中层战功级(季度/项目·实物奖品+照片上墙+专属车位)；底层即时认可(Spot Bonus 经理手中有预算即发+电子勋章·24h内)。治理层：殿堂级须荣誉委员会(管理者+高管+员工代表)评审、全员公示异议、造假即撤；荣誉与晋升答辩挂钩。',
   exec_txt='HR/高管搭荣誉体系：顶层树标杆(长期服务奖阶梯+隆重庆典+故事化传播)→中层刺产出(实物+环境展示)→底层润关系(经理小额即时+24h)→治理防腐(委员会评审+公示+与晋升挂钩)。',
   url='https://m.hrloo.com/rz/14781546.html',
   note='② HR/高管设计企业荣誉体系全景（上下级、长期服务奖为顶层支柱，治理防通胀/分猪肉）。二手·三茅网。',
   sourceType='secondary', relation='supervisor'),
 dict(emoji='📜', title='干部职工荣誉退休仪式方案（谈心谈话+宣读批文+颁证+家属+领导主持·gov一手）', cat='荣休仪式', rel='r2',
   val='濮阳市人大方案：会前主要领导/秘书长与退休干部谈心谈话(政策待遇答疑)；仪式由主要领导/秘书长主持——①宣读退休批文 ②颁发荣誉退休证书/奖章 ③赠送纪念品鲜花 ④合影 ⑤在职互动。参加含常委会主要领导/委办室主任/人事老干等部门。组织保障细化到科室(证书奖章采购/主持词/座签)。把退休做成有温度的组织告别。',
   exec_txt='行政/HR 办荣休：领导主持+宣读批文+颁荣誉证章+赠纪念品鲜花+合影→会前一对一谈心(政策待遇)→明确组织分工(证书采购/主持词/座签)；庄重温馨兼具。',
   url='https://pysrd.henanrd.gov.cn/2025/12-17/230738.html',
   note='② 行政/工会办员工荣休仪式（上下级、领导主持颁证+家属，尊重不越界）。一手·濮阳人大 gov 方案。',
   sourceType='primary', relation='supervisor'),
 dict(emoji='🌸', title='荣休仪式领导致辞「不舍·情怀·关爱」三维度框架（妇幼保健院一手案例）', cat='荣休致辞', rel='r2',
   val='西充县妇幼保健院荣休仪式：院长/党总支书记温情讲话三维度——①满心不舍：数十年坚守岗位、与单位同成长、是同事更是战友；②妇幼如家：岗位有终点情谊不落幕，常回"家"看看；③温情关爱：把对老职工的敬重落到实处(持续关怀服务)。现场献花+颁荣誉纪念证书与纪念品，家属共同见证。',
   exec_txt='领导/主管写荣休致辞：用「不舍(战友情)+情怀(如家)+关爱(持续关怀)」三维度→点名具体贡献与难忘瞬间→邀家属共证→落"常回家看看"暖尾；拒空泛套话与数据堆砌。',
   url='https://sc.china.com.cn/2026-07/21/content_43464628.html',
   note='② 领导/主管写荣休致辞（上下级、温情三维度，尊重不越界）。一手·中国网四川报道案例。',
   sourceType='primary', relation='supervisor'),
 dict(emoji='🏆', title='总裁俱乐部机制·资格阶梯+舞台表扬+奖励旅游（销售精英认可）', cat='销售激励', rel='r2',
   val='4Life 总裁俱乐部=顶尖销售认可机制：资格阶梯(黄金总监I/II、白金总裁、首席白金总裁，按12个月内达成阶衔月数)；每两年大会表杨、豪华VIP体验、普吉岛奖励旅游；资格持续至隔年12月。把"最高销售成就"做成稀缺荣誉+旅行体验，向全员传递"够优秀就能被特别看见"。',
   exec_txt='销售/高管设总裁俱乐部：定阶衔资格阶梯(按月数达成)→年度大会舞台表扬+VIP体验→奖励旅游(目的地仪式感颁奖)→资格期延续制造长期目标；让顶尖销售被看见、成榜样。',
   url='https://taiwan.4life.com/hd/page/148/presidents-club',
   note='② 销售负责人/高管设总裁俱乐部（上下级、销售精英认可+奖励旅游，非平级游戏）。一手·4Life 官方。',
   sourceType='primary', relation='supervisor'),
 dict(emoji='🔝', title='自上而下认可体系·经理提名审批+公司活动公开颁奖（连接领导与员工）', cat='认可体系', rel='r2',
   val='Workhuman：自上而下奖(top-down)由领导层连接员工、确保战略聚焦；经理负责提名与审批，适合高价值正式奖(年度卓越/晋升认可)，在公司活动由领导公开颁奖。优点：战略对齐、领导可见、员工感到被高层重视。缺点：仅靠此易漏掉日常贡献、造成年度单点瓶颈。需与 peer 即时认可互补。',
   exec_txt='HR/高管搭自上而下认可：经理提名审批高价值正式奖→公司活动由领导公开颁奖→与 peer 即时认可互补(避免只年终单点)→用奖项传递战略重点。',
   url='https://www.workhuman.com/blog/employee-recognition-awards',
   note='② HR/高管设计自上而下认可（上下级、经理提名审批+领导公开颁奖，战略对齐）。一手·Workhuman 官方博客。',
   sourceType='primary', relation='supervisor'),
 dict(emoji='🏅', title='政府质量奖·企业如何带队申报并登台领奖（区长质量奖/高管陈述答辩）', cat='专项质量奖', rel='r2',
   val='浦东新区政府质量奖(区长质量奖最高)：每五年评一次，自下而上、好中选优；申报前内部公示≥5工作日、资格审查、材料评审、现场评审、高管(管理层代表)陈述答辩、审定公示、区政府颁奖。评审标准 GB/T 19580 卓越绩效。获奖发奖牌证书+奖金，须发挥标杆示范、每年报绩效。是企业"质量标杆+政府背书"杠杆。',
   exec_txt='企业质量/高管带队申政府质量奖：先内部公示→备材料(卓越绩效自评)→现场评审→高管亲陈述答辩→区领导颁奖；把奖项当质量标杆与政府背书杠杆，反哺内部改进。',
   url='https://www.pudong.gov.cn/zwgk/qt-qzf/2025/345/348574.html',
   note='② 企业质量负责人/高管带队申报政府质量奖（上下级、内部公示+高管答辩+政府颁奖）。一手·浦东新区 gov 管理办法。',
   sourceType='primary', relation='supervisor'),
 dict(emoji='🌐', title='高阶领袖激励行程·专属社群晚宴+高空圆桌（决策者共创愿景）', cat='高管激励', rel='r3',
   val='奖励旅游分线：高阶领袖激发行程=汇聚决策者与创变者，透过专属社群晚宴与高空圆桌，激荡更大愿景与责任感。把"奖励"升维为"战略对话场"——在放松中完成跨高管共识。区别于菁英员工表杨之旅(感谢之路/主管亲颁)与 Top Sales 尊荣盛典，定位纯高管间思想碰撞。',
   exec_txt='高管/HR 办高阶领袖行程：选决策者同频群体→专属社群晚宴+高空圆桌设战略议题→在体验中沉淀跨高管共识与责任感；非单纯享乐，落战略对话。',
   url='https://jollifytravel.com/incentives',
   note='③ 高管/HR 办高阶领袖激励行程（高管间、社群晚宴+圆桌共创愿景，商务化）。二手·jollifytravel。',
   sourceType='secondary', relation='exec'),
 dict(emoji='🏛️', title='行业名人堂颁奖·企业领袖互颁+终身成就标杆（中国酒店名人堂）', cat='名人堂', rel='r3',
   val='中国酒店名人堂颁奖：200+行业领袖/运营管理者/院校专家共证；往届功勋人物任提名委员、现任董事长/协会会长/院校院长等高管互颁；中国旅游协会会长致辞"入选者引领行业发展、激励年轻一代"。核心=铭记奋斗史、树立卓越标杆、见贤思齐。行业奥斯卡级别荣誉。',
   exec_txt='高管/协会办行业名人堂：设提名委员会(往届功勋)+终审→行业领袖互颁→会长/院长致辞升华(标杆引领)→传播功勋事迹激励同业；把荣誉做成行业精神资产。',
   url='https://m.tech.china.com/hea/articles/20251107/202511071761011.html',
   note='③ 高管/协会办行业名人堂颁奖（高管间、领袖互颁+终身成就，商务标杆）。二手·中华网科技。',
   sourceType='secondary', relation='exec'),
 dict(emoji='🎓', title='名人堂+终身成就奖·创始人董事长获颁（理大荣誉体系案例）', cat='名人堂', rel='r3',
   val='香港理工大学酒店及旅游业管理学院将美诺国际创始人兼董事长 William Heinecke 列入名人堂，并颁「终身成就奖」；由行政及拓展副校长、学院院长及讲座教授颁授奖座、于晚宴致欢迎辞、获奖者发表感言。表彰近60年带领公司从初创到全球最大酒店集团之一、推动行业变革的领导力。',
   exec_txt='高管/校方办名人堂+终身成就奖：由最高层(副校长/院长)颁授→晚宴致辞+获奖者感言→定位"终身领导力标杆"；用于致敬创始人/董事长的行业贡献。',
   url='https://polyu.edu.hk/tc/media/Media-Releases/2025/0520_Pioneering-entrepreneur-William-Heinecke-inducted-into-SHTM-Gallery-of-Honour',
   note='③ 高管/校方办名人堂+终身成就奖（高管间、最高层颁授创始人董事长，商务标杆）。一手·香港理工大学官方发布。',
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

# ===== 2) 增量页 award-20260906b.html =====
r3 = [c for c in new_cards if c['rel'] == 'r3']
r2 = [c for c in new_cards if c['rel'] == 'r2']
r3_html = ''.join(card_html(c) for c in r3)
r2_html = ''.join(card_html(c) for c in r2)
inc_body = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>颁奖典礼 · 第35轮补采（独立页）</title>
{CSS}
</head>
<body>
<div class="wrap">
  <a class="back" href="../award.html">← 返回累计总索引 award.html</a>
  <div class="hero">
    <h1>🏆 颁奖典礼 · 第35轮补采（独立页）</h1>
    <p>采集于 2026-09-06 ｜ 本轮新增 {N} 卡（③高管间 {len(r3)} / ②上下级 {len(r2)}）｜ 六维评估 ｜ 一手/二手标注 ｜ 受众关系分层（仅②③，剔除①）｜ 累计总索引见 <a href="../award.html" style="color:#fff;text-decoration:underline;">award.html</a></p>
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
new_p = hm.group(2) + f' ｜ {ROUND_LABEL} enrich 2026-09-06({ROUND_TAG})'
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
# 更新 摘要 计数 226 -> 236
note = note.replace('共 226 张', '共 236 张', 1)
round_sec = f'''## 轮次 2026-09-06·三十五轮（+{N}）
本轮新增（均通过六维评估、仅 ②上下级 / ③高管间）：
'''
for c in new_cards:
    rel_text = '②上下级' if c['rel'] == 'r2' else '③高管间'
    src_text = '一手' if c['sourceType'] == 'primary' else '二手'
    round_sec += f"- {c['title']}（award/award.html） | {rel_text} | {src_text}\n"
# 插入到第一个 轮次 段之前
m = re.search(r'\n## 轮次 ', note)
assert m, 'round section not found'
note = note[:m.start()] + round_sec + note[m.start():]
open(NOTE, 'w', encoding='utf-8').write(note)
print(f'[obsidian note] inserted round section (+{N})')

# ===== 6) 00-知识采集索引.md =====
idx00 = open(IDX00, encoding='utf-8').read()
# 更新 section header（## 主题：颁奖典礼 ...）追加本轮
mh = re.search(r'^(## 主题：颁奖典礼.*)$', idx00, re.M)
assert mh, 'award section header not found'
header_new = mh.group(1).rstrip() + f' ｜ 三十五轮 enrich 2026-09-06(+{N})'
idx00 = idx00[:mh.start()] + header_new + idx00[mh.end():]
# 在表格分隔行 |---|---|---|---|---| 后插入新行（award 表头为该5列格式）
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
    'name': 'award-20260906b.html',
    'note': f'轮次页 R35 (+{N}：{len(r3)}③高管间+{len(r2)}②上下级，{sum(1 for c in new_cards if c["sourceType"]=="primary")}一手+{sum(1 for c in new_cards if c["sourceType"]=="secondary")}二手)｜乐享待补传(connector disconnected/token 401，待重连后补传并回填 entry_id)'
})
json.dump(mp, open(MAP, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'[lexiang map] appended round R35 (+{N}) entry_id=null (pending upload)')

print('\n=== SUMMARY ===')
print(f'topic=颁奖  round=35  date=2026-09-06')
print(f'新增 N={N} (③{len(r3)} + ②{len(r2)})  去重删 M={M}  URL命中跳过={dup_skipped}')
print(f'增量页: award/award-20260906b.html')
print(f'累计墙: award/award.html')
print(f'index.json: +{N} (total {len(idx)})')
print(f'Obsidian: 颁奖-知识卡汇总.md + 00-知识采集索引.md 已更新')
print(f'乐享: 跳过实际上传(connector disconnected/token 401)，map 已追加 pending round')
