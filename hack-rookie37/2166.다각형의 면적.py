import sys

input = sys.stdin.readline

N = int(input())
cood = [tuple(map(int, input().split())) for _ in range(N)]
cood.append(cood[0])

answer = 0
for i in range(len(cood) - 1):
    answer += (cood[i][0] + cood[i + 1][0]) * (cood[i][1] - cood[i + 1][1])

print(abs(answer) / 2)
