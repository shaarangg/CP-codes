n = int(input())
a = input()
c = a.count('0')
d= a.count('1')
if(c>d):
    print(c-d)
else:
    print(d-c)