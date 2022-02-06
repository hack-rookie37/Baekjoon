from collections import deque

def bfs():
    queue = deque()
    queue.append((a, ''))
    visited[a] = True
    
    while queue:
        current_value, cmd = queue.popleft()
        if current_value == b:
            return cmd
        
        next_value = (2 * current_value) % 10000 # D
        if not visited[next_value]:
            queue.append([next_value, cmd + "D"])
            visited[next_value] = True
        
        next_value = (current_value - 1) % 10000 # S (-1 % 10000 = 9999임) 
        if not visited[next_value]:
            queue.append([next_value, cmd + "S"])
            visited[next_value] = True
            
        next_value = (current_value % 1000) * 10 + (current_value // 1000) # L
        if not visited[next_value]:
            queue.append([next_value, cmd + "L"])
            visited[next_value] = True
            
        next_value =  (current_value - (current_value // 10) * 10) * 1000 + (current_value // 10) # R
        if not visited[next_value]:
            queue.append([next_value, cmd + "R"])
            visited[next_value] = True

for t in range(int(input())):
    a, b = map(int, input().split())
    visited = [False] * 10000
    print(bfs())