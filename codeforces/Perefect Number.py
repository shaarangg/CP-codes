def sumOfDigits(s):
    c = 0
    while s > 0:
        c += s % 10
        s //= 10

    return c


k = int(input())
s = 19
while k > 1:
    s += 9
    if sumOfDigits(s) == 10:
        k -= 1
print(s)
