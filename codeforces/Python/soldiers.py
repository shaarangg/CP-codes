a = list(map(int,input().split()))
cost = ((a[2]*(a[2]+1))//2)*a[0]
if(a[1]>=cost):
    print(0)
else:
    print(cost-a[1])