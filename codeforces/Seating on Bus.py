n, m = map(int, input().split())
c = 1
b = []
for i in range(n):
    temp = []
    for j in range(4):
        temp.append(0)
    b.append(temp)
i = 0
jr = 3
jl = 0
while c <= m:
    if c % 2 == 0:
        b[i][jr] = c
        i += 1
    else:
        b[i][jl] = c
    c += 1
    if i == n:
        i = 0
        jr = 2
        jl = 1
i = 0
j = 1
l = []
while i < n:
    if b[i][j] != 0:
        l.append(b[i][j])
    if j == 1:
        j = 0
    elif j == 0:
        j = 2
    elif j == 2:
        j = 3
    elif j == 3:
        j = 1
        i += 1
print(*l)
