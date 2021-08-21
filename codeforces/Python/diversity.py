s = input()
k = int(input())
if k > len(s):
    print("impossible")
else:
    a = len(set(s))
    if a >= k:
        print(0)
    else:
        print(k - a)
