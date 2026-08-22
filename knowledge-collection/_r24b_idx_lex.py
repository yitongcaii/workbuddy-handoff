# -*- coding: utf-8 -*-
# 下午茶研讨 R24 收尾：仅 00-索引 + 乐享上传（笔记已先行完成）。
import json, os, re, urllib.request, urllib.error

BASE = os.path.dirname(os.path.abspath(__file__))
AT_DIR = os.path.join(BASE, "afternoontea")
DATE = "20260822"
RUN_NAME = "afternoontea-20260822b.html"
RUN_PATH = os.path.join(AT_DIR, RUN_NAME)

CARDS = [
    ("盐城港集团「总经理接待日」·心声有回声","一手","②上下级"),
    ("中国诚通「书记接待日」·建账督办十五五建言","一手","②上下级"),
    ("悦达汽车「党委书记、工会主席接待日」座谈会","一手","②上下级"),
    ("大唐甘肃「书记接待日」·开门教育连心桥","一手","②上下级"),
    ("索普集团职工恳谈会·30年闭环制度","二手","②上下级"),
    ("亚太森博「厂长沟通会」·季度直面一线","二手","②上下级"),
    ("CEO 同侪顾问小组深度指南·孤独决策破局","二手","③高管间"),
]
REL_TXT = {"②上下级":"②上下级","③高管间":"③高管间"}

# ============ 1) 00-索引 ============
VAULT = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库"
IDX0 = os.path.join(VAULT, "00-知识采集索引.md")
i0 = open(IDX0, encoding="utf-8").read()

# timeline
OLD_TL = "\u4e8c\u5341\u4e09\u8f6e enrich 2026-08-22(+6)\uff09"
NEW_TL = "\u4e8c\u5341\u4e09\u8f6e enrich 2026-08-22(+6) \uff5c \u4e8c\u5341\u56db\u8f6e enrich 2026-08-22(+7)\uff09"
assert OLD_TL in i0, "timeline old not found"
i0 = i0.replace(OLD_TL, NEW_TL, 1)

# counts
assert "**151 卡**" in i0, "151 marker"
i0 = i0.replace("**151 卡**", "**158 卡**", 1)
assert "\u4e00\u624b 47 + \u4e8c\u624b 104" in i0, "47/104 marker"
i0 = i0.replace("\u4e00\u624b 47 + \u4e8c\u624b 104", "\u4e00\u624b 51 + \u4e8c\u624b 107", 1)

# bg count block: ③ X 卡 / ② Y 卡（含 4 张跨档双标，去重后 Z）
mm = re.search(r'([0-9]+) \u5361 / [^卡]*?([0-9]+) \u5361\uff08\u542b 4 \u5f20\u8de8\u6863\u53cc\u6807\uff0c\u53bb\u91cd\u540e ([0-9]+)\uff09', i0)
assert mm, "bg count block not found"
r3c, r2c, dedu = int(mm.group(1)), int(mm.group(2)), int(mm.group(3))
new_block = "{0} \u5361 / {1} \u5361\uff08\u542b 4 \u5f20\u8de8\u6863\u53cc\u6807\uff0c\u53bb\u91cd\u540e {2}\uff09".format(r3c+1, r2c+6, dedu+7)
i0 = i0[:mm.start()] + new_block + i0[mm.end():]

# append 7 card rows before next "## 主题：" after afternoontea header
apos2 = i0.find("## 主题：下午茶研讨")
npos2 = i0.find("## 主题：", apos2 + 10)
assert npos2 != -1, "next topic not found"
rows = "".join(
    "| {0}\uff08afternoontea.html\uff09 | 4 | {1} | {2} | \n".format(c[0], c[1], c[2])
    for c in CARDS
)
i0 = i0[:npos2] + rows + "" + i0[npos2:]
open(IDX0, "w", encoding="utf-8").write(i0)
print("00-索引更新完成")

# ============ 2) 乐享上传（新建独立页文件模式）============
MCP_JSON = os.path.expanduser("~/.workbuddy/mcp.json")
LEXIANG_URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"
FOLDER = "96e0ca6a548e4202a12d43dc91b48938"
class LexiangMCP:
    def __init__(self, token):
        self.token = token; self.session = None
    def _post(self, payload, retries=2):
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
def put_bytes(url, data):
    req = urllib.request.Request(url, data=data, method="PUT")
    req.add_header("Content-Type", "text/html")
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.status
try:
    token = json.load(open(MCP_JSON, encoding="utf-8"))["mcpServers"]["lexiang"]["headers"]["Authorization"]
    mc = LexiangMCP(token); mc.initialize(); mc.initialized()
    try:
        print("whoami:", json.dumps(mc.call("whoami", {}), ensure_ascii=False)[:120])
    except Exception as e:
        print("whoami 跳过:", str(e)[:120])
    data_bytes = open(RUN_PATH, "rb").read()
    r = mc.call("file_apply_upload", {"parent_entry_id": FOLDER, "name": RUN_NAME, "extension":"html", "mime_type":"text/html", "upload_type":"PRE_SIGNED_URL", "size": str(len(data_bytes))})
    biz = mc.biz(r)
    if biz.get("code") != 0:
        raise RuntimeError("apply_upload FAIL {0}".format(biz.get("message")))
    sess = biz["data"]["session"]
    sid = sess.get("session_id") or sess.get("id")
    url = sess.get("upload_url") or sess["objects"][0]["upload_url"]
    st = put_bytes(url, data_bytes)
    if st != 200: raise RuntimeError("PUT status " + str(st))
    r2 = mc.call("file_commit_upload", {"session_id": sid})
    biz2 = mc.biz(r2)
    if biz2.get("code") != 0: raise RuntimeError("commit FAIL " + str(biz2.get("message")))
    rid = biz2["data"]["entry"]["id"]
    print("乐享新建页 OK entry_id=", rid)
    mapf = json.load(open(os.path.join(BASE, "lexiang-entry-map.json"), encoding="utf-8"))
    sm = mapf.setdefault("afternoontea", {"folder_id": FOLDER, "rounds": []})
    sm["folder_id"] = FOLDER
    sm["rounds"].append({"date": DATE, "entry_id": rid, "name": RUN_NAME})
    json.dump(mapf, open(os.path.join(BASE, "lexiang-entry-map.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("已回写 lexiang-entry-map.json")
except Exception as e:
    print("\u26a0\ufe0f 乐享上传跳过（warning，不中断）：" + str(e)[:300])

print("\n=== R24 收尾完成（索引+乐享）===")
