# -*- coding: utf-8 -*-
# 员工大会 · 第三十轮补采（r30, 2026-09-02）+7 卡：4 ②上下级(含2一手) + 3 ③高管间(含1机构一手)
# 新域：Teams Q&A 官方配置 / 目的性匿名治理 / 负面评论治理(该不该取消匿名) / 实时字幕CART安排(政府一手)
#      / 管理者级联包 / 艰难决定5拍+72h+14天 / 战略翻译4步+仪表盘5问
import re, os, json, subprocess, sys, urllib.request, urllib.error

WS = r"C:\Users\v_yitcai\WorkBuddy\20260728154244"
KC = os.path.join(WS, "knowledge-collection")
HTML = os.path.join(KC, "staff-meeting", "staff-meeting.html")
TMP  = os.path.join(KC, "staff-meeting", ".run_newcards.tmp.html")
IDX  = os.path.join(KC, "index.json")
OB_SUM = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\staff-meeting\员工大会-知识卡汇总.md"
OB_IDX = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
OB_RUN = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\staff-meeting\runs\员工大会-2026-09-02-第三十轮-知识卡.md"
GH = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/staff-meeting.html"
GH_RUN = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/runs/staff-meeting-2026-09-02-r30.html"
DATE = "2026-09-02"
ROUND = "30"
ROUND_CN = "第三十轮"

