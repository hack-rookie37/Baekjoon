import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]

    for idx in range(1, n):
        stickers[0][idx] += stickers[1][idx - 1] if idx == 1 else max(stickers[1][idx - 1], stickers[1][idx - 2])
        stickers[1][idx] += stickers[0][idx - 1] if idx == 1 else max(stickers[0][idx - 1], stickers[0][idx - 2])

    print(max(stickers[0][n - 1], stickers[1][n - 1]))

loop_count = int(input())
for i in range(loop_count):
    solution()

# 50 40  200 130 250
# 30 100 110 210 260