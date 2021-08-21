with open("commands.txt") as f:
    c = f.readlines()
c = [i[: len(i) - 1] for i in c]
p = []
t = 0
for i in range(len(c)):
    if c[i][0] == "+":
        p.append(c[i][1:])
    elif c[i][0] == "-":
        p.remove(c[i][1:])
    else:
        n, m = c[i].split(":")
        t += len(m) * len(p)
print(t)
