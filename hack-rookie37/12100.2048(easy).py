import sys, copy

input = sys.stdin.readline

N = int(input())
board = [[*map(int, input().split())] for _ in range(N)]

direct = {0: [0, 1], 1: [N - 1, -1], 2: [0, 1], 3: [N - 1, -1]}


def merge(board, d):

    # up or down
    if d == 0 or d == 1:
        for col in range(N):
            row = direct[d][0]
            x = row + direct[d][1]
            while 0 <= x < N:
                if board[row][col] == 0:
                    while 0 <= x < N:
                        if board[x][col] != 0:
                            board[row][col] = board[x][col]
                            board[x][col] = 0
                            x += direct[d][1]
                            break
                        else:
                            x += direct[d][1]

                if not (0 <= x < N):
                    break

                if board[row][col] == board[x][col]:
                    board[row][col] *= 2
                    board[x][col] = 0
                    row += direct[d][1]
                    x += direct[d][1]
                else:
                    if board[x][col] != 0:
                        row += direct[d][1]
                        if row == x:
                            x += direct[d][1]
                    else:
                        x += direct[d][1]

    # left or right
    elif d == 2 or d == 3:
        for row in range(N):
            col = direct[d][0]
            y = col + direct[d][1]
            while 0 <= y < N:
                if board[row][col] == 0:
                    while 0 <= y < N:
                        if board[row][y] != 0:
                            board[row][col] = board[row][y]
                            board[row][y] = 0
                            y += direct[d][1]
                            break
                        else:
                            y += direct[d][1]

                if not (0 <= y < N):
                    break

                if board[row][col] == board[row][y]:
                    board[row][col] *= 2
                    board[row][y] = 0
                    col += direct[d][1]
                    y += direct[d][1]
                else:
                    if board[row][y] != 0:
                        col += direct[d][1]
                        if col == y:
                            y += direct[d][1]
                    else:
                        y += direct[d][1]


def move(board, n):
    global max_val

    if n >= 5:
        max_val = max(max_val, max(map(max, board)))
        return

    for d in range(4):
        t_board = copy.deepcopy(board)
        merge(t_board, d)
        move(t_board, n + 1)


max_val = 0
move(board, 0)
print(max_val)
