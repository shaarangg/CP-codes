a1 = int(input())
a2 = int(input())
k1 = int(input())
k2 = int(input())
n = int(input())
if(k1>k2):
    k1+=k2
    k2=k1-k2
    k1-=k2
    a1+=a2
    a2=a1-a2
    a1-=a2
mn = a1*(k1-1) + a2*(k2-1)
if(mn>=n):
    mn=0
else:
    mn=n-mn
mx=0
if(n<=a1*k1):
    mx = n//k1
else:
    mx= a1 + (n-a1*k1)//k2
print("{} {}".format(mn,mx))