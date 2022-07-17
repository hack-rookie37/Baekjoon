import sys

input = sys.stdin.readline

H, W = map(int, input().split())
(*b,) = map(int, input().split())

answer = [0] * W
top = b[0]
for i in range(1, W):
    if top >= b[i]:
        answer[i] = top - b[i]
    else:
        top = b[i]

top = b[-1]
for i in range(W - 2, 0, -1):
    if top >= b[i]:
        answer[i] = min(answer[i], top - b[i])
    else:
        answer[i] = 0
        top = b[i]

print(sum(answer[1:-1]))
