# -*- coding: utf-8 -*-
# Open Day 二十四轮补采（r24, 2026-08-23）+6 卡：5 ②上下级 + 1 ③高管间
# 新域：国企开放日(城市级) / 企业公众开放日 / 工厂游方法论 / 车企工业旅游开放日 / 政府开放月水务 / 高管间闭门可持续转型
import re, os, json

WS = r"C:\Users\v_yitcai\WorkBuddy\20260728154244"
KC = os.path.join(WS, "knowledge-collection")
HTML = os.path.join(KC, "openday", "openday.html")
INC  = os.path.join(KC, "openday", "openday-20260823.html")
CACHE= os.path.join(KC, "openday", ".rows_cache.json")
IDX  = os.path.join(KC, "index.json")
OB_SUM = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\openday\OpenDay-开放日-知识卡汇总.md"
OB_IDX = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
GH = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday-20260823.html"

cards = [
 dict(emoji='🏛️', title='北京市国资委 2026「首都国企开放日」（45 家国企 142 条线路·常态化开放）', cat='国企开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.beijing.gov.cn/gate/big5/www.beijing.gov.cn/renwen/sy/whkb/202606/t20260602_4682358.html',
      val='北京市国资委启动 2026「首都国企开放日」，45 家首都国企推出 142 条线路（点位）向市民开放，覆盖企业博物馆、生产车间、研发实验室、重点工程现场、城市更新项目、民生服务阵地、职工创新工作室、研学基地等；首次突破集中模式，周期从 2026.4 贯穿至 2027.3，推行「特定时段集中开放+常态化开放」双轨，紧扣国庆中秋等节点联动阅读季、国企消费季等活动，让国企文化融入城市生活；市民经「国资京京」公众号及专属小程序一键查线路、点位、容量。',
      how='把「国企开放日」从一日盛会升级为全年长效开放——用 142 条主题线路塑造「一企一特色」矩阵，覆盖车间/实验室/城市更新等多元场景；以「集中开放+常态开放」双轨降低参与门槛；用官方小程序做一站式预约导览；把开放日与城市节庆/消费季绑定，让国企形象自然走进市民日常。',
      note='② 城市级国企开放日（北京市政府/国资委官网一手），国资委领导以城市共建者姿态，市民/师生/行业代表/媒体零距离感受国企民生保障与科技创新硬核担当。'),
 dict(emoji='🚛', title='山东重工中国重汽 2026 合作伙伴大会「公众开放日」·可触摸的品牌温暖之旅', cat='企业公众开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://app.people.cn/h5/detail/normal/6628265830679552',
      val='山东重工中国重汽在 2026 合作伙伴大会期间办「公众开放日」，员工及家属、社会公众逾万人参与；以全景式沉浸式展览呈现新能源、数智化、自动驾驶成果，从数智化方案到新能源整车及核心技术、覆盖重中轻微客特全系列商用车产业链；设超级卡车打卡、模拟驾驶、答题扭蛋、拉花咖啡等十余项互动；乐高创意车间、涂鸦、热缩片手作工坊让品牌认同在亲子共创中萌芽；恰逢成立 95 周年，特别邀请退休干部职工重回展区，承载制造强国精神薪火相传。',
      how='把企业开放日做成「可触摸、可互动、可带走」的品牌深度体验——用全景沉浸展区系统呈现技术矩阵；以模拟驾驶/手作工坊等体验环节把硬核科技变可亲可感；借周年节点邀请退休职工回流，把品牌传承与情感连接做进互动；用亲子共创让认同感代际传递。',
      note='② 企业公众开放日（人民网一手），企业领导以品牌共建者姿态，员工家属/社会公众沉浸式感受中国制造实力与人文温度，强化品牌认同。'),
 dict(emoji='🏭', title='半月谈｜不再「谢绝参观」，「工厂游」拉满体验感（盼盼/小米/青岛啤酒/顺美）', cat='工业旅游开放日方法论',
      rel='r2', src='二手', src_cls='b2',
      url='https://www.toutiao.com/article/7650035668780843529',
      val='半月谈（北京日报）观察：曾经「谢绝参观」的工厂车间正成热门打卡地；盼盼食品 5G 智慧工厂七道工序零人工接触、2025 年接待超 3.5 万人次参观（同比+48%）；小米汽车工厂开放首日涌入 2.7 万人注册；福建民天酱油「日晒夜露」发酵体验+红曲酒封坛手作；顺美陶瓷配 30 余名专职讲解员、年逾十万人次参观；青岛啤酒博物馆以老厂房+沉浸式剧本杀+品酒拉满体验；工厂游已超越观光，成为连接公众与现代工业的桥梁。',
      how='把「工厂游」做成品牌体验引擎——用透明产线（玻璃隔断看全流程、屏幕实时跳动温湿度投料数据）制造「智造震撼」；把生产环节转化为体验动线（打酱油/封坛/手作陶瓷）；用工业遗产厚重度+互动趣味（剧本杀/品酒）制造情感共鸣；以「预约抽选+专职讲解」控制体验质量，让参观变自发传播。',
      note='② 工业旅游/企业开放日方法论（半月谈二手综论），企业领导以开放共生姿态，公众/亲子沉浸式感受制造实力，把参观流量转化为品牌口碑。'),
 dict(emoji='🚗', title='小鹏「AI 科技智造之旅」正式对外开放（工业旅游+CEO 亲临交付）', cat='车企工业旅游开放日',
      rel='r2', src='二手', src_cls='b2',
      url='https://www.jwview.com/jingwei/01-14/654164.shtml',
      val='小鹏广州智造基地「AI 科技智造之旅」正式对公众开放，定位「大湾区 AI 科技文旅新地标、多形态未来出行体验平台」；百余家媒体与 2026 款 P7+ 首批车主共同见证，公众可经小鹏 APP/公众号预约，亲临全球总部、广州及肇庆两大探索中心，探秘 AI 视觉质检、智慧物流、一体化大压铸等智能制造前沿；同期 P7+ 第十万台下线、首批车主交付仪式举行，董事长何小鹏亲临交付，以「上市即交付」让用户率先体验 AI 出行。',
      how='把车企工厂开放做成「科技文旅 IP」——用「物理 AI 从研发到制造到产品到服务」完整体系作沉浸主线；以 APP/公众号预约降低参与门槛；借新车下线+首批车主交付的高光节点，让 CEO 亲临交付把开放日变成用户共创现场；用「亲眼所见亲身所感」化解公众对智造的黑箱感。',
      note='② 车企工业旅游开放日（中新经纬二手），企业创始人/CEO 以用户体验共创者姿态，车主/媒体/公众深度探秘智造，把工厂开放变品牌信任场景。'),
 dict(emoji='🌊', title='上海宝山区水务局 2026「政府开放月」（滨江水务新图景·政民面对面）', cat='政府开放月/水务开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://xxgk.shbsq.gov.cn/article.html?infoid=cb478f07-3372-4933-9c3d-276e4379bc6d',
      val='宝山区水务局 2026「政府开放月」以「绿色生态·宜居新城——走进十五五滨江水务新图景」为主题，主场落吴淞炮台湾湿地森林公园，串起滨江生态修复示范段与邮轮旅游度假区滨水公共空间；活动含开幕仪式、滨江水务实地参观、「政民面对面」座谈交流会，集中展示水环境治理与幸福河湖建设成效、解读十五五水务绿色规划；现场报名限 60 人，推动水务工作从「单向发布」向「双向互动」转型。',
      how='把「政府开放月」做成滨水生态的体验式政务公开——以湿地森林公园+滨江修复段为实地参观动线，把规划蓝图变可走可看的空间；用「政民面对面」座谈把水务决策从单向发布转为双向互动；限额实名报名保证沟通质量；紧扣十五五节点让市民共绘生态新城共识。',
      note='② 政府开放月/水务开放日（上海宝山区政府官网一手），水务部门领导以生态共建者姿态，市民代表实地感受水治理成效、参与十五五水务规划对话。'),
 dict(emoji='🌐', title='可持续市场倡议（SMI）2026 中国论坛·全球 CEO 北京闭门可持续转型', cat='高管间闭门开放日',
      rel='r3', src='一手', src_cls='b1',
      url='https://www.sustainable-markets.org/news/the-sustainable-markets-initiative-convenes-global-ceos-in-beijing-for-flagship-forum-on-sustainable-transition',
      val='可持续市场倡议（SMI，查尔斯国王发起）2026 中国论坛 6.21-25 在北京举办，汇聚全球领先企业 CEO 与中国顶尖 CEO 及政府高层，通过圆桌对话、双边会谈、实地考察（探访北京商业图景与中国企业绿色实践）探讨可持续转型；议题聚焦 AI、健康、碳捕集、海洋渔业等战略优先事项；继首届后二度在华集结全球与中国 CEO 直接协作，搭建 CEO 级对话与行动平台，推动可持续创新与全球合作。',
      how='把「高管闭门开放日」做成 CEO 级战略对话场——以圆桌+双边会谈+实地考察组合，让全球与中国 CEO 及政府高层就可持续转型直接协作；用「共建双赢伙伴关系」替代单向宣讲；借国际供应链博览会同期联动放大产业落地；以闭门高阶对话凝聚跨国产学政共识，规避幼稚互动、纯商务切入。',
      note='③ 高管间闭门开放日（SMI 官网一手），全球与中国企业 CEO 及政府高层以专业/共同目标（可持续转型）切入，闭门圆桌+实地考察促跨国产学政协作，忌幼稚游戏、纯资本/IR 叙事。'),
]

