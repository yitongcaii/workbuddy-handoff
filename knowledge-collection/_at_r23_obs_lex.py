# -*- coding: utf-8 -*-
"""R23 后续：从已生成的增量页解析 10 卡，更新 Obsidian 笔记 + 00-索引 + runs 笔记 + 乐享上传。
不触碰累计墙/index.json（已在主脚本完成）。"""
import json, os, re, urllib.request, urllib.error

BASE = os.path.dirname(os.path.abspath(__file__))
RUN_NAME = "staff-meeting-2026-08-22-r23.html"
RUN_PATH = os.path.join(BASE, "staff-meeting", "runs", RUN_NAME)

def unesc(s):
    return s.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")

html = open(RUN_PATH, encoding="utf-8").read()
titles = re.findall(r'<h3>(.*?)</h3>', html)
rels = re.findall(r'<span class="badge r[23]">(.*?)</span>', html)
srcs = re.findall(r'<span class="badge b[12]">(.*?)</span>', html)
assert len(titles) == 10, ("parsed count", len(titles))
CARDS = []
for k in range(10):
    rel = "r3" if rels[k] == "高管间" else "r2"
    src = "b1" if srcs[k] == "一手" else "b2"
    CARDS.append({
        "title": unesc(titles[k]),
        "rel": rel, "rel_text": rels[k], "src": src, "src_text": srcs[k],
    })
print("解析卡:", len(CARDS))

cards_sec3 = [c for c in CARDS if c["rel"] == "r3"]
cards_sec2 = [c for c in CARDS if c["rel"] == "r2"]
print("③高管间:", len(cards_sec3), "②上下级:", len(cards_sec2))

# 质量分 + 一句话定位（按 CARDS 顺序，匹配 index 五列格式）
META_LIST = [
    (5, "领导建可复用可度量自上而下体系，核心消息两周内多渠道重复≥3次"),
    (5, "央企一手：政治属性挂帅+科技产业融合+穿透监管，视频分会场全覆盖"),
    (5, "省属国企一手：红黑榜晾晒短板+三级管理体系把战略拆到一线"),
    (4, "AI转型先治信任：living toolkit+town hall+透明AI政策+双向对话"),
    (4, "给管理者一套落地工具包，全员会→团队会/1:1 可复用"),
    (4, "对AI焦虑分群沟通，禁用空洞安抚陈词，给路径序列"),
    (4, "大会后逐级情境化下传，给管理者briefing包+反馈回路"),
    (4, "把大消息拆到个人动作级，核心信息跨渠道重复≥3次约半年"),
    (4, "按消息性质选模式：正面团结构用大会、坏消息用级联、草根可信用大使"),
    (5, "官方一手：CART字幕+ASL+轮梯+大字号，残障/感官/多语言可达"),
]
assert len(META_LIST) == len(CARDS), ("meta len", len(META_LIST), len(CARDS))
for c, (sc, ol) in zip(CARDS, META_LIST):
    c["score"], c["oneliner"] = sc, ol

# ============ Obsidian 汇总笔记（末尾追加轮次段） ============
VAULT = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库"
NOTE = os.path.join(VAULT, "素材", "staff-meeting", "员工大会-知识卡汇总.md")
t = open(NOTE, encoding="utf-8").read()
round_section = "\n## 轮次 20260822（二十三轮补采 +10）\n\n| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n"
for c in CARDS:
    round_section += "| {0}（staff-meeting.html） | {1} | {2} |\n".format(c["title"], c["rel_text"], c["src_text"])
t = t.rstrip("\n") + "\n" + round_section
open(NOTE, "w", encoding="utf-8").write(t)
print("Obsidian 汇总笔记追加完成")

# ============ runs 笔记（新建） ============
RUNS_NOTE = os.path.join(VAULT, "素材", "staff-meeting", "runs", "员工大会-2026-08-22-第二十三轮-知识卡.md")
runs_md = """---
title: 员工大会-2026-08-22-第二十三轮-知识卡
type: 自动化采集
date: 2026-08-22
tags: [知识采集, 员工大会, 二十三轮]
relation: [supervisor, exec]
---

# 员工大会 · 第二十三轮补采（2026-08-22，+10）

- **GitHub Pages 独立页**：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/runs/staff-meeting-2026-08-22-r23.html
- **本地路径**：`knowledge-collection/staff-meeting/runs/staff-meeting-2026-08-22-r23.html`
- **累计卡片墙（总索引）**：`knowledge-collection/staff-meeting/staff-meeting.html`（[线上](https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/staff-meeting.html)）
- **覆盖关系档**：③高管间 4 卡 / ②上下级 6 卡（无①平级）
- **乐享团队文件夹**：员工大会子文件夹（a753a4ebc526495c9e9b2e2fb3cac314）

## 本轮新增 10 卡

| 卡 | 适用关系 | 一手/二手 |
|---|---|---|
"""
for c in CARDS:
    runs_md += "| {0} | {1} | {2} |\n".format(c["title"], c["rel_text"], c["src_text"])
runs_md += "\n> 本笔记仅索引，不拷 HTML 副本；完整卡片见上方 GitHub Pages 独立页。\n"
open(RUNS_NOTE, "w", encoding="utf-8").write(runs_md)
print("runs 笔记新建完成:", RUNS_NOTE)

