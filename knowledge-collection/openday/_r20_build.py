# -*- coding: utf-8 -*-
# Open Day 二十轮补采（r20, 2026-08-20）+7 卡，全②上下级
# 主题：城市生命线与民生安全公众开放日（垃圾焚烧发电/再生水厂/燃气安全/血站/海事局/规划展览馆/排水品牌系列）
import re, os, json

BASE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(BASE, 'openday.html')
TMP  = os.path.join(BASE, '.run_newcards.tmp.html')
CACHE= os.path.join(BASE, '.rows_cache.json')
IDX  = os.path.join(os.path.dirname(BASE), 'index.json')

html = open(HTML, encoding='utf-8').read()

cards = [
 dict(emoji='♻️', title='垃圾焚烧发电「从闲人免进到城市客厅」开放日', cat='环保设施开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://big5.mee.gov.cn/gate/big5/www.mee.gov.cn/xxgk2018/xxgk/xxgk15/201908/t20190814_728909.html',
      val='生态环境部「美丽中国先锋榜」常州垃圾焚烧发电项目：建设初期即预留公众观摩基础设施，设参观走廊+多媒体教室+沙盘+中英文解说牌；每月第一个周末设为公众开放日，支持预约现场参观监督；组织「跟着垃圾去旅行」环保科普实践，针对学生/政府/专家设计不同接待方案；2017年评为江苏省工业旅游示范点，把工厂变特色环境教育基地（花园式工厂+公众服务中心+环保纪念品）。',
      how='设计阶段就预埋公众参观通道（长廊+玻璃窗看核心设备+中控室大屏）；把开放日固定为月度机制（每月首个周末）形成公众预期；针对不同群体定制接待方案；用「工业旅游+环保纪念品」提升体验与传播；进社区进校园做延伸科普。',
      note='② 环保设施公众开放日，生态环境部门/企业以透明科普姿态，市民/学生监督并了解垃圾「变废为宝」，化解邻避疑虑。'),
 dict(emoji='💧', title='再生水厂「地下治污\u00b7地上造绿」公众开放日', cat='环保设施开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.neijiang.gov.cn/njs/c134045/202606/6d0022b2405c43c48f35ebdfc37b293c.shtml',
      val='内江市政府：谢家河再生水厂「隐形」绿色基础设施，地埋式设计把噪音异味锁住、把地面空间还给城市；市民/师生深入地下生物反应池+深床滤池，看污水变清流；中央集控室实时调控数公里外乡镇污水站；出水达地表水准Ⅳ类补给谢家河；工作人员称此为「把邻避效应转化为邻利设施」的实践。',
      how='用全地埋式设计消除邻避（噪音异味锁地下、地面做海绵公园）；用「城市肾脏」比喻+实时数据大屏把治污变可感；出水口前后对比直观震撼；把开放日变成「邻避转邻利」的沟通范例。',
      note='② 政府环保设施公众开放日，住建/生态环境部门+企业以透明沟通姿态，市民/学生探秘再生水「地下治污地上造绿」。'),
 dict(emoji='🔥', title='燃气安全「政府开放日」（住建局+燃气企业）', cat='燃气安全开放日',
      rel='r2', src='一手', src_cls='b1',
      url='http://www.ruijin.gov.cn/rjsxxgk/rjin80925/202510/b12588572f4f42839db4305da40b3901.shtml',
      val='瑞金市住建局联合深燃公司办「燃气安全政府开放日」：观看企业宣传片+燃气管道安全宣传片（真实案例警示）；「三件套」安全装置参观+实操培训（燃气报警器等）；参观经开区场站了解布局/储运/安全监控/应急机制；市民座谈政企民现场答疑。搭建「政府引导、企业负责、市民参与」沟通桥梁。',
      how='以「政府开放日」为载体把企业开放日与政民互动合并；用真实事故案例宣传片做警示开场；「三件套」装置实操培训让市民掌握应急技能；场站参观+座谈答疑形成「听意见-现场答」闭环。',
      note='② 政府+企业联合公众开放日，住建部门领导+企业以安全责任姿态，市民代表/人大代表/政协委员参与燃气安全共治。'),
 dict(emoji='🩸', title='血站/血液中心「探秘一袋热血」科普开放日', cat='卫健科普开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://csbt.org.cn/plus/view.php?aid=135865',
      val='中国输血协会：广州血液中心科普开放日（世界献血者日/科技活动周），市民化身「血液科学探索官」零距离探秘采血-检测-储存-发放全流程，破除献血误区；现场出现母女同行科普后暖心献血、准爸爸献血压守护母婴等公益瞬间；沈阳中心血站同步办社会公众开放日，透明化展示采供血全貌+站长面对面答疑。',
      how='把「一袋血的旅程」做成可参观动线（采血大厅→供血科→成分科→检验科→科普馆游戏识血）；用「破除误区+现场献血」把科普转公益行动；站长/专家面对面答疑建立信任；亲子/准爸妈场景化传播让奉献「言传身教」。',
      note='② 卫健科普公众开放日，血液中心领导/医护以科学透明姿态，市民/学生/亲子探秘血液安全与无偿献血公益。'),
 dict(emoji='⚓', title='海事局「中国航海日」公众开放日（VTS交管+海巡船艇）', cat='海事/航海开放日',
      rel='r2', src='一手', src_cls='b1',
      url='https://www.ln.msa.gov.cn/c/2026-07-13/670060.shtml',
      val='辽宁海事局（营口/大连/常州/锦州）：中国航海日系列活动——VTS交管政务开放日邀请市民/媒体参观海上安全联管中心，演示船舶动态监测/智能通航调度/远程巡航；「海巡0301/15009」轮敞开舱门当流动科普课堂，海事执法人员讲航标原理/船舶定位/执法装备，指导救生衣穿戴与航海绳结；青少年研学登台子山灯塔学守塔精神。',
      how='把「智慧交管平台」当稀缺开放钩子（实时看百艘船动态）；海巡船艇开放+执法人员化身讲解员把执法装备变科普；「海事微课堂」实操救生衣/绳结增强参与；分群体（市民/青少年/企业）设计活动，航海日品牌化连办。',
      note='② 海事执法公众开放日，海事局领导/执法人员以航海文化传播+水上安全科普姿态，市民/学生/航运企业零距离感受「海上执法力量」。'),
 dict(emoji='🏙️', title='城市规划展览馆「政府开放日」（城市会客厅·规划连心桥）', cat='规划展览馆开放日',
      rel='r2', src='一手', src_cls='b1',
      url='http://www.rushan.gov.cn/art/2025/8/1/art_77646_5716006.html',
      val='乳山市自然资源局「政府开放日」：邀社会群众观城乡规划展览馆，专业讲解员带看城市概况/历史溯源/特色文化/建设成就/交通变化/道德模范等板块；深圳宝安区在城市规划展览馆办政府开放日，50米柔性超长屏数字画卷+4米空中球体LED+大型沙盘+UE5沉浸式体验区，市民围沙盘提问、工作人员一一解答。',
      how='把规划成果展厅当「政府开放日」主场，用沙盘+数字投影+沉浸式体验让规划「看得见摸得着」；专业讲解员深度解说+市民现场提问形成互动；定位展馆为「永不落幕的城市会客厅与规划连心桥」，把政务公开变公众参与。',
      note='② 政府规划公开开放日，自然资源部门领导以阳光规划姿态，市民代表沉浸式了解城市发展脉络、增强认同感与参与度。'),
 dict(emoji='🚰', title='「万名市民看排水」品牌系列开放日（地上公园地下工厂）', cat='排水/水务开放日',
      rel='r2', src='二手', src_cls='b2',
      url='https://new.qq.com/rain/a/20260702A06Y4000?refer=cp_1009',
      val='上海排水行业「万名市民看排水」系列品牌活动：南翔污水处理厂「地上是公园、地下是工厂」生态治理范例，市民分批次走安全观摩通道看污水预处理-生化-深度净化全流程，现场对比进出水；讲解员讲「占地仅传统1/3、出水达地表Ⅳ类、再生水利用率100%」硬核指标；嘉定水环境科普馆趣味答题+互动赢礼品，品牌化连办多站。',
      how='用「地上公园地下工厂」反差制造打卡钩子；系列化品牌活动（「万名市民看排水」）持续走进排水一线，诚邀市民报名；进出水对比+硬核指标把治污科技变可感；科普馆趣味答题「寓教于乐」让市民刷新对污水厂的认知。',
      note='② 城市水务公众开放日，排水行业领导/员工以开放透明姿态，市民（含亲子）探秘「污水变活水、厂区变公园」治理成果。'),
]

