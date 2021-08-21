for i in range(int(input())):
    n, m = map(int, input().split())
    matrix = []
    row = 0
    col = 0
    for i in range(n):
        f = 0
        c = list(map(int, input().split()))
        for j in c:
            if j == 1:
                f = 1
                break
        if f == 0:
            row += 1
        matrix.append(c)
    for i in range(m):
        f = 0
        for j in range(n):
            if matrix[j][i] == 1:
                f = 1
                break
        if f == 0:
            col += 1
    if(min(row,col)%2==0):
        print("Vivek")
    else:
        print("Ashish")