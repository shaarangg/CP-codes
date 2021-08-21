n = int(input())
a = list(map(int,input().split()))
m=0
for i in range(n-1):
    if(m==0):
        if(a[i]==a[i+1]):
            m=1
        elif(a[i]>a[i+1]):
            m=2
    elif(m==1):
        if(a[i]<a[i+1]):
            print("NO")
            exit(0)
        elif(a[i]>a[i+1]):
            m=2
    else:
        if(a[i]<a[i+1] or a[i]==a[i+1]):
            print("NO")
            exit(0)
print("YES")