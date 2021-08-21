t = int(input())
res=[]
for i in range(t):
    a = input()
    cq=0
    c=0
    if(len(a)%2!=0 or a[0]==')' or a[len(a)-1]=='('):
        res.append("NO")
    else:
        res.append("YES")
for i in res:
    print(i)