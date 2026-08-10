# -*- coding: utf-8 -*-
import json, re

def norm(t):
    return re.sub(r'[\s·，。、：；（）()【】\[\]“”—\-·/]', '', t)

PATH = "index.json"
d = json.load(open(PATH, encoding="utf-8"))

new = [
 dict(title="中国一汽2026年职工家属开放日（总部·1+7会场）", url="http://www.jl.xinhua.org/20260727/58929fe35e63493aa623a06bb82016ff/c.html",
      sourceType="secondary", relation="supervisor",
      summary="一汽总部家属开放日：董事长致辞「职工是主人、家庭是后盾」，主题「同职工心连心 与企业共命运」，创新1+7多会场分流，文化/产品/制造体验之旅+食堂+惠工大集。"),
 dict(title="中车兰州机车「红色引擎 智造未来」职工家属开放日", url="https://www.crrcgc.cc/lz/2026-06/01/article_2026060114134412177.html",
      sourceType="primary", relation="supervisor",
      summary="央企官网：家属走进生产车间与劳模创新工作室，观摩检修/智造流程、听劳模故事；科普分享+家风宣讲+亲子互动，让家属成发展见证者支持者。"),
 dict(title="华能营口电厂「三十华诞」国企开放日（150+职工家属）", url="https://www.toutiao.com/article/7596990196597228032",
      sourceType="secondary", relation="supervisor",
      summary="第一书记致辞感谢家属；电力科普游园会猜安全规程；家属戴安全帽进主控室看发电流程与保供责任，亲历「守护灯火」价值。"),
 dict(title="国能孟津热电2026企业开放日暨环保开放日（企民+家企双场）", url="https://www.thepaper.cn/newsDetail_forward_33699250",
      sourceType="secondary", relation="supervisor",
      summary="上午面向伙伴/群众展示一主两翼+超低排放治理；下午家属专场结合八一走进集控/质检/运维一线，打通大家与小家、厚植拥军文化。"),
 dict(title="科环集团2026品牌开放日·龙源技术专场（客户+对标企业+媒体）", url="https://lyjs.chnenergy.com.cn/lyjsww/jygl/202608/95309634c28042b085cd4dc6c74f59c1.shtml",
      sourceType="primary", relation="supervisor,exec",
      summary="国家能源集团官网：启幕+客户证言+数字展厅+产线探访四段式展现28年节能环保积淀；标杆客户讲应用成效；坚持安全第一简约高质廉洁合规办会。"),
 dict(title="中国铁塔「走进新国企·探秘数智铁塔」企业开放日", url="https://www.china-tower.com/Index/show/catid/17/id/1704.html",
      sourceType="primary", relation="supervisor",
      summary="国资委新闻中心指导：媒体+意见领袖+用户代表走进展厅与超级/储能基站一线，以「数字生命线/韧性网络」国家叙事替代自夸，站位高传播广。"),
 dict(title="口子窖77周年「大厂开放日·邀你来探厂」（媒体+伙伴沉浸探秘）", url="https://www.ahnews.com.cn/dangjian/pc/con/2026-07/17/548_1775226.html",
      sourceType="secondary", relation="supervisor",
      summary="媒体+核心伙伴沉浸探厂：博物馆/智能酿造/地下酒库全链路，投壶套圈品鉴沙龙破刻板；「真大厂·长期主义」反差定位+答谢晚宴情感收尾。"),
 dict(title="中国联通内蒙古2026国企开放日主场（公众+媒体+政企）", url="https://m.northnews.cn/p/2511928.html",
      sourceType="secondary", relation="supervisor",
      summary="专利荣誉墙+双核智算园区+行业AI落地案例展；文创周边成打卡点；参观后交流环节现场答疑并承诺专人对接，开放日转合作线索。"),
 dict(title="南航吉林「亲和精细 南航相伴」媒体开放日（核心业务沉浸体验）", url="https://so.html5.qq.com/page/real/search_news?docid=70000021_4636a0f0bc897352",
      sourceType="secondary", relation="supervisor",
      summary="记者亲历飞行训练/客舱/航食一线；A320静态模拟舱还原失火释压撤离场景，以「亲和精细」服务标准落地可感知安全与体验。"),
 dict(title="纳微科技2026投资者开放日（百余家机构实地参访）", url="https://www.sohu.com/a/1051551327_122014422",
      sourceType="secondary", relation="exec",
      summary="董事长领衔管理层全员出场，战略宣讲+研发中心实地参访+互动问答，展示向分离纯化整体方案商转型；硬科技实地参访建机构信任。"),
 dict(title="新乡化纤关于举办投资者开放日活动的公告（官方披露范式）", url="https://www.cnfin.com/announ/detail/index.html?dannoun=lcdetail&id=835371270308",
      sourceType="primary", relation="exec",
      summary="公告即SOP：明确时间/地点/方式/出席人员/报名/合规六要素；现场提交问题+承诺函签署+身份查验；参观生产线+菌草基地眼见为实。"),
]

# dedup: skip if url already present
existing = {x.get("url","").strip() for x in d}
added=[]
for n in new:
    if n["url"] in existing:
        print("SKIP dup:", n["title"])
        continue
    n["normKey"] = norm(n["title"])
    d.append(n)
    added.append(n["title"])

json.dump(d, open(PATH,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
print("total now:", len(d))
print("added:", len(added))
for a in added:
    print(" +", a)
