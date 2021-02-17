t = int(input())
res=[]
for i in range(t):
    a,b = map(int,input().split())
    count=0
    mcount=0
    f=0
    if(a>=b):
        while(a>=b):
            if(a==b):
                f=1
                break
            if(a%2==0):
                a=a>>1
            else:
                break
            count+=1
    else:
        while(b>a):
            if(b%2==0):
                b=b>>1
            else:
                break
            count+=1
            if(a==b):
                f=1
                break
    if(f==1):
        if(count>=3):
            mcount = count//3
            count%=3
        if(count>=2):
            mcount+=count//2
            count%=2
        if(count>=1):
            mcount+=count//1
        res.append(mcount)
    else:
        res.append(-1)
for i in res:
    print(i)