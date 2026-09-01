# -*- coding: utf-8 -*-
"""乐享同步 · 员工大会 r30（自动化 step 10）
- whoami 探活（不依赖连接器状态面板）
- 更新累计墙 staff-meeting.html（in-place update）
- 新建独立轮次页 staff-meeting-2026-09-02-r30.html（落 员工大会 子文件夹 a753a4eb）
- 回填 lexiang-entry-map.json
非阻塞：whoami 失败则告警跳过、不抛异常。
"""
import json, os, sys, time, socket, urllib.request, urllib.error

WS = r"C:\Users\v_yitcai\WorkBuddy\20260728154244"
KC = os.path.join(WS, "knowledge-collection")
ROOT = "5106d5b2decc442780c1cae5014c6fb6"          # 待清洗素材（根）
STAFF_FOLDER = "a753a4ebc526495c9e9b2e2fb3cac314"  # 员工大会 子文件夹（map 权威）
WALL_FILE_ID = "a1415122f8034d8d988fb06e41be44ac"
WALL_ENTRY_ID = "f3b5ea59395e49ca859f8726142742c2"
WALL_NAME = "staff-meeting.html"
RUN_NAME = "staff-meeting-2026-09-02-r30.html"
ROUND_DATE = "2026-09-02"

TOKEN = "lxmcp_1b82fcd9c11ff51ea657ee591e793c39825fb1748510b241ab29443a1106b708"
BASE = "https://mcp.lexiang-app.com/mcp?company_from=csig"
HEADERS = {
    "Authorization": "Bearer " + TOKEN,
    "Content-Type": "application/json",
    "Accept": "application/json, text/event-stream",
}
_session_id = [None]
_req_id = [0]

log = []
def L(*a):
    s = " ".join(str(x) for x in a)
    log.append(s)
    print(s, flush=True)

def rpc(method, params=None, is_notification=False):
    _req_id[0] += 1
    body = {"jsonrpc": "2.0", "method": method}
    if not is_notification:
        body["id"] = _req_id[0]
    if params is not None:
        body["params"] = params
    data = json.dumps(body).encode("utf-8")
    last = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(BASE, data=data, method="POST")
            for k, v in HEADERS.items():
                req.add_header(k, v)
            if _session_id[0]:
                req.add_header("Mcp-Session-Id", _session_id[0])
            resp = urllib.request.urlopen(req, timeout=25)
            sid = resp.headers.get("Mcp-Session-Id") or resp.headers.get("mcp-session-id")
            if sid:
                _session_id[0] = sid
            raw = resp.read().decode("utf-8", "replace")
            ctype = resp.headers.get("Content-Type", "")
            return parse_resp(raw, ctype)
        except Exception as e:
            last = e
            L(f"  ! rpc {method} attempt {attempt+1} 失败: {e}")
            time.sleep(1.2)
    raise last

def parse_resp(raw, ctype):
    if "text/event-stream" in ctype:
        out = None
        for line in raw.splitlines():
            line = line.strip()
            if line.startswith("data:"):
                payload = line[5:].strip()
                if payload and payload != "[DONE]":
                    try:
                        out = json.loads(payload)
                    except Exception:
                        pass
        return out
    try:
        return json.loads(raw)
    except Exception:
        return None

def call_tool(name, args=None):
    resp = rpc("tools/call", {"name": name, "arguments": args or {}})
    if resp is None:
        return None
    if "error" in resp and resp.get("error"):
        raise RuntimeError(f"tool {name} error: {resp['error']}")
    return resp.get("result")

# 兼容两种返回形态：result.data（结构化） 或 result.content[0].text（JSON 文本）
def get_struct(result):
    if result is None:
        return None
    if isinstance(result, dict) and "data" in result and not isinstance(result.get("content"), list):
        return result["data"]
    # content[0].text -> JSON 文本
    content = result.get("content")
    if isinstance(content, list):
        for c in content:
            if isinstance(c, dict) and c.get("type") == "text" and c.get("text"):
                try:
                    return json.loads(c["text"])
                except Exception:
                    return c["text"]
    if "data" in result:
        return result["data"]
    return result

