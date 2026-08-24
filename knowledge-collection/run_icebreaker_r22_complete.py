# -*- coding: utf-8 -*-
"""破冰 二十二轮「收尾补全」(2026-08-24 晚) — r22 卡片墙+Obsidian 已由早前运行注入，本脚本补全缺失尾步：
1) 用 gen_run_page.py 从既有的 9 张 r22 卡（icebreaker-20260824.html）生成规范化 runs/icebreaker-2026-08-24-r22.html
2) index.json 补齐 r22 的 9 条（按 URL 去重，跳过已存在）
3) GitHub 同步
4) 乐享：累计墙 in-place 更新 + 新建 r22 独立页 + 回写 map
5) last-topic.txt 推进至 颁奖
绝不向累计墙 icebreaker.html 重复注入卡片（已含 r22）。"""
import json, os, re, subprocess, urllib.request, urllib.error

BASE = os.path.dirname(os.path.abspath(__file__))
AT_DIR = os.path.join(BASE, "icebreaker")
CUM = os.path.join(AT_DIR, "icebreaker.html")
RUN_SRC = os.path.join(AT_DIR, "icebreaker-20260824.html")   # 既有 r22 运行页（9 卡，干净无重复）
TMP = os.path.join(AT_DIR, ".run_newcards.tmp.html")
RUN_NAME = "icebreaker-2026-08-24-r22.html"
RUN_PATH = os.path.join(AT_DIR, "runs", RUN_NAME)
IDX = os.path.join(BASE, "index.json")
DATE = "2026-08-24"
ROUND = 22

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---- 1) 从既有 r22 运行页抽取 9 张卡块 ----
raw_src = open(RUN_SRC, encoding="utf-8").read()
cards = []
for m in re.finditer(r'<div class="hl">', raw_src):
    s = m.start(); i = m.end(); d = 1; j = i
    while j < len(raw_src):
        if raw_src[j:j+4] == '<div': d += 1; j += 4
        elif raw_src[j:j+5] == '</div': d -= 1; j += 6
        else: j += 1
        if d == 0: break
    cards.append(raw_src[s:j])
print("从运行页抽取卡块:", len(cards))
open(TMP, "w", encoding="utf-8").write("\n".join(cards))

# ---- 2) gen_run_page.py 生成规范化 runs 页 ----
gen = os.path.join(BASE, "gen_run_page.py")
r = subprocess.run(["python", gen, "--topic", "icebreaker", "--topic-name",
                    "破冰 团队信任", "--date", DATE, "--round", str(ROUND),
                    "--cards-file", TMP, "--out", RUN_PATH], capture_output=True, text=True)
print("gen_run_page:", r.returncode, r.stdout.strip(), (r.stderr.strip()[:300] if r.stderr else ""))

# ---- 3) index.json 补齐 r22 的 9 条 ----
def normkey(t):
    out = []
    for ch in t.lower():
        if ch.isalnum() or "一" <= ch <= "鿿":
            out.append(ch)
    return "".join(out)

def parse_field(card, tag):
    mm = re.search(r'<'+tag+r'[^>]*>(.*?)</'+tag+r'>', card, re.S)
    return mm.group(1).strip() if mm else ""

data = json.load(open(IDX, encoding="utf-8"))
existing_urls = {e.get("url", "").lower().rstrip("/") for e in data}
added = 0
for c in cards:
    title = re.sub(r'<[^>]+>', '', parse_field(c, "h3")).strip()
    mm = re.search(r'href="([^"]+)"', c)
    url = mm.group(1) if mm else ""
    u = url.lower().rstrip("/")
    if not u:
        print("SKIP 无 URL 卡:", title[:30]); continue
    if u in existing_urls:
        print("SKIP 已存在:", u); continue
    rels = []
    if "badge r3" in c: rels.append("r3")
    if "badge r2" in c: rels.append("r2")
    src = "b1" if "badge b1" in c else "b2"
    cat = re.sub(r'<[^>]+>', '', parse_field(c, "span class=\"cat\"".replace('"',''))) if False else ""
    # cat 在 <span class="cat">..</span>
    mc = re.search(r'class="cat">([^<]*)<', c)
    cat = mc.group(1).strip() if mc else ""
    val = re.sub(r'<[^>]+>', '', parse_field(c, "p class=\"val\"".replace('"',''))) if False else ""
    mv = re.search(r'class="val">([\s\S]*?)</p>', c)
    val = re.sub(r'<[^>]+>', '', mv.group(1)).strip() if mv else ""
    entry = {
        "title": title,
        "normKey": normkey(title),
        "url": url,
        "sourceType": "primary" if src == "b1" else "secondary",
        "relation": "exec,supervisor" if len(set(rels)) > 1 else ("exec" if "r3" in rels else "supervisor"),
        "summary": (cat + "：" + val[:60]) if val else cat,
        "topic": "icebreaker",
    }
    data.append(entry); added += 1; existing_urls.add(u)
print("index.json 本轮新增:", added, "-> 现", len(data), "条 (icebreaker 现",
      sum(1 for e in data if e.get("topic") == "icebreaker"), "条)")
