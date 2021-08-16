for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(1, n):
        d[i] = [i + 1]
    for i in range(n):
        if a[i] == 0:
            temp = d.get(i + 1, 0)
            if temp == 0:
                d[i + 1] = [n + 1]
            else:
                temp.append(n + 1)
                d[i + 1] = temp
        else:
            temp = d.get(n + 1, 0)
            if temp == 0:
                d[n + 1] = [i + 1]
            else:
                temp.append(i + 1)
                d[n + 1] = temp
