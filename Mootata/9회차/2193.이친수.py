n = int(input())

dp = [0, 1, 1, 2, 3]

for i in range(4, n + 1):
    dp.append(dp[i - 1] + dp[i])

print(dp[n])

# n = 1, 1
# n = 2, 10
# n = 3, 100, 101
# n = 4, 1000, 1001, 1010