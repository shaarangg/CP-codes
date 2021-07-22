n = int(input())
d = input()
u = list(map(int, input().split()))
f = 0
for i in range(n):
    p = 0
    if d[i] == "<":
        p = i - u[i]
    if d[i] == ">":
        p = i + u[i]
    if p < 0 or p >= n:
        print("FINITE")
        f = 1
        break
if f == 0:
    print("INFINITE")
