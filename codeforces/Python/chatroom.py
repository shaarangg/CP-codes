a = input()
b = ['h','e','l','l','o']
c=0
for i in a:
    if(i==b[c]):
        c+=1
    if(c==5):
        print("YES")
        exit()
print("NO")