n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))

dp = [1] + [0] * k

for i in coins:
    for j in range(i, k + 1):
        dp[j] += dp[j - i] # j원을 만드는 경우의 수에 각 코인을 더한 경우의 수를 더함

print(dp[k])