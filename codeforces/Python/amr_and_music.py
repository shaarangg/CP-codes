n,k = map(int,input().split())
a = list(map(int,input().split()))
b=[i for i in a]
b.sort()
c=[]
for i in b:
    if(k-i>=0):
        k-=i
        for j in range(len(a)):
            if(a[j]==i and j+1 not in c):
                c.append(j+1)
                break
print(len(c))
s=""
for i in c:
    s+=str(i)+" "
if(s!=""):
    print(s[:len(s)-1]) 