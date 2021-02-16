t = int(input())
res=[]
for i in range(t):
    n = int(input())
    a = n//4
    if(n%4!=0):
        a+=1 
    s = "9"*(n-a)+"8"*(a)
    res.append(s)
for i in res:
    print(i)