# -*- coding: utf-8 -*-
# 员工大会 R26 补采 · Part 2（仅补齐 00-索引 + GitHub 同步 + 乐享上传 + 推进 last-topic）
# 墙 HTML / 独立页 / index.json / 主题汇总笔记 已在主脚本正确完成，本脚本不重注入、不重复计数。
import json, os, re, subprocess, sys, urllib.request, urllib.error

KC = r"C:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection"
WS = r"C:\Users\v_yitcai\WorkBuddy\20260728154244"
HTML = os.path.join(KC, "staff-meeting", "staff-meeting.html")
RUN_PATH = os.path.join(KC, "staff-meeting", "runs", "staff-meeting-2026-08-25-r26.html")
RUN_NAME = os.path.basename(RUN_PATH)
OB_IDX = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
LT = os.path.join(KC, "last-topic.txt")

# ---- 解析本轮 8 卡（来自已生成的独立页，避免重复注入）----
h = open(RUN_PATH, encoding="utf-8").read()
parts = h.split('<div class="hl">')[1:]
assert len(parts) == 8, "run page card count = %d (expect 8)" % len(parts)
cards = []
for p in parts:
    title = re.search(r'<h3>(.*?)</h3>', p).group(1)
    cat = re.search(r'<span class="cat">(.*?)</span>', p).group(1)
    rel = "③高管间" if "badge r3\">高管间" in p else "②上下级"
    src = "一手" if "badge b1\">一手" in p else "二手"
    val = re.search(r'<p class="val">(.*?)</p>', p, re.S).group(1)
    cards.append({"title": title, "cat": cat, "rel": rel, "src": src, "val": val})
n3 = sum(1 for c in cards if c["rel"] == "③高管间")
n2 = sum(1 for c in cards if c["rel"] == "②上下级")
print("parsed run-page cards:", len(cards), "| ②", n2, "③", n3)

# ===== 00-索引更新（从既有基线 +8，保持与墙的常量差）=====
idx_txt = open(OB_IDX, encoding="utf-8").read()
HDR_TAIL = '二十五轮补采 2026-08-23（+7）'
assert HDR_TAIL in idx_txt, '00-index header tail not found'
idx_txt = idx_txt.replace(HDR_TAIL, HDR_TAIL + '｜ 二十六轮补采 2026-08-25(+8）', 1)
assert '**255 卡**' in idx_txt, '255 卡 not found'
idx_txt = idx_txt.replace('**255 卡**', '**263 卡**', 1)
m88 = re.search(r'(③高管间\([^)]*\)\s*)88( 卡)', idx_txt)
assert m88, '88 卡 not found'
idx_txt = idx_txt[:m88.start()] + m88.group(1) + str(88+n3) + m88.group(2) + idx_txt[m88.end():]
m137 = re.search(r'(②上下级\([^)]*\)\s*)137( 卡)', idx_txt)
assert m137, '137 卡 not found'
idx_txt = idx_txt[:m137.start()] + m137.group(1) + str(137+n2) + m137.group(2) + idx_txt[m137.end():]
NEXT = idx_txt.find('## 主题：', idx_txt.find('二十六轮补采'))
assert NEXT != -1
rows = ''.join(
    "| {0}（staff-meeting.html） | 4 | {1} | {2} | {3}：{4} |\n".format(
        c["title"], c["src"], c["rel"], c["cat"], c["val"][:30])
    for c in cards)
idx_txt = idx_txt[:NEXT] + rows + "\n" + idx_txt[NEXT:]
open(OB_IDX, "w", encoding="utf-8").write(idx_txt)
print("OK 00-索引更新（263 / ③%d / ②%d / +8 行）" % (88+n3, 137+n2))

# ===== GitHub 同步 =====
sync = os.path.join(WS, "sync_knowledge_github.py")
try:
    rs = subprocess.run([sys.executable, sync], capture_output=True, text=True, timeout=300)
    print("sync_knowledge_github:", rs.returncode, (rs.stdout.strip()[-300:] if rs.stdout else ""), (rs.stderr.strip()[:200] if rs.stderr else ""))
except Exception as e:
    print("\u26a0\ufe0f GitHub 同步异常（告警不阻断）：" + str(e)[:200])

# ===== 乐享上传（whoami 探活）=====
MCP_JSON = os.path.expanduser("~/.workbuddy/mcp.json")
LEXIANG_URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"
FOLDER = "a753a4ebc526495c9e9b2e2fb3cac314"
WALL_FILE_ID = "a1415122f8034d8d988fb06e41be44ac"
WALL_ENTRY_ID = "f3b5ea59395e49ca859f8726142742c2"

class LexiangMCP:
    def __init__(self, token):
        self.token = token; self.session = None
    def _post(self, payload, retries=3):
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

