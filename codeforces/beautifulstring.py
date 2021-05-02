t = int(input())
res=[]
for i in range(t):
    s = input()
    c=['a','b','c']
    f=0
    for i in range(len(s)-1):
        if(s[i]!='?' and s[i]==s[i+1]):
            res.append(-1)
            f=1
            break
        elif(s[i]=='?'):
            if(i==0):
                for j in range(3):
                    if(c[j]!=s[i+1]):
                        s=s[:i]+c[j]+s[i+1:]
                        break
            else:
                for j in range(3):
                    if(c[j]!=s[i-1] and c[j]!=s[i+1]):
                        s=s[:i]+c[j]+s[i+1:]
                        break
    if(f==0):
        if(s[len(s)-1]=='?'):
            for j in range(3):
                if(c[j]!=s[len(s)-2]):
                    s=s[:len(s)-1]+c[j]
                    break
        res.append(s)
for i in res:
    print(i)