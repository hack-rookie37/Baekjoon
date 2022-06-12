from collections import deque
import sys

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우

def bfs(px, py):
    q = deque()
    q.append((px, py))
    visited = [[-1 for _ in range(w + 2)] for _ in range(h + 2)]
    visited[px][py] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= h + 2 or ny >= w + 2 or visited[nx][ny] != -1 or cell[nx][ny] == '*':
                continue
            
            if cell[nx][ny] == '.':
                visited[nx][ny] = visited[x][y]
                q.appendleft((nx, ny))
            elif cell[nx][ny] == '#':
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    return visited

for t in range(int(input())):
    h, w = map(int, input().split()) # 평면도의 높이 h, 너비 w
    p_list = []
    answer = float('inf')
    
    cell = [list('.' * (w + 2))] # 평면도 테두리 +1
    for _ in range(h):
        cell.append(list('.' + input().strip() +'.'))
    cell.append(list('.' * (w + 2)))
    
    for i in range(h + 2):
        for j in range(w + 2):
            if cell[i][j] == '$':
                cell[i][j] = '.'
                p_list.append((i, j))
    
    p1, p2, s = bfs(p_list[0][0], p_list[0][1]), bfs(p_list[1][0], p_list[1][1]), bfs(0, 0)
    
    for i in range(h + 2):
        for j in range(w + 2):
            if p1[i][j] != -1 and p2[i][j] != -1 and s[i][j] != -1:
                if cell[i][j]=='*': # -1이라 빼줘야 함
                    continue
                k = p1[i][j] + p2[i][j] + s[i][j]
                if cell[i][j] == '#':
                    k -= 2
                answer = min(k,answer)
    print(answer)