def put_bytes(url, data, retries=3):
    last = None
    for _ in range(retries):
        try:
            req = urllib.request.Request(url, data=data, method="PUT")
            req.add_header("Content-Type", "text/html")
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.status
        except Exception as e:
            last = str(e); continue
    raise RuntimeError("PUT fail: " + str(last))

try:
    token = json.load(open(MCP_JSON, encoding="utf-8"))["mcpServers"]["lexiang"]["headers"]["Authorization"]
    mc = LexiangMCP(token); mc.initialize(); mc.initialized()
    try:
        w = mc.call("whoami", {})
        print("whoami:", json.dumps(mc.biz(w), ensure_ascii=False)[:120])
    except Exception as e:
        print("whoami 跳过:", str(e)[:120])

    # (a) 更新累计墙文件本体
    wall_bytes = open(HTML, "rb").read()
    r = mc.call("file_apply_upload", {"file_id": WALL_FILE_ID, "parent_entry_id": WALL_ENTRY_ID,
                                      "name": "staff-meeting.html", "extension":"html",
                                      "mime_type":"text/html", "upload_type":"PRE_SIGNED_URL",
                                      "size": str(len(wall_bytes))})
    biz = mc.biz(r)
    if biz.get("code") != 0:
        raise RuntimeError("apply_upload(wall) FAIL {0}".format(biz.get("message")))
    sess = biz["data"]["session"]
    sid = sess.get("session_id") or sess.get("id")
    url = sess.get("upload_url") or sess["objects"][0]["upload_url"]
    st = put_bytes(url, wall_bytes)
    if st != 200: raise RuntimeError("PUT(wall) status " + str(st))
    r2 = mc.call("file_commit_upload", {"session_id": sid})
    biz2 = mc.biz(r2)
    if biz2.get("code") != 0: raise RuntimeError("commit(wall) FAIL " + str(biz2.get("message")))
    print("乐享累计墙已更新 OK")

    # (b) 新建本轮独立页条目
    run_bytes = open(RUN_PATH, "rb").read()
    r = mc.call("file_apply_upload", {"parent_entry_id": FOLDER, "name": RUN_NAME,
                                      "extension":"html", "mime_type":"text/html",
                                      "upload_type":"PRE_SIGNED_URL", "size": str(len(run_bytes))})
    biz = mc.biz(r)
    if biz.get("code") != 0:
        raise RuntimeError("apply_upload(run) FAIL {0}".format(biz.get("message")))
    sess = biz["data"]["session"]
    sid = sess.get("session_id") or sess.get("id")
    url = sess.get("upload_url") or sess["objects"][0]["upload_url"]
    st = put_bytes(url, run_bytes)
    if st != 200: raise RuntimeError("PUT(run) status " + str(st))
    r2 = mc.call("file_commit_upload", {"session_id": sid})
    biz2 = mc.biz(r2)
    if biz2.get("code") != 0: raise RuntimeError("commit(run) FAIL " + str(biz2.get("message")))
    rid = biz2["data"]["entry"]["id"]
    print("乐享新建独立页 OK entry_id=", rid)

    # 回写 lexiang-entry-map.json
    mapf = json.load(open(os.path.join(KC, "lexiang-entry-map.json"), encoding="utf-8"))
    sm = mapf.setdefault("staff-meeting", {"folder_id": FOLDER, "rounds": []})
    sm["folder_id"] = FOLDER
    if "wall" not in sm:
        sm["wall"] = {"entry_id": WALL_ENTRY_ID, "file_id": WALL_FILE_ID, "name": "staff-meeting.html"}
    sm["rounds"].append({"date": "2026-08-25", "entry_id": rid, "name": RUN_NAME,
                         "note": "轮次页 R26 (+8：会后行动闭环/一线吐槽会/圆桌问政/安全主讲/降本坦诚/CEO说不知道/CEO个人反馈/变革叙事·5②3③)"})
    json.dump(mapf, open(os.path.join(KC, "lexiang-entry-map.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("已回写 lexiang-entry-map.json")
except Exception as e:
    print("\u26a0\ufe0f 乐享上传跳过（warning，不中断）：" + str(e)[:300])

# ===== 推进 last-topic.txt =====
with open(LT, "r", encoding="utf-8") as f:
    cur_topic = f.read().strip()
NEXT_TOPIC = "Offsite"
if cur_topic == "\u5458\u5de5\u5927\u4f1a":
    with open(LT, "w", encoding="utf-8") as f:
        f.write(NEXT_TOPIC + "\n")
    print("last-topic.txt 推进：%s -> %s" % (cur_topic, NEXT_TOPIC))
else:
    print("\u26a0\ufe0f last-topic.txt 当前为「%s」非预期「员工大会」，未自动推进（请人工确认）" % cur_topic)

print("\n=== R26 Part2 完成 ===")
