s = input()
c=0
j=s.find('1')
if(j!=-1):
    for i in range(j+1,len(s)):
        if(s[i]=='0'):
            c+=1
        if(c==6):
            print("yes")
            exit(0)
print("no")