def card_html(c):
    url_disp = c['url'].replace('https://','').replace('http://','')
    return f'''    <div class="hl">
      <div class="top"><span class="emoji">{c['emoji']}</span><h3>{c['title']}</h3><span class="cat">{c['cat']}</span><span class="badge {c['rel']}">上下级</span><span class="badge {c['src_cls']}">{c['src']}</span></div>
      <p class="val">{c['val']}</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">{c['how']}</div></details>
      <div class="src">🔗 <a href="{c['url']}" target="_blank">{url_disp}</a></div>
      <div class="note">适用：{c['note']}</div>
    </div>'''

new_blocks = '\n'.join(card_html(c) for c in cards)
n = len(cards)

# write temp file for run page
open(TMP, 'w', encoding='utf-8').write(new_blocks + '\n')

# 1) insert before sec3 header
marker = '  <div class="sec sec3">'
idx = html.find(marker)
assert idx != -1, 'sec3 marker not found'
html = html[:idx] + new_blocks + '\n' + html[idx:]

# 2) update sec2 tag count (144 -> 151)
html = re.sub(r'(<div class="sec sec2">.*?<span class="tag">)\d+ 卡(</span>)',
              lambda m: m.group(1) + str(144 + n) + ' 卡' + m.group(2),
              html, count=1, flags=re.S)

# 3) update hero p: append r20 segment
seg = '\uff5c 二十轮补采 2026-08-20(+7，垃圾焚烧发电城市客厅/再生水厂地下治污/燃气安全政府开放日/血站科普开放日/海事局航海日/城市规划展览馆政府开放日/万名市民看排水品牌系列\uff65全\uff12上下级)'
html = html.replace('</div>\n  <div class="sec sec2">',
                    seg + '</div>\n  <div class="sec sec2">', 1)

open(HTML, 'w', encoding='utf-8').write(html)
print(f'OK inserted {n} cards | sec2 now {144+n} | tmp={TMP}')

# ---- index.json 追加 7 条 openday 条目 ----
idx_data = json.load(open(IDX, encoding='utf-8'))
assert isinstance(idx_data, list)
before = len(idx_data)
for c in cards:
    idx_data.append({
        'title': c['title'],
        'normKey': c['title'],
        'url': c['url'],
        'sourceType': 'primary' if c['src'] == '一手' else 'secondary',
        'relation': 'supervisor',
        'summary': c['val'][:120],
        'topic': 'openday',
    })
json.dump(idx_data, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'OK index.json {before} -> {len(idx_data)} (+{len(cards)})')

# ---- .rows_cache.json 追加 7 行 ----
cache = json.load(open(CACHE, encoding='utf-8'))
for c in cards:
    cache.append([c['title'], c['src'], '②上下级', c['val']])
json.dump(cache, open(CACHE, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'OK rows_cache.json {len(cache)-n} -> {len(cache)}')
