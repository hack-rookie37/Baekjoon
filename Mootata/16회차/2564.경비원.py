import sys

input = sys.stdin.readline

block_x, block_y = map(int, input().split())
n = int(input()) # 상점의 수
stores = [tuple(map(int, input().split())) for _ in range(n + 1)]
block_size = (block_x + block_y) * 2
answer = 0

for i in range(len(stores)):
    if stores[i][0] == 1: # 북
        stores[i] = stores[i][1]
    elif stores[i][0] == 4: # 동
        stores[i] = block_x  + stores[i][1]
    elif stores[i][0] == 2: # 남
        stores[i] = (block_x * 2) + block_y - stores[i][1]
    else: # 서
        stores[i] = (block_x + block_y) * 2 - stores[i][1]

for i in range(len(stores)):
    if stores[-1] > stores[i]:
        answer += min(abs(stores[-1] - stores[i]), block_size - stores[-1] + stores[i])
    else:
        answer += min(abs(stores[-1] - stores[i]), block_size - stores[i] + stores[-1])

print(answer)


# 블록을 펼쳐서 직선이라고 생각하고 동근이에서 가게까지의 거리와
# 동근이와 가게 각각으로부터 가까운 끝점 까지의 거리의 합 중 더 작은 것을 고름.