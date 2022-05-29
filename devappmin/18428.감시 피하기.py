import sys
from itertools import combinations

dy, dx = (1, -1, 0, 0), (0, 0, 1, -1)

n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().split()) for _ in range(n)]
teachers = []
empty = []

for y in range(n):
    for x in range(n):
        if graph[y][x] == 'T':
            teachers.append((y, x))

        if graph[y][x] == 'X':
            empty.append((y, x))

def isHidable():
    for y, x in teachers:
        for idx in range(4):
            ny, nx = y + dy[idx], x + dx[idx]
            while 0 <= ny < n and 0 <= nx < n:
                if graph[ny][nx] == 'S':
                    return False

                if graph[ny][nx] == 'O':
                    break

                ny, nx = ny + dy[idx], nx + dx[idx]

    return True

answer = False

for places in combinations(empty, 3):
    for y, x in places:
        graph[y][x] = 'O'

    
    if isHidable():
        answer = True
        break

    for y, x in places:
        graph[y][x] = 'X'

print('YES' if answer else 'NO')
