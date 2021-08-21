t = int(input())
res=[]
for i in range(t):
    n=int(input())
    r = input()
    m=0
    for i in range(n):
        if(r[i]=="1"):
            if(i+1>m):
                m=i+1
            if(n-i>m):
                m=n-i
    res.append(m*2 if m*2>n else n)
for i in res:
    print(i)