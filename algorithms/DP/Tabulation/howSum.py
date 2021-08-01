def howSum(n):
    table = [None for i in range(n + 1)]
    table[0] = []
    for i in range(n + 1):
        if table[i] != None:
            for j in a:
                if i + j <= n:
                    table[i + j] = [j, *table[i]]
    return table[n]


n, *a = map(int, input().split())
print(*howSum(n))
