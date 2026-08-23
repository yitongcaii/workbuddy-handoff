# -*- coding: utf-8 -*-
"""Fix inner ASCII double-quotes in run_award_r23.py CARDS strings -> 「」."""
import io
p = r"c:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection\run_award_r23.py"
s = open(p, encoding="utf-8").read()

repl = [
    # card1
    ("从次要到重要", "从次要到重要"),
    ("全场景落地SOP", "全场景落地SOP"),
    ("次要→重要", "次要→重要"),
    ("流程不翻车", "流程不翻车"),
    # card2 val
    ("点题-叙事-升华", "点题-叙事-升华"),
    ("[姓名/团队]以……荣获[奖项]", "[姓名/团队]以……荣获[奖项]"),
    ("真诚感+画面感+温度感", "真诚感+画面感+温度感"),
    ("该员工/此团队", "该员工/此团队"),
    ("他/她/他们", "他/她/他们"),
    ("加班时的咖啡渍/调研时的泥泞鞋", "加班时的咖啡渍/调研时的泥泞鞋"),
    ("岗位特质+独特事迹+精神内核", "岗位特质+独特事迹+精神内核"),
    ("努力认真", "努力认真"),
    ("别人没做过/克服的特殊困难", "别人没做过/克服的特殊困难"),
    # card2 how
    ("该员工", "该员工"),
    ("她/他们", "她/他们"),
    ("成长的勋章，精神的火种", "成长的勋章，精神的火种"),
    # card3
    ("混合异步", "混合异步"),
    # card4
    ("晚宴/奥斯卡风/白金统一", "晚宴/奥斯卡风/白金统一"),
    ("评选标准透明性", "评选标准透明性"),
    # card5
    ("像自己", "像自己"),
    ("6周落地+季度审计", "6周落地+季度审计"),
    ("团队协作", "团队协作"),
    # card6
    ("月度员工", "月度员工"),
    ("被看见", "被看见"),
    # card7
    ("The Builder/Connector/Trailblazer", "The Builder/Connector/Trailblazer"),
    # card9
    ("向下表彰", "向下表彰"),
    ("peer 之间互相看见", "peer 之间互相看见"),
    ("向下发奖", "向下发奖"),
    # card10
    ("被理解", "被理解"),
    ("过程＞结果", "过程＞结果"),
]

for inner, _ in repl:
    old = '"' + inner + '"'
    new = "「" + inner + "」"
    n = s.count(old)
    s = s.replace(old, new)
    if n:
        print("replaced", n, "x:", inner)

# 即时 must be context-specific (protect cat "即时奖金")
for old, new in [
    ('胜在"即时"。', '胜在「即时」。'),
    ('保"即时"；', '保「即时」；'),
]:
    n = s.count(old)
    s = s.replace(old, new)
    if n:
        print("replaced", n, "x (context):", old)

open(p, "w", encoding="utf-8").write(s)
print("done")
