# n보다 작거나 같은 제곱수를 찾고 n제곱수를 인덱스로 가진 값에 1을 더해주면 된다.

import sys

n = int(sys.stdin.readline())
dp = [0, 1]

for i in range(2, n + 1):
    val = 1e9
    j = 1

    while(j ** 2) <= i:
        val = min(val, dp[i - j ** 2])
        j+=1
    
    dp.append(val + 1)

print(dp[n])