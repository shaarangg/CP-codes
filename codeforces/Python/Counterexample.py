l, r = map(int, input().split())
if (r - l) < 2 or (r - l == 2 and r % 2 != 0):
    print(-1)
else:
    for i in range(l, r + 1):
        if i % 2 == 0:
            print("{} {} {}".format(i, i + 1, i + 2))
            break
