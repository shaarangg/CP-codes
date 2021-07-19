s = input()
c = 0
for i in s:
    if i.islower():
        c += 1
    else:
        c -= 1
if c >= 0:
    print(s.lower())
else:
    print(s.upper())
