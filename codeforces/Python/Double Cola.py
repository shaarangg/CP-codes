from math import log2, floor

n = int(input())
name = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
t = floor(log2((n / 5) + 1))
if t == 0:
    print(name[n - 1])
else:
    n1 = 5 * ((2 ** t) - 1)
    n -= n1
    if n == 0:
        print("Howard")
    else:
        i = 0
        while n > 0:
            n -= 2 ** t
            i += 1
        print(name[i - 1])
