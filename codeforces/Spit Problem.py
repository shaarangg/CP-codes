n = int(input())
d = {}
for i in range(n):
    n, k = map(int, input().split())
    d.update({n: k})
f = 0
for i in d.keys():
    s = i + d[i]
    v = d.get(s, None)
    if v == None:
        continue
    s = s + v
    if s == i:
        print("YES")
        f = 1
        break
if f == 0:
    print("NO")
