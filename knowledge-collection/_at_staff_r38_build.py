# -*- coding: utf-8 -*-
"""员工大会 r38 补采 build：注入 4×③ + 4×② 共 8 张新卡到累计墙，写 tmp 卡文件，追加 index.json。"""
import json, os, re

KC = os.path.dirname(os.path.abspath(__file__))
WALL = os.path.join(KC, 'staff-meeting', 'staff-meeting.html')
TMP = os.path.join(KC, 'staff-meeting', '.run_newcards.tmp.html')
IDX = os.path.join(KC, 'index.json')
RUN_DATE = '2026-09-08'
ROUND = 'r38'

def card(emoji, title, cat, rel_badge, rel_label, src_badge, src_label, val, exec_txt, url, note):
    return f'''<div class="hl">
      <div class="top"><span class="emoji">{emoji}</span><h3>{title}</h3><span class="cat">{cat}</span><span class="badge {rel_badge}">{rel_label}</span><span class="badge {src_badge}">{src_label}</span></div>
      <p class="val">{val}</p>
      <details class="exec"><summary>怎么做</summary><div class="inner">{exec_txt}</div></details>
      <div class="src">🔗 <a href="{url}" target="_blank">{url}</a></div>
      <div class="note">适用：{note}</div>
    </div>'''

# ---------- ③ 高管间 (4) ----------
c3_1 = card('🤖', '高管 AI 数字分身出席内部会议·替代领导参与常规同步（信任治理红线）', '高管AI分身', 'r3', '高管间', 'b2', '二手',
  'Meta 据 FT 正开发 CEO 的实时 3D 写实 AI 分身，训练其声纹与举止，可在部分内部会议代表本人、传达战略优先级、回答常规问题；本质是「视频致辞升级版」到「实时无脚本对话」两档。关键治理问题：分身说的话是否等同 CEO 表态？谁定它能说什么？训练数据/应答边界谁管？Wharton 教授 Ethan Mollick：「真正考验不是像不像，是员工信不信它说的」。须明确标注 AI 生成、对话留痕、设人工升级通道。',
  '高管用 AI 分身替代出席内部常规会议（状态同步/战略重申/FAQ）是趋势而非科幻；落地红线=透明标注+对话留痕+人工升级通道，绝不让「戴 CEO 脸的 AI」在薪酬/组织变动上替领导表态；适合异地万人组织做「领导永远在场」的轻量触达，但重大宣布仍须真人。',
  'https://morningoverview.com/meta-is-building-an-ai-zuckerberg-to-handle-some-meetings',
  '③ 高管 × 全员（morningoverview 二手；Meta AI 分身出席内部会议，可作「高管AI替身」治理范本）。')

c3_2 = card('📜', '股权激励启动会·创始人讲 Why + HR 讲规则 + 坦诚 Q&A + 授予仪式（四段式）', '股权激励启动会', 'r3', '高管间', 'b1', '一手',
  '笛杨咨询实务文——一份好方案传递不到位会沦为「独角戏」。启动会四段：① 创始人/CEO 亲讲 Why（初心与梦想、事业共同体，非条款）；② HR/顾问讲 What&How（术语翻译人话：授予日/等待期/行权价/归属，用虚拟员工演算估值让「纸面富贵」可感知）；③ 坦诚 Q&A（创始人亲自答战略/估值/上市，透明建信任）；④ 正式授予仪式（CEO 亲手发《股权授予通知书》，仪式感强归属感）。目标超越「告知」达成理解→认同→共鸣三共识。',
  '办股权激励启动会学笛杨「四段式」：创始人必须亲讲 Why 把激励升到事业共同体高度、HR 用大白话+案例演算把条款讲懂、留足时间让创始人坦诚答战略、用亲手授予仪式赋予荣耀；适合成长期公司首次发期权，关键是「创始人出面对齐期待+仪式感落地认同」。',
  'https://www.diyangsh.com/archives/p70hp4e7',
  '③ 创始人/CEO × 激励对象（笛杨咨询原创一手；股权激励启动会四段式，可作期权发放全员会范本）。')

