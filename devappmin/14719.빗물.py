import sys
from collections import defaultdict

h, w = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
blocks = list(map(int, sys.stdin.readline().split()))

for idx, height in enumerate(blocks):
    for h_block in range(height + 1):
        graph[h_block].append(idx)

answer = 0
for height, block in sorted(graph.items(), key=lambda a: -a[0]):
    if len(block) == 1:
        continue

    answer += block[-1] - block[0] - len(block) + 1

print(answer)