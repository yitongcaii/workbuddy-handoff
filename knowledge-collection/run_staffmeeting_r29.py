# -*- coding: utf-8 -*-
# 员工大会 · 第二十九轮补采（r29, 2026-08-28）+6 卡：3 ②上下级(含1一手) + 3 ③高管间
# 新域：ROI 5层度量 / 全远程异步播客(GitLab一手) / 远程最佳实践 / 裁员后全员会信任双引擎 / 致辞5段情感弧 / 高管叙事6步+三类削弱叙事
import re, os, json, subprocess, sys, urllib.request, urllib.error

WS = r"C:\Users\v_yitcai\WorkBuddy\20260728154244"
KC = os.path.join(WS, "knowledge-collection")
HTML = os.path.join(KC, "staff-meeting", "staff-meeting.html")
TMP  = os.path.join(KC, "staff-meeting", ".run_newcards.tmp.html")
IDX  = os.path.join(KC, "index.json")
OB_SUM = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\staff-meeting\员工大会-知识卡汇总.md"
OB_IDX = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\00-知识采集索引.md"
OB_RUN = r"C:\Users\v_yitcai\Documents\Obsidian\活动\知识采集库\素材\staff-meeting\runs\员工大会-2026-08-28-第二十九轮-知识卡.md"
GH = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/staff-meeting.html"
GH_RUN = "https://yitongcaii.github.io/workbuddy-handoff/knowledge-collection/staff-meeting/runs/staff-meeting-2026-08-28-r29.html"

