t = int(input())
res=[]
for i in range(t):
    a = input()
    s = min(a.count('0'),a.count('1'))
    if(s%2==0):
        res.append("NET")
    else:
        res.append("DA")
for i in res:
    print(i)