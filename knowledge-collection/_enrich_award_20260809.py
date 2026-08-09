# -*- coding: utf-8 -*-
import re, json, os
BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, "award", "award.html")
JSON = os.path.join(BASE, "index.json")
OUT_HTML = HTML
OUT_JSON = JSON

def slug(t):
    out = []
    for ch in t.lower():
        if ch.isalnum() or '\u4e00' <= ch <= '\u9fff':
            out.append(ch)
        else:
            out.append('')
    return ''.join(out)

# (sec, title, emoji, cat, rel, src, disp, val, inner, note)
# sec: '3' = 高管间 grid, '2' = 上下级 grid ; rel list of 'supervisor'/'exec'
cards = [
 dict(sec='2', title='颁奖典礼危机预案与控场话术SOP', emoji='🛡️', cat='危机预案',
   rel=['supervisor'],
   src='https://idea-plan.com/news_dtl-98',
   disp='idea-plan.com/news_dtl-98',
   val='企业颁奖典礼最常见的「出包」来自准备不足：舞台视听(音爆/麦无声/简报放不出)需活动前一周完整测试+当天总检；主持稿逐字稿/cue卡防临场卡词；最重要的是「Plan B 突发应对SOP」——代领人(主管代领+奖品后续送达)、影片故障(切主持口头简介/备用简报)、贵宾延迟(该奖项后移+更新cue卡)，事前与主持人/控场拟好SOP，让危机变无声解决。',
   inner='代领话术「由××主管代领，稍后奖品送达得主」；影片故障立即转主持口播或备用文件；贵宾迟到把其颁奖项后移并同步后场cue卡；名单一式两份交叉核对(拼音/全名)；5大扣分区=流程拖延/冷场/灯光错/名单错/忽略确认——企业正式场合出包会被记一年。',
   note='颁奖典礼现场危机预案与控场SOP，降低正式场合翻车风险。'),
 dict(sec='3', title='多元包容(D&I)奖项设计框架', emoji='🤝', cat='包容设计',
   rel=['exec','supervisor'],
   src='https://beingcounsellor.com/the-role-of-awards-in-supporting-diversity-and-inclusion-efforts',
   disp='beingcounsellor.com/.../diversity-and-inclusion-efforts',
   val='把 D&I 写进认可策略，奖项从「少数精英」变成「所有贡献都被看见」的信号：扩大评选标准(不只结果，也认协作/共情/共享成功等行为)、用同事提名+轮换评审panel+透明文档流程消除偏袒、提供多格式/多语言提名降低参与门槛、按个人偏好个性化认可(公开掌声/私下致谢/团队highlight)、公开获奖故事教育全员「包容长什么样」。研究显示包容奖项项目更能吸引留存多元人才。',
   inner='评审标准公开透明，避免只认「最外露/最外向」员工；peer nomination+轮换panel防favoritism；多语言/多格式提名覆盖一线与远程；把文化里程碑/无障碍需求纳入认可；领导层培训经理识别各类贡献并用包容语言；定期调研不同群体是否被看见并迭代。',
   note='多元包容导向的奖项设计框架，让认可覆盖所有群体、反无意识偏见。'),
 dict(sec='2', title='表彰大会内部传播与复盘闭环SOP', emoji='📣', cat='传播复盘',
   rel=['supervisor'],
   src='https://blog.ihr360.com/p/275104',
   disp='blog.ihr360.com/p/275104',
   val='表彰不止于现场——用「会前-会中-会后」闭环把荣誉变组织资产：会前预热视频(30-60s「今年一起完成了什么」)+内网征集「高光协作瞬间」+经理晨会带队观看讨论；会中HR讲解三步法(我们是谁→如何一起赢→下一步怎么参与)+现场投票上墙；会后拆条3-5条短视频二次分发内网/学习平台、复盘工作坊把案例拆成SOP模板、纳入新人Onboarding、7/30/90日脉搏调查比对行为指标。用数据闭环(观看完成率/eNPS/跨部门响应时长/知识库新增条目)证明价值。',
   inner='会前预热造期待、经理一分钟带看强化部门共鸣；会中互动投票即时上墙+跨部门握手合影巩固共同身份；会后拆条再传播延长影响、复盘工作坊沉淀SOP、新员工融入用真实案例；指标联合看「表彰数量+覆盖面/代表性」防偏；A/B部门对照看有无观看差异。',
   note='表彰大会前后传播与复盘闭环，把单次活动沉淀为可复用组织资产。'),
 dict(sec='3', title='高管层把员工家属请进表彰盛典', emoji='👨‍👩‍👧', cat='家属参与',
   rel=['exec'],
   src='https://www.jiushuo99.com/z/jiushuo/info/7047',
   disp='jiushuo99.com/.../info/7047',
   val='把「家属」请进正式表彰盛典，是高管层情感温度与人文关怀的高杠杆表达：古井贡酒秋酿大典专车接一线先进工作者父母坐贵宾席，党委书记/董事长及全体高管亲自接待、敬头酒致谢「为企业培养了优秀的孩子」，合影留念后参观厂区、礼赠护送回家，并定为每年常态。同样的「高管颁奖+家属在场」也见于汉拿集团家属日暨高考学子颁奖礼(高管着正装颁红包)。把家属纳入荣耀时刻，让「个人获奖」升级为「家庭与企业双向奔赴」。',
   inner='一线先进父母/家属坐贵宾席、高管亲自接待与致谢；颁奖环节让家属见证亲人荣耀(高管颁/合影)；活动后参观工作环境+礼赠护送，闭环关怀；定为年度常态IP而非一次性；对一线员工，家属认可比奖金更催忠诚。',
   note='高管层把员工家属纳入表彰盛典，用家庭认同放大荣誉与留任意愿。'),
 dict(sec='2', title='优秀员工携家属出席表彰+家属关爱', emoji='🎁', cat='家属关爱',
   rel=['supervisor'],
   src='https://www.xmgh.org/ghsc/ghdt/jcghdt/202603/t20260311_305906.htm',
   disp='xmgh.org/.../t20260311_305906.htm',
   val='工会/管理层把「表彰优秀员工」与「感恩家属」绑定：路达集团获评「年度最优秀」员工携家人参加开春大早会表彰大会，家属坐专属席位共见证荣耀；会后组织「最优秀员工家属厦门游」三天温情陪伴，生产主管与工会主席亲临晚宴向家属致谢「默默支持是奋斗最坚实后盾」。郑州太古则在厂庆颁奖现场连线获奖员工爱人、抽奖送配偶钻戒/手表，让「看见家人获奖」比自己拿奖更动人。家属参与把单向表彰变成「企业-员工-家庭」三方认同。',
   inner='表彰大会设家属专属席位、邀请共同见证；会后为优秀员工家属组织关爱游/晚宴，主管层当面致谢；颁奖/抽奖环节设计「连线爱人/送配偶礼」等温情桥段；把「感谢家属」写进主持词与领导寄语，强化三方双向奔赴。',
   note='优秀员工携家属出席表彰并配套家属关爱，把单向表彰升级为家庭认同。'),
]

