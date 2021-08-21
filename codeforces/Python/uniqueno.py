t= int(input())
for i in range(t):
    x = int(input())
    a=[]
    for i in range(9,-1,-1):
        if(x>=i and x>0):
            a.append(i)
            x-=i
    if(x==0):
        s=0
        for i in range(len(a)-1,-1,-1):
            s+=a[i]*(10**i)
        print(s)
    else:
        print(-1)