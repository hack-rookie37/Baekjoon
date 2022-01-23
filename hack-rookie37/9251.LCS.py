from sys import setrecursionlimit

setrecursionlimit(2000)

"""
def lcs_td(s1, s2, i, j):

    if i < len(s1) and j < len(s2):

        if dp[i][j] != 0:
            return dp[i][j]

        if s1[i] != s2[j]:
            if dp[i][j] == 0:
                dp[i][j] += max(lcs_td(s1, s2, i + 1, j), lcs_td(s1, s2, i, j + 1))
        else:
            dp[i][j] += 1
            dp[i][j] += lcs_td(s1, s2, i + 1, j + 1)
    else:
        return 0

    return dp[i][j]
"""


def lcs_bu(s1, s2, l1, l2):
    cache = [0] * l2

    for i in range(l1):
        cnt = 0

        for j in range(l2):
            if cnt < cache[j]:
                cnt = cache[j]
            elif s1[i] == s2[j]:
                cache[j] = cnt + 1

    return max(cache)


s1 = input()
s2 = input()

print(lcs_bu(s1, s2, len(s1), len(s2)))

# i = j = 0
# dp = [[0] * len(s2) for _ in range(len(s1))]
# lcs = lcs_td(s1, s2, i, j)
