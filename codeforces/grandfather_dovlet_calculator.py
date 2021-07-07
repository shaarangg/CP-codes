a, b = map(int, input().split())
s = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
c = 0
for i in range(a, b + 1):
    if i < 10:
        c += s[i]
    else:
        while i > 0:
            c += s[i % 10]
            i //= 10
print(c)
