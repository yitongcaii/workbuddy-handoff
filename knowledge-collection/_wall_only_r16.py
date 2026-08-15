# -*- coding: utf-8 -*-
"""仅更新累计墙（修复 hero 计数 +107 -> +11 后重新上传），不新建轮次页。"""
import os, json, urllib.request, urllib.error

WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KC = os.path.join(WS, "knowledge-collection")
MCP_JSON = os.path.expanduser("~/.workbuddy/mcp.json")
LEXIANG_URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"
WALL_ENTRY = "f3b5ea59395e49ca859f8726142742c2"
WALL_FILE  = "a1415122f8034d8d988fb06e41be44ac"

def load_token():
    return json.load(open(MCP_JSON, encoding="utf-8"))["mcpServers"]["lexiang"]["headers"]["Authorization"]

class MC:
    def __init__(self, token): self.token=token; self.session=None
    def _post(self, p, retries=2):
        data=json.dumps(p).encode(); req=urllib.request.Request(LEXIANG_URL,data=data,method="POST")
        req.add_header("Content-Type","application/json"); req.add_header("Accept","application/json, text/event-stream")
        req.add_header("Authorization",self.token)
        if self.session: req.add_header("Mcp-Session-Id",self.session)
        for _ in range(retries):
            try:
                r=urllib.request.urlopen(req,timeout=120); sid=r.headers.get("mcp-session-id")
                if sid: self.session=sid
                return self._parse(r.read().decode("utf-8","replace"))
            except Exception as e: last=str(e); continue
        raise RuntimeError(last)
    def _parse(self,raw):
        raw=raw.strip()
        if raw.startswith("data:"): raw="\n".join(l[5:].strip() for l in raw.splitlines() if l.startswith("data:"))
        try: return json.loads(raw)
        except Exception: return json.loads(raw[raw.find("{"):])
    def initialize(self): self._post({"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"wb","version":"1.0"}}})
    def initialized(self):
        try: self._post({"jsonrpc":"2.0","method":"notifications/initialized"})
        except Exception: pass
    def call(self,n,a): return self._post({"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":n,"arguments":a}})
    def biz(self,r):
        res=r.get("result")
        if not res: raise RuntimeError("no result")
        for c in (res.get("content") or []):
            if c.get("type")=="text":
                try: return json.loads(c.get("text",""))
                except Exception: return {"_raw":c.get("text","")}

def put_bytes(url,data):
    req=urllib.request.Request(url,data=data,method="PUT"); req.add_header("Content-Type","text/html")
    return urllib.request.urlopen(req,timeout=120).status

mc=MC(load_token()); mc.initialize(); mc.initialized()
mc.biz(mc.call("whoami",{}))
data=open(os.path.join(KC,"staff-meeting","staff-meeting.html"),"rb").read()
r=mc.call("file_apply_upload",{"file_id":WALL_FILE,"parent_entry_id":WALL_ENTRY,"name":"staff-meeting.html","mime_type":"text/html","size":str(len(data)),"upload_type":"PRE_SIGNED_URL"})
b=mc.biz(r)
sess=b["data"]["session"]; sid=sess.get("session_id") or sess.get("id")
url=sess.get("upload_url") or sess["objects"][0]["upload_url"]
print("PUT status", put_bytes(url,data))
b2=mc.biz(mc.call("file_commit_upload",{"session_id":sid}))
print("commit code", b2.get("code"), "entry", b2.get("data",{}).get("entry",{}).get("id"))