def put_file(url, body_bytes, ctype="text/html"):
    req = urllib.request.Request(url, data=body_bytes, method="PUT")
    req.add_header("Content-Type", ctype)
    req.add_header("Content-Length", str(len(body_bytes)))
    resp = urllib.request.urlopen(req, timeout=30)
    return resp.status, resp.read()

def list_children(parent_id, max_pages=20):
    items = []
    token = None
    for _ in range(max_pages):
        args = {"parent_id": parent_id}
        if token:
            args["page_token"] = token
        res = call_tool("entry_list_children", args)
        data = get_struct(res) or {}
        for e in (data.get("entries") or []):
            items.append(e)
        token = data.get("next_page_token")
        if not token:
            break
    return items

def main():
    L("== 乐享 sync · 员工大会 r30 ==")
    # 1) initialize
    try:
        init = rpc("initialize", {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "wb-auto", "version": "1.0"},
        })
        L("initialize:", "ok" if init else "no-resp")
        rpc("notifications/initialized", is_notification=True)
    except Exception as e:
        L("initialize 失败:", e)
        return {"ok": False, "step": "initialize", "err": str(e)}

    # 2) whoami 探活
    try:
        who = call_tool("whoami", {})
        L("whoami:", who)
        if who is None:
            L("⚠️ whoami 返回空 -> 视为断开，跳过（非阻断）")
            return {"ok": False, "step": "whoami", "err": "empty"}
    except Exception as e:
        L("⚠️ whoami 失败 -> 断开，跳过（非阻断）:", e)
        return {"ok": False, "step": "whoami", "err": str(e)}

    # 3) 读取本地 HTML
    wall_path = os.path.join(KC, "staff-meeting", "staff-meeting.html")
    run_path = os.path.join(KC, "staff-meeting", "runs", RUN_NAME)
    wall_bytes = open(wall_path, "rb").read()
    run_bytes = open(run_path, "rb").read()
    L(f"wall bytes={len(wall_bytes)}  run bytes={len(run_bytes)}")

    # 4) 定位 staff-meeting 子文件夹（校验 map）
    root_items = list_children(ROOT)
    L(f"root 待清洗素材 children={len(root_items)}")
    folder = None
    for e in root_items:
        if e.get("id") == STAFF_FOLDER or (e.get("name") or "").find("员工大会") >= 0:
            folder = e
            break
    if folder is None:
        L(f"⚠️ 未在根下找到 员工大会 子文件夹（map={STAFF_FOLDER}），尝试直接用 map folder_id")
    else:
        L(f"staff-meeting 子文件夹: id={folder.get('id')} name={folder.get('name')}")

    # 5) 定位墙 entry（校验 map）
    folder_id = folder["id"] if folder else STAFF_FOLDER
    items = list_children(folder_id)
    wall_entry = None
    for e in items:
        nm = (e.get("name") or "")
        if nm == "staff-meeting" or e.get("id") == WALL_ENTRY_ID:
            wall_entry = e
            break
    if wall_entry is None:
        L(f"⚠️ 子文件夹内未找到墙 entry，回退 map ids: file={WALL_FILE_ID} entry={WALL_ENTRY_ID}")
        wall_entry = {"id": WALL_ENTRY_ID, "file_id": WALL_FILE_ID, "name": "staff-meeting"}
    else:
        L(f"wall entry: id={wall_entry.get('id')} file_id={wall_entry.get('file_id')} name={wall_entry.get('name')}")

    # 6) 更新墙（update 模式）
    try:
        up = call_tool("file_apply_upload", {
            "file_id": wall_entry.get("file_id") or WALL_FILE_ID,
            "parent_entry_id": wall_entry.get("id"),
            "name": WALL_NAME,
            "extension": "html",
            "mime_type": "text/html",
            "upload_type": "PRE_SIGNED_URL",
        })
        up_data = get_struct(up) or {}
        # 兼容 data.session / data.objects
        sess = up_data.get("session") or {}
        session_id = sess.get("session_id")
        upload_url = sess.get("upload_url")
        if not upload_url and up_data.get("objects"):
            upload_url = (up_data["objects"][0] or {}).get("upload_url")
        L(f"apply_upload(update) session_id={session_id} upload_url?={'Y' if upload_url else 'N'}")
        if not (session_id and upload_url):
            raise RuntimeError("update 未能获取 session_id/upload_url: " + json.dumps(up_data, ensure_ascii=False)[:300])
        st, _ = put_file(upload_url, wall_bytes)
        L(f"PUT wall -> HTTP {st}")
        cm = call_tool("file_commit_upload", {"session_id": session_id})
        L("commit update:", "ok" if cm else "no-resp")
    except Exception as e:
        L("⚠️ 墙更新失败:", e)
        return {"ok": False, "step": "update_wall", "err": str(e)}

    # 7) 新建独立轮次页（create 模式）
    try:
        cr = call_tool("file_apply_upload", {
            "parent_entry_id": folder_id,
            "name": RUN_NAME,
            "extension": "html",
            "mime_type": "text/html",
            "upload_type": "PRE_SIGNED_URL",
        })
        cr_data = get_struct(cr) or {}
        sess = cr_data.get("session") or {}
        session_id = sess.get("session_id")
        upload_url = sess.get("upload_url")
        if not upload_url and cr_data.get("objects"):
            upload_url = (cr_data["objects"][0] or {}).get("upload_url")
        L(f"apply_upload(create) session_id={session_id} upload_url?={'Y' if upload_url else 'N'}")
        if not (session_id and upload_url):
            raise RuntimeError("create 未能获取 session_id/upload_url: " + json.dumps(cr_data, ensure_ascii=False)[:300])
        st, _ = put_file(upload_url, run_bytes)
        L(f"PUT run -> HTTP {st}")
        cm = call_tool("file_commit_upload", {"session_id": session_id})
        # 取新 entry id（commit 可能回传，否则重新 list 取最新）
        run_entry_id = None
        cm_struct = get_struct(cm)
        if isinstance(cm_struct, dict):
            run_entry_id = cm_struct.get("entry_id") or cm_struct.get("id") or (cm_struct.get("data") or {}).get("entry_id")
        if not run_entry_id:
            # 重新 list 子文件夹取最新一条同名
            items2 = list_children(folder_id)
            for e in items2:
                if (e.get("name") or "") == RUN_NAME.replace(".html", ""):
                    run_entry_id = e.get("id")
                    break
        L(f"run page entry_id={run_entry_id}")
    except Exception as e:
        L("⚠️ 轮次页新建失败:", e)
        return {"ok": False, "step": "create_run", "err": str(e)}

    # 8) 回填 map
    try:
        map_path = os.path.join(KC, "lexiang-entry-map.json")
        mp = json.load(open(map_path, "r", encoding="utf-8"))
        rec = mp.setdefault("staff-meeting", {})
        rounds = rec.setdefault("rounds", [])
        rounds.append({
            "date": ROUND_DATE,
            "entry_id": run_entry_id,
            "name": RUN_NAME,
            "note": "轮次页 R30（+7）｜乐享新建模式，落 员工大会 子文件夹 a753a4eb",
        })
        # 更新墙记录
        rec["wall"] = {
            "entry_id": wall_entry.get("id"),
            "file_id": wall_entry.get("file_id") or WALL_FILE_ID,
            "name": WALL_NAME,
            "note": "R30 累计墙（323卡）in-place 更新",
        }
        json.dump(mp, open(map_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        L("OK map 回填完成")
    except Exception as e:
        L("⚠️ map 回填失败:", e)
        return {"ok": False, "step": "map", "err": str(e)}

    L("== 乐享 sync 完成 ==")
    return {"ok": True, "run_entry_id": run_entry_id, "wall_entry_id": wall_entry.get("id")}

if __name__ == "__main__":
    socket.setdefaulttimeout(25)
    try:
        res = main()
    except Exception as e:
        res = {"ok": False, "fatal": str(e)}
        L("FATAL:", e)
    L("RESULT=" + json.dumps(res, ensure_ascii=False))
    sys.exit(0)
