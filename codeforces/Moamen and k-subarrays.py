for i in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [a[j] for j in range(n)]
    a.sort()
    d = {}
    c = 0
    for j in range(n):
        d[a[j]] = j + 1
    for j in range(n):
        b[j] = d[b[j]]
    for j in range(n - 1):
        if b[j + 1] - b[j] != 1:
            c += 1
    c += 1
    if c > k:
        print("NO")
    else:
        print("YES")
