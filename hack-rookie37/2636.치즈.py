import sys
from collections import deque

input = sys.stdin.readline
DX, DY = (1, -1, 0, 0), (0, 0, 1, -1)


def bfs(X, Y, cheese):
    q = deque([(0, 0)])

    while q:
        r, c = q.popleft()

        for k in range(4):
            dr = r + DX[k]
            dc = c + DY[k]

            if 0 <= dr < X and 0 <= dc < Y:
                if cheese[dr][dc] == 0:
                    cheese[dr][dc] = 3
                    q.append((dr, dc))


def melt(X, Y, cheese):

    bfs(X, Y, cheese)

    # down
    row = [0] * Y
    for r in range(1, X - 1):
        for c in range(1, Y - 1):
            if cheese[r][c] == 3:
                row[c] = 0

            if cheese[r][c] == 1 and row[c] == 0:
                cheese[r][c] = 8
                row[c] = 1

    # up
    row = [0] * Y
    for r in range(X - 1, 0, -1):
        for c in range(1, Y - 1):
            if cheese[r][c] == 3:
                row[c] = 0

            if cheese[r][c] == 1 and row[c] == 0:
                cheese[r][c] = 8
                row[c] = 1
            elif cheese[r][c] == 8:
                row[c] = 1

    # left
    col = [0] * X
    for c in range(1, Y - 1):
        for r in range(1, X - 1):
            if cheese[r][c] == 3:
                col[r] = 0

            if cheese[r][c] == 1 and col[r] == 0:
                cheese[r][c] = 8
                col[r] = 1
            elif cheese[r][c] == 8:
                col[r] = 1

    # right
    col = [0] * X
    for c in range(Y - 1, 0, -1):
        for r in range(1, X - 1):
            if cheese[r][c] == 3:
                col[r] = 0

            if cheese[r][c] == 1 and col[r] == 0:
                cheese[r][c] = 8
                col[r] = 1
            elif cheese[r][c] == 8:
                col[r] = 1

    for r in range(X):
        for c in range(Y):
            if cheese[r][c] == 8 or cheese[r][c] == 3:
                cheese[r][c] = 0


X, Y = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(X)]

prev = count = 0
while sum(map(sum, cheese)) > 0:
    count += 1
    prev = sum(map(sum, cheese))
    melt(X, Y, cheese)

print(count, prev)
