for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    table = [0 for i in range(n)]
    m = 0
    for j in reversed(range(n)):
        table[j] = a[j]
        k = j + a[j]
        if k < n:
            table[j] += table[k]
        if table[j] > m:
            m = table[j]
    print(m)
