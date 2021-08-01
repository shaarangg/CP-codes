n = int(input())
x = list(map(int, input().split()))
x.sort()
c = 0
a = []
for i in range(x[n - 1]):
    if i == x[c]:
        c += 1
    a.append(c)
q = int(input())
for i in range(q):
    m = int(input())
    if m >= x[n - 1]:
        print(n)
    else:
        print(a[m])
