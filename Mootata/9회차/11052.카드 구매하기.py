import sys

input = sys.stdin.readline

n = int(input()) # 구매하려는 카드의 수 n
prices = [0] + list(map(int, input().split()))

dp = [0] * 1001

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + prices[j])
        

print(dp[n])

# 카드 n개 살 때 최대 비용을 구하기 위한 비교
# dp[n]은 카드 n개를 구매할 때의 최대 비용이 들어있으므로,
# dp[1] + dp[n - 1]
# dp[2] + dp[n - 2]
# dp[3] + dp[n - 3]
# .
# .
# .
# dp[n] + dp[0]
# 이 값들을 모두 비교해서 가장 큰 값을 넣어주면 됨.