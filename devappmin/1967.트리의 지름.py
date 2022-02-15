import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())
matrix = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(n - 1):
    input_list = list(map(int, sys.stdin.readline().split()))
    matrix[input_list[0]].append((input_list[1], input_list[2]))
    matrix[input_list[1]].append((input_list[0], input_list[2]))

av, aa = 1, 0

def dfs(v, a):
    global av, aa

    visited[v] = True

    for vt in matrix[v]:
        if not visited[vt[0]]:
            a += vt[1]
            dfs(vt[0], a)
            a -= vt[1]
        
    visited[v] = False
    if a > aa:
        av = v
        aa = a

dfs(1, 0)
aa = 0
visited = [False] * (n + 1)
dfs(av, 0)
print(aa)