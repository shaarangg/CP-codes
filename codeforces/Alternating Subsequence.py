for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] < 0:
        c = 1
    else:
        c = 0
    m = a[0]
    s = 0
    for i in a:
        if i < 0 and c == 1 and i > m:
            m = i
        elif i > 0 and c == 1:
            s += m
            c = 0
            m = i
        elif i < 0 and c == 0:
            s += m
            c = 1
            m = i
        elif i > 0 and c == 0 and i > m:
            m = i
    s += m
    print(s)
