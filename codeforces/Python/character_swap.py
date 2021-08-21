t = int(input())
res=[]
for i in range(t):
    n = int(input())
    a = input()
    b = input()
    c=[]
    if(a==b):
        res.append("Yes")
        break
    else:
        if(n==2):
            if(a[0]==a[1] and b[0]==b[1]):
                res.append("Yes")
            else:
                res.append("No")
        else:
            for i in range(n):
                if(a[i]!=b[i]):
                    if(a[i] not in c):
                        c.append(a[i])
                    if(b[i] not in c):
                        c.append(b[i])
            if(len(c)==2):
                res.append("Yes")
            else:
                res.append("No")
for i in res:
    print(i)