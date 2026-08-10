#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Push latest 6 HTML walls (with KM cards, pruned) to 乐享 待清洗素材 folder.
Update-in-place mode: use entry_id as parent_entry_id AND target file_id.
Steps: apply_upload -> PUT bytes -> commit_upload.
"""
import os, sys, json, urllib.request

BASE = os.path.dirname(os.path.abspath(__file__))
FOLDER = "5106d5b2decc442780c1cae5014c6fb6"

# (rel_path, entry_id (parent_entry_id for update), target_id (file_id))
TARGETS = {
    "staff-meeting": ("staff-meeting/staff-meeting.html", "af3113ee47b14b74a76d9b057bfe244c", "2e59bcaeb4b34c6494b90cbaaae5bdac"),
    "offsite":       ("offsite/offsite.html",            "21975983edbb44208260c10cc89f5925", "d7d973f143404cf48f9e4d8c9388a5ad"),
    "icebreaker":    ("icebreaker/icebreaker.html",      "93fd6bf9d0884ee48f62dfbce65166a1", "ae23e8f2972b45eaae1995ddeba4f48b"),
    "award":         ("award/award.html",                "bafb696e49254f779476a1f167850904", "f0c8d2533a4246b68e327cc2b5ffa722"),
    "afternoontea":  ("afternoontea/afternoontea.html",  "a5c7f6e57c2744688f16f117659c0d77", "5faeedc268e24b449a512103eef37c16"),
    "openday":       ("openday/openday.html",            "460133b55d6542bda6e00fa7ec0fc6bc", "85668f7859b64e1eb1cdec1420a04b81"),
}

def mcp(tool, params):
    import subprocess
    NODEBIN = "C:/Users/v_yitcai/.workbuddy/binaries/node/versions/22.22.2"
    cmd = [f"{NODEBIN}/mcporter.cmd", "call", f"lexiang.{tool}({json.dumps(params, ensure_ascii=False)})"]
    out = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", timeout=120)
    txt = out.stdout + out.stderr
    try:
        return json.loads(txt)
    except Exception:
        # try extract first {...}
        s = txt.find("{"); e = txt.rfind("}")
        if s >= 0 and e > s:
            return json.loads(txt[s:e+1])
        raise RuntimeError(f"parse fail {tool}: {txt[:300]}")

def main():
    for theme, (rel, entry_id, file_id) in TARGETS.items():
        path = os.path.join(BASE, rel)
        data = open(path, "rb").read()
        size = len(data)
        print(f"\n=== {theme} ({size} bytes) ===")
        # 1) apply_upload (update mode: name MUST carry .html extension, NO extension field)
        r = mcp("file_apply_upload", {
            "file_id": file_id,
            "parent_entry_id": entry_id,
            "name": theme + ".html",
            "mime_type": "text/html",
            "size": str(size),
            "upload_type": "PRE_SIGNED_URL",
        })
        if r.get("code") != 0:
            print("  apply_upload FAIL:", r.get("message")); continue
        sess = r["data"]["session"]
        sid = sess["id"]; url = sess["upload_url"]
        # 2) PUT
        req = urllib.request.Request(url, data=data, method="PUT")
        req.add_header("Content-Type", "text/html")
        with urllib.request.urlopen(req, timeout=120) as resp:
            print("  PUT:", resp.status)
        # 3) commit
        r2 = mcp("file_commit_upload", {"session_id": sid})
        if r2.get("code") == 0:
            eid = r2["data"]["entry"]["id"]
            print(f"  commit OK -> https://csig.lexiangla.com/pages/{eid}")
        else:
            print("  commit FAIL:", r2.get("message"))

if __name__ == "__main__":
    main()
