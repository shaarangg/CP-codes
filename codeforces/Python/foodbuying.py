t = int(input())
res=[]
for i in range(t):
    s = int(input())
    if(s<10):
        res.append(s)
    else:
        a=0
        n=s
        while(s>=10):
            c=s//10
            s=s+c
            s-=c*10
            a+=c
        res.append(n+a)
for i in res:
    print(i)