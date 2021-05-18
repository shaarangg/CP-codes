n = int(input())
a = set(map(int,input().split()))
c=n-len(a)
for i in a:
    if(i>n):
        c+=1
print(c)