n = int(input())
a = list(map(int, input().split()))
n = 0
c = 0
f = []
for i in a:
    if i < 0:
        n += 1
    if n == 3:
        f.append(c)
        c = 0
        n = 1
    c += 1
if n != 0:
    f.append(c)
print(len(f))
print(*f)
