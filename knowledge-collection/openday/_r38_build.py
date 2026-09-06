# -*- coding: utf-8 -*-
"""Open Day r38 enrich build — 8 new cards (②×5 / ③×3), all NEW in index."""
import json, os, re

BASE = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(BASE, 'openday.html')
TMP  = os.path.join(BASE, '.run_newcards.tmp.html')
IDX  = os.path.join(os.path.dirname(BASE), 'index.json')

# ---- 8 cards ----
cards = []

# ② 上下级 ×5
cards.append('''<div class="hl">
  <div class="top"><span class="emoji">🔬</span><h3>青岛市2026"科技筑梦 育见未来"科普游（7所高校实验室路线·青少年常态化科普）</h3><span class="cat">高校科普游/城市级项目</span><span class="badge r2">上下级</span><span class="badge b1">一手</span></div>
  <p class="val">青岛市科协2026年启动"科技筑梦 育见未来"科普游，发布7条高校实验室路线（山东大学微生物/中国海洋大学海洋生命/石油大学石油地质/青岛大学理化/山东科技土木/青岛科技化学/青岛理工物理），面向中小学生常态化开放，把高校国家级实验室变成"可预约的科普课堂"；每路由专家报告+显微镜实操+趣味实验组成，是"大科普"格局下资源整合与教育创新的城市样本。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">把开放日升级为"城市级科普游项目"而非单次活动——以7条高校专线把散落实验室资源打包成可预约产品，常态化（非一年一次）触达青少年；每条路线"专家报告+动手实验"标准化，政府/科协做资源整合方。</div></details>
  <div class="src">🔗 <a href="https://www.qdast.org.cn/kxdt/KXYW/art/2026/art_d368cb1874e044409c975887963cda46.html" target="_blank">www.qdast.org.cn/kxdt/KXYW/art/2026/art_d368cb1874e044409c975887963cda46.html</a></div>
  <div class="note">适用：② 城市级高校科普游（青岛市科协一手），教育部门/科协以"资源组织者"姿态，青少年走进高校实验室常态化科普，专业严谨、不娱乐化。</div>
</div>''')

cards.append('''<div class="hl">
  <div class="top"><span class="emoji">🧬</span><h3>复旦大学复杂性状遗传调控全国重点实验室公众开放日（5-8年级·基因世界）</h3><span class="cat">高校实验室开放日</span><span class="badge r2">上下级</span><span class="badge b1">一手</span></div>
  <p class="val">复旦大学复杂性状遗传调控全国重点实验室2026.5.30在江湾校区举办社会公众开放日（第八个"全国科技工作者日"），全市多所5-8年级中小学生走进实验室；副主任以"与基因握手交谈"开场，分组进"中华古史探秘"（DNA讲历史）/植物避荫反应/细胞死亡与免疫三平台，通过显微镜观察、简易实验触摸科研；实验室还持续接待社会公众来访。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">高校实验室开放日做"分龄分层"——给5-8年级设计"基因/植物/细胞"三主题互动平台，用生活问题（你长得像谁/植物怎么竞争光）切入高深遗传；现场观察蛋白质晶体、亲手做实验，把"科研"变"可触摸的探索"。</div></details>
  <div class="src">🔗 <a href="http://sklgdp.fudan.edu.cn/f1/de/c48803a782814/page.htm" target="_blank">sklgdp.fudan.edu.cn/f1/de/c48803a782814/page.htm</a></div>
  <div class="note">适用：② 高校重点实验室公众开放日（复旦一手），科研团队以"科学引路人"姿态，青少年走进国家级实验室，分龄分层、专业不幼稚。</div>
</div>''')

cards.append('''<div class="hl">
  <div class="top"><span class="emoji">🔬</span><h3>南昌大学基础医学院实验室开放日（千名中小学生·显微探微观）</h3><span class="cat">高校实验室开放日</span><span class="badge r2">上下级</span><span class="badge b1">一手</span></div>
  <p class="val">南昌大学基础医学院2026.7.9-10举办第四届实验室开放日，主题"奋进科普十五五，探索生命万千象"，南昌市1000余名中小学生及家长走进专业实验室；在病原生物学实验室化身"小小侦探"找微生物、形态学实验室看肾脏"净化工厂"动画、亲手操作显微镜；由工会+学院+志愿者协会+思政工作室多方协同，党建思政引领科普。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">高校实验室开放日做"规模+思政"——单场承接千名中小学生，用"显微世界/形态学/病原侦探"三模块把生命科学变沉浸课；"校地科普协同+思政引领"组织模式可复制；鼓励"敢于质疑"开场，把科研精神种进孩子心里。</div></details>
  <div class="src">🔗 <a href="https://bms.ncu.edu.cn/xyxw/ba86eba5efae474faf908e3996ee5d07.htm" target="_blank">bms.ncu.edu.cn/xyxw/ba86eba5efae474faf908e3996ee5d07.htm</a></div>
  <div class="note">适用：② 高校医学院实验室开放日（南昌大学一手），医学团队以"生命科学引路人"姿态，中小学生显微镜下探微观，规模承接+思政引领。</div>
</div>''')

