from sys import stdin
from itertools import accumulate as acc

input = stdin.readline

N, M = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(N)]
quest = [[*map(int, input().split())] for _ in range(M)]
# matrix = [[0]*N for _ in range(N)]

# 10^6
for i in range(N):
    board[i] = list(acc(board[i]))
for i in range(1, N):
    for j in range(N):
        board[i][j] += board[i - 1][j]

# 10^5
for q in quest:
    x1, y1, x2, y2 = q[0] - 1, q[1] - 1, q[2] - 1, q[3] - 1

    temp = board[x2][y2]
    if x1 > 0:
        temp -= board[x1 - 1][y2]
    if y1 > 0:
        temp -= board[x2][y1 - 1]
    if x1 * y1 > 0:
        temp += board[x1 - 1][y1 - 1]

    print(temp)
