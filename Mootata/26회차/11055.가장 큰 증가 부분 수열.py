n = int(input())
nums = list(map(int, input().split()))

dp = nums[:] # ex) dp[3] nums[0] ~ nums[3]의 가장 큰 증가 부분 수열의 합

for i in range(1, n):
    for j in range(i):
        if nums[j] < nums[i]: # nums[i]보다 작을 때만 더함 (증가 부분 수열)
            dp[i] = max(dp[i], dp[j] + nums[i])

print(max(dp))