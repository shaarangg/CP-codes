n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a != b:
        print("Happy Alex")
        exit(0)
print("Poor Alex")
