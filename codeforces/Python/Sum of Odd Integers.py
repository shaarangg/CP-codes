t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    if n % 2 == k % 2 and n >= k ** 2:
        print("YES")
    else:
        print("NO")
