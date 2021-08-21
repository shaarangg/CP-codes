for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = [0, 0]
    for i in a:
        if i == 0:
            c[0] += 1
        else:
            c[1] += 1
    if c[1] <= (n // 2):
        a = [i for i in a if i == 0]
        print(len(a))
        print(*a)
    else:
        a = [i for i in a if i == 1]
        if len(a) % 2 != 0:
            a.pop()
        print(len(a))
        print(*a)
