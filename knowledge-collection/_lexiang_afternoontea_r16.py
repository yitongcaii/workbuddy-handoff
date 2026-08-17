# -*- coding: utf-8 -*-
"""乐享同步 · 下午茶研讨 十六轮（2026-08-17）。
直连 streamable-http 客户端。仅新建当轮独立页 afternoontea-20260817.html -> 子文件夹 96e0ca6a（afternoontea）。
回写 lexiang-entry-map.json。失败仅 warning 跳过。"""
import os, json, urllib.request, urllib.error

WS = r"C:\Users\v_yitcai\WorkBuddy\20260728154244"
KC = os.path.join(WS, "knowledge-collection")
MCP_JSON = os.path.expanduser("~/.workbuddy/mcp.json")
LEXIANG_URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"

FOLDER = "96e0ca6a548e4202a12d43dc91b48938"
RUN_NAME = "afternoontea-20260817.html"
RUN_PATH = os.path.join(KC, "afternoontea", RUN_NAME)

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

def main():
    try:
        token = load_token()
        mc = LexiangMCP(token)
        mc.initialize(); mc.initialized()
        try:
            b = mc.biz(mc.call("whoami", {}))
            print("whoami:", json.dumps(b, ensure_ascii=False)[:160])
        except Exception as e:
            print("whoami 跳过:", str(e)[:120])

        data = open(RUN_PATH, "rb").read()
        print(f"\n=== 新建独立页 {RUN_NAME} ({len(data)}B) -> 子文件夹 {FOLDER} ===")
        rid = upload_new(mc, FOLDER, RUN_NAME, data)
        print(f"    OK entry_id={rid} -> https://csig.lexiangla.com/pages/{rid}")

        mapf = json.load(open(os.path.join(KC, "lexiang-entry-map.json"), encoding="utf-8"))
        sm = mapf.setdefault("afternoontea", {"folder_id": FOLDER, "rounds": []})
        sm["folder_id"] = FOLDER
        sm["rounds"].append({"date": "20260817", "entry_id": rid, "name": RUN_NAME})
        json.dump(mapf, open(os.path.join(KC, "lexiang-entry-map.json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=2)
        print("=== 已回写 lexiang-entry-map.json ===")
    except Exception as e:
        print(f"⚠️ 乐享上传跳过（warning，不中断）：{str(e)[:300]}")

if __name__ == "__main__":
    main()
