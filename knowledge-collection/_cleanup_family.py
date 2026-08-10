# -*- coding: utf-8 -*-
import re, json

KC = r'c:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection'
OBS = r'C:/Users/v_yitcai/Documents/Obsidian/知识采集库'

# 22 张家庭日/家属开放日向（HTML h3 精确文本）
REMOVE = [
 "山东公司「粽情端午 乐伴童心 家企共建」员工家庭日",
 "中国化学七化建首届「员工家属开放日」",
 "博众精工第五届家庭开放日（家企同心盛夏计划）",
 "企业家庭日实战攻略·三阶段体验（ESG/Open House）",
 "员工家庭日策划（亲子运动会/DIY）",
 "办公室家庭日攻略（捞金鱼/套圈）",
 "企业家庭日趣味活动（运动会/亲子）",
 "华丰科技四期「情融华丰·家倍温暖」家属开放日",
 "景嘉微2025「同心同行·乐享嘉时光」家庭开放日",
 "安科生物「安科嘉年华·秋日奇遇记」家属开放日",
 "中国电科二十七所「同心筑梦 一路有你」家属开放日",
 "东方电气「智造零距离·能源科普行」企业开放日",
 "江铃汽车「暑期家庭行」全民开放日（智造+研学）",
 "新升公司光电事业部「同心同行家企共融」家庭开放日",
 "凯格精机员工家庭开放日（廿年同行 家企同心）",
 '中船集团家属开放日：邮轮登船+亲子互动，把"小家"连"大家"',
 '中国一汽第六届"红旗荟"员工家属开放日：4 分场地·品牌温度',
 "中建四局家属开放日暨廉洁文化进家庭：VR安全+家庭助廉",
 "中国一汽2026年职工家属开放日（总部·1+7会场）",
 "中车兰州机车「红色引擎 智造未来」职工家属开放日",
 "华能营口电厂「三十华诞」国企开放日（150+职工家属）",
 "国能孟津热电2026企业开放日暨环保开放日（企民+家企双场）",
]

def is_remove(title):
    for r in REMOVE:
        if r in title or title in r:
            return True
    return False

# ---------- HTML ----------
html = open(f'{KC}/openday/openday.html', encoding='utf-8').read()
cards = re.findall(r'<div class="hl">[\s\S]*?\n    </div>\n', html)
removed = 0
for c in cards:
    h3 = re.search(r'<h3>(.*?)</h3>', c)
    if h3 and is_remove(h3.group(1)):
        html = html.replace(c, '', 1)
        removed += 1
html = html.replace('<span class="tag">32 卡</span>', '<span class="tag">10 卡</span>')
html = html.replace('尊重、不隐私暴露、建信任不越界；公司 hosting 员工家属、领导致辞+员工带队的开放日 / 客户开放日（领导以伙伴姿态）',
                    '尊重、不隐私暴露、建信任不越界；客户/媒体/品牌/公众开放日，领导致辞+员工带队的参观路线（领导以伙伴姿态）')
html = html.replace('六轮补采 2026-08-10(+11)</p>', '六轮补采 2026-08-10(+11)｜ 七轮清洗 2026-08-10(-22，移除家庭日/家属开放日向)</p>')
open(f'{KC}/openday/openday.html', 'w', encoding='utf-8').write(html)
print('HTML sec2 removed', removed, '| kept rebuilt')

