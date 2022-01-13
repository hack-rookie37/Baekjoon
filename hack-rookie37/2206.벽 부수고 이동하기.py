from collections import deque
from sys import stdin

input = stdin.readline


def bfs():
    queue = deque([[0, 0, 1]])
    visit = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visit[0][0][1] = 1

    while queue:
        # x: row, y: column, w[0]: count_crashed, w[1]: count_no_crashed
        x, y, w = queue.popleft()
        if x == N - 1 and y == M - 1:
            return visit[x][y][w]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] == 1 and w == 1:  # 벽을 만나고 벽을 한번 부술 수 있는 경우
                    visit[nx][ny][0] = visit[x][y][w] + 1
                    queue.append([nx, ny, 0])
                elif matrix[nx][ny] == 0 and visit[nx][ny][w] == 0:  # 벽이 없고 방문한적이 없는 경우
                    visit[nx][ny][w] = visit[x][y][w] + 1
                    queue.append([nx, ny, w])
    return -1


N, M = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(N)]

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

print(bfs())
