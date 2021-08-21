a = input()
b = input()
if(a!=b):
    print(len(a) if len(a)>len(b) else len(b))
else:
    print(-1)