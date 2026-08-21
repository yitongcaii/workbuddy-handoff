# -*- coding: utf-8 -*-
"""R22 后续：从已生成的增量页解析 7 卡，更新 Obsidian 笔记 + 00-索引 + 乐享上传。
不触碰累计墙/index.json（已在主脚本完成）。"""
import json, os, re, urllib.request, urllib.error

BASE = os.path.dirname(os.path.abspath(__file__))
AT_DIR = os.path.join(BASE, "afternoontea")
RUN_NAME = "afternoontea-20260821.html"
RUN_PATH = os.path.join(AT_DIR, RUN_NAME)

def unesc(s):
    return s.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")

html = open(RUN_PATH, encoding="utf-8").read()
emojis = re.findall(r'<span class="emoji">(.*?)</span>', html)
titles = re.findall(r'<h3>(.*?)</h3>', html)
cats = re.findall(r'<span class="cat">(.*?)</span>', html)
rels = re.findall(r'<span class="badge r[23]">(.*?)</span>', html)
srcs = re.findall(r'<span class="badge b[12]">(.*?)</span>', html)
vals = re.findall(r'<p class="val">(.*?)</p>', html)
hows = re.findall(r'<div class="inner">(.*?)</div>', html)
urls = re.findall(r'<div class="src">.*?<a href="(.*?)"', html, re.S)
notes = re.findall(r'<div class="note">(.*?)</div>', html)
assert len(titles) == 7, ("parsed count", len(titles))
CARDS = []
for k in range(7):
    rel = "r3" if rels[k] == "高管间" else "r2"
    src = "b1" if srcs[k] == "一手" else "b2"
    CARDS.append({
        "emoji": emojis[k], "title": unesc(titles[k]), "cat": cats[k],
        "rel": rel, "rel_text": rels[k], "src": src, "src_text": srcs[k],
        "val": unesc(vals[k]), "how": unesc(hows[k]), "url": urls[k], "note": unesc(notes[k]),
    })
print("解析卡:", len(CARDS), "首张:", CARDS[0]["title"][:30])

cards_sec3 = [c for c in CARDS if c["rel"] == "r3"]
cards_sec2 = [c for c in CARDS if c["rel"] == "r2"]
print("③高管间:", len(cards_sec3), "②上下级:", len(cards_sec2))

# ============ Obsidian 笔记 ============
VAULT = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库"
NOTE = os.path.join(VAULT, "素材", "afternoontea", "下午茶研讨-知识卡汇总.md")
t = open(NOTE, encoding="utf-8").read()
assert "（138 卡 · 上下级/高管间）" in t
t = t.replace("（138 卡 · 上下级/高管间）", "（145 卡 · 上下级/高管间）", 1)
# timeline blockquote 补 R20/R21/R22（此前停在十九轮）
tl_old = "十九轮 enrich 2026-08-19(+12)"
assert tl_old in t, "timeline marker not found"
t = t.replace(tl_old, tl_old + " ｜ 二十轮 enrich 2026-08-20(+6) ｜ 二十一轮 enrich 2026-08-20(+9) ｜ 二十二轮 enrich 2026-08-21(+7)", 1)
assert "累计 138 卡（③高管间 53 / ②上下级 89，含 4 张跨档双标；一手 40 + 二手 98）" in t
t = t.replace("累计 138 卡（③高管间 53 / ②上下级 89，含 4 张跨档双标；一手 40 + 二手 98）",
              "累计 145 卡（③高管间 56 / ②上下级 93，含 4 张跨档双标；一手 43 + 二手 102）", 1)
