n = int(input())
t = list(map(int, input().split()))
if n == 2:
    print(2 * t[1] - t[0])
else:
    f = 0
    d = t[1] - t[0]
    for i in range(2, n):
        if t[i] != d + t[i - 1]:
            print(t[n - 1])
            f = 1
            break
    if f == 0:
        print(t[n - 1] + d)
