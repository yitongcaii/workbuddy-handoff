# -*- coding: utf-8 -*-
"""Second pass: fix remaining inner ASCII double-quotes in run_award_r23.py."""
p = r"c:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection\run_award_r23.py"
s = open(p, encoding="utf-8").read()

repl = [
    # card4 val
    ("请一言", "请一言"),
    ("开封演出/MC吊胃口/全员聚焦瞬间", "开封演出/MC吊胃口/全员聚焦瞬间"),
    ("选择制礼物/体验型礼品", "选择制礼物/体验型礼品"),
    ("为什么是他", "为什么是他"),
    ("姓名+理由+本人评论", "姓名+理由+本人评论"),
    ("获奖者一覧/访谈", "获奖者一覧/访谈"),
    # card4 how
    ("谁因什么被评", "谁因什么被评"),
    # card5 val
    ("什么该奖/怎么写认可话术", "什么该奖/怎么写认可话术"),
    # card6 val
    ("黑箱", "黑箱"),
    ("被认可的行为", "被认可的行为"),
    # card6 how
    ("价值绑定+peer提名", "价值绑定+peer提名"),
    ("桥梁建设者", "桥梁建设者"),
    ("具体可观察行为", "具体可观察行为"),
    # card7 how
    ("品牌延伸", "品牌延伸"),
    ("哪些行为体现哪条价值", "哪些行为体现哪条价值"),
    # card8 how
    ("制作即记忆点", "制作即记忆点"),
    ("酒会+奖块+用餐+娱乐+祝酒", "酒会+奖块+用餐+娱乐+祝酒"),
    # card9 val/how
    ("高管 peer 提名奖", "高管 peer 提名奖"),
    ("peer-adjudicated", "peer-adjudicated"),
    # card10 val
    ("哪些决策/在场/情商改变了项目轨迹", "哪些决策/在场/情商改变了项目轨迹"),
]

for inner, _ in repl:
    old = '"' + inner + '"'
    new = "「" + inner + "」"
    n = s.count(old)
    s = s.replace(old, new)
    if n:
        print("replaced", n, "x:", inner)

# 即时 second context (protect cat "即时奖金")
for old, new in [('注意"即时"——', '注意「即时」——')]:
    n = s.count(old)
    s = s.replace(old, new)
    if n:
        print("replaced", n, "x (context):", old)

open(p, "w", encoding="utf-8").write(s)
print("done")
