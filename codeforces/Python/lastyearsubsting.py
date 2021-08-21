t = int(input())
res=[]
for i in range(t):
    n = int(input())
    a = input()
    b="2020"
    f=0
    for j in range(5):
        if(b[:j]==a[:j] and b[j:]==a[n-(4-j):]):
            res.append("YES")
            f=1
            break
    if(f==0):
        res.append("NO")
for i in res:
    print(i)