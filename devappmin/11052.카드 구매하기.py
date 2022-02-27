import sys

n = int(sys.stdin.readline())
card_pack = [0, *list(map(int, sys.stdin.readline().split()))]
dp = [0] * (n + 1)

for i_idx in range(1, n + 1):
    for j_idx in range(1, i_idx + 1):
        dp[i_idx] = max(dp[i_idx], dp[i_idx - j_idx] + card_pack[j_idx])

print(dp[i_idx])