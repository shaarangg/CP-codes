for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    even = []
    odd = []
    for j in range(2 * n):
        if a[j] % 2 == 0:
            even.append(j + 1)
        else:
            odd.append(j + 1)
    if len(even) >= 2 and len(even) % 2 == 0:
        even.pop()
        even.pop()
    elif len(odd) >= 2 and len(odd) % 2 == 0:
        odd.pop()
        odd.pop()
    else:
        even.pop()
        odd.pop()
    if len(even) != 0:
        for j in range(0, len(even), 2):
            print("{} {}".format(even[j], even[j + 1]))
    if len(odd) != 0:
        for j in range(0, len(odd), 2):
            print("{} {}".format(odd[j], odd[j + 1]))
