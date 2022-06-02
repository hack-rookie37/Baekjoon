quantity = lambda x: x // 5
reamin = lambda x, y: x - quantity(x) * y
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def spread(R, C):
    global room

    temp = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if room[r][c] > 0:
                d = 0
                for k in range(4):
                    dr = r + dx[k]
                    dc = c + dy[k]
                    if 0 <= dr < R and 0 <= dc < C:
                        if dc == 0 and (dr == pf[0] or dr == pf[1]):
                            continue

                        temp[dr][dc] += quantity(room[r][c])
                        d += 1

                temp[r][c] += reamin(room[r][c], d)

    room = temp
    room[pf[0]][0] = room[pf[1]][0] = -1


def purify(R, C):
    global room

    # in
    for r in range(pf[0] - 1, 0, -1):
        room[r][0] = room[r - 1][0]
    for r in range(pf[0] + 1, R - 1):
        room[r][0] = room[r + 1][0]

    # left
    room[0] = room[0][1:] + [0]
    room[-1] = room[-1][1:] + [0]

    # wall
    for r in range(0, pf[0]):
        room[r][-1] = room[r + 1][-1]
    for r in range(R - 1, pf[1], -1):
        room[r][-1] = room[r - 1][-1]
    # out
    room[pf[0]] = [-1, 0] + room[pf[0]][1 : C - 1]
    room[pf[1]] = [-1, 0] + room[pf[1]][1 : C - 1]


def sol(R, C, T):
    for _ in range(T):
        spread(R, C)
        purify(R, C)

    print(sum(map(sum, room)) + 2)


if __name__ == "__main__":

    R, C, T = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(R)]
    pf = [r for r in range(R) if room[r][0] == -1]

    sol(R, C, T)
