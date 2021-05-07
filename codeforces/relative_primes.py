l,r = map(int,input().split())
print("YES")
for i in range(l,r+1,2):
    print("{} {}".format(i,i+1))