n = int(input())
a = list(map(int,input().split()))
a.sort()
s=""
t=0
for i in range(n):
    if(i%2!=0):
        t=a[i]
        a[i]=a[i-1]
        a[i-1]=t
for i in a:
    s+=str(i)+" "
print((n-1)//2)
print(s[:len(s)-1])