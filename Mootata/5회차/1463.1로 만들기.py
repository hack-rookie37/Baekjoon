n = int(input())
dp = [0] * (n + 1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    
    if i % 2 == 0: # 짝수 일 때
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0: # 3의 배수일 때는 (i값을 3으로 나눈 값을 인덱스로 하는 dp값 + 1)
        dp[i] = min(dp[i], dp[i // 3] + 1)
        
print(dp[n])