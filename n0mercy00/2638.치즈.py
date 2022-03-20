import sys
from collections import deque
dy = [-1, 1, 0, 0]
dx = [0,0,-1,1]
n, m = map(int, sys.stdin.readline().split())
visited = [[False]*m for _ in range(n)] #이거 왜 이리 적는지 모르겠음
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 0

# 바깥 공기를 -1로 초기화
def outSide():
    dq = deque()
    out_visited = [[False]*m for _ in range(n)] #역시나 이부분 문법을 모르겠음 / #방문한곳 다 false
    dq.append((0,0))
    out_visited[0][0] = True
    board[0][0] = -1
    #00에서 시작이고 대충 방문했고 외부공기라는 시발점
   
   #이제 반복 큐들어오는것(치즈만난애들 )
    while dq:
        y, x= dq.popleft()        #문법 이해안됨 변수두개한번에 터트리는건가?
        
        #상하좌우 무빙
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            #경계선이거나 이미 크문한곳이거나 치즈면 다음으로 ㄱㄱ
            if 0 > ny or ny >=n or 0 > nx or nx>= m: continue
            if board[ny][nx] == 1 or out_visited[ny][nx]: continue 
            
            #경계도 방문한곳도 치즈도 아니면 외부공기 체크
            dq.append((ny,nx))
            board[ny][nx] = -1
            out_visited[ny][nx] = True
    return

# 치즈가 다 녹았는지 확인
def isMelt():
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                return False
    return True

while not isMelt(): # 치즈가 다 녹을 때 까지 반복    
    outSide()   # 바깥 공기를 -1로 초기화
    check = []  # 바깥 공기와 맞닿은 칸을 저장
    # 외부 공기와 접촉한 치즈 녹음
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                cnt = 0 # 바깥 공기와 맞닿은 칸의 개수
                for k in range(4):
                    ny = dy[k] + i
                    nx = dx[k] + j
                    if 0 > ny or ny >=n or 0 > nx or nx>= m: continue
                    if board[ny][nx] == -1: 
                        cnt += 1
                if cnt >= 2: # 2칸 이상 맞닿아야지 녹을 수 있음
                    check.append([i, j])    
    for y, x in check: # 바깥 공기와 맞닿은 칸은 녹음
        #print(y, x)
        board[y][x] = 0    
    answer += 1 


print(answer)