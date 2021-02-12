t = int(input())
res=[]
for i in range(t): 
    n = int(input())
    moves = (n*(n+1)*(n-1))//3
    res.append(moves)
for i in res:
    print(i)