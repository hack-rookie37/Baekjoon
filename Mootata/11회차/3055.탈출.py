import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우

r, c = map(int, input().split()) # r행 c열
forest = [list(input().rstrip()) for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]
q = deque()

for i in range(r): # 고슴도치, 물의 위치 큐에 넣어주고, 비버 굴의 위치 파악
    for j in range(c):
        if forest[i][j] == 'S':
            q.appendleft((i, j))
        elif forest[i][j] == '*':
            q.append((i, j))
        elif forest[i][j] == 'D':
            cave_x = i
            cave_y = j

def bfs(cave_x, cave_y):
    while q:
        x, y = q.popleft()
        
        if forest[cave_x][cave_y] == 'S': # 고슴도치가 비버굴에 도착하면 종료
            return visited[cave_x][cave_y]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0:
                continue
            elif nx >= r or ny >= c:
                continue
            
            if (forest[nx][ny] == '.' or forest[nx][ny] =='D') and forest[x][y] == 'S': # 다음 이동할 곳이 비버 굴이거나 비어있는 곳이면 이동함
                forest[nx][ny] = 'S'
                visited[nx][ny] = visited[x][y] + 1 # 고슴도치가 이동하는데 걸리는 시간 체크
                q.append((nx, ny))
            elif (forest[nx][ny] == '.' or forest[nx][ny] =='S') and forest[x][y] == '*':
                forest[nx][ny] = '*'
                q.append((nx, ny))
            
    return 'KAKTUS' # bfs 탐색이 끝나도 도착하지 못했다면 'KAKTUS' 출력

print(bfs(cave_x, cave_y))