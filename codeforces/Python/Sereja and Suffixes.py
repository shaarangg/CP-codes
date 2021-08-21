n, m = map(int, input().split())
a = list(map(int, input().split()))
d = {}
s = 0
table = [0 for i in range(n)]
for i in reversed(range(n)):
    if d.get(a[i], 0) == 0:
        d[a[i]] = 1
        s += 1
    table[i] = s
for i in range(m):
    l = int(input())
    print(table[l - 1])
