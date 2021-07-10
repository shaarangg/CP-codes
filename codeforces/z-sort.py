n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    for j in range(1, n):
        if (j + 1) % 2 == 0 and a[j] < a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
        if (j + 1) % 2 != 0 and a[j] > a[j - 1]:
            a[j], a[j - 1] = a[j - 1], a[j]
print(*a)
