t = int(input())
for i in range(t):
    n = int(input())
    print(2)
    a = n
    b = n-1
    for i in range(n-1):
        print("{} {}".format(a,b))
        a = round((a+b)/2)
        b-=1    