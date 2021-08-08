n = int(input())
bills = list(map(int, input().split()))
change = [0, 0]
f = 0
for i in bills:
    if i == 100:
        if change[1] >= 1 and change[0] >= 1:
            change[0] -= 1
            change[1] -= 1
        elif change[0] >= 3:
            change[0] -= 3
        else:
            print("NO")
            f = 1
            break
    if i == 50:
        if change[0] >= 1:
            change[0] -= 1
            change[1] += 1
        else:
            print("NO")
            f = 1
            break
    if i == 25:
        change[0] += 1
if f == 0:
    print("YES")
