n = int(input())
d = input()
u = list(map(int, input().split()))
f = [0 for i in range(n)]
i = 0
while True:
    f[i] = 1
    if d[i] == "<":
        i = i - u[i]
    elif d[i] == ">":
        i = i + u[i]
    if i < 0 or i >= n:
        print("FINITE")
        break
    if f[i] == 1:
        print("INFINITE")
        break
