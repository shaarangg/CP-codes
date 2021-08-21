import math
k = int(input())
l = int(input())
c=-1
while(l>1):
    if(l%k==0):
        l//=k
        c+=1
    else:
        print("NO")
        exit(0)
print("YES")
print(c)