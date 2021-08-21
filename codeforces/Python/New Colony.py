for t in range(int(input())):
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    pos = 0
    if n == 1:
        pos = -1
    else:
        for i in range(k):
            j = 0
            while True:
                if h[j] < h[j + 1]:
                    h[j] += 1
                    pos = j + 1
                    break
                if j == n - 2:
                    pos = -1
                    break
                j += 1
            if pos == -1:
                break
    print(pos)
