import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상 하 좌 우

r, c, n = map(int, input().split()) # r x c 크기의 격자판 n초 뒤의 상태
board = [list(input().strip()) for _ in range(r)] # 맨처음 폭탄 설치
n -= 1

q = deque()

def bfs():
    while q:
        x, y = q.popleft()
        board[x][y] = '.'
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            
            board[nx][ny] = '.'

while n:
    for i in range(r): # 남아있는 설치된 폭탄을 찾음
        for j in range(c):
            if board[i][j] == 'O':
                q.append((i, j))
    
    for i in range(r): # 비어있는 곳을 폭탄으로 채움
        for j in range(c):
            if board[i][j] == '.':
                board[i][j] = 'O'
    
    n -= 1
    if n == 0:
        break
    
    bfs() # 폭탄이 터짐 
    
    n -= 1

for i in range(r):
    print(*board[i], sep='')