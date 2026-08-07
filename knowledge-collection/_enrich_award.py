# -*- coding: utf-8 -*-
import re, json, os

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "award", "award.html")
JSON = os.path.join(BASE, "index.json")

def slug(t):
    out = []
    for ch in t.lower():
        if ch.isalnum() or '\u4e00' <= ch <= '\u9fff':
            out.append(ch)
        else:
            out.append('')
    return ''.join(out)

# (title, emoji, cat, relation_list, src, display, val, inner, note, sec)
# sec: '3' = 高管间(exec first grid), '2' = 上下级(supervisor grid)
cards = [
 dict(sec='3', title='颁奖词与领导致辞撰写框架', emoji='🎙️', cat='文案SOP',
      rel=['supervisor','exec'], src='https://m.renrendoc.com/paper/494018902.html',
      disp='m.renrendoc.com/paper/494018902.html',
      val='表彰大领导致辞"成果回顾(数据+案例)→感谢致敬(团队/伙伴/家属)→战略展望(行业趋势+企业行动)"三段式结构；颁奖词用"阐述奖项意义→细节化描述获奖者特质→邀请颁奖嘉宾"话术，把表彰与战略闭环、让荣誉具象化而非念名单。',
      inner='致辞时长控8-10min；颁奖词先讲奖项对应价值观(如"攻坚先锋奖"=突破创新)再点名特质；员工代表致辞5-8min重真实感；闭幕用"回顾+感谢+展望"把情感落点从个体升级到共同体。',
      note='适用：②+③ 领导致辞与颁奖词撰写，战略传递与价值共鸣。'),
 dict(sec='3', title='长期服务奖(工龄荣誉)体系设计', emoji='🏅', cat='荣誉体系',
      rel=['supervisor','exec'], src='https://www.gusto.com/resources/articles/hr/team-management/years-of-service-awards',
      disp='gusto.com/.../years-of-service-awards',
      val='长期服务奖(5/10/15/20年里程碑)是留任与忠诚的杠杆：提升 retention、engagement、loyalty、招聘吸引力与组织文化；可自动化执行；设计需清晰标准、可执行框架、部分环节平台化。',
      inner='设清晰里程碑门槛与对应象征奖(勋章/别针承载文化)；高层出席职业庆典=重视信号；评选标准能量化就量化；纪念录像/证书作文化提醒；集成社媒让个人与职业社区共贺。',
      note='适用：②+③ 长期主义荣誉体系，降低流失、沉淀组织知识。'),
 dict(sec='3', title='长期主义功勋荣誉体系案例(平安人寿)', emoji='🏛️', cat='战略案例',
      rel=['exec','supervisor'], src='https://m.chinanews.com/wap/detail/chs/zw/378987.shtml',
      disp='chinanews.com/.../378987.shtml',
      val='平安人寿发布"代理人功勋荣誉体系"：4大类7奖25子奖，设入围业务品质/继续率门槛并兼顾业绩与服务年限；含"长期忠诚"(10/15/20/25/30年)、"卓越贡献"、"责任担当"、"战略引领"四类，不以业绩为唯一标准，呼应监管专业化职业化导向。',
      inner='长期忠诚类按服务年限分级；卓越贡献类要求连续入围高峰会；战略引领类紧跟集团战略纳入不同渠道价值；兼顾社会价值与责任担当；以"长期主义"替代唯业绩论。',
      note='适用：③+② 战略级荣誉体系设计，长期价值>短期业绩。'),
 dict(sec='3', title='虚拟/混合颁奖典礼运营指南', emoji='💻', cat='远程运营',
      rel=['supervisor','exec'], src='https://www.hifives.in/a-guide-to-organizing-a-virtual-employee-awards-ceremony/',
      disp='hifives.in/.../virtual-employee-awards-ceremony',
      val='远程/混合团队颁奖全运营：领导力参与(高管演讲/颁奖/致谢)建信任；数字荣誉墙+社交feed公开庆祝；直播+预录故事混剪保制作质感；内部 microsite 集中日程/提名；实时投票/Q&A/抽奖防掉线；技术彩排+专属支持；会后录像/亮点延续影响；成本显著低于线下、ROI更优。',
      inner='选稳定可交互平台(Teams/Zoom/Webex或专用)；高管录制视频提前brief；预录人物故事+颁奖呈现混剪；奖项与价值观对齐；远程与混合员工平等可见；活动精简快节奏防疲劳；数字证书/e礼卡即时 gratification。',
      note='适用：②+③ 多城/远程/混合团队，强参与与平等可见。'),
 dict(sec='3', title='颁奖典礼预算基准与ROI框架', emoji='💰', cat='预算ROI',
      rel=['exec'], src='https://bwproductions.co.za/the-complete-guide-to-corporate-event-roi-how-9000-events-taught-us-what-works/',
      disp='bwproductions.co.za/.../corporate-event-roi',
      val='颁奖典礼行业基准：人均成本(含场地/餐饮/AV/制作)约 R900-1800，ROI 乘数 3.0-3.5x；活动ROI=(营收−成本)/成本×100%，无形价值用 cost-per-impression/lead转化/品牌声量代理；向CFO证明投入用"获客成本/留存影响/媒体等值"语言。',
      inner='设清晰 pre-event 目标对齐业务结果；最大ROI杠杆=会后30-90天 activation(内容/连接/动量的转化)；追踪 pre/post 基线(留存/参与/推荐)；颁奖典礼制作占预算25-35%是记忆点。',
      note='适用：③ 向财务/高管证明颁奖投入回报，预算与ROI框架。'),
 dict(sec='3', title='员工认可活动ROI与留存逻辑', emoji='📈', cat='效果衡量',
      rel=['supervisor','exec'], src='https://the-happy-manager.com/the-roi-of-gratitude-why-employee-appreciation-events-matter/',
      disp='the-happy-manager.com/the-roi-of-gratitude',
      val='认可活动商业回报：敬业度 top quartile 企业离职率低65%(Gallup)；HBR 追踪 peer-recognition 项目3个月生产率+12%；单员工替换成本=年薪50-200%；即便仅算留存节省，保守 ROI 也常>200%；活动摄影把瞬时聚会变持久雇主品牌资产。',
      inner='定义清晰目标(留高绩效/跨职能协作/服务里程碑)；让员工参与策划；量化成本与收益(离职率/任期/内推/敬业度)；会后 spotlight 画廊邮件/内刊/社媒延续；用留存节省算 ROI 向管理层证明。',
      note='适用：②+③ 用留存与生产率数据证明认可投入，争取预算。'),
 dict(sec='2', title='颁奖环节主持词话术设计', emoji='🎤', cat='主持话术',
      rel=['supervisor'], src='https://renrendoc.com/paper/503921332.html',
      disp='renrendoc.com/paper/503921332.html',
      val='颁奖环节主持词"赋予荣誉仪式感与价值感"话术框架：先阐述奖项意义(如"攻坚先锋奖"对应突破创新)→再用细节化语言描述获奖者特质→最后邀请颁奖嘉宾强化仪式感；让奖项"含金量"可视化而非念名单。',
      inner='表达要点=奖项意义+获奖者细节特质+邀请嘉宾；参考"年度攻坚先锋奖"话术把价值观具象化；闭幕主持用"回顾+感谢+展望"结构把情感从个体升级到共同体；主持词提前brief公司文化与敏感话题。',
      note='适用：② 颁奖环节主持词撰写，强化仪式感与价值传递。'),
 dict(sec='2', title='活动成效KPI设计(含内部凝聚指标)', emoji='📊', cat='成效评估',
      rel=['supervisor'], src='http://www.mocs.com.tw/news-detail/how-evaluate-activity-effectiveness.htm',
      disp='mocs.com.tw/news-detail/how-evaluate-activity-effectiveness.htm',
      val='活动成效评估KPI/ROI框架：每场设2-4个对准目的的可量化KPI；员工内部凝聚类指标=员工参与率(部门覆盖)、满意度调查、建议与回馈比率；ROI=(成果价值−总成本)/总成本×100%，无直接营收时可估社群触达/媒体PR值/名单价值等长期内部回报。',
      inner='KPI对准目的才有意义(品牌曝光/客户经营/员工凝聚各配不同指标)；员工活动用参与率+满意度+回馈数作辅助；活动后整理呈现成效累积为决策依据；避免"大家感觉还不错"式主观判断。',
      note='适用：② 颁奖/文化活动成效量化，KPI与ROI评估。'),
]

