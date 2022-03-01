import sys

n = int(sys.stdin.readline())

dp = []
dp.extend([1, 2, 5])

ans = []
ans.extend([2, 6, 16])

for idx in range(3, n):
    dp.append(( dp[idx - 1] + ans[idx - 2] + 1 ) % 9901)
    ans.append(( dp[idx] * 2 + ans[idx - 1] ) % 9901)

print(( ans[n - 1] + 1 ) % 9901)

# 1     2 + 1               3   2
# 2     4 + 2 + 1           7   6
# 3     6 + 6 + 2 + 1       17  16
# 4                         41  40

# 1 1
# 2 2
# 5 5
# 12 12
