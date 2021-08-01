def bestSum(n):
    table = [None for i in range(n + 1)]
    table[0] = []
    for i in range(n):
        if table[i] != None:
            for j in a:
                temp = [j, *table[i]]
                if i + j <= n and (table[i + j] == None or len(temp) < len(table[i])):
                    table[i + j] = temp
    return table[n]


n, *a = map(int, input().split())
print(*bestSum(n))
