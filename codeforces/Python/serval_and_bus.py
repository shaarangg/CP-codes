n,t = map(int,input().split())
m=10**9
j=0
for i in range(n):
    s,d = map(int,input().split())
    if(t<=s):
        a=s-t
    else:
        a=t-s
        if(a%d==0):
            a=0
        else:
            a = (a//d + 1)*d -t + s
    if(m>a):
        m=a
        j=i+1
print(j)