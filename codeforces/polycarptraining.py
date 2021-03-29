n = int(input())
a = list(map(int, input().split()))
a.sort()
c=1
for i in a:
    if(c>i):
        continue
    c+=1
print(c-1)