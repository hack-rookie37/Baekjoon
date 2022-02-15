import sys

input = sys.stdin.readline

n = int(input()) # 집의 수 n
costs = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    costs[i][0] = min(costs[i - 1][1], costs[i - 1][2]) + costs[i][0] # 이전 집들을 칠하는데 들어간 비용이 작은 것과, 현재 집 i를 빨강으로 칠하는 비용을 더함
    costs[i][1] = min(costs[i - 1][0], costs[i - 1][2]) + costs[i][1] # 이전 집들을 칠하는데 들어간 비용이 작은 것과, 현재 집 i를 초록으로 칠하는 비용을 더함
    costs[i][2] = min(costs[i - 1][0], costs[i - 1][1]) + costs[i][2] # 이전 집들을 칠하는데 들어간 비용이 작은 것과, 현재 집 i를 파랑으로 칠하는 비용을 더함

print(min(costs[n - 1]))