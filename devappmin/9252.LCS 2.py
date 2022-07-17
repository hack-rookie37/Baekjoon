import sys

MAX = 1001

s1 = list(sys.stdin.readline().rstrip())
s2 = list(sys.stdin.readline().rstrip())
s1l, s2l = len(s1), len(s2)
dp = [[0] * MAX for _ in range(MAX)]
path = [[""] * MAX for _ in range(MAX)]

for y in range(1, s1l + 1):
    for x in range(1, s2l + 1):
        if s1[y - 1] == s2[x - 1]:
            dp[y][x] = dp[y - 1][x - 1] + 1
            path[y][x] = path[y - 1][x - 1] + s1[y - 1]
            continue

        dp[y][x] = max(dp[y][x - 1], dp[y - 1][x])
            
        if dp[y][x] == dp[y][x - 1]:
            path[y][x] = path[y][x - 1]
        else:
            path[y][x] = path[y - 1][x]

print(dp[y][x], path[y][x], sep="\n")