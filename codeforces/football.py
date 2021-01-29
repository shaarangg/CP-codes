a =input()
for i in range(len(a)-6):
    c1,c2=0,0
    if(a[i]=='1'):
        for j in range(i, len(a)):
            if(a[j]=='1'):
                c1+=1
            else:
                break
    else:
        for j in range(i, len(a)):
            if(a[j]=='0'):
                c2+=1
            else:
                break
    if(c1>=7 or c2>=7):
        print("YES")
        exit()
print("NO")