def card_html(c):
    url_disp = c['url'].replace('https://','').replace('http://','')
    rel_text = '上下级' if c['rel']=='r2' else '高管间'
    return (f'    <div class="hl">\n'
            f'      <div class="top"><span class="emoji">{c["emoji"]}</span><h3>{c["title"]}</h3>'
            f'<span class="cat">{c["cat"]}</span><span class="badge {c["rel"]}">{rel_text}</span>'
            f'<span class="badge {c["src_cls"]}">{c["src"]}</span></div>\n'
            f'      <p class="val">{c["val"]}</p>\n'
            f'      <details class="exec"><summary>怎么做</summary><div class="inner">{c["how"]}</div></details>\n'
            f'      <div class="src">🔗 <a href="{c["url"]}" target="_blank">{url_disp}</a></div>\n'
            f'      <div class="note">适用：{c["note"]}</div>\n'
            f'    </div>')

cards2 = [c for c in cards if c['rel']=='r2']
cards3 = [c for c in cards if c['rel']=='r3']
n2, n3 = len(cards2), len(cards3)
assert n2+n3 == len(cards), (n2,n3,len(cards))
print(f'cards total={len(cards)} | ②={n2} ③={n3}')

html = open(HTML, encoding='utf-8').read()

# ---- dynamic current counts ----
cur2 = html.count('badge r2">上下级<')
cur3 = html.count('badge r3">高管间<')
print(f'current wall: ②={cur2} ③={cur3} (hl divs={html.count(chr(34)+"hl"+chr(34))})')
assert cur2 == 167, cur2
assert cur3 == 19, cur3

