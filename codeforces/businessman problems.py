n = int(input())
d = {}
s = 0
for i in range(n):
    a, b = map(int, input().split())
    try:
        if d[a] < b:
            s -= d[a]
            d[a] = b
            s += b
    except:
        d[a] = b
        s += b
m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    try:
        if d[a] < b:
            s -= d[a]
            d[a] = b
            s += b
    except:
        d[a] = b
        s += b
print(s)
