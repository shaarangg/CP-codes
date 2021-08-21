n = int(input())
if((n & n-1)==0):
    print(1)
else:
    a = str(bin(n))
    print(a.count('1'))