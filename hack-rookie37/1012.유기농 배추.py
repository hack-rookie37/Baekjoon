from sys import stdin
from collections import deque

input = stdin.readline


def bfs(r, c):
    dr = (1, -1, 0, 0)
    dc = (0, 0, 1, -1)

    queue = deque([(r, c)])

    while queue:
        r, c = queue.popleft()
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if 0 <= nc < M and 0 <= nr < N:
                if matrix[nr][nc] == 1:
                    matrix[nr][nc] = 0
                    queue.append((nr, nc))

    return 1


if __name__ == "__main__":

    tc = int(input())
    q = []
    answer = []

    # M: column, N: row
    for case in range(tc):
        M, N, K = map(int, input().split())

        # (column, row)
        q.append([list(map(int, input().split())) for _ in range(K)])
        matrix = [[0] * M for _ in range(N)]

        for c, r in q[case]:
            matrix[r][c] = 1

        count = 0

        for c, r in q[case]:
            if matrix[r][c] == 1:
                count += bfs(r, c)

        answer.append(count)

    print(*answer, sep="\n")
