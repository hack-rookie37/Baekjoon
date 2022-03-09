import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())

dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]

w_matrix = []
s_matrix = []
wq = deque()
sq = deque()

for idx in range(r):
    row = list(input().rstrip())

    if '*' in row:
        wq.append((idx, row.index('*')))
        w_matrix.append([*row])
        w_matrix[-1][row.index('*')] = 0
    else:
        w_matrix.append([*row])
    
    if 'S' in row:
        sq.append((idx, row.index('S')))
        s_matrix.append([*row])
        s_matrix[-1][row.index('S')] = 0
    else:
        s_matrix.append([*row])

while wq:
    y, x = wq.popleft()

    for idx in range(4):
        ny, nx = y + dy[idx], x + dx[idx]

        if not (0 <= ny < r and 0 <= nx < c):
            continue

        if w_matrix[ny][nx] == 'X' or w_matrix[ny][nx] == 'D':
            continue

        if type(w_matrix[ny][nx]) == int:
            continue

        w_matrix[ny][nx] = w_matrix[y][x] + 1
        wq.append((ny, nx))
    

while sq:
    y, x = sq.popleft()

    for idx in range(4):
        ny, nx = y + dy[idx], x + dx[idx]

        if not (0 <= ny < r and 0 <= nx < c):
            continue

        if s_matrix[ny][nx] == 'X':
            continue

        if type(s_matrix[ny][nx]) == int:
            continue
        
        if type(w_matrix[ny][nx]) == int and s_matrix[y][x] + 1 >= w_matrix[ny][nx]:
            continue

        if s_matrix[ny][nx] == 'D':
            print(s_matrix[y][x] + 1)
            exit(0)

        s_matrix[ny][nx] = s_matrix[y][x] + 1
        sq.append((ny, nx))

print("KAKTUS")

# print(w_matrix)
# print(s_matrix)