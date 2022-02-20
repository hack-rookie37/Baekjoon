# 1. 임의의 정점으로 부터 가장 먼 정점을 구한다.
# 2. 1에서 나온 정점으로 부터 가장 먼 정점을 구한다.
# 3. 1과 2에서 나온 정점간의 거리가 트리의 지름!
# 이 말은 즉슨,
# 1. 트리에서 임의의 정점 x를 잡는다.
# 2. 정점 x에서 가장 먼 정점 y를 찾는다.
# 3. 정점 y에서 가장 먼 정점 z를 찾는다.

import sys

n = int(sys.stdin.readline())
matrix = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(1, n + 1):
    input_list = list(map(int, sys.stdin.readline().split()))
    
    for idx in range(1, len(input_list) - 1, 2):
        matrix[input_list[0]].append((input_list[idx], input_list[idx + 1]))


av, aa = 1, 0

def dfs(v, a):
    global av, aa

    visited[v] = True

    for i in matrix[v]:
        # if not matrix[v][i]:
        #     continue
        if not visited[i[0]]:
            a += i[1]
            dfs(i[0], a)
            a -= i[1]
    
    visited[v] = False
    if a > aa:
        av = v
        aa = a

dfs(1, 0)
visited = [False] * (n + 1)
aa = 0
dfs(av, 0)
print(aa)