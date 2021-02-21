t = int(input())
res=[]
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    s=""
    for j in a:
        s+=str(j)+" "
    res.append(s[:len(s)-1])
for i in res:
    print(i)