import sys
from collections import deque

input = sys.stdin.readline
dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]

r, c, n = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
second_graph = [['O'] * c for _ in range(r)]
third_graph = [['O'] * c for _ in range(r)]

q = deque()

for y_idx in range(r):
    for x_idx in range(c):
        if graph[y_idx][x_idx] == 'O':
            q.append((y_idx, x_idx))
            second_graph[y_idx][x_idx] = '.'

while q:
    y, x = q.popleft()

    for idx in range(4):
        ny, nx = y + dy[idx], x + dx[idx]

        if not (0 <= ny < r and 0 <= nx < c):
            continue
            
        second_graph[ny][nx] = '.'

for y_idx in range(r):
    for x_idx in range(c):
        if second_graph[y_idx][x_idx] == 'O':
            q.append((y_idx, x_idx))
            third_graph[y_idx][x_idx] = '.'

while q:
    y, x = q.popleft()

    for idx in range(4):
        ny, nx = y + dy[idx], x + dx[idx]

        if not (0 <= ny < r and 0 <= nx < c):
            continue
            
        third_graph[ny][nx] = '.'


for idx in range(r):
    print(''.join(  graph[idx] if n == 1 else 
                    'O' * c if not n % 2 else
                    second_graph[idx] if n % 4 == 3 else
                    third_graph[idx]))
