# -*- coding: utf-8 -*-
"""
split_wall_to_runs.py — 把"累计卡片墙"按顺序均匀拆成若干【批次独立页】。
用于把历史上合并在一页的素材，拆回为每个自动化批次的独立页面。

输入：knowledge-collection/<topic>/<topic>.html（累计墙）
输出：knowledge-collection/<topic>/runs/<topic>-<date>-b<batch>.html  （每批一页）
      knowledge-collection/<topic>/runs/index.html                 （本主题分页索引）
      Obsidian 知识采集库/素材/<topic>/runs/<topic>-<date>-第<batch>批-知识卡.md

特性：
- 顺序切片（保留累计墙的文档顺序：③高管间段 → ②上下级段）
- 每页排版统一：渐变 hero + 批次徽标 + 上/下批导航 + 回链累计墙 + 三色关系 chip + 页脚
- --exclude-file 可排除已单独成页的真·轮次页（如 offsite 第7轮 r7.html）的卡，避免重复
"""
import argparse, os, re
from gen_run_page import split_cards, relation_of, rel_label, EMOJI, CSS

FOOTER = ('<footer style="text-align:center;padding:24px;color:#94a3b8;font-size:13px;'
          'border-top:1px solid #e2e8f0;margin-top:40px;">'
          '📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>')

EXTRA_CSS = """
.nav{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 18px;}
.nav a,.nav span{font-size:13px;padding:7px 14px;border-radius:20px;font-weight:600;text-decoration:none;}
.nav a{background:#eef0ff;color:#6c5ce7;}
.nav a:hover{background:#e0e3ff;}
.nav span.disabled{background:#f1f5f9;color:#cbd5e1;}
.hl{transition:transform .15s ease, box-shadow .15s ease;}
.hl:hover{transform:translateY(-3px);box-shadow:0 16px 40px rgba(108,92,231,.18);}
.idxlist{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:22px 14px;margin-top:14px;}
.idxcard{position:relative;background:#fff;border-radius:16px;padding:22px 18px 16px;border-top:4px solid var(--accent);box-shadow:0 10px 32px rgba(108,92,231,.10);}
.idxcard .seq{position:absolute;top:-14px;left:18px;width:30px;height:30px;border-radius:50%;background:linear-gradient(135deg,var(--accent) 0%,var(--accent2) 100%);color:#fff;font-weight:800;font-size:14px;display:flex;align-items:center;justify-content:center;box-shadow:0 6px 16px rgba(108,92,231,.35);}
.idxcard h3{font-size:16px;margin-bottom:6px;}
.idxcard .meta{font-size:12.5px;color:var(--sub);}
.idxcard .note{font-size:12px;color:#7b2cbf;margin-top:5px;font-weight:600;}
.idxcard a{display:inline-block;margin-top:10px;color:var(--accent2);text-decoration:none;font-weight:600;font-size:13px;}
"""


def norm(u):
    u = u.strip().replace('&amp;', '&').lower()
    u = re.sub(r'^https?://', '', u)
    u = re.sub(r'^www\.', '', u)
    return u.rstrip('/')


def href_of(card):
    m = re.search(r'href="([^"]+)"', card)
    return m.group(1) if m else ''


def title_of(card):
    m = re.search(r'<h3>(.*?)</h3>', card, re.S)
    return re.sub(r'<[^>]+>', '', m.group(1)).strip() if m else '无标题'


def src_of(card):
    return '一手' if 'badge b1' in card else '二手'


def rel_of_card(card):
    if 'badge r3' in card:
        return '③高管间'
    if 'badge r2' in card:
        return '②上下级'
    return '①平级'


