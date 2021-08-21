t = int(input())
res=[]
for i in range(t):
    n = int(input())
    s = input()
    count=0
    sn=0
    for i in range(n):
        if(s[i]=='('):
            sn+=1
        elif(s[i]==')'):
            sn-=1
        if(sn==-1):
            count+=1
            sn=0
    res.append(count)
for i in res:
    print(i)