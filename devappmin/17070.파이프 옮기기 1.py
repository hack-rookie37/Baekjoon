import sys

n = int(sys.stdin.readline())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
directions = [[[] for _ in range(n)] for _ in range(n)]
dp = [[[0, 0, 0, 0] for _ in range(n)] for _ in range(n)]
directions[0][1] = [1] # 1 for right, 2 for cross, and 3 for down
dp[0][1][1] = 1

for i in range(n):
    for j in range(n):
        if matrix[i][j]:
            continue
        
        if i > 0 and j > 0 and directions[i - 1][j - 1] and not matrix[i - 1][j] and not matrix[i][j - 1]:
            directions[i][j].append(2)
            dp[i][j][2] = sum(dp[i - 1][j - 1])
        
        if i > 0 and (2 in directions[i - 1][j] or 3 in directions[i - 1][j]):
            directions[i][j].append(3)
            dp[i][j][3] = sum(dp[i - 1][j][2:])
        
        if j > 0 and (1 in directions[i][j - 1] or 2 in directions[i][j - 1]):
            directions[i][j].append(1)
            dp[i][j][1] = sum(dp[i][j - 1][:3])

        directions[i][j] = list(set(directions[i][j]))

print(sum(dp[n - 1][n - 1]))