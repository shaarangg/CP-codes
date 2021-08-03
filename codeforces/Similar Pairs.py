t = int(input())
res = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    f = False
    count = [0, 0]
    for i in range(n):
        if i != 0 and a[i] - a[i - 1] == 1:
            f = True
        if a[i] % 2 == 0:
            count[0] += 1
        else:
            count[1] += 1
    if count[0] % 2 == 0 and count[1] % 2 == 0:
        res.append("YES")
    elif count[0] % 2 != 0 and count[1] % 2 != 0 and f:
        res.append("YES")
    else:
        res.append("NO")
for i in res:
    print(i)
