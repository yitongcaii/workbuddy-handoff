# -*- coding: utf-8 -*-
import os, re, json

WS="c:/Users/v_yitcai/WorkBuddy/20260728154244/knowledge-collection"
AWARD=os.path.join(WS,"award/award.html")

# 5 new cards (4 supervisor + 1 exec, 0 peer)
cards=[
 {"emoji":"🧭","title":"主管日常认可战术手册·非正式/流动奖杯/微笑箱/星标计划","cat":"管理实操",
  "rel":["supervisor"],"src":"二手","url":"https://www.ualberta.ca/human-resources-health-safety-environment/culture-and-well-being/culture/recognition/recognition-tips-for-supervisors.html",
  "val":"主管日常认可作战手册：把认可拆成非正式(每周团队会点名表扬/月度旅行奖杯/「微笑箱」收正向便签抽选/星标计划公开表彰)/自发(一对一 Praising、手写感谢卡、周五惊喜)/正式(年度 booklet、部门披萨/冰淇淋社交)三档；强调「年度盛典若无全年高频互动则影响极小」，认可须贴合个人情境且真诚。",
  "howto":"在周/月例会与 1:1 中嵌入固定认可环节；设部门「Way to Go」公告板/旅行奖杯制造持续正反馈；害羞员工改邮件/备忘录公开表彰；把客户表扬信在会上宣读。",
  "note":"适用：② 主管→团队日常认可战术（上下级），把颁奖的微认可下沉为全年高频、可落地的管理动作。"},
 {"emoji":"🚀","title":"管理者要领 recognition 而非只审批·5个领导转变","cat":"领导力",
  "rel":["supervisor"],"src":"二手","url":"http://bringjoytowork.com/blog/managers-guide-how-to-lead-recognition-not-just-approve-it/",
  "val":"管理者「领 recognition」五转变：① 被动审批→主动（不等大奖/里程碑，实时看见努力与进步就点名）；② 泛泛→个性化（\"Great job\"→具体行为+影响）；③ 合规→连接（重情感可信度而非走流程）；④ 委托 HR→融入日常领导行为；⑤ 只参加正式时刻→实时 intentional 认可。Gallup：直属经理的认可比全员广播更能拉升敬业度。",
  "howto":"每周做一次 recognition reflection：本周谁有进展/帮了同事/搞定难客户；用 Slack/Teams 频道流动分享 quick wins；把「观察→影响→感激」三段式变成 manager 默认话术。",
  "note":"适用：② 管理者领导认可文化（上下级），让颁奖从「HR 项目」变「直线经理的日常领导习惯」。"},
 {"emoji":"🌿","title":"绿色颁奖盛典运营·ESG评分卡+可复用物料+素食餐饮","cat":"绿色运营",
  "rel":["exec"],"src":"二手","url":"https://pentawards.com/live/zh/page/sustainbility-esg",
  "val":"绿色颁奖盛典运营范本（Pentawards Gala 获 ESG 铂金/金牌）：建 ESG 评分卡（铜/银/金/铂分级，作各场次基准）；所有前菜素食、可持续采购餐饮商、无印刷手册改数字标牌/环保可复用料、标牌用 5mm 木板+可回收油墨、本地供应商合作；Easyfairs 承诺 2050 净零、2030 减排一半。",
  "howto":"办颁奖/表彰盛典时把 ESG 评分卡当硬指标：餐饮素食化+本地采购、物料可复用/可回收、去印刷改数字、与本地社区供应商绑定；把可持续作为雇主品牌与「绿色荣誉」叙事的一部分。",
  "note":"适用：③ 高管/活动负责人绿色盛典运营（高管间），把颁奖的可持续与品牌价值一体化，而非只重舞美。"},
 {"emoji":"🖥️","title":"Digital Wall of Fame·实时认可流+区块链徽章","cat":"数字荣誉",
  "rel":["supervisor"],"src":"二手","url":"https://www.verifyed.io/blog/employee-recognition-performance-examples",
  "val":"数字荣誉墙（Digital Wall of Fame）运营：动态实时认可流替代静态展示——Peer kudos、实时 shoutout、团队排行榜持续可见；区块链验证徽章（IBM 技能/里程碑徽章使培训参与度 +21%、微软×LinkedIn 学习徽章完课率 +40%）；数字成就证书可社交分享、跨系统 API 凭证；社交认可流让成就跨部门可见，形成文化涟漪。",
  "howto":"用认可平台建「荣誉墙」模块沉淀实时认可与徽章；关键成就发区块链/可验证数字证书提升职业可信度；把荣誉墙接入 Slack/Teams 让认可在日常流中发生；新人可浏览历史认可理解「组织看重什么」。",
  "note":"适用：② 主管/HR 用数字荣誉墙把颁奖的荣誉「持续化、可见化、可携带」（上下级+平台运营）。"},
 {"emoji":"🏅","title":"数字荣誉墙·14类电子徽章体系(大陆汽车电子案例)","cat":"数字荣誉",
  "rel":["supervisor"],"src":"一手","url":"https://www.workercn.cn/c/2025-07-31/8572180.shtml",
  "val":"【工人日报案例·大陆汽车电子】「乐享汇」职工关爱平台用游戏化「徽章+积分」双激励，发服务年限/技能比武/劳模/技术专家/创新贡献等 14 类电子荣誉徽章，荣誉墙呈现职工成长轨迹；已累计发 1200+ 数字徽章、95% 职工至少获 1 枚；配「5+14」限时办结民主反馈闭环，建议办结率 98%。基层工会深度参与徽章标准制定。",
  "howto":"建数字化荣誉墙沉淀各类电子徽章（工龄/技能/创新/劳模），让荣誉「挂墙上、可回看」；工会/基层管理参与评选标准制定增强公信力；把荣誉墙与民主反馈闭环绑定，形成「被看见—被响应」的正循环。",
  "note":"适用：② 基层管理/工会/HR 数字荣誉墙（上下级），一手企业案例验证徽章体系的高覆盖与归属感提升。"},
]

