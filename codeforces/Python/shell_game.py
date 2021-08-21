n = int(input())
x = int(input())
s = [0,1,2]
n=n%6
for i in range(1,n+1):
    if(i%2==0):
        s[1],s[2]=s[2],s[1]
    else:
        s[0],s[1]=s[1],s[0]
print(s[x])