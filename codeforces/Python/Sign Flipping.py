for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    for i in range(n):
        if i % 2 == 0 and a[i] > 0:
            a[i] = -a[i]
        if i % 2 != 0 and a[i] < 0:
            a[i] = -a[i]
    print(*a)