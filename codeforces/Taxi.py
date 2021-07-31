from math import ceil

n = int(input())
d = {1: 0, 2: 0, 3: 0, 4: 0}
a = map(int, input().split())
for i in a:
    d[i] += 1
t = d[4]
d[4] = 0
t += d[3]
if d[1] >= d[3]:
    d[1] -= d[3]
    d[3] = 0
else:
    d[1] = 0
t += d[2] // 2
d[2] %= 2
if d[2] != 0:
    t += 1
    d[2] = 0
    d[1] -= 2
if d[1] > 0:
    t += ceil(d[1] / 4)
    d[1] = 0
print(t)
