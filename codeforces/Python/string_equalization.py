t = int(input())
res =[]
for i in range(t):
    s = input()
    t = input()
    f=0
    for i in range(len(s)):
        for j in range(len(t)):
            if(s[i]==t[j]):
                res.append("YES")
                f=1
                break
        if(f==1):
            break
    if(f==0):
        res.append("NO")
for i in res:
    print(i)