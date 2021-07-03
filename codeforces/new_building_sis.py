n, h, a, b, k = map(int, input().split())
res = []
for i in range(k):
    m = 0
    ta, fa, tb, fb = map(int, input().split())
    m = abs(ta - tb)
    if m == 0:
        print(abs(fa - fb))
    else:
        if fa > b:
            m += fa - b + abs(b - fb)
        elif fa < a:
            m += a - fa + abs(fb - a)
        else:
            m += abs(fa - fb)
        print(m)
