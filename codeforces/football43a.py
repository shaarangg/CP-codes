n = int(input())
dict={}
for i in range(n):
    a=input()
    try:
        dict[a]+=1
    except:
        dict.update({a:1})
max=0
s=""
for i in dict:
    if(dict[i]>max):
        max=dict[i]
        s=i
print(s)