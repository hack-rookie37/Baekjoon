import sys

n = int(sys.stdin.readline()) # n개의 정점
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][i] and graph[i][k]: # 갈 수 있는지 없는 지만 알면 되기 때문에 j -> i로 i -> k로 갈 수 있는지만 확인
                graph[j][k] = 1             # 거쳐서 갈 수 있다면 값을 1로 변경

for i in graph:
    for j in i:
        print(j, end = ' ')
    print()