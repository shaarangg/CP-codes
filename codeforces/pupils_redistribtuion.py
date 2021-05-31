n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c=0
ac=[]
bc=[]
ac.append(a.count(1))
ac.append(a.count(2))
ac.append(a.count(3))
ac.append(a.count(4))
ac.append(a.count(5))
bc.append(b.count(1))
bc.append(b.count(2))
bc.append(b.count(3))
bc.append(b.count(4))
bc.append(b.count(5))
for i in range(5):
    if((ac[i]+bc[i])%2!=0):
        print(-1)
        exit(0)
    else:
        if(ac[i]>bc[i]):
            c+=ac[i]-bc[i]
c = c//2
print(c)