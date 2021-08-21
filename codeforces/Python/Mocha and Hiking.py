for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    index = -1
    s = ""
    for i in reversed(range(n)):
        if a[i] == 0:
            index = i
            break
    if index == -1:
        s = str(n + 1)
        for i in range(1, n + 1):
            s += " " + str(i)
    else:
        for i in range(1, index + 2):
            s += str(i) + " "
        s += str(n + 1)
        for i in range(index + 2, n + 1):
            s += " " + str(i)
    print(s)
