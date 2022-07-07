import sys

input = sys.stdin.readline


def sol():

    if n < 3:
        print(sum(wine))
        return

    dp[0] = wine[0]
    dp[1] = wine[1] + wine[0]
    dp[2] = max(wine[2] + wine[0], wine[2] + wine[1], dp[1])

    for i in range(3, n):
        dp[i] = max(wine[i] + dp[i - 2], wine[i] + wine[i - 1] + dp[i - 3], dp[i - 1])

    print(dp[n - 1])


n = int(input())
(*wine,) = (int(input()) for _ in range(n))
dp = [0] * n

sol()
