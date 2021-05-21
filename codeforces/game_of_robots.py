import math
n,k = map(int,input().split())
id = list(map(int,input().split()))
i = (-1 + math.sqrt(8*k + 1))/2
if(int(i)==i):
    i= int(i)
    print(id[i-1])
else:
    i=int(i)
    s = (i*(i+1))//2
    print(id[k - s -1])