c3_3 = card('🧭', 'Purpose 渗透全员会·把组织目的讲成「过去-现在-未来」叙事 + 叠加个人目的', 'Purpose渗透', 'r3', '高管间', 'b2', '二手',
  'CrossFields 2026 活动报告——ESG/DE&I 逆风下企业更需把 purpose 渗到一线。痛点：管理层把 purpose 反复讨论后凝成「金字塔图」下发，员工只收到「文字符号」无共鸣。解法：把公司「起源(过去)/为何做此刻(现在)/想去哪(未来=purpose)」讲成单一故事（人才能共情）；更进一步组织要提供「叙事装置」让每位员工叠加自己的 My-Purpose（组织做平台而非单向宣讲）。',
  '在全员会讲 purpose 别发「金字塔图」——改成「过去-现在-未来」一则故事让员工共情，再给员工渠道讲「我为何而工作」叠加个人目的；适合价值观/使命宣贯型全员会，关键是把抽象目的变可感的个人叙事而非墙上标语。',
  'https://note.crossfields.jp/n/n06ac049c9270?hl=en',
  '③ 高管/文化负责人 × 全员（CrossFields 二手；Purpose 渗透全员会，可作「使命叙事」范本）。')

c3_4 = card('🌱', '用全员会驱动 CSR 内部倡导·高管以身作则 + 月度 Impact Chats + spotlight 认可', 'CSR内部倡导', 'r3', '高管间', 'b2', '二手',
  'CSR Connect——内部倡导不能靠自上而下指令，要给真实参与空间；领导以身作则（参与志愿、全员会公开谈可持续目标、分享个人动机「为后代减废」显人性化）；某 SaaS 公司 CEO 开月度 Impact Chats 让员工无审批提点子后，员工主导绿色倡议 +40%；认可也很关键：内部通讯/全员会 spotlight 贡献，显倡导被重视非强制；入职即嵌可持续仪表盘、配 sustainability buddy；远程用 Slack 频道+虚拟 town hall 轮值员工主持让文化分布式可达。',
  '用全员会推 CSR 倡导学 CSR Connect「领导以身作则+认可非强制」：高管在全员会亲谈可持续目标、开月度 Impact Chats 收员工点子、spotlight 表彰贡献；入职嵌可持续仪表盘+sustainability buddy；远程用专属频道+虚拟 town hall 轮值主持；适合价值观驱动型组织，关键是「Advocacy 来自 ownership 而非 compliance」。',
  'http://csrconnect.org/csr-india/building-a-csr-culture-of-internal-advocacy',
  '③ 高管 × 员工（CSR Connect 二手；全员会驱动 CSR 内部倡导，可作「目的驱动文化」范本）。')

# ---------- ② 上下级 (4) ----------
c2_1 = card('🌐', '多语全员会引导技巧·提前定语言+术语库+80%语速+转录锚点（不让任何人掉队）', '多语会议引导', 'r2', '上下级', 'b2', '二手',
  'LecSync 指南——多语会议常因「半屋人脑内翻译」丢决策。三策略：单一 lingua franca+实时转录翻译 / 双语引导 / 全多语 AI 桥接；会前 48h 发多语议程、上传术语表提升转录精度。会中引导：讲者降速到 80% 常态、关键点后停顿等翻译、把实时转录投屏当视觉锚点、鼓励任意语言贡献、显式确认理解；远端用各自设备跟转录。把「被动听译」变「主动贡献」。',
  '办多语全员会学 LecSync「会前术语库+会中降速停顿+转录锚点」：提前 48h 发多语议程、上传专业术语表、讲者控 80% 语速并关键点停顿、把实时转录投屏当共同参照、邀请任意语言提问；适合跨国/多地区团队，关键是「让非母语者从旁观变参与者」。',
  'https://www.lecsync.com/blog/how-to-run-multilingual-workshop-meeting',
  '② 行政/HR × 多语团队（LecSync 二手；多语会议引导技巧，可作跨国全员会范本）。')

c2_2 = card('🔤', '全员会实时翻译·两种模式不打断对话流（被动 participant-side / 共享 meeting-level）', '实时翻译模式', 'r2', '上下级', 'b2', '二手',
  'OLVA——多语会议摩擦=误解/遗漏行动项/非母语者心理安全下降。两模式：① 被动 participant-side（每人本地助手显自己语言转录/翻译，不打断、不塞 bot，柏林 PM 跟英文 design review 看德文转录）；② 共享 meeting-level（组织者开翻译字幕流，全员同视图，适合全员会/客户演示）。原则：尊重对话节奏（最小注意力成本）、理解优先于逐字、参与者可控、主动处理同意与隐私、提供会后翻译稿/行动项。botless 工具不进会议花名册但须告知并守法。',
  '给全员会上实时翻译学 OLVA「两模式+四原则」：常规同步用被动 participant-side 不打断，全员会/对客用共享 meeting-level 字幕；守住「节奏不被打断+理解>逐字+参与者可控+同意隐私+会后翻译稿」；适合分布式多语团队，关键是翻译做 enabler 而非 disruption。',
  'https://olva.ai/blog/real-time-translation-multilingual-meetings',
  '② IT/行政 × 全员（OLVA 二手；实时翻译两模式，可作多语全员会技术范本）。')

