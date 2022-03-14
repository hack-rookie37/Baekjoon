import sys

input = sys.stdin.readline

n, k = map(int, input().split()) # 동전의 종류 N, 가치의 합 K

dp = [10001 for _ in range(10001)]
coins = [int(input()) for _ in range(n)]

def sol1():
    for i in coins:
        if i <= 10000: # 동전의 크기는 100000까지 가능하지만 의미 없으므로 그 이하만 넣음
            dp[i] = 1

    for i in range(1, k + 1):
        for j in range(1, i + 1):
            if i + j > 10000: # 10000이 넘어가는 값은 찾을 필요 없음
                break
            dp[i + j] = min(dp[i + j], dp[i] + dp[j])
            # k = 17, coins = 1, 4, 7, 15
            # dp[14 + 3] = min(dp[14 + 3], dp[14] + dp[3]) -> 2 + 3 = 5
            # dp[15 + 2] = min(dp[14 + 3], dp[15] + dp[2])
            # ㄴ> 이미 dp[17]에는 위의 2 + 3 = 5가 들어있음 하지만
            # dp[15 + 2] -> 1 + 2 = 3 가 더 작으므로, 값을 바꿔줌

    if dp[k] >= 10001:
        return -1
    else:
        return dp[k]

def sol2():
    n, k = map(int, input().split())

    dp = [0] + [10001 for _ in range(k + 1)]
    coins = sorted([int(input()) for _ in range(n)])

    for i in range(1, k + 1):
        for j in coins:
            if i - j < 0:
                break
            dp[i] = min(dp[i], dp[i - j] + 1)

    if dp[k] >= 10001:
        return -1
    else:
        return dp[k]

print(sol1())

# dp[i]는 i원을 만드는데 들어가는 동전의 최소 개수.