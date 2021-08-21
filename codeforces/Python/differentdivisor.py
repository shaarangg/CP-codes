t =int(input())
res=[]
def primecheck(n):
    for i in range(2,round(n**0.5)+1):
        if(n%i==0):

            return False
    return True
for i in range(t):
    d = int(input())
    a=[]
    p=1+d
    while(True):
        if(primecheck(p)):
            break
        else:
            p+=1
    q=p+d
    while(True):
        if(primecheck(q)):
            res.append(p*q)
            break
        else:
            q+=1
for i in res:
    print(i)