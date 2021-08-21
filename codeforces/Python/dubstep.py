a =input().split('WUB')
a= [i for i in a if i]
s=""
for i in a:
    s+=i+" "
print(s[:len(s)-1])