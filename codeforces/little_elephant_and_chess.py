f = 0
for i in range(8):
    l = list(input())
    if f != -1:
        for j in range(7):
            if l[j] == l[j + 1]:
                f = -1
                break
if f == -1:
    print("NO")
else:
    print("YES")
