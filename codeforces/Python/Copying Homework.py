n = int(input())
A = list(map(int, input().split()))
B = []
B.append(A[n - 1])
for i in range(n - 1):
    B.insert(i + 1, A[i])
print(*B)
