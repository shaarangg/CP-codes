n = int(input())
a = list(map(int,input().split()))
a.sort()
if(sum(a[:n])==sum(a[n:])):
    print(-1)
else:
    s=""
    for i in a:
        s+=str(i)+" "
    print(s[:len(s)-1])