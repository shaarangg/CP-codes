def fibo(n, d):
    if n in d:
        return d[n]
    if n <= 1:
        return 1
    f = fibo(n - 1, d) + fibo(n - 2, d)
    d[n] = f
    return f


n = int(input())
if n == 1:
    print(1)
else:
    print(fibo(n, {}))
