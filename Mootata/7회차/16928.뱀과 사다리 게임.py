from collections import deque

n, m = map(int, input().split()) # 사다리의 수 n, 뱀의 수 m

board = [0] + [i for i in range(1, 101)]
visited = [False] * 101
dice = [1, 2, 3, 4, 5, 6]

for i in range(n):
    x, y = map(int, input().split())
    board[x] = y
    
for i in range(m):
    u, v = map(int, input().split())
    board[u] = v
    
def bfs():
    q = deque()
    q.append((1, 0))
    visited[1] = True
    
    while q:
        current_location, count = q.popleft()
        
        if current_location == 100:
            return count
        
        if current_location != board[current_location]:
            current_location = board[current_location]
        
        for i in range(6):
            next_location = current_location + dice[i]
            
            if next_location > 100:
                continue
            
            if not visited[next_location]:
                q.append((next_location, count + 1))
                visited[next_location] = True
                
print(bfs())