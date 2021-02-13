n,m = map(int,input().split())
dict={}
for i in range(m):
    b = input().split()
    dict.update({b[0]:b[1]})
lecture=input().split()
s=""
for i in lecture:
    if(len(dict[i])<len(i)):
        s+=dict[i]+" "
    else:
        s+=i+" "
print(s[:len(s)-1])