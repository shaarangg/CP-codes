n, s = map(int, input().split())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))
for i in range(n - 1):
    for j in range(n - 1 - i):
        if p[j + 1][0] > p[j][0]:
            p[j], p[j + 1] = p[j + 1], p[j]
t = 0
for i in range(n):
    t += s - p[i][0]
    if t < p[i][1]:
        t += p[i][1] - t
    s = p[i][0]
t += s
print(t)
