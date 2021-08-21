n = input()
if(len(n)<2):
    print(0)
else:
    c=0
    s=11
    while(s>=10):
        x=0
        for i in n:
            x+=int(i)
        n=str(x)
        c+=1
        s=x
    print(c)