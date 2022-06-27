import sys

dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]

r, c = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
item = [False] * 100
item[ord(board[0][0])] = True
answer = 0

def dfs(y, x, count):
    global answer
    answer = max(count, answer)

    for idx in range(4):
        ny, nx = y + dy[idx], x + dx[idx]

        if 0 <= ny < r and 0 <= nx < c and not item[ord(board[ny][nx])]:
            item[ord(board[ny][nx])] = True
            dfs(ny, nx, count + 1)
            item[ord(board[ny][nx])] = False

dfs(0, 0, 1)

print(answer)