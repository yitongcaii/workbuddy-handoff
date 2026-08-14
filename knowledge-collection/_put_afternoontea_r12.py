# -*- coding: utf-8 -*-
import os, sys, json
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
from upload_rounds_lexiang import LexiangMCP, load_token

WS = os.path.dirname(os.path.abspath(__file__))
MAPF = os.path.join(WS, "lexiang-entry-map.json")
FP = os.path.join(WS, "afternoontea", "afternoontea-20260814.html")
NAME = "afternoontea-20260814.html"

try:
    token = load_token()
    mc = LexiangMCP(token)
    mc.initialize()
    mc.initialized()
    print("乐享连接: whoami/initialize OK")
except Exception as e:
    print(f"⚠️ 乐享连接失败（跳过上传，不中断）：{e}")
    sys.exit(0)

mapf = json.load(open(MAPF, encoding="utf-8"))
folder = mapf["afternoontea"]["folder_id"]
print("afternoontea folder:", folder)

try:
    data = open(FP, "rb").read()
    eid = mc.upload_new(folder, NAME, data)
    print(f"✅ 乐享上传成功 entry_id={eid} 字节={len(data)}")
    mapf["afternoontea"]["rounds"].append({
        "date": "20260814",
        "entry_id": eid,
        "name": NAME,
        "note": "轮次页·十二轮 enrich (+7)"
    })
    json.dump(mapf, open(MAPF, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("✅ 已回写 lexiang-entry-map.json")
except Exception as e:
    print(f"⚠️ 乐享上传调用失败（跳过，不中断）：{e}")
    sys.exit(0)
