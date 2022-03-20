import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우

r, c = map(int, input().split()) # 세로 길이 r, 가로 길이 c
lake = [list(input().rstrip()) for _ in range(r)]
w_visited = [[False for _ in range(c)] for _ in range(r)] # 물 방문 체크
s_visited = [[False for _ in range(c)] for _ in range(r)] # 백조 방문 체크
swans = [] # 백조 두 마리의 위치
iq1, iq2 = deque(), deque()
sq1, sq2 = deque(), deque()
day = 0

for x in range(r):
    for y in range(c):
        if lake[x][y] == 'L': 
            swans.append((x, y))
            lake[x][y] = '.'
            iq1.append((x, y)) # 백조가 있는 위치도 물이므로 iq1에 넣고, 방문 처리함
            w_visited[x][y] = True
        elif lake[x][y] == '.':
            iq1.append((x, y))
            w_visited[x][y] = True

sq1.append(swans[0]) # 백조 한 마리는 탐색 시작 위치로 쓰고, 나머지 한 마리는 도착지임

def melting(): # 얼음이 녹는 BFS
    while iq1:
        x, y = iq1.popleft()
        lake[x][y] = '.' # 
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= r or ny >= c or w_visited[nx][ny]:
                continue
            
            if lake[nx][ny] == '.': # 이번 탐색에서 갈 수 있는 위치(물)는 iq1에 넣고, 얼음이 얼어있어 가지 못하는 곳
                iq1.append((nx, ny))
            elif lake[nx][ny] == 'X': # 즉 다음 탐색에서 얼음이 녹아 물이 되는 위치는 iq2에 넣음
                iq2.append((nx, ny))
            
            w_visited[nx][ny] = True

def bfs(): # 백조의 길 탐색 BFS
    while sq1:
        x, y = sq1.popleft()
        if (x, y) == swans[1]: # 두 번째 백조에 도달하면 종료
            return True
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= r or ny >= c or s_visited[nx][ny]:
                continue
            
            if lake[nx][ny] == '.': # 이번 탐색에서 갈 수 있는 위치는 sq1에 넣어서 모두 탐색하고,
                sq1.append((nx, ny))
            elif lake[nx][ny] == 'X': # 얼음을 만난다면, 얼음의 위치는 다음 탐색의 시작점이므로, sq2에 넣음
                sq2.append((nx, ny))
            
            s_visited[nx][ny] = True

while True:
    melting()
    
    if bfs():
        print(day)
        break
    
    iq1 = iq2 # iq1과 sq1에 iq2, sq2에 담아 두었던 다음 시작 위치를 옮겨줌
    sq1 = sq2
    iq2, sq2 = deque(), deque() # iq2, sq2는 초기화해서 다시 다음 시작 위치를 담을 때 사용
    day += 1




# 얼음이 녹아 백조들이 서로 만날 수 있는 길이 생기는데 걸리는 날을 구하는 문제.

# 얼음이 한 번 녹을 때, 녹은 뒤에 다음 얼음이 나오는 지점까지 탐색한 후, 해당 얼음들의 위치는 iq2에 담아서 다음 탐색의 시작점으로 사용함.
# 백조의 탐색도 마찬가지로, 일단 갈 수 있는 위치까지 탐색하고, 얼음의 위치를 sq2에 담아서 다음 탐색의 시작점으로 사용함.
