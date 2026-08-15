# -*- coding: utf-8 -*-
# 员工大会 第十六轮（+11）入库 index.json
import json, os, re

BASE = os.path.dirname(os.path.abspath(__file__))
IDX = os.path.join(BASE, 'index.json')

def norm(t):
    t = t.strip().lower()
    t = re.sub(r'[，。、：；！？·\.\,\:\;\!\?\(\)（）/／]', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

entries = [
  dict(title="南方电网2026年中工作会（腾讯新闻现场报道）",
       url="https://new.qq.com/rain/a/20260803A04REY00",
       sourceType="secondary", relation="supervisor,exec",
       summary="南方电网8月1日召开2026年中工作会，董事长钱朝阳讲话、总经理季明彬主持并讲话，传达全国党建座谈会与中央企业负责人研讨班精神，锚定十五五航向部署下半年；提出国家战略贯彻者/能源强国建设者/现代产业引领者/改革创新先行者/万家灯火守护者五定位，聚焦能源强国/一流企业/科技产业创新/六网协同/全面深化改革五方向，强调一张蓝图干到底；季明彬要求层层压实责任、一级抓一级。真实央企高管↔全员战略沟通场景（权威媒体报道）。",
       source="腾讯新闻", topic="staff-meeting"),
  dict(title="字节跳动CEO梁汝波全员信：刷新文化+10条领导力原则（2026）",
       url="https://caifuhao.eastmoney.com/news/20260630153230934220020",
       sourceType="secondary", relation="supervisor,exec",
       summary="2026年6月29日梁汝波时隔四年再发全员信，刷新适配AI变革的文化与领导力准则：使命仍为激发创造丰富生活，补上从推荐时代到AI时代践行使命方法一致（计算换智能、智能提创造力）；管理理念沉淀为业务战略/组织管理/人才策略/公共事务四部分；新版10条领导力原则补充做有高度的事/敢于设定高目标、把有危机感保持外部视角/深入一线列为独立条目、强调Context over Control；原则纳入晋升与年度考核，脱离业务一线管理层同步调整权责。",
       source="东方财富", topic="staff-meeting"),
  dict(title="CEO如何向员工沟通并购（不引发恐慌的7步）",
       url="https://www.straighttalk.marketing/post/how-ceos-should-communicate-an-acquisition-to-employees-without-sparking-panic",
       sourceType="secondary", relation="exec",
       summary="并购/收购员工沟通框架：①快且透明——签约即宣布、说已知承认知未知、承诺定期更新，沉默=secrecy；②讲战略故事而非仅头条——why与对员工好处，避免空谈synergies；③正面回应岗位安全与文化——诚实讲重组/汇报变化、别讲一切不变；④CEO亲自发声——全员town hall/视频会+团队级答疑+远程录播；⑤给下一步与匿名Q&A渠道；⑥示文化尊重用走到一起而非接管；⑦高频跟进（周/双周更新+庆祝小胜）。核心塑造员工对未来的感受。",
       source="straighttalk", topic="staff-meeting"),
  dict(title="All-Hands/Town Hall 设计实践（领导力沟通 playbook）",
       url="https://raganmcgill.co.uk/c4e/leadership/Practice/practice-all-hands-and-town-hall-design",
       sourceType="secondary", relation="supervisor,exec",
       summary="RaganMcGill 把全员会/town hall 定义为刻意设计成双向参与而非广播的领导力实践：会前问听众最需理解/最担心/我们需听到什么，至少留30-40%时间给问答与对话；匿名提交让真问题浮出；领导者为硬问题备诚实直答不回避；会后速发书面摘要含跟进承诺。演进：每场后短调研、轮换主讲/主持、大群体用实时投票或分组讨论。成功信号：硬问题被诚实回答、承诺被可见兑现、员工被理解（知其所以然）。",
       source="RaganMcGill", topic="staff-meeting"),
  dict(title="全员会三段式议程（Community/Business/Q&A）+ Etsy开场秀",
       url="https://slab.com/blog/all-hands-meetings",
       sourceType="secondary", relation="supervisor",
       summary="Slab 全员会议程分三段：I.Community（10-15%）——非结构开场暖场（Etsy用opening act员工才艺制造脆弱exchange与连接感）、新人介绍、里程碑/生日庆祝、按价值观点名shoutout；II.Business（55-65%）——重申purpose（不讲PPT，改团队讲难题/客户讲价值/投资者讲理由）、讲指标（团队讲initiative如何关联指标）；III.Live Q&A（20-25%）——匿名提交、远程同权答、Slack会后追问。建议轮换演讲者、提前测tech。",
       source="Slab", topic="staff-meeting"),
  dict(title="当代全员会环节库（客户聚焦/Sli.do问答/文化故事/月度数据）",
       url="https://lattice.com/de/articles/how-to-organize-a-more-successful-contemporary-all-hands-meeting",
       sourceType="secondary", relation="supervisor",
       summary="Lattice 高人气全员会环节：Customer spotlight（新客户谁/为何选我们，建客户同理心）、Photo of the month（远程工位/客户现场拉近距离）、Leadership Q&A（Sli.do或Slack提前收问题+upvote排序，须定是否匿名政策）、Culture stories（体现文化最佳面向的故事）、Anniversaries（周年员工讲故事+老照片）、Data of the month（一张图表+有人讲）。强调会完即规划下一届、用Airtable管内容、一次只改一个点增量迭代。",
       source="Lattice", topic="staff-meeting"),
  dict(title="HubSpot 式全员会指南（节奏+议程+匿名Q&A）",
       url="https://consultevo.com/hubspot-all-hands-meeting-guide",
       sourceType="secondary", relation="supervisor",
       summary="HubSpot 式全员会：目标=战略更新（讲why非仅结论）+亮点与教训（own失策）+强化文化（故事非口号）+双向通道。节奏：月度全员/季度深潜/临时town hall（重大发布/并购/危机）。议程模板：欢迎定调5m→指标进展10-15m→产品项目聚焦10m→客户员工故事10m→表彰5-10m→开放Q&A10-20m→收尾5m。Q&A：匿名表单+公开投票+直播chat、会前发链接分组、会后书面汇总。",
       source="HubSpot(consultevo)", topic="staff-meeting"),
  dict(title="让大型内部会议更吸引人的19招（Forbes Council）",
       url="https://www.forbes.com/councils/forbesbusinesscouncil/2025/02/26/how-companies-can-make-large-scale-internal-meetings-more-engaging",
       sourceType="secondary", relation="supervisor",
       summary="Forbes商业委员会19位成员方法：客户/患者故事开场连使命；会议当迷你学习市集（贡献者station轮转）；电视节目分Good News Network/Behind the Scenes/AMA三段保能量；提前给议题让团队带贡献来；趣味主题（如Back to the Future租DeLorean+cosplay讲转型）；互动元素（live Q&A/投票/故事）；任命有感染力leader当host；聚焦驱动使命的人做spotlight；故事把工作连到真实的人；KPI连回对人的影响；请使命一致外部分享者破信息茧房。",
       source="Forbes Council", topic="staff-meeting"),
  dict(title="麦当劳（台湾）董事长年度员工信：真诚+危机后交心",
       url="https://news.mcdonalds.com.tw/news/20250203/index.html",
       sourceType="secondary", relation="supervisor",
       summary="台湾麦当劳历任最高负责人每年农历年后给全员写信，2018起由董事长李昌霖接续。2025初经历震撼品牌事件后，信直白写道麦当劳由25000名麦胞共同打造、应用最高标准守护每位伙伴确保安全透明快乐职场，对让麦胞担心/粉丝失望没有任何借口必须彻底检讨并有具体改革作为——已责成全面检视职场安全/申诉流程/身心照护并请益专业非营利组织。把真诚内化为不自满落实日常。一把手以信交心、危机后坦诚担责的上下级信任修复样本。",
       source="麦当劳(台湾)", topic="staff-meeting"),
  dict(title="全员会是什么·目的收益与常见误区（Glints）",
       url="https://talenthub.glints.com/en-sg/blog/all-hands-meeting",
       sourceType="secondary", relation="supervisor",
       summary="Glints 全员会定义与最佳实践：目的=同步方向/知角色/有提问反馈论坛；清晰可达语言（避jargon/未解释财务术语）；不同演讲者（部门负责人/项目负责人/客户face员工）；互动（live poll/短调查/员工presentation/提前提问）；留足Q&A（答不了承认并承诺跟进）；诚实讲难题（岗位安全/财务/决策/薪酬/组织变化，机密待定就明说）；包容性（全球混合考虑时区/语言/字幕/录制）；会后跟进（含决策/行动项/未答问题摘要+录制+材料）。常见误区：信息过载/单向广播/只讲正面/细分详审/不回应反馈/无明确目的。",
       source="Glints", topic="staff-meeting"),
  dict(title="让全员会更有影响力的8个要素（PeopleWiseHR）",
       url="https://peoplewisehr.com/post/maximizing-the-impact-of-all-hands-meetings",
       sourceType="secondary", relation="supervisor",
       summary="PeopleWiseHR 8要素：①明确目的（更新/庆祝/攻坚）；②建透明（公开成绩与挑战、分享绩效指标/新举措/待改进）；③跨团队亮点（点名个人团队成就boost士气）；④留双向空间（live或预提交Q&A）；⑤保持参与感（互动投票/视频/团建，虚拟用breakout）；⑥聚焦愿景文化（提醒bigger picture与贡献意义）；⑦倡导福祉（顶部强调work-life balance与心理健康，支持文化自上而下）；⑧会后跟进（摘要邮件/录制显领导commitment）。核心透明+参与+双向。",
       source="PeopleWiseHR", topic="staff-meeting"),
]

for e in entries:
    e['normKey'] = norm(e['title'])

d = json.load(open(IDX, encoding='utf-8'))
before = len(d)
for e in entries:
    d.append(e)
after = len(d)
json.dump(d, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
# 校验所有新 URL 唯一
urls = [e['url'] for e in d if isinstance(e, dict)]
assert len(urls) == len(set(urls)), 'dup url!'
sm = [e for e in d if isinstance(e, dict) and e.get('topic') == 'staff-meeting']
print('index before=%d after=%d | staff-meeting topic count=%d | added=%d' % (before, after, len(sm), after - before))
