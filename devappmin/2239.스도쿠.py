import sys

dy, dx = [1, 1, 1, 0, -1, -1, -1, 0, 0], [1, 0, -1, -1, -1, 0, 1, 1, 0]
SIZE = 9
CENTER = [(1, 1), (1, 4), (1, 7), (4, 1), (4, 4), (4, 7), (7, 1), (7, 4), (7, 7)]

puzzle = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(9)]

empty = [(y, x) for y in range(9) for x in range(9) if not puzzle[y][x]]
empty_length = len(empty)

def get_center(y, x):
    my = y // 3 
    mx = x // 3
    return CENTER[my * 3 + mx]

def promising(puzzle, y, x):
    center_y, center_x = get_center(y, x)
    num_sets = set(x for x in range(1, 10))

    num_sets -= set(puzzle[center_y + dy[v]][center_x + dx[v]] for v in range(9))
    num_sets -= set(puzzle[y][v] for v in range(9))
    num_sets -= set(puzzle[v][x] for v in range(9))

    return num_sets 

def dfs(puzzle, depth):
    if depth == empty_length:
        for row in puzzle:
            print(*[x for x in row], sep="")
        exit(0)

    ey, ex = empty[depth]

    for value in promising(puzzle, ey, ex):
        puzzle[ey][ex] = value
        dfs(puzzle, depth + 1)
        puzzle[ey][ex] = 0

dfs(puzzle, 0)