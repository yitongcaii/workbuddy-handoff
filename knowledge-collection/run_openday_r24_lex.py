# -*- coding: utf-8 -*-
# Open Day 二十四轮（r24, 2026-08-23）· 乐享同步：仅新建当轮增量页文件（不覆盖历史页/墙）
import os, json, urllib.request, urllib.error, socket

WS = r"C:\Users\v_yitcai\WorkBuddy\20260728154244"
KC = os.path.join(WS, "knowledge-collection")
MCP_JSON = os.path.expanduser("~/.workbuddy/mcp.json")
LEXIANG_URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"
SUBFOLDER = "22eea86cd58a46729ed69380092c2c13"

def load_token():
    cfg = json.load(open(MCP_JSON, encoding="utf-8"))
    return cfg["mcpServers"]["lexiang"]["headers"]["Authorization"]

class LexiangMCP:
    def __init__(self, token):
        self.token = token; self.session = None
    def _post(self, payload, retries=7):
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(LEXIANG_URL, data=data, method="POST")
        req.add_header("Content-Type", "application/json")
        req.add_header("Accept", "application/json, text/event-stream")
        req.add_header("Authorization", self.token)
        if self.session: req.add_header("Mcp-Session-Id", self.session)
        last_err = None
        for _ in range(retries):
            try:
                resp = urllib.request.urlopen(req, timeout=25)
                sid = resp.headers.get("mcp-session-id")
                if sid: self.session = sid
                raw = resp.read().decode("utf-8", "replace")
                return self._parse(raw)
            except (urllib.error.HTTPError, socket.error, Exception) as e:
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
        for c in content:
            if c.get("type")=="text":
                try: return json.loads(c.get("text",""))
                except Exception: return {"_raw_text": c.get("text","")}
        return {}

def put_bytes(url, data):
    req = urllib.request.Request(url, data=data, method="PUT")
    req.add_header("Content-Type", "text/html")
    with urllib.request.urlopen(req, timeout=25) as resp:
        return resp.status

def main():
    token = load_token()
    mc = LexiangMCP(token)
    mc.initialize(); mc.initialized()
    # whoami 探活
    try:
        b = mc.biz(mc.call("whoami", {}))
        print("whoami:", json.dumps(b, ensure_ascii=False)[:160])
    except Exception as e:
        print("⚠️ whoami 失败:", str(e)[:120])

    run_path = os.path.join(KC, "openday", "openday-20260823.html")
    run_data = open(run_path, "rb").read()
    run_name = "openday-20260823.html"
    print(f"\n=== 新建独立页 {run_name} ({len(run_data)}B) -> 子文件夹 {SUBFOLDER} ===")
    try:
        r = mc.call("file_apply_upload", {
            "parent_entry_id": SUBFOLDER, "name": run_name, "extension":"html",
            "mime_type":"text/html", "upload_type":"PRE_SIGNED_URL", "size": str(len(run_data)),
        })
        biz = mc.biz(r)
        if biz.get("code") != 0:
            raise RuntimeError(f"apply_upload FAIL {biz.get('message')} | {json.dumps(biz, ensure_ascii=False)[:300]}")
        sess = biz["data"]["session"]
        sid = sess.get("session_id") or sess.get("id")
        url = sess.get("upload_url") or sess["objects"][0]["upload_url"]
        st = put_bytes(url, run_data)
        if st != 200: raise RuntimeError(f"PUT status {st}")
        r2 = mc.call("file_commit_upload", {"session_id": sid})
        biz2 = mc.biz(r2)
        if biz2.get("code") != 0:
            raise RuntimeError(f"commit FAIL {biz2.get('message')}")
        rid = biz2["data"]["entry"]["id"]
        print(f"    OK entry_id={rid} -> https://csig.lexiangla.com/pages/{rid}")
    except Exception as e:
        print(f"    ⚠️ 乐享上传失败（跳过，不重试不中断）: {str(e)[:200]}")
        rid = None

    # 回写 map
    if rid:
        mapf = json.load(open(os.path.join(KC, "lexiang-entry-map.json"), encoding="utf-8"))
        sm = mapf.setdefault("openday", {"folder_id": SUBFOLDER, "wall": {}, "rounds": []})
        sm["folder_id"] = SUBFOLDER
        sm["rounds"].append({
            "round": "r24",
            "date": "2026-08-23", "entry_id": rid, "name": run_name,
            "note": "轮次页 R24 (+6：国企开放日城市级/企业公众开放日/工厂游方法论/车企工业旅游/政府开放月水务/高管间闭门可持续转型·5②1③)"
        })
        json.dump(mapf, open(os.path.join(KC, "lexiang-entry-map.json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=2)
        print(f"=== 完成：独立页已新建，已回写 lexiang-entry-map.json ===")
    else:
        print("=== 乐享上传未成功，跳过 map 回写 ===")

if __name__ == "__main__":
    main()
