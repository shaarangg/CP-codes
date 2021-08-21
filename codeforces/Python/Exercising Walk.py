for t in range(int(input())):
    a, b, c, d = map(int, input().split())
    x, y, x1, y1, x2, y2 = map(int, input().split())
    xaxis = b - a
    yaxis = d - c
    x = x + xaxis
    y = y + yaxis
    if x == x1 == x2 and (a > 0 or b > 0):
        print("NO")
    elif (c > 0 or d > 0) and y == y1 == y2:
        print("NO")
    elif x >= x1 and x <= x2 and y >= y1 and y <= y2:
        print("YES")
    else:
        print("NO")
