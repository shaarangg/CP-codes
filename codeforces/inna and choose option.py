t = int(input())
res = []
for i in range(t):
    s = input()
    c = 0
    p = []
    for j in range(12):
        if s[j] == "X":
            p.append("1x12")
            c += 1
            break
    for j in range(6):
        if s[j] == "X" and s[j + 6] == "X":
            p.append("2x6")
            c += 1
            break
    for j in range(4):
        if s[j] == "X" and s[j + 4] == "X" and s[j + 8] == "X":
            p.append("3x4")
            c += 1
            break
    for j in range(3):
        if s[j] == "X" and s[j + 3] == "X" and s[j + 6] == "X" and s[j + 9] == "X":
            p.append("4x3")
            c += 1
            break
    for j in range(2):
        if (
            s[j] == "X"
            and s[j + 2] == "X"
            and s[j + 4] == "X"
            and s[j + 6] == "X"
            and s[j + 8] == "X"
            and s[j + 10] == "X"
        ):
            p.append("6x2")
            c += 1
            break
    if s.count("X") == 12:
        p.append("12x1")
        c += 1
    if c == 0:
        res.append(c)
    else:
        res.append("{} {}".format(c, " ".join(p)))
for i in res:
    print(i)
