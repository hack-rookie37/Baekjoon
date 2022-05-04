import sys

input = sys.stdin.readline
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1] # 오른쪽, 위쪽, 왼쪽, 아래쪽

n = int(input()) # 드래곤 커브의 수
curves = [[0 for _ in range(101)] for _ in range(101)] # 값이 1 이면 드래곤 커브가 지나는 정점
answer = 0

for _ in range(n):
    x, y, d, g = map(int, input().split()) # x, y, 시작방향, 세대
    curves[x][y] = 1 # 시작지점
    curve = [d] # 이동 경로
    
    for _ in range(g): # 세대만큼 반복
        for i in list(reversed(curve)): # 규칙에 따라 이전 세대의 이동방향 뒤에서 부터
            if i != 3:
                curve.append(i + 1)
            else:
                curve.append(0) # 3일땐 0으로
    
    for i in curve: # curve에 따라 x, y값 이동하면서 지나는 정점 체크
        nx, ny = x + dx[i], y + dy[i]
        curves[nx][ny] = 1
        x, y = nx, ny
    

for i in range(100):
    for j in range(100):
        if curves[i][j] + curves[i + 1][j] + curves[i][j + 1] + curves[i + 1][j + 1] == 4: # 사각형의 네 점을 모두 지나갔을 때
            answer += 1

print(answer)