def build_batch_page(topic, topic_name, date, batch, total, cards, prev_file, next_file, master, idx):
    rel = {'r1': 0, 'r2': 0, 'r3': 0}
    for c in cards:
        for r in relation_of(c):
            rel[r] += 1
    n = len(cards)
    parts = []
    if rel['r3']:
        parts.append(f'③高管间 {rel["r3"]}')
    if rel['r2']:
        parts.append(f'②上下级 {rel["r2"]}')
    if rel['r1']:
        parts.append(f'①平级 {rel["r1"]}')
    rel_str = ' / '.join(parts) if parts else '—'

    groups = {'r3': [], 'r2': [], 'r1': []}
    for c in cards:
        rs = relation_of(c)
        groups[rs[0] if rs else 'r2'].append(c)
    order = [k for k in ('r3', 'r2', 'r1') if groups[k]]
    sec_html = ''
    for k in order:
        cls = {'r3': 'sec3', 'r2': 'sec2', 'r1': 'sec1'}[k]
        sec_html += f'''  <div class="sec {cls}">
    <h2>{rel_label(k)}</h2>
    <span class="tag">{len(groups[k])} 卡</span>
  </div>
  <div class="grid">
{chr(10).join(groups[k])}
  </div>
'''

    emoji = EMOJI.get(topic, '📚')
    title = f'{topic_name} · 第 {batch}/{total} 批（拆分页）'
    nav = '<div class="nav">'
    nav += (f'<a href="{prev_file}">← 上一批</a>' if prev_file
            else '<span class="disabled">← 上一批</span>')
    nav += f'<a href="{idx}">📑 本主题分页</a>'
    nav += f'<a href="{master}">🗂 累计总索引</a>'
    nav += (f'<a href="{next_file}">下一批 →</a>' if next_file
            else '<span class="disabled">下一批 →</span>')
    nav += '</div>'

    hero = f'''  <div class="hero">
    <h1>{emoji} {topic_name} · 第 {batch} / 共 {total} 批</h1>
    <p>由 <a href="{master}" style="color:#fff;text-decoration:underline;">{topic}.html</a> 累计墙顺序拆分（非原始轮次）｜ 拆分于 {date} ｜ 本批 {n} 卡（{rel_str}）｜ 受众关系分层（仅②③，剔除①）</p>
    <div class="relbar">
      <span>② 领导↔员工（上下级）</span>
      <span>③ 领导↔领导（高管间）</span>
    </div>
  </div>'''

    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
{CSS}{EXTRA_CSS}</style>
</head>
<body>
<div class="wrap">
{nav}
{hero}
{sec_html}
</div>
{FOOTER}
</body>
</html>
'''


def build_index_page(topic, topic_name, date, batches, master):
    emoji = EMOJI.get(topic, '📚')
    batches = sorted(batches, key=lambda b: b['seq'])
    n = len(batches)
    cards_html = ''
    for b in batches:
        note = f'<div class="note">{b["note"]}</div>' if b.get('note') else ''
        cards_html += f'''    <div class="idxcard">
      <div class="seq">{b['seq']}</div>
      <h3>{b['label']}</h3>
      <div class="meta">{b['n']} 卡 ｜ {b['rel_str']}</div>{note}
      <a href="{b['file']}">查看本批 →</a>
    </div>
'''
    nav = f'<div class="nav"><a href="../{topic}.html">🗂 累计总索引</a></div>'
    hero = f'''  <div class="hero">
    <h1>{emoji} {topic_name} · 分页索引</h1>
    <p>累计墙 <a href="../{topic}.html" style="color:#fff;text-decoration:underline;">{topic}.html</a> 共拆为 {n} 个批次独立页｜ 按<b>采集 / 创建顺序从早到晚</b>排列（序号 1 → {n}）｜ 拆分于 {date}</p>
  </div>'''
    return f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{topic_name} · 分页索引</title>
<style>
{CSS}{EXTRA_CSS}</style>
</head>
<body>
<div class="wrap">
{nav}
{hero}
  <div class="idxlist">
{cards_html}  </div>
</div>
{FOOTER}
</body>
</html>
'''


