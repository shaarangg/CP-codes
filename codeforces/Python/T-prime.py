import math

max = 10 ** 6
f = [True] * max
f[0] = f[1] = False
for j in range(2, max):
    if f[j] == True:
        for k in range(j * j, max, j):
            f[k] = False


n = int(input())
x = map(int, input().split())
for i in x:
    if i == 1:
        print("NO")
    elif i == 4:
        print("YES")
    elif i % 2 == 0:
        print("NO")
    else:
        a = math.sqrt(i)
        if a == int(a):
            a = int(a)
            if f[a]:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
