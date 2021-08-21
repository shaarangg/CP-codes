t = int(input())
res = []
for i in range(t):
    a, b = map(int, input().split())
    res.append(min(a, b, (a + b) // 3))
for i in res:
    print(i)
