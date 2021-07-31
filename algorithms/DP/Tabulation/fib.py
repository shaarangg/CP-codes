def fib(n):
    table = [0 for i in range(n + 1)]
    table[1] = 1
    for i in range(n):
        table[i + 1] += table[i]
        if i + 2 <= n:
            table[i + 2] += table[i]
    return table


n = int(input())
table = fib(n)
print(table[n])
