n,m,k = map(int,input().split())
a = list(map(int,input().split()))
a.sort(reverse=True)
s = a[0]*k + a[1]
if(m%(k+1)==0):
    print(s*(m//(k+1)))
else:
    print(s*(m//(k+1)) + a[0]*(m%(k+1)))