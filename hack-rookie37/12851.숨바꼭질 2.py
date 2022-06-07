from collections import deque


def sol(N, K):
    if K <= N:
        print(N - K)
        print(1)
        return

    dist = 0
    q = deque([(N, dist)])
    visited = {N: dist}

    while q:
        x, dist = q.popleft()

        if x == K:
            print(dist)
            print(len([x for x in q if x[0] == K]) + 1)
            return

        if x * 2 <= K + 1:
            if visited.get(x * 2, dist + 1) >= dist + 1:
                q.append((x * 2, dist + 1))
                visited[x * 2] = dist + 1
        if x + 1 <= K:
            if visited.get(x + 1, dist + 1) >= dist + 1:
                q.append((x + 1, dist + 1))
                visited[x + 1] = dist + 1
        if x - 1 > 0:
            if visited.get(x - 1, dist + 1) >= dist + 1:
                q.append((x - 1, dist + 1))
                visited[x - 1] = dist + 1


sol(*map(int, input().split()))
