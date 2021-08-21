t = int(input())
res=[]
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    res.append(abs(a[n]-a[n-1]))
for i in res:
    print(i)