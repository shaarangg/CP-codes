n = input()
if(len(n)==1):
    print(n*2)
else:
    s = n[:len(n)-1]
    a = n[len(n)-1]
    print(s + a*2 + s[::-1])