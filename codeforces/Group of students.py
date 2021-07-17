m = int(input())
c = list(map(int, input().split()))
x, y = map(int, input().split())
f = 0
for i in range(1, m):
    g1 = sum(c[:i])
    g2 = sum(c[i:])
    if g1 <= y and g1 >= x and g2 <= y and g2 >= x:
        f = 1
        print(i + 1)
        break
if f == 0:
    print(0)
