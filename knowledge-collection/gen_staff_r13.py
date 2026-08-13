# -*- coding: utf-8 -*-
import io, os

HTML_PATH = 'staff-meeting/staff-meeting.html'
TMP_PATH  = 'staff-meeting/.run_newcards.tmp.html'

# ---------- SEC3 (高管间 / exec) : 3 cards ----------
sec3_cards = []

sec3_cards.append('''<div class="hl">
      <div class="top"><span class="emoji">📖</span><h3>高管该讲的 3 类故事（First Round Review）</h3><span class="cat">叙事模板</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
      <p class="val">First Round Review——创始人/高管在全员大会该讲的 3 类故事：①榜样故事（讲"践行价值观的员工"让价值观成公司传说，Facebook 实习生故事被讲几十次、Pinterest CEO 每次全员会开讲一个客户故事）②认可故事（把高潜员工故事讲出来→动机 hyperdrive+团队榜样）③励志故事（连接个人与组织宏大目标，防规模期关系断裂）。关键：重复讲、由管理者学会讲、从"小处见大"慢慢 zoom out 串到使命。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">建"故事库"收集一线践行价值观的真实案例；全员会固定留 5 分钟讲一个客户/员工故事而非念指标；让管理者也学讲；故事要重复讲成公司传说。</div></details>
      <div class="src">🔗 <a href="https://firstround.com/review/the-pivotal-stories-every-startup-leader-should-be-able-to-tell/" target="_blank">firstround.com/review/the-pivotal-stories-every-startup-leader-should-be-able-to-tell</a></div>
      <div class="note">适用：③ 高管用故事（而非口号）把价值观与战略"讲进"团队，避免文化停留在墙上。</div>
    </div>''')

sec3_cards.append('''<div class="hl">
      <div class="top"><span class="emoji">🎯</span><h3>季度全员会 OKR 对齐（Kdan Mobile CEO）</h3><span class="cat">目标对齐</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
      <p class="val">Kdan Mobile CEO 分享全员会 OKR 复盘范式（170+人，2h+ 仍高参与）：①CEO 不抢戏——部门 head 更新产品进展/路线/下季计划，CEO 只答最尖锐问题+讲战略 ②不指责（公开 blame 最伤士气）③未来导向（回顾上季更要展望下 90 天）④互动公平——会前在共享文档收问题，现场抽签编号作答，确保内向者也参与 ⑤现场表彰团队。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">季度全员会设为 OKR 对齐主场；部门 head 主讲、CEO 只答难题；用共享文档+抽签让所有人（含内向者）的问题被公平回答；禁止公开指责；会前收问、现场表彰。</div></details>
      <div class="src">🔗 <a href="https://www.linkedin.com/pulse/inspiring-performance-through-quarterly-okr-meetings-kenny-su" target="_blank">linkedin.com/pulse/inspiring-performance-through-quarterly-okr-meetings-kenny-su</a></div>
      <div class="note">适用：③ 高管用季度全员会做透明 OKR 对齐+表彰，避免变成 CEO 个人秀。</div>
    </div>''')

sec3_cards.append('''<div class="hl">
      <div class="top"><span class="emoji">🌐</span><h3>多语言全员会包容性四步（Interpretwise）</h3><span class="cat">全球同步</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
      <p class="val">多语言全员会包容性四步：①提前规划语种+给译员材料+清晰说明同传用法 ②打破单一语言/时区——为主要语言提供同声传译、支持多语实时 Q&A ③录全音轨+多语字稿，让不同时区点播完整体验 ④人工同传（高规格高管沟通）vs AI 翻译（快/便宜）按会重要性混合。现代 RSI 平台基于浏览器、用手机+耳机即可，无需实体隔间。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">全球全员会前定语种、briefing 译员；用支持多语 Q&A 的平台；录制含全音轨+多语字稿；按会议重要度选人工/AI 同传；无需特殊硬件。</div></details>
      <div class="src">🔗 <a href="https://www.interpretwise.com/blog/run-multilingual-town-hall" target="_blank">interpretwise.com/blog/run-multilingual-town-hall</a></div>
      <div class="note">适用：③ 跨国/多语言组织高管办包容性全员会，破单一语言时区排斥。</div>
    </div>''')

# ---------- SEC2 (上下级 / supervisor) : 10 cards ----------
sec2_cards = []

