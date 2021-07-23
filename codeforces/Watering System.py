n, A, B = map(int, input().split())
s = list(map(int, input().split()))
S = sum(s)
w = s[0] * A
if w / S >= B:
    print(0)
else:
    s = s[1:]
    s.sort(reverse=True)
    for i in range(n - 1):
        S -= s[i]
        if w / S >= B:
            print(i + 1)
            break
