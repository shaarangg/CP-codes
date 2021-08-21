n = int(input())
a = list(map(int,input().split()))
x = a.count(5)
y = a.count(0)
s=""
if(x>=9):
    if(y==0):
        print(-1)
    else:
        s = int(("5"*((x//9)*9)) + ("0"*y))
    print(s)
else:
    if(y==0):
        print(-1)
    else:
        print(0)