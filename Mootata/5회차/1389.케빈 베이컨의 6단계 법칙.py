from collections import deque

n, m = map(int, input().split()) # 유저의 수 n, 친구 관계의 수 m

friends = [[]for _ in range(n + 1)]
answer = [float('inf')] * (n + 1)

for i in range(0, m):
    u1, u2 = map(int, input().split())
    friends[u1].append(u2)
    friends[u2].append(u1)
    
def bfs(k):
    queue = deque()
    queue.append(k)
    visited[k] = True
    count = [0 for _ in range(n + 1)]
    
    while queue:
        v = queue.popleft()
        
        for i in friends[v]:
            if not visited[i]:
                count[i] = count[v] + 1
                queue.append(i)
                visited[i] = True
            
    return sum(count)
        
for i in range(1, n + 1):
    visited = [False for _ in range(n + 1)]
    answer[i] = bfs(i)
    
print(answer.index(min(answer)))