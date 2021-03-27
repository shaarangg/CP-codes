k = int(input())
a = input()
dict={}
s=""
for i in a:
    if i in dict.keys():
        dict[i]+=1
    else:
        dict[i]=1
for i in dict:
    if(dict[i]%k==0):
        s+=(i)*(dict[i]//k)
    else:
        print(-1)
        exit()
print(s*k)