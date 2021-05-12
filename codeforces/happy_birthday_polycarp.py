import math
t = int(input())
res=[]
for i in range(t):
    n = int(input())
    a = math.floor(math.log10(n))
    c=9*a
    ch="1"
    g = int(ch*(a+1))
    while(g<=n):
        c+=1
        if(ch=="9"):
            break
        ch = chr(ord(ch)+1)
        g = int(ch*(a+1))
    res.append(c)
for i in res:
    print(i)