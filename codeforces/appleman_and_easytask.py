n = int(input())
a=[]
for i in range(n):
    a.append(list(input()))
for i in range(n):
    c=0
    for j in range(n):
        if(i-1>=0 and j>=0 and j<n and a[i-1][j]=='o'):
            c+=1
        if(i+1<n and j>=0 and j<n and a[i+1][j]=='o'):
            c+=1
        if(i>=0 and i<n and j-1>=0 and a[i][j-1]=='o'):
            c+=1
        if(i>=0 and i<n and j+1<n and a[i][j+1]=='o'):
            c+=1
        if(c%2!=0):
            print("NO")
            exit(0)
print("YES")