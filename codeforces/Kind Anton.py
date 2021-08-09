for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    f = [0, 0]
    s = 0
    for i in range(n):
        if (b[i] < a[i] and f[0] != 1) or (b[i] > a[i] and f[1] != 1):
            print("NO")
            s = 1
            break
        if a[i] == -1:
            f[0] = 1
        if a[i] == 1:
            f[1] = 1
    if s == 0:
        print("YES")
