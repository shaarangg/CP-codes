n = int(input())
s = input()
if(n<=26):
    print(len(s)-len(set(list(s))))
else:
    print(-1)