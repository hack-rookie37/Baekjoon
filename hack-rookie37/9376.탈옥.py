import sys
from collections import deque

input = sys.stdin.readline
D = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def bfs(x, y):
    q = deque([(x, y)])
    cnt = [[-1] * (c + 2) for _ in range(r + 2)]
    cnt[x][y] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in D:
            tx = x + dx
            ty = y + dy
            if 0 <= tx < r + 2 and 0 <= ty < c + 2:
                if cnt[tx][ty] == -1:
                    if jail[tx][ty] == ".":
                        q.appendleft((tx, ty))
                        cnt[tx][ty] = cnt[x][y]
                    elif jail[tx][ty] == "#":
                        q.append((tx, ty))
                        cnt[tx][ty] = cnt[x][y] + 1
    return cnt


if __name__ == "__main__":
    TC = int(input().strip())

    for _ in range(TC):
        r, c = map(int, input().split())
        jail = (
            [["."] * (c + 2)]
            + [list("." + input().strip() + ".") for _ in range(r)]
            + [["."] * (c + 2)]
        )
        psnr = []
        for i in range(1, r + 1):
            for j in range(1, c + 1):
                if jail[i][j] == "$":
                    psnr.append((i, j))
                    jail[i][j] = "."

        cnt = bfs(*psnr[0]), bfs(*psnr[1]), bfs(0, 0)
        ans = float("inf")
        for j, p, q, r in zip(jail, *cnt):
            for i in range(c + 2):
                if p[i] != -1 and q[i] != -1 and r[i] != -1:
                    if j[i] == ".":
                        ans = min(ans, p[i] + q[i] + r[i])
                    elif j[i] == "#":
                        ans = min(ans, p[i] + q[i] + r[i] - 2)
        print(ans)
