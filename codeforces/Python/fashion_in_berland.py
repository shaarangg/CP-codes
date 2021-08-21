n = int(input())
a = list(map(int, input().split()))
if n == 1:
    if a[0] == 0:
        print("NO")
    else:
        print("YES")
else:
    c = 0
    for i in a:
        if i == 0:
            c += 1
    if c != 1:
        print("NO")
    else:
        print("YES")
