n, m, r = map(int, input().split()) # 지역의 개수 n, 수색범위 m, 길의 개수 r
items = list(map(int, input().split()))
graph = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
answer = 0

for _ in range(r):
    v1, v2, weight = map(int, input().split())
    graph[v1][v2] = weight
    graph[v2][v1] = weight

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1): # j에서 k로 바로 가는 것과 j에서 i를 거쳐 k를 가는 것중 더 가까운 것을 선택
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])
            if j == k: # 자기 자신으로 향하는 것은 0
                graph[j][k] = 0

for i in range(1, n + 1):
    temp = 0
    for j in range(1, n + 1):
        if graph[i][j] <= m: # 수색범위(가중치)가 m보다 작거나 같으면 가능
            temp += items[j - 1]
    answer = max(answer, temp)

print(answer)

# 11 ~ 16 각 노드로부터 다른 모든 노드까지의 거리를 계산하여 graph 리스트에 저장
# 18 ~ 23 구해진 거리를 이용하여 m보다 작거나 같은 가중치를 가진 노드에 해당하는 item 값을 모두 더하여 정답 찾기