def rel_badges(rel):
    out=""
    if "exec" in rel: out+='<span class="badge r3">高管间</span>'
    if "supervisor" in rel: out+='<span class="badge r2">上下级</span>'
    return out
def src_badge(src):
    return '<span class="badge b1">一手</span>' if src=="一手" else '<span class="badge b2">二手</span>'

def card_html(c):
    return (f'<div class="hl">\n'
            f'  <div class="top"><span class="emoji">{c["emoji"]}</span><h3>{c["title"]}</h3>'
            f'<span class="cat">{c["cat"]}</span>{rel_badges(c["rel"])}{src_badge(c["src"])}</div>\n'
            f'  <p class="val">{c["val"]}</p>\n'
            f'  <details class="exec"><summary>怎么做</summary><div class="inner">{c["howto"]}</div></details>\n'
            f'  <div class="src">🔗 <a href="{c["url"]}" target="_blank">{c["url"]}</a></div>\n'
            f'  <div class="note">{c["note"]}</div>\n'
            f'</div>\n')

r3_new="".join(card_html(c) for c in cards if "exec" in c["rel"])
r2_new="".join(card_html(c) for c in cards if "supervisor" in c["rel"])

html=open(AWARD,encoding="utf-8").read()
# insert into sec3 grid
html=re.sub(r'(<div class="sec sec3">.*?<div class="grid">)(.*?)(</div>\s*<div class="sec sec2">)',
            lambda m:m.group(1)+m.group(2)+r3_new+m.group(3), html, flags=re.S, count=1)
# insert into sec2 grid (last grid before footer)
html=re.sub(r'(<div class="sec sec2">.*?<div class="grid">)(.*?)(</div>\s*<footer>)',
            lambda m:m.group(1)+m.group(2)+r2_new+m.group(3), html, flags=re.S, count=1)
# hero round label
html=html.replace("十一轮 enrich 2026-08-13(+5)</p>","十一轮 enrich 2026-08-13(+5) ｜ 十二轮 enrich 2026-08-14(+5)</p>",1)
tmp=AWARD+".tmp"; open(tmp,"w",encoding="utf-8").write(html); os.replace(tmp,AWARD)
print("award.html -> cards:",html.count('<div class="hl">'),"| r3:",html.count('badge r3'),"sec3+sec2 check")

# ---- increment page ----
head=open(AWARD,encoding="utf-8").read().split("<body>")[0]
inc=head+"<body>\n<div class=\"wrap\">\n"
inc+='<p style="margin:0 0 16px"><a href="award.html" style="display:inline-block;background:#eef0ff;color:#6c5ce7;font-weight:700;font-size:13px;padding:8px 16px;border-radius:20px;text-decoration:none;">← 返回累计卡片墙</a></p>\n'
inc+='  <div class="hero"><h1>🏆 颁奖典礼 · 十二轮独立页（2026-08-14 · +5）</h1><p>本轮新增 5 张（③1 / ②4，0 平级/朋友向）｜ 受众关系分层：仅②上下级 / ③高管间。</p></div>\n'
inc+='  <div class="grid">\n'+ "".join(card_html(c) for c in cards) + '  </div>\n'
inc+='  <footer>📌 本页由 yitong 沉淀整理 · 文化活动知识库</footer>\n'
inc+='</div>\n</body>\n</html>\n'
ipath=os.path.join(WS,"award/award-20260814.html")
open(ipath,"w",encoding="utf-8").write(inc)
print("increment award-20260814.html bytes:",os.path.getsize(ipath),"cards:",inc.count('<div class="hl">'))

# ---- index.json ----
idx=json.load(open(os.path.join(WS,"index.json"),encoding="utf-8"))
for c in cards:
    idx.append({"topic":"award","title":c["title"],"url":c["url"],"source":c["url"],
                "relation":c["rel"],"type":c["src"],"quality":5,
                "summary":c["val"][:140],"date":"2026-08-14"})
json.dump(idx,open(os.path.join(WS,"index.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("index.json total:",len(idx),"| award now:",sum(1 for x in idx if x.get('topic')=='award'))

# save metadata for obsidian/portal step
json.dump(cards,open(os.path.join(WS,"_award_new.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("RENDER DONE")
