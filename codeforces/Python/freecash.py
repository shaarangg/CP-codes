n = int(input())
b=input()
max=0
count=1
for i in range(n-1):
    a=input()
    if(b==a):
        count+=1
    else:
        b=a
        if(count>max):
            max=count
        count=1
if(count>max):
        max=count
print(max)