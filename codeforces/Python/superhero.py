t = input()
s = input()
v = ['a','e','i','o','u']
c = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
if(len(s)!=len(t)):
    print("No")
else:
    for i in range(len(s)):
        if((s[i] in v and t[i] in v) or (s[i] in c and t[i] in c)):
            continue
        else:
            print("No")
            exit(0)
    print("Yes")