# ---- inject ② cards at end of sec2 grid (before sec3 marker) ----
marker = '  <div class="sec sec3">'
idx = html.find(marker)
assert idx != -1, 'sec3 marker not found'
new2_blocks = '\n'.join(card_html(c) for c in cards2)
html = html[:idx] + new2_blocks + '\n' + html[idx:]

# ---- inject ③ card at top of sec3 grid ----
# find first <div class="hl"> after sec3 header
j = html.find('<div class="sec sec3">')
k = html.find('<div class="hl">', j)
assert k != -1, 'no hl in sec3'
new3_blocks = '\n'.join(card_html(c) for c in cards3)
html = html[:k] + new3_blocks + '\n' + html[k:]

# ---- update sec2 / sec3 tag counts ----
m2 = re.search(r'(<div class="sec sec2">.*?<span class="tag">)(\d+)( 卡</span>)', html, re.S)
assert m2, 'sec2 tag not found'
html = html[:m2.start()] + m2.group(1) + str(cur2+n2) + m2.group(3) + html[m2.end():]
m3 = re.search(r'(<div class="sec sec3">.*?<span class="tag">)(\d+)( 卡</span>)', html, re.S)
assert m3, 'sec3 tag not found'
html = html[:m3.start()] + m3.group(1) + str(cur3+n3) + m3.group(3) + html[m3.end():]

