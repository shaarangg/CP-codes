n = int(input())
res=[]
def remove1():
    global a
    u=0
    global max
    max=0
    b=""
    for i in range(len(a)):
        c=0
        if(a[i]=='1'):
            for j in range(i,len(a)):
                if(a[j]=='1'):
                    c+=1
                    u=j
                else:
                    break
        if(max<c):
            max=c
            b=a[i:u+1]
    a=a.replace(b,"",1)

for i in range(n):
    a=input()
    alice=0
    while('1' in a):
        remove1()
        alice+=max
        remove1()
    res.append(alice)
for i in res:
    print(i)