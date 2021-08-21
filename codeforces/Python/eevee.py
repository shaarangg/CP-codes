p = [
    "vaporeon",
    "jolteon",
    "flareon",
    "espeon",
    "umbreon",
    "leafeon",
    "glaceon",
    "sylveon",
]
m = 0
s = ""
n = int(input())
a = input()
for i in range(8):
    c = 0
    if len(p[i]) == n:
        if a == n * ".":
            s = p[i]
        else:
            for j in range(n):
                if p[i][j] == a[j]:
                    c += 1
    if c > m:
        m = c
        s = p[i]
print(s)
