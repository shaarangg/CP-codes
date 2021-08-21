n = int(input())
a = list(map(int, input().split()))
d = {}
keymax = 0
valuemax = 0
for i in a:
    v = d.get(i, None)
    if v != None:
        d[i] = d[i] + 1
    else:
        d[i] = 1
    if d[i] > valuemax:
        valuemax = d[i]
        keymax = i
print(keymax)
