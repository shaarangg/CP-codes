n = int(input())
s = input()
c = 0
for i in range(n):
    if s[i] == "A":
        c += 1
    else:
        c -= 1
if c > 0:
    print("Anton")
elif c == 0:
    print("Friendship")
else:
    print("Danik")
