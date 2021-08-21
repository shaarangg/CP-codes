A,B,C,N = map(int,input().split())
if(N-(A+B-C)>=1 and C<=A and C<=B):
    print(N-(A+B-C))
else:
    print(-1)