def checkPrime(n):
    c = 0
    for i in range(2, int(n ** (0.5)) + 1):
        if n % i == 0:
            return n // i
    return 1


n = int(input())
s = n
while n > 1:
    n = checkPrime(n)
    s += n
print(s)
