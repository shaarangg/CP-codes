def calc():
    a = ["1"]
    i = 1
    while i <= 10 ** 18:
        i *= 2
        a.append(str(i))
    return a


a = calc()
for t in range(int(input())):
    n = input()
    m = 10 ** 9
    for i in range(60):
        temp = a[i]
        l = len(temp)
        k = 0
        res = 0
        for j in range(len(n)):
            if k < l and n[j] == temp[k]:
                k += 1
                res += 1
        moves = (len(n) - res) + (l - res)
        if moves < m:
            m = moves
    print(m)
