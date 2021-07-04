n = int(input())
a = list(map(int, input().split()))
if n == 1:
    print(-1)
elif n == 2 and a[0] == a[1]:
    print(-1)
else:
    m = 10 ** 3 + 1
    j = 0
    for i in range(n):
        if a[i] < m:
            j = i + 1
            m = a[i]
    print("{} {}".format(1, j))
