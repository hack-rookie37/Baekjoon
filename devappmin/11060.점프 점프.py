import sys

n = int(sys.stdin.readline())
graph = list(map(int, sys.stdin.readline().split()))
dp = [9999999] * n
dp[0] = 0
ans = False

for idx in range(n):
    for jump in range(1, graph[idx] + 1):
        if idx + jump >= n:
            break

        dp[idx + jump] = min(dp[idx + jump], dp[idx] + 1)

    if dp[n - 1] != 9999999:
        ans = True
        break

print(-1 if not ans else dp[n - 1])
