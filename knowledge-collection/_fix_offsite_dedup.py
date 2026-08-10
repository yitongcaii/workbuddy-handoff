import re

html_path = 'offsite/offsite.html'
html = open(html_path, encoding='utf-8').read()

def block_by_url(u):
    i = html.find(f'href="{u}"')
    assert i != -1, f"url not found: {u}"
    start = html.rfind('<div class="hl">', 0, i)
    nxt = html.find('<div class="hl">', i)
    ftr = html.find('<footer>', i)
    e = min([x for x in [nxt, ftr] if x != -1])
    return html[start:e]

# ---- 1. DELETE card 33 (iceindia) ----
u33 = "https://www.iceindia.biz/annual-corporate-offsite-planning"
blk33 = block_by_url(u33)
assert blk33 in html, "blk33 not found in html"
html = html.replace(blk33, "\n")
print("deleted 33 block, len removed:", len(blk33))

# ---- 2. MERGE 33's distinct points into card 34 (easyhotelrfp) exec + note ----
u34 = "https://easyhotelrfp.com/blog/corporate-offsite-planning-guide"
old_exec34 = '<div class="inner">倒推议程——从「离场要带走的 3-5 条承诺」反排；目的→人数→场地→时长→议程 50/30/20 严格排序；高风险战略场请外部引导师；给领导 2-3 个差异化方案选项而非单一推荐以暴露真实对齐；48h 内调研度量。</div>'
new_exec34 = '<div class="inner">倒推议程——从「离场要带走的 3-5 条承诺」反排；先于场地与高管定义 outcomes+KPI（会后调研/业务结果/团队表现）再启动；目的→人数→场地形态（山地/海滨/别墅单间vs共享）→时长→议程 50/30/20 严格排序；议程留白含本地文化体验+spa/社交晚餐；高风险战略场请外部引导师；给领导 2-3 个差异化方案选项而非单一推荐以暴露真实对齐；48h 内调研度量。</div>'
assert old_exec34 in html, "old_exec34 not found"
html = html.replace(old_exec34, new_exec34, 1)

old_note34 = '<div class="note">适用：③ 领导/战略 offsite 立项与预算审批，含可抄的欧元预算基准与时间轴。</div>'
new_note34 = '<div class="note">适用：③ 领导/战略 offsite 立项与预算审批，含可抄的欧元预算基准与时间轴。📌 已合并原「企业年度 Offsite 全流程」（iceindia）差异化点：年会式 offsite 的 outcomes+KPI 定义、选址形态匹配、体验活动留白。</div>'
assert old_note34 in html, "old_note34 not found"
html = html.replace(old_note34, new_note34, 1)
print("merged into 34")

# ---- 3. card 39 (goteamassemble) add differentiation note ----
u39 = "https://blog.goteamassemble.com/posts/how-to-lead-an-offsite-for-distributed-teams-tips-tricks-and-a-touch-of-magic"
old_note39 = '<div class="note">适用：② 管理者带分布/远程团队做线下聚首 offsite，混合式连接设计。</div>'
new_note39 = '<div class="note">适用：② 管理者带分布/远程团队做线下聚首 offsite，混合式连接设计。🔍 差异化：区别于卡片22「虚拟/混合高管 Offsite（45+15法则）」——本卡偏管理者带分布式团队实操工具链（Zoom/Teams+Miro/Donut），含跨时区排期与会前 survey 对齐，非高管闭门场景。</div>'
assert old_note39 in html, "old_note39 not found"
html = html.replace(old_note39, new_note39, 1)
print("annotated 39")

# ---- 4. card 40 (kathrynlandis) add differentiation note ----
u40 = "https://www.kathrynlandisconsulting.com/blog/4-strategies-for-an-impactful-team-offsite"
old_note40 = '<div class="note">适用：② 管理者带团队务虚/团建，四策略覆盖目标-安全-引导-跟进全闭环。</div>'
new_note40 = '<div class="note">适用：② 管理者带团队务虚/团建，四策略覆盖目标-安全-引导-跟进全闭环。🔍 差异化：区别于卡片20「领导力 Offsite 选型与心理安全」、卡片5「高管团队 Offsite 21条实操」——本卡聚焦「四策略」闭环且明确反对用 MBTI/大五性格测评填充，强调组织因素（资源/目标/角色清晰度）更影响业务。</div>'
assert old_note40 in html, "old_note40 not found"
html = html.replace(old_note40, new_note40, 1)
print("annotated 40")

# ---- 5. counts: sec3 tag 26 -> 25 ----
assert '    <span class="tag">26 卡</span>' in html, "sec3 tag 26 not found"
html = html.replace('    <span class="tag">26 卡</span>', '    <span class="tag">25 卡</span>', 1)

# ---- 6. hero dedup note ----
old_hero = '采集于 2026-08-07 ｜ 2026-08-08 三轮 enrich +10 ｜ 2026-08-09 五轮 enrich +8 ｜ 2026-08-09(夜) 六轮 enrich +5 ｜ 六维评估（含关系适配度）｜ 一手/二手标注 ｜ 历史去重 ｜ 受众关系分层（仅②上下级 / ③高管间）'
new_hero = '采集于 2026-08-07 ｜ 2026-08-08 三轮 enrich +10 ｜ 2026-08-09 五轮 enrich +8 ｜ 2026-08-09(夜) 六轮 enrich +5 ｜ 2026-08-10 语义去重 -1（合并 iceindia→easyhotelrfp，保留预算基准硬数据）｜ 六维评估（含关系适配度）｜ 一手/二手标注 ｜ 历史去重 ｜ 受众关系分层（仅②上下级 / ③高管间）'
assert old_hero in html, "hero anchor not found"
html = html.replace(old_hero, new_hero, 1)

# ---- verify ----
n_cards = html.count('class="hl"')
r3 = html.count('badge r3')
r2 = html.count('badge r2')
footer = '📌 本页由 yitong 沉淀整理 · 文化活动知识库' in html
print("cards now:", n_cards, "| r3:", r3, "| r2:", r2, "| footer:", footer)
assert n_cards == 39, f"expected 39 cards, got {n_cards}"
assert r3 == 25, f"expected 25 r3, got {r3}"
assert r2 == 14
assert footer

open(html_path, 'w', encoding='utf-8').write(html)
print("OFFSITE HTML FIXED & SAVED")
