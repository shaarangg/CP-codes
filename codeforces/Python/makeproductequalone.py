n=int(input())
a =  list(map(int,input().split()))
b=a.count(0)
mcoin=0
c0=0
cn=0
for i in a:
    if(i>0):
        mcoin+=i-1
    elif(i<0):
        cn+=1
        mcoin+=-1-i
    else:
        c0+=1
if(cn%2==0):
    mcoin=mcoin+c0
elif(cn%2!=0 and c0>0):
    mcoin=mcoin+c0
else:
    mcoin=mcoin+2
print(mcoin)