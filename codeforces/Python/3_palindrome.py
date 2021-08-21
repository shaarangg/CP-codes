n = int(input())
s=""
for i in range(1,n+1):
    if(i%4==1 or i%4==2):
        s+="a"
    if(i%4==0 or i%4==3):
        s+="b"
print(s)