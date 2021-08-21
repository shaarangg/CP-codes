n = int(input())
a = list(map(int, input().split()))
d = {}
for i in a:
    s = d.get(i, 0)
    if s == 0:
        d[i] = 1
    else:
        d[i] = d[i] + 1
c = 0
for i in d.keys():
    c += d[i] // 2
print(c // 2)
