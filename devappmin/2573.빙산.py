import sys
from collections import deque
input = sys.stdin.readline

dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]

n, m = map(int, input().split())

matrix = []
mq = deque()
ans = 0
total = 0

for y_idx in range(n):
    row = list(map(int, input().split()))

    for x_idx in range(m):
        if row[x_idx] != 0:
            mq.append((y_idx, x_idx))
            total += 1
    

    matrix.append(row)


def solution():
    global total
    global mq
    visited = [[0] * m for _ in range(n)]
    ntotal = 0
    qq = deque()

    if mq:
        # ntotal +=1
        qq.append(mq.popleft())

    while qq:

        y, x = qq.popleft()

        for idx in range(4):
            ny, nx = y + dy[idx], x + dx[idx]


            if not (0 <= ny < n and 0 <= nx < m):
                continue

            if matrix[ny][nx] == 0:
                continue

            if visited[ny][nx] != 0:
                continue

            qq.append((ny, nx))
            visited[ny][nx] = 1
            ntotal += 1
            for i in range(4):
                nny, nnx = ny + dy[i], nx + dx[i]

                if not(0 <= nny < n and 0 <= nnx < m):
                    continue
                
                if matrix[nny][nnx] != 0:
                    continue

                visited[ny][nx] += 1
    
    
    if total == 0 or total == 1:
        global ans
        ans = 0
        return False

    if ntotal != total:
        return False

    mq = deque()
    total = 0

    for y_idx in range(n):
        for x_idx in range(m):
            if visited[y_idx][x_idx] == 0:
                continue

            matrix[y_idx][x_idx] = max(0, matrix[y_idx][x_idx] - visited[y_idx][x_idx] + 1)

            if matrix[y_idx][x_idx] > 0:
                mq.append((y_idx, x_idx))
                total += 1

    return True



while solution():
    ans += 1

print(ans)