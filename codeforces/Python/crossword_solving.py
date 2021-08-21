n,m = map(int,input().split())
s = input()
t = input()
p=""
mi=10**9
for i in range(m-n+1):
    temp = t[i:n+i]
    tp=""
    c=0
    for j in range(n):
        if(s[j]!=temp[j]):
            c+=1
            tp+=str(j+1)+" "
    if(c<mi):
        mi=c
        p=tp
print(mi)
print(p)