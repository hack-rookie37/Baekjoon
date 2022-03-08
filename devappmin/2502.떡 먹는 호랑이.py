import sys

d, k = map(int, sys.stdin.readline().split())

dp = [(1, 0), (0, 1)]

for idx in range(2, d):
    dp.append((dp[idx - 1][0] + dp[idx - 2][0],
              dp[idx - 1][1] + dp[idx - 2][1]))


def solution():
    i, j = 0, 0
    while True:
        j = 0
        while True:
            if dp[d - 1][0] * i + dp[d - 1][1] * j == k:
                print(i, j, sep='\n')
                return

            if dp[d - 1][0] * i + dp[d - 1][1] * j > k:
                break
            j += 1
        i += 1


solution()

# for i in range(d):
#     for j in range(d):
#         if dp[d - 1][0] * i + dp[d - 1][1] * j == k:
#             print(i, j, sep='\n')
#             return
#         if dp[d - 1][0] * i + dp[d - 1][1] * j > k:
#             break
# 2 26 28 54 82 136 218 354
