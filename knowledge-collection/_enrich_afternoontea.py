# -*- coding: utf-8 -*-
import json, io, os, sys

BASE = r"c:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection"
HTML = os.path.join(BASE, "afternoontea", "afternoontea.html")
IDX  = os.path.join(BASE, "index.json")

def card(emoji, title, cat, rel, reltxt, val, how, url, note):
    badge = "r3" if rel == "exec" else "r2"
    return (
        '    <div class="hl">\n'
        f'      <div class="top"><span class="emoji">{emoji}</span><h3>{title}</h3>'
        f'<span class="cat">{cat}</span><span class="badge {badge}">{reltxt}</span>'
        f'<span class="badge b2">二手</span></div>\n'
        f'      <p class="val">{val}</p>\n'
        '      <details class="exec"><summary>怎么做</summary>'
        f'<div class="inner">{how}</div></details>\n'
        f'      <div class="src">\u2757 <a href="{url}" target="_blank">{url}</a></div>\n'
        f'      <div class="note">适用：{note}</div>\n'
        '    </div>\n'
    )

# ---- new ③ exec cards (2) ----
new_three = (
    card("\U0001F338", "红颜会「红颜下午茶」·女性领导者圈层私享社交", "圈层私享", "exec", "高管间",
        "菁英女性领导者俱乐部「红颜会」为会员量身定制的精品圈层活动「红颜下午茶」：同趣相交的心流聚场，主题涵盖时尚艺术、文化教育、情感、健康、财富传承等多元角度；与玛莎拉蒂、正和岛等联名下午茶，打造集生活方式与私享社交的互动场景，不期而遇的闺蜜及伙伴，缔结信任、对接人脉与商脉。",
        "定向邀约制锁定同频女性领导者；主题化精致下午茶(时尚/文化/财富传承)；跨界品牌联名(豪车/正和岛)抬升圈层；以私享社交沉淀信任与人脉。",
        "http://m.cnhrtv.com/nd.jsp?id=443",
        "③ 女性高管圈层私享社交场景，强调「同频+精致+跨界联名」，可作女性领导力活动对外版参考。")
    + card("\U0001F4BC", "女性投资人闭门沙龙·VC/PE 女合伙人同侪对话", "女性闭门", "exec", "高管间",
        "21世纪创投研究院「影响力女性投资人闭门沙龙暨股权投资春季策略会」：由南方财经全媒体集团、中国投资协会创投委指导，中华女创投家联谊会主办；定向邀约女性 VC/PE 合伙人(唐兴资本/元禾辰坤/优山资本等)，主题分享 + 圆桌讨论，在外部环境与行业剧变下交流投资策略与应对，构建女性投资人同侪学习网络。",
        "定向邀约女性投资合伙人(资质同频)；权威机构指导+联谊会主办抬公信；主题分享+圆桌双结构；以「女性力量+投资策略」为钩子建长效同侪网络。",
        "https://m.10jqka.com.cn/20240309/c655765938.shtml",
        "③ 投资圈高管同侪闭门沙龙，定向邀约+主题分享+圆桌，与私董会互补(行业同侪 vs 案主制)。")
)

# ---- new ② supervisor cards (4) ----
new_two = (
    card("\U0001F36A", "微管理茶歇·主管日常茶水间情绪温度计", "微管理", "supervisor", "上下级",
        "部门主管每天下午固定 10 分钟在茶水间停留、与同事随意闲聊(不谈工作进度)，是一种低成本、高频率的「情绪温度计」——通过碎片化交流及时发现成员压力点与潜在冲突；本质是「不打扰的参与」，多为听少说、关注平时不表达意见的成员，避免变成新型例会。",
        "固定短时段(10-15min)随机出现在茶水间；只聊生活/兴趣/八卦不问正事；多听少说、关注沉默成员；适度自曝拉近距离；发现异常(如加班过多)次日即协调资源(护眼灯/调休)。",
        "https://landian.cc/content.aspx?p=1632",
        "② 管理者日常微管理茶歇，零成本高频触达，补足正式会议捕捉不到的情绪信号。")
    + card("\U0001F6CB\uFE0F", "开放式茶歇区设计·空间促跨部门日常沟通", "空间设计", "supervisor", "上下级",
        "开放式茶歇区(沙发+圆桌+高脚椅+绿植+柔光)作为非正式交流空间，在上午 10 点、下午 3 点提供免费咖啡/水果/点心吸引不同部门员工聚集；设数字留言板/可书写玻璃墙收集灵感；关键是「领导层也参与喝咖啡」，层级隔阂自然消融，一线真实想法与跨部门灵感即时碰撞。",
        "布局用开放式沙发圆桌柔光降心理防线；在能量低谷时段供免费补给聚人；设白板/玻璃墙承接灵感；管理者自然参与(非刻意)才有效；定期换装饰维持新鲜。",
        "https://www.lanqiaocycyy.cn/20250521.html",
        "② 以空间设计承载日常非正式沟通，低成本促跨部门连接，领导参与是成败关键。")
    + card("\U0001F504", "台湾二代接班·每周下午茶倾听+员工信箱闭环", "接班倾听", "supervisor", "上下级",
        "台湾企业二代接班人为打破「课长级声音不易被听见」的断层，每周找六名年资 3-5 年员工或课长级喝下午茶(累计两百多人)，了解一线想法；同步设员工信箱，宣导后员工敢于反映主管小事，问题被认真看待即建立信任；凭一年茶会洞察推动奖金制度改革(按绩效而非本薪配奖金)。",
        "接班人亲自每周小范围下午茶(避正式汇报)；设员工信箱作补充通道并宣导可用；反映的问题必追踪有回馈；把一线洞察转化为真实制度改革(奖金/流程)。",
        "https://www.businesstoday.com.tw/article/category/183034/post/201907100036/",
        "② 接班人/高管常态化下午茶倾听+信箱双通道闭环，把非正式沟通转为治理改进。")
    + card("\U0001F343", "茶文化融入HRM·入职品茗/以老带新/以茶表彰", "茶文化HRM", "supervisor", "上下级",
        "把中华茶文化系统融入人力资源管理：定期部门/全员下午茶、公共茶歇区建设；新员工入职由主管带领共饮「迎新之茗」缓解紧张；「以老带新」结对喝「成长之杯」培养师徒情；对优秀者「以茶表彰」传递尊重认可；将企业价值观与茶道精神(包容/诚信/敬业)结合，提升归属感与雇主品牌。",
        "定期下午茶+开放式茶歇区作日常连接；新人第一天主管迎新品茗；老带新结对喝成长之杯；以茶表彰替代部分物质奖励；茶道精神绑定价值观入职即植入。",
        "https://blog.ihr360.com/p/180499",
        "② 茶文化仪式化融入HRM(迎新/传帮带/表彰)，低成本的归属感与认可工程。")
)

