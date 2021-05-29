a = list(map(int,input().split()))
m = sum(a)
if(m%2==0):
    m=m//2
    for i in range(len(a)):
        s=a[i]
        for j in range(len(a)):
            s=a[i]
            if(j==i):
                continue
            if(s+a[j]<=m):
                s+=a[j]
                for k in range(len(a)):
                    if(k==i or k==j):
                        continue
                    if(s+a[k]==m):
                        print("YES")
                        exit(0)
print("NO")