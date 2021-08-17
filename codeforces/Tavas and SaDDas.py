n = int(input())
a = [4, 7]
if n in a:
    print(a.index(n) + 1)
else:
    u = 1
    c = 0
    while True:
        l = len(a)
        for i in range(c, l):
            temp = 4 * (10 ** u) + a[i]
            a.append(temp)
            if temp == n:
                print(len(a))
                exit(0)
        for i in range(c, l):
            temp = 7 * (10 ** u) + a[i]
            a.append(temp)
            if temp == n:
                print(len(a))
                exit(0)
        u += 1
        c = l
