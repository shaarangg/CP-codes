n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
u = list(bytearray(n))
s=""
pos=0
for i in b:
    if(u[i-1]):
        s+="0 "
        continue
    c=0
    while(True):
        c+=1
        u[a[pos]-1]=1
        if(a[pos]==i):
            break
        pos+=1
    s+=str(c)+" "
    pos+=1
print(s)