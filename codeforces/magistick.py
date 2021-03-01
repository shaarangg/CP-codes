t = int(input())
res=[]
for i in range(t):
    x,y = map(int,input().split())
    if(x==y):
        res.append("YES")
    elif(y<x):
        res.append("YES")
    else:
      if(x==2 and y==3):
          res.append("YES")
      elif(x<=3):
          res.append("NO")
      else:
          res.append("YES")
for i in res:
    print(i)  