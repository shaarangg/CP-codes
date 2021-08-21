for t in range(int(input())):
    useless = input()
    k, n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    seq = []
    i = 0
    j = 0
    fa = 0
    fb = 0
    while True:
        if (
            (fa == 1 and fb == 1)
            or (j == len(b) and i == len(a))
            or (fa == 1 and j == len(b))
            or (fb == 1 and i == len(a))
        ):
            break
        while i < n:
            if a[i] != 0 and a[i] > k:
                fa = 1
                break
            if a[i] == 0:
                k += 1
            seq.append(a[i])
            i += 1
            fb = 0
        while j < m:
            if b[j] != 0 and b[j] > k:
                fb = 1
                break
            if b[j] == 0:
                k += 1
            seq.append(b[j])
            j += 1
            fa = 0
    if len(seq) != n + m:
        print(-1)
    else:
        print(*seq)
