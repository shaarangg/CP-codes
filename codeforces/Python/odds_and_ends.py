n = int(input())
a = list(map(int, input().split()))
if n % 2 == 0:
    print("No")
else:
    if a[0] % 2 == 0 or a[n - 1] % 2 == 0:
        print("No")
    else:
        print("Yes")