cards = [
 dict(emoji='🛠️', title='Teams 全员会 Q&A 官方配置全解（审核/匿名/上投票/报告）', cat='工具官方',
      rel='r2', src='一手', src_cls='b1',
      url='https://support.microsoft.com/en-us/teams/meetings/q-a-in-microsoft-teams',
      val='微软官方文档：大型结构化会议（town hall / webinar）用 Q&A 而非聊天来管提问。开启入口三处——Outlook 新日历事件 → Meeting Options → Enable Q&A；Teams 日历 → View event → Options → Participation 打开 Q&A；会中 Controls → View more options → Participation。最佳实践：加 co-organizers 帮你审核；不想双通道就把 meeting chat 设为 Off，只留 Q&A。town hall/webinar 可用「Who can manage Q&A」把审核权开给 presenter，会前/会中/会后随时可改、无人数上限（限本组织或有 M365 登录的外部主持人）。开 moderation 后 Q&A 面板出现三个 tab：In review / Published / Dismissed（被 dismiss 的问题之后仍可发布）；private replies 默认随审核开启，仅审核员与提问者可见，问题一旦 publish 私回即删，匿名帖不支持私回。审核员可用本人或「Organizer」统一身份回答（对参会者与其他组织者隐藏姓名，但下载报告里仍可追溯，合规留痕）。上投票每人每问一次、可按 Most upvoted 排序、可整体关闭。匿名提问/匿名评论是两个独立开关：匿名帖组织无法追踪，随后关闭开关不影响历史匿名；匿名评论无法被审核；对匿名问题的回复与表情不匿名——官方建议关掉 reactions 以保匿名。超容量的 view-only 参会者看不到 Q&A；周期性会议可 archive 问题；会后可下载 Q&A 报告。',
      how='办 500 人以上全员会先在日历事件里开 Q&A、把 meeting chat 关掉，只留一条提问通道；指定 2 名 co-organizer 当审核员，开 moderation 走 In review → Published；敏感场次打开匿名提问但同时关掉 reactions（否则表情会暴露身份）；用 Most upvoted 排序决定现场答哪些；会后导出 Q&A 报告，把没答到的问题逐条书面回复——这一步是信任杠杆。周期性全员会记得 archive 上一期问题，避免旧问题混进新场。',
      note='② HR/IT/会议组织者（Microsoft 官方支持文档·一手）；Teams 全员会 Q&A——三处开启入口、moderation 三 tab、匿名与 reactions 冲突、上投票排序、报告导出。'),
 dict(emoji='🕵️', title='目的性匿名（Purposeful Anonymity）· 匿名不是开关是契约', cat='匿名治理',
      rel='r2', src='一手', src_cls='b1',
      url='https://blog.pigeonholelive.com/purposeful-anonymity-in-town-hall-qna',
      val='Pigeonhole Live 官方立场文档，把匿名分成两种：传统匿名（身份可能被追踪、自由被滥用；产出常不可行动甚至伤人；本质是"盾"，问责几乎归零）vs 目的性匿名（规则明确、设计上身份完全不可追溯、配保障机制防滥用；能浮出本来会被藏起的问题；本质是"桥"——员工敢说真话，领导承诺透明回应并偏向行动）。技术保证：SSO 登录与 IP 白名单只控制"谁能进会"，永不覆盖匿名，即使开了这些设置匿名回答仍不可回溯到个人。五条落地清单：①Start with the why——匿名不该常开，只在议题高风险/敏感、员工可能不敢说、权力距离形成障碍时开；②Set expectations clearly——提前讲清什么匿名什么不匿名、谁会看到、如何审核、会后如何处理，且会前/会中/会后都要重申；③选配对的工具并提前配好，现场不要调设置；④Prepare to respond well——谢谢每个提问包括难听的，不能行动的要解释为什么，让员工看到声音没进黑洞；⑤Always close the loop——会后回告哪些已处理、哪些将行动、哪些暂缓（parked）。数据：74% 员工在真匿名通道下更愿给反馈（Forbes）；感到被听见的员工 4.6x 更可能高绩效；对反馈采取行动的组织创新高 +80%（McKinsey）。',
      how='别把匿名当默认开关。先问"这场为什么需要匿名"，只对敏感议题开；开之前用一页话讲清四件事（什么匿名/谁能看/怎么审/会后怎么处理），会前会中会后各讲一次。会中对难听的提问先说谢谢再答，答不了就讲清约束。会后 3 个工作日内发闭环清单：已处理 / 将行动 / 暂缓+原因——这一步才是匿名从"盾"变"桥"的关键。工具侧确认匿名与 SSO/IP 白名单互不覆盖，并对匿名帖关掉表情反应。',
      note='② HR/内部沟通（Pigeonhole Live 官方产品立场文档·一手）；匿名治理——传统匿名 vs 目的性匿名，五步清单(为什么/讲清规则/提前配置/好好回应/闭环回告)。'),
 dict(emoji='🧯', title='全员会想「取消匿名压负面」？四类替代做法（从业者答疑）', cat='负面治理',
      rel='r2', src='二手', src_cls='b2',
      url='https://www.strictlyinternal.com/p/ama-managing-negative-comments-in-town-halls',
      val='真实提问：领导层倾向把全员会 Q&A 改成完全实名，以此打消负面或不建设性评论——内部沟通从业者的回答是这会同时牺牲心理安全与真实反馈，并给出四类替代：①正面立规而非事后压制——开场由领导引用公司价值观定调（"我们要建设性对话，请保持专业、与价值观一致"），不点名批评个人（除非行为真的不可接受）；同时对建设性提问实时正强化（"这正是帮我们挖到真问题的提问方式""我很欣赏你这个提法"）。②中间路线——会前匿名征集问题、会中实名提问混合使用；用审核员先收全部问题只发布合适的（过滤刻意挑事）；引导员工点赞/表情，负面评论得不到同伴点赞会自然形成规范（thumbs-down 要谨慎使用）。③检查格式本身——负面评论往往反映"不被听见"或对单向格式的不满；可加分组讨论/breakout、让更多层级员工而非只有高管参与 Q&A、引入业务其他线的嘉宾或外部讲者。④角色示范——全员会是高杠杆的示范场，跨层级真实对话被看到，就是在示范公司珍视什么样的坦诚；领导怕负面评论，先问自己为建设性对话创造了什么条件——把好对话的责任全推给员工是不成立的。',
      how='领导提"这次全员会 Q&A 改实名吧"，别直接照办。先给中间方案：会前匿名征集 + 会中实名 + 审核员过滤 双轨并行。开场 30 秒由领导引价值观定调，会中对好问题当场点名表扬（正强化比压制有效）。如果负面评论集中，回头查格式而不是查人——加 breakout、让一线员工也上台答、请外部嘉宾破单向。给领导一句话对齐：负面评论多，往往是"没被听见"的症状，不是纪律问题。',
      note='② HR/内部沟通/中层（Strictly Internal 从业者专栏·二手）；负面治理——取消匿名的代价与四类替代(正面立规/混合双轨/改格式/角色示范)。'),
 dict(emoji='📝', title='全员会实时字幕（CART）安排规范 · 24h 术语表是硬要求', cat='无障碍',
      rel='r2', src='一手', src_cls='b1',
      url='https://mn.gov/deaf-hard-of-hearing/communication-access/cart/index.jsp',
      val='明尼苏达州聋与听障服务司官方指南（可直接照搬到企业全员大会/培训/大型会议）。CART=受训认证的速录员用速录法把口语实时转成文字，显示在笔电/平板上，也可投到大屏供大群阅读，字号与配色可按个人需求调，速录员可现场或远程。关键区分：实时字幕 ≠ 自动语音识别（ASR/自动字幕），自动字幕可能不满足无障碍法定义务，要按提出需求者的实际需求走。费用归属明确：谁办活动谁安排谁付费，不得把账单转给提出需求的人。预约时必须提供的十项信息：联系人姓名/邮箱/电话（速录员要对接他）、活动日期时间、地点及现场or线上、速录员现场or远程、字幕给一人还是多人、如何交付（投大屏 or 每人一条链接）、活动主题、会用到的行业术语与黑话、全部发言人姓名及正确拼写、发票收件人与付款方式。现场执行：联系人负责架平板/笔电并接稳定有线网，速录员把观看链接发给联系人，多设备可同时看，要能帮人调字号配色，弱声讲者与提问者都必须用麦确保收音；线上执行：分发链接是联系人的责任，速录员需入会听音。协作规范：**活动前至少 24 小时**把参会名单、专业术语、讲稿材料、会议链接发给速录员；为速录员留工位与休息；讲话语速适中、吐字清楚、句间停顿；提问之间留空档让人读完字幕再回应；多讲者场合强制轮次发言并先报自己名字。',
      how='全员大会有听障或母语非中文的同事，别只靠会议软件自动字幕交差。提前 2-3 周确认是否有人需要专业实时字幕，按十项清单一次性把信息给到服务方（含发言人姓名拼写与业务黑话表）。会前 24 小时把讲稿/术语表/会议链接发给速录员——这是字幕质量的最大变量。现场备一块投影或给每人一条观看链接，弱声讲者与提问者一律用麦，多讲者强制"先报名字再说话"。费用由主办方出，绝不让提出需求的同事自付。',
      note='② HR/组织者/行政（美国明尼苏达州政府官方无障碍指南·一手）；无障碍——实时字幕(CART)与自动字幕的区别、十项预约清单、会前 24h 术语表、多讲者报名字规范。'),
 dict(emoji='📦', title='管理者级联包（Cascade Packet）· 全员会开完才算开了一半', cat='级联对齐',
      rel='r3', src='二手', src_cls='b2',
      url='https://www.antoinebuteau.com/all-hands-meetings-that-actually-run-the-company-series-8-the-manager-cascade-is-half-the-meeting/',
      val='全员会不在通话结束时结束，而在管理者能把消息翻译成本地决策且不失真时才结束。典型失败：领导层以为"全公司听到了同一条消息 = 全公司理解了同一条消息"，然后管理者带着残缺上下文走进团队会，面对全员会没回答的问题。正确动作是在全员会**之前**就把级联包搭好。员工很少停在"领导说了什么"，他们问的是"这对我们的路线图/配额/招聘计划/客户承诺/项目/绩效评估/预算/团队优先级意味着什么"。弱级联=转发一封备忘录，它假设管理者是管道；管理者其实是翻译者、意义构建者、优先级执行者、困惑探测器、反馈路由器。强级联包应含：核心消息、什么变了、什么没变、预期员工问题、可接受的回答边界、按职能的具体例子、决策规则、客户侧影响、未答问题的上行路径——会前就绪，不是等困惑出现才拼。裁员、未达标、重组、战略转向、包装变更、招聘冻结、质量问题、大客户流失时最关键：不该让管理者在实时对话中第一次撞见这些问题，那对他们不公平、对公司昂贵。级联还是反向传感器：如果管理者反馈团队都卡在同一个点，说明全员会没真正解决问题——这不是失败，是信号，下一封领导信/FAQ/经营复盘/全员会要回应它。要度量：管理者是否在会前收到包、是否开了跟进对话、哪些问题反复出现、哪些团队理解不一致、哪些本地取舍仍不清楚；否则领导层只能靠掌声和出席率判断效果。边界感很重要：管理者需要知道哪里有裁量权、哪里没有、哪些例子可以安全使用、哪些问题该上行、哪些承诺绝不能许——边界缺失会让本地即兴发挥变成事实政策。管理者与全员同时得知重要消息，就等于多出一批困惑观众；带明确保密预期地提前给上下文不是偏袒，是基础设施。',
      how='把级联包做成全员会的前置交付物而不是会后补丁：一页纸写清核心消息、变了什么/没变什么、预期问题+可接受回答边界、按职能的例子、决策规则、客户侧影响、上行路径。会前给管理者（明确保密预期），并明确三条边界：哪里可自主决定、哪些问题必须上行、哪些承诺绝不能许。会后收集四项信号：哪些问题反复出现、哪些团队理解不一致、哪些本地取舍不清、哪些例子好用；同一个问题反复出现就写进下一封领导信或下场全员会。管理者讲不清 = 消息本身还不够清楚，回去改消息不要怪管理者。',
      note='③ 高管/内部沟通负责人（Antoine Buteau 系列#8·二手）；级联对齐——会前就绪的级联包九要素、三条裁量边界、四项反向信号，管理者不是管道是翻译者。'),
 dict(emoji='⏱️', title='宣布艰难决定：第5拍要留下 + 72小时三动作 + 14天可见跟进', cat='危机沟通',
      rel='r3', src='二手', src_cls='b2',
      url='https://www.poweredby.com.au/blog/communicating-tough-decisions-without-losing-trust',
      val='五拍结构的最后一拍最常被做坏：开放提问后要**留下来**——问到没有问题为止，而不是日历上写的 15 分钟；提前离场坐实了"你们不想回答"的猜疑。更关键的是配比：全员会只占这件事的 20%，80% 发生在之后 72 小时里，三个动作决定结局——①中层先拿到 brief：不是会前两分钟，是**提前两天**，内容含背景、可能被问到的问题，以及那些"听起来无法自辩"的问题你会怎么答；中层是公告后一周里业务唯一会稳定听取的群体，不装备他们他们就帮不上。②书面记录要精确且公开：公告后 24 小时内发一份文字，重申核心决定、理由与承诺——书面消息会被转发、被反复读，它才是真正的记录，全员会不是。③跟进要可见：公告里每一条具体承诺都应在 **14 天内**产出一个可见动作；跟进缺失是"下一次公告将被冷嘲"的最强单一预测因子。撑得住的领导姿态：不过度推销（"这是最好的前进方式"听起来像公关话术，"这是我们选择的路、原因是…、我理解它的代价"才落地成诚实；过度推销是"领导自己都不信这个决定"的最大破绽）；难的时候保持眼神接触（线下不看稿、线上不静音——情绪时刻正是组织判断你是认真还是表演的地方）；把"已定"和"仍开放"分清（"是否重组已经定了；如何支持受影响的人，我们想听你们意见"——这条能预防"到底有什么是真的可以反馈的"这种腐蚀性讨论）；90 天内亲自做跟进（第一周开放论坛、第一个月管理者级联、第一季进展更新，不外包给 HR 也不外包给 comms）。做坏的代价 18 个月后才显形：后悔性离职升高、变革采纳停滞、中层不再愿意传递难消息、整个文化开始"读字缝"。',
      how='有艰难公告要发（重组/裁员/目标未达/战略急转），提前一周让领导班子把五拍完整走一遍并**排练**；中层 brief 提前两天到手；公告后 24 小时内发书面版重申决定+理由+承诺；把每条承诺挂上 14 天内的可见动作与责任人。现场最后一拍不要卡表，问到没人举手再散。话术上砍掉"这是最好的选择"，换成"这是我们选的路、原因是 X、我知道代价是 Y"；明确区分"已决定"与"想听你们意见"的部分。90 天内的三次跟进（周/月/季）由决策人本人做，不要转给 HR。',
      note='③ 高管/HR 负责人（Powered by 咨询·二手）；危机沟通——第5拍留到问完、72h 三动作(中层提前2天/24h书面/14天可见跟进)、不过度推销、90天亲自跟进。'),
 dict(emoji='🔁', title='战略不是领导宣布的，是管理者重复的：四步 + 仪表盘 5 问', cat='战略落地',
      rel='r3', src='一手', src_cls='b1',
      url='https://greatplacetowork.me/your-strategy-is-not-what-leaders-announce-it-is-what-managers-repeat/',
      val='Great Place To Work 官方机构文章。断层出现的瞬间：领导层宣布 → 管理者和团队同时第一次听到 → 当天下午管理者被要求解释。四步把断层补上：①**公告前**就 brief 管理者，给四样东西：为什么这么决定、对他们团队什么变了、他们自己能决定什么、答不上的问题往哪送；然后做一次测试——请一位管理者用自己的话把决定讲一遍，如果他离开幻灯片就讲不出来，说明这次公告还没准备好。级联不是"消息发出去"就完成，是"管理者能撑住那场对话"才完成。②把价值观翻译成"真有事时能用的规则"：公平在"一个团队突然承担远超他人的工作量"时具体意味着什么，要说出口；信任=什么信息、对谁、多快公开，包括不舒服的信息；人优先=截止期与团队健康冲突时到底怎么办。员工不会因为价值观挂在墙上就信它，他们信的是"能预测领导在压力下的行为"。③让倾听可见：调研只能造出倾听的表象，信任建立在事后员工能看到的三件事——我们听到了什么、我们要做什么、什么现在还改不了；倾听之后的沉默会教会员工"参与只是象征性的"，这一课一旦学会要好几年才能教回来。④测一致性而非平均值：全公司一个漂亮的总分可以掩盖某个职能、某个地点、某个管理层级的糟糕体验；最有用的文化数据不是证明公司做得好，而是精确指出战略在哪里翻译丢失。应当上转型仪表盘的 5 个问题：管理者能否用自己的话讲出战略？员工是否知道对自己团队什么变了、为什么？领导消息在各职能各地点是否一致？高管、管理者、一线之间最大的信任差在哪？员工能否指出因为他们发声而发生的可见行动？这些是"能否通过人来执行"的最早期指标——等硬指标动的时候，翻译断层早已决定结局。',
      how='全员会公告前一天做一次"翻译测试"：抽 1-2 位管理者用自己的话讲一遍决定，讲不出就回去改消息（别改管理者）。给管理者的 brief 固定四要素：为什么/团队变什么/你能自己定什么/答不了往哪送。价值观别停在词上，挑三个高频冲突场景写成明规则（工作量失衡时怎么算公平、坏消息多快公开、截止期撞团队健康怎么选）。倾听后必发三段回告：听到了什么/要做什么/暂时改不了什么。度量改看一致性：按职能、地点、管理层级拆分看分差，把上面 5 个问题放进转型仪表盘。',
      note='③ 高管/HR 负责人（Great Place To Work 官方机构·一手）；战略落地——公告前 brief 四要素+翻译测试、价值观变明规则、倾听三段回告、按职能/地点/层级测一致性+仪表盘 5 问。'),
]