# ---- dedup against existing index.json + award.html ----
idx = json.load(open(JSON, encoding='utf-8'))
existing_urls = set(e.get('url','') for e in idx)
html_text = open(HTML, encoding='utf-8').read()
existing_html_urls = set(re.findall(r'href="(.*?)" target="_blank"', html_text))
existing_html_titles = set(re.findall(r'<h3>(.*?)</h3>', html_text))

kept = []
skipped = []
for c in cards:
    reasons = []
    if c['src'] in existing_urls: reasons.append('index.json url')
    if c['src'] in existing_html_urls: reasons.append('award.html url')
    if c['title'] in existing_html_titles: reasons.append('award.html title')
    if reasons:
        skipped.append((c['title'], reasons))
    else:
        kept.append(c)

print('dedup: kept %d, skipped %d' % (len(kept), len(skipped)))
for t, r in skipped:
    print('  SKIP', t, '->', ', '.join(r))

# ---- build card html ----
def card_html(c):
    rel_badges = ''.join(f'<span class="badge r2">上下级</span>' if r=='supervisor' else f'<span class="badge r3">高管间</span>' for r in c['rel'])
    note_rel = '/'.join('②' if r=='supervisor' else '③' for r in c['rel'])
    return (
        '    <div class="hl">\n'
        f'      <div class="top"><span class="emoji">{c["emoji"]}</span><h3>{c["title"]}</h3>'
        f'<span class="cat">{c["cat"]}</span>{rel_badges}<span class="badge b2">二手</span></div>\n'
        f'      <p class="val">{c["val"]}</p>\n'
        '      <details class="exec"><summary>怎么做</summary>'
        f'<div class="inner">{c["inner"]}</div></details>\n'
        f'      <div class="src">🔗 <a href="{c["src"]}" target="_blank">{c["disp"]}</a></div>\n'
        f'      <div class="note">适用：{note_rel} {c["note"]}</div>\n'
        '    </div>\n'
    )

