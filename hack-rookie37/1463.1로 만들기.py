from collections import deque
from array import array


def bfs(X):
    queue = deque([1])

    while queue:
        node = queue.popleft()

        for i in (3, 2, 1):
            if i == 1:
                if dp[node + 1] == -1:
                    dp[node + 1] = dp[node] + 1
                    if node + 1 == X:
                        return dp[node] + 1
                    queue.append(node + 1)
            else:
                if node * i <= X:
                    if dp[node * i] == -1:
                        dp[node * i] = dp[node] + 1
                        if node * i == X:
                            return dp[node] + 1
                        queue.append(node * i)


if __name__ == "__main__":
    X = int(input())

    if X == 1:
        print(0)
        exit()

    dp = array("i", [-1] * (X + 1))
    dp[1] = 0

    print(bfs(X))
