from collections import deque


def bfs(N, K):

    if N >= K:
        print(N - K)
        print(*range(N, K - 1, -1))
        return

    dist = 0
    visited = {N}
    route = str(N)
    q = deque([(N, dist, route)])

    while q:
        x, dist, route = q.popleft()

        if x == K:
            print(dist)
            print(*route.split())
            return

        if x * 2 <= K + 1 and x * 2 not in visited:
            q.append((x * 2, dist + 1, route + " " + str(x * 2)))
            visited.add(x * 2)

        if x - 1 > 0 and x - 1 not in visited:
            q.append((x - 1, dist + 1, route + " " + str(x - 1)))
            visited.add(x - 1)

        if x + 1 <= K and x + 1 not in visited:
            q.append((x + 1, dist + 1, route + " " + str(x + 1)))
            visited.add(x + 1)


N, K = map(int, input().split())
bfs(N, K)
