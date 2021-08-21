for i in range(int(input())):
    t = input()
    c = [0, 0]
    f = t[0]
    for i in t:
        if i == "0":
            c[0] += 1
        else:
            c[1] += 1
    if f == "0":
        if c[0] == len(t):
            print(t)
        else:
            print("01" * len(t))
    if f == "1":
        if c[1] == len(t):
            print(t)
        else:
            print("10" * len(t))
