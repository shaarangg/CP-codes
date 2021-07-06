n = int(input())
c = list(input())
px = 0
py = 0
for i in c:
    if i == "L":
        px += 1
    elif i == "R":
        px -= 1
    elif i == "U":
        py += 1
    else:
        py -= 1
print(n - abs(px) - abs(py))
