import sys

n = int(input()) # 자연수 n

dp = [0, 1]

for i in range(2, n + 1):
    minval = sys.maxsize
    s = 1
    while(s**2) <= i:
        minval = min(minval, dp[i - (s ** 2)]) # 9같은 경우에는 dp[8]의 값에 1을 더해주는 것보다 3의 제곱으로 나타내는 것이
        s += 1                                 # 더 적은 제곱수를 사용하는 것이기 때문에 이런 경우를 방지하기 위해서 확인해줌
    dp.append(minval + 1)                      # dp[i - (s ** 2)] 의 경우의 수에 dp[(s ** 2)]의 경우의 수를 더하면 됨.
                                               # 어차피 제곱수의 경우의 수는 1이기 때문에 dp에 append 할때 +1을 해주면 끝
print(dp[n])