from collections import deque

n, k = map(int, input().split()) # 수빈의 위치 N, 동생의 위치 K
visited = [-1 for _ in range(100001)] # 경로
route = []

def bfs():
    q = deque()
    q.append(n)
    
    while q:
        current = q.popleft()
        
        if current == k:
            return
        
        for next in (current - 1, current + 1, current * 2):
            if 0 <= next <= 100000 and visited[next] == -1:
                q.append(next)
                visited[next] = current

bfs()

while k != n:
    route.append(k)
    k = visited[k] # visited[k]에는 k 이전의 위치가 들어있음

route.append(k)

print(len(route) - 1) # 모든 이동 방법은 1초 소모
print(*reversed(route))