def func(a):
    s = [0 for i in range(10 ** 6)]
    for i in a:
        if i > 0:
            s[i] = 1
    for i in range(1, 10 ** 6):
        if s[i] == 0:
            return i


if __name__ == "__main__":
    a = list(map(int, input().split()))
    print(func(a))
