n = int(input())
c = input()
s = 0
for i in range(n):
    for j in range(i + 1, n):
        x = 0
        y = 0
        sub = c[i : j + 1]
        for k in sub:
            if k == "L":
                x -= 1
            elif k == "R":
                x += 1
            elif k == "U":
                y += 1
            else:
                y -= 1
        if x == 0 and y == 0:
            s += 1
print(s)