json.dump(data, open(IDX, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

# ---- 4) GitHub 同步 ----
sync = os.path.join(os.path.dirname(BASE), "sync_knowledge_github.py")
try:
    rs = subprocess.run(["python", sync], capture_output=True, text=True, timeout=300)
    print("sync_knowledge_github:", rs.returncode, (rs.stdout.strip()[-300:] if rs.stdout else ""),
          (rs.stderr.strip()[:200] if rs.stderr else ""))
except Exception as e:
    print("⚠️ GitHub 同步异常（告警不阻断）：" + str(e)[:200])

# ---- 5) 乐享上传（whoami 探活；累计墙 in-place 更新 + 新建 r22 独立页）----
MCP_JSON = r"C:/Users/v_yitcai/.workbuddy/mcp.json"
LEXIANG_URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"
FOLDER = "f51480b0cfac4857bc28495b151c624f"  # 破冰 子文件夹（待清洗素材下）
WALL_ENTRY = "637b3b31280140349221fbe6fa4e08ed"
WALL_FILE = "3c5c841631e54e1bb56474afc95af1b6"

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
                last = "HTTP {0}: {1}".format(e.code, e.read().decode("utf-8", "replace")[:400]); continue
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
        return self._post({"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"wb-uploader","version":"1.0"}}})
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
            if c.get("type") == "text": text = c.get("text", ""); break
        try: return json.loads(text)
        except Exception: return {"_raw_text": text}

def put_bytes(url, data, retries=3):
    last = None
    for _ in range(retries):
        try:
            req = urllib.request.Request(url, data=data, method="PUT")
            req.add_header("Content-Type", "text/html")
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.status
        except Exception as e:
            last = str(e); continue
    raise RuntimeError("PUT fail: " + str(last))

try:
    token = json.load(open(MCP_JSON, encoding="utf-8"))["mcpServers"]["lexiang"]["headers"]["Authorization"]
    mc = LexiangMCP(token); mc.initialize(); mc.initialized()
    try:
        w = mc.call("whoami", {})
        print("whoami:", json.dumps(mc.biz(w), ensure_ascii=False)[:120])
    except Exception as e:
        print("whoami 跳过:", str(e)[:120])

    # 5a) 累计墙 in-place 更新（现含 r22=202 卡）
    wall_bytes = open(CUM, "rb").read()
    r = mc.call("file_apply_upload", {"parent_entry_id": FOLDER, "name": "icebreaker.html",
                                      "extension":"html", "mime_type":"text/html",
                                      "upload_type":"PRE_SIGNED_URL", "size": str(len(wall_bytes)),
                                      "file_id": WALL_FILE, "entry_id": WALL_ENTRY})
    biz = mc.biz(r)
    if biz.get("code") != 0:
        raise RuntimeError("apply_upload(wall) FAIL {0}".format(biz.get("message")))
    sess = biz["data"]["session"]
    sid = sess.get("session_id") or sess.get("id")
    url = sess.get("upload_url") or sess["objects"][0]["upload_url"]
    st = put_bytes(url, wall_bytes)
    if st != 200: raise RuntimeError("PUT(wall) status " + str(st))
    r2 = mc.call("file_commit_upload", {"session_id": sid})
    biz2 = mc.biz(r2)
    if biz2.get("code") != 0: raise RuntimeError("commit(wall) FAIL " + str(biz2.get("message")))
    print("乐享累计墙 in-place 更新 OK entry_id=", WALL_ENTRY)

    # 5b) 新建 r22 独立页
    run_bytes = open(RUN_PATH, "rb").read()
    r = mc.call("file_apply_upload", {"parent_entry_id": FOLDER, "name": RUN_NAME,
                                      "extension":"html", "mime_type":"text/html",
                                      "upload_type":"PRE_SIGNED_URL", "size": str(len(run_bytes))})
    biz = mc.biz(r)
    if biz.get("code") != 0:
        raise RuntimeError("apply_upload(run) FAIL {0}".format(biz.get("message")))
    sess = biz["data"]["session"]
    sid = sess.get("session_id") or sess.get("id")
    url = sess.get("upload_url") or sess["objects"][0]["upload_url"]
    st = put_bytes(url, run_bytes)
    if st != 200: raise RuntimeError("PUT(run) status " + str(st))
    r2 = mc.call("file_commit_upload", {"session_id": sid})
    biz2 = mc.biz(r2)
    if biz2.get("code") != 0: raise RuntimeError("commit(run) FAIL " + str(biz2.get("message")))
    rid = biz2["data"]["entry"]["id"]
    print("乐享新建独立页 OK entry_id=", rid)

    mapf = json.load(open(os.path.join(BASE, "lexiang-entry-map.json"), encoding="utf-8"))
    sm = mapf.setdefault("icebreaker", {"folder_id": FOLDER, "wall": {}, "rounds": []})
    sm["folder_id"] = FOLDER
    sm["wall"] = {"entry_id": WALL_ENTRY, "file_id": WALL_FILE, "name": "icebreaker.html", "note": "R22 累计墙（202卡）in-place 更新"}
    # 去重：若已记录同名轮次则更新，否则追加
    rec = {"date": DATE, "entry_id": rid, "name": RUN_NAME, "note": "轮次页 R22 (+9)"}
    if not any(x.get("name") == RUN_NAME for x in sm["rounds"]):
        sm["rounds"].append(rec)
    json.dump(mapf, open(os.path.join(BASE, "lexiang-entry-map.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("已回写 lexiang-entry-map.json（wall + rounds）")
except Exception as e:
    print("⚠️ 乐享上传跳过（warning，不中断）：" + str(e)[:300])

# ---- 6) last-topic.txt 推进至 颁奖 ----
lt = os.path.join(BASE, "last-topic.txt")
open(lt, "w", encoding="utf-8").write("颁奖\n")
print("last-topic.txt -> 颁奖")

print("\n=== R22 补全完成：新增 index", added, "条；runs 页", RUN_PATH, "；累计墙", len(open(CUM,encoding='utf-8').read()), "字节 ===")
