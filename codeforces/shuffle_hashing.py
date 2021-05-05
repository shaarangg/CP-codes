t = int(input())
for i in range(t):
    p = list(input())
    p.sort()
    h = input()
    l=len(p)
    f=0
    for j in range(len(h)-l+1):
        s=list(h[j:j+l])
        s.sort()
        if(p==s):
            print("YES")
            f=1
            break
    if(f==0):
        print("NO")