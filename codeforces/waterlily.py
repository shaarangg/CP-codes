h,l = map(int,input().split())
x = (pow(l,2) - pow(h,2))/(2*h)
print("{0:.13f}".format(x))