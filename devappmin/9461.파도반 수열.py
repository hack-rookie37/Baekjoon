loop = int(input())

dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(10, 101):
    dp.append(dp[i - 3] + dp[i - 2])

for i in range(loop):
    print(dp[int(input()) - 1])