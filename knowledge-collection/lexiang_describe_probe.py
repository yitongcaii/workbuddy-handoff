#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, json, urllib.request, urllib.error
MCP_JSON = os.path.expanduser("~/.workbuddy/mcp.json")
LEXIANG_URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"
def tok():
    c=json.load(open(MCP_JSON,encoding="utf-8"));return c["mcpServers"]["lexiang"]["headers"]["Authorization"]
class MC:
    def __init__(s,t):s.token=t;s.session=None
    def _post(s,p,retries=2):
        d=json.dumps(p).encode();req=urllib.request.Request(LEXIANG_URL,data=d,method="POST")
        req.add_header("Content-Type","application/json");req.add_header("Accept","application/json, text/event-stream")
        req.add_header("Authorization",s.token)
        if s.session:req.add_header("Mcp-Session-Id",s.session)
        last="unknown"
        for _ in range(retries):
            try:
                r=urllib.request.urlopen(req,timeout=120);sid=r.headers.get("mcp-session-id")
                if sid:s.session=sid;return s._parse(r.read().decode("utf-8","replace"))
            except Exception as e: last=str(e)
        raise RuntimeError(f"POST fail: {last}")
    def _parse(s,raw):
        raw=raw.strip()
        if raw.startswith("data:"):
            t=[l[5:].strip() for l in raw.splitlines() if l.startswith("data:")];raw="\n".join(t)
        try:return json.loads(raw)
        except Exception:return json.loads(raw[raw.find("{"):])
    def init(s):return s._post({"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"wb","version":"1.0"}}})
    def initialized(s):
        try:s._post({"jsonrpc":"2.0","method":"notifications/initialized"})
        except Exception:pass
    def call(s,n,a):return s._post({"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":n,"arguments":a}})
    def biz(s,r):
        res=r.get("result")
        if not res:return {"_err":json.dumps(r,ensure_ascii=False)[:200]}
        for x in res.get("content") or []:
            if x.get("type")=="text":
                try:return json.loads(x.get("text",""))
                except Exception:return {"_raw":x.get("text","")}
        return {}
mc=MC(tok());mc.init();mc.initialized()
EID="f06a4c5394df4b458ffeb9dff42653ba"
for tool,arg in [("entry_describe_entry",{"entry_id":EID}),("file_describe_file",{"entry_id":EID})]:
    print(f"\n=== {tool} ===")
    b=mc.biz(mc.call(tool,arg))
    print(json.dumps(b,ensure_ascii=False)[:900])
