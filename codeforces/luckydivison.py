import re
n = int(input())
def luckynocheck(a):
    s= r"^(4|7)*$"
    if re.match(s,str(a)):
        return True
    else: 
        return False
if(luckynocheck(n)):
    print("YES")
    exit()
for i in range(4,n):
    if(n%i==0 and luckynocheck(i)):
        print("YES")
        exit()
print("NO")