n,k = map(int,input().split())
a=input()
s = [int(a[i:i + 1]) for i in range(0,n)]
if(n==1):
    if(k>0):
        print(0)
    else:
        print(a)
else:
    i=1
    if(s[0]>1 and k>0):
        s[0]=1
        k-=1
    while(i<n and k>0):
        if(s[i]!=0):
            s[i]=0
            k-=1
        i+=1
    b=""
    for i in s:
        b+=str(i)
    print(b)