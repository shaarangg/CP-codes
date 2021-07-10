t = int(input())
res = []
for i in range(t):
    n, nt = map(int, input().split())
    tp = list(map(int, input().split()))
    w = [n for j in range(n)]
    for j in range(nt):
        for k in range(n):
            if tp[j] > k:
                a = tp[j] - k
                if w[k] > a:
                    w[k] = a
            else:
                a = k - tp[j] + 2
                if w[k] > a:
                    w[k] = a
    res.append(max(w))
for i in res:
    print(i)
