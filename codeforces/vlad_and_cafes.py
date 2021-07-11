n = int(input())
a = list(map(int, input().split()))
b = [0 for i in range(2 * (10 ** 5) + 1)]
m = 0
for i in reversed(range(n)):
    if b[a[i]] == 0:
        m = a[i]
        b[a[i]] = 1
print(m)
