x,y,z = map(int,input().split())
n = x//z + y//z
x%=z
y%=z
if(x!=0 and y!=0 and x+y>=z):
    print("{} {}".format(n+1,z-x if x>y else z-y))
else:
    print("{} {}".format(n,0))