# ============ 00-索引 ============
IDX0 = os.path.join(VAULT, "00-知识采集索引.md")
i0 = open(IDX0, encoding="utf-8").read()
hdr_old = "二十二轮补采 2026-08-21（+16））"
assert hdr_old in i0, "title marker not found"
i0 = i0.replace(hdr_old, "二十二轮补采 2026-08-21（+16）｜ 二十三轮补采 2026-08-22（+10））", 1)
rel_map = {"r3": "③高管间", "r2": "②上下级"}
next_theme = i0.find("## 主题：", i0.find("## 主题：员工大会") + 10)
assert next_theme != -1, "next theme not found"
rows = "".join(
    "| {0}（staff-meeting.html） | {1} | {2} | {3} | {4} |\n".format(
        c["title"], c["score"], c["src_text"], rel_map[c["rel"]], c["oneliner"])
    for c in CARDS
)
i0 = i0[:next_theme] + rows + "\n" + i0[next_theme:]
open(IDX0, "w", encoding="utf-8").write(i0)
print("00-索引更新完成")

# ============ 乐享上传（新建独立页文件模式） ============
MCP_JSON = os.path.expanduser("~/.workbuddy/mcp.json")
LEXIANG_URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"
FOLDER = "a753a4ebc526495c9e9b2e2fb3cac314"
class LexiangMCP:
    def __init__(self, token):
        self.token = token; self.session = None
    def _post(self, payload, retries=2):
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(LEXIANG_URL, data=data, method="POST")
        req.add_header("Content-Type", "application/json")
        req.add_header("Accept", "application/json, text/event-stream")
        req.add_header("Authorization", self.token)
        if self.session: req.add_header("Mcp-Session-Id", self.session)
        last = None
        for _ in range(retries):
            try:
                resp = urllib.request.urlopen(req, timeout=120)
                sid = resp.headers.get("mcp-session-id")
                if sid: self.session = sid
                return self._parse(resp.read().decode("utf-8", "replace"))
            except urllib.error.HTTPError as e:
                last = "HTTP {0}: {1}".format(e.code, e.read().decode("utf-8", "replace")[:400]); continue
            except Exception as e:
                last = str(e); continue
        raise RuntimeError("POST fail: " + last)
    def _parse(self, raw):
        raw = raw.strip()
        if raw.startswith("data:"):
            raw = "\n".join(l[5:].strip() for l in raw.splitlines() if l.startswith("data:"))
        try: return json.loads(raw)
        except Exception: return json.loads(raw[raw.find("{"):])
    def initialize(self):
        return self._post({"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"wb-uploader","version":"1.0"}}})
    def initialized(self):
        try: self._post({"jsonrpc":"2.0","method":"notifications/initialized"})
        except Exception: pass
    def call(self, name, args):
        return self._post({"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":name,"arguments":args}})
    def biz(self, resp):
        res = resp.get("result")
        if not res: raise RuntimeError("no result: " + json.dumps(resp, ensure_ascii=False)[:300])
        text = ""
        for c in (res.get("content") or []):
            if c.get("type") == "text": text = c.get("text", ""); break
        try: return json.loads(text)
        except Exception: return {"_raw_text": text}
def put_bytes(url, data):
    req = urllib.request.Request(url, data=data, method="PUT")
    req.add_header("Content-Type", "text/html")
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.status
try:
    token = json.load(open(MCP_JSON, encoding="utf-8"))["mcpServers"]["lexiang"]["headers"]["Authorization"]
    mc = LexiangMCP(token); mc.initialize(); mc.initialized()
    try:
        w = mc.call("whoami", {})
        print("whoami:", json.dumps(mc.biz(w), ensure_ascii=False)[:120])
    except Exception as e:
        print("whoami 跳过:", str(e)[:120])
    data_bytes = open(RUN_PATH, "rb").read()
    r = mc.call("file_apply_upload", {"parent_entry_id": FOLDER, "name": RUN_NAME, "extension":"html", "mime_type":"text/html", "upload_type":"PRE_SIGNED_URL", "size": str(len(data_bytes))})
    biz = mc.biz(r)
    if biz.get("code") != 0:
        raise RuntimeError("apply_upload FAIL {0}".format(biz.get("message")))
    sess = biz["data"]["session"]
    sid = sess.get("session_id") or sess.get("id")
    url = sess.get("upload_url") or sess["objects"][0]["upload_url"]
    st = put_bytes(url, data_bytes)
    if st != 200: raise RuntimeError("PUT status " + str(st))
    r2 = mc.call("file_commit_upload", {"session_id": sid})
    biz2 = mc.biz(r2)
    if biz2.get("code") != 0: raise RuntimeError("commit FAIL " + str(biz2.get("message")))
    rid = biz2["data"]["entry"]["id"]
    print("乐享新建页 OK entry_id=", rid)
    mapf = json.load(open(os.path.join(BASE, "lexiang-entry-map.json"), encoding="utf-8"))
    sm = mapf.setdefault("staff-meeting", {"folder_id": FOLDER, "rounds": []})
    sm["folder_id"] = FOLDER
    sm["rounds"].append({"round": "r23", "date": "2026-08-22", "entry_id": rid, "name": RUN_NAME, "note": "轮次页 R23 (+10)｜新建模式，落员工大会子文件夹 a753a4eb"})
    json.dump(mapf, open(os.path.join(BASE, "lexiang-entry-map.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("已回写 lexiang-entry-map.json")
except Exception as e:
    print("⚠️ 乐享上传跳过（warning，不中断）：" + str(e)[:300])

print("\n=== R23 后续完成 ===")
