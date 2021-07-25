s = input()
m = ["A", "H", "I", "M", "O", "T", "U", "V", "W", "X", "Y"]
a = s[::-1]
f = 0
if a == s:
    for i in a:
        if i in m:
            continue
        else:
            f = 1
            print("NO")
            break
else:
    print("NO")
    f = 1
if f == 0:
    print("YES")
