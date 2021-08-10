a = list(map(int, input().split()))
c = a.index(min(a))
m = 0
if a[0] == 1 and a[1] == 1:
    print(0)
else:
    while a[0] > 0 and a[1] > 0:
        if c == 0:
            a[0] += 1
            a[1] -= 2
        else:
            a[0] -= 2
            a[1] += 1
        c = a.index(min(a))
        m += 1
    print(m)
