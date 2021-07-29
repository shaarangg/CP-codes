k = int(input())
i = 0
while k > 0:
    i += 1
    k -= len(str(i))
i = str(i)
print(i[len(i) - 1 + k])
