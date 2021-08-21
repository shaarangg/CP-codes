def remzeros(a):
    s=0
    i=0
    while(a>0):
        t = a%10
        a=a//10
        if(t==0):
            continue
        s+=t*pow(10,i)
        i+=1
    return s
if __name__=="__main__":
    x = int(input())
    y = int(input())
    s1 = remzeros(x+y)
    s2 = remzeros(x)+remzeros(y)
    if(s1==s2):
        print("YES")
    else:
        print("NO")