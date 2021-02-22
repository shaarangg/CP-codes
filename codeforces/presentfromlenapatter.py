n = int(input())
s=""
a=[]
for i in range(n+1):
    s=" "*((n-i)*2)
    for j in range(0,i):
        s+=str(j)+" "
    for k in range(i,-1,-1):
        if(k>0):
            s+=str(k)+" "
        else:
            s+=str(k)
    print(s)
    a.append(s)
for i in range(n-1,-1,-1):
    print(a[i])