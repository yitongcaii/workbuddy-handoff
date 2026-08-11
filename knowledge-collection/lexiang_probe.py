#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, json, urllib.request, urllib.error
WS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MCP_JSON = os.path.expanduser("~/.workbuddy/mcp.json")
LEXIANG_URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"
def load_token():
    cfg = json.load(open(MCP_JSON, encoding="utf-8"))
    return cfg["mcpServers"]["lexiang"]["headers"]["Authorization"]
class MC:
    def __init__(self, t): self.token=t; self.session=None
    def _post(self, p, retries=2):
        d=json.dumps(p).encode("utf-8")
        req=urllib.request.Request(LEXIANG_URL,data=d,method="POST")
        req.add_header("Content-Type","application/json")
        req.add_header("Accept","application/json, text/event-stream")
        req.add_header("Authorization",self.token)
        if self.session: req.add_header("Mcp-Session-Id",self.session)
        last=None
        for _ in range(retries):
            try:
                resp=urllib.request.urlopen(req,timeout=120)
                sid=resp.headers.get("mcp-session-id")
                if sid: self.session=sid
                raw=resp.read().decode("utf-8","replace"); return self._parse(raw)
            except urllib.error.HTTPError as e:
                last=f"HTTP {e.code}: {e.read().decode('utf-8','replace')[:400]}"; continue
            except Exception as e: last=str(e); continue
        raise RuntimeError(f"POST fail: {last}")
    def _parse(self, raw):
        raw=raw.strip()
        if raw.startswith("data:"):
            txt=[l[5:].strip() for l in raw.splitlines() if l.startswith("data:")]; raw="\n".join(txt)
        try: return json.loads(raw)
        except Exception: return json.loads(raw[raw.find("{"):])
    def init(self):
        return self._post({"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"wb","version":"1.0"}}})
    def initialized(self):
        try: self._post({"jsonrpc":"2.0","method":"notifications/initialized"})
        except Exception: pass
    def call(self,n,a):
        return self._post({"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":n,"arguments":a}})
    def biz(self,r):
        res=r.get("result")
        if not res: raise RuntimeError(json.dumps(r,ensure_ascii=False)[:300])
        c=res.get("content") or []
        for x in c:
            if x.get("type")=="text":
                try: return json.loads(x.get("text",""))
                except Exception: return {"_raw":x.get("text","")}
        return {}
def list_children(mc, pid, token=None):
    args={"parent_id":pid}
    if token: args["page_token"]=token
    r=mc.call("entry_list_children", args)
    return mc.biz(r)
def main():
    mc=MC(load_token()); mc.init(); mc.initialized()
    # 取新建累计墙的 file_id 供后续 in-place 更新
    EID="f06a4c5394df4b458ffeb9dff42653ba"
    for tool,arg in [("entry_describe_entry",{"entry_id":EID}),("file_describe_file",{"entry_id":EID})]:
        print(f"\n=== {tool} ===")
        b=mc.biz(mc.call(tool,arg))
        print(json.dumps(b,ensure_ascii=False)[:900])
    targets={
        "待清洗素材(root)":"5106d5b2decc442780c1cae5014c6fb6",
        "icebreaker子文件夹":"f51480b0cfac4857bc28495b151c624f",
        "归档":"da1a6240994a44d686a76dcbd9bd9d60",
    }
    for name,pid in targets.items():
        print(f"\n===== {name} ({pid}) =====")
        tok=None; n=0
        while True:
            b=list_children(mc, pid, tok)
            if b.get("code")!=0:
                print("  ERR:", b.get("message")); break
            items=b.get("data",{}).get("entries") or b.get("data",{}).get("list") or []
            if not items: 
                print("  (空或无 entries 字段)"); break
            for it in items:
                print(f"  - {it.get('id')}  | name={it.get('name')}  | type={it.get('entry_type') or it.get('type')}")
                n+=1
            tok=b.get("data",{}).get("next_page_token")
            if not tok: break
        print(f"  total listed: {n}")
if __name__=="__main__":
    main()