cards.append('''<div class="hl">
  <div class="top"><span class="emoji">🧪</span><h3>新余市市场监管局2026"政府开放日"·探秘食药检测·守护健康"童"行（免费送检+亲子）</h3><span class="cat">政府开放日/食药透明化</span><span class="badge r2">上下级</span><span class="badge b1">一手</span></div>
  <p class="val">新余市市场监管局2026.8.20办"政府开放日"，主题"探秘食药检测·守护健康童行"，邀6-18岁中小学生及家长20人走进市综合检验检测中心；四阶段流程：看宣传片→食药检测科普宣讲→实验室沉浸式体验检测流程→问答讨论；把"食品药品检测"从幕后搬到台前，让公众看懂"舌尖上的安全"如何被守护。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">政府开放日做"食药透明化+亲子科普"——以"免费送检/实验室沉浸体验"打破检测机构神秘感；限龄限人（6-18岁+家长、20人）保证互动质量；四阶段"看-讲-做-议"闭环；市场监管部门以"透明服务者"姿态建信任。</div></details>
  <div class="src">🔗 <a href="https://scjg.xinyu.gov.cn/scj/gggs/2026-08/11/content_94d577dfb2e34aa599eb669ba1e989c6.shtml" target="_blank">scjg.xinyu.gov.cn/scj/gggs/2026-08/11/content_94d577dfb2e34aa599eb669ba1e989c6.shtml</a></div>
  <div class="note">适用：② 食药检测政府开放日（新余市政府一手），市场监管部门以"透明服务者"姿态，亲子家庭走进检测实验室看懂食安，尊重边界、专业不幼稚。</div>
</div>''')

cards.append('''<div class="hl">
  <div class="top"><span class="emoji">📐</span><h3>开放日设计方法论（Engage for Success·互动/≤50人/固定时段/免费）</h3><span class="cat">方法论/开放日设计</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
  <p class="val">英国员工敬业度机构 Engage for Success 的开放日指南：核心原则——互动性（访客与host组织员工充分对话、提问）、可看性（展示真实工作场景/车间/团队环境）、安全性（不参与未经培训的工作）、规模≤50人保互动质量、固定到离时段（非"随时开门"）、活动免费；可含领导简述敬业实践+访客参观工作地+参与敬业工作坊+知识互换。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">把"办开放日"当方法论套用——先定"互动/可看/安全/小众(≤50)/定时/免费"六原则；用"领导讲敬业→员工带看现场→共创工作坊→知识互换"四段式把访客变参与者；直接迁移到企业/部门开放日策划，避免"走马观花式开放"。</div></details>
  <div class="src">🔗 <a href="https://engageforsuccess.org/running-an-open-day/" target="_blank">engageforsuccess.org/running-an-open-day/</a></div>
  <div class="note">适用：② 开放日策划方法论（Engage for Success二手），适用于企业/部门内部开放日设计，六原则+四段式可直接复用。</div>
</div>''')

# ③ 高管间 ×3
cards.append('''<div class="hl">
  <div class="top"><span class="emoji">🌍</span><h3>迪拜商会在沪举办企业家圆桌会议（中企出海中东·高管对话平台）</h3><span class="cat">国际商会圆桌/出海</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
  <p class="val">迪拜商会2026.7在沪举办圆桌，邀先进制造/跨境电商/新材料/医疗健康/低空经济/AI等领域二十余位国内头部企业高管、产业投资者齐聚，搭建中企布局中东高质量对话平台；迪拜商会执行副总裁致辞、驻沪代表做《为什么选择迪拜》推介（区位/低税/无外汇管制/自由区集群），君合律所合伙人讲合规架构；围绕中东市场洞察、政策环境、合规与运营实践深入对话。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">把"商会圆桌"做成出海高管对话场——以"东道主商会+头部企业高管+产业投资者"同量级阵容，围绕"目标市场政策/合规/落地"务实对话（非寒暄）；用"专题推介+法律合规洞见+圆桌问答"结构，把开放日变"战略情报+资源对接"双价值场；忌幼稚互动。</div></details>
  <div class="src">🔗 <a href="https://new.qq.com/rain/a/20260706A05IBI00?refer=cp_1009" target="_blank">new.qq.com/rain/a/20260706A05IBI00</a></div>
  <div class="note">适用：③ 国际商会企业家圆桌（腾讯新闻二手），商会以"跨境生态组织者"姿态，企业高管围绕出海中东务实对话，商务化、以共同目标切入，层级清晰不越界。</div>
</div>''')

