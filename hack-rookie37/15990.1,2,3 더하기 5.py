import sys

input = sys.stdin.readline
MOD, LEN = int(1e9 + 9), int(1e5 + 1)
dp = [[0] * LEN for _ in range(4)]
dp[1][1] = dp[2][2] = dp[1][3] = dp[2][3] = dp[3][3] = 1


def memo():
    for i in range(4, LEN):
        if i - 1 >= 0:
            dp[1][i] = (dp[2][i - 1] + dp[3][i - 1]) % MOD
        if i - 2 >= 0:
            dp[2][i] = (dp[1][i - 2] + dp[3][i - 2]) % MOD
        if i - 3 >= 0:
            dp[3][i] = (dp[1][i - 3] + dp[2][i - 3]) % MOD


if __name__ == "__main__":

    memo()

    TC = int(input())
    for _ in range(TC):
        N = int(input())
        print((dp[1][N] + dp[2][N] + dp[3][N]) % MOD)
