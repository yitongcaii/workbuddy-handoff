# -*- coding: utf-8 -*-
"""r40 lexiang 实调：initialize -> whoami 探活；通则更新墙 + 新建当轮独立页。"""
import json, urllib.request, urllib.error

URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"
TOKEN = "lxmcp_1b82fcd9c11ff51ea657ee591e793c39825fb1748510b241ab29443a1106b708"

def post(session, payload, raw=False):
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(URL, data=data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('Accept', 'application/json, text/event-stream')
    req.add_header('Authorization', 'Bearer ' + TOKEN)
    if session:
        req.add_header('Mcp-Session-Id', session)
    try:
        resp = urllib.request.urlopen(req, timeout=25)
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', 'ignore')
        return None, e.code, body
    except Exception as e:
        return None, 0, str(e)
    sid = resp.headers.get('Mcp-Session-Id')
    txt = resp.read().decode('utf-8', 'ignore')
    if raw:
        return txt, resp.status, sid
    # parse SSE or json
    out = None
    if txt.strip().startswith('{'):
        out = json.loads(txt)
    else:
        # SSE: take last event data
        for line in txt.splitlines():
            if line.startswith('data:'):
                try:
                    out = json.loads(line[5:].strip())
                except: pass
    return out, resp.status, sid

def main():
    # 1. initialize
    r, code, sid = post(None, {
        "jsonrpc": "2.0", "id": 1, "method": "initialize",
        "params": {"protocolVersion": "2024-11-05", "capabilities": {},
                   "clientInfo": {"name": "kb-probe", "version": "1.0"}}
    })
    print("INIT code:", code, "sid:", (sid or '')[:20])
    if code != 200 or not r:
        print("INIT FAIL:", str(r)[:300])
        return False
    # 2. initialized notification
    post(sid, {"jsonrpc": "2.0", "method": "notifications/initialized", "params": {}})
    # 3. whoami 探活 (try common tool names)
    for tname in ["whoami", "lexiang_whoami", "mcp__lexiang__whoami"]:
        r2, c2, _ = post(sid, {
            "jsonrpc": "2.0", "id": 2, "method": "tools/call",
            "params": {"name": tname, "arguments": {}}
        })
        print(f"WHOAMI [{tname}] code={c2}")
        if c2 == 200 and r2:
            print("  result:", json.dumps(r2, ensure_ascii=False)[:400])
            return True
    print("WHOAMI: no tool responded 200")
    return False

if __name__ == '__main__':
    ok = main()
    print("WHOAMI_OK" if ok else "WHOAMI_FAIL")
