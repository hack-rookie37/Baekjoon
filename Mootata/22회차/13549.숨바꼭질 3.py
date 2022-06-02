from collections import deque

n, k = map(int, input().split()) # 수빈이의 위치 N, 동생의 위치 K
visited = [False for _ in range(100001)]

def bfs():
    q = deque()
    q.append((n, 0))
    
    while q:
        x, t = q.popleft()
        
        if x != k:
            if x * 2 <= 100000 and not visited[x * 2]: 
                q.appendleft((x * 2, t))
                visited[x * 2] = True
                
            if x + 1 <= 100000 and not visited[x + 1]:
                q.append((x + 1, t + 1))
                visited[x + 1] = True
            
            if x - 1 >= 0 and not visited[x - 1]:
                q.append((x - 1, t + 1))
                visited[x - 1] = True
                
        else:
            return t

print(bfs())

# 순간이동은 0초가 걸리기 때문에 가장 먼저 나온 값이 가장 빠른 것은 아님
# 따라서 순간이동의 우선순위를 높이기 위해 큐의 맨 앞에 넣어줌