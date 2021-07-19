n = int(input())
c = 0
while n > 0:
    t = n % 10
    if t == 4 or t == 7:
        c += 1
    n //= 10
f = 0
if c == 0:
    print("NO")
else:
    while c > 0:
        t = c % 10
        if t != 4 and t != 7:
            f = 1
            print("NO")
            break
        c //= 10
    if f == 0:
        print("YES")
