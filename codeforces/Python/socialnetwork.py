n,k = map(int,input().split())
id = list(map(int,input().split()))
m=[]
for i in range(n):
    if id[i] not in m:
        if(len(m)!=k):
            m.insert(0,id[i])
        else:
            m.pop(k-1)
            m.insert(0,id[i])
if(len(set(id))<k):
    print(len(set(id)))
else:
    print(k)
s=""
for i in m:
    s+=str(i)+" "
print(s[:len(s)-1])