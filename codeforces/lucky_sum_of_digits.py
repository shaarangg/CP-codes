n = int(input())
n1=n
c=0
if(n%7==0):
    print("7"*(n//7))
    exit(0)
while(n1>0):
    n1-=4
    c+=1
    if(n1%7==0):
        print("4"*c + "7"*(n1//7))
        exit(0)
if(n%4==0):
    print("4"*(n//4))
else:    
    print(-1)