def card_html(c):
    rel_badges = ''.join(f'<span class="badge r2">上下级</span>' if r=='supervisor' else f'<span class="badge r3">高管间</span>' for r in c['rel'])
    rel_txt = ','.join(c['rel'])
    note_rel = '②+③' if len(c['rel'])>1 else ('②' if c['rel'][0]=='supervisor' else '③')
    return (
        '    <div class="hl">\n'
        f'      <div class="top"><span class="emoji">{c["emoji"]}</span><h3>{c["title"]}</h3>'
        f'<span class="cat">{c["cat"]}</span>{rel_badges}<span class="badge b2">二手</span></div>\n'
        f'      <p class="val">{c["val"]}</p>\n'
        '      <details class="exec"><summary>怎么做</summary>'
        f'<div class="inner">{c["inner"]}</div></details>\n'
        f'      <div class="src">🔗 <a href="{c["src"]}" target="_blank">{c["disp"]}</a></div>\n'
        f'      <div class="note">适用：{note_rel} {c["note"].split("：",1)[1] if "：" in c["note"] else c["note"]}</div>\n'
        '    </div>\n'
    )

html = open(HTML, encoding='utf-8').read()

# dedup check by URL
existing_urls = set(re.findall(r'href="(.*?)" target="_blank"', html))
for c in cards:
    assert c['src'] not in existing_urls, f"URL collision: {c['src']}"

