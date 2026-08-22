# -*- coding: utf-8 -*-
import json, urllib.request, urllib.error
MCP_JSON = os.path.expanduser("~/.workbuddy/mcp.json") if False else r"C:/Users/v_yitcai/.workbuddy/mcp.json"
LEXIANG_URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"
FOLDER = "463f5f5387de4a9bb87b773aef79767b"

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
                last = "HTTP {0}: {1}".format(e.code, e.read().decode("utf-8","replace")[:400]); continue
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
        return self._post({"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"wb-probe","version":"1.0"}}})
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
            if c.get("type") == "text": text = c.get("text",""); break
        try: return json.loads(text)
        except Exception: return {"_raw_text": text}

token = json.load(open(MCP_JSON, encoding="utf-8"))["mcpServers"]["lexiang"]["headers"]["Authorization"]
mc = LexiangMCP(token)
mc.initialize(); mc.initialized()
try:
    w = mc.call("whoami", {})
    print("whoami:", json.dumps(mc.biz(w), ensure_ascii=False)[:120])
except Exception as e:
    print("whoami err:", str(e)[:120])

# list children of offsite folder
r = mc.call("entry_list_children", {"parent_id": FOLDER, "limit": 100})
biz = mc.biz(r)
print("code:", biz.get("code"), "msg:", biz.get("message"))
data = biz.get("data") or {}
entries = data.get("entries") or data.get("list") or []
print("next_page_token:", data.get("next_page_token"))
print("=== entries (id | name | extension | type) ===")
for e in entries:
    print(e.get("id"), "|", e.get("name"), "|", e.get("extension"), "|", e.get("type"))
