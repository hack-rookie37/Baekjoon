import sys

n = int(input()) # 자연수 n

dp = [0, 1]

for i in range(2, n + 1):
    minval = sys.maxsize
    s = 1
    while(s**2) <= i:
        minval = min(minval, dp[i - (s ** 2)])
        s += 1
    dp.append(minval + 1)
    
print(dp[n])