with open("input.txt") as f:
    lines = f.readlines()
n, k = map(int, lines[0].split())
a = list(map(int, lines[1].split()))
b = [i for i in a]
b.sort()
m = b[n - k]
h = []
for i in range(n):
    if len(h) == k:
        break
    if a[i] >= m:
        h.append(i + 1)
with open("output.txt", "w") as f:
    f.write("{}\n".format(m))
    for i in h:
        f.write("{} ".format(i))
