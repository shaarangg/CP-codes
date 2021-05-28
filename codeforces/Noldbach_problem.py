n, k = map(int,input().split())
p=[]
c=0
if(n<13 and k>0):
    print("NO")
elif(n<13 and k==0):
    print("YES")
else:
    for i in range(2,n+1):
        f=0
        for j in range(2,i):
            if(i%j==0):
                f=1
                break
        if(f==0):
            p.append(i)
    for i in range(5,len(p)):
        for j in range(len(p)-1):
            if(p[i]==p[j]+p[j+1]+1):
                c+=1
                break
    if(c>=k):
        print("YES")
    else:
        print("NO")