def card_html(c):
    url_disp = c['url'].replace('https://','').replace('http://','')
    rel_text = '上下级' if c['rel']=='r2' else '高管间'
    return (f'    <div class="hl">\n'
            f'      <div class="top"><span class="emoji">{c["emoji"]}</span><h3>{c["title"]}</h3>'
            f'<span class="cat">{c["cat"]}</span><span class="badge {c["rel"]}">{rel_text}</span>'
            f'<span class="badge {c["src_cls"]}">{c["src"]}</span></div>\n'
            f'      <p class="val">{c["val"]}</p>\n'
            f'      <details class="exec"><summary>怎么做</summary><div class="inner">{c["how"]}</div></details>\n'
            f'      <div class="src">🔗 <a href="{c["url"]}" target="_blank">{url_disp}</a></div>\n'
            f'      <div class="note">适用：{c["note"]}</div>\n'
            f'    </div>')

cards2 = [c for c in cards if c['rel']=='r2']
cards3 = [c for c in cards if c['rel']=='r3']
n2, n3 = len(cards2), len(cards3)
assert n2+n3 == len(cards)
print(f'cards total={len(cards)} | 2={n2} 3={n3}')

# ---------- WALL injection (sec3 BEFORE sec2) ----------
html = open(HTML, encoding='utf-8').read()
S3 = html.find('class="sec sec3"')
S2 = html.find('class="sec sec2"')
assert S3 != -1 and S2 != -1 and S3 < S2, 'section headers not found / wrong order'

