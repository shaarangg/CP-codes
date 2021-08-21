n = int(input())
sqrt = n ** (0.5)
if sqrt == int(sqrt):
    print(int(sqrt) * 4)
else:
    sqrt = int(sqrt)
    if sqrt * (sqrt + 1) >= n:
        print(2 * (sqrt + sqrt + 1))
    else:
        print(4 * (sqrt + 1))
