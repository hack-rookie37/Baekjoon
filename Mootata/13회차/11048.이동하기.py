import sys

input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        elif i == 0: # i가 0일 때는 대각선 위쪽과 바로 위쪽은 범위를 벗어나므로, 왼쪽 값만 더함
            maze[i][j] += maze[i][j - 1]
        elif j == 0: # j가 0일 때는 대각선 위쪽과 왼쪽은 범위를 벗어나므로, 위쪽 값만 더함
            maze[i][j] += maze[i - 1][j]
        else: # 위의 경우가 아니라면, 왼쪽, 대각선, 위쪽의 값들 중 더 큰 값을 더함
            maze[i][j] += max(maze[i - 1][j], maze[i][j - 1], maze[i - 1][j - 1])

print(maze[-1][-1])