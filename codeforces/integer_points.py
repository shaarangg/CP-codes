t = int(input())
for i in range(t):
    n = int(input())
    p = list(map(int,input().split()))
    m = int(input())
    q = list(map(int,input().split()))
    c1=0
    c2=0
    for j in p:
        if(j%2==0):
            c1+=1
    for j in q:
        if(j%2==0):
            c2+=1
    print(n*m-((n-c1)*c2+(m-c2)*c1))