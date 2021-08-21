n = int(input())
a = list(map(int,input().split()))
a.sort()
b=""
b1=0
c=""
c1=0
d={}
for i in range(n):
    if(a[i] in d):
        s=d[a[i]]
        if(s==1):
            d.update({a[i]:s+1})
            c=str(a[i])+" "+c
            c1+=1
        else:
            print("NO")
            exit(0)
    else:
        d.update({a[i]:1})
        b+=str(a[i])+" "
        b1+=1
print("YES")
print(b1)
print(b)
print(c1)
print(c)