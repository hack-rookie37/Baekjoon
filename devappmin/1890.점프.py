import sys
input = sys.stdin.readline

dy, dx = [1, 0], [0, 1]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            print(dp[n - 1][n - 1])
            break

        current = graph[i][j]

        if j + current < n:
            dp[i][j + current] += dp[i][j]
        
        if i + current < n:
            dp[i + current][j] += dp[i][j]

# DFS, BFS로 하면 시간/메모리 초과가 발생하니 DP로 해결하자