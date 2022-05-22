n, m = map(int, input().split()) # 표의 크기 N, 합을 구해야 하는 횟수 M
table = [list(map(int, input().split())) for _ in range(n)]
coordinates = [list(map(int, input().split())) for _ in range(m)]

for j in range(n):
    for i in range(n):
        if i != 0:
            table[i][j] += table[i - 1][j]

for x1, y1, x2, y2 in coordinates:
    answer = 0
    for i in range(y1 - 1, y2):
        if x1 != 1:
            answer -= table[x1 - 2][i] # x1 ~ x2 까지의 합을 구하려면 dp[x2]에서 dp[x1 - 1]의 값을 뺴야함
        answer += table[x2 - 1][i]
    
    print(answer)

# 구간합 구하는 방법을 이용해서 각 행의 열에 해당 열까지의 합들을 넣음
# ex) table(2, 1)에는 (0, 1), (1, 1), (2, 1) 의 합이 들어있음
# 이후에 원하는 구간의 값을 구함