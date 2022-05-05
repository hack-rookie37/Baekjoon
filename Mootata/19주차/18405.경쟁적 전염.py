import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우

n, k = map(int, input().split()) # N x N 크기의 시험관, k 종류의 바이러스
test_info = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split()) # S초 뒤에 (X, Y)에 존재하는 바이러스의 종류
visited = [[False for _ in range(n)] for _ in range(n)]
q1, q2 = deque(), deque()

for i in range(n):
    for j in range(n):
        if test_info[i][j] != 0:
            q1.append((test_info[i][j], i, j))

q1 = deque(sorted(q1))

def bfs():
    while q1:
        w, x, y = q1.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny]:
                continue
            
            test_info[nx][ny] = w
            visited[nx][ny] = True
            q2.append((w, nx, ny))

for i in range(s):
    bfs()
    q1 = q2
    q2 = deque()

print(test_info[x - 1][y - 1])