from math import ceil

r, g, b = map(int, input().split())
r = ceil(r / 2)
g = ceil(g / 2)
b = ceil(b / 2)
if r == 0 and g == 0 and b == 0:
    t = 0
elif b >= g and b >= r:
    t = 30 + (b - 1) * 3 + 2
elif g >= b and g >= r:
    t = 30 + (g - 1) * 3 + 1
else:
    t = 30 + (r - 1) * 3
print(t)
