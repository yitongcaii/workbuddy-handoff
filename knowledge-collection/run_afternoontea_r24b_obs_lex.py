# -*- coding: utf-8 -*-
"""下午茶研讨 R24 收尾：仅补 Obsidian 笔记 + 00-索引 + 乐享上传（墙/增量页/index.json 已在上一步完成，不重复）。"""
import json, os, re, urllib.request, urllib.error

BASE = os.path.dirname(os.path.abspath(__file__))
AT_DIR = os.path.join(BASE, "afternoontea")
DATE = "20260822"
RUN_NAME = "afternoontea-20260822b.html"
RUN_PATH = os.path.join(AT_DIR, RUN_NAME)
INC_URL = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/afternoontea/afternoontea-20260822b.html"
WALL_URL = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/afternoontea/afternoontea.html"

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# ---- 本轮卡（与正脚本一致；用于 笔记/索引 行渲染）----
CARDS = [
    ("\U0001F91D","盐城港集团「总经理接待日」·心声有回声","r2","b1","②上下级","一手"),
    ("\U0001F5D3\uFE0F","中国诚通「书记接待日」·建账督办十五五建言","r2","b1","②上下级","一手"),
    ("\U0001F375","悦达汽车「党委书记、工会主席接待日」座谈会","r2","b1","②上下级","一手"),
    ("\U0001F309","大唐甘肃「书记接待日」·开门教育连心桥","r2","b1","②上下级","一手"),
    ("\U0001F4CB","索普集团职工恳谈会·30年闭环制度","r2","b2","②上下级","二手"),
    ("\U0001F3ED","亚太森博「厂长沟通会」·季度直面一线","r2","b2","②上下级","二手"),
    ("\U0001F465","CEO 同侪顾问小组深度指南·孤独决策破局","r3","b2","③高管间","二手"),
]
REL_TXT = {"r2":"②上下级","r3":"③高管间"}

# ============ 1) Obsidian 笔记 ============
VAULT = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库"
NOTE = os.path.join(VAULT, "素材", "afternoontea", "下午茶研讨-知识卡汇总.md")
t = open(NOTE, encoding="utf-8").read()

# counts
assert "（151 卡 · 上下级/高管间）" in t, "H1 marker"
t = t.replace("（151 卡 · 上下级/高管间）", "（158 卡 · 上下级/高管间）", 1)
acc_old = "\u7d2f\u8ba1 151 \u5361\uff08③\u9ad8\u7ba1\u95f4 58 / ②\u4e0a\u4e0b\u7ea7 97\uff0c\u542b 4 \u5f20\u8de8\u6863\u53cc\u6807\uff1b\u4e00\u624b 47 + \u4e8c\u624b 104\uff09"
acc_new = "\u7d2f\u8ba1 158 \u5361\uff08③\u9ad8\u7ba1\u95f4 59 / ②\u4e0a\u4e0b\u7ea7 103\uff0c\u542b 4 \u5f20\u8de8\u6863\u53cc\u6807\uff1b\u4e00\u624b 51 + \u4e8c\u624b 107\uff09"
assert acc_old in t, "acc marker"
t = t.replace(acc_old, acc_new, 1)
# timeline
tl_old = "\u4e8c\u5341\u4e09\u8f6e enrich 2026-08-22(+6)"
tl_new = "\u4e8c\u5341\u4e09\u8f6e enrich 2026-08-22(+6) \uff5c \u4e8c\u5341\u56db\u8f6e enrich 2026-08-22(+7)"
assert tl_old in t, "timeline marker"
t = t.replace(tl_old, tl_new, 1)
# section headers
assert "## ③ 领导↔领导（高管间 · exec）— 56 卡" in t
t = t.replace("## ③ 领导↔领导（高管间 · exec）— 56 卡", "## ③ 领导↔领导（高管间 · exec）— 57 卡", 1)
assert "## ② 领导↔员工（上下级 · supervisor）— 93 卡" in t
t = t.replace("## ② 领导↔员工（上下级 · supervisor）— 93 卡", "## ② 领导↔员工（上下级 · supervisor）— 99 卡", 1)

m3 = t.find("## ③"); m2 = t.find("## ②")
r3_region = t[m3:m2]
r3_nums = [int(x) for x in re.findall(r'^\| (\d+) \|', r3_region, re.M)]
max_r3 = max(r3_nums) if r3_nums else 0
r3_cards = [c for c in CARDS if c[2]=="r3"]
r3_rows = "".join(
    "| {0} | {1}\uff08afternoontea.html\uff09 | {2} | {3} |\n".format(max_r3+1+i, esc(c[1]), c[5], REL_TXT[c[2]])
    for i, c in enumerate(r3_cards)
)
marker3 = "## ③ 领导↔领导（高管间 · exec）— 57 卡"
assert marker3 in t
t = t.replace(marker3, r3_rows + "\n" + marker3, 1)

