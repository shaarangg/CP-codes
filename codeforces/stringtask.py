a = input().lower()
vowel = ["a","o","y","e","u","i"]
s=""
for i in a:
    if i not in vowel:
        s+="."+i
print(s)