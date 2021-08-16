for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(a[0])
    else:
        mx = 0
        index = 0
        m = 10 ** 9
        for i in range(n):
            if a[i] > mx:
                mx = a[i]
                index = i
        for i in range(n):
            if i == index:
                continue
            temp = a[i] & mx
            if temp < m:
                m = temp
        print(m)
