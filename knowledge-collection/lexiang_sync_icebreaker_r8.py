#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""乐享同步 · 破冰第八轮（2026-08-12）。
直连 streamable-http 客户端（mcporter CLI 已失效）。
(a) 更新累计墙 icebreaker.html -> entry 93fd6bf9（in-place，file_id=ae23e8f2）
(b) 新建当轮独立页 icebreaker-2026-08-12-r8.html -> icebreaker 子文件夹 f51480b0
回写 lexiang-entry-map.json。
"""
import os, sys, json, urllib.request, urllib.error

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # workspace root
KC = os.path.join(WS, "knowledge-collection")
MCP_JSON = os.path.expanduser("~/.workbuddy/mcp.json")
LEXIANG_URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"

# 累计墙 93fd6bf9 已被 2026-08-11 reorg 移入「归档」失效；icebreaker 子文件夹当前仅 R1-R6 轮次页。
# 对齐 staff-meeting reorg 范式：在子文件夹【新建】累计墙文件，并记录 entry/file 供后续 in-place 更新。
WALL_NAME = "icebreaker.html"
IC_SUBFOLDER = "f51480b0cfac4857bc28495b151c624f"

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
    r = mc.call("whoami", {})
    b = mc.biz(r)
    print("whoami:", json.dumps(b, ensure_ascii=False)[:200])
    return b

def upload_new(mc, parent_entry_id, name, data):
    size = str(len(data))
    r = mc.call("file_apply_upload", {
        "parent_entry_id": parent_entry_id, "name": name, "extension":"html",
        "mime_type":"text/html", "upload_type":"PRE_SIGNED_URL", "size": size,
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
    size = str(len(data))
    r = mc.call("file_apply_upload", {
        "file_id": file_id, "parent_entry_id": entry_id, "name": name,
        "mime_type":"text/html", "size": size, "upload_type":"PRE_SIGNED_URL",
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

def describe_file(mc, entry_id):
    r = mc.call("file_describe_file", {"entry_id": entry_id})
    b = mc.biz(r)
    if b.get("code") != 0:
        return None
    return b.get("data", {})

def main():
    token = load_token()
    mc = LexiangMCP(token)
    mc.initialize(); mc.initialized()
    whoami(mc)

    # (a) 在 icebreaker 子文件夹【新建】累计墙（旧墙 93fd6bf9 已在归档失效）
    wall_path = os.path.join(KC, "icebreaker", "icebreaker.html")
    wall_data = open(wall_path, "rb").read()
    print(f"\n=== 新建累计墙 {WALL_NAME} ({len(wall_data)}B) -> 子文件夹 {IC_SUBFOLDER} ===")
    eid = upload_new(mc, IC_SUBFOLDER, WALL_NAME, wall_data)
    print(f"    commit OK entry_id={eid} -> https://csig.lexiangla.com/pages/{eid}")
    # 取 file_id 供后续 in-place 更新
    fdesc = describe_file(mc, eid)
    file_id = None
    if fdesc:
        file_id = (fdesc.get("id") or fdesc.get("file_id") or
                   (fdesc.get("file") or {}).get("id"))
    print(f"    wall file_id={file_id}")

    # (b) new run page
    run_path = os.path.join(KC, "icebreaker", "runs", "icebreaker-2026-08-12-r8.html")
    run_data = open(run_path, "rb").read()
    run_name = "icebreaker-2026-08-12-r8.html"
    print(f"\n=== 新建独立页 {run_name} ({len(run_data)}B) -> 子文件夹 {IC_SUBFOLDER} ===")
    rid = upload_new(mc, IC_SUBFOLDER, run_name, run_data)
    print(f"    OK entry_id={rid} -> https://csig.lexiangla.com/pages/{rid}")

    # 回写 map：wall 键记录累计墙 entry/file，rounds 追加 r8
    mapf = json.load(open(os.path.join(KC, "lexiang-entry-map.json"), encoding="utf-8"))
    ic = mapf.setdefault("icebreaker", {"folder_id": IC_SUBFOLDER, "rounds": []})
    ic["folder_id"] = IC_SUBFOLDER
    ic["wall"] = {"entry_id": eid, "file_id": file_id, "name": WALL_NAME}
    ic["rounds"].append({
        "date": "2026-08-12", "entry_id": rid, "name": run_name,
        "note": "轮次页 R8 (+11)"
    })
    json.dump(mapf, open(os.path.join(KC, "lexiang-entry-map.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print(f"\n=== 完成：累计墙已新建 + 独立页已新建，已回写 lexiang-entry-map.json ===")

if __name__ == "__main__":
    main()
