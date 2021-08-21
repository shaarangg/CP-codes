n = int(input())
a = list(map(int, input().split()))
m = min(a)
for i in a:
    if i % m != 0:
        print(-1)
        exit(0)
print(m)
