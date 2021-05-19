n,m,a,b = map(int, input().split())
if(n%m==0):
    print(0)
else:
    print(min((n-(n//m)*m)*b, ((n//m + 1)*m -n)*a))