a, b, c = map(int, input().split())
t = a / b
h = int((c / t) ** (0.5))
b = c // h
l = a // b
s = 4 * (l + b + h)
print(s)