sec2_cards.append('''<div class="hl">
      <div class="top"><span class="emoji">📖</span><h3>任正非叙事艺术·员工大会赋能（华为）</h3><span class="cat">叙事框架</span><span class="badge r2">上下级</span><span class="badge r3">高管间</span><span class="badge b2">二手</span></div>
      <p class="val">任正非在员工大会用故事"赋能"——①"晒钱"故事（阳台要大、钱会发霉，兑现后华为高薪成向往）②军事术语讲组织/人才/战略，反复讨论成管理文化 ③"干就完了"面对封锁的定力叙事。核心：会讲故事的人更具领导力，故事传情感、建信任连接；"一个好故事胜过百万雄师"。华为把讲故事当给员工"赋能"的方式，力出一孔、利出一孔。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">高管在员工大会用具体故事（而非口号）承载战略与激励；可准备 2-3 个反复讲的"公司传说"级故事；故事要真、要兑现；用叙事把个体努力连到组织大图。</div></details>
      <div class="src">🔗 <a href="https://m.dtm.com.cn/news/202601/165370.html" target="_blank">m.dtm.com.cn/news/202601/165370.html</a></div>
      <div class="note">适用：②+③ 高管/leader 用真实叙事（任正非范式）在员工大会点燃组织活力，故事>口号。</div>
    </div>''')

sec2_cards.append('''<div class="hl">
      <div class="top"><span class="emoji">🤝</span><h3>全员会帮新人融入（All-Hands Onboarding）</h3><span class="cat">新人融入</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">用全员会帮新人融入：新人入职 2 周-1 月后开 all-hands，问其 pet peeves/反馈偏好帮定制互动；配 30 天 mentor；跨部门 orientation 建连接；与高管 coffee date 让新人感被重视+看战略；60 天调研优化 onboarding；前 6 月刻意表彰 big wins。核心：全员会是新人"被看见、被连接"的第一现场。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">新人入职 1 月内安排全员会亮相+问答；配 mentor；安排与高管的非正式 coffee；60 天做 onboarding 调研；前半年持续 shout-out 新人的 early wins。</div></details>
      <div class="src">🔗 <a href="https://www.jobshopsf.com/post/welcoming-new-employees" target="_blank">jobshopsf.com/post/welcoming-new-employees</a></div>
      <div class="note">适用：② leader/HR 用全员会做新人融入与连接，降低早期流失。</div>
    </div>''')

sec2_cards.append('''<div class="hl">
      <div class="top"><span class="emoji">🦺</span><h3>班前会"五个一分钟"安全法（西北工业集团）</h3><span class="cat">一线安全</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">西北工业集团一线班组长"五个一分钟"高效班前会：①仪容自查互检（唤醒安全状态）②生产任务布置（当日工序+风险点+防控）③警示教育（案例举一反三）④亮点推广（表扬安全突出者分享窍门）⑤安全口号共鸣（集体宣誓"我的安全我负责"）。配"安全质量积分卡"隐患有奖、违章重罚，推动班组安全从被动执行→自主管理。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">班前会固化为"五个一分钟"仪式；每日宣 1 个风险点+对应防控；当场表扬安全亮点并复制；用积分卡把隐患上报/违章纳入绩效，激发内生动力。</div></details>
      <div class="src">🔗 <a href="https://www.sina.cn/news/detail/5313651721634400.html" target="_blank">sina.cn/news/detail/5313651721634400.html</a></div>
      <div class="note">适用：② 一线/班组长用"五个一分钟"班前会把安全质量文化落到最小单元（契合质量稳定性文化）。</div>
    </div>''')

sec2_cards.append('''<div class="hl">
      <div class="top"><span class="emoji">🌅</span><h3>"徽州早安"班前安全会·五必讲（官方一手）</h3><span class="cat">一线安全</span><span class="badge r2">上下级</span><span class="badge b1">一手</span></div>
      <p class="val">黄山市徽州区推广"徽州早安"班前安全会（全区 353 家企业+21 项目常态运行，累计 5200+ 场、排查隐患 260 条）：①编制方案定"五必讲"（讲上班安全/现场措施标准/违章警示/特种岗位要求/当班责任）②"察言观色+酒精检测+班前谈心+违章追溯"人员状态排查，已阻止 12 名状态异常者上岗 ③班前 15 分钟≥，高风险岗延长。把班前会做成"安全前置"闭环机制。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">班前会制度化为"五必讲"+人员状态四排查；带班负责人照单落实；班前 15 分钟雷打不动；与数字化平台融合实现风险清单动态更新。</div></details>
      <div class="src">🔗 <a href="https://www.ahhz.gov.cn/zxzx/mtkhz/9312344.html" target="_blank">ahhz.gov.cn/zxzx/mtkhz/9312344.html</a></div>
      <div class="note">适用：② 政府/企业一线用"徽州早安"班前安全会模式把人的不安全行为阻隔在作业前（官方一手范式）。</div>
    </div>''')

