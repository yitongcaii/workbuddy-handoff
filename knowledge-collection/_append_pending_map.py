# -*- coding: utf-8 -*-
import json, os
p = r"C:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection\lexiang-entry-map.json"
m = json.load(open(p, "r", encoding="utf-8"))
rec = m.setdefault("staff-meeting", {})
rounds = rec.setdefault("rounds", [])
# 去重：若已存在同 date+name 则跳过
name = "staff-meeting-2026-09-02-r30.html"
if not any(r.get("name") == name for r in rounds):
    rounds.append({
        "date": "2026-09-02",
        "entry_id": None,
        "name": name,
        "note": "轮次页 R30 (+7)｜乐享待补传（mcp.json lxmcp_ token 401 过期/断开，待重配后补传并回填 entry_id）",
    })
    print("appended pending r30 -> map")
else:
    print("r30 already in map, skip")
json.dump(m, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
