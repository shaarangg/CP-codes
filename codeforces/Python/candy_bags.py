n = int(input())
a=[]
res=[]
for i in range(1,((n**2)//2)+1):
    a.append(i)
    a.append((n**2)+1-i)

for i in range(0,n**2,n):
    s=""
    for j in range(i,n+i):
        s+=str(a[j])+" "
    res.append(s)
for i in res:
    print(i[:len(i)-1])