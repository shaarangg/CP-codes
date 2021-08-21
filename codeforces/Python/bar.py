n = int(input())
d = [
    "ABSINTH",
    "BEER",
    "BRANDY",
    "CHAMPAGNE",
    "GIN",
    "RUM",
    "SAKE",
    "TEQUILA",
    "VODKA",
    "WHISKEY",
    "WINE",
]
c = 0
for i in range(n):
    s = input()
    if s.isnumeric():
        s = int(s)
        if s < 18:
            c += 1
    else:
        if s in d:
            c += 1
print(c)