c2_3 = card('🔮', '全息 3D 远程在场·Google Beam 缩混合办公「包容鸿沟」（远程者如临现场）', '3D远程在场', 'r2', '上下级', 'b2', '二手',
  'UC Today——Google Beam（原 Project Starline）用 65 寸光场屏+6 摄像头+AI，让远端参与者以真人尺寸「坐」在桌边、无需头显/眼镜；2026 I/O 已扩展至 Google Meet/Zoom 群组通话，非 Beam 端普通接入即被空间化排布、空间音频定位发言者。Google 自有研究称相较网格视频：社会连接感 +50%、自感贡献能力 +21%；根因是远程者常觉「旁观者非参与者」，空间渲染从硬件层补包容缺口。',
  '解决混合全员会「远端像旁观」学 Google Beam「空间化在场」：用光场屏让异地领导/员工以真人尺寸入会、空间音频定位发言，把包容缺口从软件 workaround 提到硬件层；适合多地集团全员会，关键是「远程者不被边缘化=平等参与」，但成本/环境要求仍高、宜先小范围试点。',
  'https://uctoday.com/google-beam-adds-3d-group-meeting-support-for-zoom-and-google-meet',
  '② IT/行政 × 全员（UC Today 二手；全息 3D 远程在场，可作混合办公包容技术范本）。')

c2_4 = card('🏟️', 'ESG 主题内部大会·ESG 评估+影响度量+数据说话（Etihad 案例 +51% 目标理解）', 'ESG内部大会', 'r2', '上下级', 'b2', '二手',
  'First Event 2026 Kick Off——把全队聚到曼城 Etihad 球场，融合业务战略/可持续承诺/员工 engagement 的一天：22 位跨部门演讲者、上午 plenary 改开放透明对话、下午互动工作坊（团队协作/ESG 落地）；会前按自身可持续政策做 ESG 评估（素食本地餐/循环厨余/可再生电力/活工资供应链），用 Impact Report 工具度量得 Advanced；用环绕球场的员工姓名营造「被看见」；会后数据：目标理解 +51%、角色理解 +31%、乐意推荐 +15%、100% 签 ESG Charter。',
  '办 ESG/可持续主题全员大会学 First Event「评估+度量+数据闭环」：会前按可持续政策做 ESG 评估选场地餐饮、把可持续嵌进工作坊而非口号、用影响度量工具出前后分、用姓名环场等仪式让每人被看见；适合价值观/ESG 驱动型组织，关键是「sustainability 被度量而非只被谈」，用 +51% 这类数据证 ROI。',
  'https://www.firstevent.co.uk/our-work/esg-focused-internal-conference-first-event-kick-off',
  '② 行政/品牌 × 全员（First Event 二手；ESG 主题内部大会，可作可持续全员会范本）。')

cards_3 = [c3_1, c3_2, c3_3, c3_4]
cards_2 = [c2_1, c2_2, c2_3, c2_4]
all_cards = cards_3 + cards_2

# ---------- 注入累计墙 ----------
html = open(WALL, encoding='utf-8').read()

# sec3 grid：在 <div class="sec sec3"> 之后的第一个 <div class="grid"> 后插入
i3 = html.index('<div class="sec sec3">')
g3 = html.index('<div class="grid">', i3)
insert_3 = ''.join(cards_3)
html = html[:g3+len('<div class="grid">')] + '\n' + insert_3 + html[g3+len('<div class="grid">'):]

# sec2 grid：在 <div class="sec sec2"> 之后的第一个 <div class="grid"> 后插入
i2 = html.index('<div class="sec sec2">')
g2 = html.index('<div class="grid">', i2)
insert_2 = ''.join(cards_2)
html = html[:g2+len('<div class="grid">')] + '\n' + insert_2 + html[g2+len('<div class="grid">'):]

# 计数更新：132→136 / 259→263
html = html.replace('    <span class="tag">132 卡</span>', '    <span class="tag">136 卡</span>', 1)
html = html.replace('    <span class="tag">259 卡</span>', '    <span class="tag">263 卡</span>', 1)

# hero 追加本轮段
html = html.replace('三十七轮 enrich 2026-09-07(+8)</p>', '三十七轮 enrich 2026-09-07(+8)｜ 三十八轮 enrich 2026-09-08(+8)</p>', 1)

# 顶部增量页链接 r37→r38
html = html.replace('runs/staff-meeting-2026-09-07-r37.html', 'runs/staff-meeting-2026-09-08-r38.html', 1)

open(WALL, 'w', encoding='utf-8').write(html)
print('WALL updated. len=', len(html))