cards = [
 dict(emoji='📊', title='全员会效果度量·5 层 ROI 框架（别只看到场率）', cat='效果度量',
      rel='r2', src='二手', src_cls='b2',
      url='https://virtuopo.com?p=9462/',
      val='Virtuopo 内部沟通事件 5 层 ROI 框架：L1 Reach(到场/on-demand/地域覆盖)→L2 Attention(平均观看时长/掉线率/提问投票参与)→L3 Understanding(清晰度评分/会后脉冲/能否复述关键消息)→L4 Emotional(情绪分析/领导可信度/"我感到被通知/有连接"分)→L5 Behaviour(倡议采纳率/后续项目参与/抗拒变化下降)。传统指标(到场率/掌声/单分满意度)只说明"谁来了"，看不出"变了什么"。ROI=相对投入产生的可衡量组织影响(理解战略↑/信任↑/行为↑/困惑↓)。',
      how='办全员会前先在 brief 写清"会后要改变什么"；会中用结构化互动、会后脉冲测 Understanding；把 ROI 建进设计而非事后补。用 Reach→Attention→Understanding→Emotional→Behaviour 五层逐步逼近真实影响，别用到场率当成功。',
      note='② HR/内部沟通/中层（Virtuopo 机构二手）；全员会效果度量——5 层 ROI 框架(到场→注意→理解→情感→行为)，到场率不算成功，看行为改变。'),
 dict(emoji='🎙️', title='全远程全员会·把沉闷周会变成异步播客（GitLab 实践·一手）', cat='异步替代',
      rel='r2', src='一手', src_cls='b1',
      url='https://about.gitlab.com/blog/how-we-turned-40-person-meeting-into-a-podcast',
      val='GitLab(全远程、100+地点)把部门全员会从"慢/同步/耗神"改成纯异步播客：一份共享文档收集要点，周三 Slackbot 提醒填、周五自动 cutoff 开讨论帖；团队抽人把"周回顾"指标+故事写成脚本、录制混音，12:00 PST 前 Slackbot 发布。结果把 40 人×1 小时"椅子时间"压成 10-15 分钟可边走边听的音频。全员会核心信息(指标/感谢/故事/公告)全保留，只是换媒介；被动收听(关摄像头/事后看)在公司手册里被鼓励而非禁止。',
      how='全远程团队的同步全员会常"长大到失去连接价值"。试把它改造成异步播客：固定周三收集+周五发布节奏，用文档+Slackbot 当"轨道"，把同步会议压成 10-15 分钟音频；保留指标/感谢/故事/公告骨架，让被动收听合法化。省下的是 40 人×1 小时的集体时间。',
      note='② HR/IT/组织者（GitLab 官方博客·一手）；全远程全员会——把沉闷同步周会改造成异步播客(文档+Slackbot 节奏)，省集体时间、保留信息骨架。'),
 dict(emoji='🌐', title='全员会目的与远程最佳实践（该讲什么/跳过什么）', cat='远程实践',
      rel='r2', src='二手', src_cls='b2',
      url='https://www.roamjobs.com/terms/all-hands',
      val='全员会定义=全员(从高管到 IC)听领导分享更新、庆祝胜利、回应提问、对齐战略优先级，月度/季度固定节奏。远程最佳实践：①务必录播+按地域时区观看+书面摘要；②互动工具(聊天实时问/投票/表情测情绪)，Zoom/Meet/Loom 按规模选；③结构化但保留真实瞬间；④Q&A 多渠道(提前匿名表/会中聊天/会后跟进)，尽可能公开答、公开追；⑤尊重注意力——演示≤30-45 分钟，用视频/客座打破"大头照"；⑥"观看派对"把被动看变社交。该覆盖：业绩指标/战略方向/团队聚焦与胜利/组织变动/产品更新/开放 Q&A；该跳过：只适用某部门的细节、会让多数观众掉线的深技术。',
      how='办远程全员会先固定节奏(月/季)，会前共享议程；务必录播+书面摘要覆盖缺席/异地；Q&A 走"提前匿名+会中+会后"三通道并公开追；演示压到 30-45 分钟以内，用视频/客座打破单调；鼓励"观看派对"把被动看变社交。该讲战略胜利、跳过部门专属细节与深技术。',
      note='② HR/组织者/中层（RoamJobs 二手）；全员会远程实践——录播+书面摘要+三通道 Q&A+演示≤45min+观看派对，该讲战略胜利、跳过部门细节。'),
 dict(emoji='⚠️', title='裁员后全员会·三种失败模式 + 信任双引擎', cat='危机沟通',
      rel='r3', src='二手', src_cls='b2',
      url='https://www.unicornlabs.ca/blog/town-hall-script-after-layoffs',
      val='裁员后全员会是信任测试，团队在决定去留。三种失败模式：①毒性乐观("更精简更聚焦"——战略正确但情绪失聪)；②模糊乐观("仍致力于使命与员工"——什么都没说，沉默被最坏解读填满)；③过度解释(财务模型/冗长辩护——听起来像在自证)。解药=带人性尊严的诚实。团队真正在问两个引擎：能力("领导有真计划还是自由落体？"——要诚实讲发生/为什么、现在什么稳定、未来 90 天具体优先)；善意("领导当我是人还是可优化资源？"——承认人的代价、坦诚无法解决的未知、兑现承诺可见跟进)。引用 Edmondson(心理安全)与 Gallup(经理解释 70% 参与度方差)。',
      how='裁员后全员会别用毒性乐观/模糊乐观/过度解释三种套路。直接回答两个信任引擎：能力(发生了什么/为什么/现在什么稳定/未来 90 天优先)与善意(承认人的代价/坦诚未知/兑现承诺)。说"我不知道接下来六个月全貌，但我知道的是…"比假装确定更可信；明确回应"你不会是下一个吗"——这一点多数领导跳过。',
      note='③ 高管/HR 负责人（Unicorn Labs 二手）；裁员后全员会——避三种失败模式(毒性/模糊/过度解释)，用能力+善意双引擎回答信任，坦诚未知。'),
 dict(emoji='🎤', title='全员会致辞·5 段情感弧（从认可现实到行动号召）', cat='致辞结构',
      rel='r3', src='二手', src_cls='b2',
      url='https://pulserevops.com/speeches/sp0191',
      val='全员会致辞是"定义数月文化的领导时刻"，有效致辞五特征：真实透明(员工能秒辨粉饰)/具体可触(点名具体团队成就而非"大家很努力")/清晰情感弧/具体可落地号召/用故事记忆。5 段情感弧(各段情绪任务+时间占比)：①Welcome(10%，先确认"我知道你们这个月熬了很多夜")；②Acknowledge Reality(20%，同时讲赢与输，"我们达标了，但客户留存没达标，我会诚实讲为什么")；③Connect to Shared Effort(30%，用具体团队/个人案例把工作连到结果，强化"我们是解决难题的团队"认同)；④Paint the Future(25%，描述 6-12 月图景并直接连到当前工作)；⑤Call to Action(15%，具体可达成请求，如"本周每团队在 standup 提一个流程改进")。混合观众要调语气。',
      how='写全员会致辞按"欢迎→认可现实(赢输都讲)→连接共同努力(具体案例)→描绘未来→行动号召"五段走，各段配情绪任务与时间盒；用一句具体客户故事(而非指标幻灯片)收尾最难忘；号召要具体可达成("本周每团队提一个改进"而非"继续加油")。别只堆内容忽略形式。',
      note='③ 高管/讲话稿撰写（Pulse RevOps 二手）；全员会致辞——5 段情感弧(欢迎→认可现实→连接努力→描绘未来→行动号召)，具体故事+可落地号召。'),
 dict(emoji='📖', title='高管叙事·6 步结构 + 三类削弱叙事（hero-only/虚假积极/甩锅）', cat='叙事框架',
      rel='r3', src='二手', src_cls='b2',
      url='https://kapable.club/glossary/what-is-executive-storytelling/',
      val='领导者用故事塑造认知，但三类叙事会削弱对齐：①hero-only(把领导当唯一英雄，贬低团队)；②不切实际的积极(听起来像剧本/虚假，引发怀疑)；③甩锅(推给外部/前任/某团队，伤信任)。6 步结构：①Context(用 SCQA 讲清为何现在讲、什么变了)；②Challenge(用差距分析说清现状→未来态→缺口)；③Insight(用 After-Action Review：预期/实际/教训→连到决策)；④Decision(用 OODA 直说决定与理由，方向清晰才给人安全感)；⑤Path Forward(连到 OKR，点名目标+2-3 关键结果)；⑥Reinforce Meaning(用 Golden Circle 回到"为什么")。可信领导展现担当、聚焦向前方案。',
      how='高管在全员会讲故事，先避开三类雷(只捧自己/虚假积极/甩锅)。按 6 步搭：背景(SCQA)→挑战(差距分析)→洞见(AAR 教训)→决定(OODA 直说)→路径(连 OKR 点名 KR)→意义(回到 Golden Circle 的为什么)。把"我们学到了什么、下一步"而非"谁的责任"作为落点，信任才立得住。',
      note='③ 高管/领导沟通（Kapable 二手）；高管叙事——避三类削弱叙事(自夸/虚假积极/甩锅)，按 6 步结构(SCQA→差距→AAR→OODA→OKR→Golden Circle)搭。'),
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
assert n2+n3 == len(cards), (n2,n3,len(cards))
print(f'cards total={len(cards)} | ②={n2} ③={n3}')

# ---------- WALL injection (current wall: sec3 BEFORE sec2) ----------
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
print(f'grid actual before: ②={cur2} ③={cur3}')

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

html = bump_tag(html, S3, new3)
html = bump_tag(html, S2, new2)

# hero round label update: 第二十八轮 +X -> 第二十九轮 +6
html = re.sub(r'第二十八轮 \+\d+', '第二十九轮 +6', html, count=1)
assert '本页由 yitong 沉淀整理' in html, 'footer missing'
open(HTML, 'w', encoding='utf-8').write(html)
print(f'OK wall updated: ②={new2} ③={new3} (hl now {html.count(chr(34)+"class=hl"+chr(34))})')

# ---------- .run_newcards.t  mp.html ----------
with open(TMP, 'w', encoding='utf-8') as f:
    for c in cards:
        f.write(card_html(c) + '\n')
print(f'OK {TMP} written ({os.path.getsize(TMP)}B)')

# ---------- gen_run_page.py -> runs/staff-meeting-2026-08-28-r29.html ----------
gen = os.path.join(KC, "gen_run_page.py")
RUN_PATH = os.path.join(KC, "staff-meeting", "runs", "staff-meeting-2026-08-28-r29.html")
r = subprocess.run([sys.executable, gen, "--topic", "staff-meeting", "--topic-name",
                    "员工大会", "--date", "2026-08-28", "--round", "29",
                    "--cards-file", TMP, "--out", RUN_PATH], capture_output=True, text=True)
print("gen_run_page:", r.returncode, r.stdout.strip(), (r.stderr.strip()[:200] if r.stderr else ""))
assert r.returncode == 0, "gen_run_page failed"

# ---------- index.json (URL dedup) ----------
idx_data = json.load(open(IDX, encoding='utf-8'))
before = len(idx_data)
existing_urls = {e.get("url","").lower().rstrip("/") for e in idx_data}
added = 0
for c in cards:
    u = c["url"].lower().rstrip("/")
    if u in existing_urls:
        print("SKIP dup url:", u); continue
    idx_data.append({
        'title': c['title'], 'normKey': c['title'], 'url': c['url'],
        'sourceType': 'primary' if c['src']=='一手' else 'secondary',
        'relation': 'supervisor' if c['rel']=='r2' else 'exec',
        'summary': c['val'][:120], 'topic': 'staff-meeting',
    })
    existing_urls.add(u); added += 1
json.dump(idx_data, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f'OK index.json {before} -> {len(idx_data)} (+{added})')

# ---------- Obsidian summary note (append 轮次 section) ----------
sum_txt = open(OB_SUM, encoding='utf-8').read()
round_section = (f'\n\n## 轮次 2026-08-28（+{len(cards)}）\n\n'
                 f'| 卡 | 适用关系 | 一手/二手 |\n|---|---|---|\n')
for c in cards:
    rel = '高管间' if c['rel']=='r3' else '上下级'
    round_section += f'| {c["title"]} | {rel} | {c["src"]} |\n'
sum_txt = sum_txt.rstrip() + '\n' + round_section
open(OB_SUM, 'w', encoding='utf-8').write(sum_txt)
print(f'OK summary note appended (轮次 2026-08-28 +{len(cards)})')

# ---------- Obsidian 00-index (append 6 rows to master table before first "## 主题：") ----------
idx_txt = open(OB_IDX, encoding='utf-8').read()
pos = idx_txt.find('## 主题：')
assert pos != -1, '00-index "## 主题：" not found'
rows = ''.join(
    f'| {c["title"]}（staff-meeting.html） | 4 | {c["src"]} | {"③高管间" if c["rel"]=="r3" else "②上下级"} | {c["cat"]}：{c["val"][:30]} |\n'
    for c in cards)
idx_txt = idx_txt[:pos] + rows + '\n' + idx_txt[pos:]
open(OB_IDX, 'w', encoding='utf-8').write(idx_txt)
print(f'OK 00-index appended +{len(cards)} rows (before first "## 主题：")')

# ---------- Obsidian runs note ----------
os.makedirs(os.path.dirname(OB_RUN), exist_ok=True)
run_md = f'''---
title: 员工大会 第二十九轮知识卡
tags: [知识采集, 员工大会, 自动化采集, 轮次]
date: 2026-08-28
type: 自动化采集
---

# 员工大会 · 第二十九轮补采（2026-08-28）

- 本轮新增 **{len(cards)} 卡**（②上下级 {n2} · ③高管间 {n3}），0 peer（硬约束）
- 一手 1（GitLab 异步播客）/ 二手 {len(cards)-1}（本轮以国际机构/公司博客二手为主，公司内部官方一手源稀缺）
- 累计墙：staff-meeting.html（主集 ② {cur2+n2} / ③ {cur3+n3}）+ 当轮独立页
- 新域：ROI 5层度量 / 全远程异步播客(GitLab一手) / 远程最佳实践 / 裁员后全员会信任双引擎 / 致辞5段情感弧 / 高管叙事6步+三类削弱叙事
- 硬排除：平级/朋友向（①）内容（用户硬约束）；安全HRBP文化知识库源（采集禁令）

## 本轮卡片

| 卡 | 质量分 | 一手/二手 | 适用关系 | 一句话定位 |
|---|---|---|---|---|
'''
for c in cards:
    one = c['note'].split('：',1)[1].rstrip('）。').strip() if '：' in c['note'] else c['note']
    run_md += f'| {c["title"]}（[staff-meeting.html]({GH})） | 4 | {c["src"]} | {"③高管间" if c["rel"]=="r3" else "②上下级"} | {one} |\n'
run_md += f'''
## 链接
- 累计卡片墙：{GH}
- 当轮独立页：{GH_RUN}
- 主题汇总笔记：[[知识采集库/素材/staff-meeting/员工大会-知识卡汇总|员工大会-知识卡汇总]]
'''
open(OB_RUN, 'w', encoding='utf-8').write(run_md)
print(f'OK runs note: {OB_RUN} ({os.path.getsize(OB_RUN)}B)')

print('DONE pipeline core.')

# ---------- GitHub Pages 同步 ----------
sync = os.path.join(WS, "sync_knowledge_github.py")
try:
    rs = subprocess.run([sys.executable, sync], capture_output=True, text=True, timeout=300)
    print("sync_knowledge_github:", rs.returncode, (rs.stdout.strip()[-300:] if rs.stdout else ""), (rs.stderr.strip()[:200] if rs.stderr else ""))
except Exception as e:
    print("⚠️ GitHub 同步异常（告警不阻断）：" + str(e)[:200])

# ---------- 乐享上传（whoami 探活，不依赖连接器状态面板）----------
MCP_JSON = os.path.expanduser("~/.workbuddy/mcp.json")
LEXIANG_URL = "https://mcp.lexiang-app.com/mcp?company_from=csig"
FOLDER = "a753a4ebc526495c9e9b2e2fb3cac314"   # 员工大会子文件夹（待清洗素材下）
WALL_FILE_ID = "a1415122f8034d8d988fb06e41be44ac"
WALL_ENTRY_ID = "f3b5ea59395e49ca859f8726142742c2"
RUN_NAME = os.path.basename(RUN_PATH)  # staff-meeting-2026-08-28-r29.html

class LexiangMCP:
    def __init__(self, token):
        self.token = token; self.session = None
    def _post(self, payload, retries=3):
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(LEXIANG_URL, data=data, method="POST")
        req.add_header("Content-Type", "application/json")
        req.add_header("Accept", "application/json, text/event-stream")
        req.add_header("Authorization", self.token)
        if self.session: req.add_header("Mcp-Session-Id", self.session)
        last = None
        for _ in range(retries):
            try:
                resp = urllib.request.urlopen(req, timeout=120)
                sid = resp.headers.get("mcp-session-id")
                if sid: self.session = sid
                return self._parse(resp.read().decode("utf-8", "replace"))
            except urllib.error.HTTPError as e:
                last = "HTTP {0}: {1}".format(e.code, e.read().decode("utf-8", "replace")[:400]); continue
            except Exception as e:
                last = str(e); continue
        raise RuntimeError("POST fail: " + last)
    def _parse(self, raw):
        raw = raw.strip()
        if raw.startswith("data:"):
            raw = "\n".join(l[5:].strip() for l in raw.splitlines() if l.startswith("data:"))
        try: return json.loads(raw)
        except Exception: return json.loads(raw[raw.find("{"):])
    def initialize(self):
        return self._post({"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"wb-uploader","version":"1.0"}}})
    def initialized(self):
        try: self._post({"jsonrpc":"2.0","method":"notifications/initialized"})
        except Exception: pass
    def call(self, name, args):
        return self._post({"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":name,"arguments":args}})
    def biz(self, resp):
        res = resp.get("result")
        if not res: raise RuntimeError("no result: " + json.dumps(resp, ensure_ascii=False)[:300])
        text = ""
        for c in (res.get("content") or []):
            if c.get("type") == "text": text = c.get("text", ""); break
        try: return json.loads(text)
        except Exception: return {"_raw_text": text}

def put_bytes(url, data, retries=3):
    last = None
    for _ in range(retries):
        try:
            req = urllib.request.Request(url, data=data, method="PUT")
            req.add_header("Content-Type", "text/html")
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.status
        except Exception as e:
            last = str(e); continue
    raise RuntimeError("PUT fail: " + str(last))

try:
    token = json.load(open(MCP_JSON, encoding="utf-8"))["mcpServers"]["lexiang"]["headers"]["Authorization"]
    mc = LexiangMCP(token); mc.initialize(); mc.initialized()
    try:
        w = mc.call("whoami", {})
        print("whoami:", json.dumps(mc.biz(w), ensure_ascii=False)[:120])
    except Exception as e:
        print("whoami 跳过:", str(e)[:120])

    # (a) 更新累计墙文件本体
    wall_bytes = open(HTML, "rb").read()
    r = mc.call("file_apply_upload", {"file_id": WALL_FILE_ID, "parent_entry_id": WALL_ENTRY_ID,
                                      "name": "staff-meeting.html", "extension":"html",
                                      "mime_type":"text/html", "upload_type":"PRE_SIGNED_URL",
                                      "size": str(len(wall_bytes))})
    biz = mc.biz(r)
    if biz.get("code") != 0:
        raise RuntimeError("apply_upload(wall) FAIL {0}".format(biz.get("message")))
    sess = biz["data"]["session"]
    sid = sess.get("session_id") or sess.get("id")
    url = sess.get("upload_url") or sess["objects"][0]["upload_url"]
    st = put_bytes(url, wall_bytes)
    if st != 200: raise RuntimeError("PUT(wall) status " + str(st))
    r2 = mc.call("file_commit_upload", {"session_id": sid})
    biz2 = mc.biz(r2)
    if biz2.get("code") != 0: raise RuntimeError("commit(wall) FAIL " + str(biz2.get("message")))
    print("乐享累计墙已更新 OK")

    # (b) 新建本轮独立页条目
    run_bytes = open(RUN_PATH, "rb").read()
    r = mc.call("file_apply_upload", {"parent_entry_id": FOLDER, "name": RUN_NAME,
                                      "extension":"html", "mime_type":"text/html",
                                      "upload_type":"PRE_SIGNED_URL", "size": str(len(run_bytes))})
    biz = mc.biz(r)
    if biz.get("code") != 0:
        raise RuntimeError("apply_upload(run) FAIL {0}".format(biz.get("message")))
    sess = biz["data"]["session"]
    sid = sess.get("session_id") or sess.get("id")
    url = sess.get("upload_url") or sess["objects"][0]["upload_url"]
    st = put_bytes(url, run_bytes)
    if st != 200: raise RuntimeError("PUT(run) status " + str(st))
    r2 = mc.call("file_commit_upload", {"session_id": sid})
    biz2 = mc.biz(r2)
    if biz2.get("code") != 0: raise RuntimeError("commit(run) FAIL " + str(biz2.get("message")))
    rid = biz2["data"]["entry"]["id"]
    print("乐享新建独立页 OK entry_id=", rid)

    # 回写 lexiang-entry-map.json
    mapf = json.load(open(os.path.join(KC, "lexiang-entry-map.json"), encoding="utf-8"))
    sm = mapf.setdefault("staff-meeting", {"folder_id": FOLDER, "rounds": []})
    sm["folder_id"] = FOLDER
    if "wall" not in sm:
        sm["wall"] = {"entry_id": WALL_ENTRY_ID, "file_id": WALL_FILE_ID, "name": "staff-meeting.html"}
    sm["rounds"].append({"date": "2026-08-28", "entry_id": rid, "name": RUN_NAME,
                         "note": "轮次页 R29 (+6：ROI 5层度量/全远程异步播客GitLab一手/远程最佳实践/裁员后全员会信任双引擎/致辞5段情感弧/高管叙事6步+三类削弱叙事·3②3③)"})
    json.dump(mapf, open(os.path.join(KC, "lexiang-entry-map.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("已回写 lexiang-entry-map.json")
except Exception as e:
    print("⚠️ 乐享上传跳过（warning，不中断）：" + str(e)[:300])

# ---------- 推进 last-topic.txt ----------
with open(os.path.join(KC, "last-topic.txt"), "r", encoding="utf-8") as f:
    cur_topic = f.read().strip()
NEXT_TOPIC = "Offsite"
if cur_topic == "员工大会":
    with open(os.path.join(KC, "last-topic.txt"), "w", encoding="utf-8") as f:
        f.write(NEXT_TOPIC + "\n")
    print("last-topic.txt 推进：%s -> %s" % (cur_topic, NEXT_TOPIC))
else:
    print("⚠️ last-topic.txt 当前为「%s」非预期「员工大会」，未自动推进（请人工确认）" % cur_topic)

print("\n=== R29 完成 ===")
