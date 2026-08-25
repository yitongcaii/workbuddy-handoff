# -*- coding: utf-8 -*-
# 员工大会 R26 · 乐享补救上传（仅当 mcp.json 的 lxmcp_ token 刷新后运行）
# 墙 HTML / 独立页 已正确生成；本脚本只把二者上传进乐享团队文件夹「待清洗素材/员工大会」
# 用法：刷新 token 后 -> python run_staffmeeting_r26_lexiang.py
import json, os, sys, urllib.request, urllib.error

KC = r"C:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection"
HTML = os.path.join(KC, "staff-meeting", "staff-meeting.html")
RUN_PATH = os.path.join(KC, "staff-meeting", "runs", "staff-meeting-2026-08-25-r26.html")
RUN_NAME = os.path.basename(RUN_PATH)
MCP_JSON = os.path.expanduser("~/.workbuddy/mcp.json")
LEXIANG_URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"
FOLDER = "a753a4ebc526495c9e9b2e2fb3cac314"          # 员工大会子文件夹（待清洗素材下）
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

token = json.load(open(MCP_JSON, encoding="utf-8"))["mcpServers"]["lexiang"]["headers"]["Authorization"]
mc = LexiangMCP(token); mc.initialize(); mc.initialized()
w = mc.call("whoami", {})
print("whoami:", json.dumps(mc.biz(w), ensure_ascii=False)[:120])

# (a) 更新累计墙文件本体
wall_bytes = open(HTML, "rb").read()
r = mc.call("file_apply_upload", {"file_id": WALL_FILE_ID, "parent_entry_id": WALL_ENTRY_ID,
                                  "name": "staff-meeting.html", "extension":"html",
                                  "mime_type":"text/html", "upload_type":"PRE_SIGNED_URL",
                                  "size": str(len(wall_bytes))})
biz = mc.biz(r)
if biz.get("code") != 0: raise RuntimeError("apply_upload(wall) FAIL {0}".format(biz.get("message")))
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
if biz.get("code") != 0: raise RuntimeError("apply_upload(run) FAIL {0}".format(biz.get("message")))
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
print("\n=== 乐享 R26 上传完成 ===")
