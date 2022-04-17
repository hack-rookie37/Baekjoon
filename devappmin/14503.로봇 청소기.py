import sys

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
suck = [[0] * m for _ in range(n)]
cnt = 0

while True:
    if graph[r][c] == 0 and not suck[r][c]:
        suck[r][c] = 1

    d = (d + 3) % 4
    
    if  graph[r + dy[d]][c + dx[d]] == 0 and \
        suck[r + dy[d]][c + dx[d]] == False:
        r, c = r + dy[d], c + dx[d]
        cnt = 0
    else:
        cnt += 1
    
    if cnt == 4:
        if graph[r - dy[d]][c - dx[d]] == 1:
            break
        else:
            r, c = r - dy[d], c - dx[d]
            cnt = 0

print(sum(map(sum, suck)))