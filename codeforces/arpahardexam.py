n = int(input())
a = [1,8,4,2,6]
if(n==0):
    n=0
elif(n%4==0):
    n=4
else:
    n=n%4
print(a[n])