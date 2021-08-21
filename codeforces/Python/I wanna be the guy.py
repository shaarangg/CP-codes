n = int(input())
p, *x = list(map(int, input().split()))
q, *y = list(map(int, input().split()))
if 0 in x:
    x.remove(0)
if 0 in y:
    y.remove(0)
if n == len(set(x + y)):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
