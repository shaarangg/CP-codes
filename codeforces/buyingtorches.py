t = int(input())
res=[]
for i in range(t):
    x,y,k = map(int,input().split())
    ns = (y+1)*k -1 + x-2 
    nt = ns//(x-1) + k
    res.append(nt)
for i in res:
    print(i)    