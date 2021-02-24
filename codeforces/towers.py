n = int(input())
a = list(map(int,input().split()))
dict={}
max=0
for i in a:
    try:
        dict[i]=dict.get(i)+1
    except:
        dict.update({i:1})
    if(dict.get(i)>max):
            max=dict.get(i)
s = str(max)+" "+str(len(set(a)))
print(s)