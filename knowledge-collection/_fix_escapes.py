# -*- coding: utf-8 -*-
import re
p = r"C:\Users\v_yitcai\WorkBuddy\20260728154244\knowledge-collection\_auto_award_r18.py"
s = open(p, encoding="utf-8").read()
bad = re.findall(r'\\u\{[0-9A-Fa-f]{4,6}\}', s)
print("非法转义出现次数:", len(bad), "去重:", sorted(set(bad)))

def fix(m):
    hexdigits = m.group(1)
    # raw string: backslash + U + 8 hex digits -> Python legal \U0001XXXX
    return r'\U' + hexdigits.rjust(8, "0")

s2 = re.sub(r'\\u\{([0-9A-Fa-f]{ 4,6})\}', fix, s) if False else re.sub(r'\\u\{([0-9A-Fa-f]{4,6})\}', fix, s)
remaining = re.findall(r'\\u\{[0-9A-Fa-f]{4,6}\}', s2)
print("修复后残留:", len(remaining))
open(p, "w", encoding="utf-8").write(s2)
print("已写回:", p)
