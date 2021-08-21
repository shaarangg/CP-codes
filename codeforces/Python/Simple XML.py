s = input().split(">")
i = 0
h = 0
while s[i] != "":
    t = s[i]
    if "/" in t:
        h -= 1
        print((2 * h * " ") + t + ">")
    else:
        print((2 * h * " ") + t + ">")
        h += 1
    i += 1
