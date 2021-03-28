a = input()
b = a[::-1]
c=0
for i in range(len(b)):
    if(a[i]!=b[i]):
        c+=1
if(c==2 or (c==0 and len(a)%2!=0)):
    print("YES")
else:
    print("NO")