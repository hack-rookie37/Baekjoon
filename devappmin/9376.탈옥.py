# 0 - 1 BFS를 통해서 문제를 해결해야함.
import sys
from collections import deque

dy, dx = (1, -1, 0, 0), (0, 0, 1, -1)

def bfs(h, w, graph, y, x):
    visited = [[-1] * (w + 2) for _ in range(h + 2)]
    q = deque([(y, x)])
    visited[y][x] = 0;

    while q:
        y, x = q.popleft()

        for idx in range(4):
            ny, nx = y + dy[idx], x + dx[idx]

            if not (0 <= ny < h + 2 and 0 <= nx < w + 2):
                continue

            if visited[ny][nx] != -1:
                continue

            # 빈 공간일 때는 가중치를 더하지 않고 앞으로 나아간다.
            # 이 때 q에다가 값을 넣을 때는 왼쪽에다가 넣어줘야한다.
            if graph[ny][nx] == '.' or graph[ny][nx] == '$':
                visited[ny][nx] = visited[y][x]
                q.appendleft((ny, nx))
                continue

            # 문을 뚫는 것은 가중치를 더하는 것이다.
            # 이 때는 가중치를 더해서 넣는데 뒷 쪽에다가 넣어준다.
            if graph[ny][nx] == '#':
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))
    
    return visited


def solution():
    h, w = map(int, sys.stdin.readline().split())
    graph = [list('.' * (w + 2))]
    graph.extend([list('.' + sys.stdin.readline().rstrip() + '.') for _ in range(h)])
    graph.append(list('.' * (w + 2)))

    jailbreaker = []

    for y in range(h + 2):
        for x in range(w + 2):
            if graph[y][x] == '$':
                jailbreaker.append((y, x))

    # 첫번째 탈옥, 두번째 탈옥, 상민이 이렇게 3번 돌려야한다.
    first = bfs(h, w, graph, *jailbreaker[0])
    second = bfs(h, w, graph, *jailbreaker[1])
    sangmin = bfs(h, w, graph, 0, 0)
    answer = float('inf')

    for i in range(h + 2):
        for j in range(w + 2):
            if first[i][j] == -1 or second[i][j] == -1 or sangmin[i][j] == -1:
                continue

            if graph[i][j] == '*':
                continue

            result = first[i][j] + second[i][j] + sangmin[i][j] - (2 if graph[i][j] == '#' else 0)

            answer = min(answer, result)

    print(answer)

test_cases = int(sys.stdin.readline())
for _ in range(test_cases): solution()