# r2 rows: insert before the LAST "## 轮次" (R23 section follows r2 table)
lr = t.rfind("## 轮次")
r2_region = t[m2:lr]
r2_nums = [int(x) for x in re.findall(r'^\| (\d+) \|', r2_region, re.M)]
max_r2 = max(r2_nums) if r2_nums else 0
r2_cards = [c for c in CARDS if c[2]=="r2"]
r2_rows = "".join(
    "| {0} | {1}\uff08afternoontea.html\uff09 | {2} | {3} |\n".format(max_r2+1+i, esc(c[1]), c[5], REL_TXT[c[2]])
    for i, c in enumerate(r2_cards)
)
t = t[:lr] + r2_rows + "\n" + t[lr:]

# round narrative section before first "## ③" header
round_section = (
    "\n## 轮次 2026-08-22（+7）\n"
    "> 二十四轮 enrich：新增 7 卡（③ 高管间 +1：CEO 同侪顾问小组深度指南·孤独决策破局（shaanrais/HBR数据）；② 上下级 +6：盐城港「总经理接待日」/ 中国诚通「书记接待日」/ 悦达汽车党委工会接待日 / 大唐甘肃「书记接待日」/ 索普集团职工恳谈会·30年闭环 / 亚太森博「厂长沟通会」）。无 peer，relation 仅取 supervisor/exec。\n"
    "> 线上预览：{0} ｜ 本轮增量页：{1}\n".format(WALL_URL, INC_URL)
)
assert "## ③ 领导↔领导（高管间 · exec）— 57 卡" in t
t = t.replace("## ③ 领导↔领导（高管间 · exec）— 57 卡", round_section + "## ③ 领导↔领导（高管间 · exec）— 57 卡", 1)
open(NOTE, "w", encoding="utf-8").write(t)
print("Obsidian 笔记更新完成 | r3 max", max_r3, "r2 max", max_r2)

# ============ 2) 00-索引 ============
IDX0 = os.path.join(VAULT, "00-知识采集索引.md")
i0 = open(IDX0, encoding="utf-8").read()
assert "\u4e8c\u5341\u4e09\u8f6e enrich 2026-08-22(+6))\uff09" in i0
i0 = i0.replace("\u4e8c\u5341\u4e09\u8f6e enrich 2026-08-22(+6))\uff09",
                "\u4e8c\u5341\u4e09\u8f6e enrich 2026-08-22(+6)) \uff5c \u4e8c\u5341\u56db\u8f6e enrich 2026-08-22(+7)\uff09", 1)
assert "**151 卡**" in i0
i0 = i0.replace("**151 卡**", "**158 卡**", 1)
assert "\u4e00\u624b 47 + \u4e8c\u624b 104" in i0
i0 = i0.replace("\u4e00\u624b 47 + \u4e8c\u624b 104", "\u4e00\u624b 51 + \u4e8c\u624b 107", 1)
# counts via regex (circled numbers may be fullwidth/ascii); use generic patterns
mm = re.search(r'([0-9]+) \u5361 / ([0-9]+) \u5361\uff08\u542b 4 \u5f20\u8de8\u6863\u53cc\u6807\uff0c\u53bb\u91cd\u540e ([0-9]+)\uff09', i0)
assert mm, "bg count block not found"
r3c, r2c, dedu = int(mm.group(1)), int(mm.group(2)), int(mm.group(3))
new_block = "{0} \u5361 / {1} \u5361\uff08\u542b 4 \u5f20\u8de8\u6863\u53cc\u6807\uff0c\u53bb\u91cd\u540e {2}\uff09".format(r3c+1, r2c+6, dedu+7)
i0 = i0[:mm.start()] + new_block + i0[mm.end():]
# append rows before next "## 主题：" after afternoontea header
apos2 = i0.find("## 主题：下午茶研讨")
npos2 = i0.find("## 主题：", apos2 + 10)
assert npos2 != -1, "next topic not found"
rows = "".join(
    "| {0}\uff08afternoontea.html\uff09 | 4 | {1} | {2} | \n".format(c[1], c[5], REL_TXT[c[2]])
    for c in CARDS
)
i0 = i0[:npos2] + rows + "\n" + i0[npos2:]
open(IDX0, "w", encoding="utf-8").write(i0)
print("00-索引更新完成")

# ============ 3) 乐享上传（新建独立页文件模式）============
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

print("\n=== R24 收尾完成（笔记+索引+乐享）===")
