N = int(input())
# dp = 0 ~ 5000 list
# len = 5001
dp = [None, None, None, 1, None, 1] + [None]*4995

# Recurrence relation(점화식)
# dp[N] = min(dp[3] + dp[N-3], dp[5] + dp[N-5])
for i in range(6, N+1):
    if not (dp[i-3] or dp[i-5]):  # NOR gate
        continue
    p = q = 5000
    if dp[i-3]:
        p = dp[3] + dp[i-3]
    if dp[i-5]:
        q = dp[5] + dp[i-5]
    dp[i] = min(p, q)

if dp[N] is None:
    print(-1)
else:
    print(dp[N])
