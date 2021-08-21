n = int(input())
a  = list(map(int,input().split()))
l=0
c=0
for i in range(n):
    if(c==0 and a[i]==1):
        c=1
        l=i
    elif(a[i]==1):
        c += min(2,i-l)
        l=i
print(c)