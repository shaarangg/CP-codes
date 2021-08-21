t = int(input())
res = []
for i in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    s = 0
    m = 0
    for i in range(n):
        s += a[i]
        if s / (i + 1) >= x:
            m = i + 1
    print(m)
