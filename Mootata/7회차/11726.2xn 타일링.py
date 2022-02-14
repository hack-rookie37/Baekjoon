n = int(input()) # 2 x n 크기의 직사각형 타일

dp = [0, 1, 2, 3]

for i in range(4, 60001):
    dp.append(dp[i - 1] + dp[i - 2])
    
print(dp[n] % 10007)