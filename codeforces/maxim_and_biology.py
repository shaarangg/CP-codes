n = int(input())
a = "ACTG"
s = input()
m = 10**9
for i in range(n-3):
    c=0
    b = s[i:i+5]
    for j in range(4):
        t=0
        if(b[j]<=a[j]):
            t = min(ord(a[j])-ord(b[j]), ord(b[j])-ord('A')+ ord('Z')-ord(a[j])+1)
        else:
            t = min(ord(b[j])-ord(a[j]), ord(a[j])-ord('A')+ ord('Z')-ord(b[j])+1)
        c+=t
    if(m>c):
        m=c
print(m)