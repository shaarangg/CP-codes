for t in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    lc = 0
    c = 0
    ls = 0
    for i in range(n):
        if s[i] == "*" and c == 0:
            c += 1
            lc = i
        elif s[i] == "*" and c != 0:
            if i - lc <= k:
                ls = i
            else:
                lc = ls
                ls = i
                c += 1
    if ls != 0:
        c += 1
    print(c)
