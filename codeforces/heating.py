n = int(input())
for i in range(n):
    r,sec = map(int,input().split())
    if(sec%r==0):
        print(((sec//r)**2)*r)
    else:
        a = sec//r
        b = sec%r
        print((a**2)*(r-b) + ((a+1)**2)*(b))