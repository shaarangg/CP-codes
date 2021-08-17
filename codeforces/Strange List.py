for t in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    s = 0
    i = 0
    while True:
        if i == len(a):
            break
        if a[i] % x == 0:
            k = a[i] // x
            for j in range(x):
                a.append(k)
        else:
            break
        i += 1
    print(sum(a))
