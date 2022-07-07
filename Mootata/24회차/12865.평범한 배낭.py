n, k = map(int, input().split()) # 물품의 수 N, 버틸 수 있는 무게 K
items = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[0 for i in range(k + 1)] for _ in range(n + 1)]

for i in range(1, n + 1): # 가방에 담을 수 있는 물건의 개수
    weight, value = items[i - 1][0], items[i - 1][1]
    for j in range(1, k + 1): # 가방에 담을 수 있는 무게
        if j < weight: # 무거워서 못 넣음
            dp[i][j] = dp[i - 1][j] # 이전에 물건을 넣었을 때의 최대값을 넣음
        else: # 넣을 수 있을 때
            dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j]) # 물건을 담을 때와 담지 않을 때를 비교 

print(dp[n][k])

# value + dp[i - 1][j - weight]는 이전 물건을 넣을 때 현재 물건을 넣고 남는 무게인 j - weight일 때의
# 최대 가치가 담긴 dp[i - 1][j - weight]의 값에 현재 물건의 가치를 넣은 값임.
# 이것과 현재 물건을 담지 않고 이전 물건을 담았을 때의 최대값인 dp[i -1][j]와 비교해
# 더 큰 값을 넣어줌.