sec2_cards.append('''<div class="hl">
      <div class="top"><span class="emoji">🏭</span><h3>班前会安全标准化（涟钢热轧板厂）</h3><span class="cat">一线安全</span><span class="badge r2">上下级</span><span class="badge b1">一手</span></div>
      <p class="val">湖南钢铁涟钢热轧板厂班前"固定动作"安全文化建设：①班前"三查"（劳保穿戴/精神状态/个人措施）②安全宣誓+随机抽背岗位规程 ③看安全事故教育视频 ④厂/车间两级督导+选树典型以点带面。用 20 分钟班前会把"安全规程"变肌肉记忆，由安全班组建设带动全厂安全文化。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">一线班组班前会标准化：三查→宣誓→抽背规程→看警示视频；建厂/车间两级督导机制；定期培训安全员+选树典型复制。</div></details>
      <div class="src">🔗 <a href="http://www.csteelnews.cn/qypd/gl/202504/t20250401_98537.html" target="_blank">csteelnews.cn/qypd/gl/202504/t20250401_98537.html</a></div>
      <div class="note">适用：② 制造型企业用班前会安全标准化（三查+宣誓+抽背）筑牢一线安全文化（中国冶金报一手）。</div>
    </div>''')

sec2_cards.append('''<div class="hl">
      <div class="top"><span class="emoji">🌍</span><h3>分布式全员会·录制+时区轮转（Atlassian）</h3><span class="cat">远程平权</span><span class="badge r2">上下级</span><span class="badge b1">一手</span></div>
      <p class="val">Atlassian 把月度本地全员会改成每周 30 分钟全员会实验：①时区——选覆盖 80% 的时段+全程录制，Austin/Amsterdam/Yokohama 次晨配公司早餐回看，建各办社区感 ②异地团队提前录好 presentation 会中播放 ③A/V 自建直播系统（live-stream 到各办+可切源+可 YouTube 直播+远程控场）④Q&A 改提前提交+up-vote，exec 现场答最多票。还用新人照片/周年/10 年"roast"视频开场暖场。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">全球分布式全员会：固定录制+非时区办次晨早餐回看；异地演讲提前录播；自建直播切源系统；Q&A 提前收集+投票排序；用新人/周年/里程碑视频开场。</div></details>
      <div class="src">🔗 <a href="https://wp.me/pgkE99-aFm" target="_blank">wp.me/pgkE99-aFm</a></div>
      <div class="note">适用：② 分布式/跨国团队用"录制+时区轮转+提前录播+投票Q&A"办人人可参与的全局全员会（Atlassian 一手）。</div>
    </div>''')

sec2_cards.append('''<div class="hl">
      <div class="top"><span class="emoji">🎤</span><h3>吐槽大会·领导包容接招（信阳文旅集团）</h3><span class="cat">创新形式</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">信阳文旅集团第二届吐槽大会：员工分组"整活"吐槽职场难题（电梯没空调/食堂油咸/找领导等叫号机/付款流程多/停车贵…），负责人吕舜上台"接招"——"吐的是槽点更是心声，把吐槽点变工作着力点，让槽点越来越少、点赞越来越多"。把情绪出口变成问题源头，领导包容接招换凝心聚力。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">办"吐槽大会"作全员参与渠道：员工用短视频/PPT/单口轻松开麦；领导现场接招并承诺从琐事改起；把吐槽点立项为工作着力点闭环；忌走过场、忌秋后算账。</div></details>
      <div class="src">🔗 <a href="https://ribao.xyxww.com.cn/html/2024-08/03/content_145210.htm" target="_blank">ribao.xyxww.com.cn/html/2024-08/03/content_145210.htm</a></div>
      <div class="note">适用：② 领导用"吐槽大会"接住员工真声音（信阳文旅一手案例），把情绪出口转治理入口。</div>
    </div>''')

sec2_cards.append('''<div class="hl">
      <div class="top"><span class="emoji">🗣️</span><h3>青年吐槽大会·听 95/00 后真声（中交一航局二公司）</h3><span class="cat">创新形式</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">中交一航局二公司预制分公司在青年座谈冷场后，按青年方式办"吐槽大会"——场地从会议室挪到活动室、沙发环形、自带奶茶，唯一保留移动麦；青年敞开吐槽（导师常年在外/食堂菜谱不动/培训用老旧课件），支部书记将吐槽转为人才金点子，定为每月固定节目，后老员工/中层也加入，频次从月→周→随时开麦。"吐槽不是开完就结束，重点得有举措。"</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">青年/新生代沟通换"他们的语言"：用开放麦/吐槽大会替代正式座谈；环形松弛场地+移动麦；领导真听并把吐槽立项；形成"随时开麦"机制而非一年一次。</div></details>
      <div class="src">🔗 <a href="https://lanjingshare.qtvnews.com/share-html/lanjing/share/newsDetailsLj.html?id=16646871" target="_blank">lanjingshare.qtvnews.com/.../newsDetailsLj.html?id=16646871</a></div>
      <div class="note">适用：② 领导/HR 用"吐槽大会"听见 95/00 后真声（中交一航局二公司案例），吐槽→金点子闭环。</div>
    </div>''')

