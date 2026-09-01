# -*- coding: utf-8 -*-
import json, os, sys, urllib.request, urllib.error, socket, time

URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"
TOKEN = "lxmcp_1b82fcd9c11ff51ea657ee591e793c39825fb1748510b241ab29443a1106b708"
FOLDER = "f51480b0cfac4857bc28495b151c624f"
FILE = "c:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection/icebreaker/icebreaker-20260901.html"
NAME = "icebreaker-20260901.html"
MAP = "c:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection/lexiang-entry-map.json"

socket.setdefaulttimeout(25)
SIZE = os.path.getsize(FILE)
print("file bytes =", SIZE)

def rpc(method, params=None, notif=False, session_id=None, rid=1):
    body = {"jsonrpc":"2.0","method":method}
    if not notif:
        body["id"] = rid
    if params is not None:
        body["params"] = params
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(URL, data=data, method="POST")
    req.add_header("Content-Type","application/json")
    req.add_header("Accept","application/json, text/event-stream")
    req.add_header("Authorization","Bearer "+TOKEN)
    if session_id:
        req.add_header("Mcp-Session-Id", session_id)
    for attempt in range(3):
        try:
            resp = urllib.request.urlopen(req)
            sid = resp.headers.get("Mcp-Session-Id", session_id)
            raw = resp.read().decode("utf-8","replace")
            return sid, raw
        except urllib.error.HTTPError as e:
            print("HTTPError", e.code, e.read().decode("utf-8","replace")[:300])
            return None, "HTTPERROR:%d" % e.code
        except Exception as e:
            print("net err attempt", attempt, repr(e))
            time.sleep(2)
    return None, "NETFAIL"

def parse_text_result(raw):
    # streamable-http may return JSON or SSE; try JSON then SSE
    raw = raw.strip()
    if raw.startswith("event:") or raw.startswith("data:"):
        for line in raw.splitlines():
            if line.startswith("data:"):
                raw = line[5:].strip(); break
    try:
        obj = json.loads(raw)
    except Exception:
        return None
    # result.content[0].text  OR  result.data
    res = obj.get("result")
    if not res:
        return obj
    if "content" in res and res["content"]:
        t = res["content"][0].get("text")
        try: return json.loads(t)
        except Exception: return t
    if "data" in res:
        return res["data"]
    return res

# 1) initialize
sid, raw = rpc("initialize", {
    "protocolVersion":"2024-11-05",
    "capabilities":{},
    "clientInfo":{"name":"wb-auto","version":"1.0"}
})
print("init sid:", sid, "raw head:", raw[:160])
if sid is None:
    print("WARN lexiang init failed -> skip upload")
    sys.exit(7)
# 2) initialized notification
rpc("notifications/initialized", notif=True, session_id=sid)
# 3) file_apply_upload
sid, raw = rpc("tools/call", {"name":"file_apply_upload","arguments":{
    "parent_entry_id":FOLDER,
    "name":NAME,
    "extension":"html",
    "mime_type":"text/html",
    "upload_type":"PRE_SIGNED_URL",
    "size":SIZE
}}, session_id=sid, rid=2)
print("apply raw head:", raw[:400])
apply = parse_text_result(raw)
if not apply or "session_id" not in str(apply):
    print("WARN file_apply_upload failed -> skip. apply=", str(apply)[:300])
    sys.exit(7)
info = apply if isinstance(apply, dict) else {}
session_id = info.get("session_id") or info.get("data",{}).get("session_id")
upload_url = None
ob = info.get("objects") or info.get("data",{}).get("objects")
if ob:
    upload_url = ob[0].get("upload_url")
if not session_id or not upload_url:
    print("WARN cannot extract session_id/upload_url -> skip. info=", str(info)[:400])
    sys.exit(7)
print("session_id:", session_id, "upload_url:", upload_url[:80], "...")
# 4) PUT file bytes
fb = open(FILE,"rb").read()
assert len(fb) == SIZE, "byte mismatch"
preq = urllib.request.Request(upload_url, data=fb, method="PUT")
preq.add_header("Content-Type","text/html")
for attempt in range(3):
    try:
        pr = urllib.request.urlopen(preq)
        print("PUT status:", pr.status)
        break
    except Exception as e:
        print("PUT err attempt", attempt, repr(e))
        time.sleep(2)
else:
    print("WARN PUT failed -> skip")
    sys.exit(7)
# 5) file_commit_upload
sid, raw = rpc("tools/call", {"name":"file_commit_upload","arguments":{"session_id":session_id}}, session_id=sid, rid=3)
print("commit raw head:", raw[:400])
commit = parse_text_result(raw)
entry_id = None
if isinstance(commit, dict):
    entry_id = commit.get("entry_id") or commit.get("data",{}).get("entry_id") or commit.get("file_id")
print("entry_id:", entry_id)

# update map
mp = json.load(open(MAP, encoding="utf-8"))
mp["icebreaker"]["rounds"].append({"date":"2026-09-01","entry_id":entry_id,"name":NAME,
    "note":"轮次页 R26 (+9：高管入职书面领导宪章/C-Suite授权书/高管入职初见+信任工作坊（③）；越级会谈HR官方手册(一手)/问题银行/议程20问+中层不在场/新经理入职清单/首场员工会45min/新团队首会6要素（②）｜乐享文件上传" if entry_id else "轮次页 R26 (+9)｜上传待补(token/网络，待重连乐享后补传并回填 entry_id)"})
json.dump(mp, open(MAP,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
print("map updated, entry_id=", entry_id)
print("OK" if entry_id else "WARN_NO_ENTRY_ID")