cards.append('''<div class="hl">
  <div class="top"><span class="emoji">🌐</span><h3>GGF2026 出海全球化百人论坛·圆桌"AI时代的全球化核心竞争力"</h3><span class="cat">出海论坛/高管圆桌</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
  <p class="val">出海全球化智库EqualOcean主办"2026出海全球化百人论坛"(GGF2026)2026.6.11在上海落幕，聚焦AI驱动全球化、品牌出海、制造业出海、合规风控；圆桌"AI时代的全球化核心竞争力"邀嘉御资本/中欧商业联合会/凯度电器/黑湖科技/MAGICBEAN创始人CEO同台，围绕"中国企业全球化竞争力如何重构、AI是短暂红利还是持久优势"深度对话，数百位出海企业家、投资人、行业专家参与。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">把"行业论坛圆桌"做成高管思想交锋场——以智库主办+头部企业创始人/CEO同台，围绕"AI×全球化"等战略命题展开（非产品宣讲）；用"多视角一个方向"结构化讨论，把开放日变"认知升级+人脉链接"的高管场；以专业/共同目标切入。</div></details>
  <div class="src">🔗 <a href="https://new.qq.com/rain/a/20260618A00RS800?refer=cp_1009" target="_blank">new.qq.com/rain/a/20260618A00RS800</a></div>
  <div class="note">适用：③ 出海全球化论坛圆桌（EqualOcean/腾讯新闻二手），智库以"行业思想领袖"姿态，企业创始人/CEO围绕全球化战略对话，商务化、以命题共创切入。</div>
</div>''')

cards.append('''<div class="hl">
  <div class="top"><span class="emoji">🤝</span><h3>2026沪港企业家圆桌会·"共拓十五五新格局 共创出海新生态"</h3><span class="cat">两地商会圆桌/高管对话</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
  <p class="val">2026.5.9上海市总商会与香港中华总商会在香港举办"共拓十五五新格局 共创出海新生态"2026沪港企业家圆桌会，上海市委统战部部长、香港特区立法会主席、香港中华总商会会长等出席致辞；围绕金融/贸易/航运/科创领域沪港功能互补、携手出海、科创融合展开，展望以香港首个五年规划为契机深化合作的机遇。</p>
  <details class="exec"><summary>怎么做</summary><div class="inner">把"两地商会圆桌"做成区域协同高管对话——以"总商会×中华总商会"同量级主办方，邀两地政商高层围绕"十五五/出海新生态"战略对话（非社交寒暄）；用"互补领域点题+高层致辞定调+圆桌共商"结构，把开放日变"跨城战略协同"场；商务化、以共同目标切入。</div></details>
  <div class="src">🔗 <a href="https://www.chinanews.com.cn/txy/2026/05-12/10619558.shtml" target="_blank">www.chinanews.com.cn/txy/2026/05-12/10619558.shtml</a></div>
  <div class="note">适用：③ 沪港企业家圆桌会（中国新闻网二手），两地商会以"区域协同组织者"姿态，政商高层围绕十五五/出海生态对话，商务化、以共同目标切入，层级清晰不越界。</div>
</div>''')

# ---- split into ② (first 5) and ③ (last 3) ----
cards_2 = cards[:5]
cards_3 = cards[5:]

# ===== 1. update cumulative wall =====
html = open(WALL, encoding='utf-8').read()

# counts
html = html.replace('<span class="tag">262 卡</span>', '<span class="tag">267 卡</span>', 1)
html = html.replace('<span class="tag">56 卡</span>', '<span class="tag">59 卡</span>', 1)

# hero round append
html = html.replace('全一手+8二手)</p>',
                   '全一手+8二手) ｜ 三十八轮补采 2026-09-06(+8，青岛科普游·复旦·南昌大学·新余食药·开放日设计方法论 + 迪拜商会·GGF2026·沪港圆桌)</p>', 1)

