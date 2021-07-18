d = {}


def canSum(n, d):
    if n in d:
        return d[n]
    if n == 0:
        return True
    if n < m:
        return False
    for i in p:
        if canSum(n - i, d):
            d[n - i] = True
            return True
    d[n] = False
    return False


n = int(input())
p = list(map(int, input().split()))
m = min(p)
print(canSum(n, d))
