n = int(input())
d={}
for i in range(n):
    a = int(input())
    if a in d:
        d[a]+=1
    else:
        d.update({a:1})
a = list(d.keys())
if(len(d)==2 and d[a[0]]==d[a[1]]):
    print("YES")
    print("{} {}".format(a[0],a[1]))
else:
    print("NO")