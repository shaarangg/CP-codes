t = int(input())
res=[]
def ls(s1,s2):
    a=[]
    if(len(s1)>len(s2)):
        a.append(s1)
        a.append(s2)
    else:
        a.append(s2)
        a.append(s1)
    return a            
for i in range(t):
    b=ls(input(),input())
    l1=len(b[0])
    l2=len(b[1])
    if(l1%l2==0 and b[0]==(b[1]*(l1//l2))):
            res.append(b[0])
    else:
        for i in range(l1+1,(l1*l2)+1):
            if(i%l2==0 and i%l1==0):
                b[0]=b[0]*(i//l1)
                b[1]=b[1]*(i//l2)
                break
        if(b[0]==b[1]):
            res.append(b[0])
        else:
            res.append(-1)
for i in res:
    print(i)