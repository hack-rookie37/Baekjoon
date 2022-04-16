import sys

input = sys.stdin.readline
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 북 동 남 서

n, m = map(int, input().split()) # 세로 n, 가로 m
r, c, dir = map(int, input().split()) # 로봇청소기의 좌표와 바라보는 방향 0 북 1 동 2 남 3 서

place = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
visited[r][c] = True

def clean(r, c, dir):
    count = 1
    while True:
        is_clear = True # 4방향 모두 청소 되었는지 체크
        for _ in range(4):
            dir = (dir + 3) % 4 # 현재 바라보는 방향 기준 왼쪽
            nx, ny = r + dx[dir], c + dy[dir]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny]:
                continue
            
            if place[nx][ny] == 0:
                visited[nx][ny] = True
                count += 1
                r, c = nx, ny
                is_clear = False
                break
            
        if is_clear: # 4방향 모두 청소 되어있다면
            d = (dir + 2) % 4 # 현재 바라보는 방향 기준 뒤쪽
            if place[r + dx[d]][c + dy[d]] == 1: # 벽이면 종료
                return count
            else: # 아니면 한칸 후진
                r, c = r + dx[d], c + dy[d]

print(clean(r, c, dir))