def grid_close(h, sec_start):
    gi = h.find('<div class="grid">', sec_start)
    assert gi != -1, "grid not found"
    depth = 0; i = gi + len('<div class="grid">')
    while i < len(h):
        if h.startswith('<div', i):
            depth += 1; i = h.find('>', i) + 1
        elif h.startswith('</div>', i):
            if depth == 0: return i
            depth -= 1; i += 5
        else: i += 1
    raise RuntimeError("unbalanced")

def grid_hl(h, sec_start):
    gi = h.find('<div class="grid">', sec_start)
    return h[gi:grid_close(h, sec_start)].count('class="hl"')

cur3 = grid_hl(html, S3)
cur2 = grid_hl(html, S2)
print(f'grid before: 2={cur2} 3={cur3}')

close3 = grid_close(html, S3)
html = html[:close3] + ''.join(card_html(c) for c in cards3) + html[close3:]
S2 = html.find('class="sec sec2"')
close2 = grid_close(html, S2)
html = html[:close2] + ''.join(card_html(c) for c in cards2) + html[close2:]

new3 = cur3 + n3
new2 = cur2 + n2

def bump_tag(h, sec_start, new_n):
    seg = h[sec_start:sec_start+400]
    m = re.search(r'<span class="tag">\d+ 卡', seg)
    assert m, 'tag not found'
    return h[:sec_start+m.start()] + f'<span class="tag">{new_n} 卡' + h[sec_start+m.end():]

