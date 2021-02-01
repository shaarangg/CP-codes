n = int(input())
a = list(map(int,input().split()))
a.sort()
s=""
for i in a:
    s=s+str(i)+" "
print(s[:len(s)-1])