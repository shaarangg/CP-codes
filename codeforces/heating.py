n = int(input())
for i in range(n):
    c,sum = map(int,input().split())
    if(sum%c==0):
        print(((sum//c)**2)*c)