# ---------- index.json ----------
data = json.load(open(f'{KC}/index.json', encoding='utf-8'))
before = len(data)
data2 = [e for e in data if not is_remove(e.get('title', ''))]
json.dump(data2, open(f'{KC}/index.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('index', before, '->', len(data2), '| removed', before - len(data2))

# ---------- Obsidian md ----------
def drop_rows(path):
    lines = open(path, encoding='utf-8').read().split('\n')
    out, d = [], 0
    for ln in lines:
        if ln.strip().startswith('|') and '（openday.html）' in ln:
            t = ln.split('（openday.html）')[0].lstrip('| ').strip()
            if is_remove(t):
                d += 1
                continue
        out.append(ln)
    return '\n'.join(out), d

# OpenDay 汇总
p = f'{OBS}/素材/openday/OpenDay-开放日-知识卡汇总.md'
txt, d1 = drop_rows(p)
txt = txt.replace('（共 57 张）', '（共 35 张）')
txt = txt.replace('新乡化纤投资者开放日公告）。', '新乡化纤投资者开放日公告）。｜ 七轮清洗 2026-08-10(-22，移除家庭日/家属开放日向)')
new_note = ('卡片墙 HTML 承载（未逐卡建 md）：`knowledge-collection/openday/openday.html`。**35 卡**，已剔除平级/朋友向（①）'
 '与家庭日/家属开放日向（用户 2026-08-10 指示），仅保留 ②上下级 / ③高管间；一手 13（甘李官方回顾/证监局范式/公告范式/四川局/常山制度 '
 '+ 和元生物官网 + 中航高科/金隅/帝王官网 + 盘龙药业官网升级 + 科环龙源/中国铁塔央企官网 + 新乡化纤公告）+ 二手 22。'
 '按「受众关系」分层：②上下级(客户/媒体/品牌/公众开放日，领导致辞+员工带队参观路线) 10 卡 / '
 '③高管间(投资者/政府/媒体/公众开放日，一手源与制度层为主) 25 卡。'
 '五轮补采新增高管间投资者开放日范式（江西证监局辖区集体接待日一手 / 中远海运资本市场日 9家45场 / Q4 虚拟投资者日指南 / Euronext 虚拟 CMD 操作法）。'
 '六轮补采新增品牌/媒体/国企开放日（科环龙源技术 / 中国铁塔 / 口子窖探厂 / 中国联通内蒙古 / 南航吉林）及高管间投资者开放日范式（纳微科技百余家机构实地参访 / 新乡化纤投资者开放日公告）。'
 '七轮清洗 2026-08-10(-22)：移除全部家属开放日/家庭日卡（含六轮新增的一汽2026/中车兰州/华能营口/国能孟津，及前几轮山东/七化建/博众/华丰/景嘉微/安科/二十七所/东方电气/江铃/新升/凯格/中船/一汽第六届/中建四局等）。')
lines = txt.split('\n')
for i, ln in enumerate(lines):
    if ln.startswith('卡片墙 HTML 承载（未逐卡建 md）：`knowledge-collection/openday/openday.html`。**'):
        lines[i] = new_note
        break
open(p, 'w', encoding='utf-8').write('\n'.join(lines))
print('OpenDay md dropped rows', d1)

# 00 索引
p0 = f'{OBS}/00-知识采集索引.md'
txt0, d0 = drop_rows(p0)
new_bq = ('卡片墙 HTML 承载（未逐卡建 md）：`knowledge-collection/openday/openday.html'
 '（[线上卡片墙·GitHub Pages](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday.html)）`。'
 '**35 卡**，已剔除平级/朋友向（①）与家庭日/家属开放日向（用户 2026-08-10 指示），仅保留 ②上下级 / ③高管间；'
 '一手 13（甘李官方回顾/证监局范式/公告范式/四川局/常山制度 + 和元生物官网 + 中航高科/金隅/帝王官网 + 盘龙药业官网升级 + 科环龙源/中国铁塔央企官网 + 新乡化纤公告）+ 二手 22。'
 '按「受众关系」分层：②上下级(客户/媒体/品牌/公众开放日，领导致辞+员工带队参观路线) 10 卡 / '
 '③高管间(投资者/政府/媒体/公众开放日，一手源与制度层为主) 25 卡。'
 '六轮补采新增品牌/媒体/国企开放日（科环龙源技术 / 中国铁塔 / 口子窖探厂 / 中国联通内蒙古 / 南航吉林）及高管间投资者开放日范式（纳微科技百余家机构实地参访 / 新乡化纤投资者开放日公告）。'
 '七轮清洗 2026-08-10(-22)：移除全部家属开放日/家庭日卡。')
lines0 = txt0.split('\n')
for i, ln in enumerate(lines0):
    if '**57 卡**' in ln and 'openday' in ln:
        lines0[i] = new_bq
        break
txt0 = '\n'.join(lines0)
txt0 = txt0.replace('2026-08-10 六轮补采 +11）', '2026-08-10 六轮补采 +11；2026-08-10 七轮清洗 -22 家庭日）')
open(p0, 'w', encoding='utf-8').write(txt0)
print('00 index md dropped rows', d0)
print('DONE')
