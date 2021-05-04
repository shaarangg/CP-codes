t = int(input())
res=[]
for i in range(t):
    n = int(input())
    s = input()
    f=0
    for i in range(0,n//2):
        a=ord(s[i])
        b=ord(s[n-i-1])
        if(a==b or a-1==b-1 or a+1==b-1 or a-1==b+1 or a+1==b+1):
            f=0
        else:
            res.append("NO")
            f=1
            break
    if(f==0):
        res.append("YES")
for i in res:
    print(i)