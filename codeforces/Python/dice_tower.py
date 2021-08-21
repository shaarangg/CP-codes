t = int(input())
a = list(map(int,input().split()))
for i in a:
    if(i%14>6 or i%14==0 or i<15):
        print("NO")
    else:
        print("YES")