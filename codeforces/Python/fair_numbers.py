t = int(input())
res=[]
for i in range(t):
    n = int(input())
    while(1):
        n1=n
        f=0
        while(n1>0):
            d=n1%10
            if(d!=0 and n%d!=0):
                f=1
                n+=1
                break
            n1//=10
        if(f==0):
            res.append(n)
            break
for i in res:
    print(i)