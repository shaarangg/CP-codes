n, *p = map(int, input().split())
d = list(map(int, input().split()))
s = 0
for i in range(n):
    if d[i] == 2:
        if d[n - i - 1] == 2:
            if p[0] < p[1]:
                d[i] = 0
            else:
                d[i] = 1
        else:
            d[i] = d[n - i - 1]
        s += p[d[i]]
for i in range(n):
    if d[i] != d[n - i - 1]:
        print(-1)
        exit(0)
print(s)
