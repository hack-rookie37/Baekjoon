t = int(input()) # 테스트 케이스 수 t

for i in range(t):
    n = int(input()) # n번째 정삼각형
    dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    
    if n > 10:
        for j in range(11, n + 1):
            dp.append(dp[j - 5] + dp[j - 1])
    print(dp[n])