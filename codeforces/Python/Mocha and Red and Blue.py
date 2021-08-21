for t in range(int(input())):
    n = int(input())
    s = list(input())
    index = -1
    for i in range(n):
        if s[i] == "R" or s[i] == "B":
            index = i
            break
    if index == -1:
        for i in range(n):
            if i % 2 == 0:
                s[i] = "R"
            else:
                s[i] = "B"
    elif index == 0:
        for i in range(n):
            if s[i] == "?":
                if s[i - 1] == "R":
                    s[i] = "B"
                else:
                    s[i] = "R"
    else:
        for i in reversed(range(index)):
            if s[i] == "?":
                if s[i + 1] == "R":
                    s[i] = "B"
                else:
                    s[i] = "R"
        for i in range(index + 1, n):
            if s[i] == "?":
                if s[i - 1] == "R":
                    s[i] = "B"
                else:
                    s[i] = "R"
    ans = ""
    for i in range(n):
        ans += s[i]
    print(ans)
