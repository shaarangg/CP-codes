n = int(input())
s = input()
max=0
maxs=""
for i in range(n-1):
    c = s[i]+s[i+1]
    count=1
    for j in range(i+1,n-1):
        if((s[j]+s[j+1])==c):
            count+=1
    if(max<count):
        max=count
        maxs=c
print(maxs) 