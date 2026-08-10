p = 'index.html'
s = open(p, encoding='utf-8').read()

old_o = '<h3>管理层 Offsite</h3><div class="cnt">40 卡</div>'
new_o = '<h3>管理层 Offsite</h3><div class="cnt">39 卡</div>'
assert old_o in s, "offsite cnt 40 not found"
s = s.replace(old_o, new_o, 1)

old_t = '<div class="n">247</div><div class="l">247 张知识卡</div>'
new_t = '<div class="n">246</div><div class="l">246 张知识卡</div>'
assert old_t in s, "total 247 not found"
s = s.replace(old_t, new_t, 1)

open(p, 'w', encoding='utf-8').write(s)
import re
print("offsite cnt:", re.search(r'<h3>管理层 Offsite</h3><div class="cnt">(\d+) 卡</div>', s).group(1))
print("total:", re.search(r'<div class="n">(\d+)</div>', s).group(1))
print("PORTAL FIXED")
