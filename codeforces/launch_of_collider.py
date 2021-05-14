n = int(input())
d = input()
p = list(map(int,input().split()))
m=max(p)
f=0
for i in range(n-1):
    if(d[i]=='R' and d[i+1]=='L'):
        s=(p[i]+p[i+1])//2 - p[i]
        if(s<m):
            m=s
        f=1
if(f==0):     
    print(-1)
else:
    print(m)