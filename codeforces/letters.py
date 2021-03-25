n,m = map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
res=[]
for i in range(m):
    sum=0
    for j in range(n):
        sum+=a[j]
        if(b[i]<=sum):
            room=str(j+1)+" "+str(a[j]-(sum-b[i]))
            res.append(room)
            break
for i in res:
    print(i)
