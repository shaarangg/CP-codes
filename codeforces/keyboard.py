s="qwertyuiop[]asdfghjkl;'zxcvbnm,./"
i='w'
ch = input()
a = input()
b=""
if(ch=='R'):    
    for i in range(len(a)):
        for j in range(len(s)):
            if(a[i]==s[j]):
                b+=s[j-1]
                break
if(ch=='L'):    
    for i in range(len(a)):
        for j in range(len(s)):
            if(a[i]==s[j]):
                b+=s[j+1]
                break
print(b)