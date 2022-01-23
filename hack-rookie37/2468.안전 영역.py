import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(x, y, rain):
    visited[x][y] = rain
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if matrix[nx][ny] > rain and visited[nx][ny] < rain:
                dfs(nx, ny, rain)


def bfs(x, y, rain):
    queue = deque([(x, y)])
    visited[x][y] = rain
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] > rain and visited[nx][ny] < rain:
                    queue.append((nx, ny))
                    visited[nx][ny] = rain


def sol():
    answer = 1
    rain = 1

    while True:
        flood = 0
        for i in range(N):
            for j in range(N):
                if matrix[i][j] > rain and visited[i][j] < rain:
                    # dfs(i, j, rain)
                    bfs(i, j, rain)
                    flood += 1

        if flood == 0:
            return answer

        rain += 1

        if flood > answer:
            answer = flood


if __name__ == "__main__":
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    print(sol())