S3 = html.find('class="sec sec3"')
html = bump_tag(html, S3, new3)
S2 = html.find('class="sec sec2"')
html = bump_tag(html, S2, new2)

# hero round label: 第二十九轮 +6 -> 第三十轮 +7
assert '第二十九轮 +6' in html, 'hero label not found'
html = html.replace('第二十九轮 +6', f'{ROUND_CN} +{len(cards)}', 1)
assert '本页由 yitong 沉淀整理' in html, 'footer missing'
open(HTML, 'w', encoding='utf-8').write(html)
print(f'OK wall updated: 2={new2} 3={new3} total_hl={html.count(chr(34)+"class=hl"+chr(34))}')

# ---------- .run_newcards.tmp.html ----------
with open(TMP, 'w', encoding='utf-8') as f:
    for c in cards:
        f.write(card_html(c) + '\n')
print(f'OK tmp written ({os.path.getsize(TMP)}B)')

# ---------- gen_run_page.py ----------
gen = os.path.join(KC, "gen_run_page.py")
RUN_PATH = os.path.join(KC, "staff-meeting", "runs", f"staff-meeting-{DATE}-r{ROUND}.html")
r = subprocess.run([sys.executable, gen, "--topic", "staff-meeting", "--topic-name",
                    "员工大会", "--date", DATE, "--round", ROUND,
                    "--cards-file", TMP, "--out", RUN_PATH], capture_output=True, text=True)
