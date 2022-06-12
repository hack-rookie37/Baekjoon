from collections import deque


def sol(N, K):
    answer = abs(N - K)

    if N >= K:
        print(answer)
        return

    q = deque([(N, 0)])
    nodes = {N}

    while q:
        x, d = q.popleft()

        if x == K:
            print(d)
            return

        if x * 2 not in nodes and x * 2 <= K + 1:
            q.append((x * 2, d))
            nodes.add(x * 2)

        if x - 1 not in nodes and x - 1 > 0:
            q.append((x - 1, d + 1))
            nodes.add(x - 1)

        if x + 1 not in nodes and x + 1 <= K:
            q.append((x + 1, d + 1))
            nodes.add(x + 1)


if __name__ == "__main__":
    sol(*map(int, input().split()))
