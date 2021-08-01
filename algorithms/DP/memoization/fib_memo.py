import sys

d = {}
n = int(input())
sys.setrecursionlimit(10 ** 9)


def fib(n, d):
    if n in d:
        return d[n]
    if n <= 2:
        return 1
    d[n] = fib(n - 1, d) + fib(n - 2, d)
    return d[n]


print(fib(n, d))