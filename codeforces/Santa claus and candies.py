n = int(input())
c = [0 for i in range(n + 1)]
t = n
res = []
for i in range(1, n + 1):
    if i == t - i:
        continue
    elif i > t:
        continue
    elif c[i] == 1 or c[t - i] == 1:
        continue
    else:
        t -= i
        c[i] = 1
        res.append(i)
print(len(res))
print(*res)
