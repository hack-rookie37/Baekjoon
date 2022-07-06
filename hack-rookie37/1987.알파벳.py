import sys

input = sys.stdin.readline

DXY = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(board, R, C):
    search = set([(0, 0, board[0][0])])
    answer = 1

    while search:
        x, y, route = search.pop()
        answer = max(answer, len(route))
        if answer >= 26:
            return answer

        for m, n in DXY:
            dx, dy = x + m, y + n
            if 0 <= dx < R and 0 <= dy < C:
                if not board[dx][dy] in route:
                    search.add((dx, dy, route + board[dx][dy]))
    return answer


R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
print(dfs(board, R, C))
