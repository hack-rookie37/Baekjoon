n = int(input()) # 2 x n 크기의 직사각형
dp = [0, 1, 3, 5, 11]

for i in range(5, n + 1):
    dp.append(dp[i - 1] + (dp[i - 2] * 2))
    
print(dp[n] % 10007)