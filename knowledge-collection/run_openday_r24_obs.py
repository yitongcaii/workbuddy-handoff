# -*- coding: utf-8 -*-
# Open Day 二十四轮补采（r24, 2026-08-23）· Obsidian 知识采集库 落库
import os
OB_SUM = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\openday\OpenDay-开放日-知识卡汇总.md"
OB_IDX = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
GH = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/openday-20260823.html"

# (title, src, rel, one-liner)
rows = [
 ("北京市国资委 2026「首都国企开放日」（45 家国企 142 条线路·常态化开放）", "一手", "②上下级", "一企一特色·常态开放矩阵"),
 ("山东重工中国重汽 2026 合作伙伴大会「公众开放日」·可触摸的品牌温暖之旅", "一手", "②上下级", "可触摸品牌温度·亲子共创"),
 ("半月谈｜不再「谢绝参观」，「工厂游」拉满体验感（盼盼/小米/青岛啤酒/顺美）", "二手", "②上下级", "透明产线+体验动线造口碑"),
 ("小鹏「AI 科技智造之旅」正式对外开放（工业旅游+CEO 亲临交付）", "二手", "②上下级", "物理AI沉浸主线+CEO交付"),
 ("上海宝山区水务局 2026「政府开放月」（滨江水务新图景·政民面对面）", "一手", "②上下级", "滨水生态体验式政务公开"),
 ("可持续市场倡议（SMI）2026 中国论坛·全球 CEO 北京闭门可持续转型", "一手", "③高管间", "CEO级可持续转型对话场"),
]

# ---------- 汇总笔记 ----------
t = open(OB_SUM, encoding='utf-8').read()
assert '共 174 张' in t, 'summary count 174 not found'
t = t.replace('共 174 张', '共 180 张', 1)

new_rows = '\n'.join(f"| {tt}（openday.html） | 4 | {src} | {rel} | {one} |" for tt,src,rel,one in rows)
assert '\n\n## 卡片墙（HTML 交互版）' in t
t = t.replace('\n\n## 卡片墙（HTML 交互版）', '\n' + new_rows + '\n\n## 卡片墙（HTML 交互版）', 1)

# 当轮独立页链接（接在已有最大轮次链接后）
link_line = f"- 当轮独立页（第二十四轮）：{GH}"
if link_line not in t:
    # 插入到 第二十二轮 链接之后
    anchor = "- 当轮独立页（第二十二轮）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday"
    if anchor in t:
        # 找该行末尾
        idx = t.index(anchor)
        eol = t.find('\n', idx)
        t = t[:eol] + '\n' + link_line + t[eol:]
    else:
        # 兜底：插到 卡片墙 小节前
        t = t.replace('\n\n## 卡片墙（HTML 交互版）', '\n' + link_line + '\n\n## 卡片墙（HTML 交互版）', 1)

# 二十四轮叙事（追加到 适用&备注 末尾）
narr = ('\n二十四轮补采（2026-08-23）新增聚焦六大未覆盖子域（5 ②上下级 + 1 ③高管间，4 一手+2 二手）：'
        '「国企开放日（城市级）」（北京市国资委，45 家国企 142 条线路·集中+常态双轨开放，一企一特色矩阵）、'
        '「企业公众开放日」（山东重工中国重汽，员工家属+社会公众逾万·全景沉浸展+手作工坊+退休职工回流传承）、'
        '「工厂游方法论」（半月谈综论，盼盼/小米/青岛啤酒/顺美——透明产线+体验动线+工业遗产情感共鸣）、'
        '「车企工业旅游开放日」（小鹏 AI 科技智造之旅，物理AI沉浸主线+APP预约+CEO亲临交付）、'
        '「政府开放月/水务开放日」（上海宝山区水务局，滨水生态修复实地参观+政民面对面座谈，十五五水务规划双向互动）、'
        '「高管间闭门开放日」（SMI 中国论坛，全球与中国 CEO 及政府高层闭门圆桌+实地考察促可持续转型协作，忌幼稚游戏/纯IR叙事）。'
        '硬排除：投资者关系/证券监管/资本市场/财经媒体类开放日（命中资本市场/IR/证监局即跳过）。\n')
if '二十四轮补采（2026-08-23）' not in t:
    t = t.rstrip('\n') + narr
open(OB_SUM, 'w', encoding='utf-8').write(t)
print('OK summary note updated (180 卡, +6 rows, r24 link+narr)')

# ---------- 00 索引 ----------
lines = open(OB_IDX, encoding='utf-8').read().split('\n')
# 1) heading 追加 r24 段
for i, ln in enumerate(lines):
    if ln.startswith('## 主题：Open Day') and ln.rstrip().endswith('）'):
        seg = ('｜ 2026-08-23 二十四轮补采 +6（国企开放日城市级/企业公众开放日/工厂游方法论/'
               '车企工业旅游/政府开放月水务/高管间闭门可持续转型·5②1③）')
        if '二十四轮补采 +6' not in lines[i]:
            lines[i] = lines[i].rstrip('）') + seg
        break
# 2) 插入 6 行到 openday 表（在 📄 主题汇总笔记 行之前）
od_rows = [f"| {tt}（openday.html） | 4 | {src} | {rel} | 二十四轮新增 |" for tt,src,rel,one in rows]
ins_at = next(i for i, ln in enumerate(lines) if ln.startswith('📄 主题汇总笔记：') and 'openday' in ln)
# 去重
existing = set(lines)
add = [r for r in od_rows if r not in existing]
if add:
    lines = lines[:ins_at] + add + lines[ins_at:]
open(OB_IDX, 'w', encoding='utf-8').write('\n'.join(lines))
print(f'OK 00-index updated (+{len(add)} rows, heading r24 seg)')
