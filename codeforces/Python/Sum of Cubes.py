from math import ceil

d = {}
i = 1
N = 10 ** 12
while i * i * i < N:
    d[i * i * i] = 1
    i += 1
for i in range(int(input())):
    x = int(input())
    r = ceil(x ** (1 / 3))
    f = 0
    for j in range(1, r):
        b = x - (j ** 3)
        if d.get(b, 0) != 0:
            f = 1
            print("YES")
            break
    if f == 0:
        print("NO")
