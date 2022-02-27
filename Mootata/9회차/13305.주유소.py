import sys

input = sys.stdin.readline

n = int(input()) # 도시의 수 n
distances = list(map(int, input().split())) # 인접한 두 도시의 도로의 길이
costs = list(map(int, input().split())) # 각 도시의 리터당 가격

answer = 0
index = 0
cheapest = float('inf')

for cost in costs[:-1]: # 마지막 도시의 가격은 볼 필요 없음
    if cost < cheapest:
        cheapest = cost
    answer += cheapest * distances[index]
    index += 1

print(answer)

# 도착지에 도달할 때까지 현재 도시보다 리터당 가격이 낮은 도시까지 갈 만큼씩만 주유함. 
# 리터당 가격을 지금까지 거쳐온 도시 중 가장 싼 가격으로 계속 갱신해줌
# 다음 도시의 가격을 봤을 때 현재 최저가(cheapest)보다 낮은 가격이라면 cheapest를 갱신해주고,
# 아니라면 현재의 최저가로 다음 도시까지 갈만큼 주유함