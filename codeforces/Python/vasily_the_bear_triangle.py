x, y = map(int, input().split())
if x > 0 and y > 0:
    a = x + y
    print("{} {} {} {}".format(0, a, a, 0))
elif x < 0 and y > 0:
    a = y - x
    print("{} {} {} {}".format(-a, 0, 0, a))
elif x > 0 and y < 0:
    a = x - y
    print("{} {} {} {}".format(0, -a, a, 0))
else:
    a = -x - y
    print("{} {} {} {}".format(-a, 0, 0, -a))
