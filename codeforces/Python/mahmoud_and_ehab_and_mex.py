n,x = map(int,input().split())
a = list(map(int,input().split()))
op=0
if(x==0):
    if(0 not in a):
        print(0)
    else:
        print(1)
else:
    for i in range(0,x):
        if(i not in a):
            op+=1
    if(x in a):
        op+=1
    print(op)