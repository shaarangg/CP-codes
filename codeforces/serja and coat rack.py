n, d = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())
if m <= n:
    a.sort()
    p = sum(a[:m])
else:
    p = sum(a) - d * (m - n)
print(p)
