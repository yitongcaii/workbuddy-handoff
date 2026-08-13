# -*- coding: utf-8 -*-
import os, json
WS="c:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection"
# portal
p=os.path.join(WS,"index.html")
s=open(p,encoding="utf-8").read()
old='<div class="emoji">🧊</div><h3>破冰（正式场景）</h3><div class="cnt">62 卡</div>'
new='<div class="emoji">🧊</div><h3>破冰（正式场景）</h3><div class="cnt">86 卡</div>'
assert old in s, "portal 破冰 old string not found"
s=s.replace(old,new)
tmp=p+".tmp"; open(tmp,"w",encoding="utf-8").write(s); os.replace(tmp,p)
print("portal 破冰 62->86 OK")
# lexiang map
p=os.path.join(WS,"lexiang-entry-map.json")
m=json.load(open(p,encoding="utf-8"))
ib=m["icebreaker"]
ib["wall"]["note"]="R10 累计墙（86卡）"
for r in ib["rounds"]:
    if r.get("date")=="2026-08-14":
        r["name"]="icebreaker-20260814.html"
        r["note"]="轮次页 R10 (+7｜修正：替换误产12重复卡)"
json.dump(m,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("lexiang map wall+R10 name/note OK (entry_id filled on upload)")
