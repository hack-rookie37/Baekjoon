import sys
from collections import defaultdict

input = sys.stdin.readline

def bellman_ford(start):
    dist[start] = 0
    
    for i in range(n):
        for j in range(1, n + 1):
            for next_node, time in world[j]:
                if dist[next_node] > dist[j] + time: # 시간이 더 적게 걸리면 갱신
                    dist[next_node] = dist[j] + time
                    if i == n - 1:
                        return 'YES'
    return 'NO'

for tc in range(int(input())):
    world = defaultdict(list)
    n, m, w = map(int, input().split()) # 지점의 수 N, 도로의 개수 M, 웜홀의 개수 W
    dist = [10001] * (n + 1) # 초기값이 float('inf') 같은 무한대라면, 이 값에 음수를 더해줘도 무한대기 때문에 값의 갱신이 일어나지 않음.
    
    for i in range(m):
        s, e, t = map(int, input().split()) # 연결된 지점의 번호 (s, e), 이동하는데 걸리는 시간 t
        world[s].append((e, t)) # s에서 e로 가는데 걸리는 시간 t
        world[e].append((s, t))
    for i in range(w):
        s, e, t = map(int, input().split())
        world[s].append((e, -t))
    
    print(bellman_ford(1))


# 음의 사이클이 존재한다는 뜻은 음의 사이클에 포함되는 정점에서는 시간이 줄어들면서
# 시작 위치로 돌아오는 것이 가능하다는 뜻이므로, 음의 사이클이 존재하는지만 판단하면 됨.
