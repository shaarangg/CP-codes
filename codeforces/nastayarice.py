t = int(input())
res=[]
for i in range(t):
    n,a,b,c,d=map(int,input().split())
    mingw = n*(a-b)
    maxgw = n*(a+b)
    minpw = c-d
    maxpw = c+d
    f=0
    if((maxgw-mingw)>(maxpw-minpw)):
        if((minpw>=mingw and minpw<=maxgw)or(maxpw<=maxgw and maxpw>=mingw)):
            res.append("YES")
        else:
            res.append("NO")
    else:
        if((mingw>=minpw and mingw<=maxpw) or (maxgw<=maxpw and maxgw>=minpw)):
            res.append("YES")
        else:
            res.append("NO")
for i in res:
    print(i)