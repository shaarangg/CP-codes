n = int(input())
x = list(map(int, input().split()))
m = max(x)
a = [0 for i in range(m + 1)]
for i in range(n):
    a[x[i]] += 1
for i in range(1, m + 1):
    a[i] += a[i - 1]
q = int(input())
for i in range(q):
    r = int(input())
    if r >= m:
        print(n)
    else:
        print(a[r])
