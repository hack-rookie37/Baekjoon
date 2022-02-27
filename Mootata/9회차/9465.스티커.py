import sys

input = sys.stdin.readline

for t in range(int(input())):
    n = int(input()) # 2n개의 스티커
    dp = [list(map(int, input().split())) for _ in range(2)]
    
    for i in range(1, n):
        if i == 1:
            dp[0][i] += dp[1][i - 1]
            dp[1][i] += dp[0][i - 1]
        else:
            dp[0][i] += max(dp[1][i - 1], dp[1][i - 2])
            dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])
    
    print(max(dp[0][n - 1], dp[1][n - 1]))

#    0  1  2   3  4
#  -----------------
# 0| 50 10 100 20 40
# 1| 30 50 70  10 60
# 이 스티커를 기준으로
# 예를 들어 dp[0][4]의 최대값을 구할 때 어차피 dp[0][3]의 값은 바로 옆이어서 선택할 수 없고,
# dp[1][3]을 선택하거나 dp[1][2]을 선택하는 두가지 경우를 비교해야함
# dp[1][2]과 dp[1][3] + dp[0][2]를 비교하는게 아닌 dp[1][3]와 비교하는 이유는
# 이미 dp[1][3]에 그것을 고려한 최대값이 들어가 있기 때문임