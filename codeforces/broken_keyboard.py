t = int(input())
res=[]
for i in range(t):
    s = list(input())
    j=0
    while(j<len(s)-1):
        if(s[j]==s[j+1]):
            del s[j]
            del s[j]
        else:
            j+=1
    s=list(set(s))
    s.sort()
    a= ''.join([k for k in s])
    res.append(a)
for i in res:
    print(i)