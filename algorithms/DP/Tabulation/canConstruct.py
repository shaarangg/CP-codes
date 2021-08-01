def canConstruct(s):
    table = [False for i in range(len(s) + 1)]
    table[0] = True
    l = len(s)
    for i in range(l):
        if table[i]:
            for j in a:
                suffix = s[i:]
                if suffix.startswith(j):
                    table[i + len(j)] = True
    print(table)
    return table[l]


s, *a = input().split()
print(canConstruct(s))
