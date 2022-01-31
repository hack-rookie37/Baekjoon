t = int(input()) # 테스트 케이스 수 t

for i in range(t):
    n = int(input()) # 나타내려는 수 n
    dp = [1, 2, 4]
    for j in range(3, n):
        dp.append(dp[j - 3] + dp[j - 2] + dp[j - 1])
    print(dp[n - 1])