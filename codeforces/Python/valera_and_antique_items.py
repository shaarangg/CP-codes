n,v = map(int, input().split())
s=""
c=0
for i in range(n):
    k = list(map(int,input().split()))
    for j in range(1,k[0]+1):
        if(v>k[j]):
            s+=str(i+1)+" "
            c+=1
            break
print(c)
if(c!=0):
    print(s[:len(s)-1])