def build_obsidian_note(topic, topic_name, date, batch, total, cards, page_url, master_url):
    rel = {'r1': 0, 'r2': 0, 'r3': 0}
    for c in cards:
        for r in relation_of(c):
            rel[r] += 1
    n = len(cards)
    parts = []
    if rel['r3']:
        parts.append(f'③高管间 {rel["r3"]}')
    if rel['r2']:
        parts.append(f'②上下级 {rel["r2"]}')
    rows = []
    for i, c in enumerate(cards, 1):
        url = href_of(c)
        urltxt = url.split('//')[-1]
        rows.append(f'| {i} | {title_of(c)} | {rel_of_card(c)} | {src_of(c)} | [{urltxt}]({url}) |')
    table = '\n'.join(rows)
    emoji = EMOJI.get(topic, '📚')
    return f'''---
title: {topic_name} · 第{batch}批（拆分页）
type: 自动化采集
tags: [活动/ai, 知识采集, {topic}, 独立页]
source: 知识采集自动化（累计墙顺序拆分）
---

# {emoji} {topic_name} · 第 {batch} / 共 {total} 批（拆分页）

> 由 `{topic}.html` 累计墙**顺序均匀拆分**（非原始轮次标记——原始轮次已丢失）；本批 **{n} 卡**（{' / '.join(parts)}）。

🔗 **独立页（点开即看）**
- GitHub Pages：{page_url}
- 累计总索引（卡片墙）：{master_url}

## 本批卡片（{n}）

| # | 标题 | 适用关系 | 来源 | 链接 |
|---|------|---------|------|------|
{table}

## 说明
- 知识采集自动化已改为「每批次独立页」：累计墙保留作总索引，每次拆分批次独立落库三端（GitHub Pages / Obsidian / 乐享），可追溯、不互相覆盖。
- 页脚硬约束：`📌 本页由 yitong 沉淀整理 · 文化活动知识库`。
'''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--topic', required=True)
    ap.add_argument('--topic-name', required=True)
    ap.add_argument('--wall', required=True)
    ap.add_argument('--date', required=True)
    ap.add_argument('--size', type=int, default=12)
    ap.add_argument('--exclude-file', help='排除此 runs html 中的卡（已单独成页的真·轮次）')
    ap.add_argument('--extra-runs', help='额外真·轮次页注入索引（排在最后=最晚采集），格式 file.html|label|note，多组用;分隔')
    ap.add_argument('--vault', help='Obsidian 知识采集库根，如 C:/.../知识采集库')
    ap.add_argument('--gh-pages-base', default='https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection')
    args = ap.parse_args()

    wall = open(args.wall, encoding='utf-8').read()
    cards = split_cards(wall)

    excluded = set()
    if args.exclude_file and os.path.exists(args.exclude_file):
        ex = open(args.exclude_file, encoding='utf-8').read()
        for c in split_cards(ex):
            u = href_of(c)
            if u:
                excluded.add(norm(u))
        if excluded:
            before = len(cards)
            cards = [c for c in cards if norm(href_of(c)) not in excluded]
            print(f'[exclude] {args.exclude_file}: 排除 {before - len(cards)} 张（保留 {len(cards)}）')

    total = max(1, (len(cards) + args.size - 1) // args.size)
    outdir = os.path.join(os.path.dirname(args.wall), 'runs')
    os.makedirs(outdir, exist_ok=True)

    batches_meta = []
    pages = []
    for i in range(total):
        chunk = cards[i * args.size:(i + 1) * args.size]
        batch = i + 1
        fname = f'{args.topic}-{args.date}-b{batch}.html'
        fpath = os.path.join(outdir, fname)
        pages.append((batch, chunk, fpath, fname))

    for idx, (batch, chunk, fpath, fname) in enumerate(pages):
        prev_file = pages[idx - 1][3] if idx > 0 else None
        next_file = pages[idx + 1][3] if idx < len(pages) - 1 else None
        html = build_batch_page(args.topic, args.topic_name, args.date, batch, total,
                                chunk, prev_file, next_file, f'../{args.topic}.html', 'index.html')
        open(fpath, 'w', encoding='utf-8').write(html)
        rel = {'r1': 0, 'r2': 0, 'r3': 0}
        for c in chunk:
            for r in relation_of(c):
                rel[r] += 1
        parts = []
        if rel['r3']:
            parts.append(f'③高管间 {rel["r3"]}')
        if rel['r2']:
            parts.append(f'②上下级 {rel["r2"]}')
        if rel['r1']:
            parts.append(f'①平级 {rel["r1"]}')
        batches_meta.append({'seq': batch, 'label': f'第 {batch} / 共 {total} 批',
                             'n': len(chunk),
                             'rel_str': ' / '.join(parts) if parts else '—', 'file': fname,
                             'note': ''})
        print(f'  ✅ {fname} | {len(chunk)} 卡 | {batches_meta[-1]["rel_str"]}')

    # 额外真·轮次页（排在最后 = 最晚采集），如 offsite 的 r7
    if args.extra_runs:
        for i, part in enumerate([p for p in args.extra_runs.split(';') if p.strip()]):
            f_html, label, note = [x.strip() for x in part.split('|')]
            epath = os.path.join(outdir, f_html)
            ex = open(epath, encoding='utf-8').read() if os.path.exists(epath) else ''
            ex_cards = split_cards(ex)
            rel = {'r1': 0, 'r2': 0, 'r3': 0}
            for c in ex_cards:
                for r in relation_of(c):
                    rel[r] += 1
            parts = []
            if rel['r3']:
                parts.append(f'③高管间 {rel["r3"]}')
            if rel['r2']:
                parts.append(f'②上下级 {rel["r2"]}')
            if rel['r1']:
                parts.append(f'①平级 {rel["r1"]}')
            batches_meta.append({'seq': total + 1 + i, 'label': label,
                                 'n': len(ex_cards),
                                 'rel_str': ' / '.join(parts) if parts else '—',
                                 'file': f_html, 'note': note})
            print(f'  ➕ 索引附加（最晚）: {f_html} | {len(ex_cards)} 卡')

    # runs index
    idx_html = build_index_page(args.topic, args.topic_name, args.date, batches_meta,
                                f'../{args.topic}.html')
    idx_path = os.path.join(outdir, 'index.html')
    open(idx_path, 'w', encoding='utf-8').write(idx_html)
    print(f'  ✅ index.html | {len(batches_meta)} 批（含额外真·轮次）')

    # Obsidian notes
    if args.vault:
        base = os.path.join(args.vault, '素材', args.topic, 'runs')
        os.makedirs(base, exist_ok=True)
        for batch, chunk, fpath, fname in pages:
            page_url = f'{args.gh_pages_base}/{args.topic}/runs/{fname}'
            master_url = f'{args.gh_pages_base}/{args.topic}/{args.topic}.html'
            note = build_obsidian_note(args.topic, args.topic_name, args.date, batch, total,
                                       chunk, page_url, master_url)
            npath = os.path.join(base, f'{args.topic}-{args.date}-第{batch}批-知识卡.md')
            open(npath, 'w', encoding='utf-8').write(note)
        print(f'  ✅ Obsidian 笔记 {len(pages)} 篇 → {base}')

    print(f'\n[{args.topic}] 拆分完成：{len(cards)} 卡 → {total} 批（每批≤{args.size}）')


if __name__ == '__main__':
    main()
