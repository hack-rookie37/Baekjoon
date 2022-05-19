from collections import deque


def sol(count):
    queue = deque([])

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and matrix[i][j] != 0:
                queue.append([i, j])
                visited[i][j] = True
                count -= 1

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]:
                    if matrix[nx][ny] != 0:
                        if matrix[x][y] < matrix[nx][ny]:
                            matrix[nx][ny] = matrix[x][y]
                    else:
                        matrix[nx][ny] = matrix[x][y]
    return count


if __name__ == "__main__":

    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    S = tuple(map(int, input().split()))
    count = N * N

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for _ in range(S[0]):
        if count < 1:
            break
        count = sol(count)

    print(matrix[S[1] - 1][S[2] - 1])
