n = int(input())
a = list(map(int, input().split()))
m = 0
f = 0
if a[0] != 0:
    f = 1
    print(1)
else:
    for i in range(1, n):
        if a[i] > m + 1:
            f = 1
            print(i + 1)
            break
        if a[i] == m + 1:
            m += 1
    if f == 0:
        print(-1)
