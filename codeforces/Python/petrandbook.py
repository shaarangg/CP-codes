n = int(input())
w = list(map(int,input().split()))
i=0
s=0
while(1):
    s+=w[i]
    if(s>=n):
        print(i+1)
        break
    i=(i+1)%7