# insert ② cards before the mixed grid at 177735 (end of main ② grid)
marker = '<div class="grid">'
pos = html.find(marker, 140000)  # first grid after sec2 header region; the mixed grid is the 3rd occurrence
# find the specific mixed grid: it's the one whose following card is 市长企业家早餐会 (r3). locate by context
import re
m = re.search(r'<div class="grid">\s*<div class="hl">\s*<div class="top"><span class="emoji">🍳</span>', html)
assert m, "mixed grid anchor not found"
insert_at = m.start()
html = html[:insert_at] + '\n'.join(cards_2) + '\n' + html[insert_at:]

# insert ③ cards before </body>
body_pos = html.rfind('</body>')
html = html[:body_pos] + '\n'.join(cards_3) + '\n' + html[body_pos:]

open(WALL, 'w', encoding='utf-8').write(html)

# ===== 2. write tmp newcards file (all 8 for gen_run_page) =====
open(TMP, 'w', encoding='utf-8').write('\n'.join(cards))

# ===== 3. update index.json =====
idx = json.load(open(IDX, encoding='utf-8'))
meta = [
 ('青岛市2026"科技筑梦 育见未来"科普游（7所高校实验室路线）','https://www.qdast.org.cn/kxdt/KXYW/art/2026/art_d368cb1874e044409c975887963cda46.html','primary','supervisor','青岛市科协官网一手：7条高校实验室路线把国家级实验室变可预约科普课堂，常态化触达青少年','青岛市科协'),
 ('复旦大学复杂性状遗传调控全国重点实验室公众开放日','http://sklgdp.fudan.edu.cn/f1/de/c48803a782814/page.htm','primary','supervisor','复旦官网一手：5-8年级中小学生进实验室，基因/植物/细胞三主题互动平台分龄分层','复旦大学'),
 ('南昌大学基础医学院实验室开放日（千名中小学生）','https://bms.ncu.edu.cn/xyxw/ba86eba5efae474faf908e3996ee5d07.htm','primary','supervisor','南昌大学官网一手：千名中小学生显微探微观，规模承接+思政引领的医学科普范式','南昌大学'),
 ('新余市市场监管局2026"政府开放日"·探秘食药检测','https://scjg.xinyu.gov.cn/scj/gggs/2026-08/11/content_94d577dfb2e34aa599eb669ba1e989c6.shtml','primary','supervisor','新余市政府一手：食药检测透明化+亲子科普，四阶段看-讲-做-议闭环','新余市政府'),
 ('开放日设计方法论（Engage for Success）','https://engageforsuccess.org/running-an-open-day/','secondary','supervisor','英国员工敬业度机构指南：互动/可看/安全/≤50人/定时/免费六原则+四段式开放日设计框架','Engage for Success'),
 ('迪拜商会在沪举办企业家圆桌会议（中企出海中东）','https://new.qq.com/rain/a/20260706A05IBI00?refer=cp_1009','secondary','exec','腾讯新闻二手：迪拜商会邀头部企业高管围绕出海中东政策/合规/落地务实对话','腾讯新闻'),
 ('GGF2026 出海全球化百人论坛·圆桌AI时代全球化','https://new.qq.com/rain/a/20260618A00RS800?refer=cp_1009','secondary','exec','EqualOcean/腾讯新闻二手：出海智库论坛圆桌，企业创始人CEO围绕AI×全球化战略命题交锋','EqualOcean/腾讯新闻'),
 ('2026沪港企业家圆桌会·共拓十五五新格局','https://www.chinanews.com.cn/txy/2026/05-12/10619558.shtml','secondary','exec','中国新闻网二手：沪港两地总商会邀政商高层围绕十五五/出海新生态战略对话','中国新闻网'),
]
existing = {e.get('url','').strip().lower().rstrip('/') for e in idx}
added = 0
for title, url, st, rel, summ, src in meta:
    if url.strip().lower().rstrip('/') in existing:
        continue
    idx.append({
        'title': title, 'normKey': title.replace(' ',''), 'url': url,
        'sourceType': st, 'relation': rel, 'summary': summ,
        'topic': 'Open Day', 'slug': 'openday', 'source': src
    })
    existing.add(url.strip().lower().rstrip('/'))
    added += 1

json.dump(idx, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f"WALL updated. cards_2={len(cards_2)} cards_3={len(cards_3)} index_added={added} total_index={len(idx)}")
