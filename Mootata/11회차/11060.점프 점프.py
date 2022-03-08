import sys

input = sys.stdin.readline

n = int(input()) # 미로의 길이 N
maze = list(map(int, input().split()))
dp = [0] + [1001] * (n - 1)

for i in range(n):
    for j in range(1, maze[i] + 1):
        if i + j >= n:
            break
        dp[i + j] = min(dp[i + j], dp[i] + 1)

if dp[n - 1] == 1001:
    print(-1)
else:
    print(dp[n - 1])


# dp에는 해당 칸에 도달하기 위한 최소한의 점프 수를 넣음.
# 1 2 0 1 3 2 1 5 4 2
# dp[3]에는 2가 들어감 (maze[0]에서 maze[1]로, maze[1]에서 maze[3]으로 이동)