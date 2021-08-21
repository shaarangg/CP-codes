def check(t, m):
    if len(t) != (len(m) * 2):
        return "NO"
    else:
        for i in range(len(m)):
            if m[i] < t[i] or m[i] > t[i + len(m)]:
                return "NO"
        return "YES"


for k in range(int(input())):
    n = int(input())
    a = input()
    t = []
    m = []
    for i in range(n):
        if a[i] == "T":
            t.append(i)
        else:
            m.append(i)
    print(check(t, m))
