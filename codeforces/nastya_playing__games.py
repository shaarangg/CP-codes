n,k = map(int,input().split())
if(k==1 or k==n):
    print(n*3)
else:
    print(min(n-k,k-1)+n*3)