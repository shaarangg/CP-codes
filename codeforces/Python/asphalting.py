n = int(input())
hr=[]
vr=[]
s=""
for i in range(n**2):
    h,v = map(int,input().split())
    if(h not in hr and v not in vr):
        hr.append(h)
        vr.append(v)
        s+=str(i+1)+" "
print(s[:len(s)-1])