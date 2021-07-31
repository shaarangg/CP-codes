m = int(input())
n = int(input())
grid = [[0 for i in range(n + 1)] for j in range(m + 1)]
grid[1][1] = 1
for i in range(m + 1):
    for j in range(n + 1):
        if j + 1 < n + 1:
            grid[i][j + 1] += grid[i][j]
        if i + 1 < m + 1:
            grid[i + 1][j] += grid[i][j]
print(grid[n][m])
