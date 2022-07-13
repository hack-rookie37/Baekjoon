import sys, time

input = sys.stdin.readline
DXY = [(1, 0), (-1, 0), (0, 1), (0, -1)]
direct = {
    1: [(0,), (1,), (2,), (3,)],
    2: [(0, 1), (2, 3)],
    3: [(0, 2), (0, 3), (1, 2), (1, 3)],
    4: [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)],
    5: [(0, 1, 2, 3)],
}


def observe(x, y, cam):
    ret = []
    for d in direct[cam]:
        temp = set()
        for k in d:
            nx, ny = x, y
            while True:
                nx, ny = nx + DXY[k][0], ny + DXY[k][1]
                if 0 <= nx < N and 0 <= ny < M:
                    if office[nx][ny] == 0:
                        temp.add((nx, ny))
                    elif office[nx][ny] == 6:
                        break
                else:
                    break
        ret.append(temp)
    return ret


def dfs(n, observed):
    global max_cnt
    if n == len(cctv):
        max_cnt = max(max_cnt, len(observed))
        return
    for cctv_case in cctv[n]:
        dfs(n + 1, observed | cctv_case)


if __name__ == "__main__":
    N, M = map(int, input().split())
    office = [list(map(int, input().split())) for _ in range(N)]

    tot_cnt = max_cnt = 0
    cctv = []
    for n in range(N):
        for m in range(M):
            if office[n][m] == 0:
                tot_cnt += 1

            elif office[n][m] != 6:
                cctv.append(observe(n, m, office[n][m]))

    dfs(0, set())
    print(tot_cnt - max_cnt)
