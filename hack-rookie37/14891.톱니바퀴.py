import sys
from collections import deque

input = sys.stdin.readline


def rotate(wn, d):
    if d > 0:
        wheels[wn].appendleft(wheels[wn].pop())
    else:
        wheels[wn].append(wheels[wn].popleft())


def set_joint():
    return tuple(False if wheels[i][2] == wheels[i + 1][6] else True for i in range(3))


wheels = [deque(input().strip()) for _ in range(4)]
K = int(input())


for _ in range(K):
    wn, d = map(int, input().split())
    joint = set_joint()
    rotate(wn - 1, d)

    if wn == 1:
        if joint[0]:
            rotate(1, d * (-1))
            if joint[1]:
                rotate(2, d)
                if joint[2]:
                    rotate(3, d * (-1))
    elif wn == 2:
        if joint[0]:
            rotate(0, d * (-1))
        if joint[1]:
            rotate(2, d * (-1))
            if joint[2]:
                rotate(3, d)
    elif wn == 3:
        if joint[2]:
            rotate(3, d * (-1))
        if joint[1]:
            rotate(1, d * (-1))
            if joint[0]:
                rotate(0, d)
    else:
        if joint[2]:
            rotate(2, d * (-1))
            if joint[1]:
                rotate(1, d)
                if joint[0]:
                    rotate(0, d * (-1))


print(sum(2 ** x for x in range(4) if wheels[x][0] == "1"))
