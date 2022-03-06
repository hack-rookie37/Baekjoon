n = int(input()) # 2 * N 크기의 우리

dp = [0, 3, 7]

for i in range(3, n + 1):
    dp.append(((dp[i - 1] * 2) + dp[i - 2]) % 9901)

print(dp[n])


# n = 1, 3
# n = 2, 4 + 2 + 1  = 7
# n = 3, 6 + 8 + 2 + 1 = 17
# n = 4, 41