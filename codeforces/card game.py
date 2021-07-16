suit = ["S", "H", "D", "C"]
rank = ["6", "7", "8", "9", "T", "J", "Q", "K", "A"]
s = input()
s1, s2 = input().split()
if s1[1] == s and s2[1] != s:
    print("YES")
elif s1[1] == s2[1] and rank.index(s1[0]) > rank.index(s2[0]):
    print("YES")
else:
    print("NO")
