for i in range(int(input())):
    s = input()
    m = 0
    index = len(s) + 1
    for j in reversed(range(len(s))):
        if s[j] == "R":
            t = index - (j + 1)
            index = j + 1
            if t > m:
                m = t
    if index > m:
        m = index
    print(m)
