n = int(input())
s = n
div = 2
while n > 1:
    if n % div == 0:
        n = n // div
    else:
        for i in range(div + 1, n + 1):
            if n % i == 0:
                div = i
                n = n // div
                break
    s += n
print(s)