print("gen_run_page:", r.returncode, (r.stdout or '').strip()[-200:], (r.stderr or '').strip()[:300])
assert r.returncode == 0, "gen_run_page failed"
assert os.path.exists(RUN_PATH), 'run page missing'
rp = open(RUN_PATH, encoding='utf-8').read()
assert '本页由 yitong 沉淀整理' in rp, 'run page footer missing'
print(f'OK run page: {RUN_PATH} ({os.path.getsize(RUN_PATH)}B, hl={rp.count(chr(34)+"class=hl"+chr(34))})')

# ---------- index.json ----------
idx_data = json.load(open(IDX, encoding='utf-8'))
before = len(idx_data)
existing_urls = {(e.get("url") or "").lower().rstrip("/") for e in idx_data}
added = 0
for c in cards:
    u = c["url"].lower().rstrip("/")
    if u in existing_urls:
        print("SKIP dup url:", u); continue
    idx_data.append({
        'title': c['title'], 'normKey': re.sub(r'[^0-9A-Za-z\u4e00-\u9fff]', '', c['title']),
        'url': c['url'],
        'sourceType': 'primary' if c['src']=='一手' else 'secondary',
        'relation': 'supervisor' if c['rel']=='r2' else 'exec',
        'summary': c['val'][:120], 'topic': 'staff-meeting',
    })
    existing_urls.add(u); added += 1
