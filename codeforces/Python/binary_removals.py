t=int(input())
res=[]
for i in range(t):
    s = input()
    c=0
    f=0
    for j in range(len(s)-1):
        if(s[j]=='1' and s[j+1]=='1'):
            c=1
            continue
        if(s[j]=='0' and s[j+1]=='0' and c==1):
            res.append("NO")
            f=1
            break
    if(f==0):
        res.append("YES")
for i in res:
    print(i)