# build grouped card html
sec3_new = ''.join(card_html(c) for c in cards if c['sec']=='3')
sec2_new = ''.join(card_html(c) for c in cards if c['sec']=='2')

# insert sec3 before the ② section comment
marker3 = '  </div>\n\n  <!-- ============ ② 上下级 ============ -->'
assert marker3 in html, "sec3 marker not found"
html = html.replace(marker3, '  ' + sec3_new + '\n  </div>\n\n  <!-- ============ ② 上下级 ============ -->', 1)

# insert sec2 before the grid-close div that precedes <footer> (robust to stray blank lines)
fi = html.rfind('<footer>')
di = html.rfind('  </div>', 0, fi)
assert di != -1, "sec2 grid-close not found"
html = html[:di] + '  ' + sec2_new + '\n' + html[di:]

# update tag counts
# sec3: after ③ 高管间 h2
html = html.replace(
    '    <h2>③ 领导↔领导（高管间 · exec）</h2>\n    <span class="tag">10 卡</span>',
    '    <h2>③ 领导↔领导（高管间 · exec）</h2>\n    <span class="tag">16 卡</span>', 1)
html = html.replace(
    '    <h2>② 领导↔员工（上下级 · supervisor）</h2>\n    <span class="tag">10 卡</span>',
    '    <h2>② 领导↔员工（上下级 · supervisor）</h2>\n    <span class="tag">12 卡</span>', 1)

# hero subtitle enrich note
html = html.replace(
    '二次补采 2026-08-07 ｜ 六维评估',
    '二次补采 2026-08-07 ｜ 三轮 enrich 2026-08-07(+8) ｜ 六维评估', 1)

open(HTML, 'w', encoding='utf-8').write(html)

# update index.json
d = json.load(open(JSON, encoding='utf-8'))
before = len(d)
for c in cards:
    d.append({
        'title': c['title'],
        'normKey': slug(c['title']),
        'url': c['src'],
        'sourceType': 'secondary',
        'relation': ','.join(c['rel']),
        'summary': c['val'][:120],
    })
after = len(d)
json.dump(d, open(JSON, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# verify
h2 = open(HTML, encoding='utf-8').read()
n_h3 = len(re.findall(r'<h3>', h2))
print('award.html <h3> count:', n_h3)
print('footer present:', '📌 本页由 yitong 沉淀整理' in h2)
print('index.json before/after:', before, '->', after, '(+%d)' % (after-before))
print('DONE')
