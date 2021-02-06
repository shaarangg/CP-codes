k = int(input())
a = list(map(int,input().split()))
s=0
i=0
a.sort(reverse=True)
while(s<k and i<12):
    s+=a[i]
    i+=1
if(s>=k):
    print(i)
else:
    print(-1)