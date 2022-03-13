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

    # 덩어리의 위치 값이 들어있는 큐에서
    # 가장 첫번째 값을 뽑아 다른 큐에 넣음
    if mq:
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
            
            # 일단 해당 위치를 방문했다는 의미에서
            # 재방문을 방지하기 위해 1을 넣음.
            # 이 값은 빙산 matrix를 업데이트할 때
            # 없앨 예정
            visited[ny][nx] = 1
            
            # 검사하면서 얻은 덩어리의 개수를 저장함.
            ntotal += 1

            # 큐에다가 넣을 다음 덩어리의 상하좌우를 검색하여
            # 0의 개수만큼 visited에 값을 추가함.
            for i in range(4):
                nny, nnx = ny + dy[i], nx + dx[i]

                if not(0 <= nny < n and 0 <= nnx < m):
                    continue
                
                if matrix[nny][nnx] != 0:
                    continue

                visited[ny][nx] += 1
    
    # 0개 혹은 1개의 덩어리가 남았을 경우 답은 0
    if total == 0 or total == 1:
        global ans
        ans = 0
        return False
    
    # 검사한 덩어리와 총 덩어리의 개수가
    # 다르면 2개 이상으로 나눠져 있는 의미
    if ntotal != total:
        return False

    mq = deque()
    total = 0

    # matrix하고 큐를 새로 업데이트하는 부분
    for y_idx in range(n):
        for x_idx in range(m):
            # 이미 물인 부분은 넘어감.
            if visited[y_idx][x_idx] == 0:
                continue

            # 만약에 빙산 부분이면 그 빙산에 visited의 값을 빼고
            # 아까 방문확인을 위해 1을 뺐으니까 다시 1을 더함
            matrix[y_idx][x_idx] = max(0, matrix[y_idx][x_idx] - visited[y_idx][x_idx] + 1)

            # 그럼에도 불구하고 빙산이 존재하면
            # 큐에다가 그 값을 삽입하고
            # 전체 빙산의 개수에 1을 더함
            if matrix[y_idx][x_idx] > 0:
                mq.append((y_idx, x_idx))
                total += 1

    # 여기까지 왔다면
    # 덩어리가 0개도 아니고 1개도 아니고
    # 두 개로 나눠진 상황도 아니기 때문에
    # True를 리턴함
    return True


while solution():
    ans += 1

print(ans)