# ---- hero append r24 segment ----
seg = ('｜ 二十四轮补采 2026-08-23(+6，国企开放日城市级/企业公众开放日/工厂游方法论/'
       '车企工业旅游/政府开放月水务/高管间闭门可持续转型·5②1③)')
assert '</div>\n  <div class="sec sec2">' in html
html = html.replace('</div>\n  <div class="sec sec2">', seg + '</div>\n  <div class="sec sec2">', 1)

open(HTML, 'w', encoding='utf-8').write(html)
print(f'OK wall updated: ②={cur2+n2} ③={cur3+n3} (hl divs now {html.count(chr(34)+"hl"+chr(34))}), footer={html.count("本页由 yitong 沉淀整理")}')

# ============ increment page (openday-20260823.html) ============
def grid(sec_cls, sec_title, sec_tag, cs):
    if not cs: return ''
    body = '\n'.join(card_html(c) for c in cs)
    return (f'  <div class="sec {sec_cls}">\n'
            f'    <h2>{sec_title}</h2>\n'
            f'    <span class="tag">{len(cs)} 卡</span>\n'
            f'  </div>\n  <div class="grid">\n{body}\n  </div>\n')

relbar = ('      <span>② 领导↔员工（上下级）</span>\n'
          '      <span>③ 领导↔领导（高管间）</span>')
