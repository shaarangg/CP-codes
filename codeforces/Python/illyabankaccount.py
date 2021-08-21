n = int(input())
if(n>0):
    print(n)
elif(n<0 and n>-10):
    print(0)
else:
    n=abs(n)
    a = n%10
    b=(n//10)%10
    if(a>b):
        print(-(n//10))
    else:
        print(-(int(str(n//100) + str(a))))