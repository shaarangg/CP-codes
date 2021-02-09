n,m = map(int,input().split())
a = list(map(int,input().split()))
sl = m
j=0
pt=[]
for i in range(n):
    if(a[i]<sl):
        sl-=a[i]
        pt.append(0)
    elif(sl==a[i]):
        sl=m
        pt.append(1)
    else:
        a[i]-=sl
        x=1
        x+=a[i]//m
        y=a[i]%m
        sl=m-y
        pt.append(x)
s=""
for i in pt:
    s+="{} ".format(i)
print(s[:len(s)-1]) 