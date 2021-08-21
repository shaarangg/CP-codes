for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    for i in range(n - 1):
        if a[i] == 1:
            c += 1
        else:
            break
    if c % 2 == 0:
        print("First")
    else:
        print("Second")
