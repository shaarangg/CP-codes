import sys

sys.setrecursionlimit(10 ** 6)
# By default the recursion limit set is 10**3 which is very less and the code would not work for large numbers, so we have to manually set the recursion limit higher so that our code can work for all the cases.


def howSum(n, d):
    if n in d:
        return d[n]
    if n == 0:
        return []
    if n < m:
        return None
    for i in p:
        res = howSum(n - i, d)
        if res != None:
            res.append(i)
            d[n - i] = res
            return res
    d[n] = None
    return None


n, *p = map(int, input().split())
m = min(p)
print(howSum(n, {}))
