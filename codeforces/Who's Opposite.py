for t in range(int(input())):
    a, b, c = map(int, input().split())
    diff = abs(a - b)
    m = diff * 2
    if c > (diff * 2) or a > m or b > m:
        print(-1)
    else:
        if (c + diff) <= m:
            print(c + diff)
        else:
            print(c - diff)
