t = int(input())
res = []
for i in range(t):
    a = int(input())
    a = 180 - a
    if 360 % a == 0:
        res.append("YES")
    else:
        res.append("NO")
for i in res:
    print(i)
