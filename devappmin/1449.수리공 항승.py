import sys

n, l = map(int, sys.stdin.readline().split())
positions = sorted(list(map(int, sys.stdin.readline().split())))
require, answer = 0, 0

for pos in positions:
    if pos > require:
        require = pos + l - 1
        answer += 1

print(answer)
