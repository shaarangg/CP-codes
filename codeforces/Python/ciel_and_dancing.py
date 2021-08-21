n, m = map(int, input().split())
print(n + m - 1)
for i in range(1, m + 1):
    print("{} {}".format(1, i))
for i in range(2, n + 1):
    print("{} {}".format(i, 1))
