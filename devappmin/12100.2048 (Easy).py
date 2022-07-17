import sys
from collections import defaultdict, deque

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

def graph_max(graph):
    return max(map(max, graph))

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = defaultdict(int)
visited[str(graph)] = 1
answer = graph_max(graph)


# 0R 2D 3L 4U    
def move(graph, pos):
    new_graph = [row[:] for row in graph]


    if pos == 0:
        for y in range(n):
            top = n - 1
            for x in range(n - 2, -1, -1):
                if not new_graph[y][x]:
                    continue

                temp = new_graph[y][x]
                new_graph[y][x] = 0

                if new_graph[y][top] == 0:
                    new_graph[y][top] = temp
                    continue

                if new_graph[y][top] == temp:
                    new_graph[y][top] = temp * 2
                    top -= 1
                    continue

                top -= 1
                new_graph[y][top] = temp


    if pos == 2:
        for y in range(n):
            top = 0
            for x in range(1, n):
                if not new_graph[y][x]:
                    continue
                
                temp = new_graph[y][x]
                new_graph[y][x] = 0

                if new_graph[y][top] == 0:
                    new_graph[y][top] = temp
                    continue

                if new_graph[y][top] == temp:
                    new_graph[y][top] = temp * 2
                    top += 1
                    continue

                top += 1
                new_graph[y][top] = temp


    if pos == 1:
        for x in range(n):
            top = n - 1
            for y in range(n - 2, -1, -1):
                if not new_graph[y][x]:
                    continue

                temp = new_graph[y][x]
                new_graph[y][x] = 0

                if new_graph[top][x] == 0:
                    new_graph[top][x] = temp
                    continue

                if new_graph[top][x] == temp:
                    new_graph[top][x] = temp * 2
                    top -= 1
                    continue

                top -= 1
                new_graph[top][x] = temp

    if pos == 3:
        for x in range(n):
            top = 0
            for y in range(1, n):
                if not new_graph[y][x]:
                    continue

                temp = new_graph[y][x]
                new_graph[y][x] = 0

                if new_graph[top][x] == 0:
                    new_graph[top][x] = temp
                    continue

                if new_graph[top][x] == temp:
                    new_graph[top][x] = temp * 2
                    top += 1
                    continue

                top += 1
                new_graph[top][x] = temp

    return new_graph


q = deque([graph])

while q:
    graph = q.popleft()

    if visited[str(graph)] > 5:
        break

    for idx in range(4):
        new_graph = move(graph, idx)
        if visited[str(new_graph)]:
            continue

        visited[str(new_graph)] = visited[str(graph)] + 1
        answer = max(answer, graph_max(new_graph))
        q.append(new_graph)

print(answer)

    # if pos == 0:
    #     for y in range(n):
    #         for x in range(n - 2, -1, -1):
    #             if not new_graph[y][x]:
    #                 continue

    #             temp = x
    #             while temp < n - 1 and not new_graph[y][temp + 1]:
    #                 new_graph[y][temp + 1] = new_graph[y][temp]
    #                 new_graph[y][temp] = 0
    #                 temp += 1
                
    #             if temp != n - 1 and new_graph[y][temp + 1] == new_graph[y][temp] and (y, temp + 1) not in store:
    #                 new_graph[y][temp + 1] *= 2
    #                 new_graph[y][temp] = 0
    #                 store.append((y, temp + 1))