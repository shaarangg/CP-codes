n,a,b = map(int,input().split())
np = n-1-a
pos=1
if(b<np):
    pos+=b
else:
    pos+=np
print(pos)