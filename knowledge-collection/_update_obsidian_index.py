# -*- coding: utf-8 -*-
import json, os
IDX = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
BASE = os.path.dirname(os.path.abspath(__file__))
cards = json.load(open(os.path.join(BASE, "_openday_r27_cards.json"), encoding="utf-8"))["cards"]

def src(c): return "一手" if c["primary"] else "二手"
def rel(c): return "②上下级" if c["rel_class"] == "r2" else "③高管间"

s = open(IDX, encoding="utf-8").read()

# 1) append 二十八轮 segment to the topic header (after 二十七轮 segment tail)
anchor = ("｜ 2026-08-26 二十七轮补采 +10（上海国企开放日城市级/脑智中心脑机接口/"
          "核能安全所核科普/固体所材料之美/成都智算AI/数博会公众开放日/信通院智算生态/"
          "知音湖北文旅/中宁工业园区闭环/章贡吐槽大会·8②2③）")
assert anchor in s, "header anchor not found"
seg = ("｜ 2026-08-26 二十八轮补采 +13（驻德使馆领事开放日/哈使馆走进中国开放日/"
       "驻澳部队军营开放/空军航空开放/工业园区政府开放日/河南联通客户开放日/"
       "国网云开放日/中石化公众开放日/余江残联开放日/崖西乡村振兴开放日·10② + "
       "包头政商早餐会/梅河口政企早餐会/中新商会CEO闭门圆桌·3③，12一手+1二手）")
s = s.replace(anchor, anchor + seg, 1)

# 2) add 13 rows before "📄 主题汇总笔记" line
rows = ""
for c in cards:
    t = c["title"].replace("|", "／")
    rows += "| {t}（openday.html） | 4 | {src} | {rel} | 二十八轮新增 |\n".format(
        t=t, src=src(c), rel=rel(c))
note_anchor = "📄 主题汇总笔记"
assert note_anchor in s
s = s.replace(note_anchor, rows + note_anchor, 1)

open(IDX, "w", encoding="utf-8").write(s)
print("00-索引 updated. bytes:", len(s.encode("utf-8")))
print("contains 二十八轮补采 +13:", "二十八轮补采 +13" in s)
print("r28 rows present:", s.count("二十八轮新增"))
