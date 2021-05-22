n,k = map(int,input().split())
if(n>=k):
    if(k%2==0):
        print(k//2 - 1)
    else:
        print(k//2)
else:
    print(max(0,(2*n - k + 1)//2))