json.dump(idx_data, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'OK index.json {before} -> {len(idx_data)} (+{added})')

# ---------- Obsidian summary note ----------
sum_txt = open(OB_SUM, encoding='utf-8').read()
sec = (f'\n\n## 轮次 {DATE}（+{len(cards)}）\n\n| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n')
for c in cards:
    sec += f'| {c["title"]} | {"高管间" if c["rel"]=="r3" else "上下级"} | {c["src"]} |\n'
open(OB_SUM, 'w', encoding='utf-8').write(sum_txt.rstrip() + '\n' + sec)
print(f'OK summary note appended (轮次 {DATE} +{len(cards)})')

# ---------- Obsidian 00-index ----------
idx_txt = open(OB_IDX, encoding='utf-8').read()
pos = idx_txt.find('## 主题：')
assert pos != -1, '00-index anchor not found'
rows = ''.join(
    f'| {c["title"]}（staff-meeting.html） | 4 | {c["src"]} | {"③高管间" if c["rel"]=="r3" else "②上下级"} | {c["cat"]}：{c["val"][:30]} |\n'
    for c in cards)
idx_txt = idx_txt[:pos] + rows + '\n' + idx_txt[pos:]
open(OB_IDX, 'w', encoding='utf-8').write(idx_txt)
print(f'OK 00-index appended +{len(cards)} rows')

# ---------- Obsidian runs note ----------
os.makedirs(os.path.dirname(OB_RUN), exist_ok=True)
n_primary = sum(1 for c in cards if c['src']=='一手')
run_md = f'''---
title: 员工大会 {ROUND_CN}知识卡
tags: [知识采集, 员工大会, 自动化采集, 轮次]
date: {DATE}
type: 自动化采集
---

# 员工大会 · {ROUND_CN}补采（{DATE}）

- 本轮新增 **{len(cards)} 卡**（②上下级 {n2} · ③高管间 {n3}），0 peer（硬约束）
- 一手 {n_primary}（Microsoft 官方文档 / Pigeonhole 官方立场 / 明尼苏达州政府无障碍指南 / Great Place To Work 机构）/ 二手 {len(cards)-n_primary}
- 累计墙：staff-meeting.html（② {new2} / ③ {new3}，共 {new2+new3}）
- 新域：Teams Q&A 官方配置 / 目的性匿名治理 / 取消匿名的代价与四类替代 / 实时字幕 CART 安排规范 / 管理者级联包 / 艰难决定 5 拍+72h+14 天 / 战略翻译 4 步+仪表盘 5 问
- 硬排除：①平级/朋友向内容（用户硬约束）；安全HRBP文化知识库源（采集禁令）

## 本轮卡片

| 卡 | 质量分 | 一手/二手 | 适用关系 | 一句话定位 |
|---|---|---|---|---|
'''
for c in cards:
    one = c['note'].split('；',1)[1].rstrip('。').strip() if '；' in c['note'] else c['note']
    run_md += f'| {c["title"]} | 4 | {c["src"]} | {"③高管间" if c["rel"]=="r3" else "②上下级"} | {one} |\n'
run_md += f'''
## 链接
- 当轮独立页（GitHub Pages）：{GH_RUN}
- 当轮独立页（本地）：`{RUN_PATH}`
- 累计卡片墙：{GH}
- 主题汇总笔记：[[知识采集库/素材/staff-meeting/员工大会-知识卡汇总|员工大会-知识卡汇总]]
'''
open(OB_RUN, 'w', encoding='utf-8').write(run_md)
print(f'OK runs note: {OB_RUN} ({os.path.getsize(OB_RUN)}B)')

# ---------- GitHub 同步 ----------
sync = os.path.join(WS, "sync_knowledge_github.py")
try:
    rs = subprocess.run([sys.executable, sync], capture_output=True, text=True, timeout=600)
    print("sync_knowledge_github:", rs.returncode, (rs.stdout or '').strip()[-400:], (rs.stderr or '').strip()[:300])
except Exception as e:
    print("WARN GitHub sync exception (not blocking): " + str(e)[:200])

print("\n=== R30 core done ===")
print(json.dumps({"run_path": RUN_PATH, "wall": HTML, "n": len(cards), "r2": n2, "r3": n3,
                  "wall_2": new2, "wall_3": new3}, ensure_ascii=False))