sec3_new = ''.join(card_html(c) for c in kept if c['sec']=='3')
sec2_new = ''.join(card_html(c) for c in kept if c['sec']=='2')

# insert sec3 before marker
marker3 = '  </div>\n\n  <!-- ============ ② 上下级 ============ -->'
assert marker3 in html_text, "sec3 marker not found"
html_text = html_text.replace(marker3, '  ' + sec3_new + '\n  </div>\n\n  <!-- ============ ② 上下级 ============ -->', 1)

# insert sec2 before <footer>
fi = html_text.rfind('<footer>')
di = html_text.rfind('  </div>', 0, fi)
assert di != -1, "sec2 grid-close not found"
html_text = html_text[:di] + '  ' + sec2_new + '\n' + html_text[di:]

# update tag counts
n3 = html_text.count('<span class="badge r3">高管间</span>')
n2 = html_text.count('<span class="badge r2">上下级</span>')
html_text = re.sub(r'(<h2>③ 领导↔领导（高管间 · exec）</h2>\n    <span class="tag">)\d+ 卡',
                   lambda m: m.group(1)+f'{n3} 卡', html_text, count=1)
html_text = re.sub(r'(<h2>② 领导↔员工（上下级 · supervisor）</h2>\n    <span class="tag">)\d+ 卡',
                   lambda m: m.group(1)+f'{n2} 卡', html_text, count=1)

# hero subtitle enrich
html_text = html_text.replace(
    '四轮 enrich 2026-08-08(+6) ｜',
    '四轮 enrich 2026-08-08(+6) ｜ 五轮 enrich 2026-08-09(+%d) ｜' % len(kept), 1)

open(OUT_HTML, 'w', encoding='utf-8').write(html_text)

# update index.json
before = len(idx)
for c in kept:
    idx.append({
        'title': c['title'],
        'normKey': slug(c['title']),
        'url': c['src'],
        'sourceType': 'secondary',
        'relation': ','.join(c['rel']),
        'summary': c['val'][:120],
    })
json.dump(idx, open(OUT_JSON, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
after = len(idx)

# verify
h2 = open(OUT_HTML, encoding='utf-8').read()
print('award.html <h3> count:', len(re.findall(r'<h3>', h2)))
print('r3 badges:', h2.count('<span class="badge r3">高管间</span>'), '| r2 badges:', h2.count('<span class="badge r2">上下级</span>'))
print('footer present:', '📌 本页由 yitong 沉淀整理' in h2)
print('index.json before/after:', before, '->', after, '(+%d)' % (after-before))
print('DONE')
