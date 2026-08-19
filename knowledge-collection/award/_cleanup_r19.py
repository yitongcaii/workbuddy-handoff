# -*- coding: utf-8 -*-
import json, os, re

KC = r"C:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection"
VAULT = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库"

r19_titles = [
 "销售激励之旅(President's Club)·SiriusDecisions 五元素框架",
 "销售精英俱乐部首办指南·节奏设计与预算基准",
 "呼叫中心/一线客服认可·VoC 认证与四类项目",
 "AI 驱动认可·2026 真实能力鉴别（7 项声明 real/hype）",
 "女性领导力表彰·去表演化、透明标准、故事驱动",
 "员工志愿者/公益表彰·VTO 与高管连接",
]

def dedupe_lines(text, pred):
    seen=set(); out=[]
    for line in text.split("\n"):
        if pred(line):
            if line in seen:
                continue
            seen.add(line)
        out.append(line)
    return "\n".join(out)

# ---- index.json: dedupe by (title,url) ----
idx = json.load(open(os.path.join(KC,"index.json"),encoding="utf-8"))
seen=set(); uniq=[]
for e in idx:
    k=(e.get("title",""),e.get("url",""))
    if k in seen: continue
    seen.add(k); uniq.append(e)
json.dump(uniq, open(os.path.join(KC,"index.json"),"w",encoding="utf-8"), ensure_ascii=False, indent=2)
print("index.json deduped:", len(idx), "->", len(uniq))

# ---- obsidian note ----
note_path = os.path.join(VAULT,"素材","award","颁奖-知识卡汇总.md")
note = open(note_path,encoding="utf-8").read()
def note_pred(line):
    if any(t in line for t in r19_titles): return True
    if "本轮增量页（十九轮" in line: return True
    if "## 轮次 2026-08-19（" in line: return True
    if "本轮新增（均通过六维评估、仅 ②上下级 / ③高管间）" in line: return True
    return False
note2 = dedupe_lines(note, note_pred)
open(note_path,"w",encoding="utf-8").write(note2)
print("note deduped. R19 section count:", note2.count("## 轮次 2026-08-19（"),
      "| R19 link count:", note2.count("本轮增量页（十九轮"),
      "| title rows each:", [note2.count("| "+t) for t in r19_titles])

# ---- 00-index ----
idx00_path = os.path.join(VAULT,"00-知识采集索引.md")
idx00 = open(idx00_path,encoding="utf-8").read()
def z_pred(line):
    if any(t in line for t in r19_titles): return True
    if "十九轮 enrich 2026-08-19" in line: return True
    return False
idx00_2 = dedupe_lines(idx00, z_pred)
open(idx00_path,"w",encoding="utf-8").write(idx00_2)
print("00-index deduped. 十九轮 header count:", idx00_2.count("十九轮 enrich 2026-08-19"),
      "| title rows each:", [idx00_2.count("| "+t) for t in r19_titles])
print("CLEANUP DONE")
