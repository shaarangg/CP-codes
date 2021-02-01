a = list(map(int,input().split()))
if(a[0]%2==0):
    if(a[1]>a[0]//2):
        print((a[1]-a[0]//2)*2)
    else:
        print(a[1]+a[1]-1)
else:
    if(a[1]>(a[0]//2)+1):
        print((a[1]-((a[0]//2)+1))*2)
    else:
        print(a[1]+a[1]-1)