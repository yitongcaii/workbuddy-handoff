# -*- coding: utf-8 -*-
"""R9：向 index.json 追加 7 张破冰新卡（③2 / ②5，全二手）。"""
import json, re, os

BASE = os.path.dirname(os.path.abspath(__file__))
IDX = os.path.join(BASE, 'index.json')

def normkey(t):
    t = t.lower()
    # 保留 CJK + 字母 + 数字，其余(空格/标点/·/+/-)全部去除
    return re.sub(r'[^一-鿿0-9a-z]', '', t)

new = [
 ('Leadership Retreat 信任引擎·8 个不靠游戏的实践',
  'https://matthiasorgler.com/2025/11/21/build-trust-to-ignite-motivation',
  'exec',
  '硅谷敏捷教练三日领导力 retreat 实战 8 个建信任实践(非游戏、不强制暴露)：Personal Histories/Lifeline/Yes-and/示弱/give-back 共创项目；信任在真实对话与日常小习惯中生长，不在理论里。'),
 ('空降高管融合工作坊·2天1夜标准化模板(20+企业验证)',
  'https://www.toutiao.com/article/7532678475656757800/',
  'exec',
  '标准化 2天1夜模板(文化基因解码+战略对齐沙盘+领导力实战推演+百日攻坚计划)，空降高管存活率 35%→82%、决策效率+40%；创始人必到场、70% 时间实战、后续接文化翻译官+决策透明度+痛点擂台。'),
 ('工程经理 First 90 Days Playbook·倾听之旅+提问框架',
  'https://www.thegarnetwiki.com/engineering-leadership/first-90-days-playbook',
  'supervisor',
  '新工程经理首 90 天战术手册(D1-30 倾听/D31-60 诊断/D61-90 行动)：Week1 倾听之旅+结构化 1:1 提问框架(诊断/职业两类)；首月画团队地图(人/流程/产品/政治)，先摸透再优化。'),
 ('带团队前 90 天路线图·清晰/联结/一致/自信四基',
  'https://successthroughpeople.com.au/the-first-90-days-of-leading-a-team-a-practical-guide',
  'supervisor',
  '基于 Success Through People 模型的 90 天四基路线图(清晰/联结/一致/自信)：首月 1:1 四问+学团队潜规则+定 3-5 条核心期望，把信任与清晰打底而非疲于「多做事」。'),
 ('10 个建信任练习·从 Be the teacher 到赏识圈',
  'https://www.indeed.com/hire/c/info/trust-exercises',
  'supervisor',
  'Indeed 给经理的 10 个专业建信任练习(Be the teacher/Opening question/Active listening/Appreciation circles 等)，弃信任摔类幼稚游戏；信任靠透明沟通与持续小动作。'),
 ('Team Charter 分步共创·绿卡/红卡行为清单',
  'http://growth-space.co.uk/blog//how-to-create-a-team-charter-a-step-by-step-guide',
  'supervisor',
  '团队契约(Team Charter/Working Agreement)分步共创+绿卡/红卡行为清单，显式化「鼓励什么/绝不容忍什么」，化解 Storming 加速 Norming；外部引导师平衡声音。'),
 ('6 个建信任练习·角色互换+感恩链',
  'https://possiedigroup.com/6-trust-building-exercises-every-leader-should-try-leadership-development-guide.html',
  'supervisor',
  '领导力发展指南给经理的 6 个建信任练习(角色互换+感恩链+Shared Vulnerability 等)，日常化(每月≥1次)而非一次性活动，authenticity 不能装。'),
]

d = json.load(open(IDX, encoding='utf-8'))
existing_urls = {e.get('url','').rstrip('/').lower() for e in d if isinstance(e,dict)}
existing_keys = {e.get('normKey','') for e in d if isinstance(e,dict)}

added = 0
for title, url, rel, summary in new:
    nk = normkey(title)
    if url.rstrip('/').lower() in existing_urls or nk in existing_keys:
        print('SKIP (exists):', title)
        continue
    d.append({
        'title': title,
        'normKey': nk,
        'url': url,
        'sourceType': 'secondary',
        'relation': rel,
        'topic': 'icebreaker',
        'summary': summary,
    })
    added += 1

json.dump(d, open(IDX, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('added:', added, '| total entries:', len(d))
