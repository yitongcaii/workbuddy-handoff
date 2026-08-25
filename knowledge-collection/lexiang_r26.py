# -*- coding: utf-8 -*-
# Lexiang probe + upload for Open Day r26 (non-fatal; skip on any failure)
import json, os, socket, urllib.request, urllib.error

MCF = r"C:\Users\v_yitcai\.workbuddy\mcp.json"
WS = r"C:\Users\v_yitcai\WorkBuddy\20260728154244"
KC = os.path.join(WS, "knowledge-collection")
WALL = os.path.join(KC, "openday", "openday.html")
RUN  = os.path.join(KC, "openday", "runs", "openday-20260825-r26.html")
FOLDER = "22eea86cd58a46729ed69380092c2c13"      # openday subfolder of 5106d5b2
WALL_ENTRY = "443dbafc774f451792c0687d08815422"
WALL_FILE  = "87d500e4b9764db9bd2595b01fd86b64"
URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"

socket.setdefaulttimeout(25)

def rpc(token, method, params, sid=None, notif=False):
    hdr = {"Authorization": token, "Content-Type": "application/json",
           "Accept": "application/json, text/event-stream"}
    if sid: hdr["Mcp-Session-Id"] = sid
    body = {"jsonrpc": "2.0", "method": method}
    if not notif:
        body["id"] = 1
    if params is not None:
        body["params"] = params
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), headers=hdr, method="POST")
    try:
        r = urllib.request.urlopen(req, timeout=25)
        sid2 = r.headers.get("Mcp-Session-Id", sid)
        txt = r.read().decode("utf-8", "replace")
        return r.status, sid2, txt
    except urllib.error.HTTPError as e:
        return e.code, sid, e.read().decode("utf-8","replace")[:400]
    except Exception as e:
        return -1, sid, f"{type(e).__name__}: {e}"

def whoami(token):
    st, sid, txt = rpc(token, "initialize", {"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"kcp","version":"1.0"}})
    if st != 200:
        return st, sid, f"initialize failed: {txt}"
    st2, sid, _ = rpc(token, "notifications/initialized", {}, sid=sid, notif=True)
    st3, sid, txt3 = rpc(token, "tools/call", {"name":"whoami","arguments":{}}, sid=sid)
    return st3, sid, txt3

def apply_upload(token, sid, parent_entry_id, name, file_id=None):
    args = {"parent_entry_id": parent_entry_id, "name": name}
    if file_id:
        args["file_id"] = file_id
    st, sid, txt = rpc(token, "tools/call", {"name":"file_apply_upload","arguments":args}, sid=sid)
    return st, sid, txt

def put_file(upload_url, path):
    # upload_url is from file_apply_upload objects[0].upload_url (pre-signed COS)
    with open(path, "rb") as f:
        data = f.read()
    req = urllib.request.Request(upload_url, data=data, method="PUT",
                                 headers={"Content-Type":"text/html"})
    try:
        r = urllib.request.urlopen(req, timeout=25)
        return r.status, r.read().decode("utf-8","replace")[:200]
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8","replace")[:300]
    except Exception as e:
        return -1, f"{type(e).__name__}: {e}"

def commit_upload(token, sid, session_id, name):
    st, sid, txt = rpc(token, "tools/call",
        {"name":"file_commit_upload","arguments":{"session_id":session_id,"name":name}},
        sid=sid)
    return st, txt

try:
    m = json.load(open(MCF, encoding="utf-8"))
    token = m["mcpServers"]["lexiang"]["headers"]["Authorization"]
except Exception as e:
    print(f"[skip] cannot read lexiang token: {e}")
    raise SystemExit(0)

print("[probe] whoami ...")
st, sid, txt = whoami(token)
print(f"[probe] whoami status={st}")
print(f"[probe] resp: {txt[:400]}")
if st != 200 or "v_yitcai" not in txt:
    print("[skip] lexiang 未连通（whoami 非成功/未返回 v_yitcai）→ 按告警跳过不阻断。待刷新 mcp.json 乐享 token 后单独补传。")
    raise SystemExit(0)

# connected: update wall in-place + create new round entry
print("[ok] lexiang 连通，开始上传 ...")
# 1) wall in-place
st, sid, atxt = apply_upload(token, sid, FOLDER, "openday.html", file_id=WALL_FILE)
print(f"[wall] apply_upload status={st} resp={atxt[:300]}")
# parse session_id + upload_url
try:
    j = json.loads(atxt)
    # result may be nested: result.content[0].text (JSON) or result.data
    payload = j.get("result", {})
    inner = payload.get("content", [{}])
    inner_txt = inner[0].get("text","") if inner else ""
    inner_j = json.loads(inner_txt) if inner_txt.strip().startswith("{") else payload
    sess = inner_j.get("session_id") or payload.get("session_id")
    up = inner_j.get("objects",[{}])[0].get("upload_url") or payload.get("upload_url")
except Exception as e:
    print(f"[wall] parse error: {e}; resp={atxt[:400]}"); raise SystemExit(0)
st2, p2 = put_file(up, WALL)
print(f"[wall] PUT status={st2}")
st3, c3 = commit_upload(token, sid, sess, "openday.html")
print(f"[wall] commit status={st3} resp={c3[:200]}")

# 2) new round entry (no file_id -> new mode)
st, sid, atxt2 = apply_upload(token, sid, FOLDER, "openday-20260825-r26.html")
print(f"[round] apply_upload status={st} resp={atxt2[:300]}")
try:
    j2 = json.loads(atxt2)
    payload2 = j2.get("result", {})
    inner2 = payload2.get("content",[{}])
    inner_txt2 = inner2[0].get("text","") if inner2 else ""
    inner_j2 = json.loads(inner_txt2) if inner_txt2.strip().startswith("{") else payload2
    sess2 = inner_j2.get("session_id") or payload2.get("session_id")
    up2 = inner_j2.get("objects",[{}])[0].get("upload_url") or payload2.get("upload_url")
except Exception as e:
    print(f"[round] parse error: {e}; resp={atxt2[:400]}"); raise SystemExit(0)
st4, p4 = put_file(up2, RUN)
print(f"[round] PUT status={st4}")
st5, c5 = commit_upload(token, sid, sess2, "openday-20260825-r26.html")
print(f"[round] commit status={st5} resp={c5[:200]}")
print("[done] lexiang 上传完成（墙 in-place + 当轮独立页新建）。")
