n = int(input())
i = 1
s = 1
while s < n:
    i += 1
    s = (i * (i + 1)) // 2
a = ((i - 1) * i) // 2
print(n - a)
