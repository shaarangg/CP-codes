n = int(input())
a = list(map(int,input().split()))
j=n
for i in range(n-1):
    if(i<j and a[i]>a[i+1]):
        if(a[i]==n):
            j=i
        else:
            print("NO")
            exit(0)
    if(i>=j and a[i]<a[i+1]):
        print("NO")
        exit(0)
print("YES")