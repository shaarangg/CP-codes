f = [True] * 10
f[0] = f[1] = False
for i in range(2, 10):
    for j in range(i * i, 10, i):
        print("{} {}".format(i, j))
        f[j] = False
print(f)
