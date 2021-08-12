n = int(input())
h = list(map(int, input().split()))
h.insert(0, 0)
e = 0
c = 0
for i in range(n):
    t = h[i] - h[i + 1]
    if t + e < 0:
        c += abs(t + e)
        e = 0
    else:
        e += t
print(c)
