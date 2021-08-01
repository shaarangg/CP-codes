def allConstruct(s):
    l = len(s)
    table = [None for i in range(l + 1)]
    table[0] = [[]]
    for i in range(l + 1):
        if table[i] != None:
            for j in a:
                if s[i : i + len(j)] == j:
                    if table[i + len(j)] == None:
                        table[i + len(j)] = [[*k, j] for k in table[i]]
                    else:
                        table[i + len(j)] += [[*k, j] for k in table[i]]
    print(table)
    return table[l]


s, *a = input().split()
print(allConstruct(s))
