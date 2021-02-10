n = int(input())
x=0
y=0
z=0
f=[]
for i in range(n):
    f = list(map(int,input().split()))
    x+=f[0]
    y+=f[1]
    z+=f[2]
if(x==0 and y==0 and z==0):
    print("YES")
else:
    print("NO")