inc_html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Open Day 开放日 · 第24轮补采（独立页）</title>
<style>
:root{{--bg:#f4f6fb; --card:#ffffff; --ink:#1f2430; --sub:#5b6478; --accent:#6c5ce7; --accent2:#00b8d9; --chip:#eef0ff;}}
*{{box-sizing:border-box;margin:0;padding:0;}}
body{{font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;background:linear-gradient(135deg,#eef1ff 0%,#e6f7ff 100%);color:var(--ink);padding:28px 18px;line-height:1.6;}}
.wrap{{max-width:1080px;margin:0 auto;}}
.hero{{background:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);border-radius:22px;padding:30px 32px;color:#fff;box-shadow:0 14px 40px rgba(108,92,231,.25);margin-bottom:22px;}}
.hero h1{{font-size:26px;font-weight:800;letter-spacing:1px;margin-bottom:8px;}}
.hero p{{font-size:14px;opacity:.95;}}
.relbar{{display:flex;gap:10px;flex-wrap:wrap;margin-top:14px;}}
.relbar span{{background:rgba(255,255,255,.2);border-radius:20px;padding:5px 14px;font-size:13px;font-weight:600;}}
.back{{display:inline-block;margin:0 0 14px;font-size:13px;color:var(--accent2);text-decoration:none;font-weight:600;}}
.sec{{margin:30px 0 12px;display:flex;align-items:center;gap:10px;}}
.sec h2{{font-size:19px;font-weight:800;}}
.sec .tag{{font-size:12px;padding:4px 12px;border-radius:12px;font-weight:700;}}
.sec3 .tag{{background:#f3e8ff;color:#7b2cbf;}} .sec3 h2{{color:#7b2cbf;}}
.sec2 .tag{{background:#fff3e0;color:#c0651a;}} .sec2 h2{{color:#c0651a;}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;}}
.hl{{background:var(--card);border-radius:18px;padding:18px 18px 16px;border-top:4px solid var(--accent);box-shadow:0 10px 32px rgba(108,92,231,.10);display:flex;flex-direction:column;gap:9px;}}
.top{{display:flex;align-items:center;gap:8px;flex-wrap:wrap;}}
.emoji{{font-size:22px;}}
.hl h3{{font-size:16px;font-weight:700;flex:1;min-width:120px;}}
.cat{{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:600;background:var(--chip);color:var(--accent);}}
.badge{{border-radius:14px;padding:3px 10px;font-size:12px;font-weight:700;}}
.b2{{background:#fff1e6;color:#c0651a;}}
.b1{{background:#e6f9ed;color:#1a9e5a;}}
.r1{{background:#eaf2ff;color:#2b6cb0;}}
.r2{{background:#fff3e0;color:#c0651a;}}
.r3{{background:#f3e8ff;color:#7b2cbf;}}
.val{{font-size:13.5px;color:var(--sub);}}
.exec{{margin-top:2px;border-top:1px dashed #e2e8f0;padding-top:8px;}}
.exec summary{{cursor:pointer;font-size:13px;font-weight:600;color:var(--accent);}}
.exec .inner{{font-size:13px;color:var(--sub);margin-top:6px;padding-left:4px;}}
.src{{font-size:12px;word-break:break-all;}}
.src a{{color:var(--accent2);text-decoration:none;}}
.note{{font-size:12px;color:#94a3b8;border-left:3px solid #e2e8f0;padding-left:8px;}}
footer{{text-align:center;padding:24px;color:#94a3b8;font-size:13px;border-top:1px solid #e2e8f0;margin-top:40px;}}
</style>
</head>
<body>
<div class="wrap">
  <div class="hero">
    <h1>🚪 Open Day 开放日 · 第24轮补采（独立页）</h1>
    <p>采集于 2026-08-23 ｜ 本轮新增 {len(cards)} 卡（②上下级 {n2} · ③高管间 {n3}）｜ 六维评估 ｜ 一手/二手标注 ｜ 受众关系分层（仅②③，剔除①）｜ 累计总索引见 <a href="../openday.html" style="color:#fff;text-decoration:underline;">openday.html</a></p>
    <div class="relbar">
{relbar}
    </div>
  </div>
{grid('sec2','② 领导↔员工（上下级，supervisor）',f'{n2} 卡',cards2)}
{grid('sec3','③ 领导↔领导（高管间 · exec）',f'{n3} 卡',cards3)}
</div>
<footer style="text-align:center;padding:24px;color:#94a3b8;font-size:13px;border-top:1px solid #e2e8f0;margin-top:40px;">📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>
</body>
</html>
'''
open(INC, 'w', encoding='utf-8').write(inc_html)
print(f'OK increment page: {INC} ({os.path.getsize(INC)}B)')

# ============ index.json ============
idx_data = json.load(open(IDX, encoding='utf-8'))
before = len(idx_data)
for c in cards:
    idx_data.append({
        'title': c['title'],
        'normKey': c['title'],
        'url': c['url'],
        'sourceType': 'primary' if c['src']=='一手' else 'secondary',
        'relation': 'supervisor' if c['rel']=='r2' else 'exec',
        'summary': c['val'][:120],
        'topic': 'openday',
    })
json.dump(idx_data, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'OK index.json {before} -> {len(idx_data)} (+{len(cards)})')

# ============ .rows_cache.json ============
cache = json.load(open(CACHE, encoding='utf-8'))
for c in cards:
    cache.append([c['title'], c['src'], '②上下级' if c['rel']=='r2' else '③高管间', c['val']])
json.dump(cache, open(CACHE, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'OK rows_cache.json {len(cache)-len(cards)} -> {len(cache)}')