with io.open(HTML, "r", encoding="utf-8") as f:
    h = f.read()

assert h.count('  <!-- ============ ② 上下级 ============ -->') == 1, "sec2 marker not unique"
marker3 = '  </div>\n\n  <!-- ============ ② 上下级 ============ -->'
assert h.count(marker3) == 1, "sec3 grid close not unique"
h = h.replace(marker3, '    ' + new_three.replace('\n', '\n    ').rstrip(' ') + '\n  </div>\n\n  <!-- ============ ② 上下级 ============ -->', 1)

marker2 = '  </div>\n\n  <footer>'
assert h.count(marker2) == 1, "sec2 grid close not unique"
h = h.replace(marker2, '    ' + new_two.replace('\n', '\n    ').rstrip(' ') + '\n  </div>\n\n  <footer>', 1)

# hero + sec tags
h = h.replace('｜ 六维评估（含关系适配度）', '｜ 五轮 enrich 2026-08-09（+6）｜ 六维评估（含关系适配度）', 1)
h = h.replace('<span class="tag">15 卡</span>', '<span class="tag">17 卡</span>', 1)
h = h.replace('<span class="tag">22 卡</span>', '<span class="tag">26 卡</span>', 1)

with io.open(HTML, "w", encoding="utf-8") as f:
    f.write(h)

# ---- index.json ----
new_entries = [
    {"title":"红颜会「红颜下午茶」·女性领导者圈层私享社交","normKey":"红颜会红颜下午茶女性领导者圈层私享社交","url":"http://m.cnhrtv.com/nd.jsp?id=443","sourceType":"secondary","relation":"exec","summary":"菁英女性领导者俱乐部红颜下午茶：同趣相交心流聚场，主题含时尚艺术/文化教育/财富传承，与玛莎拉蒂/正和岛联名私享社交"},
    {"title":"女性投资人闭门沙龙·VC/PE女合伙人同侪对话","normKey":"女性投资人闭门沙龙vcpe女合伙人同侪对话","url":"https://m.10jqka.com.cn/20240309/c655765938.shtml","sourceType":"secondary","relation":"exec","summary":"21世纪创投研究院女性投资人闭门沙龙：定向邀约女性VC/PE合伙人，主题分享+圆桌，行业剧变下交流投资策略"},
    {"title":"微管理茶歇·主管日常茶水间情绪温度计","normKey":"微管理茶歇主管日常茶水间情绪温度计","url":"https://landian.cc/content.aspx?p=1632","sourceType":"secondary","relation":"supervisor","summary":"部门主管每天10分钟茶水间闲聊作情绪温度计，低成本高频不打扰的参与，捕捉会议外的压力点"},
    {"title":"开放式茶歇区设计·空间促跨部门日常沟通","normKey":"开放式茶歇区设计空间促跨部门日常沟通","url":"https://www.lanqiaocycyy.cn/20250521.html","sourceType":"secondary","relation":"supervisor","summary":"开放式茶歇区+能量低谷时段免费补给，领导参与则层级消融，促跨部门灵感碰撞"},
    {"title":"台湾二代接班·每周下午茶倾听+员工信箱闭环","normKey":"台湾二代接班每周下午茶倾听员工信箱闭环","url":"https://www.businesstoday.com.tw/article/category/183034/post/201907100036/","sourceType":"secondary","relation":"supervisor","summary":"台湾企业二代每周找6名课长级喝下午茶(200+人)+员工信箱双通道，洞察推动奖金制度改革"},
    {"title":"茶文化融入HRM·入职品茗/以老带新/以茶表彰","normKey":"茶文化融入hrm入职品茗以老带新以茶表彰","url":"https://blog.ihr360.com/p/180499","sourceType":"secondary","relation":"supervisor","summary":"茶文化融入HRM：迎新品茗/老带新成长之杯/以茶表彰，绑定茶道精神(包容诚信敬业)提升归属感"},
]

with io.open(IDX, "r", encoding="utf-8") as f:
    data = json.load(f)

existing_urls = {e.get("url") for e in data}
added, skipped = [], 0
for e in new_entries:
    if e["url"] in existing_urls:
        skipped += 1
        continue
    data.append(e)
    added.append(e["title"])
    existing_urls.add(e["url"])

with io.open(IDX, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("HTML bytes:", os.path.getsize(HTML))
print("index total:", len(data))
print("added:", len(added), "skipped:", skipped)
for t in added:
    print("  +", t)
