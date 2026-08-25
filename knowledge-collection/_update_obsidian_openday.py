# -*- coding: utf-8 -*-
import json, os, re
BASE = os.path.dirname(os.path.abspath(__file__))
NOTE = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\openday\OpenDay-开放日-知识卡汇总.md"
cards = json.load(open(os.path.join(BASE, "_openday_r27_cards.json"), encoding="utf-8"))["cards"]

def src(c):
    return "一手" if c["primary"] else "二手"
def rel(c):
    return "②上下级" if c["rel_class"] == "r2" else "③高管间"

# table rows
def oneliner(c):
    n = c["note"].replace("适用：", "").strip()
    # cut at first full-width parenthesis closing that is long
    if len(n) > 90:
        n = n[:88] + "…"
    return n

rows = ""
for c in cards:
    t = c["title"].replace("|", "／")
    rows += "| {t}（openday.html） | 4 | {s} | {r} | {o} |\n".format(
        t=t, s=src(c), r=rel(c), o=oneliner(c))

s = open(NOTE, encoding="utf-8").read()

# 1) 摘要 count + 二十八轮 segment
s = s.replace("共 207 张", "共 220 张", 1)
assert "共 220 张" in s
seg = (" + **二十八轮补采 2026-08-26(+13：驻德使馆领事开放日/哈使馆走进中国开放日/"
       "驻澳部队军营开放/空军航空开放/工业园区政府开放日/河南联通客户开放日/"
       "国网云开放日/中石化公众开放日/余江残联开放日/崖西乡村振兴开放日·10② + "
       "包头政商早餐会/梅河口政企早餐会/中新商会CEO闭门圆桌·3③，12一手+1二手)**")
anchor = ("+ **二十七轮补采 2026-08-26(+10：上海国企开放日城市级/脑智中心脑机接口/"
          "核能安全所核科普/固体所材料之美/成都智算AI/数博会公众开放日/信通院智算生态/"
          "知音湖北文旅/中宁工业园区闭环/章贡吐槽大会·8②2③，9一手+1二手)**。")
assert anchor in s
s = s.replace(anchor, anchor + seg, 1)

# 2) 适用&备注 counts
s = s.replace("**207 卡**", "**220 卡**", 1)
s = s.replace("一手 119 + 二手 88", "一手 131 + 二手 89", 1)
s = s.replace("②上下级 192 卡 / ③高管间 27 卡", "②上下级 202 卡 / ③高管间 30 卡", 1)

# 3) 二十八轮 prose block (append after the 二十四轮 block, before the last blank/section end)
prose = ("\n二十八轮补采（2026-08-26）新增聚焦外交领事/军营/央企云/政企早餐会等未覆盖子域"
         "（10 ②上下级 + 3 ③高管间，12 一手+1 二手）：「外交领事开放日」（驻德使馆领事大厅开放日，"
         "办证窗口+结婚角实景+免签政策宣讲+端午有奖问答+侨胞诉求直通车 / 驻哈使馆「走进中国」文化+叙事沉浸体验，"
         "大使致辞讲命运共同体）、「军营开放日」（解放军驻澳门部队第十九次军营开放，升国旗+课目展示+装备体验+联谊演出+线上发券，"
         "16万澳门市民累计参与 / 2025空军航空开放活动军营开放，抗眩晕训练+枪支射击+静态飞机+创客无人机机器人打卡）、"
         "「园区/乡村振兴政府开放日」（隆德县六盘山工业园区管委会政府开放日，员工代表≥2/3+四步闭环+15工作日办结 / "
         "崖西镇政务公开乡村振兴，便民服务中心实景+政策座谈）、「企业客户开放日」（河南联通2025客户开放日，一把手携领导班子+智慧展厅+现场派单回应）、"
         "「央企云开放日」（国家电网2025中巴智云开放日，汉剧文化载体+三国七地同步+云端 / 中国石化2025公众开放日，"
         "VR/慢直播/白鹭园把工厂变可探秘景区，二手补一手）、「残联政府开放日」（余江区残联辅具适配零距离，政策宣讲+个性化适配+征求意见台账）。"
         "「政企高管早餐会」（包头市政商恳谈早餐会，市长做东+现场派单+台账+微信群，34场431企办结率超九成 / "
         "梅河口市政企早餐会，三定三精+三级闭环，7期破解102诉求）、「跨国企业CEO闭门圆桌」（中国新加坡商会·上海×大华银行CEO闭门圆桌，"
         "邀请制+闭门保障同量级一把手坦诚战略对话）。硬排除：家庭日/家属开放日、投资者/资本市场/IR/证监局开放日（非 HRBP 企业文化活动向）。\n")
# 适用&备注 is the final section; append 二十八轮 prose at EOF (after the last 轮 block).
s = s.rstrip("\n") + "\n" + prose.rstrip("\n") + "\n"

# 4) 当轮独立页（第二十八轮）link after 二十七轮 link
old_link = "- 当轮独立页（第二十七轮）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/runs/openday-20260826-r27.html"
new_link = old_link + "\n- 当轮独立页（第二十八轮）：https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/openday/runs/openday-20260826-r28.html"
assert old_link in s
s = s.replace(old_link, new_link, 1)

# 5) 13 table rows before "## 适用 & 备注"
assert "## 适用 & 备注" in s
s = s.replace("## 适用 & 备注", rows + "\n## 适用 & 备注", 1)

open(NOTE, "w", encoding="utf-8").write(s)
print("Obsidian note updated. new bytes:", len(s.encode("utf-8")))
# sanity
print("contains 220 卡:", "220 卡" in s)
print("contains 二十八轮补采 2026-08-26(+13:", "二十八轮补采 2026-08-26(+13" in s)
print("contains r28 link:", "openday-20260826-r28.html" in s)
print("table rows added (count ｜ in file):", s.count("|"))
