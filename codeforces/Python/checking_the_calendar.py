d = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d1 = input()
d2 = input()
i = d.index(d1)
c = 0
while True:
    if d[i] == d2:
        break
    i = (i + 1) % 7
    c += 1
if c == 0 or c == 2 or c == 3:
    print("YES")
else:
    print("NO")
