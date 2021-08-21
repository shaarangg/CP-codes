import math

a, b, c = map(int, input().split())
t = math.ceil(a * c / b) - c
print(t)
