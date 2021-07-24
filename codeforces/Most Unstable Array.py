t = int(input())
res = []
for i in range(t):
    n, m = map(int, input().split())
    if n == 1:
        res.append(0)
    elif n == 2:
        res.append(m)
    else:
        res.append(m * 2)
for i in res:
    print(i)
