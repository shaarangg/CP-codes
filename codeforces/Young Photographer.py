n, x0 = map(int, input().split())
x = 0
y = 1000
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        if b > x:
            x = b
        if a < y:
            y = a
    else:
        if a > x:
            x = a
        if b < y:
            y = b
if x > y:
    print(-1)
else:
    if x0 >= x and x0 <= y:
        print(0)
    elif x0 < x:
        print(x - x0)
    else:
        print(abs(y - x0))