# ---------- tmp 卡文件（供 gen_run_page.py）----------
open(TMP, 'w', encoding='utf-8').write(''.join(all_cards))
print('TMP written. cards=', len(all_cards))

# ---------- index.json 追加 ----------
def normkey(t):
    t = t.lower()
    t = re.sub(r'[^\w\u4e00-\u9fff]', '', t)
    return t

idx = json.load(open(IDX, encoding='utf-8'))
before = len(idx)

entries = [
  ('高管 AI 数字分身出席内部会议·替代领导参与常规同步', 'https://morningoverview.com/meta-is-building-an-ai-zuckerberg-to-handle-some-meetings', 'secondary', 'exec', 'Meta 据 FT 开发 CEO 实时 3D 写实 AI 分身，可代表本人出席部分内部会议、答常规问题；治理红线=透明标注+对话留痕+人工升级通道，重大宣布仍须真人；Wharton 教授：考验在员工信不信。'),
  ('股权激励启动会·创始人讲 Why+HR 讲规则+坦诚 Q&A+授予仪式', 'https://www.diyangsh.com/archives/p70hp4e7', 'primary', 'exec', '笛杨咨询原创：启动会四段=创始人亲讲 Why(事业共同体)/HR 大白话+案例演算讲规则/创始人坦诚答战略 Q&A/CEO 亲手发授予通知书仪式；目标超越告知达成理解→认同→共鸣。'),
  ('Purpose 渗透全员会·组织目的叙事+叠加个人目的', 'https://note.crossfields.jp/n/n06ac049c9270?hl=en', 'secondary', 'exec', 'CrossFields 2026：ESG 逆风下更需把 purpose 渗到一线；别发金字塔图，改讲公司过去-现在-未来单一故事让员工共情，再给员工渠道叠加个人 My-Purpose；组织做平台而非单向宣讲。'),
  ('用全员会驱动 CSR 内部倡导·高管以身作则+月度 Impact Chats', 'http://csrconnect.org/csr-india/building-a-csr-culture-of-internal-advocacy', 'secondary', 'exec', 'CSR Connect：内部倡导靠 ownership 非 compliance；领导以身作则(全员会谈可持续目标/分享个人动机)、CEO 开月度 Impact Chats 收点子、spotlight 表彰；远程用 Slack 频道+虚拟 town hall 轮值主持。'),
  ('多语全员会引导技巧·提前定语言+术语库+80%语速+转录锚点', 'https://www.lecsync.com/blog/how-to-run-multilingual-workshop-meeting', 'secondary', 'supervisor', 'LecSync：三策略(lingua franca+实时转录/双语/全多语 AI)；会前 48h 发多语议程+上传术语表；会中讲者降速 80%、关键点停顿、实时转录投屏当锚点、鼓励任意语言贡献。'),
  ('全员会实时翻译·两种模式不打断对话流', 'https://olva.ai/blog/real-time-translation-multilingual-meetings', 'secondary', 'supervisor', 'OLVA：两模式=被动 participant-side(本地助手不打断不塞 bot)/共享 meeting-level(组织者开字幕流全员同视)；四原则=节奏不被打断/理解>逐字/参与者可控/同意隐私+会后翻译稿。'),
  ('全息 3D 远程在场·Google Beam 缩混合办公包容鸿沟', 'https://uctoday.com/google-beam-adds-3d-group-meeting-support-for-zoom-and-google-meet', 'secondary', 'supervisor', 'UC Today：Google Beam 用 65 寸光场屏+6 摄像头让远端以真人尺寸入会、空间音频定位发言；Google 研究称较网格视频社会连接+50%、贡献感+21%，从硬件层补远程包容缺口。'),
  ('ESG 主题内部大会·ESG 评估+影响度量+数据说话', 'https://www.firstevent.co.uk/our-work/esg-focused-internal-conference-first-event-kick-off', 'secondary', 'supervisor', 'First Event 2026：聚曼城 Etihad 球场融合战略/可持续/engagement；会前 ESG 评估、Impact Report 度量得 Advanced；会后目标理解+51%、角色理解+31%、100% 签 ESG Charter。'),
]

existing_urls = set(e.get('url','') for e in idx)
added = 0
for title, url, st, rel, summ in entries:
    if url in existing_urls:
        print('SKIP dup url:', url)
        continue
    idx.append({
        'title': title, 'normKey': normkey(title), 'url': url,
        'sourceType': st, 'relation': rel, 'summary': summ,
        'topic': '员工大会', 'slug': 'staff-meeting', 'round': ROUND, 'date': RUN_DATE,
    })
    added += 1

json.dump(idx, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f'INDEX: before={before} added={added} after={len(idx)}')
