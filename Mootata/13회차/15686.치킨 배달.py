import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split()) # N x N 크기의 도시, 치킨집의 최대 개수 m
city = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []
answer = 999999

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

for i in combinations(chicken, m): # 치킨집들중 m개 선택
    temp = 0
    for j in house: # 모든 집으로부터 위에서 선택한 m개의 치킨집까지의 거리를 구함
        dist = 999
        for k in range(m): # m개의 치킨집 중 집 j에 가장 가까운 거리를 찾아냄
            dist = min(dist, abs(j[0] - i[k][0]) + abs(j[1] - i[k][1]))
        temp += dist # 이런식으로 모든 집까지의 가장 가까운 거리를 더하고,
    answer = min(answer, temp) # 그 값이 가장 작은 것이 정답

print(answer)

# 치킨집중에 m개를 선택해서 각 집으로부터 m개의 치킨집까지의 거리가 가장 짧은 것을 
# 모두 temp에 더하고, 치킨집 조합중 가장 작은 temp값을 가진 것이 정답.