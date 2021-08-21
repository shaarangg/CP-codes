n = int(input())
l = []
o = [False for i in range(n)]
p = 1000
index = 0
for i in range(n):
    spec = list(map(int, input().split()))
    l.append(spec)
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if l[i][0] < l[j][0] and l[i][1] < l[j][1] and l[i][2] < l[j][2]:
            o[i] = True
for i in range(n):
    if not o[i] and l[i][3] <= p:
        p = l[i][3]
        index = i + 1
print(index)
