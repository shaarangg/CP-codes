n,k = map(int,input().split())
a = list(map(int,input().split()))
t=0
for i in range(n-1):
    s =  a[i] + a[i+1]
    if(s<k):
        t+=k-s
        a[i+1]+=k-s
s=""
for i in range(n):
    s+=str(a[i])+" "
print(t)
print(s[:len(s)-1])