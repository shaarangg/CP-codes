t = int(input())
res=[]
for i in range(t):
    n = int(input())
    if(n<2):
        res.append(-1)
    else:
        s="3"*(n-1)
        s = "2"+s 
        res.append(int(s))
for i in res:
    print(i)