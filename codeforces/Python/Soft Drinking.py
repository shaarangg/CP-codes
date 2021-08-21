n, k, l, c, d, p, nl, np = map(int, input().split())
tl = k * l
# Total no. of literes of drink
ns = c * d
# Total no. of slice of lime
# print(tl // (n * nl))
# print(ns // n)
# print(p // (n * np))
print(min(tl // (n * nl), ns // n, p // (n * np)))
