n = int(input())
m=0
for i in range(n):
    w,h = map(int,input().split())
    if(i==0):
        m=max(w,h)
    else:
        if(m>=w and m>=h):
            m = max(w,h)
        elif(m>=w):
            m=w
        elif(m>=h):
            m=h
        else:
            print("NO")
            exit(0)
print("YES")