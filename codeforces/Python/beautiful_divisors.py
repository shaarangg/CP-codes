n = int(input())
m = 0
b = "1"
k = int(b, 2)
while k <= n:
    if n % k == 0 and k > m:
        m = k
    b = "1" + b + "0"
    k = int(b, 2)
print(m)
