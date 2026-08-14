# -*- coding: utf-8 -*-
import json, re

def norm(t):
    return re.sub(r'[\s·，。、：；（）()【】\[\]“”—\-·/]', '', t)

PATH = "index.json"
d = json.load(open(PATH, encoding="utf-8"))

new = [
 dict(title="中国有色集团2026工作会·董事长讲话+总经理报告（一手）",
      url="http://cnmnc.com/content/content.html?id=7424339308267442176",
      sourceType="primary", relation="exec",
      summary="央企官网一手：1月26日中国有色集团2026工作会暨三届六次职代会。董事长文岗讲话提出“十五五”一核两链双业协同、资源报国、七大攻坚战；总经理张晋军作工作报告六方面部署2026；签经营/安全/廉政责任书、通过职代会决议，现场+视频召开。"),
 dict(title="通用技术集团2026工作会·董事长报告+总经理总结讲话（一手）",
      url="https://www.cntic.com.cn/xwzx/jtxw/art/2026/art_30304f95125246e4b202259a9b342654.html",
      sourceType="primary", relation="exec",
      summary="央企官网一手：1月5日通用技术集团2026工作会暨三届五次职代会。董事长于旭波作主题工作报告（1251方针、打赢五场战役）；总经理崔志成作总结讲话收口动员。围绕中央精神与央企负责人会议要求定调。"),
 dict(title="中国中煤2026工作会·工作会+职代会+安全会三会合一（一手）",
      url="https://jsjt.chinacoal.com/col/col524/art/2026/art_8644d2c19858e740c0eaa39a50c361be.html",
      sourceType="primary", relation="exec",
      summary="央企官网一手：1月8日中国中煤2026工作会暨职代会、安全工作会议。董事长王树东讲话+总经理高士岗报告+党建/安全专题报告；会中表彰劳模先进；提出存量提效增量转型、两个联营+、八项重点；主会场+视频分会场。"),
 dict(title="中国电建贵阳院2026工作会暨职代会（一手）",
      url="http://gepcc.powerchina.cn/col/col514/art/2026/art_a6ce7181dfcf4ca5b616cf19989898d8.html",
      sourceType="primary", relation="exec",
      summary="央企官网一手：2月9日中国电建贵阳院2026工作会暨二届四次职代会。总经理王远辉作工作报告+讲话双文本（部署+动员）；主持领导传达上级精神；目标用“六个更”具象化；职代会同步审议。"),
 dict(title="中国电建十六局2026工作会·报告+责任书+表彰（一手）",
      url="http://16j.powerchina.cn/col/col5174/art/2026/art_b4d562e9c9384d8a880abd1fe03a7339.html",
      sourceType="primary", relation="exec",
      summary="央企官网一手：中国电建十六局2026工作会暨十六届六次职代会。董事长杨刚讲话+总经理潘金仁报告；审议工作/财务/提案三报告；签经营/安全/廉政三责任书；表彰优秀项目部/班子/经理；现场+视频。"),
 dict(title="统帅装饰2026企业文化大训·董事长平等思想交流（案例）",
      url="https://new.qq.com/rain/a/20260618A09LS400",
      sourceType="secondary", relation="supervisor",
      summary="案例：6月11日统帅装饰企业文化大训，董事长定义为“平等的思想交流”而非单向灌输，全员诵读《员工十大行为准则》，管理者现身说法拆解“真诚·极致”八大内核，文化落地为可践行行为标准。"),
 dict(title="佛山金控职工大会·党委书记1小时宣讲新文化（案例）",
      url="https://www.fs-financial.com",
      sourceType="secondary", relation="supervisor",
      summary="案例：7月3日佛山金控总部职工大会宣讲新文化，党委书记宗颖1小时亲自宣讲、提“五要五不能”；全员征集建立合规专业阳光共责价值观；同步审议薪酬/绩效/问责制度+选职工董事，文化落治理。"),
 dict(title="康洋集团文化落地大会·创始人主持500人分队宣贯（案例）",
      url="https://reportify.cn/news/1194721203584110592",
      sourceType="secondary", relation="supervisor",
      summary="案例：康洋集团文化落地大会，创始人冯启勇主持、500人参与，发布新版文化体系；全员分16分队上台宣贯；文化内核定为“爱/利他”，落成工作作风/人才战略等可执行条目。"),
 dict(title="富维车轮合创文化·高管定调+中层穿透落地（案例）",
      url="https://caifuhao.eastmoney.com/news/20250723070209019776470",
      sourceType="secondary", relation="supervisor",
      summary="案例：富维车轮合创文化宣贯，党委书记总经理提“三个带头”并把文化注入考核；中层用部门会下沉到班组岗位；配赛事/美食节+矩阵传播（公众号/视频/屏保）让文化可感可达。"),
 dict(title="九州通“合格家人”文化宣导·董事长家书+话剧（案例）",
      url="https://m.cnhubei.com/cmdetail/167726",
      sourceType="secondary", relation="supervisor",
      summary="案例：九州通“做一名合格的家人”文化宣导大会暨五定大会，1400余员工参会；战略宣贯+五定+签业绩合同；区域公司宣读“八家”释义；话剧演真实案例；董事长亲笔家书作情感收尾。"),
 dict(title="年度员工表彰大会策划模板·评选机制+流程（模板）",
      url="https://renrendoc.com/paper/464311311.html",
      sourceType="secondary", relation="supervisor",
      summary="模板：年度员工表彰大会标准策划——致辞+颁奖+展示+闭幕四段；奖项分个人/团队/专项三层、评选“部门推荐→评审团→OA公示”三步走；颁奖重VCR+感言+高层交叉颁奖仪式感。"),
]

existing = {x.get("url","").strip() for x in d}
added=[]
for n in new:
    if n["url"] in existing:
        print("SKIP dup:", n["title"])
        continue
    n["normKey"] = norm(n["title"])
    n["topic"] = "staff-meeting"
    n["source"] = "web"
    d.append(n)
    added.append(n["title"])

json.dump(d, open(PATH,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
print("total now:", len(d))
print("added:", len(added))
for a in added:
    print(" +", a)
