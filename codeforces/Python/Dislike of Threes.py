d = {}

for t in range(int(input())):
    c = 1
    k = int(input())
    i = 1
    a = []
    if d.get(k, 0) != 0:
        print(d[k])
    else:
        while c <= k:
            if i % 3 == 0 or i % 10 == 3:
                i += 1
                continue
            d[c] = i
            c += 1
            a.append(i)
            i += 1
        print(d[k])
