import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    coins = [*map(int, input().split())]
    M = int(input())

    dp = [1] + [0] * M

    for i in coins:
        for j in range(i, M + 1):
            if j - i >= 0:
                dp[j] += dp[j - i]

    print(dp[-1])
