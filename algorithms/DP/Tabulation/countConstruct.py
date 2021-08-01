def counContruct(s):
    l = len(s)
    table = [0 for i in range(l + 1)]
    table[0] = 1
    for i in range(l + 1):
        if table[i]:
            for j in a:
                if s[i : i + len(j)] == j:
                    table[i + len(j)] += table[i]
    return table[l]


s, *a = input().split()
print(counContruct(s))
