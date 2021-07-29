n = int(input())
numbers = [0 for i in range(n + 1)]
numbers[0] = numbers[1] = 1
for i in range(2, n + 1):
    if numbers[i] == 0:
        for j in range(i * i, n + 1, i):
            numbers[j] = 1
prime = []
for i in range(1, n):
    if numbers[i] == 0:
        prime.append(i)
print(*prime)