sec2_cards.append('''<div class="hl">
      <div class="top"><span class="emoji">📊</span><h3>500人年度大会·实时投票+词云（案例）</h3><span class="cat">现场互动</span><span class="badge r2">上下级</span><span class="badge b2">二手</span></div>
      <p class="val">某互联网公司 500 人年度大会用"实时投票+词云"破互动困局：①开场词云收"年度关键词"（3 分钟全员进状态）②正式环节实时投票选"年度之星"（大屏柱状图实时跳、悬念留到最后）③收尾词云凝"新年愿望"，CEO 当场回应高频词纳入规划。从"低头刷手机"到"抬头看大屏"，问卷回收率从<30% 提升。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">大型全员会嵌实时互动：开场词云暖场、核心评选用实时投票（大屏动态排名造悬念）、收尾词云收愿望且 leader 当场回应；用扫码即投、无需 APP。</div></details>
      <div class="src">🔗 <a href="https://www.shougan.net/docs/use-cases/internet-company-annual-meeting" target="_blank">shougan.net/docs/use-cases/internet-company-annual-meeting</a></div>
      <div class="note">适用：② 大型全员会/年会用实时投票+词云让 500 人同时参与、声音被即时看见。</div>
    </div>''')

sec2_cards.append('''<div class="hl">
      <div class="top"><span class="emoji">🔄</span><h3>运营节奏·QBR 替代全员会（Skillshare）</h3><span class="cat">沟通节奏</span><span class="badge r2">上下级</span><span class="badge b1">一手</span></div>
      <p class="val">Skillshare 运营节奏把全员会分层：①季度末用半天 QBR 替代常规 town hall——复盘上季+定下季优先级，预留半天团建 ②月度 all-hands（月末周五）hijack 周会 review 财务/关键指标+「Ask Skillshare Anything」自由提问 ③OKR 半年度制定、月度更新（个人→部门→公司对齐）④周/双周部门会+周一 BizOps 看板跟踪 OKR+管理会 flex agenda/周三月会深潜。远程 20% 成员每半年至少飞一次 QBR。</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">把全员会按节奏分层：季度 QBR（半日复盘+团建）、月度 all-hands（指标+自由问）、周 departmental；用 OKR 串个人→公司；远程成员定期飞聚；配看板跟踪。</div></details>
      <div class="src">🔗 <a href="https://coda.io/@matt-cooper/staying-connected-and-strategically-consistent-in-a-remote-workplace/staying-connected-and-strategically-consistent-in-a-remote-workp-1" target="_blank">coda.io/@matt-cooper/.../staying-connected-and-strategically-consistent-in-a-remote-workp-1</a></div>
      <div class="note">适用：② Leader 用"QBR+月度all-hands+周部门会"分层节奏让全员会不超载、战略一致（Skillshare 一手）。</div>
    </div>''')

# ---------- assemble ----------
all_cards = sec3_cards + sec2_cards
tmp_html = '\n'.join(all_cards) + '\n'
with io.open(TMP_PATH, 'w', encoding='utf-8') as f:
    f.write(tmp_html)
print("wrote tmp:", TMP_PATH, "cards:", len(all_cards))

# ---------- insert into wall ----------
html = io.open(HTML_PATH, encoding='utf-8').read()
marker = '<div class="sec sec2">'
idx = html.index(marker)
sec3_part = html[:idx]
sec2_part = html[idx:]

# insert sec3 cards before sec3 grid close (last </div> in sec3_part)
last3 = sec3_part.rfind('</div>')
sec3_part = sec3_part[:last3] + '\n' + '\n'.join(sec3_cards) + '\n  ' + sec3_part[last3:]

# insert sec2 cards before sec2 grid close (last </div> before <footer>)
footer_idx = sec2_part.index('<footer>')
last2 = sec2_part.rfind('</div>', 0, footer_idx)
sec2_part = sec2_part[:last2] + '\n' + '\n'.join(sec2_cards) + '\n  ' + sec2_part[last2:]

new_html = sec3_part + sec2_part

# update hero
new_html = new_html.replace(
    '采集于 2026-08-12（十一轮补采 +11）',
    '采集于 2026-08-13（十三轮补采 +13）')

# update counts
new_html = new_html.replace('<span class="tag">31 卡</span>', '<span class="tag">34 卡</span>')
new_html = new_html.replace('<span class="tag">89 卡</span>', '<span class="tag">99 卡</span>')

io.open(HTML_PATH, 'w', encoding='utf-8').write(new_html)
print("wall updated. sec3+3, sec2+10, total 133")
