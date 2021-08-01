def canSum(n):
    table = [False for i in range(n + 1)]
    table[0] = True
    for i in range(n + 1):
        if table[i]:
            for j in a:
                if j + i <= n:
                    table[j + i] = True
    return table[n]


n, *a = map(int, input().split())
print(canSum(n))