round_section = (
    "\n## 轮次 2026-08-21（+7）\n"
    "> 二十二轮 enrich：新增 7 卡（③ 高管间 +3：CEO 同侪顾问小组·保密决策压力测试（Vistage/EO/Helix）/ 高管闭门早餐会·策展式同行对话（Val Wright）/ 保密早餐会·董事会级敏感决策场；② 上下级 +4：建行兴安分行党委书记一对一访谈 / 苏州园林集团经营层谈心谈话 / 台茂精机新员工茶话会 / 沃尔玛式越级沟通·二八倾听法则）。无 peer，relation 仅取 supervisor/exec。\n"
    "> 线上预览：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/afternoontea/afternoontea.html ｜ 本轮增量页：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/afternoontea/afternoontea-20260821.html\n"
)
marker3 = "## ③ 领导↔领导（高管间 · exec）— 51 卡"
assert marker3 in t
t = t.replace(marker3, round_section + marker3.replace("51 卡", "56 卡"), 1)
marker2 = "## ② 领导↔员工（上下级 · supervisor）— 83 卡"
assert marker2 in t
def nrow(num, c):
    return "| {0} | {1} | {2} | {3} |\n".format(num, c["title"], c["src_text"], c["val"])
r3_rows = "".join(nrow(52 + i, c) for i, c in enumerate(cards_sec3))
t = t.replace(marker2, r3_rows + "\n" + marker2.replace("83 卡", "93 卡"), 1)
r2_rows = "".join(nrow(84 + i, c) for i, c in enumerate(cards_sec2))
t = t.rstrip("\n") + "\n" + r2_rows
open(NOTE, "w", encoding="utf-8").write(t)
print("Obsidian 笔记更新完成")

# ============ 00-索引 ============
IDX0 = os.path.join(VAULT, "00-知识采集索引.md")
i0 = open(IDX0, encoding="utf-8").read()
hdr_old = "二十一轮 enrich 2026-08-20(+9)）"
assert hdr_old in i0
i0 = i0.replace(hdr_old, "二十一轮 enrich 2026-08-20(+9) ｜ 二十二轮 enrich 2026-08-21(+7)）", 1)
assert "**138 卡**" in i0
i0 = i0.replace("**138 卡**", "**145 卡**", 1)
assert "一手 40 + 二手 98" in i0
i0 = i0.replace("一手 40 + 二手 98", "一手 43 + 二手 102", 1)
assert "③高管间(...) 53 卡 / ②上下级(...) 89 卡（含 4 张跨档双标，去重后 128）" in i0
i0 = i0.replace("③高管间(...) 53 卡 / ②上下级(...) 89 卡（含 4 张跨档双标，去重后 128）",
                "③高管间(...) 56 卡 / ②上下级(...) 93 卡（含 4 张跨档双标，去重后 141）", 1)
narr_tail = "卓尔科技总经理接待日，从员工状态/发展方向四方向听建议）。"
assert narr_tail in i0
i0 = i0.replace(narr_tail, narr_tail
    + "二十二轮 enrich 新增（③CEO 同侪顾问小组·保密决策压力测试 / ③高管闭门早餐会·策展式同行对话 / ③保密早餐会·董事会级敏感决策场 + ②建行兴安分行党委书记一对一访谈 / ②苏州园林集团经营层谈心谈话 / ②台茂精机新员工茶话会 / ②沃尔玛式越级沟通·二八倾听法则）。", 1)
next_theme = i0.find("## 主题：", i0.find("## 主题：下午茶研讨") + 10)
assert next_theme != -1
rel_map = {"r3": "③高管间", "r2": "②上下级"}
rows = "".join(
    "| {0}（afternoontea.html） | 6 | {1} | {2} |  |\n".format(c["title"], c["src_text"], rel_map[c["rel"]])
    for c in CARDS
)
i0 = i0[:next_theme] + rows + "\n" + i0[next_theme:]
open(IDX0, "w", encoding="utf-8").write(i0)
print("00-索引更新完成")

# ============ 乐享上传（新建独立页文件模式）============
MCP_JSON = os.path.expanduser("~/.workbuddy/mcp.json")
LEXIANG_URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"
FOLDER = "96e0ca6a548e4202a12d43dc91b48938"
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
    sm = mapf.setdefault("afternoontea", {"folder_id": FOLDER, "rounds": []})
    sm["folder_id"] = FOLDER
    sm["rounds"].append({"date": "20260821", "entry_id": rid, "name": RUN_NAME})
    json.dump(mapf, open(os.path.join(BASE, "lexiang-entry-map.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("已回写 lexiang-entry-map.json")
except Exception as e:
    print("⚠️ 乐享上传跳过（warning，不中断）：" + str(e)[:300])

print("\n=== R22 后续完成 ===")
