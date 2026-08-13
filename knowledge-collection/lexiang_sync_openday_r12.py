# -*- coding: utf-8 -*-
"""乐享同步 · Open Day 第十二轮（2026-08-13）。
直连 streamable-http 客户端（mcporter CLI 已失效）。
(a) 更新累计墙 openday.html -> 子文件夹 22eea86c 下 wall entry a6ba9c18（in-place）
(b) 新建当轮独立页 openday-2026-08-13-r12.html -> 子文件夹 22eea86c
回写 lexiang-entry-map.json。
"""
import os, json, urllib.request, urllib.error

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KC = os.path.join(WS, "knowledge-collection")
MCP_JSON = os.path.expanduser("~/.workbuddy/mcp.json")
LEXIANG_URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"

OPENDIR_SUBFOLDER = "22eea86cd58a46729ed69380092c2c13"
WALL_ENTRY = "a6ba9c18bfdd47c1ae845dd0bdc579e9"
WALL_FILE  = "1026ac8c23ff4e949c27d37a67747c3a"

def load_token():
    cfg = json.load(open(MCP_JSON, encoding="utf-8"))
    return cfg["mcpServers"]["lexiang"]["headers"]["Authorization"]

class LexiangMCP:
    def __init__(self, token):
        self.token = token; self.session = None
    def _post(self, payload, retries=2):
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(LEXIANG_URL, data=data, method="POST")
        req.add_header("Content-Type", "application/json")
        req.add_header("Accept", "application/json, text/event-stream")
        req.add_header("Authorization", self.token)
        if self.session:
            req.add_header("Mcp-Session-Id", self.session)
        last_err = None
        for _ in range(retries):
            try:
                resp = urllib.request.urlopen(req, timeout=120)
                sid = resp.headers.get("mcp-session-id")
                if sid: self.session = sid
                raw = resp.read().decode("utf-8", "replace")
                return self._parse(raw)
            except urllib.error.HTTPError as e:
                last_err = f"HTTP {e.code}: {e.read().decode('utf-8','replace')[:400]}"; continue
            except Exception as e:
                last_err = str(e); continue
        raise RuntimeError(f"POST fail: {last_err}")
    def _parse(self, raw):
        raw = raw.strip()
        if raw.startswith("data:"):
            txt = [l[5:].strip() for l in raw.splitlines() if l.startswith("data:")]
            raw = "\n".join(txt)
        try: return json.loads(raw)
        except Exception: return json.loads(raw[raw.find("{"):])
    def initialize(self):
        return self._post({"jsonrpc":"2.0","id":1,"method":"initialize",
            "params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"wb-uploader","version":"1.0"}}})
    def initialized(self):
        try: self._post({"jsonrpc":"2.0","method":"notifications/initialized"})
        except Exception: pass
    def call(self, name, args):
        return self._post({"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":name,"arguments":args}})
    def biz(self, resp):
        res = resp.get("result")
        if not res: raise RuntimeError(f"no result: {json.dumps(resp, ensure_ascii=False)[:300]}")
        content = res.get("content") or []
        text = ""
        for c in content:
            if c.get("type")=="text": text = c.get("text",""); break
        try: return json.loads(text)
        except Exception: return {"_raw_text": text}

def put_bytes(url, data):
    req = urllib.request.Request(url, data=data, method="PUT")
    req.add_header("Content-Type", "text/html")
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.status

def whoami(mc):
    b = mc.biz(mc.call("whoami", {}))
    print("whoami:", json.dumps(b, ensure_ascii=False)[:200])
    return b

def upload_new(mc, parent_entry_id, name, data):
    r = mc.call("file_apply_upload", {
        "parent_entry_id": parent_entry_id, "name": name, "extension":"html",
        "mime_type":"text/html", "upload_type":"PRE_SIGNED_URL", "size": str(len(data)),
    })
    biz = mc.biz(r)
    if biz.get("code") != 0:
        raise RuntimeError(f"apply_upload FAIL {biz.get('message')} | {json.dumps(biz, ensure_ascii=False)[:300]}")
    sess = biz["data"]["session"]
    sid = sess.get("session_id") or sess.get("id")
    url = sess.get("upload_url") or sess["objects"][0]["upload_url"]
    st = put_bytes(url, data)
    if st != 200: raise RuntimeError(f"PUT status {st}")
    r2 = mc.call("file_commit_upload", {"session_id": sid})
    biz2 = mc.biz(r2)
    if biz2.get("code") != 0:
        raise RuntimeError(f"commit FAIL {biz2.get('message')}")
    return biz2["data"]["entry"]["id"]

def update_wall(mc, entry_id, file_id, name, data):
    r = mc.call("file_apply_upload", {
        "file_id": file_id, "parent_entry_id": entry_id, "name": name,
        "mime_type":"text/html", "size": str(len(data)), "upload_type":"PRE_SIGNED_URL",
    })
    biz = mc.biz(r)
    if biz.get("code") != 0:
        raise RuntimeError(f"apply_upload(update) FAIL {biz.get('message')} | {json.dumps(biz, ensure_ascii=False)[:300]}")
    sess = biz["data"]["session"]
    sid = sess.get("session_id") or sess.get("id")
    url = sess.get("upload_url") or sess["objects"][0]["upload_url"]
    st = put_bytes(url, data)
    if st != 200: raise RuntimeError(f"PUT status {st}")
    r2 = mc.call("file_commit_upload", {"session_id": sid})
    biz2 = mc.biz(r2)
    if biz2.get("code") != 0:
        raise RuntimeError(f"commit FAIL {biz2.get('message')}")
    return biz2["data"]["entry"]["id"]

def main():
    token = load_token()
    mc = LexiangMCP(token)
    mc.initialize(); mc.initialized()
    whoami(mc)

    # (a) 更新累计墙（in-place）
    wall_path = os.path.join(KC, "openday", "openday.html")
    wall_data = open(wall_path, "rb").read()
    print(f"\n=== 更新累计墙 openday.html ({len(wall_data)}B) -> entry {WALL_ENTRY} ===")
    eid = update_wall(mc, WALL_ENTRY, WALL_FILE, "openday.html", wall_data)
    print(f"    commit OK entry_id={eid} -> https://csig.lexiangla.com/pages/{eid}")

    # (b) 新建当轮独立页
    run_path = os.path.join(KC, "openday", "runs", "openday-2026-08-13-r12.html")
    run_data = open(run_path, "rb").read()
    run_name = "openday-2026-08-13-r12.html"
    print(f"\n=== 新建独立页 {run_name} ({len(run_data)}B) -> 子文件夹 {OPENDIR_SUBFOLDER} ===")
    rid = upload_new(mc, OPENDIR_SUBFOLDER, run_name, run_data)
    print(f"    OK entry_id={rid} -> https://csig.lexiangla.com/pages/{rid}")

    # 回写 map
    mapf = json.load(open(os.path.join(KC, "lexiang-entry-map.json"), encoding="utf-8"))
    od = mapf.setdefault("openday", {"folder_id": OPENDIR_SUBFOLDER, "wall": {}, "rounds": []})
    od["folder_id"] = OPENDIR_SUBFOLDER
    od["wall"] = {"entry_id": WALL_ENTRY, "file_id": WALL_FILE, "name": "openday.html"}
    od["rounds"].append({
        "date": "2026-08-13", "entry_id": rid, "name": run_name,
        "note": "轮次页 R12 (+13)"
    })
    json.dump(mapf, open(os.path.join(KC, "lexiang-entry-map.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print(f"\n=== 完成：累计墙已更新 + 独立页已新建，已回写 lexiang-entry-map.json ===")

if __name__ == "__main__":
    main()
