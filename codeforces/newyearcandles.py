a,b = map(int,input().split())
t=0
while(a>0):
    a-=1
    t+=1
    if(t%b==0):
        a+=1
print(t)